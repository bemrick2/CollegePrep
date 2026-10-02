"""Turn a crawl into candidates, re-verification results, an exception queue and coverage.

Outputs in the run directory (all deterministic for a given crawl and repository state):
  candidates.json   every extracted candidate with evidence, checks, issues and diff status
  verify.json       existing curated records re-checked value by value against raw source text
  review.md         the compact queue a reviewer reads: ready items, exceptions, upgrades, leads
  coverage.json     institution x category status, plus state and category rollups
"""
from __future__ import annotations
import json, re
from collections import Counter, defaultdict
from datetime import date

from backend.catalog import ROOT, records
from backend.store import natural_key
from . import text as T, topics
from .crawl import Run
from .extractors import cds, costs, credit, merit

EXTRACTORS = [credit.extract, costs.extract, cds.extract, merit.extract]
SCALAR_SKIP = {'entering_fall_year', 'unitid', 'term_index', 'choose_count'}
# Policy wording that must also appear verbatim before a record can be upgraded: paraphrased text
# (for example from a summarising fetch tool) is exactly what the earlier status downgrade was for.
TEXT_POLICY_FIELDS = {'eligibility_summary', 'gpa_requirement', 'test_requirement', 'renewal_requirements', 'award_amount_text',
                      'summary', 'process_summary', 'rule_text', 'min_grade', 'required_documents', 'deadline_text',
                      'residency_requirement'}
STATUS_ORDER = ['verified_current', 'partially_verified_current', 'candidate_ready', 'candidate_exception',
                'source_found', 'not_found', 'fetch_failed']
CATEGORY_KINDS = {'ap_credit': 'AP', 'clep_credit': 'CLEP', 'ib_credit': 'IB', 'dual_enrollment': 'dual_enrollment'}


def existing_records(keys):
    out = defaultdict(list)
    for path, domain, r in records():
        if r.get('institution_key') in keys:
            out[r['institution_key']].append((path, domain, r))
    return out


def extract_run(registry, run: Run, today_year):
    insts = {i['institution_key']: i for i in registry['institutions']}
    out = []
    for e in run.entries():
        inst = insts.get(e.get('institution_key'))
        if not inst or not e.get('page_file'): continue
        page, _ = run.load_page(e['page_file'])
        for fn in EXTRACTORS:
            try:
                out += fn(inst, e, page, today_year)
            except Exception as exc:  # An extractor bug must not hide other results; it is queued instead.
                out.append({'candidate_id': f'error-{fn.__module__}-{e["page_file"]}', 'domain': None,
                            'institution_key': inst['institution_key'], 'issues': [f'extractor_error:{type(exc).__name__}: {exc}'],
                            'source': {'url': e['url']}, 'extractor': fn.__module__, 'evidence': [], 'record': {}})
    return dedupe(out)


def dedupe(cands):
    """Same candidate id from several fetches of one document -> keep one; different documents yielding
    the same natural key with different values -> both flagged as conflicting."""
    by_id = {}
    for c in cands:
        by_id.setdefault(c['candidate_id'], c)
    by_key = defaultdict(list)
    for c in by_id.values():
        if c.get('domain'):
            by_key[natural_key(c['domain'], c['record'])].append(c)
    for key, group in by_key.items():
        if len(group) < 2: continue
        payloads = {json.dumps(_comparable(g['record']), sort_keys=True) for g in group}
        if len(payloads) > 1:
            for g in group:
                g['issues'].append('conflicting_sources:' + ','.join(sorted(x['source']['url'] for x in group if x is not g)))
    # Distinct ids for one natural key (e.g. two extractors) would collide on import; keep the richest.
    keep = {}
    for key, group in by_key.items():
        keep[key] = max(group, key=lambda g: (len(g['evidence']), g['candidate_id']))
        for g in group:
            if g is not keep[key] and not any(i.startswith('conflicting_sources') for i in g['issues']):
                g['superseded_by'] = keep[key]['candidate_id']
    return [c for c in by_id.values() if not c.get('superseded_by')]


def _comparable(r):
    return {k: v for k, v in r.items() if k not in {'source_url', 'policy_url', 'last_verified_at', 'notes',
                                                    'verification_status', 'academic_year_basis'}}


def diff(cands, existing):
    for c in cands:
        if not c.get('domain'): continue
        key = natural_key(c['domain'], c['record'])
        match = next((r for _, d, r in existing.get(c['institution_key'], []) if d == c['domain'] and natural_key(d, r) == key), None)
        if match is None:
            c['diff'] = {'status': 'new'}; continue
        changes = compare(c['domain'], match, c['record'])
        c['diff'] = {'status': 'changed' if changes else 'same', 'existing_status': match.get('verification_status'),
                     'changes': changes}
        if changes and match.get('verification_status') == 'verified':
            c['issues'].append('conflicts_with_verified_record')
    return cands


EQUIVALENT = {'cost_period': [{'academic_year', 'fall_and_spring_semesters'}]}


def equivalent(field, a, b):
    """Same meaning in two vocabularies, or a less specific candidate value ('undergraduate' vs
    'full_time_undergraduate') — not a change worth an exception."""
    if any({a, b} <= group for group in EQUIVALENT.get(field, [])): return True
    return field == 'student_population' and isinstance(a, str) and isinstance(b, str) and (a.endswith(b) or b.endswith(a))


def compare(domain, old, new):
    changes = []
    for k, v in new.items():
        if k in {'source_url', 'policy_url', 'last_verified_at', 'notes', 'verification_status', 'academic_year_basis',
                 'equivalencies', 'components', 'living_arrangements'}: continue
        if v is not None and old.get(k) is not None and old.get(k) != v and not equivalent(k, old.get(k), v):
            changes.append({'field': k, 'existing': old.get(k), 'candidate': v})
    if domain == 'credit_policies':
        def keyed(eqs):
            return {(re.sub(r'[^a-z0-9]', '', (e.get('exam_or_course_name') or '').lower().replace('ap', '', 1)),
                     str(e.get('minimum_score') or '').strip()): (e.get('institution_course_equivalent') or '').strip()
                    for e in eqs or []}
        o, n = keyed(old.get('equivalencies')), keyed(new.get('equivalencies'))
        for k in sorted(set(o) & set(n)):
            if T.normalize_for_search(o[k]) != T.normalize_for_search(n[k]):
                changes.append({'field': f'equivalency {k[0]} score {k[1]}', 'existing': o[k], 'candidate': n[k]})
        if len(n) != len(o):
            changes.append({'field': 'equivalency_count', 'existing': len(o), 'candidate': len(n)})
    return changes


# ------------------------------------------------------------------ re-verification of curated records
def _values(r, prefix=''):
    """(field, value) pairs worth checking verbatim: numbers and short course strings."""
    for k, v in r.items():
        if k in SCALAR_SKIP or k.endswith('_url') or k in {'notes', 'last_verified_at', 'academic_year', 'summary'}: continue
        name = f'{prefix}{k}'
        if isinstance(v, bool) or v is None: continue
        if isinstance(v, (int, float)): yield name, v
        elif isinstance(v, dict): yield from _values(v, name + '.')
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    sub = {kk: vv for kk, vv in item.items() if kk in {'minimum_score', 'institution_course_equivalent', 'credits_awarded',
                                                                       'total_cost_of_attendance', 'housing', 'food', 'amount', 'code',
                                                                       'credit_hours', 'any_of', 'items', 'courses'}}
                    yield from _values(sub, f'{name}[{i}].')
                elif isinstance(item, str) and re.fullmatch(r'[A-Z]{2,5}\s?\d{3,4}[A-Z]?', item.strip()):
                    yield f'{name}[{i}]', item


def _texts(r, prefix=''):
    for k, v in r.items():
        if k in TEXT_POLICY_FIELDS: yield prefix + k, v
        elif isinstance(v, dict): yield from _texts(v, prefix + k + '.')


def found_in(text_norm, value):
    if isinstance(value, (int, float)):
        v = int(value) if float(value).is_integer() else value
        return re.search(rf'(?<![\d.]){re.escape(str(v))}(?![\d])', text_norm) is not None
    s = T.normalize_for_search(str(value)).strip()
    return bool(s) and s in text_norm


def verify_existing(registry, run: Run, existing):
    by_url = defaultdict(list)
    for e in run.entries():
        if e.get('page_file'):
            for u in {e['url'], e.get('final_url')}:
                if u: by_url[u].append(e)
    results = []
    for inst in registry['institutions']:
        for path, domain, r in existing.get(inst['institution_key'], []):
            if path.suffix != '.json' or r.get('verification_status') == 'verified': continue
            hits = by_url.get(r.get('source_url'), [])
            entry = {'path': str(path.relative_to(ROOT)), 'domain': domain, 'natural_key': natural_key(domain, r),
                     'source_url': r.get('source_url'), 'status': r.get('verification_status')}
            if not hits:
                entry['result'] = 'source_not_fetched'; results.append(entry); continue
            page, _ = run.load_page(hits[-1]['page_file'])
            norm = T.normalize_for_search(page.text + '\n' + '\n'.join(' | '.join(row) for t in page.tables for row in t['rows']))
            vals = list(_values(r))
            missing = [f for f, v in vals if not found_in(norm, v)]
            texts = [(k, v) for k, v in _texts(r) if isinstance(v, str) and v.strip()]
            paraphrased = [k for k, v in texts if not found_in(norm, v)]
            label, basis = T.dominant_year(page.text[:60000], page.title)
            entry.update({'checked': len(vals), 'missing': missing[:40], 'missing_count': len(missing),
                          'source_sha256': hits[-1].get('sha256'), 'fetched_at': hits[-1].get('fetched_at'),
                          'source_year_label': label, 'year_basis': basis})
            entry['texts_checked'] = len(texts); entry['texts_not_verbatim'] = paraphrased[:20]
            if not vals: entry['result'] = 'nothing_to_check'
            elif missing: entry['result'] = 'values_not_found_verbatim'
            elif paraphrased: entry['result'] = 'policy_text_not_verbatim'
            elif label == r.get('academic_year'): entry['result'] = 'all_values_found_year_labeled'
            else: entry['result'] = 'all_values_found_year_not_labeled'
            results.append(entry)
    return results


# ------------------------------------------------------------------ coverage
def coverage(registry, run: Run, cands, existing, today_year):
    pages = defaultdict(lambda: defaultdict(list)); failed = Counter(); fetched = Counter()
    for e in run.entries():
        k = e.get('institution_key'); fetched[k] += 1
        if not e.get('page_file'): failed[k] += 1; continue
        page, _ = run.load_page(e['page_file'])  # recomputed so topic fixes apply to archived runs
        for t in topics.page_topics(page.title, page.headings, page.text): pages[k][t].append(e['url'])
    rows = []
    for inst in registry['institutions']:
        k = inst['institution_key']
        row = {'institution_key': k, 'name': inst['name'], 'pages_fetched': fetched[k], 'fetch_failures': failed[k], 'categories': {}}
        for cat, domain in topics.CATEGORY_DOMAINS.items():
            have = [r for _, d, r in existing.get(k, []) if d == domain and r.get('academic_year') == today_year
                    and (cat not in CATEGORY_KINDS or r.get('policy_kind') == CATEGORY_KINDS[cat])]
            mine = [c for c in cands if c.get('institution_key') == k and c.get('domain') == domain
                    and (cat not in CATEGORY_KINDS or c['record'].get('policy_kind') == CATEGORY_KINDS[cat])]
            if any(r.get('verification_status') == 'verified' for r in have): status = 'verified_current'
            elif have: status = 'partially_verified_current'
            elif any(not c['issues'] and c['academic_year'] == today_year for c in mine): status = 'candidate_ready'
            elif mine: status = 'candidate_exception'
            elif pages[k].get(cat): status = 'source_found'
            elif fetched[k] == 0 or failed[k] == fetched[k]: status = 'fetch_failed'
            else: status = 'not_found'
            row['categories'][cat] = status
        rows.append(row)
    by_cat = {cat: Counter(r['categories'][cat] for r in rows) for cat in topics.CATEGORY_DOMAINS}
    totals = Counter(s for r in rows for s in r['categories'].values())
    state_key = f"state-{registry['state']}"
    state = {'pages_fetched': fetched[state_key], 'fetch_failures': failed[state_key],
             'categories': {cat: len(set(pages[state_key].get(cat, []))) for cat in topics.CATEGORY_DOMAINS}}
    blocked = sorted(r['institution_key'] for r in rows if r['pages_fetched'] and r['fetch_failures'] == r['pages_fetched'])
    return {'state': registry['state'], 'academic_year': today_year, 'institutions': len(rows),
            'status_order': STATUS_ORDER, 'by_category': {c: dict(v) for c, v in by_cat.items()},
            'totals': dict(totals), 'statewide_sources': state, 'blocked_institutions': blocked, 'rows': rows}


# ------------------------------------------------------------------ queue
def write_queue(run: Run, registry, cands, verify, cov):
    exc = [c for c in cands if c['issues']]
    ready = [c for c in cands if not c['issues']]
    upgrades = [v for v in verify if v.get('result') == 'all_values_found_year_labeled']
    names = {i['institution_key']: i['name'] for i in registry['institutions']}
    L = [f"# Review queue — {registry['state']} ({cov['academic_year']})", '',
         f"Pages fetched: {sum(r['pages_fetched'] for r in cov['rows'])}; failures: {sum(r['fetch_failures'] for r in cov['rows'])}. "
         f"Candidates: {len(cands)} ({len(ready)} without issues, {len(exc)} exceptions). "
         f"Re-verification upgrades proposed: {len(upgrades)}.", '',
         '## Coverage by category', '', '| category | ' + ' | '.join(STATUS_ORDER) + ' |', '|---' * (len(STATUS_ORDER) + 1) + '|']
    for cat, counts in cov['by_category'].items():
        L.append(f'| {cat} | ' + ' | '.join(str(counts.get(s, 0)) for s in STATUS_ORDER) + ' |')
    def block(title, items):
        L.extend(['', f'## {title} ({len(items)})', ''])
        for c in sorted(items, key=lambda c: (names.get(c['institution_key'], ''), c.get('domain') or '', c['candidate_id'])):
            d = c.get('diff', {})
            L.append(f"### `{c['candidate_id']}` {names.get(c['institution_key'], c['institution_key'])} — {c.get('domain')} "
                     f"{c.get('academic_year', '')} [{d.get('status', '?')}] ({c.get('year_basis', '')})")
            L.append(f"- source: {c['source']['url']}" + (f" (sha256 {c['source'].get('sha256', '')[:12]})" if c['source'].get('sha256') else ''))
            if c['issues']: L.append('- issues: ' + ', '.join(c['issues']))
            if c.get('checks'): L.append('- checks: ' + json.dumps(c['checks'], sort_keys=True))
            for ch in d.get('changes', [])[:12]:
                L.append(f"- change {ch['field']}: `{ch['existing']}` → `{ch['candidate']}`")
            for ev in c['evidence'][:25]:
                L.append(f"  - {ev['field']}: {ev.get('value', '')} ⟵ “{ev['snippet']}”")
            if len(c['evidence']) > 25: L.append(f"  - … {len(c['evidence']) - 25} more rows")
    block('Ready for review', ready)
    block('Exceptions', exc)
    L.extend(['', f'## Re-verification of existing records ({len(verify)})', ''])
    for v in verify:
        L.append(f"- {v['result']}: {v['path']} {v['natural_key']}" + (f" missing={v['missing'][:8]}" if v.get('missing') else '')
                 + (f" year={v.get('source_year_label')}" if v.get('source_year_label') else ''))
    st = cov.get('statewide_sources', {})
    L.extend(['', '## Statewide sources', '', f"Pages fetched: {st.get('pages_fetched', 0)}; pages by category: "
              + ', '.join(f'{k} {v}' for k, v in sorted(st.get('categories', {}).items()) if v)])
    if cov.get('blocked_institutions'):
        L.extend(['', '## Blocked by the site (every request refused; needs the browser fallback)', ''])
        L.extend(f"- {names.get(k, k)} (`{k}`)" for k in cov['blocked_institutions'])
    L.extend(['', '## Leads: official pages found with no extracted record', ''])
    for r in cov['rows']:
        found = [c for c, s in r['categories'].items() if s == 'source_found']
        if found: L.append(f"- {r['name']}: {', '.join(found)}")
    (run.dir / 'review.md').write_text('\n'.join(L) + '\n', encoding='utf-8')


def review(registry, run: Run, today=None):
    today_year = T.current_academic_year(today or date.today())
    keys = {i['institution_key'] for i in registry['institutions']}
    existing = existing_records(keys)
    cands = diff(extract_run(registry, run, today_year), existing)
    verify = verify_existing(registry, run, existing)
    cov = coverage(registry, run, cands, existing, today_year)
    for name, obj in [('candidates.json', cands), ('verify.json', verify), ('coverage.json', cov)]:
        (run.dir / name).write_text(json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False, default=str) + '\n', encoding='utf-8')
    write_queue(run, registry, cands, verify, cov)
    return cands, verify, cov
