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


def _columns(rows):
    header = rows[0]
    exam = _find(header, 'exam', 'test', 'subject', 'ap course', 'clep', 'ib ')
    score = _find(header, 'score', 'minimum', 'level')
    course = _find(header, 'equivalen', 'course', 'credit granted', 'credit awarded', 'awarded')
    hours = _find(header, 'hours', 'hrs', 'credits', 'sch')
    has_header = score is not None or (exam is not None and course is not None)
    if not has_header:
        body = rows
        width = max(len(r) for r in body)
        exam = 0
        score = next((i for i in range(1, width) if sum(bool(SCORE_CELL.match(r[i])) for r in body if i < len(r)) >= len(body) / 2), None)
        course = next((i for i in range(1, width) if i != score and sum(bool(COURSE_RE.search(r[i])) for r in body if i < len(r)) >= len(body) / 3), None)
        hours = None
    if course == exam: course = None
    if hours in (exam, score, course): hours = None
    return has_header, exam if exam is not None else 0, score, course, hours


def _credits(cell):
    m = re.fullmatch(r'\s*(\d{1,2}(?:\.\d)?)\s*(hours?|hrs?\.?|credits?|sch)?\s*', cell or '', re.I)
    return float(m.group(1)) if m and '.' in m.group(1) else int(m.group(1)) if m else None


def table_equivalencies(kind, rows):
    if len(rows) < 2: return []
    has_header, ex, sc, co, hr = _columns(rows)
    body = rows[1:] if has_header else rows
    width = len(rows[0])
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
        eq = {'exam_or_course_code': code, 'exam_or_course_name': name,
              'minimum_score': score or None, 'institution_course_equivalent': course or None,
              'credits_awarded': _credits(get(hr)), 'notes': None}
        used = {ex, sc, co, hr}
        rest = [c for i, c in enumerate(cells) if i not in used and c.strip()]
        if rest: eq['notes'] = ' | '.join(rest)
        out.append((eq, ' | '.join(cells)))
    return out


def extract(inst, entry, page, today_year):
    if not page.tables: return []
    by_kind = {}
    for t in page.tables:
        kind = exams.detect_kind(t.get('caption'), t.get('heading')) or exams.detect_kind(page.title, entry['url'])
        if not kind: continue
        for eq, row_text in table_equivalencies(kind, t['rows']):
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
        out.append(common.make('credit_policies', inst['institution_key'], year, basis, record, evidence, entry,
                               EXTRACTOR, {'policy_kind': kind}, checks, issues))
    return out
