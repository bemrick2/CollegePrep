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
CHOOSE_N = re.compile(r'\b(?:choose|select|complete|take)\s+(?:any\s+)?(one|two|three|four|five|six|\d)\s+(?:courses?\s+)?(?:of|from)\b|'
                      # Issue #95 (WKU): "Choose two courses at 5 hours each"
                      r'\b(?:choose|select|complete|take)\s+(?:any\s+)?(one|two|three|four|five|six|\d)\s+(?:[\w-]+\s+){0,3}?(?:courses|classes)\b', re.I)
CHOOSE_HOURS = re.compile(r'\b(?:choose|select|complete|take)\s+(?:a\s+minimum\s+of\s+|at\s+least\s+|an?\s+additional\s+)?'
                          r'(\d{1,2}|one|two|three|four|five|six)\s+(?:additional\s+)?(?:semester\s+)?(?:credit\s+)?(?:hours|credits)\b', re.I)
# Issue #95: a printed choice ("Choose from:", "from the following", "(choose one)") whose count could not be read.
CHOICE_CUE = re.compile(r'\bchoose\b|\bselect\b|\bfrom\s+the\s+following\b|\bone\s+of\s+the\s+following\b', re.I)
DEGREE = [('bachelor', r'\bB\.?\s?(S|A|BA|FA|M|SN|SW|AS|ArCH|ED|Mus)\b\.?|(?i:bachelor)'), ('associate', r'\bA\.?\s?(S|A|AS|AT|ST|F\.?A)\b\.?|(?i:associate)')]
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


def courseleaf_tables(page):
    """Courseleaf 'Course List' tables (Code / Title / Hours)."""
    out = []
    for t in page.tables:
        head = [c.strip().lower() for c in (t['rows'][0] if t.get('rows') else [])]
        if (t.get('caption') or '').strip().lower() == 'course list' or head[:2] == ['code', 'title']:
            out.append(t)
    return out


def is_program_page(entry, page):
    return ('preview_program' in (entry.get('url') or '') or bool(re.search(r'^Program:', page.title or ''))
            or bool(courseleaf_tables(page)))


CL_CODE = re.compile(r'^([A-Z]{2,5}(?:/[A-Z]{2,5})*)\s?(\d{3,4}[A-Z]?)$')  # "ENG/FILM 366" (WKU): a cross-listed code


def courseleaf_groups(page):
    """Same shape as groups_from(): one group per Course List table, split at area-header rows."""
    out = []
    # Footnote markers render as a trailing digit ("Introduction to Food Science 1", NC State); the page lists the
    # footnotes as lines holding just that digit. Only those markers are stripped.
    notes = {l.strip() for l in page.lines if re.fullmatch(r'\s*[1-9]\s*', l)}
    unmark = lambda x: re.sub(r'\s+([1-9])(?:,\s*[1-9])*$', lambda m: '' if m.group(1) in notes else m.group(0), x) if notes else x
    for t in courseleaf_tables(page):
        rows = t['rows'][1:] if [c.strip().lower() for c in t['rows'][0]][:2] == ['code', 'title'] else t['rows']
        base = t.get('heading') or t.get('lead') or 'Program Requirements'
        cur = {'heading': base, 'courses': [], 'rules': [], 'total': None}; out.append(cur); first_group = len(out) - 1
        for r in rows:
            cells = [c.strip() for c in r]
            if not any(cells): continue
            first = cells[0]
            m = CL_CODE.match(first)
            if m:
                item = {'code': f'{m.group(1)} {m.group(2)}', 'title': unmark(cells[1]) if len(cells) > 1 else ''}
                if len(cells) > 2 and re.fullmatch(r'[\d.]+(\s*-\s*[\d.]+)?', cells[2]): item['credits'] = _credits(cells[2])
                cur['courses'].append(item); continue
            tm = re.match(r'^total\s+(?:credit\s+)?(?:hours|credits)$', first, re.I)
            if tm and len(cells) > 1 and re.fullmatch(r'\d{1,3}', cells[-1]):
                cur['total'] = int(cells[-1]); cur['rules'].append(' '.join(cells)); continue
            cells[0] = first = unmark(first)
            text = ' '.join(c for c in cells if c)
            if re.match(r'^[A-Z]{2,5}\s?\d{3,4}[A-Z]?\b', first):  # "ENG 382 & ENG 391": a course pairing, kept verbatim
                cur['rules'].append(text[:300]); cur['pairings'] = True; continue
            if len(cells) == 1 or (not re.search(r'\d', ' '.join(cells[1:])) and not re.search(r'select|choose|complete|take|\bor\b', first, re.I)):
                if cur['courses'] or cur['rules']:  # an area header starts the next group of the same table
                    cur = {'heading': f'{base} — {first}'[:200], 'courses': [], 'rules': [], 'total': None}; out.append(cur)
                else:
                    cur['heading'] = f'{base} — {first}'[:200]
                continue
            if cur['courses'] and CHOICE_CUE.search(text): cur['courses_before_choice'] = True  # Issue #95 (UVU, WKU)
            cur['rules'].append(text[:300])  # "Select 1 ... from the list below: 3", "or PE 333" stay verbatim
        kept = [g for g in out[first_group:] if g['courses'] or g['rules']]
        for g in kept: g['table_groups'] = len(kept)  # a table's "Total Hours" is one group's only if it holds one group
    return [g for g in out if g['courses'] or g['rules']]


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
    t = re.sub(r'^Program:\s*', '', page.title or '').split(' < ')[0].split(' - ')[0].split(' | ')[0].strip()  # "| Virginia State University Catalog"
    t = re.sub(r'\s*\((?:[0-9]{2,6}[A-Z]?)(?:,\s*[0-9]{2,6}[A-Z]?)*\)$', '', t)  # Courseleaf codes: "(1752)", "(514P, 514)"
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
        if len(line) <= 300:
            if cur['courses'] and CHOICE_CUE.search(line): cur['courses_before_choice'] = True  # Issue #95
            cur['rules'].append(line)
    return out


def _credits(v):
    v = v.replace('–', '-').replace(' ', '')
    return v if '-' in v else (int(float(v)) if float(v).is_integer() else float(v))


def extract(inst, entry, page, today_year):
    if not is_program_page(entry, page) or common.professional_source(entry, page): return []
    name = program_name(page)
    # Bachelor's and associate programs only: university-wide "Bachelor's Degree Requirements" pages and the
    # Oregon Transfer Module are not programs (OR: UO, SOCC).
    if not name or not credential(name) or re.search(r'\brequirements?\b|transfer\s+module', name, re.I): return []
    year, printed_year = catalog_year(page)
    issues = []
    if year is None:
        return []  # requirement_group/v1 needs the printed catalog year; an unlabeled program page is skipped
    if re.search(r'archived\s+catalog', page.text[:4000], re.I) or year < today_year:
        issues.append(f'stale_year_label:{year}')
    pkey = slug(name)
    src = common.source_of(entry)['url']
    total, groups, skipped, seen = None, [], 0, {}
    courseleaf = bool(courseleaf_tables(page))
    if courseleaf:
        # Each Course List ends with its own subtotal; the degree total is printed as prose ("Total Hours 120").
        # The degree total is prose or a one-cell plan row ("| Total Hours 120", WKU Finish in Four); two-cell rows
        # ("| Total Hours | 42") are course-list subtotals. Every candidate must agree.
        found = {int(m.group(1)) for l in page.lines if l.count('|') <= 1 for m in [TOTAL.match(l.lstrip('| '))]
                 if m and not re.match(r'\s*[-–]\s*\d', l.lstrip('| ')[m.end():])}  # "112-124" is a range (WKU Theatre)
        total = found.pop() if len(found) == 1 else None
    for g in (courseleaf_groups(page) if courseleaf else groups_from(page)):
        h = g['heading']
        if not courseleaf and g['total'] and re.search(r'total', h + ' ' + ' '.join(g['rules']), re.I) and total is None:
            total = g['total']
        text = ' '.join([h] + g['rules'])
        cat = next((c for c, rx in CATEGORY if re.search(rx, h, re.I)), 'other')
        rd = {'schema': 'requirement_group/v1', 'catalog_year': printed_year, 'category': cat, 'source_section': h[:200]}
        mins = HEAD_CREDITS.search(h.split(' — ')[-1])  # a parent heading's "(52 hours)" is not each sub-area's minimum
        n_course = CHOOSE_N.search(text); n_hours = CHOOSE_HOURS.search(text)
        rules_text = ' '.join(g['rules'])
        choice_issues = []
        # Issue #95: a group that prints a required part and a choice part ("Select two ... Required Capstone Course"),
        # or two separate choices, is neither all-required nor one choice; it is held for review rather than split.
        cue_lines = [r for r in g['rules'] if CHOICE_CUE.search(r)]
        if len(cue_lines) > 1 or (cue_lines and any(re.search(r'\brequired\b', r, re.I) and not CHOICE_CUE.search(r) for r in g['rules'])):
            choice_issues.append('mixed_required_and_choice')
        elif g.get('courses_before_choice'):
            # UVU Music, WKU Professional Education: courses printed above "Choose two ... from the following" are
            # required and only the courses below it are the choice; the group is held rather than called one choice.
            choice_issues.append('mixed_required_and_choice')
        if cat == 'concentration': rd['concentration'] = h[:120]
        if g['courses'] and n_course:
            n = (n_course.group(1) or n_course.group(2)).lower()
            rd.update(group_type='choose_courses', choose_count=WORDS.get(n) or int(n), courses=g['courses'])
        elif n_hours:
            n = n_hours.group(1).lower()
            rd.update(group_type='choose_credits', choose_credits=WORDS.get(n) or int(n))
            if g['courses']: rd['courses'] = g['courses']
            elif g['rules']: rd['course_rules'] = g['rules'][:10]
            else: skipped += 1; continue
        elif g['courses'] and re.search(r'elective|\bchoose\b|\bselect\b|options?\b|\blist\s+[A-Z0-9]\b', h.split(' — ')[-1], re.I):
            # "Application Electives I" (NC State): a list to choose from, not courses all required
            rd.update(group_type='elective_pool', courses=g['courses'])
        elif g['courses'] and CHOICE_CUE.search(rules_text):
            # Issue #95 (NC State "Choose from: 3-4"): a choice whose count is not printed in a readable form
            rd.update(group_type='elective_pool', courses=g['courses'])
            choice_issues.append('choice_rule_unparsed')
        elif g['courses']:
            rd.update(group_type='all_required', courses=g['courses'])
        elif re.search(r'elective', h, re.I) and g['rules']:
            rd.update(group_type='elective_pool', course_rules=g['rules'][:10])
        else:
            if not g['total'] or g.get('pairings'): skipped += 1  # a pairing list has no schema shape: reported, not dropped
            continue
        if g['rules'] and 'course_rules' not in rd: rd['rule_text'] = ' '.join(g['rules'])[:800]
        key = slug(h); seen[key] = seen.get(key, 0) + 1
        if seen[key] > 1: key = f'{key}-{seen[key]}'
        rec = {'program_key': pkey, 'requirement_key': key,
               'requirement_kind': KIND.get(cat, 'other'), 'rule_details': rd}
        if g.get('pairings') or any(re.match(r'^\W*or\b', r, re.I) for r in g['rules']):
            rec['_issues'] = ['course_alternatives_in_rule_text']  # "or CHEM 116": the group is not simply all-required
        if choice_issues: rec['_issues'] = rec.get('_issues', []) + choice_issues
        if mins and cat != 'program_total': rec['minimum_credits'] = int(mins.group(1))
        # Issue #95 (WKU Film): a group's own printed "Total Hours 15" outranks a parent heading's "(36 hours)".
        if g.get('total') and g.get('table_groups') == 1 and cat != 'program_total': rec['minimum_credits'] = g['total']
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
        g_issues = list(issues) + g.pop('_issues', [])
        gev = [{'field': 'courses', 'value': c['code'], 'snippet': f"{c['code']} - {c.get('title', '')}"[:200]}
               for c in g['rule_details'].get('courses', [])[:40]] or [{'field': 'section', 'value': g['requirement_key'],
                                                                        'snippet': g['rule_details'].get('source_section', '')}]
        out.append(common.make('degree_requirements', inst['institution_key'], year, basis, g, gev, entry, EXTRACTOR,
                               {'program_key': pkey, 'requirement_key': g['requirement_key']}, {}, g_issues))
    return out
