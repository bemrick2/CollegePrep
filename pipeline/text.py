"""Deterministic text primitives: HTML to text/tables/links, PDF to text, year labels, money.

Standard library only (PDF text uses the poppler `pdftotext` CLI when present), so repository CI
needs no extra packages. Nothing here guesses: unparseable values come back as None.
"""
from __future__ import annotations
import html, re, shutil, subprocess, tempfile
from html.parser import HTMLParser
from urllib.parse import urljoin, urldefrag

BLOCK = {'p', 'div', 'br', 'li', 'tr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'section', 'article',
         'header', 'footer', 'table', 'ul', 'ol', 'dt', 'dd', 'caption', 'blockquote', 'pre'}
SKIP = {'script', 'style', 'noscript', 'svg', 'template', 'iframe'}
CELL = {'td', 'th'}


class Page:
    """Parsed view of one fetched document."""
    def __init__(self, text: str, title: str = '', tables=None, links=None, headings=None):
        self.text = text
        self.title = title
        self.tables = tables or []      # list of {'caption','heading','rows': [[cell,...],...]}
        self.links = links or []        # list of (absolute_url, anchor_text)
        self.headings = headings or []  # list of heading strings in order

    @property
    def lines(self):
        return [l for l in (x.strip() for x in self.text.splitlines()) if l]


class _Parser(HTMLParser):
    def __init__(self, base_url):
        super().__init__(convert_charrefs=True)
        self.base = base_url; self.out = []; self.skip = 0; self.title = ''; self.in_title = False
        self.links = []; self.link = None; self.headings = []; self.heading = None
        self.tables = []; self.stack = []; self.last_heading = ''; self.year_heading = ''

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in SKIP: self.skip += 1; return
        if tag == 'base' and a.get('href'): self.base = urljoin(self.base, a['href'])
        if tag == 'title': self.in_title = True
        if tag in BLOCK: self.out.append('\n')
        if tag in CELL: self.out.append(' | ')
        if tag == 'a' and a.get('href'): self.link = [a['href'], []]
        if tag in {'h1', 'h2', 'h3', 'h4'}: self.heading = []
        if tag == 'table':
            # The text block right before a table often names it (accordion buttons, bold labels).
            prior = [l.strip() for l in ''.join(self.out[-60:]).split('\n') if l.strip()]
            lead = prior[-1][:200] if prior else ''
            self.stack.append({'caption': '', 'heading': self.last_heading, 'year_heading': self.year_heading,
                               'lead': lead, 'rows': [], 'row': None, 'cell': None})
        elif self.stack:
            t = self.stack[-1]
            if tag == 'tr': t['row'] = []
            elif tag in CELL:
                if t['row'] is None: t['row'] = []
                t['cell'] = []
            elif tag == 'caption': t['cell'] = []

    def handle_endtag(self, tag):
        if tag in SKIP: self.skip = max(0, self.skip - 1); return
        if tag == 'title': self.in_title = False
        if tag in BLOCK: self.out.append('\n')
        if tag == 'a' and self.link:
            href, text = self.link; self.link = None
            if not href.startswith(('mailto:', 'tel:', 'javascript:', '#')):
                self.links.append((urldefrag(urljoin(self.base, href.strip()))[0], squash(''.join(text))))
        if tag in {'h1', 'h2', 'h3', 'h4'} and self.heading is not None:
            h = squash(''.join(self.heading)); self.heading = None
            if h:
                self.headings.append(h); self.last_heading = h
                if YEAR_RE.search(h) or FALL_SPRING_RE.search(h): self.year_heading = h
        if not self.stack: return
        t = self.stack[-1]
        if tag in CELL and t['cell'] is not None:
            (t['row'] if t['row'] is not None else []).append(squash(''.join(t['cell']))); t['cell'] = None
        elif tag == 'caption' and t['cell'] is not None:
            t['caption'] = squash(''.join(t['cell'])); t['cell'] = None
        elif tag == 'tr' and t['row'] is not None:
            if any(c for c in t['row']): t['rows'].append(t['row'])
            t['row'] = None
        elif tag == 'table':
            done = self.stack.pop()
            if done['rows']:
                self.tables.append({'caption': done['caption'], 'heading': done['heading'],
                                    'year_heading': done['year_heading'], 'lead': done['lead'], 'rows': done['rows']})

    def handle_data(self, data):
        if self.skip: return
        if self.in_title: self.title += data
        self.out.append(data)
        if self.link: self.link[1].append(data)
        if self.heading is not None: self.heading.append(data)
        if self.stack and self.stack[-1]['cell'] is not None: self.stack[-1]['cell'].append(data)


def squash(s: str) -> str:
    return re.sub(r'\s+', ' ', html.unescape(s or '')).strip()


def parse_html(raw: bytes | str, base_url: str = '') -> Page:
    if isinstance(raw, bytes):
        raw = raw.decode(sniff_charset(raw), errors='replace')
    p = _Parser(base_url)
    p.feed(raw); p.close()
    text = re.sub(r'[ \t\r\f\v]+', ' ', ''.join(p.out))
    text = '\n'.join(l.strip() for l in text.split('\n'))
    text = re.sub(r'\n{3,}', '\n\n', text).strip()
    return Page(text, squash(p.title), p.tables, p.links, p.headings)


def sniff_charset(raw: bytes) -> str:
    m = re.search(rb'charset=["\']?([A-Za-z0-9_\-]+)', raw[:4096])
    enc = m.group(1).decode('ascii', 'ignore').lower() if m else 'utf-8'
    try:
        b''.decode(enc); return enc
    except LookupError:
        return 'utf-8'


def pdf_text(raw: bytes) -> str | None:
    """Layout-preserving text via poppler. Returns None when the tool is unavailable or fails."""
    exe = shutil.which('pdftotext')
    if not exe: return None
    with tempfile.NamedTemporaryFile(suffix='.pdf') as f:
        f.write(raw); f.flush()
        try:
            r = subprocess.run([exe, '-layout', '-enc', 'UTF-8', f.name, '-'], capture_output=True, timeout=120)
        except subprocess.TimeoutExpired:
            return None
    if r.returncode: return None
    text = r.stdout.decode('utf-8', 'replace')
    fields = pdf_form_fields(raw)
    if fields:  # Fillable forms (common for Common Data Set PDFs) keep values out of the page text.
        text += '\n\n[form fields]\n' + '\n'.join(f'{k}: {v}' for k, v in fields)
    return text


def pdf_form_fields(raw: bytes):
    """AcroForm field values when the optional pypdf package is installed; otherwise []."""
    try:
        from io import BytesIO
        from pypdf import PdfReader
    except ImportError:
        return []
    try:
        fields = PdfReader(BytesIO(raw)).get_fields() or {}
    except Exception:
        return []
    out = []
    for name, f in fields.items():
        v = f.get('/V') if hasattr(f, 'get') else None
        if v not in (None, '', '/Off'):
            out.append((name, squash(str(v))))
    return out


def parse_pdf(raw: bytes) -> Page | None:
    text = pdf_text(raw)
    if text is None: return None
    first = next((l.strip() for l in text.splitlines() if l.strip()), '')
    return Page(text, first[:200], [], [], [])


# ---------------------------------------------------------------- academic years
YEAR_RE = re.compile(r'(?<![\d$])(20\d{2})\s*(?:-|–|—|/|to|through)\s*(20)?(\d{2})(?!\d)')


COURSE_BEFORE = re.compile(r'\b(?!FY\b|AY\b)[A-Z]{2,5}\s?$')


FALL_SPRING_RE = re.compile(r'fall\s+(20\d{2})\s*(?:-|–|—|/|to|through|and|&)\s*spring\s+(20\d{2})', re.I)


def academic_year(first: int) -> str:
    return f'{first}-{str(first + 1)[-2:]}'


TRACKING = re.compile(r'^(?:_gl|utm_[a-z]+|fbclid|gclid|msclkid|mc_[a-z]+|_ga|hsa_[a-z]+)$', re.I)


def strip_tracking(query: str) -> str:
    """Drop analytics parameters (Lipscomb links carry '?_gl=1*13kx7ol*...'): they make one page look like several."""
    if not query: return query
    return '&'.join(kv for kv in query.split('&') if kv and not TRACKING.match(kv.split('=', 1)[0]))


def canonical_url(url: str) -> str:
    from urllib.parse import urlsplit, urlunsplit
    p = urlsplit(url)
    return urlunsplit((p.scheme, p.netloc, p.path, strip_tracking(p.query), p.fragment))


def year_labels(text: str):
    """Academic-year labels printed in text, e.g. '2026-2027', '2026–27', 'FY27' is ignored.
    Returns {label: count}; only consecutive years count as academic-year labels."""
    found = {}
    for m in YEAR_RE.finditer(text or ''):
        if COURSE_BEFORE.search((text or '')[max(0, m.start() - 8):m.start()]):
            continue  # "PHYS 2010/2011" and "HIST 2010-2020" are course numbers, not academic years
        first = int(m.group(1)); second = int((m.group(2) or str(first)[:2]) + m.group(3))
        if second == first + 1:
            label = academic_year(first); found[label] = found.get(label, 0) + 1
    for m in FALL_SPRING_RE.finditer(text or ''):
        first, second = int(m.group(1)), int(m.group(2))
        if second == first + 1:
            label = academic_year(first); found[label] = found.get(label, 0) + 1
    return found


def dominant_year(text: str, title: str = ''):
    """(label, basis). A label in the title wins; otherwise one label must dominate the page."""
    t = year_labels(title)
    if len(t) == 1: return next(iter(t)), 'labeled_in_title'
    labels = year_labels(text)
    if not labels: return None, 'source_unlabeled'
    ranked = sorted(labels.items(), key=lambda kv: (-kv[1], kv[0]))
    if len(ranked) == 1 or ranked[0][1] >= 2 * ranked[1][1]:
        return ranked[0][0], 'labeled_in_source'
    return None, 'ambiguous_year_labels'


def current_academic_year(today) -> str:
    """Academic year in force on a date (July-June)."""
    return academic_year(today.year if today.month >= 7 else today.year - 1)


# ---------------------------------------------------------------- numbers
MONEY_RE = re.compile(r'\$\s?([0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:\.([0-9]{2}))?')
NUM_RE = re.compile(r'(?<![\w.])-?([0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:\.([0-9]+))?(?![\w])')


def money_values(s: str):
    """Dollar amounts in a string, as numbers. '$1,234' -> 1234; '$12.50' -> 12.5."""
    out = []
    for m in MONEY_RE.finditer(s or ''):
        whole = int(m.group(1).replace(',', ''))
        out.append(whole + int(m.group(2)) / 100 if m.group(2) and m.group(2) != '00' else whole)
    return out


def plain_number(s: str):
    """A cell that is exactly one number (optionally $ or %), else None."""
    v = (s or '').strip().replace('$', '').replace('%', '').replace(',', '').strip()
    if re.fullmatch(r'-?\d+', v): return int(v)
    if re.fullmatch(r'-?\d+\.\d+', v): return float(v)
    return None


def normalize_for_search(s: str) -> str:
    """Lowercase, unify dashes/quotes/whitespace and drop thousands separators, for evidence matching."""
    s = html.unescape(s or '').lower().replace('–', '-').replace('—', '-').replace('’', "'")
    s = re.sub(r'(?<=\d),(?=\d{3})', '', s)
    return re.sub(r'\s+', ' ', s)


def snippet(text: str, needle: str, width: int = 90) -> str | None:
    """Verbatim context around the first occurrence of needle (case-insensitive), or None."""
    i = text.lower().find(needle.lower())
    if i < 0: return None
    a = max(0, i - width); b = min(len(text), i + len(needle) + width)
    return re.sub(r'\s+', ' ', text[a:b]).strip()
