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
        elif tag in ('td', 'th') and self._td is not None and self._table_depth == 1:
            td = self._td; td['text'] = re.sub(r'\s+', ' ', ''.join(td['text'])).replace(' ', ' ').strip()
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
        elif self._td is not None: self._td['text'].append(data)


def course_lists(html_bytes):
    """[{'heading', 'context', 'caption', 'rows': [{'classes', 'cells': [{'text', 'classes', 'colspan', 'indent', 'spans'}]}]}]"""
    r = _Reader()
    try:
        r.feed(html_bytes.decode('utf-8', 'replace') if isinstance(html_bytes, bytes) else html_bytes)
        r.close()
    except Exception:  # a malformed page yields whatever was read before the error
        pass
    return r.tables


def to_text(tables):
    return json.dumps(tables, ensure_ascii=False, indent=0)
