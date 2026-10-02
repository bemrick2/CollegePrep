"""Apply reviewed decisions: write approved candidates and re-verification upgrades into data/.

Decisions live in `pipeline/decisions/<STATE>.json` and are reviewed in the PR like data:

  {"run": "pipeline/runs/TN/2026-10-02",
   "approve": [{"candidate_id": "...", "reason": "values match the cited rows"}],
   "reject":  [{"candidate_id": "...", "reason": "table is graduate tuition"}],
   "upgrade": [{"natural_key": "...", "reason": "all values found verbatim in the year-labeled source"}]}

Status rule (never raised by a decision): a reviewed candidate from a year-labeled source with no
open issues becomes `verified`; an unlabeled source, or one with issues the reviewer accepted,
becomes `partially_verified`. A record never replaces a verified one with weaker or older
evidence. Evidence (snippets, source hashes, fetch times) is archived next to the run's other
official-source manifests so every promoted value stays traceable.
"""
from __future__ import annotations
import json
from datetime import date
from pathlib import Path

from backend.catalog import ROOT
from backend.store import natural_key
from .review import existing_records

RANK = {'verified': 3, 'partially_verified': 2, 'unverified': 1, 'stale': 0, 'not_applicable': 0}


INFORMATIONAL = ('stale_year_label',)  # a correctly labelled prior year is history, not a defect


def blocking(issues):
    return [i for i in issues if not i.startswith(INFORMATIONAL)]


def status_for(c, accepted_issues: bool):
    if c['year_basis'] in {'labeled_in_title', 'labeled_in_heading', 'labeled_in_source'} and not blocking(c['issues']):
        return 'verified'
    return 'partially_verified' if (not blocking(c['issues']) or accepted_issues) else None


def _file_for(folder, domain, year):
    return ROOT / 'data/institutions' / folder / domain / f'{year}.json'


def _upsert(path: Path, inst_key, year, record, domain):
    payload = json.loads(path.read_text()) if path.exists() else {'institution_key': inst_key, 'academic_year': year, 'records': []}
    key = natural_key(domain, record)
    recs = payload['records']
    for i, old in enumerate(recs):
        merged_old = {'institution_key': payload['institution_key'], 'academic_year': payload['academic_year'], **old}
        if natural_key(domain, merged_old) == key:
            if old.get('verification_status') == 'verified' and (
                    RANK.get(record['verification_status'], 0) < 3 or str(old.get('last_verified_at', '')) > record['last_verified_at']):
                raise ValueError(f'{path}: refusing to replace verified {key} with weaker or older evidence')
            recs[i] = {k: v for k, v in record.items() if k not in {'institution_key', 'academic_year'}}
            break
    else:
        recs.append({k: v for k, v in record.items() if k not in {'institution_key', 'academic_year'}})
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def promote(registry, decisions_path: Path, log=print):
    decisions = json.loads(decisions_path.read_text())
    run_dir = ROOT / decisions['run']
    cands = {c['candidate_id']: c for c in json.loads((run_dir / 'candidates.json').read_text())}
    verify = {v['natural_key']: v for v in json.loads((run_dir / 'verify.json').read_text())}
    folders = {i['institution_key']: i['folder'] for i in registry['institutions']}
    evidence = {}
    written = 0
    for d in decisions.get('approve', []):
        c = cands.get(d['candidate_id']) or (_ for _ in ()).throw(KeyError(f"unknown candidate {d['candidate_id']}"))
        if c.get('diff', {}).get('status') == 'same':
            log(f"skip {c['candidate_id']}: identical to existing record"); continue
        status = status_for(c, accepted_issues=bool(d.get('accept_issues')))
        if status is None:
            raise ValueError(f"{c['candidate_id']} has open issues {c['issues']}; set accept_issues with a reason to promote it as partially_verified")
        rec = dict(c['record'])
        rec['verification_status'] = status
        rec['notes'] = (rec.get('notes', '') + f" Reviewed {date.today().isoformat()}: {d.get('reason', '').strip()} "
                        f"Evidence: sources/pipeline/{registry['state']}/{Path(decisions['run']).name}/evidence.json#{c['candidate_id']}.").strip()
        _upsert(_file_for(folders[c['institution_key']], c['domain'], c['academic_year']), c['institution_key'], c['academic_year'], rec, c['domain'])
        evidence[c['candidate_id']] = {'source': c['source'], 'extractor': c['extractor'], 'year_basis': c['year_basis'],
                                       'issues': c['issues'], 'evidence': c['evidence'], 'decision': d}
        written += 1
    for d in decisions.get('upgrade', []):
        v = verify.get(d['natural_key'])
        if not v or v.get('result') != 'all_values_found_year_labeled':
            raise ValueError(f"upgrade {d['natural_key']} is not supported by verify.json")
        path = ROOT / v['path']
        payload = json.loads(path.read_text())
        for r in payload['records']:
            if natural_key(v['domain'], {**{k: payload[k] for k in ('institution_key', 'academic_year', 'state') if k in payload}, **r}) == v['natural_key']:
                r['verification_status'] = 'verified'
                r['last_verified_at'] = v['fetched_at'][:10]
                r['notes'] = (r.get('notes', '') + f" Re-verified {v['fetched_at'][:10]}: every recorded value was found verbatim in "
                              f"the year-labeled source (sha256 {v['source_sha256'][:16]}). {d.get('reason', '')}").strip()
                break
        else:
            raise ValueError(f"record {d['natural_key']} not found in {path}")
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        evidence['upgrade:' + d['natural_key']] = {'verify': v, 'decision': d}
        written += 1
    out = ROOT / 'sources/pipeline' / registry['state'] / Path(decisions['run']).name / 'evidence.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    prior = json.loads(out.read_text()) if out.exists() else {}
    out.write_text(json.dumps({**prior, **evidence}, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8')
    from .registry import write as write_registry
    write_registry(registry['state'])  # promoted records cite new sources, which every later run re-checks
    log(f'promoted {written} records; evidence in {out.relative_to(ROOT)}; registry refreshed')
    return written
