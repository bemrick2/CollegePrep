"""Program-depth coverage audit for the deep-dive states.

Joins three things per four-year institution:
  * persisted, reviewed data in data/institutions/<folder>/ (academic_programs, degree_requirements,
    program_catalogs, awards) -- the only things the product may show;
  * the newest program-depth run's outputs (programs/runs/<STATE>/<run>/) -- what official sources
    exist and what was retrieved, unreviewed;
  * the target configuration (catalog platform, priority).

Field coverage is by printed program name only (labelled as such): it says where to look, never that a
program is or is not offered. Writes docs/coverage/programs/<STATES>.json and .md; --check fails when
the committed audit is stale relative to the persisted data.
"""
from __future__ import annotations
import json, re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'docs/coverage/programs'
FIELDS = {
    'engineering': re.compile(r'\bengineering\b(?!\s+technology)|\bengineering\s+physics\b', re.I),
    'computer_science': re.compile(r'\bcomputer\s+science|\bcomputing\b|\bsoftware\s+engineering|\bdata\s+science', re.I),
    'business_finance': re.compile(r'\bbusiness|\bfinance\b|\baccounting\b|\bmanagement\b|\bmarketing\b|\beconomics\b', re.I),
    'nursing_health': re.compile(r'\bnursing\b|\bhealth\s+sciences?\b|\bpublic\s+health|\bkinesiology|\bexercise\s+science|\bpre-?health', re.I),
    'psychology': re.compile(r'\bpsycholog', re.I),
}
CIP_FIELD = {'engineering': ('14',), 'computer_science': ('11',), 'business_finance': ('52',), 'nursing_health': ('51',), 'psychology': ('42',)}
EVIDENCE_KEYS = ['direct_admission', 'apply_to_major', 'pre_major', 'progression', 'open_declaration', 'gpa_requirement', 'undeclared', 'declare_by',
                 'change_major', 'cip_code', 'major_scholarship', 'exam_credit_in_program']


def load_records(folder, domain):
    d = ROOT / 'data/institutions' / folder / domain
    out = []
    if d.is_dir():
        for f in sorted(d.glob('*.json')):
            w = json.loads(f.read_text())
            for r in w.get('records', [w]):
                out.append({**{k: w[k] for k in ('institution_key', 'academic_year') if k in w}, **r})
    return out


def latest_run(state):
    base = ROOT / 'programs/runs' / state
    runs = sorted(p for p in base.glob('*') if (p / 'summary.json').exists()) if base.exists() else []
    return runs[-1] if runs else None


def field_hits(names, cips=()):
    hits = {}
    for f, rx in FIELDS.items():
        n = [x for x in names if rx.search(x)]
        n += [c for c in cips if c and c.startswith(CIP_FIELD[f])]
        hits[f] = len(n)
    return hits


def school_row(t, run, lists, summary, evidence, year='2026-27'):
    key, folder = t['institution_key'], t['folder']
    progs = [r for r in load_records(folder, 'academic_programs') if r.get('academic_year') == year]
    verified = [r for r in progs if r.get('verification_status') == 'verified']
    reqs = [r for r in load_records(folder, 'degree_requirements') if r.get('academic_year') == year]
    plans = {r['program_key'] for r in reqs if r.get('requirement_kind') == 'program_plan'}
    cats = [r for r in load_records(folder, 'program_catalogs') if r.get('academic_year') == year]
    awards = [r for r in load_records(folder, 'awards') if r.get('program_keys') or r.get('cip_codes')]
    lst = lists.get(key, {}); s = summary.get(key, {})
    listed = [p.get('printed') or p['name'] for p in lst.get('programs', []) if (p.get('listed_as') or p.get('credential_level')) in ('bachelor', 'major')]
    roles = s.get('roles', {})
    ev = defaultdict(int)
    for e in evidence.get(key, []): ev[e['category']] += 1
    cat_errors = defaultdict(int)
    for r in ('catalog_home', 'catalog_nav', 'program_list', 'program_page'):
        for k, n in roles.get(r, {}).get('errors', {}).items(): cat_errors[k] += n
    vfields = field_hits([r['program_name'] for r in verified], [r.get('cip_code') for r in verified])
    pfields = field_hits([r['program_name'] for r in progs], [r.get('cip_code') for r in progs])
    row = {
        'institution_key': key, 'folder': folder, 'name': t['name'], 'control': t.get('control'), 'priority': t.get('priority'),
        'catalog_platform': (t.get('catalog') or {}).get('platform') or ('to be located' if t.get('mode') == 'discover' else None),
        'catalog_home': (t.get('catalog') or {}).get('home'),
        'run': {'printed_catalog_years': lst.get('printed_years', []),
                'catalog_pages_ok': sum(roles.get(r, {}).get('ok', 0) for r in ('catalog_home', 'catalog_nav', 'program_list')),
                'program_pages_ok': roles.get('program_page', {}).get('ok', 0),
                'listed_bachelor_programs': len(listed), 'listed_program_links': len(lst.get('programs', [])),
                'degree_map_docs_ok': roles.get('degree_map', {}).get('ok', 0),
                'policy_pages_ok': roles.get('policy', {}).get('ok', 0) + roles.get('policy_link', {}).get('ok', 0),
                'catalog_fetch_errors': dict(cat_errors), 'candidates': s.get('candidates', 0),
                'listed_fields_by_name': field_hits(listed), 'evidence_sentences': {k: ev.get(k, 0) for k in EVIDENCE_KEYS}} if run else None,
        'persisted': {'programs': len(progs), 'verified_programs': len(verified),
                      'partially_verified_programs': sum(1 for r in progs if r.get('verification_status') == 'partially_verified'),
                      'programs_with_cip': sum(1 for r in progs if r.get('cip_code')), 'programs_with_degree_plan': len(plans),
                      'requirement_rows': len(reqs), 'program_catalog_record': bool(cats),
                      'programs_complete': any(c.get('programs_complete') is True for c in cats),
                      'verified_fields_by_name_or_cip': vfields, 'all_fields_by_name_or_cip': pfields,
                      'cr14': {'cip_code': sum(1 for r in progs if r.get('cip_code')),
                               'admission_type': sum(1 for r in progs if r.get('admission_type')),
                               'internal_transfer': sum(1 for r in progs if r.get('internal_transfer')),
                               'undeclared_policy': any(c.get('undeclared_policy') for c in cats),
                               'program_linked_awards': len(awards)}},
    }
    row['gaps'] = gaps(row)
    return row


def gaps(row):
    g, p, r = [], row['persisted'], row['run']
    if r is None: g.append('no program-depth run yet')
    else:
        errs = r['catalog_fetch_errors']
        if any(k.startswith(('blocked_bot_challenge', 'host_challenge_stop')) for k in errs):
            g.append('catalog program pages behind a bot challenge (recorded, not evaded)')
        elif r['catalog_pages_ok'] == 0: g.append('current catalog not retrieved' + (f" ({', '.join(errs)})" if errs else ''))
        elif r['listed_bachelor_programs'] == 0: g.append('catalog retrieved but no program list parsed')
    if not p['program_catalog_record']: g.append('no reviewed program_catalogs record (completeness unknown)')
    if p['verified_programs'] == 0:
        g.append('no verified programs' + (f" ({p['partially_verified_programs']} partially verified from the state inventory)" if p['partially_verified_programs'] else ''))
    elif r and r['listed_bachelor_programs'] and p['verified_programs'] < r['listed_bachelor_programs']:
        g.append(f"{r['listed_bachelor_programs'] - p['verified_programs']} listed bachelor programs not yet verified")
    missing = [f for f, n in p['verified_fields_by_name_or_cip'].items() if not n and (not r or r['listed_fields_by_name'].get(f))]
    if missing: g.append('priority fields listed but not verified: ' + ', '.join(missing))
    if p['programs_with_degree_plan'] == 0: g.append('no verified degree maps')
    if p['cr14']['admission_type'] == 0: g.append('no verified admission-to-major facts')
    if not p['cr14']['undeclared_policy']: g.append('undeclared policy not verified')
    return g


def all_runs(state):
    base = ROOT / 'programs/runs' / state
    return sorted(p for p in base.glob('*') if (p / 'summary.json').exists()) if base.exists() else []


def build(states):
    """Per institution, the newest run that crawled it (inventory-only runs add the state inventory count)."""
    out = {'states': states, 'academic_year': '2026-27', 'institutions': [], 'runs': {}}
    for st in states:
        targets = json.loads((ROOT / 'programs/targets' / f'{st}.json').read_text())
        runs = all_runs(st)
        out['runs'][st] = [str(r.relative_to(ROOT)) for r in runs]
        per, inventory = {}, {}
        for run in runs:
            summary = json.loads((run / 'summary.json').read_text())
            lists = json.loads((run / 'program_lists.json').read_text())
            if (run / 'state_inventory.json').exists():
                for k, rows in json.loads((run / 'state_inventory.json').read_text()).items():
                    inventory[k] = {'run': str(run.relative_to(ROOT)), 'bachelor_rows': sum(1 for r in rows if re.match(r'^B', str(r.get('Award') or '')))}
            evidence = defaultdict(list)
            if (run / 'evidence.jsonl').exists():
                for l in (run / 'evidence.jsonl').read_text().splitlines():
                    e = json.loads(l); evidence[e['institution_key']].append(e)
            for k, s in summary.items():
                crawled = any(r not in ('state_inventory', 'state_source') for r in s.get('roles', {}))
                if crawled: per[k] = (run, lists, summary, evidence)
        for t in targets['institutions']:
            run, lists, summary, evidence = per.get(t['institution_key'], (None, {}, {}, {}))
            row = school_row(t, run, lists, summary, evidence)
            row['run_dir'] = str(run.relative_to(ROOT)) if run else None
            if t['institution_key'] in inventory: row['state_inventory'] = inventory[t['institution_key']]
            out['institutions'].append({'state': st, **row})
    out['institutions'].sort(key=lambda x: (x['priority'] or 9, x['state'], x['name']))
    return out


def markdown(a):
    yes = lambda b: 'yes' if b else '—'
    L = [f"# Program-depth coverage audit: {' + '.join(a['states'])} ({a['academic_year']})", '',
         'Generated by `python -m programs audit`. "Verified" columns count reviewed records in `data/` (what the product may show). '
         '"Run" columns count what the newest program-depth run retrieved from official sources, unreviewed. Field columns match printed '
         'program names (or CIP when present) and only say where to look; they never mean a program is not offered.', '',
         'Runs: ' + '; '.join(f"{k}: " + ', '.join(f'`{x}`' for x in v) for k, v in a['runs'].items()), '',
         '| P | School | Catalog | Run: listed bachelor | State inventory bachelor | Verified programs | Partially verified | With CIP | Complete? | Eng | CS | Bus | Health | Psy | Degree maps (verified) | Admission facts | Undeclared |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for s in a['institutions']:
        r, p = s['run'] or {}, s['persisted']
        vf, af = p['verified_fields_by_name_or_cip'], p['all_fields_by_name_or_cip']
        cell = lambda f: f"{vf[f]}" + (f" / {af[f]}" if af[f] != vf[f] else '')
        inv = (s.get('state_inventory') or {}).get('bachelor_rows', '–')
        L.append(f"| {s['priority']} | {s['name']} ({s['state']}) | {s['catalog_platform'] or '?'} | {r.get('listed_bachelor_programs', '–')} | {inv} | "
                 f"{p['verified_programs']} | {p['partially_verified_programs']} | {p['programs_with_cip']} | {yes(p['programs_complete'])} | {cell('engineering')} | "
                 f"{cell('computer_science')} | {cell('business_finance')} | {cell('nursing_health')} | {cell('psychology')} | "
                 f"{p['programs_with_degree_plan']} | {p['cr14']['admission_type']} | {yes(p['cr14']['undeclared_policy'])} |")
    L += ['', 'Field cells: verified programs matching the field by printed name or CIP family (/ including partially verified state-inventory records).', '',
          '## CR-14 field obtainability from retrieved official sources (sentences found, unreviewed)', '',
          '| School | direct admit | apply to major | pre-major | progression | open declaration | GPA rule | undeclared | declare-by | change major | CIP | major scholarship | AP/IB/dual credit in program text |',
          '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for s in a['institutions']:
        if not s['run']: continue
        e = s['run']['evidence_sentences']
        L.append(f"| {s['name']} | " + ' | '.join(str(e[k]) for k in EVIDENCE_KEYS) + ' |')
    L += ['', '## Largest gaps by school', '']
    for s in a['institutions']:
        L.append(f"- **{s['name']}** ({s['state']}, P{s['priority']}): " + '; '.join(s['gaps']))
    return '\n'.join(L) + '\n'


def main(states, check=False):
    a = build(states)
    name = '-'.join(states)
    j = json.dumps(a, indent=1, sort_keys=True) + '\n'; m = markdown(a)
    if check:
        cur = (OUT / f'{name}.json').read_text() if (OUT / f'{name}.json').exists() else ''
        if cur != j: print(f'docs/coverage/programs/{name}.json is stale: run python -m programs audit'); return 1
        return 0
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f'{name}.json').write_text(j); (OUT / f'{name}.md').write_text(m)
    print(f'wrote docs/coverage/programs/{name}.json and .md ({len(a["institutions"])} institutions)')
    return 0
