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
    terms, cur, total = [], None, None
    for row in t.get('rows') or []:
        cells = [c.strip() for c in row]
        nonempty = [c for c in cells if c]
        if not nonempty: continue
        if TERM.match(nonempty[0]) and all(c.lower() in HEADER_CELLS for c in nonempty[1:]):  # 'Fall | Milestones | Credits' (UO)
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
            cur['items'].append(item)
        else:
            cur['items'].append(' | '.join(nonempty)[:300])
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
