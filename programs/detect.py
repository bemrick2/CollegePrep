"""Catalog platform detection from a discovery run (`programs detect --state XX --run programs/runs/XX/<id>`).

A discovery run fetches each institution's official website and likely catalog hosts (mode=discover targets). This
reads only what the run stored and proposes a catalog configuration per institution when a known platform is
recognisable from official links:

  * Acalog (Modern Campus): links to <host>/index.php?catoid=N / content.php?catoid=N / preview_program.php?catoid=N.
    The current catalog is the catoid the catalog's own home page links most, among catalogs whose link text or the
    page carries the newest academic-year label; program lists are its navoid pages whose link text names programs,
    degrees or majors.
  * SmartCatalog: <school>.smartcatalogiq.com/<lang>/<year-path>/...: the newest year path linked.
  * Kuali: <school>.kuali.co/catalog...
  * CourseLeaf: catalog hosts linking /programs-az/, /azindex/ or /<level>/programs/ (program list) pages.
  * Catalog PDF: an official .pdf link whose text or file name says catalog/bulletin and carries an academic year.

Output: programs/targets/configs/<STATE>.json {folder: {catalog: {...}, detected: {url, sha256, reason}}}. Nothing
here is a fact about programs; a wrong guess only means the catalog run finds no current-year program pages (every
record still needs a printed year and award on the program page). Existing entries in the file are kept unless
--refresh is given, so reviewed corrections survive re-detection.
"""
from __future__ import annotations
import gzip, json, re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit, parse_qs

ROOT = Path(__file__).resolve().parent.parent
YEAR = re.compile(r'\b(20\d{2})\s*[-–/]\s*(20\d{2}|\d{2})\b')
LIST_TEXT = re.compile(r'\b(programs?|degrees?|majors?)\b', re.I)
NOT_LIST = re.compile(r'\b(graduate|minors?|certificates?|archived?|course descriptions?)\b', re.I)
CATALOG_WORD = re.compile(r'catalog|catalogue|bulletin', re.I)


def _years(text):
    out = set()
    for a, b in YEAR.findall(text or ''):
        b = b if len(b) == 4 else a[:2] + b
        if int(b) == int(a) + 1: out.add(int(a))
    return out


def pages(run_dir):
    run = Path(run_dir)
    for line in (run / 'manifest.jsonl').read_text().splitlines():
        m = json.loads(line)
        if not m.get('page_file'): continue
        try: p = json.load(gzip.open(run / 'pages' / m['page_file']))
        except (OSError, ValueError): continue
        yield m, p


def detect_institution(entries):
    """entries: [(manifest, page)] for one institution -> (config, evidence) or (None, reason)."""
    acalog = defaultdict(Counter); acalog_year = defaultdict(lambda: defaultdict(set)); navs = defaultdict(dict)
    smart = Counter(); kuali = set(); courseleaf = defaultdict(set); pdfs = []; coursedog = Counter()
    for m, p in entries:
        text = (p.get('title') or '') + ' ' + (p.get('text') or '')[:4000]
        page_years = _years(text)
        for href, anchor in p.get('links', []):
            u = urlsplit(href); host = u.netloc.lower(); a = (anchor or '').strip()
            q = parse_qs(u.query)
            if re.search(r'/(index|content|preview_program|search_advanced)\.php$', u.path) and 'catoid' in q:
                cat = q['catoid'][0]
                if not cat.isdigit(): continue
                acalog[host][int(cat)] += 1
                acalog_year[host][int(cat)] |= _years(a)
                if m['url'].startswith(f'https://{host}') or m['url'].startswith(f'http://{host}'):
                    acalog_year[host][int(cat)] |= page_years
                if 'navoid' in q and LIST_TEXT.search(a) and not NOT_LIST.search(a):
                    navs[(host, int(cat))][int(q['navoid'][0])] = a
            elif host.endswith('.smartcatalogiq.com'):
                # /en/2026-2027/<catalog>/... or /en/2026/2026-27-undergraduate-catalogue/...
                ym = re.match(r'^/(?:([a-z]{2})/)?(20\d{2}(?:-20\d{2})?)/([^/]*(?:catalog|bulletin)[^/]*/)?', u.path, re.I)
                if ym: smart[(host, ym.group(1) or '', ym.group(2) + '/' + (ym.group(3) or '').rstrip('/'))] += 1
            elif host.endswith('.kuali.co'):
                kuali.add(host)
            elif host.startswith(('catalog.', 'catalogs.', 'bulletin.', 'undergrad', 'undergraduate.')) and re.match(r'^/programs/[A-Za-z0-9._-]+/?$', u.path):
                coursedog[host] += 1  # Coursedog program URLs: /programs/<code>
            elif host.startswith(('catalog.', 'catalogs.', 'bulletin.')) and re.search(r'/(programs-az|azindex|programs)/?$|/(undergraduate|undergrad)/programs?/?', u.path):
                courseleaf[host].add(f'https://{host}{u.path}')
            elif u.path.lower().endswith('.pdf') and CATALOG_WORD.search(a + ' ' + u.path) and not re.search(r'graduate|archive|handbook', a + u.path, re.I):
                ys = _years(a + ' ' + u.path)
                if ys: pdfs.append((max(ys), href, m))
    found = []  # (dated, cfg, why): a platform whose links carry a current year label wins over an undated one
    if acalog:
        host = max(acalog, key=lambda h: sum(acalog[h].values()))
        cats = acalog[host]
        dated = {c: max(ys) for c, ys in acalog_year[host].items() if ys}
        newest = max(dated.values()) if dated else None
        pool = [c for c, y in dated.items() if y == newest] or list(cats)
        cat = max(pool, key=lambda c: (cats[c], c))
        lists = sorted(navs.get((host, cat), {}))
        found.append((newest is not None, {'platform': 'acalog', 'home': f'https://{host}/index.php?catoid={cat}', 'catoid': cat,
                      'program_lists': [f'https://{host}/content.php?catoid={cat}&navoid={n}' for n in lists]},
                      f'Acalog catoid {cat} on {host}' + (f' (labelled {newest}-{newest + 1})' if newest else ' (no year label seen)')))
    if smart:
        (host, lang, ypath), _ = max(smart.items(), key=lambda kv: (kv[0][2], kv[1]))
        prefix = f"/{lang + '/' if lang else ''}{ypath.rstrip('/')}/"
        found.append((True, {'platform': 'smartcatalog', 'home': f'https://{host}{prefix}', 'path_prefix': prefix, 'min_depth': 1, 'program_lists': []},
                      f'SmartCatalog {host} newest year path {ypath}'))
    if coursedog:
        host, n = coursedog.most_common(1)[0]
        if n >= 3:
            found.append((False, {'platform': 'coursedog', 'home': f'https://{host}/', 'path_prefix': '/programs/', 'min_depth': 0,
                                  'program_lists': [f'https://{host}/programs'] + [f'https://{host}/programs?page={k}&pq=&sortBy=name' for k in range(2, 16)],
                                  'render': 'browser'}, f'Coursedog-style program URLs on {host} ({n} links)'))
    if kuali:
        host = sorted(kuali)[0]
        found.append((False, {'platform': 'kuali', 'home': f'https://{host}/catalog', 'path_prefix': '/catalog', 'min_depth': 0, 'program_lists': []}, f'Kuali {host}'))
    if courseleaf:
        host = max(courseleaf, key=lambda h: len(courseleaf[h]))
        found.append((False, {'platform': 'courseleaf', 'home': f'https://{host}/', 'path_prefix': '/', 'min_depth': 1, 'program_lists': sorted(courseleaf[host])[:3]},
                      f'CourseLeaf-style program list on {host}'))
    if pdfs:
        y, href, _ = max(pdfs, key=lambda x: x[0])
        found.append((True, {'platform': 'pdf', 'home': href, 'catalog_pdfs': [href]}, f'catalog PDF labelled {y}-{y + 1}'))
    if found:
        order = {'acalog': 0, 'smartcatalog': 1, 'coursedog': 2, 'kuali': 3, 'courseleaf': 4, 'pdf': 5}
        # undated Acalog links are usually a retired catalog host left behind after a platform change
        dated, cfg, why = sorted(found, key=lambda f: (not f[0] if f[1]['platform'] != 'pdf' else 1, order[f[1]['platform']]))[0]
        if cfg['platform'] == 'acalog' and not dated and any(f[1]['platform'] in ('coursedog', 'smartcatalog', 'kuali', 'courseleaf') for f in found):
            dated, cfg, why = next(f for f in found if f[1]['platform'] in ('smartcatalog', 'coursedog', 'kuali', 'courseleaf'))
        cfg = dict(cfg)
        if cfg.get('render'): cfg.pop('render'); return {**cfg, '_render': 'browser'}, why
        return cfg, why
    return None, 'no catalog platform recognised on stored pages'


def detect(state, run_dirs, refresh=False):
    by_inst = defaultdict(list)
    for d in run_dirs:
        for m, p in pages(d): by_inst[m.get('institution_key')].append((m, p))
    reg = {i['institution_key']: i for i in json.loads((ROOT / 'pipeline/registry' / f'{state}.json').read_text())['institutions'] if i['level'] == 'four_year'}
    path = ROOT / 'programs/targets/configs' / f'{state}.json'
    have = {} if refresh or not path.exists() else json.loads(path.read_text())
    out, misses = dict(have), {}
    for key, inst in sorted(reg.items(), key=lambda kv: kv[1]['folder']):
        if inst['folder'] in have and have[inst['folder']].get('reviewed'): continue
        cfg, why = detect_institution(by_inst.get(key, []))
        if cfg:
            render = cfg.pop('_render', None)
            out[inst['folder']] = {'catalog': cfg, 'detected': why, **({'render': render} if render else {})}
        else: misses[inst['folder']] = why
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=1, sort_keys=True) + '\n')
    plats = Counter(v['catalog']['platform'] for v in out.values())
    print(f'{state}: {len(out)} configured {dict(plats)}; {len(misses)} without a recognised catalog')
    return out, misses
