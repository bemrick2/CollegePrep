"""python -m programs crawl|extract|promote|audit|status  (see programs/README.md)"""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_targets(state):
    return json.loads((ROOT / 'programs/targets' / f'{state.upper()}.json').read_text())


def main(argv=None):
    ap = argparse.ArgumentParser(prog='programs')
    sub = ap.add_subparsers(dest='cmd', required=True)
    c = sub.add_parser('crawl'); c.add_argument('--state', required=True); c.add_argument('--run', required=True)
    c.add_argument('--only', nargs='*'); c.add_argument('--workers', type=int, default=8); c.add_argument('--no-browser', action='store_true'); c.add_argument('--adapters-only', action='store_true')
    c.add_argument('--policy-only', action='store_true')
    e = sub.add_parser('extract'); e.add_argument('--state', required=True); e.add_argument('--run', required=True)
    pr = sub.add_parser('promote'); pr.add_argument('decisions')
    a = sub.add_parser('audit'); a.add_argument('--states', nargs='+', default=['TN', 'OR']); a.add_argument('--check', action='store_true')
    st = sub.add_parser('status'); st.add_argument('--states', nargs='*'); st.add_argument('--check', action='store_true')
    args = ap.parse_args(argv)
    if args.cmd == 'crawl':
        from .crawl import crawl
        crawl(load_targets(args.state), args.run, only=args.only, workers=args.workers, use_browser=not args.no_browser, adapters_only=args.adapters_only, policy_only=args.policy_only)
    elif args.cmd == 'extract':
        from .extract import extract_run
        s = extract_run(load_targets(args.state), args.run)
        print(json.dumps({k: {'candidates': v['candidates'], 'list': v['program_list_links']} for k, v in s.items()}, indent=1))
    elif args.cmd == 'promote':
        from .promote import promote
        promote(Path(args.decisions))
    elif args.cmd == 'audit':
        from .audit import main as audit_main
        return audit_main(args.states, check=args.check)
    elif args.cmd == 'status':
        from .status import main as status_main
        return status_main([s.upper() for s in args.states] if args.states else None, check=args.check)


if __name__ == '__main__':
    raise SystemExit(main())
