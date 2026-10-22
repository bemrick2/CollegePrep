"""Apply reviewed decisions: write approved candidates and re-verification upgrades into data/.

Decisions live in `pipeline/decisions/<STATE>-<run>.json` (one file per reviewed run) and are reviewed in the PR like data:

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
import json, re
from datetime import date
from pathlib import Path

from backend.catalog import ROOT
from backend.store import natural_key
from .review import existing_records

RANK = {'verified': 3, 'partially_verified': 2, 'unverified': 1, 'stale': 0, 'not_applicable': 0}


INFORMATIONAL = ('stale_year_label',)  # a correctly labelled prior year is history, not a defect


def blocking(issues):
    return [i for i in issues if not i.startswith(INFORMATIONAL)]


# A value the page did not print in that place can never be accepted by a reviewer: a merged cell inferred without the
# page's span markup, or a cell spanning several criteria columns whose label is unknown (#273 review).
NEVER_ACCEPTED = ('merged_cell_inferred', 'cell_spans_criteria_columns')


def status_for(c, accepted_issues: bool):
    if c['year_basis'] in {'labeled_in_title', 'labeled_in_heading', 'labeled_in_source'} and not blocking(c['issues']):
        return 'verified'
    if any(i.startswith(NEVER_ACCEPTED) for i in c['issues']): return None
    return 'partially_verified' if (not blocking(c['issues']) or accepted_issues) else None


def _file_for(folder, domain, year, state=None):
    if domain == 'state_policies':
        return ROOT / 'data/state_policies' / state / f'{year}.json'
    return ROOT / 'data/institutions' / folder / domain / f'{year}.json'


WRAPPER = ('institution_key', 'state', 'academic_year')


def _on_file(path: Path, record, domain):
    """The record on file under the same natural key, or None."""
    if not path.exists(): return None
    payload = json.loads(path.read_text())
    key = natural_key(domain, record)
    return next((old for old in payload['records'] if natural_key(domain, {**{k: payload[k] for k in WRAPPER if k in payload}, **old}) == key), None)


def _upsert(path: Path, inst_key, year, record, domain):
    """Write the record; returns the record it replaced (None when it was new)."""
    owner = {'state': record['state']} if domain == 'state_policies' else {'institution_key': inst_key}
    payload = json.loads(path.read_text()) if path.exists() else {**owner, 'academic_year': year, 'records': []}
    key = natural_key(domain, record)
    recs = payload['records']
    replaced = None
    for i, old in enumerate(recs):
        merged_old = {**{k: payload[k] for k in WRAPPER if k in payload}, **old}
        if natural_key(domain, merged_old) == key:
            if old.get('verification_status') == 'verified' and (
                    RANK.get(record['verification_status'], 0) < 3 or str(old.get('last_verified_at', '')) > record['last_verified_at']):
                raise ValueError(f'{path}: refusing to replace verified {key} with weaker or older evidence')
            recs[i] = {k: v for k, v in record.items() if k not in WRAPPER}
            replaced = old
            break
    else:
        recs.append({k: v for k, v in record.items() if k not in WRAPPER})
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return replaced


EVIDENCE_REF = re.compile(r'Evidence: (sources/pipeline/\S+?#\w+)\.')


def may_supersede(decision, old, record, verified_on_main=False):
    """A 'supersede' decision replaces only a record the pipeline promoted from the same document, and says why. A verified
    record already on main is replaced only with the owner's recorded approval (decision 'owner_approval')."""
    why = decision.get('supersede')
    if verified_on_main and not (isinstance(decision.get('owner_approval'), str) and decision['owner_approval'].strip()):
        return False
    return bool(isinstance(why, str) and why.strip() and old and old.get('source_url') == record.get('source_url')
                and EVIDENCE_REF.search(old.get('notes') or ''))


def verified_on_main(path: Path, record, domain):
    """True when origin/main holds this record (same natural key) as verified, or when that cannot be checked."""
    import subprocess
    try:
        rel = path.resolve().relative_to(ROOT.resolve())
        if subprocess.run(['git', 'rev-parse', '--verify', '-q', 'origin/main'], cwd=ROOT, capture_output=True).returncode != 0:
            return True  # main cannot be read: assume the record is protected
        out = subprocess.run(['git', 'show', f'origin/main:{rel.as_posix()}'], cwd=ROOT, capture_output=True, text=True)
    except (ValueError, OSError):
        return True
    if out.returncode != 0: return False  # the file is not on main: nothing verified there to protect
    payload = json.loads(out.stdout)
    key = natural_key(domain, record)
    return any(r.get('verification_status') == 'verified' and
               natural_key(domain, {**{k: payload[k] for k in WRAPPER if k in payload}, **r}) == key for r in payload.get('records', []))


def supersedes_note(old):
    """What a replaced record was, for the new record's notes (provenance is never silently overwritten)."""
    refs = EVIDENCE_REF.findall(old.get('notes') or '')
    return (f" Supersedes the {old.get('verification_status')} record last verified {old.get('last_verified_at')}"
            + (f" (evidence {refs[-1]})" if refs else '') + '.')


def merge_evidence(prior, new):
    """New entries win, but a replaced entry keeps the earlier version under 'superseded' (oldest first): a later decision on the
    same candidate id never erases the evidence and decision that an earlier record was promoted on."""
    out = dict(prior)
    for k, v in new.items():
        old = prior.get(k)
        if old is not None and {x: y for x, y in old.items() if x != 'superseded'} != {x: y for x, y in v.items() if x != 'superseded'}:
            v = {**v, 'superseded': old.get('superseded', []) + [{x: y for x, y in old.items() if x != 'superseded'}]}
        elif old is not None and old.get('superseded'):
            v = {**v, 'superseded': old['superseded']}
        out[k] = v
    return out


def promote(registry, decisions_path: Path, log=print):
    decisions = json.loads(decisions_path.read_text())
    run_dir = ROOT / decisions['run']
    cands = {c['candidate_id']: c for c in json.loads((run_dir / 'candidates.json').read_text())}
    verify = {v['natural_key']: v for v in json.loads((run_dir / 'verify.json').read_text())}
    folders = {i['institution_key']: i['folder'] for i in registry['institutions']}
    evidence = {}
    written = 0
    # A requirement row is promoted only with its program (approved now, or already on file): the importer
    # refuses orphans (VA r1: VSU Agriculture Education's program went to review, three of its rows did not).
    approved = [cands.get(d['candidate_id']) for d in decisions.get('approve', [])]
    have_program = {(c['institution_key'], c['academic_year'], c['record'].get('program_key')) for c in approved
                    if c and c['domain'] == 'academic_programs'}
    for f in (ROOT / 'data/institutions').glob('*/academic_programs/*.json'):
        j = json.loads(f.read_text())
        have_program |= {(j.get('institution_key'), j.get('academic_year'), r.get('program_key')) for r in j.get('records', [])}
    for d in decisions.get('approve', []):
        c = cands.get(d['candidate_id']) or (_ for _ in ()).throw(KeyError(f"unknown candidate {d['candidate_id']}"))
        if c['domain'] == 'degree_requirements' and (c['institution_key'], c['academic_year'], c['record'].get('program_key')) not in have_program:
            raise ValueError(f"{c['candidate_id']}: requirement row for program {c['record'].get('program_key')!r}, which is neither approved nor on file")
        target = _file_for(folders.get(c['institution_key']), c['domain'], c['academic_year'], c['record'].get('state'))
        old = _on_file(target, c['record'], c['domain'])
        if d.get('supersede'):
            # A reviewed re-read of the same document replaces a record the pipeline itself promoted from it (fields the earlier
            # reader missed). Anything else - another source, a hand-curated record - is not superseded by a decision.
            on_main = bool(old and old.get('verification_status') == 'verified' and verified_on_main(target, c['record'], c['domain']))
            if not may_supersede(d, old, c['record'], on_main):
                raise ValueError(f"{c['candidate_id']}: supersede needs a reason, a pipeline-promoted record from the same source on file, "
                                 "and owner_approval when that record is verified on main")
            c = {**c, 'issues': [i for i in c['issues'] if i != 'conflicts_with_verified_record']}
        elif c.get('diff', {}).get('status') == 'same':
            log(f"skip {c['candidate_id']}: identical to existing record"); continue
        status = status_for(c, accepted_issues=bool(d.get('accept_issues')))
        if status is None:
            raise ValueError(f"{c['candidate_id']} has open issues {c['issues']}; set accept_issues with a reason to promote it as partially_verified")
        rec = dict(c['record'])
        rec['verification_status'] = status
        rec['notes'] = (rec.get('notes', '') + f" Reviewed {date.today().isoformat()}: {d.get('reason', '').strip()} "
                        + (f"{d['supersede'].strip()} " if d.get('supersede') else '')
                        + f"Evidence: sources/pipeline/{registry['state']}/{Path(decisions['run']).name}/evidence.json#{c['candidate_id']}."
                        + (supersedes_note(old) if old else '')).strip()
        _upsert(target, c['institution_key'], c['academic_year'], rec, c['domain'])
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
    out.write_text(json.dumps(merge_evidence(prior, evidence), indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8')
    from .registry import write as write_registry
    write_registry(registry['state'])  # promoted records cite new sources, which every later run re-checks
    log(f'promoted {written} records; evidence in {out.relative_to(ROOT)}; registry refreshed')
    return written
