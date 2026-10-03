"""Four-year plan / academic map documents -> academic_programs + degree_requirements candidates.

Many schools publish one PDF per program: a year-labeled title, the program name, a term-by-term
plan laid out in two columns ("Fall Semester:  Hrs   Spring Semester:  Hrs") and a summary of hour
requirements (UTC "Clear Path for Advising", MTSU "Academic Map", Tennessee Tech "Degree Map").

What is recorded, all copied as printed:
  - the plan as one requirement_group/v1 `sequence` row; each term keeps its printed subtotal and its
    items in order. An item is a course ("CPSC 1100: Fundamentals of Computer Science", 4) when it
    starts with one course code, otherwise the printed text ("Humanities and Fine Arts (3-4)").
  - the hour summary lines ("120 Total Hours", "30 Hours at UTC", "34-40 General Education Hours").
Nothing is inferred: a plan's item order is the school's suggestion, not a requirement, and items
are never summed. A document without a printed academic year is skipped.
"""
from __future__ import annotations
import re

from .. import text as T
from . import common
from .catalog import credential, slug

EXTRACTOR = 'program_map/v1'
TITLE_HINT = re.compile(r'clear\s+path|academic\s+map|degree\s+map|four[- ]year\s+(?:plan|map)|4[- ]year\s+plan|program\s+map|'
                        r'plan\s+of\s+study|curriculum\s+map|suggested\s+(?:course\s+)?sequence|finish\s+in\s+four', re.I)
YEAR_HEAD = re.compile(r'^\s*(First|Second|Third|Fourth|Fifth|Freshman|Sophomore|Junior|Senior)\s+Year\b(.*)$', re.I)
TERM_HEAD = re.compile(r'(Fall|Spring|Summer)(?:\s+Semester|\s+Term)?\s*:?', re.I)
HOURS = r'\d{1,2}(?:\s*-\s*\d{1,2})?'
TRAIL_HOURS = re.compile(r'^(.*?\S)?\s{2,}(' + HOURS + r')\s*$|^\s*(' + HOURS + r')\s*$')
COURSE_ITEM = re.compile(r'^([A-Z]{2,5}\s?\d{3,4}[A-Z]?(?:/\d{3,4}[A-Z]?)?)\s*[:\-–]\s*(.+)$')
SUMMARY = re.compile(r'(?<![\w-])(\d{1,3}(?:\s*-\s*\d{1,3})?)\s+((?:Total|Upper\s+Division(?:\s*\([^)]*\))?|General\s+Education|Program\s*\(Major\)|'
                     r'Major|Minor/Concentration|Minor|Concentration|Elective)\s+Hours|Hours\s+at\s+\w[\w&.\- ]*?(?=\s{2,}|\*|$))', re.I)


def _norm_hours(h):
    return re.sub(r'\s+', '', h)


def _split(line, cols):
    """Two-column line -> (left, right) using the header's column positions."""
    right_at = cols['right']
    if len(line) <= right_at - 4: return line, ''
    # A left-column hours token can run into the right column ("0-3 Elective (3000-4000 Level)").
    m = re.match(r'^(.*?\S)?(\s+)(' + HOURS + r')(\s+)(\S.*)$', line)
    if m and abs(m.start(3) - cols['left_hrs']) <= 4 and m.start(5) >= right_at - 6:
        return line[:m.end(3)], m.group(5)
    k = right_at - 4
    while k < len(line) and not (line[k] != ' ' and line[k - 2:k] == '  '): k += 1
    return line[:k], line[k:]


def _column(fragments):
    """[text-or-hours fragments] -> [(item_text, hours)], plus the printed subtotal."""
    items, subtotal, wrapped = [], None, False
    for text, hours in fragments:
        text = text.strip()
        last = items[-1] if items else None
        if text and hours is None:
            # A cell printed on two lines puts its hours on a line of their own between them
            # ("CPEN 3700: Digital Logic and Introduction to Computer" / "4" / "Hardware").
            cont = last and (last[1] is None or wrapped or text[:1] in '(,;' or text[:1].islower()
                             or last[0].count('(') > last[0].count(')') or re.search(r'(\bor|\band|:)$', last[0]))
            wrapped = False
            if cont: last[0] = f'{last[0]} {text}'
            else: items.append([text, None])
            continue
        wrapped = False
        if text:
            if last and last[1] is None and (text[:1] in '(' or text[:1].islower()):
                last[0] = f'{last[0]} {text}'; last[1] = hours
            else: items.append([text, hours])
        elif hours is not None:
            if last and last[1] is None: last[1] = hours; wrapped = True
            else: subtotal = hours
    return [(t, h) for t, h in items], subtotal


def _item(text, hours):
    m = COURSE_ITEM.match(text)
    if m and not re.search(r'\bor\b', m.group(2)):
        return {'code': re.sub(r'\s+', ' ', m.group(1)), 'title': m.group(2).strip(), 'credits': hours if '-' in hours else int(hours)} \
            if hours else {'code': m.group(1), 'title': m.group(2).strip()}
    return f'{text} ({hours})' if hours else text


def parse_plan(lines):
    """Terms in order: [{label, credit_hours, items}]. Returns (terms, summary lines)."""
    terms, cols, year_label, cur = [], None, None, None
    summary = []
    for raw in lines:
        line = raw.rstrip()
        if re.match(r'^\s*(Completed:|Graduation\s+Requirements|Degree\s+Requirements)', line, re.I):
            cur = 'summary'
        if cur == 'summary':
            summary.append(line); continue
        y = YEAR_HEAD.match(line)
        if y:
            year_label = y.group(1).title() + ' Year'; cur = None; continue
        heads = list(TERM_HEAD.finditer(line))
        if year_label and len(heads) >= 1 and re.search(r'\bHrs\b|\bHours\b|Semester', line):
            hrs = [m.start() for m in re.finditer(r'\bHrs\b|\bHours\b', line)]
            cur = {'terms': [], 'frags': []}
            cols = {'left_hrs': hrs[0] if hrs else len(line), 'right': heads[1].start() if len(heads) > 1 else 10 ** 6,
                    'right_hrs': hrs[1] if len(hrs) > 1 else None}
            for h in heads[:2]:
                t = {'label': f'{year_label} {h.group(1).title()}', 'items': [], 'credit_hours': None}
                terms.append(t); cur['terms'].append(t); cur['frags'].append([])
            continue
        if not isinstance(cur, dict) or not line.strip(): continue
        if line.lstrip().startswith('*'): continue  # footnotes
        parts = _split(line, cols) if len(cur['terms']) > 1 else (line, '')
        for i, part in enumerate(parts[:len(cur['terms'])]):
            if not part.strip(): continue
            m = TRAIL_HOURS.match(part.rstrip())
            if not m and i == 1 and cols.get('right_hrs'):
                tight = re.match(r'^(.*\S)\s(' + HOURS + r')\s*$', part.rstrip())
                if tight and abs(len(line.rstrip()) - len(tight.group(2)) - cols['right_hrs']) <= 3:
                    cur['frags'][i].append((tight.group(1), _norm_hours(tight.group(2)))); continue
            if m and m.group(3): cur['frags'][i].append(('', _norm_hours(m.group(3))))
            elif m: cur['frags'][i].append((m.group(1) or '', _norm_hours(m.group(2))))
            else: cur['frags'][i].append((part, None))
        for t, frags in zip(cur['terms'], cur['frags']):
            items, subtotal = _column(frags)
            t['items'] = [_item(x, h) for x, h in items]
            t['credit_hours'] = subtotal
    return [t for t in terms if t['items']], summary


def program_title(lines):
    for line in lines[:6]:
        clean = re.sub(r'\s{2,}.*$', '', line.strip())  # drop the right-aligned year
        clean = re.sub(r'^.*?(clear\s+path\s+for\s+advising|academic\s+map|degree\s+map|four[- ]year\s+plan)\s*[–:-]?\s*', '', clean, flags=re.I)
        clean = re.sub(r'^20\d{2}\s*[–-]\s*(?:20)?\d{2}\s*', '', clean).strip(' –-')
        if clean and credential(clean): return clean
    return None


def extract(inst, entry, page, today_year):
    if entry.get('kind') != 'pdf' or common.professional_source(entry, page): return []
    head = '\n'.join(page.lines[:6])
    if not TITLE_HINT.search(head + ' ' + (entry.get('url') or '')): return []
    labels = T.year_labels(head)
    if len(labels) != 1: return []  # requirement_group/v1 needs the printed catalog year
    year = next(iter(labels)); printed = f'{year[:4]}-{int(year[:4]) + 1}'
    name = program_title(page.lines)
    if not name: return []
    terms, summary = parse_plan(page.text.splitlines())
    if len(terms) < 4: return []  # a plan has at least two years of terms
    issues = [f'stale_year_label:{year}'] if year < today_year else []
    pkey = slug(name)
    rd = lambda **k: {'schema': 'requirement_group/v1', 'catalog_year': printed, **k}
    seq = [{'term_index': i + 1, 'label': t['label'], 'credit_hours': t['credit_hours'], 'items': t['items']} for i, t in enumerate(terms)]
    for t in seq:
        if t['credit_hours'] is None: t.pop('credit_hours')
    rows = [{'program_key': pkey, 'requirement_key': 'four-year-plan', 'requirement_kind': 'program_plan',
             'rule_details': rd(group_type='sequence', category='recommended_sequence', terms=seq,
                                rule_text='Recommended term sequence as printed; generic slots (e.g. "Humanities and Fine Arts") '
                                          'are general-education placeholders, not specific courses.')}]
    found = {}
    for line in summary:
        for m in SUMMARY.finditer(line):
            found.setdefault(re.sub(r'\s+', ' ', m.group(2)).strip(), (m.group(1).replace(' ', ''), line.strip()))
    total = None
    for label, (val, line) in found.items():
        lo = int(val.split('-')[0])
        low = label.lower()
        if low.startswith('total'):
            total = lo if '-' not in val else None
            rows.append({'program_key': pkey, 'requirement_key': 'program-total', 'requirement_kind': 'total_credits', 'minimum_credits': lo,
                         'rule_details': rd(group_type='credit_total', category='program_total', rule_text=f'{val} {label} (as printed)')})
        elif low.startswith('upper division'):
            rows.append({'program_key': pkey, 'requirement_key': 'upper-division-hours', 'requirement_kind': 'other', 'minimum_credits': lo,
                         'rule_details': rd(group_type='credit_total', category='university_requirement', rule_text=f'{val} {label} (as printed)')})
        elif low.startswith('hours at'):
            key = 'residency-hours' if '4-year' not in low and 'four-year' not in low else 'four-year-institution-hours'
            rows.append({'program_key': pkey, 'requirement_key': key, 'requirement_kind': 'residency', 'minimum_credits': lo,
                         'rule_details': rd(group_type='residency_rule', category='university_requirement', rule_text=f'{label}: {val} (as printed)')})
        elif low.startswith('general education'):
            rows.append({'program_key': pkey, 'requirement_key': 'gen-ed-hours', 'requirement_kind': 'general_education', 'minimum_credits': lo,
                         'rule_details': rd(group_type='credit_total', category='general_education', rule_text=f'{val} {label} (as printed)')})
        elif low.startswith('program') or low == 'major hours':
            rows.append({'program_key': pkey, 'requirement_key': 'major-hours', 'requirement_kind': 'major', 'minimum_credits': lo,
                         'rule_details': rd(group_type='credit_total', category='major_core', rule_text=f'{val} {label} (as printed)')})
    src = common.source_of(entry)['url']
    prog = {'program_key': pkey, 'program_name': name, 'catalog_year': printed, 'program_url': src,
            'notes': f'Extracted by {EXTRACTOR} from the published program map; terms and hours copied as printed.'}
    lvl = credential(name)
    if lvl: prog['credential_level'] = lvl
    if total: prog['total_credits'] = total
    out = [common.make('academic_programs', inst['institution_key'], year, 'labeled_in_title', prog,
                       [{'field': 'program_name', 'value': name, 'snippet': head[:300]}], entry, EXTRACTOR, {'program_key': pkey},
                       {'terms': len(seq), 'summary_lines': len(found)}, issues)]
    for r in rows:
        ev = [{'field': 'terms', 'value': len(seq), 'snippet': ' | '.join(t['label'] for t in seq)[:300]}] if r['requirement_key'] == 'four-year-plan' else \
             [{'field': 'minimum_credits', 'value': r.get('minimum_credits'), 'snippet': next((l for v, l in found.values()
                                                                                              if r['rule_details']['rule_text'].split(' ')[0] in l), '')[:300]}]
        out.append(common.make('degree_requirements', inst['institution_key'], year, 'labeled_in_title', r, ev, entry, EXTRACTOR,
                               {'program_key': pkey, 'requirement_key': r['requirement_key']}, {}, issues))
    return out
