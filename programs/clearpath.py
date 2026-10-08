"""UTC "Clear Path for Advising" four-year plans (`clearpath_plan/v1`).

The PDFs print two semesters side by side ("Fall Semester: ... Hrs   Spring Semester: ... Hrs"); the text layer keeps
each printed line but long titles wrap onto the next line, which moves hours between columns (the shared
program_map/v1 misreads exactly this). This reader rebuilds each column item by item and then checks itself against
the plan's own printed numbers: every term prints its hour total ("15-18"), and a term is accepted only when the
minimum and maximum hours of its items add up to exactly that printed range. A plan with any term that does not add
up is marked `term_totals_mismatch` and held.
"""
from __future__ import annotations
import re

from pipeline.extractors import common

from programs.years import academic_year_of
EXTRACTOR = 'clearpath_plan/v1'
HRS = re.compile(r'^\d{1,2}(?:-\d{1,2})?$')
YEAR = re.compile(r'^(First|Second|Third|Fourth|Fifth) Year\b')
HEADER = re.compile(r'^Fall Semester:.*Spring Semester:', re.I)
TITLE = re.compile(r'^CLEAR PATH for ADVISING\s*[–-]\s*(.+?)\s{2,}(20\d{2})\s*-\s*(20\d{2})\s*$')
COURSE = re.compile(r'^([A-Z]{2,5} \d{4}[A-Z]?(?:/\d{4}[A-Z]?)?): (.+)$')


def _span(h):
    a, _, b = h.partition('-')
    return int(a), int(b or a)


def _item(text, hrs):
    m = COURSE.match(text)
    item = {'code': m.group(1), 'title': m.group(2)} if m and '/' not in m.group(1) else {'text': text}
    item['credits'] = int(hrs) if hrs.isdigit() else hrs
    return item


def _tokens(raw):
    """[(start column, text)] split on runs of 3+ spaces; 'Title 3' (hours one space after the title) is split too."""
    out = []
    for m in re.finditer(r'\S(?:.*?\S)?(?=\s{3,}|\s*$)', raw):
        t, col = m.group(0), m.start()
        h = re.match(r'^(.*\S)\s(\d{1,2}(?:-\d{1,2})?)$', t)
        if h and not HRS.match(t) and not re.search(r'\b(Level|Hours?)$', h.group(1)):
            out += [(col, h.group(1)), (col + len(h.group(1)) + 1, h.group(2))]
        else:
            out.append((col, t))
    return out


def _unfinished(title):
    return title.count('(') > title.count(')') or bool(re.search(r'\b(and|or|with|of|in|for|the|to|Global|Natural|Social)$', title))


def parse(lines):
    """[(year_label, fall_items, fall_total, spring_items, spring_total, problems)] or None when the layout is not recognised.
    Columns come from character positions: a token starting at or right of the header's 'Spring Semester:' column (less a
    small margin) is in the right column. A text line printed alone at the left margin (a wrapped title) is resolved by
    the hours that follow: it becomes the title of the column whose hours arrive without a title, or the continuation of
    an unfinished title; anything else is a problem and the plan is held."""
    years, i = [], 0
    while i < len(lines):
        line = lines[i].strip()
        if not YEAR.match(line): i += 1; continue
        label = line
        if i + 1 >= len(lines) or not HEADER.match(lines[i + 1].strip()): return None
        hdr = lines[i + 1]; split = hdr.find('Spring Semester:') - 6
        i += 2
        cols = {'L': [], 'R': []}
        floating, problems, totals = [], set(), None
        while i < len(lines):
            raw = lines[i].rstrip(); i += 1
            toks = _tokens(raw)
            if not toks: continue
            if len(toks) == 2 and all(HRS.match(t) for _, t in toks): totals = [t for _, t in toks]; break
            if YEAR.match(toks[0][1]) or HEADER.match(raw.strip()): return None
            if len(toks) == 1 and not HRS.match(toks[0][1]) and toks[0][0] < 5:   # a text line alone at the margin
                floating.append(toks[0][1]); continue
            side_title = {'L': None, 'R': None}
            for col, t in toks:
                side = 'R' if col >= split else 'L'
                if HRS.match(t):
                    if side_title[side] is not None:
                        cols[side].append([side_title[side], t]); side_title[side] = None
                    elif floating:                       # hours for a title printed on its own line above
                        cols[side].append([floating.pop(0), t])
                    elif cols[side] and cols[side][-1][1] is None:
                        cols[side][-1][1] = t
                    else:
                        problems.add('hours_without_title')
                else:
                    if side_title[side] is not None: problems.add('two_titles_in_column')
                    side_title[side] = t
            for side in 'LR':
                if side_title[side] is not None: cols[side].append([side_title[side], None])   # title wrapped: hours follow
            # floating lines not consumed here continue an unfinished title
            for f in list(floating):
                cands = [c for c in cols['L'][-1:] + cols['R'][-1:] if _unfinished(c[0])]
                if len(cands) == 1: cands[0][0] += ' ' + f; floating.remove(f)
        for f in floating:
            cands = [c for c in cols['L'][-1:] + cols['R'][-1:] if _unfinished(c[0])]
            if len(cands) == 1: cands[0][0] += ' ' + f
            else: problems.add('unattached_text')
        if totals is None: return None
        years.append((label, cols['L'], totals[0], cols['R'], totals[1], problems))
    return years or None


def term_ok(items, total):
    if any(h is None for _, h in items): return False
    lo, hi = _span(total)
    return sum(_span(h)[0] for _, h in items) == lo and sum(_span(h)[1] for _, h in items) == hi


def extract(inst, entry, page, program_key, today_year):
    lines = page.lines
    head = next((l for l in lines[:3] if TITLE.match(l.strip())), None)
    if not head: return []
    m = TITLE.match(head.strip())
    year = f'{m.group(2)}-{m.group(3)}'
    acad = academic_year_of(year)
    years = parse(lines)
    if not years: return []
    terms, issues = [], set()
    for label, fall, ft, spring, st, probs in years:
        issues |= probs
        for name, items, total in (('Fall Semester', fall, ft), ('Spring Semester', spring, st)):
            if not term_ok(items, total): issues.add('term_totals_mismatch')
            terms.append({'term_index': len(terms) + 1, 'label': f'{label} — {name}', 'credit_hours': total,
                          'items': [_item(t, h) for t, h in items if h is not None]})
    rd = {'schema': 'requirement_group/v1', 'catalog_year': year, 'group_type': 'sequence', 'category': 'recommended_sequence',
          'terms': terms, 'source_section': f'Clear Path for Advising – {m.group(1)}'}
    rec = {'program_key': program_key, 'requirement_key': 'clear-path-four-year-plan', 'requirement_kind': 'program_plan', 'rule_details': rd}
    ev = [{'field': 'catalog_year', 'value': year, 'snippet': head.strip()[:200]}] + \
         [{'field': 'term', 'value': t['label'], 'snippet': f"{t['label']}: {len(t['items'])} items, {t['credit_hours']} hours"} for t in terms]
    return [common.make('degree_requirements', inst['institution_key'], acad, 'labeled_in_source', rec, ev, entry, EXTRACTOR,
                        {'program_key': program_key, 'requirement_key': 'clear-path-four-year-plan'}, {'terms': len(terms)},
                        sorted(issues | ({f'stale_year_label:{acad}'} if acad < today_year else set())))]


# ---- layout reader (word positions from programs.pdf_layout) -----------------------------------------------------
def _line_text(ws):
    return ' '.join(w[2] for w in ws)


UNFINISHED = re.compile(r'(\b(or|and|the|of|for|to|in|with)|[,:\-–])$')


def blocks(line_ys, hour_ys):
    """Split title lines (sorted by y) into len(hour_ys) consecutive non-empty blocks, block k centred as closely as
    possible on hours k: a wrapped title's lines straddle the hours printed on its middle line. Returns [(start, end)]
    index ranges, or None when there are fewer lines than hours."""
    n, m = len(line_ys), len(hour_ys)
    if n < m or m == 0: return None
    INF = float('inf')
    best = [[INF] * (n + 1) for _ in range(m + 1)]; back = [[0] * (n + 1) for _ in range(m + 1)]
    best[0][0] = 0.0
    for k in range(1, m + 1):
        for j in range(k, n - (m - k) + 1):
            for i in range(k - 1, j):
                if best[k - 1][i] == INF: continue
                c = best[k - 1][i] + (sum(line_ys[i:j]) / (j - i) - hour_ys[k - 1]) ** 2
                if c < best[k][j]: best[k][j], back[k][j] = c, i
    out, j = [], n
    for k in range(m, 0, -1):
        i = back[k][j]; out.append((i, j)); j = i
    return out[::-1]


def parse_layout(pages):
    """[(year_label, fall_items, fall_total, spring_items, spring_total, problems)] from word positions.

    Per page: every word with its x and vertical centre. Year rows ('First Year – 30-37 Hours') and header rows ('Fall
    Semester: Hrs Spring Semester: Hrs') are found by their words; a year section runs from its header to the next year
    row (or the page's 'Completed:' row). Columns split at the header's 'Spring' word. An hours value is an hours-shaped
    word within 25pt of its column's 'Hrs' word; the lowest one in the column is the printed term total, the others belong
    to items. Title words are grouped into lines by y, and each title line joins the nearest item hours by y."""
    years = []
    for page in pages:
        W = [(w[0], (l['y'] + l['y1']) / 2, w[2]) for l in page['lines'] for w in l['words']]
        rows = {}
        for x, y, t in W: rows.setdefault(round(y), []).append((x, t))
        def row_text(y): return ' '.join(t for _, t in sorted(rows[y]))
        ys = sorted(rows)
        year_rows = [y for y in ys if YEAR.match(row_text(y))]
        ends = [y for y in ys if re.match(r'^(Completed:|Graduation Requirements)', row_text(y))]
        for k, yr in enumerate(year_rows):
            stop = min([y for y in year_rows[k + 1:]] + [y for y in ends if y > yr] + [10 ** 6])
            hdr = next((y for y in ys if yr < y < stop and re.match(r'^Fall Semester:', row_text(y))), None)
            problems = set()
            if hdr is None: return None
            hw = sorted(rows[hdr])
            spring = next((x for x, t in hw if t == 'Spring'), None)
            hrs = [x for x, t in hw if t == 'Hrs']
            if spring is None or len(hrs) != 2: return None
            split, bands = spring - 4, {'L': hrs[0], 'R': hrs[1]}
            sect = [(x, y, t) for x, y, t in W if hdr + 2 < y < stop - 2]
            out, totals = [], []
            for side in 'LR':
                col = [(x, y, t) for x, y, t in sect if (x >= split) == (side == 'R')]
                hours = sorted([(y, t) for x, y, t in col if HRS.match(t) and abs(x - bands[side]) < 25])
                if not hours: return None
                total = hours.pop()                     # the lowest hours value is the term total
                lines = {}
                for x, y, t in col:
                    if HRS.match(t) and abs(x - bands[side]) < 25: continue
                    if t.startswith('*') and y > total[0]: continue    # footnote rows below the total
                    lines.setdefault(round(y), []).append((x, t))
                tl = [(ly, ' '.join(t for _, t in sorted(ws))) for ly, ws in sorted(lines.items()) if ly <= total[0] + 2]
                groups = blocks([y for y, _ in tl], [h[0] for h in hours])
                built = []
                if groups is None:
                    problems.add('titles_not_matched_to_hours')
                else:
                    for (a, b), (hy, ht) in zip(groups, hours):
                        if abs(sum(y for y, _ in tl[a:b]) / (b - a) - hy) > 12: problems.add('title_far_from_hours')
                        title = ' '.join(t for _, t in tl[a:b])
                        if UNFINISHED.search(title) or re.match(r'^([a-z]|1 \()', title): problems.add('title_looks_split')
                        built.append([title, ht])
                out.append(built); totals.append(total[1])
            years.append((row_text(yr), out[0], totals[0], out[1], totals[1], problems))
    return years or None


def extract_layout(inst, entry, page_text_lines, pages, program_key, today_year):
    """As extract(), from word positions; the plan title and year still come from the text layer's first line."""
    head = next((l for l in page_text_lines[:3] if TITLE.match(l.strip())), None)
    if not head: return []
    m = TITLE.match(head.strip()); year = f'{m.group(2)}-{m.group(3)}'; acad = academic_year_of(year)
    years = parse_layout(pages)
    if not years: return []
    terms, issues = [], set()
    for label, fall, ft, spring, st, probs in years:
        issues |= probs
        ym = re.search(r'[–-]\s*(\d{1,2})(?:-(\d{1,2}))?(?:\s+hours)?\s*$', label, re.I)  # 'Third Year – 30 hours', 'First Year – 31-33'
        if not ym or (_span(ft)[0] + _span(st)[0], _span(ft)[1] + _span(st)[1]) != (int(ym.group(1)), int(ym.group(2) or ym.group(1))):
            issues.add('year_total_mismatch')  # 'First Year – 30-37 Hours' must equal the two printed term totals
        for name, items, total in (('Fall Semester', fall, ft), ('Spring Semester', spring, st)):
            if not term_ok(items, total): issues.add('term_totals_mismatch')
            terms.append({'term_index': len(terms) + 1, 'label': f'{label} — {name}', 'credit_hours': total, 'items': [_item(t, h) for t, h in items]})
    if len(terms) < 8: issues.add('fewer_than_four_years')
    rd = {'schema': 'requirement_group/v1', 'catalog_year': year, 'group_type': 'sequence', 'category': 'recommended_sequence',
          'terms': terms, 'source_section': f'Clear Path for Advising – {m.group(1)}'}
    rec = {'program_key': program_key, 'requirement_key': 'clear-path-four-year-plan', 'requirement_kind': 'program_plan', 'rule_details': rd}
    ev = [{'field': 'catalog_year', 'value': year, 'snippet': head.strip()[:200]}] + \
         [{'field': 'term', 'value': t['label'], 'snippet': f"{t['label']}: {len(t['items'])} items, {t['credit_hours']} hours"} for t in terms]
    return [common.make('degree_requirements', inst['institution_key'], acad, 'labeled_in_source', rec, ev, entry, EXTRACTOR,
                        {'program_key': program_key, 'requirement_key': 'clear-path-four-year-plan'}, {'terms': len(terms)},
                        sorted(issues | ({f'stale_year_label:{acad}'} if acad < today_year else set())))]
