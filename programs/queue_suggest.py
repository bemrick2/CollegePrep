"""Draft exceptions-queue entries from run evidence (review input, never promoted as is).

    python -m programs queue-suggest --state TN [--runs programs/runs/TN/*]

For every in-scope four-year institution whose status (programs/status.py) has a gap that the committed queue does not
already account for, this looks at what the runs actually fetched and proposes one entry per open gap:

  * institution: no program records. The catalog host answered with bot challenges -> bot_challenge; robots.txt
    disallowed it -> robots_disallowed; nothing was fetched -> not_yet_researched.
  * catalog: only state-inventory records (partially verified) -> state_inventory_only; otherwise not_yet_researched.
  * degree_maps: program pages were read and none prints a plan marker -> not_published (with counts); otherwise
    not_yet_researched.
  * requirement_groups: requirement candidates exist but all carry review issues -> layout_not_readable; otherwise
    not_yet_researched.
  * admission_rules: pages of the high-value programs (and policy pages) were read and no admission-category sentence
    names them -> no_official_statement; otherwise not_yet_researched.

Output: programs/queue/<STATE>.proposed.json. A reviewer checks each entry against the cited run, edits the detail,
and moves accepted entries into programs/queue/<STATE>.json. The proposal is deliberately conservative: when the
runs cannot show why a gap is open, it says not_yet_researched.
"""
from __future__ import annotations
import glob, gzip, json, re
from collections import Counter, defaultdict
from pathlib import Path

from . import status as S

CHALLENGE = ('blocked_bot_challenge', 'host_challenge_stop', 'blocked_forbidden')
PLAN = re.compile(r'four[- ]year (plan|degree plan|curriculum|map)|degree map|sample (schedule|plan)|suggested (sequence|plan|schedule)|'
                  r'plan of study|\bfirst year\b.{0,40}\bfall\b|fall semester|\bsemester 1\b|year one', re.I | re.S)
ADMISSION_CATS = ('direct_admission', 'apply_to_major', 'pre_major', 'open_declaration')


def run_dirs(state, runs=None):
    return sorted(runs or glob.glob(str(S.ROOT / 'programs/runs' / state / '*')))


def fetch_summary(dirs):
    """institution_key -> {'errors': Counter, 'roles': Counter, 'program_pages': [(run, url, page_file)], 'hosts_challenged': Counter}"""
    out = defaultdict(lambda: {'errors': Counter(), 'roles': Counter(), 'program_pages': [], 'challenged': Counter(), 'robots': Counter(),
                               'unreachable': Counter(), 'ok_hosts': Counter()})
    for d in dirs:
        mf = Path(d) / 'manifest.jsonl'
        if not mf.exists(): continue
        for line in mf.read_text().splitlines():
            m = json.loads(line); k = m.get('institution_key'); x = out[k]
            x['roles'][m.get('role')] += 1
            err = m.get('error') or ''
            if err: x['errors'][err.split(':')[0][:40]] += 1
            host = re.sub(r'^https?://([^/]+).*', r'\1', m.get('url') or '')
            if err.startswith(CHALLENGE): x['challenged'][host] += 1
            if err.startswith('disallowed_by_robots'): x['robots'][host] += 1
            if err.startswith('robots_unreachable'): x['unreachable'][host] += 1
            if m.get('page_file'): x['ok_hosts'][host] += 1
            if m.get('role') == 'program_page' and m.get('page_file'): x['program_pages'].append((d, m['url'], m['page_file']))
    return out


def plan_pages(pages):
    n = hit = 0; seen = set()
    for d, url, pf in pages:
        if url in seen: continue
        seen.add(url); n += 1
        try: t = json.load(gzip.open(Path(d) / 'pages' / pf)).get('text', '')
        except (OSError, ValueError): continue
        if PLAN.search(t): hit += 1
    return n, hit


def requirement_candidates(dirs, key):
    c = Counter()
    for d in dirs:
        p = Path(d) / 'candidates.jsonl'
        if not p.exists(): continue
        for line in p.read_text().splitlines():
            x = json.loads(line)
            if x['institution_key'] == key and x['domain'] == 'degree_requirements' and x['record'].get('requirement_kind') == 'major':
                c['issues' if x['issues'] else 'clean'] += 1
    return c


def admission_evidence(dirs, key, urls):
    hits = []
    for d in dirs:
        p = Path(d) / 'evidence.jsonl'
        if not p.exists(): continue
        for line in p.read_text().splitlines():
            e = json.loads(line)
            if e['institution_key'] == key and e['category'] in ADMISSION_CATS and (e['url'] in urls or e['role'] == 'policy'):
                hits.append(e)
    return hits


def suggest(state, runs=None):
    st = S.state_status(state)
    if not st: raise SystemExit(f'no registry for {state}')
    dirs = run_dirs(state, runs)
    fs = fetch_summary(dirs)
    have = {(e['institution_key'], e['gap']) for e in S.queue(state).get('entries', [])}
    reg = {i['institution_key']: i for i in S.registry(state)['institutions']}
    runs_named = ', '.join(Path(d).name for d in dirs) or 'none'
    out = []

    def add(k, gap, reason, next_action, detail=None, url=None):
        if (k, gap) in have or (k, 'institution') in have: return
        e = {'institution_key': k, 'gap': gap, 'reason': reason, 'next_action': next_action}
        if detail: e['detail'] = detail
        if url: e['evidence_url'] = url
        e['_name'] = reg[k]['name']
        out.append(e)

    for r in st['institutions']:
        k = r['institution_key']; f = fs.get(k) or fs.default_factory()
        d = r['dimensions']
        if not r['verified_bachelor_programs']:  # nothing verified: one institution-level entry says why
            inv = f" {r['partially_verified_programs']} partially verified state-inventory records exist." if r['partially_verified_programs'] else ''
            if f['challenged'] and not f['program_pages'] and f['challenged'].most_common(1)[0][1] >= 3:
                host, n = f['challenged'].most_common(1)[0]
                add(k, 'institution', 'bot_challenge', 'Request catalog access or an official program export; the challenge is not evaded.',
                    f'{host} answered {n} requests with a bot challenge or block in runs {runs_named}; no program page was stored.{inv}', f'https://{host}/')
            elif r['partially_verified_programs']:
                add(k, 'institution', 'state_inventory_only', 'Obtain a readable current catalog to verify the inventory programs.',
                    f"Only state-inventory records (no academic-year label).{inv} Catalog fetch errors: {dict(f['errors'].most_common(3))}.")
            elif f['robots'] and not f['program_pages'] and not f['ok_hosts'][f['robots'].most_common(1)[0][0]]:
                host, n = f['robots'].most_common(1)[0]
                # Runs before 2026-10-06 recorded an unreachable robots.txt (no such host) as a refusal too.
                add(k, 'institution', 'not_yet_researched', f'Confirm with a diagnose run whether {host}/robots.txt disallows the catalog or the host does not exist; then locate the catalog.',
                    f'{n} requests to {host} were refused as disallowed_by_robots or robots-unreachable in runs {runs_named}.')
            else:
                why = 'discovery found no catalog' if f['roles'].get('discover') else 'not yet crawled'
                add(k, 'institution', 'not_yet_researched', f'Locate and configure the catalog ({why}).')
            continue
        if d['catalog'] == 'open':
            cat_host = [h for h, n in f['challenged'].items() if n >= 3 and re.match(r'(catalog|bulletin|catalogs)\.', h)]
            if cat_host:
                add(k, 'catalog', 'bot_challenge', 'Request catalog access or an official program export; the challenge is not evaded.',
                    f"{cat_host[0]} answered {f['challenged'][cat_host[0]]} requests with a bot challenge in runs {runs_named}; "
                    f"{r['verified_bachelor_programs']} programs are verified from other official pages.", f'https://{cat_host[0]}/')
            elif r['partially_verified_programs'] and not r['verified_bachelor_programs']:
                add(k, 'catalog', 'state_inventory_only', 'Obtain catalog access (the institution catalog was not readable) to verify the inventory programs.',
                    f"Only {r['partially_verified_programs']} partially verified state-inventory records (no academic-year label); "
                    f"catalog fetch errors: {dict(f['errors'].most_common(3))}.")
            else:
                add(k, 'catalog', 'not_yet_researched', 'Record the official listed bachelor\'s count and verify the remaining listed programs.',
                    f"{r['verified_bachelor_programs']} verified; listed count {r['listed_bachelor_programs'] or 'not yet recorded'}.")
        if d['degree_maps'] == 'open':
            n, hit = plan_pages(f['program_pages'])
            if n and hit == 0:
                add(k, 'degree_maps', 'not_published', 'Re-check at the next catalog release; look for departmental plans outside the catalog.',
                    f'{n} catalog program pages were read (runs {runs_named}); none prints a four-year plan marker.')
            else:
                add(k, 'degree_maps', 'not_yet_researched', 'Read the published plans (' + (f'{hit} of {n} program pages print a plan marker' if n else 'no program pages stored') + ').')
        if d['requirement_groups'] == 'open':
            c = requirement_candidates(dirs, k)
            if c and not c['clean']:
                add(k, 'requirement_groups', 'layout_not_readable', 'Improve the requirement reader for this layout and re-review.',
                    f"All {c['issues']} major-requirement candidates carry review issues (held).")
            else:
                add(k, 'requirement_groups', 'not_yet_researched',
                    'Review the clean requirement candidates' if c['clean'] else 'Capture requirement lists in a run', f'candidates: {dict(c)}' if c else None)
        if d['admission_rules'] == 'open' and r['high_value_without_admission_rule']:
            fams = ', '.join(r['high_value_without_admission_rule'])
            pages = {u for _, u, _ in f['program_pages']}
            ev = admission_evidence(dirs, k, pages)
            if f['program_pages'] and not ev:
                add(k, 'admission_rules', 'no_official_statement', 'Re-check department and admission pages at the next catalog release.',
                    f'High-value families without an admission rule: {fams}. {len(pages)} program pages and the policy pages in runs {runs_named} '
                    'print no admission-to-major sentence.')
            else:
                add(k, 'admission_rules', 'not_yet_researched', f'Review {len(ev)} admission-category sentences for: {fams}.' if ev else
                    f'Fetch department/admission pages for: {fams}.')
    return out


def main(state, runs=None):
    entries = suggest(state, runs)
    p = S.ROOT / 'programs/queue' / f'{state}.proposed.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({'state': state, 'note': 'Draft for review; see programs/queue_suggest.py. Not read by programs status.',
                             'entries': entries}, indent=1, ensure_ascii=False) + '\n')
    print(f'{state}: {len(entries)} proposed entries -> {p.relative_to(S.ROOT)} ' + str(dict(Counter(e["reason"] for e in entries))))
    return 0
