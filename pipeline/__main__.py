"""CLI for the official-source research pipeline.

  python -m pipeline registry --state TN            # (re)build pipeline/registry/TN.json from IPEDS HD
  python -m pipeline crawl --state TN --run DIR     # fetch official pages (needs open internet; resumable)
  python -m pipeline review --state TN --run DIR    # extract, re-verify, diff, exception queue, coverage
  python -m pipeline run --state TN --run DIR       # crawl + review
  python -m pipeline promote --state TN --decisions pipeline/decisions/TN-<run>.json
"""
from __future__ import annotations
import argparse, sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline import registry as reg  # noqa: E402


def main(argv=None):
    p = argparse.ArgumentParser(prog='pipeline')
    p.add_argument('command', choices=['registry', 'crawl', 'review', 'run', 'promote'])
    p.add_argument('--state', required=True)
    p.add_argument('--run', type=Path, help='run directory (default pipeline/runs/<STATE>/<today>)')
    p.add_argument('--only', nargs='*', help='institution keys or folders to limit the crawl to')
    p.add_argument('--budget', type=int, default=45, help='pages per institution')
    p.add_argument('--program-budget', type=int, default=40, help='catalog program pages per institution')
    p.add_argument('--workers', type=int, default=8)
    p.add_argument('--delay', type=float, default=1.0, help='seconds between requests to one host')
    p.add_argument('--decisions', type=Path)
    a = p.parse_args(argv)
    state = a.state.upper()
    if a.command == 'registry':
        print(reg.write(state)); return 0
    registry = reg.load(state)
    run_dir = a.run or Path('pipeline/runs') / state / date.today().isoformat()
    if a.command in {'crawl', 'run'}:
        from pipeline.crawl import crawl
        crawl(registry, run_dir, only=set(a.only or []), budget=a.budget, workers=a.workers, delay=a.delay,
              program_budget=a.program_budget)
    if a.command in {'review', 'run'}:
        from pipeline.crawl import Run
        from pipeline.review import review
        cands, verify, cov = review(registry, Run(run_dir))
        print(f"candidates={len(cands)} exceptions={sum(1 for c in cands if c['issues'])} "
              f"reverified={sum(1 for v in verify if v.get('result') == 'all_values_found_year_labeled')} totals={cov['totals']}")
    if a.command == 'promote':
        from pipeline.promote import promote
        promote(registry, a.decisions or sys.exit('--decisions pipeline/decisions/<STATE>-<run>.json is required'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
