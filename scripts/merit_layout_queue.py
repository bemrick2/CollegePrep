#!/usr/bin/env python3
"""Queue of schools whose merit-scholarship pages the reader has not turned into awards, by layout.

For every in-scope school whose merit status (docs/coverage/baseline/policy_queue.csv) is source_found or
source_inaccessible, runs the current merit reader over the archived pages of its latest pipeline run and classifies
what the pages hold. The result is a work queue, never a finding about the school: no extraction never means no
scholarship.

  layout_status:
    reader_extracts     - the reader extracts candidates; they still need review and may be rejected there (a typical
                          profile, a transfer table, or a reader false positive such as a credit table)
    table_unread        - a page prints a table with dollar amounts and a test-score or GPA figure the reader does not read
    text_mentions       - a page's text names dollar amounts with a test score or GPA, but not in a table (often a renewal
                          rule or a typical profile, sometimes a criteria list); needs a person or a new reader
    no_criteria_seen    - merit pages were crawled but print no amount beside a score or GPA (often holistic or
                          competitive awards; record a quoted 'no published score formula' only when the school says so)
    no_merit_page_seen  - no page in the crawl looked like a scholarship page
    inaccessible        - the crawl could not fetch the school's pages (blocked or failed); recorded, never evaded
    reader_error        - the reader raised an error on a merit page (a reader bug to fix, never a finding)
    run_not_found       - the school's run could not be located on any pipeline-run branch (a tooling gap)
    not_in_run          - the run holds no page for the school (e.g. a targeted re-crawl of other schools); never 'inaccessible'

  Transfer, graduate, international and dual-enrollment pages are neither counted nor classified.

  python scripts/merit_layout_queue.py     writes docs/coverage/merit_layout_queue.csv (reads the pipeline-run branches)
"""
from __future__ import annotations
import csv, gzip, json, re, subprocess, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from pipeline import text as T  # noqa: E402
from pipeline.extractors import merit  # noqa: E402

OUT = ROOT / 'docs/coverage/merit_layout_queue.csv'
SCORE = re.compile(r'\b(ACT|SAT|CLT)\b[^.|]{0,40}\b\d{2,4}\b|\b\d{2,4}\b[^.|]{0,20}\b(ACT|SAT|CLT)\b', re.I)
GPA = re.compile(r'\b[1-4]\.\d{1,2}\b[^.|]{0,30}\bGPA\b|\bGPA\b[^.|]{0,30}\b[1-4]\.\d{1,2}\b', re.I)
MONEY = re.compile(r'\$\s?\d[\d,]{2,}')
OTHER_PAGE = re.compile(r'transfer|(?<!under)graduate|/grad/|law\.|/law/|international|pre-college|dual-enrollment|veteran', re.I)
FIELDS = ['rank', 'institution_key', 'name', 'state', 'undergraduate_enrollment', 'merit_status', 'run', 'layout_status',
          'pages_crawled', 'merit_pages', 'candidates', 'score_linked_candidates', 'gpa_linked_candidates', 'sample_url']


def git(*args, binary=False):
    p = subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, text=not binary)
    return p.stdout if p.returncode == 0 else None


class Run:
    def __init__(self, st, day):
        self.st, self.day = st, day
        # TN/2026-10-02-r2 lives on pipeline-run/tn-2026-10-02 beside -r3...-r5, so try the date prefix too
        refs = sorted(set((git('branch', '-r', '--list', f'origin/pipeline-run/{st.lower()}-{day}*') or '').split()
                          + (git('branch', '-r', '--list', f'origin/pipeline-run/{st.lower()}-{day[:10]}*') or '').split()))
        self.ref = next((r for r in refs if git('cat-file', '-e', f'{r}:pipeline/runs/{st}/{day}/manifest.jsonl') is not None), None)
        self.cat = subprocess.Popen(['git', '-C', str(ROOT), 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE) if self.ref else None

    def get(self, path):
        self.cat.stdin.write(f'{self.ref}:pipeline/runs/{self.st}/{self.day}/{path}\n'.encode()); self.cat.stdin.flush()
        hdr = self.cat.stdout.readline().split()
        if hdr[-1] == b'missing': return None
        n = int(hdr[2]); data = self.cat.stdout.read(n); self.cat.stdout.read(1); return data


def classify(run, schools, registry, today_year):
    out = {k: {'pages': 0, 'merit_pages': 0, 'candidates': 0, 'score': 0, 'gpa': 0, 'table': [], 'text': [], 'read': [], 'error': []} for k in schools}
    man = run.get('manifest.jsonl') if run.ref else None
    seen = set()
    sys.path.insert(0, str(ROOT / 'scripts'))
    import build_baseline as B
    for line in (man or b'').decode().splitlines():
        if not line.strip(): continue
        e = json.loads(line); k = e.get('institution_key')
        if k not in out or not e.get('page_file') or (k, e['page_file']) in seen: continue
        seen.add((k, e['page_file']))
        raw = run.get(f"pages/{e['page_file']}")
        if raw is None: continue
        d = json.loads(gzip.decompress(raw)); r = out[k]; r['pages'] += 1
        page = T.Page(d['text'], d['title'], d['tables'], [tuple(x) for x in d.get('links', [])], d['headings'])
        if not merit.SCHOLARSHIP_CONTEXT.search(page.title + ' ' + ' '.join(page.headings[:6]) + ' ' + e.get('url', '')): continue
        if OTHER_PAGE.search(e.get('url', '')): continue
        r['merit_pages'] += 1
        try:
            cands = merit.extract(registry.get(k, {'institution_key': k}), e, page, today_year)
        except Exception:  # a reader crash is its own queue entry, not a stop and not a finding
            r['error'].append(e.get('url')); continue
        if cands:
            r['candidates'] += len(cands); r['read'].append(e.get('url'))
            r['score'] += sum(bool(B.score_linked(c['record'])) for c in cands); r['gpa'] += sum(bool(B.gpa_linked(c['record'])) for c in cands)
            continue
        if any(MONEY.search(json.dumps(t['rows'])) and (SCORE.search(json.dumps(t['rows'])) or GPA.search(json.dumps(t['rows']))) for t in page.tables):
            r['table'].append(e.get('url'))
        elif any(MONEY.search(s) and (SCORE.search(s) or GPA.search(s)) for s in re.split(r'(?<=[.!?])\s+|\n+', page.text[:60000])):
            r['text'].append(e.get('url'))
    return out


def main():
    queue = [r for r in csv.DictReader(open(ROOT / 'docs/coverage/baseline/policy_queue.csv'))
             if r['merit_status'] in ('source_found', 'source_inaccessible')]
    attempts = json.loads((ROOT / 'baseline/policy/pipeline_attempts.json').read_text())['schools']
    sys.path.insert(0, str(ROOT / 'scripts'))
    from build_baseline import PLANNING_YEAR  # a fixed year, so the queue is reproducible
    today_year = PLANNING_YEAR
    by_run = {}
    for r in queue:
        run = (attempts.get(r['institution_key'], {}).get('merit_scholarships') or {}).get('run') or r['merit_run']
        by_run.setdefault(run, []).append(r)
    rows = []
    for run_id, rs in sorted(by_run.items()):
        st, day = run_id.split('/', 1)
        registry = {i['institution_key']: i for i in json.loads((ROOT / f'pipeline/registry/{st}.json').read_text())['institutions']}
        run = Run(st, day)
        res = classify(run, {r['institution_key'] for r in rs}, registry, today_year)
        for r in rs:
            x = res[r['institution_key']]
            if not run.ref: status, url = 'run_not_found', ''
            elif r['merit_status'] == 'source_inaccessible' and not x['pages']: status, url = 'inaccessible', ''
            elif x['error']: status, url = 'reader_error', x['error'][0]
            elif x['candidates']: status, url = 'reader_extracts', x['read'][0]
            elif x['table']: status, url = 'table_unread', sorted(x['table'])[0]
            elif x['text']: status, url = 'text_mentions', sorted(x['text'])[0]
            elif x['merit_pages']: status, url = 'no_criteria_seen', ''
            elif x['pages']: status, url = 'no_merit_page_seen', ''
            else: status, url = 'not_in_run', ''
            rows.append({'rank': int(r['rank']), 'institution_key': r['institution_key'], 'name': r['name'], 'state': r['state'],
                         'undergraduate_enrollment': r['undergraduate_enrollment'], 'merit_status': r['merit_status'], 'run': run_id,
                         'layout_status': status, 'pages_crawled': x['pages'], 'merit_pages': x['merit_pages'], 'candidates': x['candidates'],
                         'score_linked_candidates': x['score'], 'gpa_linked_candidates': x['gpa'], 'sample_url': url})
    rows.sort(key=lambda r: r['rank'])
    with open(OUT, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n'); w.writeheader(); w.writerows(rows)
    print(f'{len(rows)} schools -> {OUT.relative_to(ROOT)}:', dict(Counter(r['layout_status'] for r in rows)))


if __name__ == '__main__':
    main()
