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
WORDS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12}
CHOOSE_N = re.compile(r'\b(?:choose|select|complete|take)\s+(?:any\s+)?(one|two|three|four|five|six|\d)\s+(?:courses?\s+)?(?:of|from)\b|'
                      # Issue #95 (WKU): "Choose two courses at 5 hours each"
                      r'\b(?:choose|select|complete|take)\s+(?:any\s+)?(one|two|three|four|five|six|\d)\s+(?:[\w-]+\s+){0,3}?(?:courses|classes)\b', re.I)
CHOOSE_HOURS = re.compile(r'\b(?:choose|select|complete|take)\s+(?:a\s+minimum\s+of\s+|at\s+least\s+|an?\s+additional\s+)?'
                          r'(\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s+(?:additional\s+)?(?:semester\s+)?(?:credit\s+)?(?:hours|credits)\b', re.I)
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


# Issue #95 recovery: a CourseLeaf group that prints a required part and printed choices is split into one group per part,
# in printed order. Only what the source prints is recorded; anything the rows cannot settle is named in the group's issues.
REQUIRED_CUE = re.compile(r'^(?:complete|take)\s+(?:all\s+)?(?:of\s+)?the\s+following(?:\s+(?:courses?|requirements))?\s*:?\s*$', re.I)
OR_ALTERNATIVE = re.compile(r'^or\s+([A-Z]{2,5}(?:/[A-Z]{2,5})*)\s?(\d{3,4}[A-Z]?)\b\s*(.*)$')
SUBTOTAL = re.compile(r'^\W*(?:sub)?total\b', re.I)
ACROSS_AREAS = re.compile(r'\bfrom\s+\d+\s+of\s+the\s+\d+\b|\beach\s+of\s+the\s+following\s+areas\b|\bfrom\s+each\b|\bdifferent\s+discipline', re.I)
CHOOSE_TAIL = re.compile(r'\b(?:choose|select)\s+(one|two|three|four|five|six|\d)\s*\)?\s*:?\s*$', re.I)  # NC State "Electives (select two):"
SECTION_LABEL = re.compile(r'^\d{1,3}\s+credits?$', re.I)  # UVU "Discipline Core Requirements | 24 Credits": a label over the parts below
CREDIT_CELL = re.compile(r'^\d{1,2}(?:\s*-\s*\d{1,2})?(?:\s+credits?)?$', re.I)


def split_choice_group(g):
    """[{'kind': 'required'|'choice'|'area', 'cue', 'courses', 'rules', 'issues'}] for a mixed CourseLeaf group.

    A row that prints a choice ("Select one of the following:", "Complete 6 credits from the following courses:") opens a
    choice; its members are the course rows that follow without hours of their own (the hours sit on the choice row).
    A course row that prints its own hours after the members ends the choice: it is required. "Complete the following:"
    opens a required part. "or X" rows are an alternative to the course above them ({"any_of": [...]}). A row that
    prints an area and hours but no courses ("Creative Arts 3", "Unrestricted Electives 12") is its own part. Subtotal
    rows close the current part."""
    segs, cur, label = [], None, None

    def start(kind, cue=None, credits=None):
        seg = {'kind': kind, 'cue': cue, 'credits': credits, 'courses': [], 'rules': [], 'issues': [], 'label': label}
        if option: seg['issues'].append('option_area_within_choice')  # one option of a printed choice, not a requirement of its own
        segs.append(seg); return seg

    option, last_area = g.get('option_of'), None
    for e in g.get('seq', []):
        prev_area, last_area = last_area, None
        if e[0] == 'course':
            item = dict(e[1])
            if cur is not None and cur['kind'] == 'choice':
                # members print no hours of their own; when the first member does (NC State "Choose from:"), where the
                # list ends cannot be read from the rows, so the rest stays in the choice and the part is held
                if not cur['courses'] or 'credits' not in item or 'choice_list_end_unclear' in cur['issues']:
                    if not cur['courses'] and 'credits' in item: cur['issues'].append('choice_list_end_unclear')
                    cur['courses'].append(item); continue
                cur = start('required')  # a course with its own hours after the choice's members: required
            elif cur is None or cur['kind'] == 'area':
                cur = start('required')
            cur['courses'].append(item)
            if re.search(r'\brecommended\b', item.get('title', ''), re.I) and 'recommended_course_not_required' not in cur['issues']:
                cur['issues'].append('recommended_course_not_required')  # UVU "PHYS 1750 ... (recommended)" under a distribution area
        elif e[0] == 'pairing':
            if cur is None or cur['kind'] != 'choice': cur = start('required')
            cur['rules'].append(e[1])
            if 'course_pairings' not in cur['issues']: cur['issues'].append('course_pairings')
        elif e[0] == 'total':
            cur = None
        else:
            text, cells = e[1], e[2]
            m = OR_ALTERNATIVE.match(text)
            if m and cur is not None and cur['courses']:
                last = cur['courses'][-1]
                alt = {'code': f'{m.group(1)} {m.group(2)}', **({'title': m.group(3).strip()} if m.group(3).strip() else {})}
                cur['courses'][-1] = {'any_of': (last['any_of'] if 'any_of' in last else [last]) + [alt]}
                continue
            if m:  # an alternative with no course above it in this part
                (cur or start('required'))['issues'].append('alternative_without_course')
                continue
            if SUBTOTAL.match(text):
                cur, option, label = None, None, ''; continue  # '' = a new section after the subtotal
            hours = next((c for c in reversed(cells[1:]) if c and CREDIT_CELL.match(c)), None)
            if hours and SECTION_LABEL.match(hours) and not (CHOICE_CUE.search(cells[0]) or CHOOSE_HOURS.search(cells[0])):
                label = cells[0].strip(); cur = None; continue
            if REQUIRED_CUE.match(cells[0]):
                cur = start('required', cue=cells[0]); continue
            if CHOICE_CUE.search(cells[0]) or CHOOSE_HOURS.search(cells[0]):
                if prev_area and (hours is None or re.sub(r'\D', '', hours) == re.sub(r'\D', '', prev_area[1].split()[-1])):
                    # "Restricted Electives 10" right above "Select 10 hours from ...: 10": the area names this choice
                    seg_a, area_text = prev_area; seg_a['areas'].remove(area_text)
                    if not seg_a['areas']: segs.remove(seg_a)
                    label = re.sub(r'\s+\d{1,3}(?:\s+credits?)?$', '', area_text, flags=re.I)
                cur = start('choice', cue=cells[0].strip(), credits=hours); continue
            if hours:  # areas printed with hours but no course list ("Creative Arts 3"): one part per consecutive run
                if cur is None or cur['kind'] != 'area':
                    cur = start('area', cue=text); cur['issues'].append('area_requirement_without_course_list'); cur['areas'] = []
                cur['areas'].append(text); last_area = (cur, text); continue
            seg = cur or start('required'); seg['rules'].append(text)
            if re.search(r'\brecommended\b', text, re.I) and 'recommended_courses_listed' not in seg['issues']:
                seg['issues'].append('recommended_courses_listed')  # UVU "Strongly Recommended:" above advice, not the pool
    return [s for s in segs if s['courses'] or s['rules'] or s['kind'] in ('choice', 'area')]


def choice_shape(seg):
    """(rule_details fields, issues) for one part of a split group."""
    issues = list(seg['issues']); cue = seg['cue'] or ''
    if seg['kind'] == 'required':
        if not seg['courses']: return None, issues
        rd = {'group_type': 'all_required', 'courses': seg['courses']}
        if seg['rules']: rd['rule_text'] = ' '.join(seg['rules'])[:800]
        return rd, issues
    if seg['kind'] == 'area':
        return {'group_type': 'elective_pool', 'course_rules': seg['areas'][:10]}, issues
    if ACROSS_AREAS.search(cue): issues.append('choice_across_areas_or_minimum')
    n_course, n_hours = CHOOSE_N.search(cue) or CHOOSE_TAIL.search(cue), CHOOSE_HOURS.search(cue)
    listed = seg['courses']
    if n_course and not n_hours:
        n = (n_course.group(1) or n_course.group(2)).lower(); count = WORDS.get(n) or int(n)
        rd = {'group_type': 'choose_courses', 'choose_count': count}
        hours = seg['credits']
        if hours and re.fullmatch(r'\d{1,2}', hours) and (int(hours) % count or int(hours) // count > 6):
            issues.append('printed_count_and_credits_disagree')
    elif n_hours:
        n = n_hours.group(1).lower(); rd = {'group_type': 'choose_credits', 'choose_credits': WORDS.get(n) or int(n)}
    else:
        rd = {'group_type': 'elective_pool'}; issues.append('choice_rule_unparsed')
    if listed: rd['courses'] = listed
    elif rd['group_type'] == 'choose_courses':  # a count of courses with no list printed: the printed rule is the pool
        rd = {'group_type': 'elective_pool'}
        if not issues: issues.append('choice_without_course_list')
    rules = ([cue] if not listed else []) + seg['rules']
    if rules: rd['course_rules'] = rules[:10]
    if rd['group_type'] == 'elective_pool' and not (listed or rules): rd['course_rules'] = [cue]
    rd['rule_text'] = (cue + (f' {seg["credits"]}' if seg['credits'] else ''))[:800]
    return rd, issues


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
        cur = {'heading': base, 'courses': [], 'rules': [], 'total': None, 'seq': []}; out.append(cur); first_group = len(out) - 1
        option_of = pending_option = None  # a header that prints a choice ("Prescribed Electives (Choose 9 hours)"): the areas below are its options
        for ri, r in enumerate(rows):
            cells = [c.strip() for c in r]
            if not any(cells): continue
            first = cells[0]
            m = CL_CODE.match(first)
            if m:
                item = {'code': f'{m.group(1)} {m.group(2)}', 'title': unmark(cells[1]) if len(cells) > 1 else ''}
                if len(cells) > 2 and re.fullmatch(r'[\d.]+(\s*-\s*[\d.]+)?', cells[2]): item['credits'] = _credits(cells[2])
                cur['courses'].append(item); cur['seq'].append(('course', item)); continue
            tm = re.match(r'^total\s+(?:credit\s+)?(?:hours|credits)$', first, re.I)
            if tm and len(cells) > 1 and re.fullmatch(r'\d{1,3}', cells[-1]):
                cur['total'] = int(cells[-1]); cur['rules'].append(' '.join(cells)); cur['seq'].append(('total', ' '.join(cells)))
                cur['open_choice'] = False; option_of = None; continue
            cells[0] = first = unmark(first)
            text = ' '.join(c for c in cells if c)
            if re.match(r'^[A-Z]{2,5}\s?\d{3,4}[A-Z]?\b', first):  # "ENG 382 & ENG 391": a course pairing, kept verbatim
                cur['rules'].append(text[:300]); cur['pairings'] = True; cur['seq'].append(('pairing', text[:300])); continue
            header = len(cells) == 1 or (not re.search(r'\d', ' '.join(cells[1:])) and not re.search(r'select|choose|complete|take|\bor\b', first, re.I))
            nxt = next(([c.strip() for c in x] for x in rows[ri + 1:] if any(c.strip() for c in x)), [])
            member_next = bool(nxt) and bool(CL_CODE.match(nxt[0])) and not (len(nxt) > 2 and nxt[2])  # a course printed without its own hours
            if header and first.endswith(':') and cur.get('open_choice') and member_next:
                # UVU "CAPSTONE COURSE:" inside "Complete 15 credits from the following courses": a label within the choice's list
                cur['rules'].append(text[:300]); cur['seq'].append(('rule', text[:300], cells)); continue
            if header:
                if cur['courses'] or cur['rules']:  # an area header starts the next group of the same table
                    cur = {'heading': f'{base} — {first}'[:200], 'courses': [], 'rules': [], 'total': None, 'seq': []}; out.append(cur)
                else:
                    cur['heading'] = f'{base} — {first}'[:200]
                if CHOICE_CUE.search(first) or CHOOSE_HOURS.search(first): option_of = first
                elif pending_option: option_of = pending_option  # TAMUSA "Prescribed Electives (Choose 9 hours)" then area headers
                if option_of and not (CHOICE_CUE.search(first) or CHOOSE_HOURS.search(first)): cur['option_of'] = option_of
                pending_option = None
                continue
            pending_option = None
            if SUBTOTAL.match(first): option_of = None; cur['open_choice'] = False
            if CHOICE_CUE.search(text) or CHOOSE_HOURS.search(first):
                cur['open_choice'] = True
                if not re.search(r'\d', ' '.join(cells[1:])): pending_option = first  # a choice row with no hours of its own
            if cur['courses'] and CHOICE_CUE.search(text): cur['courses_before_choice'] = True  # Issue #95 (UVU, WKU)
            cur['rules'].append(text[:300])  # "Select 1 ... from the list below: 3", "or PE 333" stay verbatim
            cur['seq'].append(('rule', text[:300], cells))
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
    if not name or not credential(name) or re.search(r'\brequirements?\b|transfer\s+module|\baccelerated\b', name, re.I): return []  # IL r1: Roosevelt's BS/MS accelerated pages list only the shared graduate courses
    year, printed_year = catalog_year(page)
    issues = []
    if year is None:
        return []  # requirement_group/v1 needs the printed catalog year; an unlabeled program page is skipped
    # an archived-catalog banner marks the page stale; a standalone 'Archived Catalogs' menu link (Stetson's nav) does not
    if re.search(r'archived\s+catalog(?!s\s*$)', page.text[:4000], re.I | re.M) or year < today_year:
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
        if len(cue_lines) > 1 or (cue_lines and any((re.search(r'\brequired\b', r, re.I) or REQUIRED_CUE.match(r)) and not CHOICE_CUE.search(r) for r in g['rules'])):
            choice_issues.append('mixed_required_and_choice')
        elif g.get('courses_before_choice'):
            # UVU Music, WKU Professional Education: courses printed above "Choose two ... from the following" are
            # required and only the courses below it are the choice; the group is held rather than called one choice.
            choice_issues.append('mixed_required_and_choice')
        if cat == 'concentration': rd['concentration'] = h[:120]
        parts = []
        if courseleaf and g.get('seq') and cue_lines:
            # Issue #95 recovery: one group per printed part instead of one misstated shape. A group that reads as one
            # clean part keeps the single-group path below.
            parts = [(seg,) + choice_shape(seg) for seg in split_choice_group(g)]
            parts = [(seg, shape, iss) for seg, shape, iss in parts if shape]
            if not ('mixed_required_and_choice' in choice_issues or len(parts) > 1 or any(iss for _, _, iss in parts)): parts = []
            if len(parts) == 1 and parts[0][2] == ['course_pairings']: parts = []  # a pairing list alone keeps its old handling (reported, skipped)
        if parts:
            own = next((i for i, (_, _, iss) in enumerate(parts) if not iss), 0)  # the group's own key: its first clean part
            for i, (seg, shape, iss) in enumerate(parts):
                label = seg['cue'] or ('Required' if seg['kind'] == 'required' else '')
                key = slug(h) if i == own else f'{slug(h)}-{i + 1}-{slug(label)[:40]}'
                seen[key] = seen.get(key, 0) + 1
                if seen[key] > 1: key = f'{key}-{seen[key]}'
                # a part under a printed section label (or after a subtotal) is named by the table heading and that label
                top = h.split(' — ')[0] if seg['label'] is not None else h
                section = ' — '.join(x for x in (top, seg['label'], label if (i != own or seg['label'] is not None) else None) if x)
                prd = {'schema': 'requirement_group/v1', 'catalog_year': printed_year, 'category': cat, 'source_section': section[:200], **shape}
                if cat == 'concentration': prd['concentration'] = h[:120]
                prec = {'program_key': pkey, 'requirement_key': key, 'requirement_kind': KIND.get(cat, 'other'), 'rule_details': prd}
                if iss: prec['_issues'] = iss
                prec['_split_of'] = slug(h)
                groups.append(prec)
            continue
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
        flat = [o for c in g['rule_details'].get('courses', []) for o in (c['any_of'] if 'any_of' in c else [c])]  # "X or Y" options
        gev = [{'field': 'courses', 'value': c['code'], 'snippet': f"{c['code']} - {c.get('title', '')}"[:200]}
               for c in flat[:40]] or [{'field': 'section', 'value': g['requirement_key'],
                                                                        'snippet': g['rule_details'].get('source_section', '')}]
        split_of = g.pop('_split_of', None)
        out.append(common.make('degree_requirements', inst['institution_key'], year, basis, g, gev, entry, EXTRACTOR,
                               {'program_key': pkey, 'requirement_key': g['requirement_key']}, {'split_of': split_of} if split_of else {}, g_issues))
    return out
