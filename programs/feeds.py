"""Complete program lists from a JavaScript catalog's own data feed (Coursedog, Kuali).

The rendered catalog page loads its program list from the catalog backend in pages of 20 (Coursedog
`/api/v1/cm/<school>/programs/search/...`) or by catalog id (Kuali `/api/v1/catalog/...`). The browser fetch records
those responses (role `catalog_feed`, with method and body). This step repeats the same request the page made, once,
asking for all rows instead of the first page (Coursedog `limit`), or requests the catalog's public program list (Kuali),
through pipeline.crawl.Fetcher's robots and politeness rules. Responses are stored as `catalog_api` documents.
"""
from __future__ import annotations
import hashlib, json, re, urllib.request
from urllib.parse import urlsplit, parse_qsl, urlencode, urlunsplit

from pipeline import text as T
from pipeline.crawl import USER_AGENT, HostGate, now


def _get(fetcher, url, method='GET', body=None):
    if not fetcher.allowed(url): return {'status': None, 'error': fetcher.refusal(url)}, None
    host = urlsplit(url).netloc.lower(); entry = fetcher.gate.wait(host)
    try:
        req = urllib.request.Request(url, data=body.encode() if body else None, method=method,
                                     headers={'User-Agent': USER_AGENT, 'Accept': 'application/json',
                                              **({'Content-Type': 'application/json'} if body else {})})
        with fetcher.opener.open(req, timeout=90) as r:
            b = r.read(); status = r.status
    except Exception as exc:
        return {'status': getattr(exc, 'code', None), 'error': f'{type(exc).__name__}: {exc}'[:300]}, None
    finally:
        HostGate.done(entry)
    return {'status': status, 'final_url': url, 'content_type': 'application/json', 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}, b


def _store(run, key, url, meta, body, via, request=None):
    e = {'institution_key': key, 'url': url, 'role': 'catalog_api', 'via': via, 'depth': 1, 'fetched_at': now(), **meta}
    if request: e['request'] = request
    if body is not None:
        try:
            text = json.dumps(json.loads(body), indent=0, ensure_ascii=False)
            e['kind'] = 'json'; e['page_file'] = run.save_page(meta['sha256'], 'json', T.Page(text, 'catalog program list (catalog backend)', [], [], []), [])
        except ValueError:
            e['error'] = 'unparsed_json'
    run.record(e)


def complete(target, run, fetcher, log=print):
    key = target['institution_key']
    entries = [e for e in run.entries() if e.get('institution_key') == key]
    done = {e['url'] for e in entries if e.get('role') == 'catalog_api' and e.get('page_file')}
    for e in entries:
        if e.get('role') != 'catalog_feed': continue
        u = e['url']
        if re.search(r'app\.coursedog\.com/api/v1/cm/[^/]+/programs/search/', u):
            p = urlsplit(u); q = dict(parse_qsl(p.query, keep_blank_values=True))
            q['skip'], q['limit'] = '0', '2000'
            full = urlunsplit((p.scheme, p.netloc, p.path, urlencode(q), ''))
            if full in done: continue
            meta, body = _get(fetcher, full, e.get('request_method') or 'GET', e.get('request_body'))
            _store(run, key, full, meta, body, u, {'method': e.get('request_method') or 'GET', 'body': e.get('request_body')})
            done.add(full); log(f'{key}: coursedog program list {meta.get("status")} {meta.get("bytes")}')
        m = re.search(r'https://([a-z0-9-]+\.kuali\.co)/api/v1/catalog/public/catalogs/([0-9a-f]{24})', u)
        if m:
            full = f'https://{m.group(1)}/api/v1/catalog/programs/{m.group(2)}'
            if full in done: continue
            meta, body = _get(fetcher, full)
            _store(run, key, full, meta, body, u)
            done.add(full); log(f'{key}: kuali program list {meta.get("status")} {meta.get("bytes")}')


LARGE_PDF_BYTES = 80 * 1024 * 1024


def fetch_large(fetcher, url):
    """A catalog's own full-catalog PDF can exceed the national fetcher's 15 MB cap (Tennessee Tech: about 16 MB).
    Same robots and per-host politeness; a larger cap only for role catalog_pdf."""
    if not fetcher.allowed(url): return {'status': None, 'error': fetcher.refusal(url)}, None
    host = urlsplit(url).netloc.lower(); entry = fetcher.gate.wait(host)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT, 'Accept': 'application/pdf'})
        with fetcher.opener.open(req, timeout=180) as r:
            b = r.read(LARGE_PDF_BYTES + 1); status = r.status; ctype = r.headers.get('Content-Type', '')
    except Exception as exc:
        return {'status': getattr(exc, 'code', None), 'error': f'{type(exc).__name__}: {exc}'[:300]}, None
    finally:
        HostGate.done(entry)
    meta = {'status': status, 'final_url': url, 'content_type': ctype, 'bytes': len(b)}
    if len(b) > LARGE_PDF_BYTES: meta['error'] = 'too_large'; return meta, None
    meta['sha256'] = hashlib.sha256(b).hexdigest()
    return meta, b
