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


def promote(decisions_path: Path, log=print):
    d = json.loads(Path(decisions_path).read_text())
    run_dir = ROOT / d['run']
    state = Path(d['run']).parts[-2]
    targets = json.loads((ROOT / 'programs/targets' / f'{state}.json').read_text())
    folders = {t['institution_key']: t['folder'] for t in targets['institutions']}
    cands, ev = load_run(run_dir)
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
    for a in approvals:
        c = cands.get(a['candidate_id'])
        if c is None: raise KeyError(f"unknown candidate {a['candidate_id']}")
        status = status_for(c, accepted_issues=bool(a.get('accept_issues')))
        if status is None:
            raise ValueError(f"{c['candidate_id']} has open issues {c['issues']}; accept_issues with a reason is required")
        rec = dict(c['record']); rec['verification_status'] = status
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
    return ' '.join(s['sentence'] for s in sents), sents[0]


def apply_field(f, folders, ev, archive):
    year = f.get('academic_year', '2026-27')
    path = _file_for(folders[f['institution_key']], 'academic_programs', year)
    payload = json.loads(path.read_text())
    rec = next((r for r in payload['records'] if r['program_key'] == f['program_key']), None)
    if rec is None: raise ValueError(f"field for {f['program_key']!r}: program not on file")
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
    else:
        raise ValueError(f"unknown field {f['field']}")
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    archive[f"field:{f['institution_key']}:{f['program_key']}:{f['field']}"] = {'decision': f, 'sentences': [ev[i] for i in f['evidence_ids']]}
    return 1


def apply_catalog(cat, folders, ev, archive):
    year = cat.get('academic_year', '2026-27')
    rec = {'institution_key': cat['institution_key'], 'academic_year': year, 'catalog_url': cat['catalog_url'],
           'source_url': cat['source_evidence']['url'], 'verification_status': 'verified',
           'last_verified_at': cat['source_evidence']['fetched_at'][:10]}
    for k in ('catalog_year_label', 'listed_bachelor_programs', 'programs_complete', 'completeness_basis', 'listed_program_keys'):
        if cat.get(k) is not None: rec[k] = cat[k]
    if cat.get('undeclared'):
        u = cat['undeclared']; quote, src = _quote(u['evidence_ids'], ev)
        rec['undeclared_policy'] = {'allowed': u['allowed'], 'quote': quote, 'source_url': src['url'], 'source_sha256': src['sha256'],
                                    **({'declare_by_text': u['declare_by_text']} if u.get('declare_by_text') else {})}
    rec['notes'] = (f"Reviewed {date.today().isoformat()}: {cat.get('reason', '')} List document sha256 "
                    f"{cat['source_evidence'].get('sha256', '')[:16]}.").strip()
    _upsert(_file_for(folders[cat['institution_key']], 'program_catalogs', year), cat['institution_key'], year, rec, 'program_catalogs')
    archive[f"catalog:{cat['institution_key']}:{year}"] = {'decision': cat, 'sentences': [ev[i] for i in (cat.get('undeclared') or {}).get('evidence_ids', [])]}
    return 1
