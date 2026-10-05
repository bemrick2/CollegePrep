"""SmartCatalog (smartcatalogiq.com) program pages -> academic_programs + degree_requirements candidates
(`smartcatalog_program/v1`, requirement_group/v1).

Page shape: a breadcrumb line "2026-2027 Bulletin > College > Department > Program", an H1 with the program
name, then requirement headings each followed by a course table whose rows are [code, title, credits] (credits
sometimes on the next line). Headings that name academic years or terms ("Freshman year", "Year 1 Fall") form a
recommended sequence (program_plan). Only printed values are recorded: no inferred totals, prerequisites or
placement. A program page without a printed catalog year in its breadcrumb is skipped.
"""
from __future__ import annotations
import re

from pipeline.extractors import common
from pipeline.extractors.catalog import CATEGORY, HEAD_CREDITS, KIND, slug

EXTRACTOR = 'smartcatalog_program/v1'
CODE = re.compile(r'^([A-Z][A-Za-z]{1,4})\s?(\d{3}[A-Z]?)$')
CRED = re.compile(r'^\d{1,2}(?:\.\d)?(?:\s*[-–]\s*\d{1,2})?$')
TERM = re.compile(r'\b(freshman|sophomore|junior|senior|first|second|third|fourth)\s+year\b|\byear\s+[1-4]\b|\b(fall|spring|winter|summer)\s+(term|semester|quarter)\b', re.I)
TOTAL = re.compile(r'^\W*total\s+(?:credit\s+)?(?:hours|credits)(?:\s+required)?\W*(?:for\s+[^:]+)?:?\s*(\d{2,3})\b', re.I)
# all_required only when the heading itself says the list is required; anything else is a pool to choose from
REQUIRED = re.compile(r'\b(required|requirements|core|major\s+courses|foundation|complete\s+(the\s+)?following|complete\s+all)\b', re.I)
CHOOSE = re.compile(r'\b(choose|select|approved|elective|electives|one\s+of|from\s+the\s+following)\b', re.I)
BACHELOR = re.compile(r'\b(B\.?\s?(A|S|F\.?A|M|S\.?N|S\.?W|A\.?S|Arch|Mus|B\.?A|S\.?[A-Z]{1,3})\b\.?|bachelor)', re.I)
NOT_PROGRAM = re.compile(r'\b(minor|certificate|graduate|master|ph\.?d|m\.?s\.?|m\.?a\.?|admission\s+requirements|objectives|outcomes|courses)\b', re.I)


CRUMB_HEAD = re.compile(r'^(?=[^>]{0,80}(Catalog|Catalogue|Bulletin))[^>]{0,80}?\b(20\d{2})\s*[-–]\s*((?:20)?\d{2})\b[^>]{0,40}>', re.I)


def program_year(page):
    """The year in the breadcrumb's first segment: "2026-2027 Bulletin > ..." (PSU), "Academic Catalog 2026-2027 > ..." (CBU)."""
    for line in page.lines[:400]:
        m = CRUMB_HEAD.match(line.strip())
        first, second = int(m.group(2)) if m else 0, (int(m.group(3)) if m else 0)
        if m and second < 100: second += 2000  # "2026-27 Undergraduate Catalogue" (Union)
        if m and second == first + 1:
            return f'{first}-{second}', line.strip()
    return None, None


def program_name(page):
    title = (page.title or '').split(' - ', 1)[-1].strip()
    return page.headings[0].strip() if page.headings else title


def rows_to_courses(rows):
    courses, rules = [], []
    for r in rows:
        cells = [c.strip() for c in r if c is not None]
        cells = [c for c in cells if c]
        if not cells: continue
        m = CODE.match(cells[0])
        if m:
            item = {'code': f'{m.group(1).upper()} {m.group(2)}', 'title': cells[1] if len(cells) > 1 else ''}
            if len(cells) > 2 and CRED.match(cells[2]):
                v = cells[2].replace('–', '-').replace(' ', '')
                item['credits'] = v if '-' in v else (int(float(v)) if float(v).is_integer() else float(v))
            courses.append(item)
        else:
            rules.append(' '.join(cells)[:300])
    return courses, rules


def extract(inst, entry, page, today_year):
    name = program_name(page)
    if not name or not BACHELOR.search(name) or NOT_PROGRAM.search(name): return []
    year, crumb = program_year(page)
    if year is None: return []
    acad = f'{year[:4]}-{year[7:9]}'
    issues = [] if acad >= today_year else [f'stale_year_label:{acad}']
    pkey = slug(name)
    groups, terms, seen = [], [], {}
    for t in page.tables:
        heading = (t.get('heading') or t.get('lead') or '').strip()
        courses, rules = rows_to_courses(t.get('rows') or [])
        if not courses and not rules: continue
        if TERM.search(heading):
            terms.append({'term_index': len(terms) + 1, 'label': heading[:80],
                          'items': courses + [x for x in rules if x]})
            continue
        if not courses: continue
        cat = next((c for c, rx in CATEGORY if re.search(rx, heading, re.I)), 'major_core')
        rd = {'schema': 'requirement_group/v1', 'catalog_year': year, 'category': cat, 'source_section': heading[:200] or 'Requirements',
              'group_type': 'all_required' if (REQUIRED.search(heading) and not CHOOSE.search(heading)) else 'elective_pool', 'courses': courses}
        if rules: rd['rule_text'] = ' '.join(rules)[:800]
        mins = HEAD_CREDITS.search(heading)
        alternatives = any(re.fullmatch(r'(or|and/or)', r.strip(), re.I) for r in rules)
        if cat == 'concentration': rd['concentration'] = heading[:120]
        key = slug(heading or 'requirements'); seen[key] = seen.get(key, 0) + 1
        if seen[key] > 1: key = f'{key}-{seen[key]}'
        g = {'program_key': pkey, 'requirement_key': key, 'requirement_kind': KIND.get(cat, 'other'), 'rule_details': rd}
        if mins and int(mins.group(1)) > 0: g['minimum_credits'] = int(mins.group(1))
        g['_issues'] = []
        if rd['group_type'] == 'elective_pool' and not CHOOSE.search(heading): g['_issues'].append('group_type_unclear_heading')
        if alternatives: g['_issues'].append('course_alternatives_in_rule_text')  # "MATH 105 OR MATH 111": not simply all required
        groups.append(g)
    if terms:
        groups.append({'program_key': pkey, 'requirement_key': 'recommended-sequence', 'requirement_kind': 'program_plan',
                       'rule_details': {'schema': 'requirement_group/v1', 'catalog_year': year, 'group_type': 'sequence',
                                        'category': 'recommended_sequence', 'terms': terms, 'source_section': 'Requirements'}})
    totals = {int(m.group(1)) for l in page.lines for m in [TOTAL.match(l.strip('| '))] if m}
    total = totals.pop() if len(totals) == 1 else None
    # A program page with no parseable requirement tables still establishes the program (name, award, URL, year).
    src = common.source_of(entry)['url']
    prog = {'program_key': pkey, 'program_name': name, 'catalog_year': year, 'program_url': src, 'credential_level': 'bachelor',
            'notes': f'Extracted by {EXTRACTOR} from the published catalog program page.'}
    if total: prog['total_credits'] = total
    ev = [{'field': 'program_name', 'value': name, 'snippet': name[:200]}, {'field': 'catalog_year', 'value': year, 'snippet': crumb[:200]}]
    checks = {'groups': len(groups), 'terms': len(terms), 'courses': sum(len(g['rule_details'].get('courses', [])) for g in groups)}
    out = [common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', prog, ev, entry, EXTRACTOR,
                       {'program_key': pkey}, checks, issues)]
    for g in groups:
        rd = g['rule_details']
        gev = [{'field': 'courses', 'value': c['code'], 'snippet': f"{c['code']} {c.get('title', '')}"[:200]} for c in rd.get('courses', [])[:40]] \
            or [{'field': 'section', 'value': g['requirement_key'], 'snippet': rd.get('source_section', '')}]
        out.append(common.make('degree_requirements', inst['institution_key'], acad, 'labeled_in_source', g, gev, entry, EXTRACTOR,
                               {'program_key': pkey, 'requirement_key': g['requirement_key']}, {}, list(issues) + g.pop('_issues', [])))
    if total:
        out.append(common.make('degree_requirements', inst['institution_key'], acad, 'labeled_in_source',
                               {'program_key': pkey, 'requirement_key': 'program-total', 'requirement_kind': 'total_credits', 'minimum_credits': total,
                                'rule_details': {'schema': 'requirement_group/v1', 'catalog_year': year, 'group_type': 'credit_total',
                                                 'category': 'program_total', 'rule_text': f'Total credits: {total} (as printed)'}},
                               [{'field': 'total', 'value': total, 'snippet': next(l for l in page.lines if TOTAL.match(l.strip('| ')))[:200]}],
                               entry, EXTRACTOR, {'program_key': pkey, 'requirement_key': 'program-total'}, {}, list(issues)))
    return out
