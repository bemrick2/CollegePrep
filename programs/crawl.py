"""Targeted program-depth retrieval for `programs/targets/<STATE>.json`.

Unlike the national first-pass crawl (topic-ranked, ~45 pages per school), this crawl is driven by
the catalog platform: it enumerates the current catalog's complete program list and program pages,
degree-map indexes and their documents, and the program-admission / undeclared / change-of-major /
major-scholarship pages a reviewer named. Each fetched URL is recorded with a `role`.

Reused unchanged from `pipeline/crawl.py`: Fetcher (robots.txt, per-host delay, challenge backoff;
challenges are recorded, never evaded), Run (manifest.jsonl + content-addressed parsed pages),
parse_document and requote. The crawl is resumable: URLs already in the manifest are skipped.

JavaScript-rendered catalogs (Coursedog, Kuali) are fetched through a headless browser only when a
target says `"render": "browser"`. Rendering is not challenge evasion: robots.txt is still honoured
and a challenge or error page is recorded as such.
"""
from __future__ import annotations
import hashlib, json, re, threading
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlsplit, parse_qs

from pipeline import text as T
from pipeline.crawl import Fetcher, HostGate, Run, parse_document, requote, now
from pipeline.registry import registrable_domain

ROLES = ('catalog_home', 'catalog_nav', 'program_list', 'program_page', 'degree_map_index', 'degree_map',
         'policy', 'policy_link', 'state_source', 'discover')

POLICY_LINK = re.compile(
    r'(direct[\s-]*admi|admission[s]?\s+(to|into)\s+(the\s+)?(major|program|college|school|nursing|engineering|business)|'
    r'pre[\s-]?(nursing|engineering|business|major|professional)|progression|upper[\s-]*division\s+admission|'
    r'apply\s+to\s+the\s+(major|program)|undeclared|undecided|exploratory|exploring\s+majors?|change\s+(of|your)\s+major|'
    r'changing\s+majors?|declar(e|ing)\s+(a|your)\s+major|internal\s+transfer|intra[\s-]*university|major\s+change|'
    r'four[\s-]*year\s+plan|4[\s-]*year\s+plan|degree\s+maps?|academic\s+maps?|program\s+maps?|plans?\s+of\s+study|'
    r'scholarships?)', re.I)
DISCOVER_LINK = re.compile(r'(catalog|catalogue|bulletin|majors|degrees|programs|academics)', re.I)
MAP_ANCHOR = re.compile(r'\b((academic|degree|program|major)\s+maps?|four[\s-]*year\s+(degree\s+)?plans?|4[\s-]*year\s+plans?|plans?\s+of\s+study|clear\s+paths?|finish\s+in\s+four|degree\s+plans?|curriculum\s+(guides?|sheets?|maps?)|check\s*sheets?)\b', re.I)
MAP_URL = re.compile(r'(academic|degree|program)[-_]?maps?|four[-_]?year[-_]?plan|4[-_]?year[-_]?plan|plan[-_]?of[-_]?study|clear[-_]?path|checksheet', re.I)
DEGREE_MAP_LINK = re.compile(r'(map|plan|path|pathway|four[\s_-]*year|4[\s_-]*year|finish|sequence|curricul|worksheet|checksheet|flowchart)', re.I)
SKIP_PATH = re.compile(r'/(search|course-search|courses?|coursesaz|azindex|coursesofinstruction|courses-of-instruction|archive|archives|pdf|print|login|calendar)(/|$)|'
                       r'preview_course|preview_entity|acalog-api|\.(jpg|png|gif|css|js|zip|docx?)$', re.I)


def host_of(url):
    h = urlsplit(url).netloc.lower().split(':')[0]
    return h[4:] if h.startswith('www.') else h


def in_scope(target, url):
    """Official hosts only: the institution's registrable domains plus explicitly listed catalog hosts."""
    h = host_of(url)
    if any(h == x or h.endswith('.' + x) for x in target.get('hosts', [])): return True
    return registrable_domain(h) in set(target.get('domains', []))


def excluded(target, url):
    """A page under one of the catalog's `exclude_paths` belongs to another institution sharing the catalog (UNH's catalog
    prints UNH Manchester and the College of Professional Studies under /undergraduate/professional-studies/)."""
    path = urlsplit(url or '').path
    return any(path.startswith(x) for x in (target.get('catalog') or {}).get('exclude_paths', []))


def canonical(url):
    url = requote(url.split('#')[0])
    if 'preview_program.php' in url or 'content.php' in url:  # Acalog: returnto/print params duplicate pages
        p = urlsplit(url); q = parse_qs(p.query)
        keep = '&'.join(f'{k}={q[k][0]}' for k in ('catoid', 'poid', 'navoid') if k in q)
        url = f'{p.scheme}://{p.netloc}{p.path}?{keep}'
    return url


def program_rule(target):
    """Predicate for a current-catalog program page URL, by platform."""
    cat = target.get('catalog') or {}
    plat = cat.get('platform'); custom = cat.get('program_link')
    if custom:
        rx = re.compile(custom); return lambda u: bool(rx.search(u)) and not SKIP_PATH.search(urlsplit(u).path)
    if plat == 'acalog':
        rx = re.compile(r'preview_program\.php\?catoid=%s&poid=\d+' % re.escape(str(cat.get('catoid'))))
        return lambda u: bool(rx.search(u))
    if plat in ('courseleaf', 'smartcatalog', 'coursedog', 'kuali', 'drupal'):
        prefix = cat.get('path_prefix', '/'); chost = host_of(cat.get('home', ''))
        def rule(u):
            p = urlsplit(u)
            if host_of(u) != chost or not p.path.startswith(prefix) or SKIP_PATH.search(p.path) or excluded(target, u): return False
            rest = p.path[len(prefix):].strip('/')
            return rest.count('/') >= (cat.get('min_depth', 1))
        return rule
    return lambda u: False


def nav_rule(target):
    """Catalog navigation pages worth expanding to find program lists (Acalog content.php of the current catoid,
    SmartCatalog / Coursedog section pages under the current catalog's path)."""
    cat = target.get('catalog') or {}
    if cat.get('platform') == 'acalog':
        rx = re.compile(r'content\.php\?catoid=%s&navoid=\d+' % re.escape(str(cat.get('catoid'))))
        return lambda u: bool(rx.search(u))
    if cat.get('platform') == 'smartcatalog':
        prefix = cat.get('path_prefix', '/'); chost = host_of(cat.get('home', ''))
        return lambda u: host_of(u) == chost and urlsplit(u).path.startswith(prefix) and not SKIP_PATH.search(urlsplit(u).path)
    if cat.get('platform') == 'courseleaf' and cat.get('nav_prefix'):
        # a CourseLeaf catalog without a sitemap (MSState): its college and department pages under the undergraduate
        # section link the program pages
        prefix = cat['nav_prefix']; chost = host_of(cat.get('home', ''))
        return lambda u: host_of(u) == chost and urlsplit(u).path.startswith(prefix) and not SKIP_PATH.search(urlsplit(u).path)
    return lambda u: False


class BrowserFetcher:
    """Rendered HTML for JavaScript catalogs via Playwright (installed only in the Actions job).
    Same contract as pipeline.crawl.Fetcher.fetch: (meta, body). Robots and politeness come from `base`."""
    def __init__(self, base: Fetcher):
        self.base = base; self.lock = threading.Lock(); self._pw = None; self._browser = None; self.last_feeds = []

    def _ensure(self):
        if self._browser is None:
            from playwright.sync_api import sync_playwright  # noqa: deferred import, optional dependency
            self._pw = sync_playwright().start()
            self._browser = self._pw.chromium.launch()

    def fetch(self, url):
        if not self.base.allowed(url):
            return {'status': None, 'error': self.base.refusal(url)}, None
        host = urlsplit(url).netloc.lower()
        with self.lock:  # one browser page at a time keeps the load equal to a person reading
            entry = self.base.gate.wait(host)
            try:
                self._ensure()
                page = self._browser.new_page(user_agent='CollegePrepResearchBot/1.0 (+https://github.com/bemrick2/collegeprep; official-source research)')
                feeds = []
                def keep(r):  # the catalog's own JSON data feed (Coursedog/Kuali), as the page itself loaded it
                    try:
                        h = urlsplit(r.url).netloc.lower()
                        catalog_backend = h.endswith(('coursedog.com', 'kuali.co')) or h == urlsplit(url).netloc.lower()
                        if 'json' in (r.headers.get('content-type') or '') and catalog_backend and len(feeds) < 60:
                            b = r.body()
                            if len(b) < 8 * 1024 * 1024: feeds.append((r.url, r.status, b, r.request.method, r.request.post_data))
                    except Exception:
                        pass
                page.on('response', keep)
                try:
                    resp = page.goto(url, wait_until='domcontentloaded', timeout=60000)
                    try:  # JavaScript catalogs keep connections open; settle briefly instead of waiting for idle
                        page.wait_for_load_state('networkidle', timeout=15000)
                    except Exception:
                        pass
                    page.wait_for_timeout(2500)
                    status = resp.status if resp else None
                    body = page.content().encode('utf-8')
                    final = page.url
                    self.last_feeds = feeds
                finally:
                    page.close()
            except Exception as exc:
                return {'status': None, 'error': f'render_exception:{type(exc).__name__}: {exc}'[:300]}, None
            finally:
                HostGate.done(entry)
        meta = {'status': status, 'final_url': final, 'content_type': 'text/html; rendered', 'bytes': len(body), 'rendered': True}
        if status != 200:
            meta['error'] = 'blocked_forbidden' if status == 403 else f'http_{status}'
            return meta, None
        meta['sha256'] = hashlib.sha256(body).hexdigest()
        return meta, body

    def close(self):
        if self._browser: self._browser.close(); self._pw.stop()


def crawl_target(target, run: Run, fetcher, browser=None, log=print, caps=None):
    caps = {'program_page': 450, 'catalog_nav': 30, 'degree_map': 250, 'degree_map_index': 300, 'policy_link': 40, 'discover': 25, 'catalog_pdf': 2, **(caps or {}),
            # discovery only locates the catalog: degree maps and policy links wait for the catalog run
            **({'degree_map': 0, 'degree_map_index': 0, 'policy_link': 0} if target.get('mode') == 'discover' else {}),
            **(target.get('caps') or {})}
    key = target['institution_key']
    seen = {e['url'] for e in run.entries() if e.get('institution_key') == key}
    counts = {}
    for e in run.entries():
        if e.get('institution_key') == key: counts[e.get('role')] = counts.get(e.get('role'), 0) + 1
    is_program, is_nav = program_rule(target), nav_rule(target)
    render = target.get('render') == 'browser' and browser is not None
    cat = target.get('catalog') or {}
    chost = host_of(cat.get('home', '')) if cat.get('home') else None
    if target.get('crawl_delay') and chost:  # a slower fixed pace for catalog hosts that rate-limit (never shortens a robots delay)
        fetcher.gate.set_delay(urlsplit(cat['home']).netloc.lower(), target['crawl_delay'])
    queue = []  # FIFO by stage keeps lists before pages

    def push(url, role, via, depth=0):
        url = canonical(url)
        if not url.startswith('https://') and not url.startswith('http://'): return
        if url in seen or not in_scope(target, url): return
        if role in caps and counts.get(role, 0) >= caps[role]: return
        seen.add(url); counts[role] = counts.get(role, 0) + 1
        queue.append((url, role, via, depth))

    if target.get('refetch'):
        # A re-fetch run (issue #129): exactly these already-reviewed program pages, nothing discovered from them, so the
        # new capture (Course List superscripts) is compared page for page with the stored one. A program page's links are
        # never followed (expand), so nothing else is fetched.
        for u in target['refetch']: push(u, 'program_page', 'refetch')
    elif cat.get('home') and not (cat.get('platform') == 'pdf' and cat['home'] in cat.get('catalog_pdfs', [])):
        # a catalog that is one PDF is fetched only as role catalog_pdf (the large-file cap; Alaska Bible College's 2026-2027
        # catalog is 15.7 MB), so it is not first refused as an over-size catalog_home page
        push(cat['home'], 'catalog_home', 'target')
    if not target.get('refetch'):
        if cat.get('platform') == 'courseleaf' and chost:  # CourseLeaf publishes /sitemap.xml: every catalog page
            push(f'https://{chost}/sitemap.xml', 'sitemap', 'target')
        for u in cat.get('program_lists', []): push(u, 'program_list', 'target')
        for u in target.get('degree_maps', []): push(u, 'degree_map_index', 'target')
        for u in (target.get('map_sources') or {}).get('lists', []): push(u, 'map_list', 'target')
        for u in cat.get('catalog_pdfs', []): push(u, 'catalog_pdf', 'target')  # a catalog's own full PDF (fetched up to 80 MB)
        for u in target.get('policy', []): push(u, 'policy', 'target')
        for u in target.get('discover', []): push(u, 'discover', 'target')
    # Resume: re-expand stored pages' links
    for e in run.entries():
        if e.get('institution_key') == key and e.get('page_file'):
            _, d = run.load_page(e['page_file'])
            expand(target, e['role'], e['url'], [tuple(x) for x in d.get('links', [])], push, is_program, is_nav, e.get('depth', 0))

    i = 0
    while i < len(queue):
        url, role, via, depth = queue[i]; i += 1
        use_browser = render and chost and host_of(url) == chost and role in ('catalog_home', 'catalog_nav', 'program_list', 'program_page')
        try:
            if role == 'catalog_pdf':
                from .feeds import fetch_large
                meta, body = fetch_large(fetcher, url)
            else:
                meta, body = (browser if use_browser else fetcher).fetch(url)
        except Exception as exc:
            meta, body = {'status': None, 'error': f'fetch_exception:{type(exc).__name__}: {exc}'[:300]}, None
        entry = {'institution_key': key, 'url': url, 'role': role, 'via': via, 'depth': depth, 'fetched_at': now(), **meta}
        if use_browser and body is not None and role in ('program_list', 'catalog_home', 'program_page'):
            for furl, fstatus, fbody, fmethod, fpost in getattr(browser, 'last_feeds', []):
                if fstatus != 200: continue
                fsha = hashlib.sha256(fbody).hexdigest()
                try:
                    text = json.dumps(json.loads(fbody), indent=0, ensure_ascii=False)
                except ValueError:
                    continue
                fe = {'institution_key': key, 'url': furl, 'role': 'catalog_feed', 'via': url, 'depth': depth + 1, 'fetched_at': now(),
                      'status': 200, 'sha256': fsha, 'bytes': len(fbody), 'kind': 'json', 'content_type': 'application/json',
                      'request_method': fmethod, **({'request_body': fpost[:4000]} if fpost else {})}
                fe['page_file'] = run.save_page(fsha, 'json', T.Page(text, 'catalog data feed', [], [], []), [])
                run.record(fe)
                # Coursedog reports the catalog's own generated full-catalog PDF ("Download Catalog as PDF")
                for m in re.finditer(r'"url":\s*"(https://coursedog-pdfs-public-prod\.s3\.[a-z0-9-]+\.amazonaws\.com/[^"]+\.pdf)"', text):
                    if '"type": "catalog"' in text: push(m.group(1), 'catalog_pdf', furl, depth + 1)
            browser.last_feeds = []
        if body is not None and role == 'sitemap':  # the catalog's own sitemap: candidate program pages by URL
            locs = [canonical(u) for u in re.findall(rb'<loc>\s*(https?://[^<\s]+)\s*</loc>', body)[:20000] for u in [u.decode('utf-8', 'replace')]]
            links = [(u, '') for u in locs if in_scope(target, u)]
            entry.update(kind='xml', page_file=run.save_page(meta['sha256'], 'xml', T.Page('\n'.join(locs), 'sitemap', [], links, []), links), urls=len(locs))
            expand(target, role, url, links, push, is_program, is_nav, depth)
            run.record(entry); continue
        if body is not None:
            try:
                kind, page = parse_document(meta.get('final_url') or url, meta.get('content_type'), body)
            except Exception as exc:
                kind, page = 'error', None; entry['error'] = f'parse_exception:{type(exc).__name__}: {exc}'[:300]
            entry['kind'] = kind
            if page is None:
                entry.setdefault('error', 'unparsed_' + kind)
            else:
                entry['title'] = (page.title or '')[:200]
                links = [(canonical(h), (a or '')[:200]) for h, a in page.links if in_scope(target, h)]
                entry['page_file'] = run.save_page(meta['sha256'], kind, page, links)
                expand(target, role, url, links, push, is_program, is_nav, depth)
                if kind == 'html' and role == 'program_page' and (target.get('catalog') or {}).get('platform') == 'courseleaf':
                    store_courselists(run, key, url, body, depth)
                if kind == 'html' and role == 'program_page' and (target.get('catalog') or {}).get('platform') == 'smartcatalog':
                    store_outline(run, key, url, body, depth)
                if kind == 'pdf' and role == 'degree_map' and target.get('pdf_layout'):
                    store_pdf_layout(run, key, url, body, depth)
        run.record(entry)
    log(f"{key}: {len(queue)} fetched {dict(sorted(counts.items()))}")
    return len(queue)


def store_courselists(run, key, url, body, depth):
    """The page's CourseLeaf Course List tables with row classes and indentation (programs.courselist_html), stored as
    their own JSON document (url + '#courselist') derived from the same fetched bytes."""
    from .courselist_html import course_lists, to_text
    tables = course_lists(body)
    if not tables: return
    text = to_text(tables); sha = hashlib.sha256(text.encode()).hexdigest()
    run.record({'institution_key': key, 'url': url + '#courselist', 'role': 'courselist', 'via': url, 'depth': depth, 'fetched_at': now(),
                'status': 200, 'sha256': sha, 'source_sha256': hashlib.sha256(body).hexdigest(), 'kind': 'json', 'tables': len(tables),
                'page_file': run.save_page(sha, 'json', T.Page(text, 'CourseLeaf course lists', [], [], []), [])})


def store_pdf_layout(run, key, url, body, depth):
    """Word positions of a PDF (poppler `pdftotext -bbox-layout`), stored as their own JSON document (url + '#layout'):
    two-column degree maps need x positions to keep the columns apart."""
    from .pdf_layout import words
    pages = words(body)
    if not pages: return
    text = json.dumps(pages, ensure_ascii=False); sha = hashlib.sha256(text.encode()).hexdigest()
    run.record({'institution_key': key, 'url': url + '#layout', 'role': 'pdf_layout', 'via': url, 'depth': depth, 'fetched_at': now(),
                'status': 200, 'sha256': sha, 'source_sha256': hashlib.sha256(body).hexdigest(), 'kind': 'json',
                'page_file': run.save_page(sha, 'json', T.Page(text, 'pdf word layout', [], [], []), [])})


def store_outline(run, key, url, body, depth):
    """The page's block outline with list nesting (programs.courselist_html.outline), stored as its own JSON document
    (url + '#outline') derived from the same fetched bytes."""
    from .courselist_html import outline
    blocks = outline(body)
    if not blocks: return
    text = json.dumps(blocks, ensure_ascii=False, indent=0); sha = hashlib.sha256(text.encode()).hexdigest()
    run.record({'institution_key': key, 'url': url + '#outline', 'role': 'outline', 'via': url, 'depth': depth, 'fetched_at': now(),
                'status': 200, 'sha256': sha, 'source_sha256': hashlib.sha256(body).hexdigest(), 'kind': 'json', 'blocks': len(blocks),
                'page_file': run.save_page(sha, 'json', T.Page(text, 'page outline', [], [], []), [])})


NOT_BACHELOR_ANCHOR = re.compile(r'\b(minor|certificate|option|concentration|graduate|master|doctor|ph\.?\s?d|m\.?\s?s\.?|m\.?\s?a\.?|mba|'
                                 r'm\.?\s?ed|ed\.?\s?d|dnp|post[- ]?bacc|endorsement|licensure|courses?)\b', re.I)
BACHELOR_ANCHOR = re.compile(r'\b(B\.?\s?[A-Z]{1,4}\b\.?|bachelor|undergraduate\s+major|H?BA\b|H?BS\b)', re.I)


def anchor_rank(anchor):
    """0: names a bachelor's degree; 1: unlabeled; 2: names a minor, certificate, option or graduate award.
    Ordering only: program pages are fetched bachelor-first so the per-school cap is spent on majors."""
    a = anchor or ''
    if BACHELOR_ANCHOR.search(a) and not re.search(r'\b(minor|certificate|option)\b', a, re.I): return 0
    return 2 if NOT_BACHELOR_ANCHOR.search(a) else 1


def expand(target, role, url, links, push, is_program, is_nav, depth):
    """Which links of a fetched page to follow, by the page's role."""
    cat = target.get('catalog') or {}
    lists_given = bool(cat.get('program_lists'))
    if role in ('catalog_home', 'catalog_nav', 'program_list'):
        tag = cat.get('list_filter')  # a branch campus on its parent's catalog: only the rows tagged with this campus
        progs = [(anchor_rank(a), h) for h, a in links if is_program(h) and (not tag or role != 'program_list' or tag in (a or ''))]
        for rank, h in sorted(progs, key=lambda x: x[0]):
            # A configured list page is the authority for which pages are programs; elsewhere only bachelor/unlabeled.
            if rank < 2 and (role == 'program_list' or not lists_given or cat.get('platform') == 'acalog'):
                push(h, 'program_page', url, depth + 1)
        if not (lists_given and cat.get('platform') != 'acalog'):
            for h, a in links:
                if not is_program(h) and is_nav(h) and depth < 3: push(h, 'catalog_nav', url, depth + 1)
        return
    if role == 'sitemap':
        # CourseLeaf program pages end in the award ('.../biology-bs/', '.../history-major/'); bachelor's first, never minors,
        # certificates or graduate pages. The page itself must still print its award and year to become a record.
        # UF writes them 'ACT_BSAC' / 'AEC_BS'; a one-word segment ('badm', 'busi': course subjects) is never an award.
        bach, other = [], []
        if cat.get('sitemap_program'):  # a catalog whose program pages carry no award in the URL (uark department pages)
            for h, _ in links:
                if is_program(h) and re.search(cat['sitemap_program'], h): push(h, 'program_page', url, depth + 1)
            return
        for h, _ in links:
            seg = urlsplit(h).path.rstrip('/').rsplit('/', 1)[-1].lower()
            if not is_program(h) or re.search(r'(^|/)(grad|graduate|graduate-school)(/|$)', urlsplit(h).path.lower()): continue
            if not re.search(r'[-_]', seg): continue
            if re.search(r'(^|[-_])(minor|certificate|cert|ms|ma|mba|mfa|med|phd|edd|dnp|pmc|aas|as|aa)([-_]|$)', seg): continue
            if re.search(r'(^|[-_])(b[a-z]{1,5}|major)([-_]|$)', seg): bach.append(h)
        for h in bach: push(h, 'program_page', url, depth + 1)
        return
    if role in ('policy', 'policy_link', 'discover'):
        # Degree-map indexes and plan documents are often linked from advising or college pages, not the catalog.
        for href, anchor in links:
            path = urlsplit(href).path.lower()
            if path.endswith('.pdf') and (MAP_ANCHOR.search(anchor or '') or MAP_URL.search(path)):
                push(href, 'degree_map', url, depth + 1)
            elif MAP_ANCHOR.search(anchor or '') and depth < 2:
                push(href, 'degree_map_index', url, depth + 1)
    if role == 'map_list':  # a school's own program directory whose program pages link that program's degree map
        ms = target.get('map_sources') or {}
        for href, anchor in links:
            if re.search(ms.get('page_link', r'^$'), href): push(href, 'degree_map_index', url, depth + 1)
        return
    for href, anchor in links:
        if role == 'degree_map_index':
            path = urlsplit(href).path.lower()
            if (path.endswith('.pdf') and (DEGREE_MAP_LINK.search(href) or DEGREE_MAP_LINK.search(anchor or '')
                                           or target.get('degree_map_any_pdf'))) or \
               (target.get('degree_map_link') and re.search(target['degree_map_link'], href)):
                push(href, 'degree_map', url, depth + 1)
        elif role == 'policy' and depth == 0:
            if POLICY_LINK.search(anchor or '') or POLICY_LINK.search(urlsplit(href).path.replace('-', ' ')):
                push(href, 'policy_link', url, depth + 1)
        elif role == 'discover' and depth < 1:
            if DISCOVER_LINK.search(anchor or '') or DISCOVER_LINK.search(urlsplit(href).netloc + urlsplit(href).path):
                push(href, 'discover', url, depth + 1)
            elif POLICY_LINK.search(anchor or ''):
                push(href, 'policy_link', url, depth + 1)


def crawl(targets, run_dir, only=None, workers=8, delay=1.0, log=print, use_browser=True, adapters_only=False, policy_only=False):
    run = Run(run_dir)
    fetcher = Fetcher(delay=delay)
    sel = [t for t in targets['institutions'] if not only or t['institution_key'] in only or t['folder'] in only]
    if policy_only:  # a follow-up run for review: only the targets' policy pages (admission, declaration), no catalog crawl
        sel = [{**t, 'catalog': {}, 'discover': [], 'render': None} for t in sel]
    browser = None
    if use_browser and any(t.get('render') == 'browser' for t in sel):
        try:
            import playwright  # noqa: F401
            browser = BrowserFetcher(fetcher)
        except ImportError:
            log('playwright not installed: browser-rendered targets fetch their static HTML only')
    adapters = [s for s in targets.get('state_sources', []) if s.get('adapter')]
    plain_sources = [s for s in targets.get('state_sources', []) if not s.get('adapter')]
    state = {'institution_key': f"state-{targets['state']}", 'folder': 'state', 'domains': [],
             'hosts': sorted({host_of(s['url']) for s in plain_sources}),
             'policy': [s['url'] for s in plain_sources]}
    if state['policy'] and not only: sel = sel + [state]
    if adapters_only: sel = []

    def one(t):
        try:
            return crawl_target(t, run, fetcher, browser=browser, log=log)
        except Exception as exc:
            run.record({'institution_key': t['institution_key'], 'url': '', 'role': 'error', 'fetched_at': now(),
                        'error': f'institution_exception:{type(exc).__name__}: {exc}'[:300]})
            log(f"{t['institution_key']}: stopped by {type(exc).__name__}: {exc}")
    # Browser-rendered targets share one browser; run them after the static ones, sequentially.
    static = [t for t in sel if not (t.get('render') == 'browser' and browser)]
    rendered = [t for t in sel if t.get('render') == 'browser' and browser]
    with ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(one, static))
    for t in rendered: one(t)
    from . import feeds
    for t in sel:
        if t.get('render') == 'browser':
            try:
                feeds.complete(t, run, fetcher, log=log)
            except Exception as exc:
                run.record({'institution_key': t['institution_key'], 'url': '', 'role': 'error', 'fetched_at': now(),
                            'error': f'feed_exception:{type(exc).__name__}: {exc}'[:300]})
    for a in adapters:
        if a['adapter'] == 'thec_api':
            from . import thec
            names = {t['institution_key']: t['name'] for t in targets['institutions']
                     if t.get('control') == 'public' and (not only or t['institution_key'] in only or t['folder'] in only)}
            try:
                thec.crawl(run, fetcher, names, log=log)
            except Exception as exc:
                run.record({'institution_key': f"state-{targets['state']}", 'url': a['url'], 'role': 'error', 'fetched_at': now(),
                            'error': f'adapter_exception:{type(exc).__name__}: {exc}'[:300]})
    if browser: browser.close()
    return run
