"""One polite request per URL with the research user agent; prints status, response headers and the first
bytes of the body. Used to characterise refusals (e.g. HTTP 202 challenge pages) without retrying around them."""
import io, json, sys, urllib.request, urllib.error
from contextlib import redirect_stdout
from pathlib import Path
from pipeline.crawl import USER_AGENT, ACCEPT

req_doc = json.load(open('programs/run-request.json'))
out = Path('programs/runs') / req_doc['state'].upper() / req_doc['run_id']
out.mkdir(parents=True, exist_ok=True)
buf = io.StringIO()
for item in req_doc.get('diagnose', []):
    url, limit = (item, 1500) if isinstance(item, str) else (item['url'], int(item.get('bytes', 1500)))
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT, 'Accept': ACCEPT})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            status, headers, body = r.status, dict(r.headers), r.read(limit)
    except urllib.error.HTTPError as e:
        status, headers, body = e.code, dict(e.headers or {}), e.read(limit)
    except Exception as e:
        status, headers, body = None, {}, str(e).encode()
    with redirect_stdout(buf):
        print('=' * 80); print(url, status); print(json.dumps(headers, indent=1)[:1500]); print(body.decode('utf-8', 'replace')[:limit])
(out / 'diagnose.txt').write_text(buf.getvalue())  # job logs are not readable from review sessions; the run commit is
