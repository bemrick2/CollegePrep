"""Polite, resumable, topic-directed retrieval of official pages for registry institutions.

For each institution: start at its registry seeds and previously cited sources, follow only links
on its own registrable domains, and spend a fixed page budget on links ranked by research topic.
robots.txt is honoured; each host gets at most one request per `delay` seconds. Every fetch (also
failures and robots refusals) is appended to `manifest.jsonl`; parsed documents are stored
content-addressed in `pages/<sha256[:20]>.json.gz`. Re-running with the same run directory skips
URLs already in the manifest and rebuilds the frontier from stored links, so an interrupted run
resumes and a finished run is a no-op.
"""
from __future__ import annotations
import gzip, hashlib, heapq, io, json, re, socket, threading, time, urllib.error, urllib.request, zipfile
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
from urllib.robotparser import RobotFileParser
from xml.etree import ElementTree

from . import text as T, topics
from .registry import registrable_domain

USER_AGENT = 'CollegePrepResearchBot/1.0 (+https://github.com/bemrick2/collegeprep; official-source research)'
MAX_BYTES = 15 * 1024 * 1024
ACCEPT = 'text/html,application/xhtml+xml,application/pdf,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;q=0.9,*/*;q=0.5'


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class HostGate:
    """Per-host politeness: one request at a time and a minimum delay between requests."""
    MAX_DELAY = 60.0

    def __init__(self, delay: float):
        self.delay = delay; self.lock = threading.Lock(); self.hosts = {}; self.host_delay = {}

    def set_delay(self, host, seconds):
        """A host asked for a longer delay (robots.txt Crawl-delay); never shorten it."""
        with self.lock:
            self.host_delay[host] = min(self.MAX_DELAY, max(self.host_delay.get(host, self.delay), float(seconds)))

    def backoff(self, host):
        """A host answered with a rate challenge (202/429): slow down for the rest of the run."""
        with self.lock:
            self.host_delay[host] = min(self.MAX_DELAY, max(2 * self.host_delay.get(host, self.delay), 5.0))

    def delay_for(self, host):
        return self.host_delay.get(host, self.delay)

    def wait(self, host):
        with self.lock:
            entry = self.hosts.setdefault(host, [threading.Lock(), 0.0])
        entry[0].acquire()
        pause = entry[1] + self.delay_for(host) - time.monotonic()
        if pause > 0: time.sleep(pause)
        return entry

    @staticmethod
    def done(entry):
        entry[1] = time.monotonic(); entry[0].release()


class Fetcher:
    def __init__(self, delay=1.0, timeout=30, opener=None):
        self.gate = HostGate(delay); self.timeout = timeout
        self.opener = opener or urllib.request.build_opener()
        self.robots = {}; self.robots_lock = threading.Lock()

    def _raw(self, url):
        """(status, final_url, headers, body) with retries on transient failures."""
        host = urlsplit(url).netloc.lower()
        last = None
        for attempt in range(3):
            entry = self.gate.wait(host)
            try:
                req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT, 'Accept': ACCEPT})
                with self.opener.open(req, timeout=self.timeout) as r:
                    body = r.read(MAX_BYTES + 1)
                    return r.status, r.geturl(), dict(r.headers), body
            except urllib.error.HTTPError as e:
                last = (e.code, url, dict(e.headers or {}), b'')
                if e.code < 500 and e.code != 429: return last
            except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError, OSError) as e:
                last = (None, url, {}, str(getattr(e, 'reason', e)).encode()[:300])
            finally:
                HostGate.done(entry)
            time.sleep(2 * (attempt + 1))
        return last

    def allowed(self, url) -> bool:
        parts = urlsplit(url); origin = f'{parts.scheme}://{parts.netloc}'
        with self.robots_lock:
            rp = self.robots.get(origin)
        if rp is None:
            status, _, _, body = self._raw(origin + '/robots.txt')
            rp = RobotFileParser()
            if status == 200:
                rp.parse(body.decode('utf-8', 'replace').splitlines())
            elif status is not None and 400 <= status < 500:
                rp.allow_all = True
            else:
                rp.disallow_all = True  # Unreachable robots: do not crawl that host this run.
            delay = rp.crawl_delay(USER_AGENT) if status == 200 else None
            if delay:
                self.gate.set_delay(parts.netloc.lower(), delay)
            with self.robots_lock:
                self.robots[origin] = rp
        return rp.can_fetch(USER_AGENT, url)

    def fetch(self, url):
        if not self.allowed(url):
            return {'status': None, 'error': 'disallowed_by_robots'}, None
        status, final, headers, body = self._raw(url)
        meta = {'status': status, 'final_url': final, 'content_type': headers.get('Content-Type', ''),
                'last_modified': headers.get('Last-Modified'), 'bytes': len(body)}
        if status in (202, 429):
            self.gate.backoff(urlsplit(url).netloc.lower())  # slow down; the caller may retry once later
        if status != 200:
            # 202/403/429 from CDNs are bot challenges or blocks. They are recorded, never evaded.
            meta['error'] = (body.decode('utf-8', 'replace')[:300] if status is None else
                             'blocked_bot_challenge' if status == 202 else 'blocked_forbidden' if status == 403 else f'http_{status}')
            return meta, None
        if len(body) > MAX_BYTES:
            meta['error'] = 'too_large'; return meta, None
        meta['sha256'] = hashlib.sha256(body).hexdigest()
        return meta, body


def parse_document(url, content_type, body):
    ct = (content_type or '').lower()
    low = url.lower().split('?')[0]
    if 'pdf' in ct or low.endswith('.pdf') or body[:5] == b'%PDF-':
        return 'pdf', T.parse_pdf(body)
    if 'spreadsheetml' in ct or low.endswith('.xlsx'):
        return 'xlsx', xlsx_page(body)
    if 'html' in ct or 'xml' in ct or body.lstrip()[:1] == b'<':
        return 'html', T.parse_html(body, url)
    return 'other', None


def xlsx_page(body):
    """Cell text of every sheet as 'Sheet!A1: value' lines (stdlib zip + XML)."""
    try:
        z = zipfile.ZipFile(io.BytesIO(body))
    except zipfile.BadZipFile:
        return None
    ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    shared = []
    if 'xl/sharedStrings.xml' in z.namelist():
        for si in ElementTree.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si', ns):
            shared.append(''.join(t.text or '' for t in si.iter('{%s}t' % ns['m'])))
    lines, rows_out = [], []
    for name in sorted(n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml$', n)):
        sheet = name.rsplit('/', 1)[1][:-4]
        for row in ElementTree.fromstring(z.read(name)).iter('{%s}row' % ns['m']):
            cells = []
            for c in row.findall('m:c', ns):
                v = c.find('m:v', ns); inline = c.find('m:is', ns)
                val = (shared[int(v.text)] if c.get('t') == 's' and v is not None else
                       ''.join(t.text or '' for t in inline.iter('{%s}t' % ns['m'])) if inline is not None else
                       (v.text if v is not None else ''))
                if val: cells.append(val); lines.append(f"{sheet}!{c.get('r')}: {val}")
            if cells: rows_out.append(cells)
    return T.Page('\n'.join(lines), '', [{'caption': 'xlsx', 'heading': '', 'rows': rows_out}], [], [])


class Run:
    """One crawl run directory: manifest.jsonl + pages/."""
    def __init__(self, run_dir: Path):
        self.dir = Path(run_dir); (self.dir / 'pages').mkdir(parents=True, exist_ok=True)
        self.manifest = self.dir / 'manifest.jsonl'; self.lock = threading.Lock()

    def entries(self):
        if not self.manifest.exists(): return []
        return [json.loads(l) for l in self.manifest.read_text(encoding='utf-8').splitlines() if l.strip()]

    def record(self, entry):
        with self.lock, self.manifest.open('a', encoding='utf-8') as f:
            f.write(json.dumps(entry, sort_keys=True, ensure_ascii=False) + '\n')

    def save_page(self, sha, kind, page, links):
        path = self.dir / 'pages' / f'{sha[:20]}.json.gz'
        if not path.exists():
            data = {'kind': kind, 'title': page.title, 'headings': page.headings, 'text': page.text,
                    'tables': page.tables, 'links': links}
            with gzip.open(path, 'wt', encoding='utf-8') as f: json.dump(data, f, ensure_ascii=False)
        return path.name

    def load_page(self, name):
        with gzip.open(self.dir / 'pages' / name, 'rt', encoding='utf-8') as f:
            d = json.load(f)
        return T.Page(d['text'], d['title'], d['tables'], [tuple(x) for x in d.get('links', [])], d['headings']), d


def crawl_institution(inst, run: Run, fetcher: Fetcher, budget=45, max_depth=3, log=print, program_budget=40):
    key = inst['institution_key']
    allowed = set(inst.get('allowed_domains') or [inst.get('domain')]) - {None}
    follow_all = set(inst.get('follow_all_domains') or [])
    done = {e['url'] for e in run.entries() if e.get('institution_key') == key}
    frontier, queued = [], set()

    def push(url, score, depth, via):
        url = url.split('#')[0]
        host = urlsplit(url).netloc
        if (not url.startswith('https://') and not url.startswith('http://')) or url in queued or depth > max_depth: return
        if registrable_domain(host) not in allowed or score < 0: return
        queued.add(url); heapq.heappush(frontier, (-score, depth, url, via))

    for label, url in inst.get('seeds', {}).items():
        if label != 'net_price': push(url, 1000, 0, 'seed:' + label)
    for url in inst.get('existing_sources', []):
        push(url, 900, 0, 'existing_source')
    for e in run.entries():  # Resume: re-expand links from pages already stored for this institution.
        if e.get('institution_key') == key and e.get('page_file') and e.get('depth', 0) < max_depth:
            _, d = run.load_page(e['page_file'])
            for url, score in d.get('links', []): push(url, score, e['depth'] + 1, e['url'])

    fetched = sum(1 for e in run.entries() if e.get('institution_key') == key)
    programs = sum(1 for e in run.entries() if e.get('institution_key') == key and topics.is_program_page(e.get('url', '')))
    retried = set()
    while frontier and fetched < budget:
        neg, depth, url, via = heapq.heappop(frontier)
        if url in done: continue
        if topics.is_program_page(url):
            if programs >= program_budget: continue  # catalog program pages have their own cap
            programs += 1
        done.add(url); fetched += 1
        try:
            meta, body = fetcher.fetch(url)
        except Exception as exc:  # A fetch bug must not stop the institution or the run.
            meta, body = {'status': None, 'error': f'fetch_exception:{type(exc).__name__}: {exc}'[:300]}, None
        entry = {'institution_key': key, 'url': url, 'depth': depth, 'via': via, 'fetched_at': now(), **meta}
        if meta.get('error') in ('blocked_bot_challenge', 'http_429') and url not in retried:
            retried.add(url); done.discard(url)  # once more, after the host's backoff delay
            heapq.heappush(frontier, (neg + 5, depth, url, via))
            entry['will_retry'] = True
        if body is not None:
            try:
                kind, page = parse_document(meta.get('final_url') or url, meta.get('content_type'), body)
            except Exception as exc:
                kind, page = 'error', None
                entry['error'] = f'parse_exception:{type(exc).__name__}: {exc}'[:300]
            entry['kind'] = kind
            if page is None:
                entry['error'] = 'unparsed_' + kind
            else:
                links = []
                for href, anchor in page.links:
                    s = topics.link_score(href, anchor)
                    if s == 0 and registrable_domain(urlsplit(href).netloc) in follow_all and not topics.EXCLUDE.search(href):
                        s = 1  # dedicated policy sites (e.g. a state transfer-pathway site): every page is relevant
                    if s > 0 and registrable_domain(urlsplit(href).netloc) in allowed:
                        links.append((href, s))
                entry['title'] = page.title[:200]
                entry['topics'] = topics.page_topics(page.title, page.headings, page.text)
                entry['year_labels'] = T.year_labels(page.text[:50000])
                entry['page_file'] = run.save_page(meta['sha256'], kind, page, links)
                for href, s in links: push(href, s, depth + 1, url)
        run.record(entry)
    log(f'{key}: {fetched} fetched, {len(frontier)} left in frontier')
    return fetched


def crawl(registry, run_dir, only=None, budget=45, workers=8, delay=1.0, fetcher=None, log=print, program_budget=40):
    run = Run(run_dir)
    fetcher = fetcher or Fetcher(delay=delay)
    targets = [i for i in registry['institutions'] if not only or i['institution_key'] in only or i['folder'] in only]
    state_inst = {'institution_key': f"state-{registry['state']}", 'seeds': {s['label']: s['url'] for s in registry.get('state_sources', [])},
                  'follow_all_domains': sorted({registrable_domain(urlsplit(s['url']).netloc) for s in registry.get('state_sources', []) if s.get('follow_all')}),
                  'allowed_domains': sorted({registrable_domain(urlsplit(s['url']).netloc) for s in registry.get('state_sources', [])}),
                  'existing_sources': []}
    if state_inst['seeds'] and not only: targets.append(state_inst)
    failures = []

    def one(inst):
        try:
            b = budget * 3 if inst['institution_key'].startswith('state-') else budget  # statewide sources cover every school
            return crawl_institution(inst, run, fetcher, budget=b, log=log, program_budget=program_budget)
        except Exception as exc:  # Isolate institutions: record the failure and keep going.
            failures.append(inst['institution_key'])
            run.record({'institution_key': inst['institution_key'], 'url': '', 'fetched_at': now(),
                        'error': f'institution_exception:{type(exc).__name__}: {exc}'[:300]})
            log(f"{inst['institution_key']}: crawl stopped by {type(exc).__name__}: {exc}")
    with ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(one, targets))
    if failures: log(f'{len(failures)} institutions stopped early (resume to continue): {failures}')
    return run
