"""Apply reviewed program-depth decisions to data/ (python -m programs promote <decisions.json>).

Decisions live in programs/decisions/<STATE>-<run>.json and are reviewed in the PR like data:

  {"run": "programs/runs/OR/2026-10-05-b", "run_branch": "program-run/or-2026-10-05", "reviewer": "...",
   "approve":   [{"candidate_id": "...", "reason": "...", "accept_issues": "why the open issues are acceptable"}],
   "approve_programs": [{"institution_key": "...", "program_key": "...", "reason": "...", "accept_issues": "..."}],
   "fields":    [{"institution_key": "...", "program_key": "...", "field": "admission_type", "value": "direct",
                  "evidence_ids": ["..."], "criteria_text": "...", "gpa_min": 3.0, "paths": [...], "reason": "..."}],
   "catalogs":  [{"institution_key": "...", "catalog_url": "...", "catalog_year_label": "2026-2027",
                  "source_evidence": {"url": "...", "sha256": "..."}, "listed_bachelor_programs": 111,
                  "programs_complete": false, "completeness_basis": "...", "listed_program_keys": [...],
                  "undeclared": {"allowed": true, "evidence_ids": ["..."], "declare_by_text": "..."}, "reason": "..."}],
   "reject":    [{"candidate_id": "...", "reason": "..."}]}

Rules (shared with pipeline/promote.py, imported unchanged): a candidate from a year-labeled source with no
blocking issue becomes `verified`; accepted issues give `partially_verified`; a verified record is never
replaced by weaker or older evidence. A field decision copies the cited sentences verbatim into the record's
evidence object; the value itself is the reviewer's reading of those sentences and the decision states why.
A CR-14 field is only written onto a program that is approved in the same decision file or already on file.
Evidence (candidate snippets, sentences, document hashes, fetch times) is archived in
sources/programs/<STATE>/<run>/evidence.json so the run branch need not be merged.
"""
from __future__ import annotations
import json
from datetime import date
from pathlib import Path

from backend.catalog import ROOT
from backend.store import natural_key
from pipeline.promote import status_for, _upsert, _file_for
from .extract import THEC_PAGE
from .match import split_catalog_name

FIELDS = ('admission_type', 'internal_transfer')


def load_run(run_dir: Path):
    cands = {}
    for line in (run_dir / 'candidates.jsonl').read_text().splitlines():
        c = json.loads(line); cands[c['candidate_id']] = c
    ev = {}
    for line in (run_dir / 'evidence.jsonl').read_text().splitlines():
        e = json.loads(line); ev.setdefault(e['evidence_id'], e)
    return cands, ev


def _records(folder, domain, year):
    p = _file_for(folder, domain, year)
    return json.loads(p.read_text()) if p.exists() else None


def check_folder_ownership(folders):
    """A data folder belongs to one institution across every committed state registry (pipeline/registry/*.json). A
    target folder that another registry also gives to a different institution must not receive records (unless this
    institution's records are already there): the national
    registry decides folder names, and its disambiguation runs when a state's registry is regenerated."""
    owners = {}
    for p in sorted((ROOT / 'pipeline/registry').glob('*.json')):
        for i in json.loads(p.read_text()).get('institutions', []):
            owners.setdefault(i['folder'], set()).add(i['institution_key'])
    def holder(f):  # the institution whose records are already in the folder, if any
        for q in (ROOT / 'data/institutions' / f).glob('*/*.json'):
            k = json.loads(q.read_text()).get('institution_key')
            if k: return k
        return None
    clash = {k: f for k, f in folders.items() if owners.get(f, {k}) - {k} and holder(f) != k}
    if clash:
        raise ValueError(f'target folders owned by other institutions in a committed registry: {clash}; '
                         'regenerate the targets from the current registries')


def promote(decisions_path: Path, log=print):
    d = json.loads(Path(decisions_path).read_text())
    run_dir = ROOT / d['run']
    state = Path(d['run']).parts[-2]
    targets = json.loads((ROOT / 'programs/targets' / f'{state}.json').read_text())
    folders = {t['institution_key']: t['folder'] for t in targets['institutions']}
    check_folder_ownership(folders)
    cands, ev = load_run(run_dir)
    from pipeline.crawl import Run
    RUN_CTX['run'] = Run(run_dir)
    archive, written = {}, 0
    approvals = list(d.get('approve', []))
    for ap in d.get('approve_programs', []):
        hit = [c for c in cands.values() if c['institution_key'] == ap['institution_key'] and c['record'].get('program_key') == ap['program_key']]
        if not any(c['domain'] == 'academic_programs' for c in hit):
            raise ValueError(f"approve_programs: no program candidate {ap['institution_key']}/{ap['program_key']}")
        rejected = {r['candidate_id'] for r in d.get('reject', [])}
        approvals += [{'candidate_id': c['candidate_id'], 'reason': ap['reason'], **({'accept_issues': ap['accept_issues']} if ap.get('accept_issues') else {})}
                      for c in sorted(hit, key=lambda c: c['domain'] != 'academic_programs') if c['candidate_id'] not in rejected]
    approvals.sort(key=lambda a: cands[a['candidate_id']]['domain'] != 'academic_programs')  # programs before their requirements
    # A program already on file from the same program URL keeps its key (as pipeline/review.py does for curated rows),
    # and so do its requirement rows: no second record for one program.
    keymap = {}
    for a in approvals:
        c = cands[a['candidate_id']]
        if c['domain'] != 'academic_programs': continue
        old = _records(folders[c['institution_key']], 'academic_programs', c['academic_year'])
        cand_name = split_catalog_name(c['record'].get('program_name', ''))
        for r in (old or {}).get('records', []):
            same_url = r.get('program_url') == c['record'].get('program_url')
            # A state-inventory record (THEC) for the same major and award becomes this catalog record: one program, the
            # catalog's stronger evidence, the inventory's CIP kept (exact name + award match only, programs.match).
            same_inventory_program = (r.get('program_url') == THEC_PAGE and c['record'].get('program_url') != THEC_PAGE
                                      and cand_name is not None and split_catalog_name(r.get('program_name', '')) == cand_name)
            if (same_url or same_inventory_program) and r['program_key'] != c['record']['program_key']:
                keymap[(c['institution_key'], c['academic_year'], c['record']['program_key'])] = r['program_key']
    for a in approvals:
        c = cands.get(a['candidate_id'])
        if c is None: raise KeyError(f"unknown candidate {a['candidate_id']}")
        status = status_for(c, accepted_issues=bool(a.get('accept_issues')))
        if status is None:
            raise ValueError(f"{c['candidate_id']} has open issues {c['issues']}; accept_issues with a reason is required")
        rec = dict(c['record']); rec['verification_status'] = status
        mapped = keymap.get((c['institution_key'], c['academic_year'], rec.get('program_key')))
        if mapped: rec['program_key'] = mapped
        note = f" Reviewed {date.today().isoformat()}: {a.get('reason', '').strip()}"
        if a.get('accept_issues'): note += f" Accepted issues {c['issues']}: {a['accept_issues']}"
        rec['notes'] = (rec.get('notes', '') + note + f" Evidence: sources/programs/{state}/{run_dir.name}/evidence.json#{c['candidate_id']}.").strip()
        if c['domain'] == 'degree_requirements':
            on_file = _records(folders[c['institution_key']], 'academic_programs', c['academic_year']) or {'records': []}
            if not any(r.get('program_key') == rec['program_key'] for r in on_file['records']):
                raise ValueError(f"{c['candidate_id']}: requirement for program {rec['program_key']!r} that is not on file")
        if c['domain'] == 'academic_programs':  # keep CR-14 fields already reviewed onto this program
            old = _records(folders[c['institution_key']], 'academic_programs', c['academic_year'])
            for r in (old or {}).get('records', []):
                if r.get('program_key') == rec['program_key']:
                    for f in FIELDS + ('admission_details', 'cip_code', 'cip_source_url'):
                        if f in r and f not in rec: rec[f] = r[f]
        _upsert(_file_for(folders[c['institution_key']], c['domain'], c['academic_year']), c['institution_key'], c['academic_year'], rec, c['domain'])
        archive[c['candidate_id']] = {'source': c['source'], 'extractor': c['extractor'], 'year_basis': c['year_basis'],
                                      'issues': c['issues'], 'evidence': c['evidence'], 'decision': a}
        written += 1
    for f in d.get('fields', []):
        written += apply_field(f, folders, ev, archive)
    for mg in d.get('merge', []):
        written += apply_merge(mg, folders, archive)
    for aw in d.get('awards', []):
        written += apply_award(aw, folders, archive)
    for cat in d.get('catalogs', []):
        written += apply_catalog(cat, folders, ev, archive)
    out = ROOT / 'sources/programs' / state / run_dir.name / 'evidence.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    prior = json.loads(out.read_text()) if out.exists() else {}
    out.write_text(json.dumps({**prior, **archive}, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8')
    log(f'promoted {written} records/fields; evidence in {out.relative_to(ROOT)}')
    return written


def _quote(ids, ev):
    sents = [ev[i] for i in ids]
    if not sents: raise ValueError('a field decision needs evidence_ids')
    urls = {s['url'] for s in sents}
    if len(urls) != 1: raise ValueError(f'evidence for one field must come from one document: {urls}')
    # Sentences are verbatim but may be far apart on the page: an ellipsis marks every join.
    return ' … '.join(s['sentence'] for s in sents), sents[0]


RUN_CTX = {}


def page_quote(pq, run):
    """pq: {'url': ..., 'lines': [...]}: the newest stored document fetched from url; every line must be one of its
    printed lines (whitespace-normalised). Joined with ' … ' because lines may be apart on the page."""
    import re
    norm = lambda x: re.sub(r'\s+', ' ', x).strip()
    if pq.get('run'):  # a page stored in another run of the same state
        from pipeline.crawl import Run
        run = Run(ROOT / pq['run'])
    hits = [e for e in run.entries() if pq['url'] in (e.get('url'), e.get('final_url')) and e.get('page_file')]
    if not hits: raise ValueError(f"page_quote: {pq['url']} not stored in the run")
    e = hits[-1]
    page, _ = run.load_page(e['page_file'])
    printed = {norm(l) for l in page.lines}
    missing = [l for l in pq['lines'] if norm(l) not in printed]
    if missing: raise ValueError(f"page_quote: not printed on {pq['url']}: {missing}")
    return ' … '.join(norm(l) for l in pq['lines']), {'url': e.get('final_url') or e['url'], 'sha256': e['sha256'], 'fetched_at': e['fetched_at']}


def apply_field(f, folders, ev, archive):
    year = f.get('academic_year', '2026-27')
    path = _file_for(folders[f['institution_key']], 'academic_programs', year)
    payload = json.loads(path.read_text())
    rec = next((r for r in payload['records'] if r['program_key'] == f['program_key']), None)
    if rec is None: raise ValueError(f"field for {f['program_key']!r}: program not on file")
    if f.get('page_quote'):  # lines copied from a stored page; each must occur in it verbatim
        quote, src = page_quote(f['page_quote'], RUN_CTX['run'])
    elif f.get('source_doc'):  # a structured official record (e.g. THEC inventory row), quoted as printed
        sd = f['source_doc']
        quote, src = sd['excerpt'], {'url': sd['url'], 'sha256': sd['sha256'], 'fetched_at': sd['fetched_at']}
    else:
        quote, src = _quote(f['evidence_ids'], ev)
    detail = {'quote': quote, 'source_url': src['url'], 'source_sha256': src['sha256'], 'retrieved_at': src['fetched_at'][:10]}
    for k in ('criteria_text', 'gpa_min', 'paths', 'notes'):
        if f.get(k) is not None: detail[k] = f[k]
    if f['field'] == 'admission_type':
        rec['admission_type'] = f['value']; rec['admission_details'] = detail
    elif f['field'] == 'internal_transfer':
        rec['internal_transfer'] = {'restricted': f['value'], **detail}
    elif f['field'] == 'cip_code':
        rec['cip_code'] = f['value']; rec['cip_source_url'] = src['url']
        rec['notes'] = (rec.get('notes', '') + f" CIP {f['value']} from {src['url']} (document sha256 {src['sha256'][:16]}): {quote}").strip()
    else:
        raise ValueError(f"unknown field {f['field']}")
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    archive[f"field:{f['institution_key']}:{f['program_key']}:{f['field']}"] = {'decision': f, 'sentences': [ev[i] for i in f.get('evidence_ids', [])]}
    return 1


def apply_merge(mg, folders, archive):
    """Reviewer-confirmed: an unpromoted-to-live state-inventory record (THEC) and a catalog record are one program whose
    printed names differ ('EARTH AND ENVIRONMENTAL SCIENCES, BS' / 'Earth and Environmental Science (B.S.)'). The
    inventory's CIP moves to the catalog record (quoted), and the inventory record is removed. Only inventory records
    may be dropped, and only before they are imported (the decision must say so)."""
    year = mg.get('academic_year', '2026-27')
    path = _file_for(folders[mg['institution_key']], 'academic_programs', year)
    payload = json.loads(path.read_text())
    recs = {r['program_key']: r for r in payload['records']}
    keep, drop = recs.get(mg['keep']), recs.get(mg['drop'])
    if not keep or not drop: raise ValueError(f"merge {mg}: record missing")
    if drop.get('program_url') != THEC_PAGE or keep.get('program_url') == THEC_PAGE:
        raise ValueError(f"merge {mg}: only a state-inventory record can be folded into a catalog record")
    if not mg.get('not_yet_imported'): raise ValueError('merge requires not_yet_imported: true (deletions do not propagate to the live database)')
    if drop.get('cip_code') and not keep.get('cip_code'):
        keep['cip_code'] = drop['cip_code']; keep['cip_source_url'] = drop['cip_source_url']
        keep['notes'] = (keep.get('notes', '') + f" CIP {drop['cip_code']} from the THEC inventory record '{drop['program_name']}', "
                         f"matched by reviewer: {mg['reason']}").strip()
    payload['records'] = [r for r in payload['records'] if r['program_key'] != mg['drop']]
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    archive[f"merge:{mg['institution_key']}:{mg['drop']}->{mg['keep']}"] = {'decision': mg, 'dropped': drop}
    return 1


def apply_award(aw, folders, archive):
    """A major-specific scholarship the institution itself ties to a field: the award fields the reviewer read from the
    page, the tie quoted verbatim (major_requirement) and checked against the stored page, and structured links to the
    programs on file. An award page without a printed academic year is partially verified."""
    year = aw.get('academic_year', '2026-27')
    quote, src = page_quote(aw['page_quote'], RUN_CTX['run'])
    progs = _records(folders[aw['institution_key']], 'academic_programs', year) or {'records': []}
    have = {r['program_key'] for r in progs['records']}
    missing = [k for k in aw.get('program_keys', []) if k not in have]
    if missing: raise ValueError(f"award {aw['award']['award_name']!r}: programs not on file {missing}")
    rec = {**aw['award'], 'institution_key': aw['institution_key'], 'academic_year': year, 'source_url': src['url'],
           'major_requirement': quote, 'verification_status': 'verified' if aw.get('year_labeled') else 'partially_verified',
           'last_verified_at': src['fetched_at'][:10]}
    if not aw.get('year_labeled'): rec['academic_year_basis'] = 'aid_year_in_force_at_review_source_unlabeled'
    if aw.get('program_keys'): rec['program_keys'] = aw['program_keys']
    rec['notes'] = (rec.get('notes', '') + f" Reviewed {date.today().isoformat()}: {aw.get('reason', '')} Source document sha256 {src['sha256'][:16]}.").strip()
    _upsert(_file_for(folders[aw['institution_key']], 'awards', year), aw['institution_key'], year, rec, 'awards')
    archive[f"award:{aw['institution_key']}:{aw['award']['award_name']}"] = {'decision': aw, 'source': src}
    return 1


def apply_catalog(cat, folders, ev, archive):
    year = cat.get('academic_year', '2026-27')
    old = _records(folders[cat['institution_key']], 'program_catalogs', year)
    if str(cat.get('reason', '')).startswith('Standing review') and any(
            'Catalog-count review' in (r.get('notes') or '') or 'Standing review' not in (r.get('notes') or '') for r in (old or {}).get('records', [])):
        return 0  # a mechanical count never replaces a reviewed one
    status = cat.get('verification_status', 'verified')
    if status not in ('verified', 'partially_verified'): raise ValueError('catalog status must be verified or partially_verified')
    rec = {'institution_key': cat['institution_key'], 'academic_year': year, 'catalog_url': cat['catalog_url'],
           'source_url': cat['source_evidence']['url'], 'verification_status': status,
           'last_verified_at': cat['source_evidence']['fetched_at'][:10]}
    for k in ('catalog_year_label', 'listed_bachelor_programs', 'verified_listed_programs', 'programs_complete', 'completeness_basis', 'listed_program_keys'):
        if cat.get(k) is not None: rec[k] = cat[k]
    if cat.get('undeclared'):
        u = cat['undeclared']
        quote, src = page_quote(u['page_quote'], RUN_CTX['run']) if u.get('page_quote') else _quote(u['evidence_ids'], ev)
        rec['undeclared_policy'] = {'allowed': u['allowed'], 'quote': quote, 'source_url': src['url'], 'source_sha256': src['sha256'],
                                    **({'declare_by_text': u['declare_by_text']} if u.get('declare_by_text') else {})}
    rec['notes'] = (f"Reviewed {date.today().isoformat()}: {cat.get('reason', '')} List document sha256 "
                    f"{cat['source_evidence'].get('sha256', '')[:16]}.").strip()
    _upsert(_file_for(folders[cat['institution_key']], 'program_catalogs', year), cat['institution_key'], year, rec, 'program_catalogs')
    archive[f"catalog:{cat['institution_key']}:{year}"] = {'decision': cat, 'sentences': [ev[i] for i in ((cat.get('undeclared') or {}).get('evidence_ids') or [])]}
    return 1
