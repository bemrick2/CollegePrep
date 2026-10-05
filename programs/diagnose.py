"""One polite request per URL with the research user agent; prints status, response headers and the first
bytes of the body. Used to characterise refusals (e.g. HTTP 202 challenge pages) without retrying around them."""
import json, sys, urllib.request, urllib.error
from pipeline.crawl import USER_AGENT, ACCEPT

for url in json.load(open('programs/run-request.json')).get('diagnose', []):
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT, 'Accept': ACCEPT})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            status, headers, body = r.status, dict(r.headers), r.read(1500)
    except urllib.error.HTTPError as e:
        status, headers, body = e.code, dict(e.headers or {}), e.read(1500)
    except Exception as e:
        status, headers, body = None, {}, str(e).encode()
    print('=' * 80); print(url, status); print(json.dumps(headers, indent=1)[:1500]); print(body.decode('utf-8', 'replace')[:1500])
