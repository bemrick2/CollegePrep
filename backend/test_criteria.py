"""Numeric ACT/SAT criteria read from an award's published test_requirement text (issue #37 CR-11).

Only what the text states is returned. ACT and SAT are read separately and never converted into
each other. A value is returned only when every number in the text belongs to a labelled ACT or SAT
figure and all parts state the same kind of criterion:
  single_minimum  "Minimum 31 ACT / 1390 SAT", "ACT 30+ / SAT 1360+", "ACT 28 and above"
  range           "ACT 30-36 / SAT 1360-1600", "22-23 ACT or 1100-1150 SAT"
  test_optional   the text says no test is needed
A bare figure ("ACT 27", "30 ACT Score") does not say whether it is a minimum or a band, so it stays
unclassified, as does anything else ambiguous. Unclassified means kind None: read the criteria.
"""
import re

NUM = r'(\d{2,4})(?:\s*-\s*(\d{2,4}))?'
OPEN = r'(\s*\+|\s*(?:and|or|&)\s+(?:above|higher|greater|better))?'
LABEL_FIRST = re.compile(r'\b(act|sat)\b\s*(?:composite|score)?\s*(?:of\s+)?:?\s*' + NUM + OPEN, re.I)
LABEL_AFTER = re.compile(NUM + r'(\s*\+)?\s*(?:composite\s+)?(act|sat)\b', re.I)
MINIMUM = re.compile(r'\b(?:minimum|min\.?|at\s+least)\b', re.I)
OPTIONAL = re.compile(r'test[- ]optional|no\s+test\s+(?:score\s+)?(?:is\s+)?required|without\s+(?:a\s+)?test\s+score', re.I)
PAIR = re.compile(r'^\s*act\s*/\s*sat\s*(?:scores?)?\s*:?\s*' + NUM + OPEN + r'\s*/\s*' + NUM + OPEN + r'\s*$', re.I)
GPA = re.compile(r'\bgpa\s*:?\s*\d\.\d{1,2}(?:\s*-\s*\d\.\d{1,2}|\+)?|\d\.\d{1,2}(?:\s*-\s*\d\.\d{1,2}|\+)?\s*gpa\b', re.I)
SCALE = {'act': (1, 36), 'sat': (400, 1600)}


def _valid(exam, n):
    lo, hi = SCALE[exam]
    return lo <= n <= hi and (exam == 'act' or n % 10 == 0)


def parse(text):
    """Return {kind, act_min, act_max, sat_min, sat_max}; kind None means unclassified."""
    out = {'kind': None, 'act_min': None, 'act_max': None, 'sat_min': None, 'sat_max': None}
    if not text or not text.strip():
        return out
    t = re.sub(r'[‐-―]', '-', text)
    if OPTIONAL.search(t):
        if not re.search(r'\d', t):
            out['kind'] = 'test_optional'
        return out
    if '*' in t:
        return out  # footnoted criteria depend on text this field does not carry
    parts, spans = {}, []
    pair = PAIR.match(t)
    if pair:
        parts = {'act': (int(pair.group(1)), int(pair.group(2)) if pair.group(2) else None, bool(pair.group(3))),
                 'sat': (int(pair.group(4)), int(pair.group(5)) if pair.group(5) else None, bool(pair.group(6)))}
        spans = [(0, len(t))]
    spans += [m.span() for m in GPA.finditer(t)]
    for rx, first in ((LABEL_FIRST, True), (LABEL_AFTER, False)):
        for m in rx.finditer(t):
            if any(m.start() < e and s < m.end() for s, e in spans):
                continue
            exam = (m.group(1) if first else m.group(4)).lower()
            lo, hi, plus = (m.group(2), m.group(3), m.group(4)) if first else (m.group(1), m.group(2), m.group(3))
            if exam in parts:
                return out
            parts[exam] = (int(lo), int(hi) if hi else None, bool(plus))
            spans.append((m.start(), m.end()))
    if not parts:
        return out
    # An alternative path outside the test figures ("24-27 ACT or National Merit") means the test is not required.
    labelled = [(s, e) for s, e in spans if not GPA.fullmatch(t[s:e])]
    first, last = min(s for s, _ in labelled), max(e for _, e in labelled)
    if any(m.start() < first or m.end() > last for m in re.finditer(r'\bor\b', t, re.I)):
        return out
    # Every number must belong to a labelled figure.
    rest = ''.join(ch for i, ch in enumerate(t) if not any(s <= i < e for s, e in spans))
    if re.search(r'\d', rest):
        return out
    minimum = bool(MINIMUM.search(rest))
    kinds = set()
    for exam, (lo, hi, plus) in parts.items():
        if not _valid(exam, lo) or (hi is not None and (not _valid(exam, hi) or hi <= lo)):
            return out
        if hi is not None:
            if plus or minimum:
                return out
            kinds.add('range')
        elif plus or minimum:
            kinds.add('single_minimum')
        else:
            return out
    if len(kinds) != 1:
        return out
    out['kind'] = kinds.pop()
    for exam, (lo, hi, _) in parts.items():
        out[exam + '_min'] = lo
        out[exam + '_max'] = hi
    return out
