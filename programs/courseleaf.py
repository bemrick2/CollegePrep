"""CourseLeaf "Plan of Study Grid" tables (the catalog's Sample Plan tab) -> program_plan sequence rows
(`courseleaf_plan/v1`), plus the program record when the page has no "Course List" table for
catalog_program/v1 to read (e.g. OSU Civil Engineering prints its requirements only as the plan).

Rows: a one-cell row names a term or year ("First Year", "Fall"); [code, title, credits] rows are items; a
[_, "Credits", n] row is the printed term subtotal; [_, "Total Credits", n] is the plan total. A code cell
naming one course becomes a course item; joined or alternative cells ("CH 201& CH 204", "CE 383or CE 481")
stay printed text. Nothing is inferred. A page with several grids (one per option) marks every plan
`multiple_plan_grids`, because the grid's option is not reliably labelled -- unless each grid sits under its own
distinct "Bachelor of ..." heading (UO "Degree Map" tables), which then names the plan.
"""
from __future__ import annotations
import re

from pipeline.extractors import common
from pipeline.extractors.catalog import credential, program_name, slug

EXTRACTOR = 'courseleaf_plan/v1'
ONE = re.compile(r'^([A-Z]{1,5})\s(\d{3}[A-Z]?)$')
TERM = re.compile(r'^(first|second|third|fourth|fifth|freshman|sophomore|junior|senior)\s+year$|^year\s+\d$|^(fall|winter|spring|summer)(\s+(term|semester|quarter))?(\s+\d)?$', re.I)

HEADER_CELLS = {'credits', 'milestones', 'hours', 'credit hours'}


def grids(page):
    return [t for t in page.tables if (t.get('caption') or '').strip().lower() in ('plan of study grid', 'degree map')]


def parse_grid(t):
    """UO grids add a Milestones column ('Fall | Milestones | Credits'): a course row is [code, title, milestone,
    credits] and a text row [text, milestone, credits] (the text cell spans two columns). The milestone is kept in its
    own field, never inside the item text. A text row printed with credits only stays a row with empty text."""
    terms, cur, total, milestones = [], None, None, False
    for row in t.get('rows') or []:
        cells = [c.strip() for c in row]
        nonempty = [c for c in cells if c]
        if not nonempty: continue
        if TERM.match(nonempty[0]) and all(c.lower() in HEADER_CELLS for c in nonempty[1:]):  # 'Fall | Milestones | Credits' (UO)
            milestones = milestones or any(c.lower() == 'milestones' for c in nonempty[1:])
            cur = {'term_index': len(terms) + 1, 'label': nonempty[0], 'items': []}; terms.append(cur); continue
        if len(nonempty) >= 2 and nonempty[-2].lower() == 'total credits':
            total = nonempty[-1]; continue
        if len(nonempty) == 2 and nonempty[0].lower() == 'credits':
            if cur is not None: cur['credit_hours'] = nonempty[1]
            continue
        if cur is None: continue
        m = ONE.match(cells[0]) if cells and cells[0] else None
        hours = cells[-1] if len(cells) >= 2 and re.fullmatch(r'\d{1,2}(\s*-\s*\d{1,2})?', cells[-1] or '') else None
        if m:
            item = {'code': f'{m.group(1)} {m.group(2)}', 'title': cells[1] if len(cells) > 2 else ''}
            if hours: item['credits'] = int(hours) if hours.isdigit() else hours
            if milestones and len(cells) == 4 and cells[2]: item['milestone'] = cells[2]
            cur['items'].append(item)
        elif milestones and len(cells) == 3 and (cells[1] or not cells[0]):
            item = {'text': cells[0]}
            if cells[2]: item['credits'] = int(cells[2]) if cells[2].isdigit() else cells[2]
            if cells[1]: item['milestone'] = cells[1]
            cur['items'].append(item)
        else:
            cur['items'].append(' | '.join(nonempty))
    return terms, total


def extract(inst, entry, page, year, year_line, have_program):
    """Candidates for the plan grids of one page; `year` is the printed catalog year label (e.g. '2026-2027')."""
    gs = grids(page)
    if not gs or not year: return []
    acad = f'{year[:4]}-{year[7:9]}'
    name = program_name(page)
    if not name or not credential(name): return []
    pkey = slug(name)
    out = []
    parsed = [parse_grid(t) for t in gs]
    if not have_program:
        prog = {'program_key': pkey, 'program_name': name, 'catalog_year': year, 'program_url': common.source_of(entry)['url'],
                'credential_level': credential(name), 'notes': f'Extracted by {EXTRACTOR} from the published catalog program page.'}
        totals = {t for _, t in parsed if t and t.isdigit()}
        if len(parsed) == 1 and len(totals) == 1: prog['total_credits'] = int(next(iter(totals)))
        out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', prog,
                               [{'field': 'program_name', 'value': name, 'snippet': page.title[:200]},
                                {'field': 'catalog_year', 'value': year, 'snippet': year_line[:200]}], entry, EXTRACTOR, {'program_key': pkey}))
    headings = [(t.get('heading') or '').strip() for t in gs]
    # UO prints one 'Degree Map' per award under its own heading ('Bachelor of Science in Computer Science'): distinct
    # headings label the plans, so several grids are not ambiguous there.
    labelled = len(parsed) > 1 and len(set(headings)) == len(headings) and all(re.search(r'\bbachelor\b', h, re.I) for h in headings)
    for i, (terms, total) in enumerate(parsed, 1):
        if not terms: continue
        if labelled:
            key = slug(headings[i - 1])
        else:
            key = 'sample-plan' if len(parsed) == 1 else f'sample-plan-{i}'
        caption = (gs[i - 1].get('caption') or 'Plan of Study Grid').strip()
        rd = {'schema': 'requirement_group/v1', 'catalog_year': year, 'group_type': 'sequence', 'category': 'recommended_sequence',
              'terms': terms, 'source_section': (headings[i - 1] if labelled else f'Sample Plan: {caption}' + (f' {i} of {len(parsed)}' if len(parsed) > 1 else ''))}
        if total: rd['rule_text'] = f'Total Credits {total} (as printed)'
        rec = {'program_key': pkey, 'requirement_key': key, 'requirement_kind': 'program_plan', 'rule_details': rd}
        ev = [{'field': 'term', 'value': t['label'], 'snippet': f"{t['label']}: {len(t['items'])} items, {t.get('credit_hours', '?')} credits"} for t in terms]
        issues = ['multiple_plan_grids'] if len(parsed) > 1 and not labelled else []
        out.append(common.make('degree_requirements', inst['institution_key'], acad, 'labeled_in_source', rec, ev, entry, EXTRACTOR,
                               {'program_key': pkey, 'requirement_key': key}, {'terms': len(terms)}, issues))
    return out


# ---- Course List tables (courseleaf_list/v1) -------------------------------------------------------------------
# The shared catalog_program/v1 extractor sometimes labels "Select ... from the following" groups all_required
# (issue #95). This reader builds requirement groups from the CourseLeaf "Course List" rows directly and emits only
# what the rows make unambiguous:
#   * consecutive course rows that print their own credits -> one all_required group;
#   * a "Select/Choose ..." row followed by option rows printed WITHOUT credits -> one choose_courses group (a printed
#     course count) or choose_credits group (a printed credit number); the options end at the first row that prints
#     credits, a section heading, or another Select row;
#   * "or CODE" rows join the previous course as {"any_of": [...]}.
# Rows the reader cannot represent exactly (joined "A& B" courses, cross-listed "A/B 101" codes, a Select row whose
# number is not printed, options that print their own credits) put an issue on the group so it is held for review.
LIST_EXTRACTOR = 'courseleaf_list/v1'
SELECT = re.compile(r'^(select|choose|complete)\b', re.I)
LEAD_IN = re.compile(r'^students\s+must\s+(?=(?:take|complete|select|choose)\s+(?:an?\s+additional\s+|at\s+least\s+)?\d{1,2}\s+(?:additional\s+)?'
                     r'(?:credit\s+hours|credits|hours)\s+(?:from|of)\s+the\s+following\b)', re.I)  # WKU Film: 'Students must take an additional 15 credit hours from the following list'
NUMBER_WORDS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
COUNT = re.compile(r'^(?:select|choose|complete|take)\s+(?:(?:a\s+)?(?:minimum|total)\s+of\s+)?(one|two|three|four|five|six|seven|eight|nine|ten|\d+)\s+'
                   r'(?:additional\s+|more\s+|upper[- ]division\s+|lower[- ]division\s+|[A-Z]{2,5}\s+)*(?:courses?|of\s+the\s+following|from\s+the\s+following)\b', re.I)
CREDITS = re.compile(r'^(?:select|choose|complete|take)\s+(?:(?:a\s+)?(?:minimum|total)\s+of\s+(?:at\s+least\s+)?|at\s+least\s+|an\s+additional\s+)?'
                     r'(\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten)(?:\s*-\s*\d{1,2})?\s+(?:additional\s+)?(?:credits?|credit\s+hours|hours|units)\b', re.I)
# 'Complete the following:' (UVU) prints an all-required list, not a choice
ALL_FOLLOWING = re.compile(r'^(?:complete|take)\s+(?:all\s+(?:of\s+)?)?the\s+following(?:\s+(?:courses|requirements))?\s*:?\s*$', re.I)


def _num(w):
    return NUMBER_WORDS.get(w.lower()) or int(w)
# One course code as printed: 'BIOL 101', 'IT222' (Purdue Global prints no space), 'ENGL 1302' / 'DANC 1100R' (TAMUSA, UVU:
# four digits and a suffix letter), 'ENG/FILM 366' (WKU: one cross-listed course, kept as printed so the list is not cut).
CODE = r'[A-Z]{1,5}(?:/[A-Z]{1,5})*\s?\d{3,4}[A-Z]?'
CODE_CELL = re.compile(rf'^{CODE}$')
OR_ROW = re.compile(rf'^or\s+({CODE})$')
# Rows that print more than one course in the code cell are held with a reason naming the shape (issue #95 recovery).
PAIR_CODE = re.compile(r'\d{3,4}[A-Z]?\s*/\s*\d{3,4}')  # 'BIOL 1306/1106' (TAMUSA): a lecture and its lab


def complex_reasons(text):
    if PAIR_CODE.search(text): return {'complex_course_row', 'lecture_lab_pair_code'}
    if '&' in text: return {'complex_course_row', 'joined_courses_row'}
    return {'complex_course_row'}
NOT_REQUIRED_HEADING = re.compile(r'\b(recommended|suggested|electives?|options?|optional|choose|select|sample|example)\b', re.I)
CREDIT_CELL = re.compile(r'^\d{1,2}(\s*-\s*\d{1,2})?$')


def _item(cells):
    item = {'code': cells[0], 'title': cells[1] if len(cells) > 1 else ''}
    cr = cells[2] if len(cells) > 2 else ''
    if CREDIT_CELL.match(cr): item['credits'] = int(cr) if cr.isdigit() else cr
    return item


def course_list_groups(table):
    """[(section, group)] for one Course List table; group = {'group_type', 'courses', 'rule_text'?, 'choose_count'?,
    'choose_credits'?, 'issues'}."""
    out, section, cur = [], (table.get('heading') or '').strip(), None

    def close():
        nonlocal cur
        if cur and not cur['courses'] and cur['group_type'] in ('choose_courses', 'choose_credits') and re.search(r'\b(following|below|list|series|tracks?|options?|groups?|areas?)\b', cur['rule_text'], re.I):
            cur['issues'].add('options_not_read')  # 'Select 2 credits from the following courses' whose list sits under sub-headings
        if cur and not cur['courses'] and cur['group_type'] in ('choose_courses', 'choose_credits') and not cur['issues']:
            # 'Select an additional 7 credits from courses that count toward either major.': a printed rule, no list
            cur = {'group_type': 'elective_pool', 'course_rules': [cur['rule_text']], 'rule_text': cur['rule_text'], 'courses': [], 'issues': set(),
                   **({'choose_credits': cur['choose_credits']} if 'choose_credits' in cur else {})}
            out.append((section, cur)); cur = None; return
        if cur and (cur['courses'] or cur['issues']):  # a group held for review is still reported
            if cur['group_type'] == 'all_required' and NOT_REQUIRED_HEADING.search(f"{table.get('heading') or ''} {section}"):
                cur['issues'].add('heading_not_all_required')  # 'Recommended ... Elective Coursework', 'Options'
            out.append((section, cur))
        cur = None

    for row in table.get('rows') or []:
        cells = [c.strip() for c in row]
        while cells and cells[-1] == '': cells.pop()
        if not cells or cells[:3] == ['Code', 'Title', 'Credits']: continue
        first = cells[0]
        orm = OR_ROW.match(first)
        if orm:
            if cur and cur['courses'] and 'code' in cur['courses'][-1] or (cur and cur['courses'] and 'any_of' in cur['courses'][-1]):
                prev = cur['courses'][-1]
                opts = prev['any_of'] if 'any_of' in prev else [prev]
                cur['courses'][-1] = {'any_of': opts + [{'code': orm.group(1), 'title': cells[1] if len(cells) > 1 else ''}]}
            elif cur is not None:
                cur['issues'].add('alternative_without_course')
            continue
        is_code = bool(CODE_CELL.match(first))
        complex_code = not is_code and bool(re.match(r'^[A-Z]{1,5}[\s/]', first)) and bool(re.search(r'\d{3}', first)) and len(first) < 40
        has_credits = len(cells) >= 2 and bool(CREDIT_CELL.match(cells[-1]))
        if SELECT.match(LEAD_IN.sub('', first)):
            close()
            cnt, crd = COUNT.match(LEAD_IN.sub('', first)), CREDITS.match(LEAD_IN.sub('', first))
            cur = {'rule_text': first + (f' {cells[-1]}' if has_credits else ''), 'courses': [], 'issues': set()}
            if cnt: cur['group_type'] = 'choose_courses'; w = cnt.group(1).lower(); cur['choose_count'] = NUMBER_WORDS.get(w) or int(w)
            elif crd: cur['group_type'] = 'choose_credits'; cur['choose_credits'] = _num(crd.group(1))
            else: cur['group_type'] = 'choose_unclear'; cur['issues'].add('choose_number_not_printed')
            continue
        if is_code or complex_code:
            choosing = cur is not None and cur['group_type'] != 'all_required'
            if choosing and not has_credits:
                if complex_code: cur['issues'] |= complex_reasons(first)
                else: cur['courses'].append(_item(cells))
                continue
            if choosing and has_credits and not cur['courses']:  # 'Select one of the following math pairs' + pairs with credits
                cur['issues'].add('options_print_credits')
                if complex_code: cur['issues'] |= complex_reasons(first)
                else: cur['courses'].append(_item(cells))
                continue
            if cur is None or cur['group_type'] != 'all_required':
                close(); cur = {'group_type': 'all_required', 'courses': [], 'issues': set()}
            if complex_code: cur['issues'] |= complex_reasons(first)
            else:
                cur['courses'].append(_item(cells))
                if not has_credits: cur['issues'].add('required_course_without_credits')
            continue
        # a heading row (text only) or a text requirement row (text + credits) ends the current group
        close()
        if len(cells) == 1: section = first
    close()
    return out


def list_candidates(inst, entry, page, year, year_line, program_key):
    acad = f'{year[:4]}-{year[7:9]}'
    out, n = [], 0
    for t in page.tables:
        if (t.get('caption') or '').strip().lower() != 'course list': continue
        for section, g in course_list_groups(t):
            n += 1
            gt = g['group_type']
            rd = {'schema': 'requirement_group/v1', 'catalog_year': year, 'group_type': gt if gt != 'choose_unclear' else 'elective_pool',
                  'category': 'major_core' if gt == 'all_required' else 'major_elective', 'courses': g['courses'],
                  'source_section': ' — '.join(x for x in ((t.get('heading') or '').strip(), section) if x) if section != (t.get('heading') or '').strip() else section}
            if g.get('rule_text'): rd['rule_text'] = g['rule_text']
            if gt == 'choose_unclear': rd['course_rules'] = [g['rule_text']]
            if g.get('course_rules'): rd['course_rules'] = g['course_rules']
            if not rd['courses']: del rd['courses']
            for k in ('choose_count', 'choose_credits'):
                if k in g: rd[k] = g[k]
            key = f'list-{n}-{slug(section or "requirements")}'[:90]
            rec = {'program_key': program_key, 'requirement_key': key, 'requirement_kind': 'major', 'rule_details': rd}
            ev = [{'field': 'source_section', 'value': section, 'snippet': section[:200]}] + ([{'field': 'rule_text', 'value': g['rule_text'], 'snippet': g['rule_text'][:200]}] if g.get('rule_text') else [])
            out.append(common.make('degree_requirements', inst['institution_key'], acad, 'labeled_in_source', rec, ev, entry, LIST_EXTRACTOR,
                                   {'program_key': program_key, 'requirement_key': key}, {'courses': len(g['courses'])}, sorted(g['issues'])))
    return out


# ---- Course List tables read with their layout (courselist_html/v1) ---------------------------------------------
# Input: programs.courselist_html tables (row classes, leading indentation). Rules (independent review 2026-10-05):
#   * 'areaheader' / 'areasubheader' rows are section headings;
#   * a non-indented course row is required; consecutive ones form one all_required group;
#   * a non-indented rule row (Select / Choose / "N of the following" / "One of the following") opens a choice whose
#     options are the indented rows that follow it; the choice ends at the next non-indented row;
#   * "or ..." rows join the previous course as {"any_of": [...]}; a joined/cross-listed/range code is not representable;
#   * held with an issue: reference or track tables (approved / distribution / area / group / courses offered /
#     recommended / suggested / sample / option / track / concentration / focus / domain / emphasis / honors / elective
#     headings, or a context paragraph saying to select one or more of them), tables naming one award on a page whose
#     program has several, counts at or above the number of listed options, "up to" / "can include" rules, printed
#     credit ranges for a choice, text options, and any row the reader cannot represent exactly.
HTML_EXTRACTOR = 'courselist_html/v1'
RULE_ROW = re.compile(r'^(select|choose|complete|take)\b|^students\s+must\s+(take|complete|select|choose)\s+(an?\s+additional\s+|at\s+least\s+)?\d{1,2}\s+(additional\s+)?(credit\s+hours|credits|hours)\s+(from|of)\s+the\s+following\b|^(one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b.*\b(of|from)\b.*\b(following|list|below)\b|^(one|two|three|four|five|\d+)\s+(courses?\s+)?(of|from)\b', re.I)
REFERENCE_HEADING = re.compile(r'\b(approved|distribution|area\s+[ivx\d]+|group\s+[a-z\d]\b|courses offered|ensembles?|recommended|suggested|sample|example|'
                               r'options?|tracks?|concentrations?|focus|focal|domains?|emphas[ie]s|specialization|honors|electives?|pass/no pass)\b', re.I)
TRACK_HEADING = re.compile(r'\b(options?|tracks?|concentrations?|focus|focal|domains?|emphas[ie]s|specialization|honors)\b', re.I)
CONTEXT_CHOICE = re.compile(r'\b(select|choose|complete)\s+(one|two|at least one|one or more)\b[^.]*\b(focus areas?|tracks?|options?|concentrations?|areas?|domains?|emphases)\b|\bsuggested course combinations\b', re.I)
AWARD_IN_HEADING = re.compile(r'\b(Bachelor of [A-Z][a-z]+|B\.?A\.?|B\.?S\.?|B\.?F\.?A\.?|B\.?M\.?)\b(?![a-z])')
OR_CODE = OR_ROW


def _row(r):
    cells = r.get('cells') or []
    first = cells[0] if cells else {'text': '', 'indent': False}
    text = (first.get('text') or '').strip()
    credits = (cells[-1].get('text') or '').strip() if len(cells) > 1 else ''
    title = (cells[1].get('text') or '').strip() if len(cells) > 2 or (len(cells) == 2 and first.get('colspan', 1) == 1) else ''
    cls = set(r.get('classes') or []) | set(first.get('spans') or [])
    return {'text': text, 'title': title, 'credits': credits if CREDIT_CELL.match(credits) else '', 'indent': bool(first.get('indent')),
            'inner': bool(first.get('inner_indent')) or '&' in text, 'header': bool(cls & {'areaheader', 'areasubheader'}),
            'or': 'orclass' in cls or text.lower().startswith('or '), 'code': bool(CODE_CELL.match(text)),
            'codeish': bool(re.match(r'^[A-Z]{1,5}[\s/]', text)) and bool(re.search(r'\d{3}', text)) and len(text) < 45}


def _course(rw):
    item = {'code': rw['text'], 'title': rw['title']}
    if rw['credits']: item['credits'] = int(rw['credits']) if rw['credits'].isdigit() else rw['credits']
    return item


def html_groups(table, program_awards=1, extra_issues=None):
    """[(section, group)] for one stored course-list table."""
    heading, context = (table.get('heading') or '').strip(), table.get('context') or ''
    out, section, cur = [], '', None
    table_issues = set(extra_issues or ())
    held_until_header = False
    last_text_ended_choice = [None]
    if CONTEXT_CHOICE.search(context): table_issues.add('context_says_choose_among_tables')
    if program_awards > 1 and AWARD_IN_HEADING.search(heading) and not re.search(r'major requirements', heading, re.I):
        table_issues.add('award_specific_table')

    def close():
        nonlocal cur
        if cur is None: return
        g = cur; cur = None
        if not g['courses'] and not g['rules']:
            if g['type'] == 'all_required' and not g['issues']: return  # a row held for its shape is reported, not dropped
            if re.search(r'\b(following|below|list)\b', g.get('rule_text', ''), re.I) or not g.get('rule_text'):
                g['issues'].add('options_not_read')
            else:  # 'Select an additional 7 credits from courses that count toward either major.': a printed rule, no list
                g['type'] = 'choose_unclear'; g['rules_only'] = True
        where = f'{heading} {section}'
        if g['type'] == 'all_required' and REFERENCE_HEADING.search(where) and not re.search(r'\b(major|core) requirements\b', section, re.I):
            g['issues'].add('reference_or_track_heading')  # a list under 'Approved ...' / 'Electives' / 'Option' is not a required list
        elif g['type'] != 'all_required' and TRACK_HEADING.search(where):
            g['issues'].add('track_heading')  # a choice inside one track or option applies only to that track
        if g['type'] == 'choose_courses' and g.get('choose_count', 0) >= len(g['courses']) + len(g['rules']):
            g['issues'].add('count_not_below_options')
        if g.get('rule_text') and re.search(r'\b(up to|can include|may include|at most|or an? (additional|other)|or another|advisor approval|approved by)\b', g['rule_text'], re.I):
            g['issues'].add('rule_mixes_other_courses')
        if g['rules']: g['issues'].add('text_option')
        titles = ' '.join(c.get('title', '') for c in g['courses'] for c in (c.get('any_of') or [c]))
        if SUBSTITUTE.search(titles): g['issues'].add('substitute_in_title')  # '(May be replaced by SOC 207)', '(or above)', '(or)'
        if RULE_ROW.match(section or ''): g['issues'].add('section_label_is_rule')
        if held_until_header: g['issues'].add('after_subheading_inside_choice')
        if g['type'] == 'all_required' and g.get('starts_after_rule'):
            g['issues'].add('follows_rule_without_options')  # 'One of the following:' + unindented courses (UO Math & CS)
        g['issues'] |= table_issues
        out.append((section or heading, g))

    for r in table.get('rows') or []:
        rw = _row(r)
        if not rw['text'] or rw['text'] in ('Code',) or re.match(r'^total (credits|hours)', rw['text'], re.I): continue
        ended_by_text, last_text_ended_choice[0] = last_text_ended_choice[0], None
        if rw['header']:
            sub = 'areasubheader' in (r.get('classes') or [])
            if cur is not None and cur['type'] != 'all_required' and sub:
                cur['issues'].add('subheading_inside_choice')  # 'Group 1 / Group 2' or 'Series' under one rule: structure not representable
                close(); held_until_header = True
            else:
                close()  # the group before a main heading still belongs to the held span
                if not sub: held_until_header = False
            section = rw['text']; continue
        if rw['or']:
            m = OR_CODE.match(rw['text'])
            if cur and cur['courses'] and m:
                prev = cur['courses'][-1]
                opts = prev['any_of'] if 'any_of' in prev else [prev]
                cur['courses'][-1] = {'any_of': opts + [{'code': m.group(1), 'title': rw['title']}]}
            elif cur is not None:
                cur['issues'].add('alternative_not_representable')
            else:
                cur = {'type': 'all_required', 'courses': [], 'rules': [], 'issues': {'alternative_not_representable'}}
            continue
        if not rw['indent']:
            if rw['code'] or rw['codeish']:
                if cur is None or cur['type'] != 'all_required':
                    after_rule = cur is not None and cur['type'] != 'all_required' and not cur['courses'] and not cur['rules']
                    close(); cur = {'type': 'all_required', 'courses': [], 'rules': [], 'issues': set(), 'starts_after_rule': after_rule}
                if rw['code'] and not rw['inner']: cur['courses'].append(_course(rw))
                else: cur['issues'] |= complex_reasons(rw['text'])
                continue
            if ALL_FOLLOWING.match(rw['text']):
                close(); cur = {'type': 'all_required', 'courses': [], 'rules': [], 'issues': set(), 'all_following': True}
                continue
            if RULE_ROW.match(rw['text']):
                close()
                t = rw['text'] + (f" {rw['credits']}" if rw['credits'] else '')
                rule = LEAD_IN.sub('', rw['text'])
                cnt, crd = COUNT.match(rule), CREDITS.match(rule)
                cur = {'type': 'choose_unclear', 'courses': [], 'rules': [], 'issues': set(), 'rule_text': t}
                if cnt: cur['type'] = 'choose_courses'; w = cnt.group(1).lower(); cur['choose_count'] = NUMBER_WORDS.get(w) or int(w)
                elif crd:
                    cur['type'] = 'choose_credits'; cur['choose_credits'] = _num(crd.group(1))
                    if re.search(r'\d\s*-\s*\d', rw['text']): cur['issues'].add('credit_range')
                else:
                    m = re.match(r'^(one|two|three|four|five|six|\d+)\b', rw['text'], re.I)
                    if m: cur['type'] = 'choose_courses'; w = m.group(1).lower(); cur['choose_count'] = NUMBER_WORDS.get(w) or int(w)
                    else: cur['issues'].add('choose_number_not_printed')
                continue
            was_choice = cur is not None and cur['type'] != 'all_required' and not rw['credits']
            close()  # any other non-indented text row (a requirement printed as text) ends the group; it is not a group itself
            if was_choice and out: last_text_ended_choice[0] = out[-1][1]  # if indented rows follow, the text was part of the option list
            continue
        # indented row: an option of the open choice
        if cur is not None and cur['type'] == 'all_required' and cur['courses'] and not cur.get('all_following'):
            cur['issues'].add('indented_rows_after_required_course')  # 'DATA 488 ... (or)' + indented alternatives (Linfield)
        if cur is None and ended_by_text is not None:
            ended_by_text['issues'].add('choice_continues_after_text')  # 'Alternative Approved Courses:' + more options
        if cur is not None and cur.get('all_following') and not cur['rules']:
            pass  # 'Complete the following courses:' + indented courses: all of them are required
        elif cur is None or cur['type'] == 'all_required':
            close(); cur = {'type': 'choose_unclear', 'courses': [], 'rules': [], 'issues': {'indented_rows_without_rule'}}
        if rw['code'] and not rw['inner']: cur['courses'].append(_course(rw))
        elif rw['codeish']: cur['issues'] |= complex_reasons(rw['text'])
        else: cur['rules'].append(rw['text'])
    close()
    return out


SUBSTITUTE = re.compile(r'substitut|replac|in lieu|waiv|exception|equivalent|or above|\(or\b|may count|proficiency|placement', re.I)
MAIN_TABLE = re.compile(r'\b((major|degree|pre-major|program) requirements|curriculum|core)\b', re.I)
PARALLEL = re.compile(r'^(.+?)\s*(\([^)]+\)\s*Major Requirements|Major\s*[-–]\s*.+)$', re.I)
TRACK_PROSE = re.compile(r'\b(choose one track|focus areas?|specializations?|concentrations?|tracks? from|one of the following (tracks|options|concentrations|areas))\b', re.I)
NOT_REQUIREMENT_HEADING = re.compile(r'^(contact information|program educational objectives|double-counting policy|internships?|learning outcomes|'
                                     r'student learning outcomes|program learning outcomes|overview|admission|advising)$', re.I)


def substitution_codes(page_text):
    """Course codes named in the page's own substitution / waiver notes ('MATH 241, MATH 246, or MATH 251Z may be
    substituted'; 'STAT 243Z ... can be taken as substitutes for SOC 312')."""
    codes = set()
    for line in (page_text or '').split('\n'):
        if re.search(r'substitut|in lieu|waive|may be replaced|placement (exam|test)|proficiency (exam|test)', line, re.I):
            found = {re.sub(r'\s+', ' ', m) for m in re.findall(r'\b[A-Z]{2,5}[\s\u00a0]\d{3}[A-Z]?\b', line)}
            codes |= found or {'*footnote*'}  # a note naming no course ('Placement test may waive the course requirement.')
    return codes


FOOTNOTED = re.compile(r'\s\d{1,2}(,\s?\d{1,2})*$')


def html_candidates(inst, entry, cl_entry, tables, year, program_key, program_awards, page_text=''):
    """Table-level holds (second independent review): every Course List table after a page's first is held unless its
    heading names the major/degree requirements, curriculum or core; parallel tables ('Classics (Greek) Major
    Requirements', 'X Major - Y') are all held; once a table's preceding prose says to choose a track / focus area /
    specialization / concentration, that table and every later one is held."""
    acad = f'{year[:4]}-{year[7:9]}'
    out, n = [], 0
    lists = [t for t in tables if (t.get('caption') or 'Course List').strip().lower() == 'course list']
    parallel = sum(1 for t in lists if PARALLEL.match((t.get('heading') or '').strip())) >= 2
    tracks_from_here = False
    for idx, t in enumerate(lists):
        heading = (t.get('heading') or '').strip()
        extra = set()
        if idx > 0 and not MAIN_TABLE.search(heading): extra.add('secondary_table')
        if parallel and PARALLEL.match(heading): extra.add('parallel_tables')
        if CONTEXT_CHOICE.search(t.get('context') or '') or TRACK_PROSE.search(t.get('context') or ''): tracks_from_here = True
        if tracks_from_here: extra.add('context_says_choose_among_tables')
        label = '' if NOT_REQUIREMENT_HEADING.match(heading) else heading
        subs = substitution_codes(page_text)
        for section, g in html_groups(t, program_awards, extra):
            n += 1
            items = [c for x in g['courses'] for c in (x.get('any_of') or [x])]
            if g['type'] == 'all_required' and (subs & {c['code'] for c in items} or
                                                 ('*footnote*' in subs and any(FOOTNOTED.search(c.get('title', '')) for c in items))):
                g['issues'].add('substitution_noted_on_page')  # a footnoted course on a page whose notes allow a waiver or substitute
            gt = {'choose_unclear': 'elective_pool'}.get(g['type'], g['type'])
            rd = {'schema': 'requirement_group/v1', 'catalog_year': year, 'group_type': gt,
                  'category': 'major_core' if gt == 'all_required' else 'major_elective',
                  'source_section': ' — '.join(x for x in dict.fromkeys((label, '' if section == heading else section)) if x) or 'Course List'}
            if g['courses']: rd['courses'] = g['courses']
            if g.get('rule_text'): rd['rule_text'] = g['rule_text']
            rules = ([g['rule_text']] if gt == 'elective_pool' and g.get('rule_text') else []) + g['rules']
            if rules: rd['course_rules'] = rules
            for k in ('choose_count', 'choose_credits'):
                if k in g: rd[k] = g[k]
            key = f'major-{n}-{slug((section if section != heading else "") or label or "requirements")}'[:90]
            rec = {'program_key': program_key, 'requirement_key': key, 'requirement_kind': 'major', 'rule_details': rd}
            ev = [{'field': 'source_section', 'value': rd['source_section'], 'snippet': rd['source_section'][:200]}]
            if g.get('rule_text'): ev.append({'field': 'rule_text', 'value': g['rule_text'], 'snippet': g['rule_text'][:200]})
            c = common.make('degree_requirements', inst['institution_key'], acad, 'labeled_in_source', rec, ev, entry, HTML_EXTRACTOR,
                            {'program_key': program_key, 'requirement_key': key}, {'courses': len(g['courses'])}, sorted(g['issues']))
            c['layout_source'] = {'url': cl_entry['url'], 'sha256': cl_entry.get('sha256')}
            out.append(c)
    return out
