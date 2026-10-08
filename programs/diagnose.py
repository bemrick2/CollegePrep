"""One polite request per URL with the research user agent; prints status, response headers and the first
bytes of the body. Used to characterise refusals (e.g. HTTP 202 challenge pages) without retrying around them.
robots.txt is honoured as in the crawler: a URL it disallows (or a host whose robots.txt cannot be read) is recorded
with the refusal and never requested."""
import io, json, urllib.request, urllib.error
from contextlib import redirect_stdout
from pathlib import Path
from pipeline.crawl import USER_AGENT, ACCEPT, Fetcher


def diagnose(items, robots, opener=urllib.request.urlopen):
    buf = io.StringIO()
    for item in items:
        url, limit = (item, 1500) if isinstance(item, str) else (item['url'], int(item.get('bytes', 1500)))
        if not robots.allowed(url):
            with redirect_stdout(buf):
                print('=' * 80); print(url, None); print(robots.refusal(url))
            continue
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT, 'Accept': ACCEPT})
        try:
            with opener(req, timeout=30) as r:
                status, headers, body = r.status, dict(r.headers), r.read(limit)
        except urllib.error.HTTPError as e:
            status, headers, body = e.code, dict(e.headers or {}), e.read(limit)
        except Exception as e:
            status, headers, body = None, {}, str(e).encode()
        with redirect_stdout(buf):
            print('=' * 80); print(url, status); print(json.dumps(headers, indent=1)[:1500]); print(body.decode('utf-8', 'replace')[:limit])
    return buf.getvalue()


if __name__ == '__main__':
    req_doc = json.load(open('programs/run-request.json'))
    out = Path('programs/runs') / req_doc['state'].upper() / req_doc['run_id']
    out.mkdir(parents=True, exist_ok=True)
    # job logs are not readable from review sessions; the run commit is
    (out / 'diagnose.txt').write_text(diagnose(req_doc.get('diagnose', []), Fetcher()))
