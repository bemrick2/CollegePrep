#!/usr/bin/env python3
"""Find explicit official statements about how a school awards freshman merit scholarships, in archived run pages.

Reads the pages the national pipeline already fetched (pipeline-run/** branches; each page is content-addressed and
retained in evidence-store) for in-scope schools, and lists sentences that state, in the school's own words, one of:

  no_fixed_criteria     "there are not fixed criteria", "no minimum GPA or test score" for merit awards
  automatic             "automatically considered", "no separate application", "guaranteed" merit awards
  competitive           "competitive", "holistic", "limited number" merit awards
  test_optional_scores  how scores are treated for scholarships when admission is test-optional
  superscore            superscoring for scholarships

The output is a review list (one row per sentence, with the page URL, run and page file), never a record: a person reads
each sentence in context and records the school's status in baseline/policy/merit_research.json with the quote. Nothing
here infers a threshold, an amount or an SAT equivalent.

  python3 scripts/scan_merit_statements.py OUT.json [--limit-schools N]   (ranked by undergraduate enrollment)
"""
from __future__ import annotations
import csv, gzip, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MERIT = re.compile(r'\b(merit|academic|freshman|first[- ]year|presidential|dean\'?s|chancellor\'?s|honors?)\b[^.]{0,40}\bscholarships?\b|'
                   r'\bscholarships?\b[^.]{0,40}\b(merit|academic)\b', re.I)
KINDS = {
    'no_fixed_criteria': re.compile(r'\b(?:no|not|aren\'t|isn\'t|there (?:is|are) no)\b[^.]{0,30}\b(?:fixed|set|specific|minimum|cut[- ]?off)\b'
                                    r'[^.]{0,40}\b(?:criteria|requirements?|scores?|gpas?|thresholds?)\b', re.I),
    'automatic': re.compile(r'\bautomatic(?:ally)?\b[^.]{0,60}\b(?:consider|award|eligib|review)|\bno (?:separate|additional) '
                            r'(?:scholarship )?application\b|\bguarantee[ds]?\b[^.]{0,40}\bscholarship', re.I),
    'competitive': re.compile(r'\b(?:competitive|holistic(?:ally)?|limited number)\b', re.I),
    'test_optional_scores': re.compile(r'\btest[- ]optional\b[^.]{0,120}\bscholarship|\bscholarship[^.]{0,120}\btest[- ]optional\b|'
                                       r'\bwithout (?:an? )?(?:ACT|SAT|test scores?)\b[^.]{0,80}\bscholarship', re.I),
    'superscore': re.compile(r'\bsuper[- ]?scor', re.I),
}


def git(*a, binary=False):
    r = subprocess.run(['git', *a], cwd=ROOT, capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode()


def sentences(text):
    for para in re.split(r'\n+', text):
        for s in re.split(r'(?<=[.!?])\s+(?=[A-Z])', para):
            s = s.strip()
            if 25 <= len(s) <= 600: yield s


def main(out, limit=None):
    queue = list(csv.DictReader(open(ROOT / 'docs/coverage/baseline/policy_queue.csv', encoding='utf-8')))
    want = {r['institution_key']: r for r in queue[:limit] if r['merit_status'] not in ('verified',)}
    branches = sorted(b.strip() for b in git('branch', '-r', '--list', 'origin/pipeline-run/*').splitlines() if b.strip())
    hits, seen = [], set()
    for b in branches:
        for path in git('ls-tree', '-r', '--name-only', b).splitlines():
            if not (path.startswith('pipeline/runs/') and path.endswith('/manifest.jsonl')): continue
            run_dir = path.rsplit('/', 1)[0]
            for line in git('show', f'{b}:{path}').splitlines():
                e = json.loads(line)
                k = e.get('institution_key')
                if k not in want or not e.get('page_file'): continue
                key = (k, e['page_file'])
                if key in seen: continue
                seen.add(key)
                try: page = json.loads(gzip.decompress(git('show', f"{b}:{run_dir}/pages/{e['page_file']}", binary=True)))
                except subprocess.CalledProcessError: continue
                text = page.get('text') or ''
                if not MERIT.search(text) and 'scholarship' not in (e.get('url') or '').lower(): continue
                for s in sentences(text):
                    if 'scholarship' not in s.lower() and not MERIT.search(s): continue
                    for kind, rx in KINDS.items():
                        if rx.search(s):
                            hits.append({'institution_key': k, 'name': want[k]['name'], 'rank': int(want[k]['rank']), 'kind': kind,
                                         'sentence': s, 'url': e.get('url'), 'page_file': e['page_file'], 'run': run_dir,
                                         'branch': b.removeprefix('origin/'), 'title': page.get('title')})
    hits.sort(key=lambda h: (h['rank'], h['kind'], h['url']))
    Path(out).write_text(json.dumps(hits, indent=1, ensure_ascii=False) + '\n')
    print(f'{len(hits)} statements from {len({h["institution_key"] for h in hits})} of {len(want)} schools -> {out}')


if __name__ == '__main__':
    lim = int(sys.argv[sys.argv.index('--limit-schools') + 1]) if '--limit-schools' in sys.argv else None
    sys.exit(main(sys.argv[1], lim))
