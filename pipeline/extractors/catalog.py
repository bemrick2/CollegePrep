"""Catalog program pages (Acalog / Modern Campus `preview_program.php`) -> academic_programs +
degree_requirements candidates in the requirement_group/v1 schema (docs/PROGRAM_DATA.md).

A program page is a sequence of headings, each followed by course lines ("ENGL 1010 - Composition I
Credit Hours: 3") and/or rule lines ("Select two of the following", "Total Hours: 120"). Each heading
with recognisable content becomes one requirement group. Only what is printed is recorded: no
prerequisite inference, no credit arithmetic, no course placement. Groups that do not fit the schema
are counted (`groups_skipped`) and the program goes to the exception queue.
"""
from __future__ import annotations
import re

from .. import text as T
from . import common

EXTRACTOR = 'catalog_program/v1'
COURSE = re.compile(r'^\W*([A-Z]{2,5})\s?(\d{3,4}[A-Z]?)\s*[-–—:]\s*(.+?)(?:\s+(?:Credit\s+Hours?|Credits?|Hours?)\s*:?\s*([\d.]+(?:\s*[-–]\s*[\d.]+)?))?\s*$')
CREDIT_ONLY = re.compile(r'^\W*(?:Credit\s+Hours?|Credits?)\s*:?\s*([\d.]+(?:\s*[-–]\s*[\d.]+)?)\s*$', re.I)
TOTAL = re.compile(r'^\W*total\s+(?:credit\s+)?(?:hours|credits|semester\s+hours)(?:\s+required)?\s*(?:for\s+[^:]+)?\s*:?\s*(\d{2,3})\b', re.I)
HEAD_CREDITS = re.compile(r'(\d{1,3})(?:\s*[-–]\s*\d{1,3})?\s*(?:semester\s+)?(?:credit\s+)?(?:hours|credits|hrs?\.?)\b', re.I)
WORDS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
CHOOSE_N = re.compile(r'\b(?:choose|select|complete|take)\s+(?:any\s+)?(one|two|three|four|five|six|\d)\s+(?:courses?\s+)?(?:of|from)\b', re.I)
CHOOSE_HOURS = re.compile(r'\b(?:choose|select|complete|take)\s+(\d{1,2})\s+(?:credit\s+)?(?:hours|credits)\b', re.I)
DEGREE = [('bachelor', r'\bB\.?\s?(S|A|BA|FA|M|SN|SW|AS|ArCH|ED|Mus)\b\.?|bachelor'), ('associate', r'\bA\.?\s?(S|A|AS|AT|ST|F\.?A)\b\.?|associate')]
GRADUATE = re.compile(r'\b(M\.?S|M\.?A|MBA|M\.?Ed|Ph\.?D|Ed\.?D|DNP|graduate|certificate|minor)\b', re.I)
CATEGORY = [
    ('general_education', r'general\s+education|gen\.?\s*ed|core\s+curriculum|university\s+core|tbr\s+core'),
    ('concentration', r'concentration|track|emphasis|option|specialization'),
    ('minor', r'\bminor\b'),
    ('free_elective', r'free\s+electives?|general\s+electives?|unrestricted'),
    ('major_elective', r'(major|program|departmental|restricted)\s+electives?|electives?\s+in\s+the\s+major'),
    ('supporting_coursework', r'support|cognate|related\s+(courses|requirements)|collateral|prerequisite\s+courses'),
    ('major_core', r'major|core|required\s+courses|program\s+requirements|requirements'),
]
KIND = {'general_education': 'general_education', 'major_core': 'major', 'major_elective': 'major', 'concentration': 'major',
        'supporting_coursework': 'major', 'program_total': 'total_credits', 'minor': 'minor'}


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', (s or '').lower()).strip('-')[:80] or 'group'


def is_program_page(entry, page):
    return 'preview_program' in (entry.get('url') or '') or bool(re.search(r'^Program:', page.title or ''))


def catalog_year(page):
    """The catalog's printed year range, e.g. '2026-2027 Undergraduate Catalog'."""
    labels = T.year_labels(page.title + '\n' + '\n'.join(page.lines[:60]))
    if len(labels) == 1:
        y = next(iter(labels)); return y, f'{y[:4]}-{int(y[:4]) + 1}'
    m = re.search(r'(20\d{2})\s*[-–]\s*(20\d{2})\s+(?:undergraduate\s+)?catalog', page.text[:5000], re.I)
    if m and int(m.group(2)) == int(m.group(1)) + 1:
        return T.academic_year(int(m.group(1))), f'{m.group(1)}-{m.group(2)}'
    return None, None


def program_name(page):
    t = re.sub(r'^Program:\s*', '', page.title or '').split(' - ')[0].strip()
    return t or (page.headings[0] if page.headings else '')


def credential(name):
    for level, rx in DEGREE:
        if re.search(rx, name): return level
    return None


def groups_from(page):
    """[(heading, [course items], [rule lines], total)] in page order."""
    heads = set(page.headings)
    out, cur = [], None
    for line in page.lines:
        if line in heads:
            cur = {'heading': line, 'courses': [], 'rules': [], 'total': None}; out.append(cur); continue
        if cur is None: continue
        m = TOTAL.match(line)
        if m: cur['total'] = int(m.group(1)); cur['rules'].append(line); continue
        m = COURSE.match(line)
        if m and len(m.group(3)) <= 160:
            item = {'code': f'{m.group(1)} {m.group(2)}', 'title': re.sub(r'\s*\*+$', '', m.group(3)).strip()}
            if m.group(4): item['credits'] = _credits(m.group(4))
            cur['courses'].append(item); continue
        m = CREDIT_ONLY.match(line)
        if m and cur['courses'] and 'credits' not in cur['courses'][-1]:
            cur['courses'][-1]['credits'] = _credits(m.group(1)); continue
        if len(line) <= 300: cur['rules'].append(line)
    return out


def _credits(v):
    v = v.replace('–', '-').replace(' ', '')
    return v if '-' in v else (int(float(v)) if float(v).is_integer() else float(v))


def extract(inst, entry, page, today_year):
    if not is_program_page(entry, page) or common.professional_source(entry, page): return []
    name = program_name(page)
    if not name or (GRADUATE.search(name) and not credential(name)): return []
    year, printed_year = catalog_year(page)
    issues = []
    if year is None:
        return []  # requirement_group/v1 needs the printed catalog year; an unlabeled program page is skipped
    if re.search(r'archived\s+catalog', page.text[:4000], re.I) or year < today_year:
        issues.append(f'stale_year_label:{year}')
    pkey = slug(name)
    src = common.source_of(entry)['url']
    total, groups, skipped, seen = None, [], 0, {}
    for g in groups_from(page):
        h = g['heading']
        if g['total'] and re.search(r'total', h + ' ' + ' '.join(g['rules']), re.I) and total is None:
            total = g['total']
        text = ' '.join([h] + g['rules'])
        cat = next((c for c, rx in CATEGORY if re.search(rx, h, re.I)), 'other')
        rd = {'schema': 'requirement_group/v1', 'catalog_year': printed_year, 'category': cat, 'source_section': h[:200]}
        mins = HEAD_CREDITS.search(h)
        n_course = CHOOSE_N.search(text); n_hours = CHOOSE_HOURS.search(text)
        if cat == 'concentration': rd['concentration'] = h[:120]
        if g['courses'] and n_course:
            n = n_course.group(1).lower(); rd.update(group_type='choose_courses', choose_count=WORDS.get(n) or int(n), courses=g['courses'])
        elif n_hours:
            rd.update(group_type='choose_credits', choose_credits=int(n_hours.group(1)))
            if g['courses']: rd['courses'] = g['courses']
            elif g['rules']: rd['course_rules'] = g['rules'][:10]
            else: skipped += 1; continue
        elif g['courses']:
            rd.update(group_type='all_required', courses=g['courses'])
        elif re.search(r'elective', h, re.I) and g['rules']:
            rd.update(group_type='elective_pool', course_rules=g['rules'][:10])
        else:
            if not g['total']: skipped += 1
            continue
        if g['rules'] and 'course_rules' not in rd: rd['rule_text'] = ' '.join(g['rules'])[:800]
        key = slug(h); seen[key] = seen.get(key, 0) + 1
        if seen[key] > 1: key = f'{key}-{seen[key]}'
        rec = {'program_key': pkey, 'requirement_key': key,
               'requirement_kind': KIND.get(cat, 'other'), 'rule_details': rd}
        if mins and cat != 'program_total': rec['minimum_credits'] = int(mins.group(1))
        groups.append(rec)
    if not groups: return []
    if skipped: issues.append('requirement_groups_skipped')
    prog = {'program_key': pkey, 'program_name': name, 'catalog_year': printed_year, 'program_url': src,
            'notes': f'Extracted by {EXTRACTOR} from the published catalog program page.'}
    lvl = credential(name)
    if lvl: prog['credential_level'] = lvl
    if total: prog['total_credits'] = total
    if total:
        groups.append({'program_key': pkey, 'requirement_key': 'program-total', 'requirement_kind': 'total_credits',
                       'minimum_credits': total, 'rule_details': {'schema': 'requirement_group/v1', 'catalog_year': printed_year,
                       'group_type': 'credit_total', 'category': 'program_total', 'rule_text': f'Total hours: {total} (as printed)'}})
    basis = 'labeled_in_source'
    ev = [{'field': 'program_name', 'value': name, 'snippet': page.title[:200]}]
    if total: ev.append({'field': 'total_credits', 'value': total, 'snippet': next((l for l in page.lines if TOTAL.match(l)), '')[:200]})
    checks = {'groups': len(groups), 'groups_skipped': skipped, 'courses': sum(len(g['rule_details'].get('courses', [])) for g in groups)}
    out = [common.make('academic_programs', inst['institution_key'], year, basis, prog, ev, entry, EXTRACTOR,
                       {'program_key': pkey}, checks, issues)]
    for g in groups:
        gev = [{'field': 'courses', 'value': c['code'], 'snippet': f"{c['code']} - {c.get('title', '')}"[:200]}
               for c in g['rule_details'].get('courses', [])[:40]] or [{'field': 'section', 'value': g['requirement_key'],
                                                                        'snippet': g['rule_details'].get('source_section', '')}]
        out.append(common.make('degree_requirements', inst['institution_key'], year, basis, g, gev, entry, EXTRACTOR,
                               {'program_key': pkey, 'requirement_key': g['requirement_key']}, {}, list(issues)))
    return out
