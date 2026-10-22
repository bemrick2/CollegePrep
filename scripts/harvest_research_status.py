#!/usr/bin/env python3
"""Snapshot what the national pipeline's runs found per school and policy topic, from the run branches.

Each `pipeline-run/**` branch holds pipeline/runs/<ST>/<run>/coverage.json with one row per registered school and a status
per topic (verified_current, partially_verified_current, candidate_ready, candidate_exception, source_found, not_found,
fetch_failed). Run branches are never merged, so this writes baseline/policy/pipeline_attempts.json: for every school and
policy topic, the most informative status any run reached, and which run. `not_found` means the crawl of the school's
official site found no page on the topic; it never means the school has no such policy.

  git fetch origin 'refs/heads/pipeline-run/*:refs/remotes/origin/pipeline-run/*'
  python3 scripts/harvest_research_status.py
"""
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ['merit_scholarships', 'ap_credit', 'clep_credit', 'ib_credit', 'aid_appeals', 'residency', 'tuition_fees',
          'cost_of_attendance', 'admissions_tests', 'common_data_set']
ORDER = ['verified_current', 'partially_verified_current', 'candidate_ready', 'candidate_exception', 'source_found',
         'not_found', 'fetch_failed']


def git(*a):
    return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def main():
    branches = sorted(b.strip() for b in git('branch', '-r', '--list', 'origin/pipeline-run/*').splitlines() if b.strip())
    best, runs = {}, []
    for b in branches:
        for path in git('ls-tree', '-r', '--name-only', b).splitlines():
            if not (path.startswith('pipeline/runs/') and path.endswith('/coverage.json')): continue
            cov = json.loads(git('show', f'{b}:{path}'))
            run = path.split('/')[2] + '/' + path.split('/')[3]
            runs.append({'branch': b.removeprefix('origin/'), 'run': run, 'commit': git('rev-parse', b).strip()[:12],
                         'schools': len(cov.get('rows', []))})
            for row in cov.get('rows', []):
                k = row['institution_key']
                for t in TOPICS:
                    s = (row.get('categories') or {}).get(t)
                    if s not in ORDER: continue
                    cur = best.setdefault(k, {}).get(t)
                    if cur is None or ORDER.index(s) < ORDER.index(cur['status']):
                        best[k][t] = {'status': s, 'run': run}
    out = {'note': __doc__.split('\n\n')[1].replace('\n', ' '), 'status_order': ORDER, 'runs': runs,
           'schools': {k: best[k] for k in sorted(best)}}
    p = ROOT / 'baseline/policy/pipeline_attempts.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=1, sort_keys=False) + '\n')
    print(f'{len(runs)} runs from {len(branches)} branches; {len(best)} schools with a recorded attempt')


if __name__ == '__main__':
    sys.exit(main())
