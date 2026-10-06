"""Review helper: print a fetched document's text from a run (python -m programs.show RUN URL-SUBSTRING [GREP])."""
import re, sys
from pathlib import Path
from pipeline.crawl import Run

run, frag = Run(Path(sys.argv[1])), sys.argv[2]
pat = re.compile(sys.argv[3], re.I) if len(sys.argv) > 3 else None
for e in run.entries():
    if frag in e['url'] and e.get('page_file'):
        p, _ = run.load_page(e['page_file'])
        print('==', e['url'], e.get('sha256', '')[:16], e.get('fetched_at'), '|', p.title)
        for i, l in enumerate(p.lines):
            if pat is None or pat.search(l): print(f'{i:4} {l[:400]}')
        break
