"""State completion status for the Program & Degree Deep Dive (docs/PROGRAM_DEPTH_COMPLETION.md).

Computed only from committed files, so CI can check it:
  * the national registry (pipeline/registry/<STATE>.json): the state's in-scope four-year institutions;
  * IPEDS 2023-24 admissions (data/national/ipeds/2023-24/<STATE>/admissions.csv): entering first-year students per
    institution, the weight used for the coverage threshold;
  * promoted program-depth records in data/institutions/<folder>/ (academic_programs, degree_requirements,
    program_catalogs, awards);
  * the exceptions queue (programs/queue/<STATE>.json): every gap the pipeline could not close, with its reason and
    next action.

    python -m programs status [--states TN OR] [--check]

writes docs/coverage/programs/STATUS.json and STATUS.md (all states that have a queue file or promoted program data).
"""
from __future__ import annotations
import csv, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The completion rule (docs/PROGRAM_DEPTH_COMPLETION.md). Changing a number here is a product decision.
COVERAGE_SHARE = 0.80        # covered institutions must enrol >= 80% of the state's entering first-year students at four-year schools
CATALOG_SHARE = 0.90         # an institution is covered when >= 90% of its official bachelor's list has verified records
PLAN_SHARE = 0.50            # degree maps: plans for >= 50% of verified programs, or a queue entry saying why not
HIGH_VALUE = {
    'engineering': re.compile(r'\bengineering\b(?!\s+technology)', re.I),
    'computer_science': re.compile(r'\bcomputer\s+science\b|\bsoftware\s+engineering\b', re.I),
    'nursing': re.compile(r'\bnursing\b|\bB\.?S\.?N\b', re.I),
    'business': re.compile(r'\bbusiness\b|\baccounting\b|\bfinance\b|\bB\.?B\.?A\b', re.I),
}
GAPS = {'catalog', 'catalog_count', 'degree_maps', 'requirement_groups', 'admission_rules', 'institution'}
REASONS = {
    'bot_challenge',            # catalog answers with a bot challenge (recorded, never evaded)
    'robots_disallowed',        # robots.txt disallows the catalog
    'fetch_failed',             # the official host could not be fetched (TLS certificate chain, DNS, server error), diagnosed
    'no_year_label',            # official pages print no academic year
    'year_inconsistent',        # the source prints conflicting years or totals
    'layout_not_readable',      # the official layout cannot yet be read exactly (held, not guessed)
    'not_published',            # the institution does not publish this item on an official page we can reach
    'no_official_statement',    # pages for the program were read and state no admission/switch rule
    'state_inventory_only',     # only the year-unlabelled state inventory covers the programs (partially verified)
    'not_yet_researched',       # queued for a run
    'out_of_scope',             # e.g. no bachelor's programs for entering students
}


def registry(state):
    p = ROOT / 'pipeline/registry' / f'{state}.json'
    return json.loads(p.read_text()) if p.exists() else None


def entering(state):
    p = ROOT / 'data/national/ipeds/2023-24' / state / 'admissions.csv'
    out = {}
    if p.exists():
        with p.open(encoding='utf-8', newline='') as fh:
            for r in csv.DictReader(fh):
                try: out[r['institution_key']] = int(r['enrolled'] or 0)
                except ValueError: out[r['institution_key']] = 0
    return out


def records(folder, domain):
    """Records of the institution's latest academic-year file for a domain (one catalog year is measured at a time)."""
    d = ROOT / 'data/institutions' / folder / domain
    files = sorted(d.glob('[0-9][0-9][0-9][0-9]-[0-9][0-9].json')) if d.is_dir() else []
    if not files: return []
    w = json.loads(files[-1].read_text())
    return [{**{k: w[k] for k in ('institution_key', 'academic_year') if k in w}, **r} for r in w.get('records', [])]


def queue(state):
    p = ROOT / 'programs/queue' / f'{state}.json'
    return json.loads(p.read_text()) if p.exists() else {'state': state, 'entries': []}


def queue_errors(q, keys):
    errs = []
    for i, e in enumerate(q.get('entries', [])):
        where = f"queue {q.get('state')} entry {i}"
        if e.get('institution_key') not in keys: errs.append(f'{where}: institution_key not in the state registry')
        if e.get('gap') not in GAPS: errs.append(f'{where}: gap must be one of {sorted(GAPS)}')
        if e.get('reason') not in REASONS: errs.append(f'{where}: reason must be one of {sorted(REASONS)}')
        if not (e.get('next_action') or '').strip(): errs.append(f'{where}: next_action is required')
        if e.get('reason') not in ('not_yet_researched',) and not (e.get('evidence_url') or e.get('detail')):
            errs.append(f'{where}: evidence_url or detail is required')
    return errs


def institution_status(inst, q_entries):
    folder = inst['folder']
    progs = records(folder, 'academic_programs')
    verified = [r for r in progs if r.get('verification_status') == 'verified' and r.get('credential_level') == 'bachelor']
    partial = [r for r in progs if r.get('verification_status') == 'partially_verified']
    cats = [c for c in records(folder, 'program_catalogs') if c.get('verification_status') in ('verified', 'partially_verified')]
    reqs = records(folder, 'degree_requirements')
    plans = {r['program_key'] for r in reqs if r.get('requirement_kind') == 'program_plan' and r.get('verification_status') == 'verified'}
    groups = [r for r in reqs if r.get('requirement_kind') == 'major' and r.get('verification_status') == 'verified']
    gaps = {e['gap'] for e in q_entries}
    # A mechanical count (autoreview 'Standing review') can undercount (UT Austin: 113 linked entries, 262 listed), so it
    # is provisional: only a reviewed count (pilot review or catalog-count review) can make the catalog dimension met.
    reviewed = [c for c in cats if 'Standing review' not in (c.get('notes') or '')]
    listed = max([c.get('listed_bachelor_programs') or 0 for c in reviewed] + [0])
    complete = any(c.get('programs_complete') is True for c in reviewed)
    # verified records that are on the official list (the reviewer's or autoreview's match) when recorded; records for
    # options or programs off the list must not inflate the share
    matched = [c['verified_listed_programs'] for c in reviewed if c.get('verified_listed_programs') is not None]
    counted = min(len(verified), max(matched)) if matched else len(verified)
    share = (counted / listed) if listed else None
    covered = complete or (share is not None and share >= CATALOG_SHARE)  # both need a catalog record
    vkeys = {r['program_key'] for r in verified}
    hv = {f: [r for r in verified if rx.search(r.get('program_name', ''))] for f, rx in HIGH_VALUE.items()}
    hv_missing = sorted(f for f, rs in hv.items() if rs and not any(r.get('admission_type') for r in rs))
    dims = {
        'catalog': 'met' if covered else ('queued' if gaps & {'catalog', 'catalog_count', 'institution'} else 'open'),
        'degree_maps': 'met' if verified and len(plans & vkeys) >= PLAN_SHARE * len(verified) else ('queued' if 'degree_maps' in gaps or 'institution' in gaps else 'open'),
        'requirement_groups': 'met' if groups else ('queued' if 'requirement_groups' in gaps or 'institution' in gaps else 'open'),
        'admission_rules': 'met' if verified and not hv_missing else ('queued' if 'admission_rules' in gaps or 'institution' in gaps else 'open'),
    }
    if covered: status = 'covered' if all(v != 'open' for v in dims.values()) else 'covered_open_items'
    elif verified or partial: status = 'partial' if not any(v == 'open' for v in dims.values()) else 'partial_unqueued'
    else: status = 'exception' if gaps else 'not_started'
    years = sorted({r.get('academic_year') for r in progs + cats + reqs if r.get('academic_year')})
    return {'institution_key': inst['institution_key'], 'name': inst['name'], 'folder': folder, 'status': status, 'academic_years': years,
            'verified_bachelor_programs': len(verified), 'partially_verified_programs': len(partial), 'listed_bachelor_programs': listed or None,
            'programs_complete': complete, 'catalog_share': round(share, 3) if share is not None else None, 'programs_with_plan': len(plans & vkeys),
            'requirement_groups': len(groups), 'high_value_without_admission_rule': hv_missing, 'dimensions': dims,
            'queue': sorted({f"{e['gap']}:{e['reason']}" for e in q_entries})}


def state_status(state):
    reg = registry(state)
    if not reg: return None
    four = [i for i in reg['institutions'] if i.get('level') == 'four_year']
    weights = entering(state)
    q = queue(state)
    by_inst = {}
    for e in q.get('entries', []): by_inst.setdefault(e['institution_key'], []).append(e)
    rows = [institution_status(i, by_inst.get(i['institution_key'], [])) for i in four]
    total = sum(weights.get(r['institution_key'], 0) for r in rows) or 1
    covered = [r for r in rows if r['status'] in ('covered', 'covered_open_items')]
    share = sum(weights.get(r['institution_key'], 0) for r in covered) / total
    unaccounted = [r['name'] for r in rows if r['status'] in ('not_started', 'partial_unqueued', 'covered_open_items')]
    errors = queue_errors(q, {i['institution_key'] for i in reg['institutions']})
    pending = sorted({e['institution_key'] for e in q.get('entries', []) if e.get('reason') == 'not_yet_researched'})
    complete = not unaccounted and not pending and not errors and share >= COVERAGE_SHARE
    started = any(r['status'] != 'not_started' for r in rows)
    return {'state': state, 'status': 'complete' if complete else ('in_progress' if started else 'not_started'),
            'four_year_institutions': len(rows), 'covered_institutions': len(covered),
            'entering_student_share_covered': round(share, 3), 'coverage_threshold': COVERAGE_SHARE,
            'unaccounted_institutions': unaccounted, 'not_yet_researched': len(pending), 'queue_entries': len(q.get('entries', [])), 'queue_errors': errors,
            'institutions': sorted(rows, key=lambda r: -weights.get(r['institution_key'], 0))}


def states_with_work():
    """States the deep dive has worked: a queue file, or a promoted program_catalogs record (only this workstream
    writes catalogs; the national crawler's occasional academic_programs records alone do not start a state)."""
    s = {p.stem for p in (ROOT / 'programs/queue').glob('*.json') if '.' not in p.stem}  # not <STATE>.proposed.json drafts
    folders = {f.parts[-3] for f in (ROOT / 'data/institutions').glob('*/program_catalogs/*.json')}
    if folders:
        for p in sorted((ROOT / 'pipeline/registry').glob('*.json')):
            if any(i.get('folder') in folders for i in json.loads(p.read_text()).get('institutions', [])): s.add(p.stem)
    return sorted(s)


def markdown(all_states, nat=None):
    L = ['# Program & Degree Deep Dive: state completion status', '',
         'Generated by `python -m programs status` from committed records, the national registry, IPEDS entering-student counts and '
         '`programs/queue/<STATE>.json`. The rule is in `docs/PROGRAM_DEPTH_COMPLETION.md`.', '']
    if nat:
        L += ['## National (50 states and D.C.)', '',
              f"**{nat['registered']} four-year schools registered, {nat['researched']} researched, {nat['covered']} meeting deep-dive coverage**; "
              f"{nat['states_tracked']} of {len(nat['states'])} jurisdictions tracked.", '', nat['definition'], '',
              '| State | Registered | Researched | Covered | Tracked |', '|---|---|---|---|---|']
        L += [f"| {r['state']} | {r['registered']} | {r['researched']} | {r['covered']} | {'yes' if r['tracked'] else 'no'} |" for r in nat['states']]
        L += ['', '## Tracked states', '']
    L += [
         f"**{sum(s['status'] == 'complete' for s in all_states)} complete, {sum(s['status'] == 'in_progress' for s in all_states)} in progress.**", '',
         '| State | Status | Four-year schools | Covered | Entering students covered | Unaccounted schools | Not yet researched | Queue entries |', '|---|---|---|---|---|---|---|---|']
    for s in all_states:
        L.append(f"| {s['state']} | **{s['status']}** | {s['four_year_institutions']} | {s['covered_institutions']} | {s['entering_student_share_covered']:.0%} "
                 f"(needs {s['coverage_threshold']:.0%}) | {len(s['unaccounted_institutions'])} | {s['not_yet_researched']} | {s['queue_entries']} |")
    for s in all_states:
        L += ['', f"## {s['state']}", '', '| School | Status | Verified bachelor\'s | Listed | Plans | Req. groups | Catalog | Maps | Groups | Admission rules | Queue |',
              '|---|---|---|---|---|---|---|---|---|---|---|']
        for r in s['institutions']:
            d = r['dimensions']
            L.append(f"| {r['name']} | {r['status']} | {r['verified_bachelor_programs']} | {r['listed_bachelor_programs'] or '–'} | {r['programs_with_plan']} | "
                     f"{r['requirement_groups']} | {d['catalog']} | {d['degree_maps']} | {d['requirement_groups']} | {d['admission_rules']} | {', '.join(r['queue']) or '–'} |")
        if s['queue_errors']: L += ['', '**Queue errors:** ' + '; '.join(s['queue_errors'])]
    return '\n'.join(L) + '\n'


RESEARCHED = ('covered', 'covered_open_items', 'partial', 'partial_unqueued')
NATIONAL_DEFINITION = ('Registered: four-year schools in the national registry (pipeline/registry; scope rule in pipeline/registry.py). '
                       'Researched: a verified or partially verified deep-dive record, or a queue entry recording an attempt other than '
                       'not_yet_researched. Covered: meets docs/PROGRAM_DEPTH_COMPLETION.md. Untracked states count as registered only.')


def national(out):
    """Registered / researched / covered four-year schools across every registry state (50 states and D.C.), kept apart.
    registered: four-year schools in the national registry (pipeline/registry, scope rule in pipeline/registry.py);
    researched: a verified or partially verified deep-dive record, or a queue entry recording an attempt (anything but
    not_yet_researched); covered: meets docs/PROGRAM_DEPTH_COMPLETION.md. Untracked states count as registered only."""
    tracked = {s['state']: s for s in out}
    rows = []
    for p in sorted((ROOT / 'pipeline/registry').glob('*.json')):
        if not re.fullmatch(r'[A-Z]{2}', p.stem) or p.stem == 'ZZ': continue
        reg = json.loads(p.read_text())
        four = [i for i in reg['institutions'] if i.get('level') == 'four_year']
        s = tracked.get(p.stem)
        if s:
            researched = sum(1 for r in s['institutions'] if r['status'] in RESEARCHED or (r['status'] == 'exception' and any(
                not q.endswith(':not_yet_researched') for q in r['queue'])))
            covered = s['covered_institutions']
        else: researched = covered = 0
        rows.append({'state': p.stem, 'registered': len(four), 'researched': researched, 'covered': covered, 'tracked': bool(s)})
    return {'definition': NATIONAL_DEFINITION,
            'registered': sum(r['registered'] for r in rows), 'researched': sum(r['researched'] for r in rows),
            'covered': sum(r['covered'] for r in rows), 'states_tracked': sum(r['tracked'] for r in rows), 'states': rows}


def main(states=None, check=False):
    OUT = ROOT / 'docs/coverage/programs'
    states = states or states_with_work()
    out = [s for s in (state_status(st) for st in states) if s]
    j = json.dumps({'rule': 'docs/PROGRAM_DEPTH_COMPLETION.md', 'thresholds': {'coverage_share': COVERAGE_SHARE, 'catalog_share': CATALOG_SHARE,
                    'plan_share': PLAN_SHARE}, 'national': national(out), 'states': out}, indent=1, sort_keys=True) + '\n'
    errors = [e for s in out for e in s['queue_errors']]
    if check:
        cur = (OUT / 'STATUS.json').read_text() if (OUT / 'STATUS.json').exists() else ''
        if errors: print('\n'.join(errors)); return 1
        if cur != j: print('docs/coverage/programs/STATUS.json is stale: run python -m programs status'); return 1
        print(f'Program-depth status current ({len(out)} states)'); return 0
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'STATUS.json').write_text(j); (OUT / 'STATUS.md').write_text(markdown(out, json.loads(j)['national']))
    for s in out: print(f"{s['state']}: {s['status']} — {s['covered_institutions']}/{s['four_year_institutions']} covered, "
                        f"{s['entering_student_share_covered']:.0%} of entering students, {len(s['unaccounted_institutions'])} unaccounted, {s['queue_entries']} queued")
    return 1 if errors else 0
