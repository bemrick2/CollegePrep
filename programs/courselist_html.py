"""CourseLeaf "Course List" tables with their layout signals (`courselist_html/v1`).

The shared page parser keeps a table's cell text but not CourseLeaf's row classes or indentation, and those carry the
requirement structure: `areaheader` / `areasubheader` rows are section headings, `courselistcomment` rows are printed
rules ("Select two courses from the following:"), `orclass` rows are alternatives, and an indented cell
(`blockindent`, or a left margin) marks a course listed under the rule above it. This module reads only the
`table.sc_courselist` elements of an already-fetched page (standard library only) and keeps, for each table, the
nearest preceding heading, the paragraph text printed between that heading and the table, and every row as printed
with those signals. Nothing is interpreted here.
"""
from __future__ import annotations
import json, re
from html.parser import HTMLParser

HEADINGS = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}


class _Reader(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables, self.heading, self.after_heading = [], '', []
        self._in_heading = None; self._heading_buf = []
        self._para = None; self._para_buf = []
        self._table_depth = 0; self._t = None; self._tr = None; self._td = None; self._indent_stack = []
        self._caption = False
        self._sup = None  # text of a <sup> inside the current cell: CourseLeaf footnote markers ('Strategic Management<sup>3</sup>')

    # --- helpers
    @staticmethod
    def _cls(attrs):
        return (dict(attrs).get('class') or '').split()

    @staticmethod
    def _indented(attrs):
        d = dict(attrs)
        return 'blockindent' in (d.get('class') or '').split() or bool(re.search(r'margin-left\s*:\s*[1-9]', d.get('style') or '', re.I))

    def handle_starttag(self, tag, attrs):
        cls = self._cls(attrs)
        if self._t is None:
            if tag in HEADINGS: self._in_heading = tag; self._heading_buf = []
            elif tag == 'p' and self._in_heading is None: self._para = True; self._para_buf = []
            if tag == 'table' and 'sc_courselist' in cls:
                self._t = {'heading': self.heading, 'context': ' '.join(self.after_heading)[-1500:], 'caption': '', 'rows': []}
                self._table_depth = 1
            return
        if tag == 'table': self._table_depth += 1
        if tag == 'caption': self._caption = True
        elif tag == 'tr' and self._table_depth == 1: self._tr = {'classes': cls, 'cells': []}
        elif tag in ('td', 'th') and self._tr is not None and self._table_depth == 1:
            d = dict(attrs)
            self._td = {'text': [], 'classes': cls, 'colspan': int(d.get('colspan') or 1) if str(d.get('colspan') or '1').isdigit() else 1,
                        'indent': self._indented(attrs), 'spans': []}
            self._indent_stack = []
        elif self._td is not None:
            if self._indented(attrs):  # leading indentation marks the row; an indented '& ENGR 115' inside a cell does not
                self._td['indent' if not ''.join(self._td['text']).strip() else 'inner_indent'] = True
            if tag == 'span' and cls: self._td['spans'] += cls
            if tag == 'br': self._td['text'].append(' ')
            if tag == 'sup':
                self._sup = []
                if self._td.get('_tail') is None: self._td['_tail'] = len(''.join(self._td['text']))  # where a trailing run of markers may start

    def handle_endtag(self, tag):
        if self._t is None:
            if tag == self._in_heading:
                self.heading = re.sub(r'\s+', ' ', ''.join(self._heading_buf)).strip(); self.after_heading = []; self._in_heading = None
            elif tag == 'p' and self._para:
                t = re.sub(r'\s+', ' ', ''.join(self._para_buf)).strip()
                if t: self.after_heading.append(t)
                self._para = None
            return
        if tag == 'caption': self._caption = False
        elif tag == 'sup' and self._td is not None and self._sup is not None:
            mark = re.sub(r'\s+', ' ', ''.join(self._sup)).strip()
            if mark: self._td.setdefault('sups', []).append(mark)
            else: self._td['_tail'] = None
            self._sup = None
        elif tag in ('td', 'th') and self._td is not None and self._table_depth == 1:
            td = self._td; raw = ''.join(td['text']); tail = td.pop('_tail', None)
            if tail is not None and td.get('sups'):
                # the cell ends in superscripts (only commas or spaces between them): record that printed tail exactly
                td['sup_tail'] = re.sub(r'\s+', ' ', raw[tail:]).replace(' ', ' ').strip()
            td['text'] = re.sub(r'\s+', ' ', raw).replace(' ', ' ').strip()
            self._tr['cells'].append(td); self._td = None
        elif tag == 'tr' and self._tr is not None and self._table_depth == 1:
            self._t['rows'].append(self._tr); self._tr = None
        elif tag == 'table':
            self._table_depth -= 1
            if self._table_depth == 0:
                self.tables.append(self._t); self._t = None; self.after_heading = []

    def handle_data(self, data):
        if self._t is None:
            if self._in_heading: self._heading_buf.append(data)
            elif self._para: self._para_buf.append(data)
            return
        if self._caption: self._t['caption'] += data.strip()
        elif self._td is not None:
            self._td['text'].append(data)
            if self._sup is not None: self._sup.append(data)
            elif self._td.get('_tail') is not None and not re.fullmatch(r'[\s,\u00a0]*', data): self._td['_tail'] = None  # text after a marker: not a tail


def course_lists(html_bytes):
    """[{'heading', 'context', 'caption', 'rows': [{'classes', 'cells': [{'text', 'classes', 'colspan', 'indent', 'spans', 'sups'?}]}]}]
    A cell's text keeps every character as printed (superscripts included); 'sups' lists the text of its <sup> elements
    (footnote markers) when it has any, so a reader can tell a marker from a number that is part of a title."""
    r = _Reader()
    try:
        r.feed(html_bytes.decode('utf-8', 'replace') if isinstance(html_bytes, bytes) else html_bytes)
        r.close()
    except Exception:  # a malformed page yields whatever was read before the error
        pass
    return r.tables


def to_text(tables):
    return json.dumps(tables, ensure_ascii=False, indent=0)


class _Outline(HTMLParser):
    """Block outline of a page's main content: headings, paragraphs, list items (with list nesting depth) and table rows,
    each with its classes and text. Used for catalogs whose requirement lists are nested HTML lists (SmartCatalog)."""
    BLOCKS = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'tr', 'dt', 'dd'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.stack, self.list_depth, self.skip, self.seq = [], [], 0, 0, 0

    def handle_starttag(self, tag, attrs):
        cls = (dict(attrs).get('class') or '').split()
        if tag in ('script', 'style', 'nav', 'footer', 'header'): self.skip += 1; return
        if tag in ('ul', 'ol'): self.list_depth += 1
        if tag in self.BLOCKS:
            self.seq += 1
            self.stack.append({'tag': tag, 'depth': self.list_depth, 'classes': cls, 'text': [], 'seq': self.seq})
        elif tag == 'br' and self.stack: self.stack[-1]['text'].append(' ')
        elif self.stack and cls and tag in ('span', 'a', 'div', 'strong', 'em', 'td'):
            self.stack[-1].setdefault('inner', []).extend(cls)

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'nav', 'footer', 'header'): self.skip = max(0, self.skip - 1); return
        if tag in ('ul', 'ol'): self.list_depth = max(0, self.list_depth - 1)
        if tag in self.BLOCKS and self.stack and self.stack[-1]['tag'] == tag:
            b = self.stack.pop()
            text = re.sub(r'\s+', ' ', ''.join(b['text'])).replace(' ', ' ').strip()
            if text and not self.skip:
                item = {'tag': b['tag'], 'depth': b['depth'], 'classes': b['classes'], 'text': text[:600], 'seq': b['seq']}
                if b.get('inner'): item['inner'] = sorted(set(b['inner']))[:8]
                self.out.append(item)
            if self.stack and text: self.stack[-1]['text'].append(' ')  # nested block text is not repeated in its parent

    def handle_data(self, data):
        if self.stack and not self.skip: self.stack[-1]['text'].append(data)


def outline(html_bytes):
    r = _Outline()
    try:
        r.feed(html_bytes.decode('utf-8', 'replace') if isinstance(html_bytes, bytes) else html_bytes); r.close()
    except Exception:
        pass
    return [{k: v for k, v in b.items() if k != 'seq'} for b in sorted(r.out, key=lambda b: b['seq'])]  # document order
