"""AP / CLEP / IB credit tables -> credit_policies candidates with equivalencies.

Only rows whose exam cell matches the canonical exam catalog are used, every equivalency keeps the
row text as evidence, and the score and course cells are copied as printed (no inference of
credit from course codes, no filling of missing scores).
"""
from __future__ import annotations
import re

from .. import exams
from . import common

EXTRACTOR = 'credit_table/v1'
COURSE_RE = re.compile(r'\b[A-Z]{2,5}\s?-?\d{3,4}[A-Z]?\b')
SCORE_CELL = re.compile(r'^\s*(score\s*(of\s*)?)?([1-7]|[2-8]\d)(\s*(\+|or\s*(higher|above|better)|-\s*[1-7]|,?\s*(or|and|&)\s*[1-7]))*\s*$', re.I)


def _find(header, *words):
    for i, h in enumerate(header):
        if any(w in h.lower() for w in words): return i
    return None


def _exam_column(kind, rows, guess):
    """The column whose cells name exams. A header guess can point at a code column ('Test Code' next to
    'AP Exam', KY: EKU), so the column with the most catalog matches wins when it beats the guess."""
    body = rows[1:]
    if not kind or not body: return guess
    width = max(len(r) for r in rows)
    hits = [sum(1 for r in body if i < len(r) and exams.match(kind, r[i])) for i in range(width)]
    best = max(range(width), key=lambda i: hits[i])
    return best if hits[best] > (hits[guess] if guess is not None and guess < width else 0) else guess


def _columns(rows, kind=None):
    header = rows[0]
    exam = _find(header, 'exam', 'test', 'subject', 'ap course', 'clep', 'ib ')
    score = _find(header, 'score', 'minimum', 'level')
    # The course column is never the exam column ("IB Course | Score | Credit Awarded", KY: Big Sandy).
    pick_course = lambda: next((i for words in (('equivalen', 'exemption'), ('course',), ('credit granted', 'credit awarded', 'awarded'))
                                for i, h in enumerate(header) if i != exam and any(w in h.lower() for w in words)), None)
    course = pick_course()
    hours = _find(header, 'hours', 'hrs', 'credits', 'sch')
    has_header = score is not None or (exam is not None and course is not None)
    if has_header:
        exam = _exam_column(kind, rows, exam)
        # "Advanced Placement Course | ... | GSW Course Credit" (GA): the exam header also says "course",
        # so the course column is chosen again once the exam column is known.
        course = pick_course()
        body = rows[1:]
        if course is not None and body and sum(_credits(r[course]) is not None for r in body if course < len(r)) >= len(body) / 2:
            course = None  # "Credit Granted | 12" holds hours, not courses (Walters State CLEP)
        if course is None or course == hours:  # GA Tech IB: "Subject | Exam Scores | Credit" with courses under Credit
            body = rows[1:]
            width = max(len(r) for r in rows)
            course = next((i for i in range(width) if i not in (exam, score)
                           and sum(bool(COURSE_RE.search(r[i])) for r in body if i < len(r)) >= max(2, len(body) / 3)), course)
    if not has_header:
        body = rows
        width = max(len(r) for r in body)
        exam = 0
        score = next((i for i in range(1, width) if sum(bool(SCORE_CELL.match(r[i])) for r in body if i < len(r)) >= len(body) / 2), None)
        course = next((i for i in range(1, width) if i != score and sum(bool(COURSE_RE.search(r[i])) for r in body if i < len(r)) >= len(body) / 3), None)
        hours = None
    if course == exam: course = None
    if hours in (exam, score, course): hours = None
    if has_header and hours is None:  # "Credit Statement: 3 credit hours" (KY, Big Sandy): find the column by its cells
        body = rows[1:]
        width = max(len(r) for r in rows)
        hours = next((i for i in range(width) if i not in (exam, score, course)
                      and sum(_credits(r[i]) is not None for r in body if i < len(r)) >= max(2, len(body) / 2)), None)
    return has_header, exam if exam is not None else 0, score, course, hours


def _credits(cell):
    m = re.fullmatch(r'\s*(\d{1,2}(?:\.\d)?)\s*(?:(?:semester\s+)?credit\s+)?(hours?|hrs?\.?|credits?|sch)?\s*', cell or '', re.I)
    return float(m.group(1)) if m and '.' in m.group(1) else int(m.group(1)) if m else None


def table_exam(kind, t):
    """An exam named by the table itself (its lead text, caption or heading) for one-table-per-exam layouts."""
    for label in (t.get('lead'), t.get('caption'), t.get('heading')):
        if label and len(label) <= 80:
            hit = exams.match(kind, label)
            if hit: return hit + (label,)
    return None


def table_equivalencies(kind, rows, table_hit=None):
    if len(rows) < 2: return []
    has_header, ex, sc, co, hr = _columns(rows, kind)
    header = [c.lower() for c in rows[0]]
    exam_column = has_header and any(w in ' '.join(header) for w in ('exam', 'test', 'subject', 'ap course'))
    if table_hit and not exam_column:
        # Rows are score tiers for the one exam the table is named after.
        body = rows[1:] if has_header else rows
        out = []
        for row in body:
            cells = list(row)
            get = lambda i: cells[i].strip() if i is not None and i < len(cells) else ''
            sc_i = sc if sc is not None else 0
            score, course = get(sc_i), get(co)
            if not score or not re.search(r'\d', score): continue
            eq = {'exam_or_course_code': table_hit[0], 'exam_or_course_name': table_hit[1], 'minimum_score': score,
                  'institution_course_equivalent': course or None, 'credits_awarded': _credits(get(hr)), 'notes': None}
            out.append((eq, f'{table_hit[2]} || ' + ' | '.join(cells)))
        return out
    body = rows[1:] if has_header else rows
    width = len(rows[0])
    # NE r1 (UNO): "Exam | Level | Score | Course" - a column of SL/HL is the level, the next numeric column the score.
    lvl = None
    col = lambda i: [r[i].strip() for r in body if i is not None and i < len(r) and r[i].strip()]
    if kind == 'IB' and sc is not None and col(sc) and all(re.fullmatch(r'(SL|HL|SL\s*/\s*HL)', c, re.I) for c in col(sc)):
        lvl = sc
        sc = next((i for i in range(width) if i not in (ex, lvl, co, hr) and col(i) and all(re.search(r'\d', c) for c in col(i))), None)
    if kind == 'IB' and lvl is None:
        lvl = next((i for i in range(width) if i not in (ex, sc, co, hr) and col(i)
                    and sum(1 for c in col(i) if re.fullmatch(r'(SL|HL|SL\s*/\s*HL|HL\s*/\s*SL)', c, re.I)) >= 0.8 * len(col(i))), None)
    out, prev = [], None
    for row in body:
        cells = list(row)
        if len(cells) < width and prev:  # rowspan: the exam cell was merged into the previous row
            cells = [prev[2]] + cells
        hit = exams.match(kind, cells[ex] if ex < len(cells) else '')
        if not hit: continue
        code, name = hit
        prev = (code, name, cells[ex])
        get = lambda i: cells[i].strip() if i is not None and i < len(cells) else ''
        score, course = get(sc), get(co)
        if not score and not course: continue
        if score and not re.search(r'\d', score) and not course: continue  # a section heading row ("Foreign Languages", Gordon State)
        # LA r1 (Xavier): "Biology, Standard Level | 6" and "Biology, Higher Level | 6" are different rules; keep the level.
        label_cell = cells[ex] if ex < len(cells) else ''
        both = re.search(r'\bSL\s*/\s*HL\b|\bHL\s*/\s*SL\b|standard\s+(?:and|or|/)\s+higher', label_cell, re.I)  # MO (Cottey): "Biology (SL/HL)"
        level = (None if both else 'HL' if re.search(r'\bhigher\b|\bHL\b', label_cell, re.I) else
                 'SL' if re.search(r'\bstandard\b|\bSL\b|\bsub(?:sidiary)?\b', cells[ex] if ex < len(cells) else '', re.I) else None)
        if kind == 'IB' and not level and not both and lvl is not None and lvl < len(cells) and re.fullmatch(r'\s*(SL|HL)\s*', cells[lvl], re.I):
            level = cells[lvl].strip().upper()  # NE (UNO): "Anthropology | SL | 5-7" keeps the level in its own column
        if kind == 'IB' and level and score and not re.search(r'\b(HL|SL)\b|higher|standard', score, re.I):
            score = f'{level} {score}'
        eq = {'exam_or_course_code': code, 'exam_or_course_name': name,
              'minimum_score': score or None, 'institution_course_equivalent': course or None,
              'credits_awarded': _credits(get(hr)), 'notes': None}
        used = {ex, sc, co, hr, lvl}
        rest = [c for i, c in enumerate(cells) if i not in used and c.strip()]
        if rest: eq['notes'] = ' | '.join(rest)
        out.append((eq, ' | '.join(cells)))
    return out


PDF_SCORE = re.compile(r'^\s*((?:[1-7]|[2-8]\d)(?:\s*(?:\+|or\s+(?:higher|above|better)|-\s*[1-7]|,?\s*(?:or|and|&|,)\s*[1-7]))*)\b(.*)$', re.I)


def pdf_equivalencies(kind, page):
    """Layout-text credit charts: '<exam name>   <score>   <course(s)>   <hours>' on one line."""
    out = []
    for line in page.lines:
        cells = [c.strip() for c in re.split(r'\s{2,}', line) if c.strip()]
        if len(cells) < 3 or len(cells[0]) > 80: continue
        hit = exams.match(kind, cells[0])
        if not hit: continue
        rest = cells[1:]
        score_i = next((i for i, c in enumerate(rest) if SCORE_CELL.match(c)), None)
        if score_i is None: continue
        others = [c for i, c in enumerate(rest) if i != score_i]
        course = next((c for c in others if COURSE_RE.search(c) or re.search(r'elective|credit', c, re.I)), None)
        hours = next((_credits(c) for c in others if _credits(c) is not None), None)
        if course is None and hours is None: continue
        eq = {'exam_or_course_code': hit[0], 'exam_or_course_name': hit[1], 'minimum_score': rest[score_i],
              'institution_course_equivalent': course, 'credits_awarded': hours, 'notes': None}
        out.append((eq, line.strip()[:300]))
    return out


def extract(inst, entry, page, today_year):
    if common.professional_source(entry, page): return []
    if entry.get('kind') == 'pdf':
        kind = exams.detect_kind(page.title, ' '.join(page.lines[:15]), entry.get('url', ''))
        if not kind: return []
        page_tables, pdf_rows = [], {kind: pdf_equivalencies(kind, page)}
    else:
        if not page.tables: return []
        page_tables, pdf_rows = page.tables, {}
    by_kind = {k: list(v) for k, v in pdf_rows.items() if v}
    heading_uses = {}
    for t in page_tables:
        heading_uses[t.get('heading')] = heading_uses.get(t.get('heading'), 0) + 1
    for t in page_tables:
        # Nearest label first: the header row, the text just above the table, its caption, then the section
        # heading (KY, Big Sandy: an IB table sits under a "CLEP" heading) and finally the page.
        header_row = ' '.join(t['rows'][0]) if t.get('rows') else ''
        kind = next((k for k in (exams.detect_kind(x) for x in (header_row, t.get('lead'), t.get('caption'), t.get('heading'))) if k), None) \
            or exams.detect_kind(page.title, entry['url'])
        if not kind: continue
        named = dict(t)
        if not t.get('lead') and heading_uses[t.get('heading')] > 1:
            named['heading'] = None  # several tables under one heading: the heading cannot name each table
        for eq, row_text in table_equivalencies(kind, t['rows'], table_exam(kind, named)):
            by_kind.setdefault(kind, []).append((eq, row_text))
    out = []
    for kind, items in by_kind.items():
        if len(items) < 3:  # A credit table lists several exams; fewer matches is usually prose/navigation.
            continue
        year, basis, issues = common.resolve_year(page, entry, today_year)
        seen, eqs, evidence = set(), [], []
        for eq, row_text in items:
            k = (eq['exam_or_course_code'], eq['minimum_score'], eq['institution_course_equivalent'])
            if k in seen: continue
            seen.add(k); eqs.append(eq)
            evidence.append({'field': f"equivalencies[{eq['exam_or_course_code']}|{eq['minimum_score']}]", 'snippet': row_text[:300]})
        record = {'policy_kind': kind, 'policy_url': common.source_of(entry)['url'], 'equivalencies': eqs,
                  'notes': f'Extracted by {EXTRACTOR} from the published table; cells copied as printed.'}
        checks = {'equivalencies': len(eqs), 'distinct_exams': len({e['exam_or_course_code'] for e in eqs}),
                  'rows_without_score': sum(1 for e in eqs if not e['minimum_score'])}
        if checks['rows_without_score']: issues = issues + ['rows_without_score']
        # "50 62" with "FREN 1101, 1102 FREN 1101, 1102, 2001, 2002": two score tiers merged into one row (Gordon State)
        if any(re.fullmatch(r'\s*\d{1,3}\s+\d{1,3}\s*', e['minimum_score'] or '') for e in eqs): issues = issues + ['merged_score_cells']
        if any((e['credits_awarded'] or 0) > 16 for e in eqs):
            issues = issues + ['credits_implausible']  # merged cells ("3" and "6" read as 36)
        # FL r1 (FSU, UWF, New College, USF, Ringling IB): the score column held course codes, subjects, levels
        # ("HL") or a header word ("MINIMUM SCORE 4"); scores are numbers, ranges or "HL 5"-style levels with a number.
        bad_score = sum(1 for e in eqs if e['minimum_score'] and (not re.search(r'\d', e['minimum_score'])
                        or re.search(r'[A-Z]{2,4}\s?\d{3,4}|score(?!\s+of\s+\d)|credit|same as', e['minimum_score'], re.I)))
        if bad_score and bad_score >= len(eqs) * 0.3: issues = issues + ['score_column_not_scores']
        # Two score tiers merged into one cell ("4 5 to 7", Broward IB).
        if any(re.fullmatch(r'\s*\d\s+\d\s+to\s+\d\s*', e['minimum_score'] or '') for e in eqs): issues = issues + ['merged_score_cells']
        # LA r1 (Louisiana Tech): "3 or 4 5" is two tiers in one cell; "4, 5" and "4 or 5" are one tier.
        if any(re.fullmatch(r'\s*\d{1,2}(?:\s*(?:or|,|-|–|to|and)\s*\d{1,2})+\s+\d{1,2}(?:\s+\d{1,2})*\s*', e['minimum_score'] or '') for e in eqs):
            issues = issues + ['merged_score_cells']
        # LA r1: "CLEP" rows scored 3 are AP rows; scores must fit the exam's scale (AP 1-5, IB 1-7, CLEP 20-80).
        scale = {'AP': (1, 5), 'IB': (1, 7), 'CLEP': (20, 80)}.get(kind)
        firsts = [int(m.group()) for e in eqs for m in [re.search(r'\d+', e['minimum_score'] or '')] if m]
        if scale and firsts and any(not scale[0] <= v <= scale[1] for v in firsts):  # OK r1 (OKBU): one CLEP row scored 3 is already wrong
            issues = issues + ['score_scale_mismatch']
        if eqs and all(not e['institution_course_equivalent'] for e in eqs): issues = issues + ['course_column_missing']
        # OK r1 (Cameron IB): "ENGL" with the number in another column is not a course.
        bare = sum(1 for e in eqs if re.fullmatch(r'\s*[A-Z]{2,5}\s*', e['institution_course_equivalent'] or ''))
        if bare and bare >= len(eqs) * 0.5: issues = issues + ['course_number_missing']
        numeric = sum(1 for e in eqs if re.fullmatch(r'\s*\d{1,2}(\.\d)?\s*', e['institution_course_equivalent'] or ''))
        if numeric and numeric >= len(eqs) / 2:
            issues = issues + ['course_column_numeric']  # the hours column was read as the course column
        out.append(common.make('credit_policies', inst['institution_key'], year, basis, record, evidence, entry,
                               EXTRACTOR, {'policy_kind': kind}, checks, issues))
    return out
