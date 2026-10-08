"""Research priority: which registered institutions to research next, and why.

Computed only from committed files (docs/coverage/programs/STATUS.json, programs/queue/<ST>.json,
programs/targets/configs/<ST>.json, IPEDS entering students via programs.status.entering), so any session can
regenerate the same ranking and resume where the last one stopped.

    python3 scripts/research_priority.py [--batch N] [--check]

writes docs/coverage/research_priority.json (every uncovered institution with its tier and reason) and prints the
next batch. Tiers, in order:
  near        catalog verified >= 75% of the listed count but under the 90% standard, or catalog met with only
              non-catalog dimensions open: closest to the coverage standard
  configured  a catalog is configured but the institution has no catalog count yet (needs a run or a re-run)
  unconfigured no catalog configured and no blocking queue reason: needs a catalog found (web search) and configured
  blocked     the institution or catalog gap is queued with a blocking reason (bot challenge, robots, fetch failure,
              no year label, unreadable layout, not published): retried only when the blocker changes
Within a tier, institutions are ordered by IPEDS 2023-24 entering first-year students (largest first).
"""
import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from programs import status as ST  # noqa: E402

BLOCKING = {'bot_challenge', 'robots_disallowed', 'fetch_failed', 'no_year_label', 'year_inconsistent',
            'layout_not_readable', 'not_published', 'state_inventory_only', 'out_of_scope'}
TIERS = ('near', 'configured', 'unconfigured', 'blocked')
OUT = ROOT / 'docs/coverage/research_priority.json'


def rank():
    s = json.loads((ROOT / 'docs/coverage/programs/STATUS.json').read_text())
    rows = []
    for st in s['states']:
        state = st['state']
        w = ST.entering(state)
        p = ROOT / 'programs/targets/configs' / f'{state}.json'
        cfg = json.loads(p.read_text()) if p.exists() else {}
        q = ST.queue(state)
        q = q.get('entries', []) if isinstance(q, dict) else q
        for i in st['institutions']:
            if i['status'] == 'covered': continue
            k = i['institution_key']
            reasons = {e['reason'] for e in q if e['institution_key'] == k and e['gap'] in ('institution', 'catalog')}
            listed, ver = i.get('listed_bachelor_programs'), i.get('verified_bachelor_programs') or 0
            share = i.get('catalog_share') if listed else None  # verified listed programs / listed (STATUS), not raw record count
            dims = i.get('dimensions') or {}
            if reasons & BLOCKING:
                tier, why = 'blocked', ', '.join(sorted(reasons & BLOCKING))
            elif share is not None and share >= 0.75:
                tier, why = 'near', f'catalog share {share:.0%} of {listed}'
            elif dims.get('catalog') == 'met':
                tier, why = 'near', 'catalog met; open: ' + ', '.join(d for d, v in dims.items() if v == 'open')
            elif i['folder'] in cfg:
                tier, why = 'configured', (f'catalog share {share:.0%} of {listed}' if listed and share is not None else f'{ver} verified, no list count')
            else:
                tier, why = 'unconfigured', 'no catalog configured'
            rows.append({'state': state, 'institution_key': k, 'folder': i['folder'], 'name': i['name'],
                         'entering_students': w.get(k, 0), 'tier': tier, 'reason': why,
                         'verified_programs': ver, 'listed_programs': listed})
    rows.sort(key=lambda r: (TIERS.index(r['tier']), -r['entering_students'], r['state'], r['folder']))
    for n, r in enumerate(rows, 1): r['rank'] = n
    return {'source': 'docs/coverage/programs/STATUS.json; programs/queue; programs/targets/configs; IPEDS 2023-24 admissions',
            'tiers': {t: sum(1 for r in rows if r['tier'] == t) for t in TIERS}, 'institutions': rows}


def main(argv=None):
    a = argparse.ArgumentParser(); a.add_argument('--batch', type=int, default=15); a.add_argument('--check', action='store_true')
    args = a.parse_args(argv)
    doc = rank(); text = json.dumps(doc, indent=1) + '\n'
    if args.check:
        if not OUT.exists() or OUT.read_text() != text:
            print('docs/coverage/research_priority.json is stale: run python3 scripts/research_priority.py'); return 1
        print('Research priority current'); return 0
    OUT.write_text(text)
    print(doc['tiers'])
    for r in [r for r in doc['institutions'] if r['tier'] != 'blocked'][:args.batch]:
        print(f"{r['rank']:4d} {r['tier']:12s} {r['state']} {r['folder']:22s} {r['entering_students']:6d}  {r['reason']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
