"""Candidates from a program-depth run (`programs/runs/<STATE>/<run-id>/`).

Outputs (all deterministic for a given run directory):
  program_lists.json   per institution: every program link found on current-catalog list/navigation pages,
                       with the anchor text exactly as printed, the credential level it states, and the source.
  candidates.jsonl     academic_programs + degree_requirements candidates from program pages and degree
                       maps, produced by the national pipeline's own extractors (catalog_program/v1,
                       program_map/v1), imported unchanged.
  evidence.jsonl       verbatim sentences relevant to CR-14 (direct admission, apply-to-major, pre-major,
                       progression GPA, undeclared, declare-by, change of major, CIP codes, major-specific
                       scholarships). Evidence is review input only: nothing here is a record.
  summary.json         per-institution fetch and extraction counts, used by programs/audit.py.

Extraction never infers: a program's absence from a list is not recorded as "not offered"; a sentence is
copied as printed with its URL and document hash; the credential level comes only from the printed name.
"""
from __future__ import annotations
import hashlib, json, re
from collections import defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

from pipeline import text as T
from pipeline.crawl import Run
from pipeline.extractors import catalog as CAT, programmap as PM, common
from .crawl import program_rule, in_scope

GRAD = re.compile(r'\b(M\.?\s?S\.?|M\.?\s?A\.?|MBA|M\.?\s?Ed|M\.?\s?F\.?A|Ph\.?\s?D|Ed\.?\s?D|DNP|D\.?\s?P\.?\s?T|J\.?\s?D|'
                  r'Master|Doctor|Graduate|Post[- ]?bacc|Certificate|Minor|Endorsement)\b', re.I)
BACHELOR = re.compile(r'\b(B\.?\s?(A|S|F\.?A|M|S\.?N|S\.?W|B\.?A|S\.?E|S\.?E\.?E|S\.?M\.?E|S\.?C\.?E|Arch|Mus|A\.?S|A\.?A\.?S|S\.?Ed|I\.?S)\b\.?|'
                      r'Bachelor|\bH?BA\b|\bH?BS\b)', re.I)
ASSOCIATE = re.compile(r'\b(A\.?\s?(A|S|A\.?S|A\.?T|S\.?T|F\.?A)\b\.?|Associate)', re.I)

NOT_BACHELOR_URL = re.compile(r'(^|[/_-])(min|minor|minors|cert|certificate|certificates|grad|graduate|masters?|phd|doctoral)([/_-]|$)', re.I)
# 'Accounting Major' in an undergraduate catalog: a major whose degree (BA/BS) the list does not print
MAJOR = re.compile(r'\bmajor\b', re.I)
NOT_MAJOR = re.compile(r'\b(minor|certificate|graduate|second\s+major|majors\))', re.I)

EVIDENCE = [
    ('direct_admission', re.compile(r'\bdirect(ly)?[\s-]+admi(t|ts|tted|ssion|ssions)\b|\badmitted\s+directly\b', re.I)),
    ('apply_to_major', re.compile(r'\b(apply|application|applying)\s+(for|to)\s+(admission\s+(to|into)\s+)?(the\s+|a\s+)?'
                                  r'(major|program|professional|upper[\s-]*division|nursing|school|college|bba|bsn|engineering)|'
                                  r'\badmission\s+(to|into)\s+the\s+(major|program|professional|upper[\s-]*division|nursing|school)|'
                                  r'\b(competitive|selective)\s+admission|\bspace[\s-]+limited\b|\blimited\s+enrollment\b', re.I)),
    ('pre_major', re.compile(r'\bpre[\s-](major|nursing|engineering|business|professional|health|computer)', re.I)),
    ('progression', re.compile(r'\b(progression|progress\s+to|continu(e|ation)\s+in\s+the\s+(major|program)|good\s+standing\s+in\s+the\s+major|'
                               r'opt[\s-]+in(to)?\b.{0,80}\bupper[\s-]*division|upper[\s-]*division\s+(admission|courses?|coursework|standing)|'
                               r'admitted\s+(formally\s+)?to\s+(your|the|their)\s+(major|program|department)|restricted,?\s+upper[\s-]*division)', re.I)),
    ('open_declaration', re.compile(r'\b(may|can)\s+(declare|choose|select)\b.{0,80}\b(at\s+any\s+time|anytime|upon\s+(admission|enrollment)|after\s+enrolling)|'
                                    r'\bautomatic(ally)?\s+admi(ssion|tted)\b|\bopen\s+to\s+all\s+students\b', re.I)),
    ('gpa_requirement', re.compile(r'\b(minimum|cumulative|overall|combined|institutional)\b[^.]{0,60}\bG\.?P\.?A\.?\b[^.]{0,30}\b[1-4]\.\d{1,2}\b|'
                                   r'\b[1-4]\.\d{1,2}\b[^.]{0,30}\b(cumulative|overall|minimum)?\s*G\.?P\.?A', re.I)),
    ('undeclared', re.compile(r'\b(undeclared|undecided|exploratory|explor(e|ing)\s+(majors|options|studies)|academic\s+focus)\b', re.I)),
    ('declare_by', re.compile(r'\bdeclare\s+(a|their|your)?\s*major\b[^.]{0,80}\b(by|before|no\s+later|prior\s+to|within|upon)\b', re.I)),
    ('change_major', re.compile(r'\b(change\s+(of\s+)?(a\s+|their\s+|your\s+)?majors?|changing\s+(their\s+|your\s+)?majors?|'
                                r'internal\s+transfer|intra[\s-]*university\s+transfer|transfer\s+(into|to)\s+(the|another)\s+(major|college|school))\b', re.I)),
    ('exam_credit_in_program', re.compile(r'\b(Advanced\s+Placement|AP\s+(exam|credit|score)|International\s+Baccalaureate|IB\s+(exam|credit)|CLEP|dual[\s-](credit|enrollment))\b', re.I)),
    ('cip_code', re.compile(r'\bCIP\b[^0-9]{0,20}\d{2}\.\d{2,4}|\b\d{2}\.\d{4}\b(?=[^\n]{0,80}\b(B\.?S|B\.?A|Bachelor)\b)')),
    ('major_scholarship', re.compile(r'scholarships?\b[^.]{0,120}\b(engineering|computer|computing|business|finance|accounting|nursing|'
                                     r'psycholog|STEM|majors?\s+in)\b|\b(engineering|computer|computing|business|finance|nursing|psycholog)\w*\b[^.]{0,80}scholarships?', re.I)),
]
SENT_SPLIT = re.compile(r'(?<=[.!?])\s+(?=[A-Z(“"])')


def sentences(page):
    for line in page.lines:
        if len(line) < 25: continue
        for s in SENT_SPLIT.split(line):
            s = s.strip(' |')
            if 25 <= len(s) <= 600: yield s


def credential_of(name):
    if GRAD.search(name) and not BACHELOR.search(name): return None
    if BACHELOR.search(name): return 'bachelor'
    if ASSOCIATE.search(name): return 'associate'
    return None


YEAR_LABEL = re.compile(r'\b(20\d{2})\s*[-–]\s*(20\d{2})\s+(?:Undergraduate\s+|University\s+|Academic\s+|General\s+)?(Catalog|Catalogue|Bulletin)\b', re.I)

LABEL_FIRST = re.compile(r'(?:Catalog|Catalogue|Bulletin)\s+(20\d{2})\s*[-–]\s*(20\d{2})(?=\s*(?:>|$))', re.I)
EDITION = re.compile(r'(20\d{2})\s*[-–]\s*(\d{2})\s+Edition', re.I)
ARCHIVE_LINK = re.compile(r'\s*(?:Download\s+)?PDF of\b', re.I)  # "PDF of the entire 2025-2026 Catalog": a download link, not this page's label


def printed_catalog_years(page):
    """Catalog year labels printed anywhere on the page ("2026-2027 Catalog" in a CourseLeaf footer,
    "2026-2027 Bulletin > ..." in a SmartCatalog breadcrumb), excluding 'Select a Catalog' archive menus."""
    found = set()
    for line in page.lines:
        if len(line) > 160 or ARCHIVE_LINK.match(line): continue
        for m in YEAR_LABEL.finditer(line):
            if int(m.group(2)) == int(m.group(1)) + 1: found.add((f'{m.group(1)}-{m.group(2)}', line.strip()))
        m = LABEL_FIRST.match(line.strip())  # Linfield header "Catalog 2026-2027"; UP breadcrumb "Bulletin 2026-2027 > ..."
        if m and int(m.group(2)) == int(m.group(1)) + 1: found.add((f'{m.group(1)}-{m.group(2)}', line.strip()))
        m = EDITION.fullmatch(line.strip())  # Lewis & Clark header: "2026-27 Edition"
        if m and int(m.group(2)) == (int(m.group(1)) + 1) % 100: found.add((f'{m.group(1)}-{int(m.group(1)) + 1}', line.strip()))
    menu = sum(1 for l in page.lines if re.fullmatch(r'20\d{2}-20\d{2}\s+(Catalog|Catalogue|Bulletin)', l.strip(), re.I))
    if menu >= 3:  # an archive selector lists every year; only labels used in context (breadcrumb, footer) count
        found = {(y, l) for y, l in found if not re.fullmatch(r'20\d{2}-20\d{2}\s+(Catalog|Catalogue|Bulletin)', l, re.I)}
    return found


def printed_line(page, anchor):
    """The list page's own line for a link when it adds the awards: 'Accounting: BA, BS' (UO)."""
    for line in page.lines:
        if line.startswith(anchor) and len(line) > len(anchor) and re.match(r'^\s*[:(,–-]', line[len(anchor):]) and len(line) < 200:
            return line
    return None


def collect_lists(target, run, entries):
    """Program links on the current catalog's list pages (configured `program_lists`; Acalog navigation pages
    otherwise), deduplicated by URL, each with the text exactly as printed."""
    is_program = program_rule(target)
    cat_filter = (target.get('catalog') or {}).get('list_filter')
    have_lists = any(e.get('role') == 'program_list' and e.get('page_file') for e in entries)
    out, years = {}, set()
    for e in entries:
        roles = ('program_list',) if have_lists else ('catalog_home', 'catalog_nav')
        if e.get('role') not in roles or not e.get('page_file'): continue
        page, d = run.load_page(e['page_file'])
        y, printed = CAT.catalog_year(page)
        if printed: years.add(printed)
        else: years |= {y for y, _ in printed_catalog_years(page)}
        for href, anchor in d.get('links', []):
            name = re.sub(r'\s+', ' ', anchor or '').strip()
            if not name or len(name) > 200 or not in_scope(target, href): continue
            line = printed_line(page, name)
            if not (is_program(href) or line): continue
            label = line or name
            if cat_filter and not re.search(cat_filter, label): continue
            if NOT_BACHELOR_URL.search(urlsplit(href).path):  # UO minors repeat the major's anchor text: /min-anthropology/
                label = name
            if href not in out:
                level = None if NOT_BACHELOR_URL.search(urlsplit(href).path) else credential_of(label)
                listed_as = level or ('major' if MAJOR.search(label) and not NOT_MAJOR.search(label) else None)
                out[href] = {'name': name, 'printed': label, 'url': href, 'credential_level': level, 'listed_as': listed_as,
                             'listed_on': e['url'], 'listed_on_sha256': e.get('sha256'), 'listed_on_title': e.get('title', '')}
    progs = sorted(out.values(), key=lambda p: p['name'].lower())
    return {'printed_years': sorted(years), 'programs': progs,
            'counts': {'links': len(progs), 'bachelor': sum(p['credential_level'] == 'bachelor' for p in progs),
                       'major_unlabeled_degree': sum(p['listed_as'] == 'major' for p in progs),
                       'associate': sum(p['credential_level'] == 'associate' for p in progs),
                       'unclassified': sum(p['credential_level'] is None for p in progs)}}


def program_page_candidates(target, inst, entry, page, today_year):
    """catalog_program/v1 (Acalog, CourseLeaf) unchanged; when it finds no printed year in the page header but the
    page itself prints exactly one catalog year label elsewhere (CourseLeaf footer "2026-2027 Catalog"), the same
    extractor runs on a view of the page whose title carries that label, and every candidate records it as an issue
    with the verbatim line. SmartCatalog pages use programs.smartcatalog."""
    plat = (target.get('catalog') or {}).get('platform')
    if plat == 'smartcatalog':
        from . import smartcatalog
        return smartcatalog.extract(inst, entry, page, today_year)
    if plat == 'drupal':
        return static_program_identity(inst, entry, page, today_year)
    if plat == 'coursedog':
        return coursedog_page_identity(inst, entry, page, today_year, target.get('_catalog_year'))
    out = CAT.extract(inst, entry, page, today_year)
    y0, printed0 = CAT.catalog_year(page)
    year, line = printed0, (page.title or '')
    if not out and y0 is None:
        labels = printed_catalog_years(page)
        if len({y for y, _ in labels}) == 1:
            year, line = min(labels)
            view = T.Page(page.text, f'{CAT.program_name(page)} - {year} Catalog', page.tables, page.links, page.headings)
            out = CAT.extract(inst, entry, view, today_year)
            for c in out:  # the year is printed on this same document (e.g. CourseLeaf footer): labeled in source, with its line as evidence
                c['evidence'] = c.get('evidence', []) + [{'field': 'catalog_year', 'value': year, 'snippet': line[:200],
                                                          'note': 'catalog year label printed outside the page header'}]
    if not out and plat in ('courseleaf', 'acalog'):
        out = stated_major_identity(inst, entry, page, today_year)
    if plat == 'courseleaf' and year:
        from . import courseleaf
        have = any(c['domain'] == 'academic_programs' for c in out)
        plan = courseleaf.extract(inst, entry, page, year, line, have)
        if have and plan:  # plan rows must use the program key the program candidate uses
            pk = next(c['record']['program_key'] for c in out if c['domain'] == 'academic_programs')
            for c in plan: c['record']['program_key'] = pk
        out += plan
    return out


def static_program_identity(inst, entry, page, today_year):
    """Static HTML catalogs (George Fox, Rhodes): the program record only (name as printed in the page heading, the
    bachelor award it names, the catalog year printed on the page). Requirement lists are not read here."""
    name = (page.headings[0] if page.headings else (page.title or '').split(' | ')[0]).strip()
    if credential_of(name) != 'bachelor' or OPTION_NAME.search(name): return []
    labels = {y for y, _ in printed_catalog_years(page)}
    if len(labels) != 1: return []
    year = next(iter(labels)); line = next(l for y, l in printed_catalog_years(page) if y == year)
    acad = f'{year[:4]}-{year[7:9]}'
    rec = {'program_key': CAT.slug(name), 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year,
           'program_url': common.source_of(entry)['url'], 'notes': 'Program heading and catalog year as printed on the catalog page.'}
    issues = [] if acad >= today_year else [f'stale_year_label:{acad}']
    return [common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                        [{'field': 'program_name', 'value': name, 'snippet': name}, {'field': 'catalog_year', 'value': year, 'snippet': line[:200]}],
                        entry, 'static_program/v1', {'program_key': rec['program_key']}, {}, issues)]


STATED_BACHELOR = re.compile(r'[^.\n]*\bthis major is available as an? (bachelor of [^.\n]*?) degree\b[^.\n]*\.', re.I)


def stated_major_identity(inst, entry, page, today_year):
    """'Accounting Major' pages (Linfield) print no award in the name but state it in a sentence: "This major is
    available as a bachelor of arts or bachelor of science degree, ...". The program record keeps the name as printed;
    the award sentence is its credential evidence and goes into the notes verbatim. No sentence, no record."""
    name = CAT.program_name(page).strip()
    if not re.search(r'\bmajor\b', name, re.I) or re.search(r'\bminor\b', name, re.I) or OPTION_NAME.search(name): return []
    m = STATED_BACHELOR.search(page.text)
    labels = printed_catalog_years(page)
    if not m or len({y for y, _ in labels}) != 1: return []
    year, line = min(labels); sentence = m.group(0).strip()
    acad = f'{year[:4]}-{year[7:9]}'
    rec = {'program_key': CAT.slug(name), 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year,
           'program_url': common.source_of(entry)['url'],
           'notes': f'Program name as printed; award as stated on the program page: "{sentence}"'}
    issues = [] if acad >= today_year else [f'stale_year_label:{acad}']
    return [common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                        [{'field': 'program_name', 'value': name, 'snippet': (page.title or name)[:200]},
                         {'field': 'credential_level', 'value': 'bachelor', 'snippet': sentence[:300]},
                         {'field': 'catalog_year', 'value': year, 'snippet': line[:200]}],
                        entry, 'stated_major/v1', {'program_key': rec['program_key']}, {}, issues)]


def major_table_candidates(target, inst, run, es, today_year):
    """A catalog's own table of majors (Lewis & Clark "Majors and Minors": Major | Minor | Discipline, an X marking
    each major) plus the catalog's own statement of the one bachelor's award its undergraduate majors lead to
    (`award_statement`: url + verbatim quote, checked here against the stored page). Each row marked in the Major
    column becomes a program record named as printed. Student-designed majors are not field programs."""
    cat = target.get('catalog') or {}
    conf, aw = cat.get('major_table'), cat.get('award_statement')
    if not conf or not aw: return []
    page_of = {e['url']: e for e in es if e.get('page_file')}
    te, ae = page_of.get(conf), page_of.get(aw['url'])
    if not te or not ae: return []
    tpage, apage = run.load_page(te['page_file'])[0], run.load_page(ae['page_file'])[0]
    if re.sub(r'\s+', ' ', aw['quote']) not in re.sub(r'\s+', ' ', apage.text): return []
    labels = printed_catalog_years(tpage)
    if len({y for y, _ in labels}) != 1: return []
    year, line = min(labels); acad = f'{year[:4]}-{year[7:9]}'
    out = []
    for t in tpage.tables:
        rows = t.get('rows') or []
        head = [c.strip().lower() for c in rows[0]] if rows else []
        if 'major' not in head or 'discipline' not in head: continue
        mi, di = head.index('major'), head.index('discipline')
        for row in rows[1:]:
            if len(row) <= max(mi, di) or row[mi].strip().upper() != 'X': continue
            name = row[di].strip()
            if not name or re.search(r'student[- ]designed', name, re.I): continue
            rec = {'program_key': CAT.slug(name), 'program_name': name, 'credential_level': aw.get('credential', 'bachelor'), 'catalog_year': year,
                   'program_url': common.source_of(te)['url'],
                   'notes': f'Marked as a major in the catalog\'s Majors and Minors table; award as stated in the catalog ({aw["url"]}): "{aw["quote"]}".'}
            issues = [] if acad >= today_year else [f'stale_year_label:{acad}']
            out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                                   [{'field': 'program_name', 'value': name, 'snippet': ' | '.join(c.strip() for c in row)[:200]},
                                    {'field': 'credential_level', 'value': rec['credential_level'], 'snippet': aw['quote'][:300], 'source_url': aw['url'], 'sha256': ae.get('sha256')},
                                    {'field': 'catalog_year', 'value': year, 'snippet': line[:200]}],
                                   te, 'major_table/v1', {'program_key': rec['program_key']}, {}, issues))
    return out


PRINTED_DEGREE = re.compile(r'^([A-Z][^*†]+?),\s*((?:B\.[A-Za-z.]+)(?:,\s*B\.[A-Za-z.]+)*)$')


def printed_list_candidates(target, inst, run, es, today_year):
    """A catalog page that prints every undergraduate degree as "Name, Award[, Award]" under one heading (UP Bulletin
    "Undergraduate Programs": "Biology, B.S., B.A."; "Civil Engineering, B.S.C.E."). Each such line under the heading
    becomes a program record named as printed; the program URL is the line's own link when the page links it, else
    the list page. Combined bachelor/master lines and post-baccalaureate degrees do not match the pattern."""
    conf = (target.get('catalog') or {}).get('printed_list')
    if not conf: return []
    le = next((e for e in es if e['url'] == conf['url'] and e.get('page_file')), None)
    if not le: return []
    page = run.load_page(le['page_file'])[0]
    labels = printed_catalog_years(page)
    if len({y for y, _ in labels}) != 1: return []
    year, line = min(labels); acad = f'{year[:4]}-{year[7:9]}'
    lines = [l.strip() for l in page.lines]
    starts = [i for i, l in enumerate(lines) if l == conf['heading']]
    if not starts: return []
    stop = conf.get('stop')
    by_text = defaultdict(set)
    for u, txt in page.links:
        if txt.strip(): by_text[txt.strip()].add(u)
    links = {t: next(iter(us)) for t, us in by_text.items() if len(us) == 1}  # 'Economics' links two programs: use neither
    out = []
    for l in lines[starts[-1] + 1:]:  # the last occurrence: the first is the table-of-contents entry
        if stop and l == stop: break
        m = PRINTED_DEGREE.match(l)
        if not m: continue
        name = l; key = CAT.slug(name)
        rec = {'program_key': key, 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year,
               'program_url': links.get(m.group(1).strip(), common.source_of(le)['url']),
               'notes': f'Printed under "{conf["heading"]}" on the catalog page that lists every undergraduate program.'}
        out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                               [{'field': 'program_name', 'value': name, 'snippet': name}, {'field': 'catalog_year', 'value': year, 'snippet': line[:200]}],
                               le, 'printed_list/v1', {'program_key': key}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}']))
    return out


LISTED_MAJOR = re.compile(r'^(.*?\bMajor \([^)]*\))')


def listed_location_candidates(target, inst, run, es, listed, today_year):
    """A branch campus whose programs are the parent university's catalog programs (OSU-Cascades): the parent catalog's
    Programs page tags each program with the campuses that offer it, and `list_filter` keeps the rows tagged with this
    campus. Each bachelor row becomes a program record for the campus, named as printed (up to the award list), linking
    the parent catalog's program page; the tagged row is the evidence."""
    tag = (target.get('catalog') or {}).get('list_filter')
    if not tag: return []
    page_of = {e['url']: e for e in es if e.get('page_file')}
    out = []
    for p in listed.get('programs', []):
        if p.get('credential_level') != 'bachelor' or tag not in p.get('printed', ''): continue
        m = LISTED_MAJOR.match(p['printed'])
        le = page_of.get(p.get('listed_on'))
        if not m or not le: continue
        labels = printed_catalog_years(run.load_page(le['page_file'])[0])
        if len({y for y, _ in labels}) != 1: continue
        year, line = min(labels); acad = f'{year[:4]}-{year[7:9]}'; name = m.group(1).strip()
        rec = {'program_key': CAT.slug(name), 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year, 'program_url': p['url'],
               'notes': f'Listed on the catalog Programs page with the campus tag "{tag}".'}
        out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                               [{'field': 'program_name', 'value': name, 'snippet': p['printed'][:300]},
                                {'field': 'catalog_year', 'value': year, 'snippet': line[:200]}],
                               le, 'listed_location/v1', {'program_key': rec['program_key']}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}']))
    return out


YEAR_STATEMENT = re.compile(r'[^.\n]*\bthis catalog applies to the (20\d{2})\s*[-–]\s*(20\d{2}) academic year[^.\n]*', re.I)


def coursedog_year(run, es):
    """(year, sentence) from the Coursedog catalog home page: "Information in this catalog applies to the 2026–2027
    academic year ..." (Willamette). None when the home page prints no such statement."""
    for e in es:
        if e.get('role') == 'catalog_home' and e.get('page_file'):
            m = YEAR_STATEMENT.search(run.load_page(e['page_file'])[0].text)
            if m and int(m.group(2)) == int(m.group(1)) + 1:
                return {'year': f'{m.group(1)}-{m.group(2)}', 'line': m.group(0).strip(), 'url': common.source_of(e)['url'], 'sha256': e.get('sha256')}
    return None


def coursedog_page_identity(inst, entry, page, today_year, cat_year):
    """Rendered Coursedog program page (Willamette): the program title printed after the 'Programs/' breadcrumb
    ('Biology (BA)') with its bachelor award, and a printed 'Bachelor of ...' degree line on the same page. The catalog
    year is the catalog home page's own statement of the year it applies to (cat_year), quoted as evidence."""
    lines = [l.strip() for l in page.lines if l.strip()]
    i = next((i for i, l in enumerate(lines) if l == 'Programs/'), None)
    if i is None or i + 1 >= len(lines) or not cat_year: return []
    name = lines[i + 1]
    degree = next((l for l in lines[i + 1:i + 40] if re.match(r'^Bachelor of ', l)), None)
    if credential_of(name) != 'bachelor' or not degree or OPTION_NAME.search(name): return []
    year = cat_year['year']; acad = f'{year[:4]}-{year[7:9]}'
    rec = {'program_key': CAT.slug(name), 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year,
           'program_url': common.source_of(entry)['url'], 'notes': f'Program title and degree ("{degree}") as printed on the catalog program page.'}
    return [common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                        [{'field': 'program_name', 'value': name, 'snippet': name}, {'field': 'credential_level', 'value': 'bachelor', 'snippet': degree},
                         {'field': 'catalog_year', 'value': year, 'snippet': cat_year['line'][:300], 'source_url': cat_year['url'], 'sha256': cat_year['sha256'],
                          'note': "the catalog home page's statement of the academic year the catalog applies to"}],
                        entry, 'coursedog_page/v1', {'program_key': rec['program_key']}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}'])]


PROGRAM_ONLY_ISSUES = ('requirement_groups_skipped',)


OPTION_NAME = re.compile(r'\b(option|concentration|track|emphasis)\b(?!.*\bmajor\b)', re.I)


def is_option_page(c):
    """'Studio Art BFA Option' (OSU) is an option inside a major, not a degree program; the major has its own record."""
    return c['domain'] == 'academic_programs' and bool(OPTION_NAME.search(c['record'].get('program_name', '')))


def program_identity(c):
    """A program record states name, award, URL, year and printed total only; a skipped requirement group elsewhere on
    the page does not weaken those facts, so that issue stays on the requirement rows and leaves the program record."""
    if c['domain'] == 'academic_programs':
        moved = [i for i in c['issues'] if i in PROGRAM_ONLY_ISSUES]
        if moved:
            c['issues'] = [i for i in c['issues'] if i not in PROGRAM_ONLY_ISSUES]
            c.setdefault('checks', {})['requirement_issues'] = moved
    return c


THEC_PAGE = 'https://thec.ppr.tn.gov/AcademicProgramInventorySearch'
AWARD_LEVEL = [('bachelor', re.compile(r'^B[A-Z.]{0,6}$|^BACHELOR', re.I)), ('associate', re.compile(r'^A[A-Z.]{0,4}$|^ASSOCIATE', re.I))]


def catalog_pdf_year(run, entries):
    """(year label, verbatim line, pdf entry) from the catalog's own generated PDF title page ("2026-2027 Catalog")."""
    for e in entries:
        if e.get('role') == 'catalog_pdf' and e.get('page_file'):
            page, _ = run.load_page(e['page_file'])
            for line in page.lines[:12]:
                m = YEAR_LABEL.search(line)
                if m and int(m.group(2)) == int(m.group(1)) + 1: return f'{m.group(1)}-{m.group(2)}', line.strip(), e
    return None, None, None


CODED_PROGRAM = re.compile(r'^([A-Z][A-Z0-9]*_[A-Z0-9_]+|[A-Z][A-Z0-9]*(?:\.[A-Z0-9]+)+|[A-Z]{2,8}) - (.+)$')  # BBA_ACCT (APSU), BIOL.BS (Carson-Newman)
AWARD_SUFFIX = re.compile(r',\s*([A-Z]{2,6}(/[A-Z]{2,4})?|CERT|Certificate|Minor|MINOR|Option)\s*$')


def catalog_pdf_programs(inst, entry, page, today_year):
    """A catalog system's generated full-catalog PDF (Coursedog): each department section prints a 'Programs' block
    listing its programs as 'Mechanical Engineering, BS' before 'Courses'. Bachelor-awarding names (award printed after
    the comma) become program records for the year printed on the PDF title page. A name wrapped onto two lines is
    rejoined only when the first line does not itself end in an award."""
    lines = page.lines
    year = None
    for line in lines[:12]:
        m = YEAR_LABEL.search(line)
        if m and int(m.group(2)) == int(m.group(1)) + 1: year = f'{m.group(1)}-{m.group(2)}'; year_line = line.strip(); break
    if not year: return []
    acad = f'{year[:4]}-{year[7:9]}'
    names, i = [], 0
    while i < len(lines):
        if lines[i].strip() == 'Programs':
            j, buf = i + 1, ''
            while j < len(lines) and lines[j].strip() not in ('Courses', 'All Programs') and j - i < 80:
                l = lines[j].strip()
                if re.search(r'\s{3,}|/\s*\d+$', l): break  # two-column layout or a page footer: not a simple list
                coded = CODED_PROGRAM.match(l)
                if coded:  # 'BBA_ACCT - Accounting (B.B.A.)' (Austin Peay): one program per line
                    names.append((coded.group(2).strip(), coded.group(1))); buf = ''; j += 1; continue
                buf = f'{buf} {l}'.strip() if buf and not AWARD_SUFFIX.search(buf) else l
                if AWARD_SUFFIX.search(buf): names.append((buf, None)); buf = ''
                j += 1
            i = j
        i += 1
    out, seen = [], set()
    for n, code in names:
        if code is not None:
            paren = re.search(r'\((B\.[A-Z.]{1,10}|B[A-Z]{1,4})\)\s*$', n)  # '(B.B.A.)', '(BS)'
            if not (paren or re.match(r'^B[A-Z]{1,5}_', code) or re.search(r'\.B[A-Z]{1,4}$', code)): continue  # award in parentheses, code prefix or code suffix
            if OPTION_NAME.search(n) or re.search(r'\bEmph\b|\bcert(ificate)?\b', n, re.I): continue  # emphases inside a major ('Emph.'), certificates
        else:
            m = AWARD_SUFFIX.search(n)
            if not m or not re.fullmatch(r'B[A-Z]{1,5}', m.group(1)): continue  # bachelor awards only; combined BS/MS left out
        key = CAT.slug(n)
        if key in seen: continue
        seen.add(key)
        rec = {'program_key': key, 'program_name': n, 'credential_level': 'bachelor', 'catalog_year': year,
               'program_url': common.source_of(entry)['url'], 'notes': "Listed in a department 'Programs' block of the catalog's generated full PDF."}
        out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                               [{'field': 'program_name', 'value': n, 'snippet': n}, {'field': 'catalog_year', 'value': year, 'snippet': year_line}],
                               entry, 'catalog_pdf_programs/v1', {'program_key': key}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}']))
    return out


def coursedog_cip(v):
    """'520301' or '52.0201 - Management' -> '52.0301' / '52.0201' (digits as printed, punctuation normalised)."""
    m = re.match(r'^\s*(\d{2})\.?(\d{4})\b', str(v or ''))
    return f'{m.group(1)}.{m.group(2)}' if m else None


def coursedog_candidates(target, inst, entry, page, yr, today_year):
    """Coursedog catalog backend program rows -> academic_programs candidates (undergraduate, active, bachelor awards).
    The catalog year comes from the same catalog's generated PDF title page; without it the year is unlabeled."""
    try:
        rows = json.loads(page.text).get('data') or []
    except (ValueError, AttributeError):
        return []
    year, line, pdf = yr
    home = (target.get('catalog') or {}).get('home', '').rstrip('/')
    out = []
    for r in rows:
        name = (r.get('catalogDisplayName') or '').strip() or (r.get('name') or '').strip()
        deg = (r.get('degreeDesignation') or '').strip()
        if (r.get('level') or '') not in ('UG', '') or (r.get('status') or 'Active') != 'Active': continue
        level = credential_of(f'{name} {deg}') if deg else credential_of(name)
        if level != 'bachelor' or not r.get('programGroupId'): continue
        acad = f'{year[:4]}-{year[7:9]}' if year else today_year
        rec = {'program_key': CAT.slug(name), 'program_name': name, 'credential_level': level,
               'program_url': f"{home}/programs/{r['programGroupId']}", 'notes': 'From the catalog backend program list (Coursedog) that the official catalog page loads.'}
        if year: rec['catalog_year'] = year
        cip = coursedog_cip(r.get('cipCode'))
        if cip: rec.update(cip_code=cip, cip_source_url=rec['program_url'])
        ev = [{'field': k, 'value': r.get(k), 'snippet': json.dumps({k: r.get(k)}, ensure_ascii=False)[:200]}
              for k in ('catalogDisplayName', 'name', 'degreeDesignation', 'level', 'cipCode', 'status', 'effectiveStartDate', 'programGroupId') if k in r]
        if year: ev.append({'field': 'catalog_year', 'value': year, 'snippet': line, 'source': (pdf or {}).get('url'), 'sha256': (pdf or {}).get('sha256')})
        c = common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source' if year else 'source_unlabeled', rec, ev, entry,
                        'coursedog_api/v1', {'program_key': rec['program_key'], 'group': r.get('programGroupId')})
        c['record']['source_url'] = rec['program_url']  # the public program page; the backend response hash is in the candidate source
        out.append(c)
    return out


def thec_rows(page):
    try:
        data = json.loads(page.text)
    except ValueError:
        return []
    rows = (data.get('ProgramList') or data.get('programList') or []) if isinstance(data, dict) else (data if isinstance(data, list) else [])
    # one spelling for every key, as the page's own table reads them (MajorName, Award, MajorCipCode, ...)
    canon = {k.lower(): k for k in ('InstitutionName', 'MajorName', 'Award', 'MajorTaxCode', 'MajorCipCode', 'CreditOrClockHours',
                                     'CurrentProgramStatus', 'ProgramId', 'EffectiveStartDate', 'FederalTaxName')}
    return [{canon.get(str(k).lower(), k): v for k, v in r.items()} for r in rows if isinstance(r, dict)]


def federal_cip(r):
    """THEC prints MajorCipCode as GG.FF.SSSS.XX, where FF.SSSS is the 6-digit federal CIP and FF is also printed as the
    row's MajorTaxCode (Mechanical Engineering BSME '09.14.1901.00' with MajorTaxCode '14' -> 14.1901; checked on all
    1,594 TN public rows of run 2026-10-05-thec2). The federal code is taken only when FF equals the printed MajorTaxCode,
    so the layout is confirmed row by row."""
    m = re.fullmatch(r'(\d{2})\.(\d{2})\.(\d{4})\.(\d{2})', (r.get('MajorCipCode') or '').strip())
    if not m or m.group(2) != str(r.get('MajorTaxCode') or '').strip(): return None
    return f'{m.group(2)}.{m.group(3)}'


def thec_candidates(inst, entry, rows, today_year):
    """THEC Academic Program Inventory rows (state-approved active programs) -> academic_programs candidates with the
    federal CIP code exactly as the inventory prints it. The inventory is not labelled with an academic year: rows are
    the programs active when fetched, recorded for the year in force at review (`source_unlabeled`)."""
    out = []
    for r in rows:
        name, award = (r.get('MajorName') or '').strip(), (r.get('Award') or '').strip()
        level = next((lvl for lvl, rx in AWARD_LEVEL if rx.match(award.replace(' ', ''))), None)
        if not name or level is None: continue
        if (r.get('CurrentProgramStatus') or 'Active').strip().lower() not in ('active', ''): continue
        cip = federal_cip(r)
        rec = {'program_key': CAT.slug(f'{name} {award}'), 'program_name': f'{name}, {award}', 'credential_level': level,
               'program_url': THEC_PAGE, 'notes': 'From the THEC Academic Program Inventory (state-approved active programs).'}
        if cip: rec.update(cip_code=cip, cip_source_url=THEC_PAGE)
        if str(r.get('CreditOrClockHours') or '').strip().isdigit(): rec['total_credits'] = int(r['CreditOrClockHours'])
        ev = [{'field': k, 'value': r.get(k), 'snippet': json.dumps({k: r.get(k)}, ensure_ascii=False)[:200]}
              for k in ('InstitutionName', 'MajorName', 'Award', 'MajorTaxCode', 'MajorCipCode', 'CreditOrClockHours', 'CurrentProgramStatus', 'ProgramId') if k in r]
        c = common.make('academic_programs', inst['institution_key'], today_year, 'source_unlabeled', rec, ev, entry,
                        'thec_inventory/v1', {'program_key': rec['program_key'], 'thec_program_id': r.get('ProgramId')})
        c['record']['source_url'] = THEC_PAGE  # the public search page; the API request and response hash are in the candidate source
        out.append(c)
    return out


def extract_run(targets, run_dir, today=None):
    run = Run(Path(run_dir)); today = today or date.today()
    today_year = T.current_academic_year(today)
    entries = run.entries()
    by_inst = defaultdict(list)
    for e in entries: by_inst[e.get('institution_key')].append(e)
    tmap = {t['institution_key']: t for t in targets['institutions']}
    lists, cands, evidence, summary, inventory = {}, [], [], {}, {}
    for key, es in sorted(by_inst.items()):
        t = tmap.get(key, {'institution_key': key, 'catalog': {}})
        roles = defaultdict(lambda: {'fetched': 0, 'ok': 0, 'errors': defaultdict(int)})
        for e in es:
            r = roles[e.get('role') or '?']; r['fetched'] += 1
            if e.get('page_file'): r['ok'] += 1
            elif e.get('error'): r['errors'][e['error'][:40]] += 1
        lists[key] = collect_lists(t, run, es) if t.get('catalog') else {'programs': [], 'counts': {}}
        if (t.get('catalog') or {}).get('platform') == 'coursedog': t = {**t, '_catalog_year': coursedog_year(run, es)}
        n_c = 0; seen_ev = set()
        for e in es:
            if not e.get('page_file'): continue
            page, _ = run.load_page(e['page_file'])
            inst = {'institution_key': key}
            if e.get('role') == 'catalog_pdf':
                for c in catalog_pdf_programs(inst, e, page, today_year):
                    c['program_role'] = 'catalog_pdf'; cands.append(c); n_c += 1
                continue
            if e.get('role') == 'catalog_api' and 'coursedog.com' in e.get('url', ''):
                yr = catalog_pdf_year(run, es)
                for c in coursedog_candidates(t, inst, e, page, yr, today_year):
                    c['program_role'] = 'catalog_api'; cands.append(c); n_c += 1
                continue
            if e.get('role') == 'state_inventory':
                rows = thec_rows(page)
                inventory[key] = rows
                for c in thec_candidates(inst, e, rows, today_year):
                    c['program_role'] = 'state_inventory'; cands.append(c); n_c += 1
                continue
            if e.get('role') == 'program_page':
                found = program_page_candidates(t, inst, e, page, today_year)
                if any(is_option_page(c) for c in found): found = []  # the option's rows belong to its major
                for c in found:
                    c['program_role'] = 'program_page'; cands.append(program_identity(c)); n_c += 1
            if e.get('kind') == 'pdf' and e.get('role') in ('degree_map', 'policy', 'policy_link'):
                try:
                    for c in PM.extract(inst, e, page, today_year):
                        c['program_role'] = 'degree_map'; cands.append(c); n_c += 1
                except Exception as exc:  # an unusual PDF must not stop the run; it is counted
                    roles['degree_map']['errors'][f'programmap:{type(exc).__name__}'] += 1
            if e.get('role') in ('policy', 'policy_link', 'program_page', 'state_source', 'degree_map_index', 'discover') or key.startswith('state-'):
                for s in sentences(page):
                    for cat, rx in EVIDENCE:
                        if rx.search(s) and (cat, s) not in seen_ev:
                            seen_ev.add((cat, s))
                            evidence.append({'evidence_id': hashlib.sha1(f"{e.get('sha256')}|{s}".encode()).hexdigest()[:14],
                                             'institution_key': key, 'category': cat, 'sentence': s,
                                             'url': common.source_of(e)['url'], 'sha256': e.get('sha256'),
                                             'fetched_at': e.get('fetched_at'), 'page_title': e.get('title', ''),
                                             'role': e.get('role'), 'year_labels': sorted(T.year_labels(page.title + ' ' + page.text[:3000]))})
        for c in listed_location_candidates(t, {'institution_key': key}, run, es, lists[key], today_year):
            c['program_role'] = 'program_list'; cands.append(c); n_c += 1
        for c in printed_list_candidates(t, {'institution_key': key}, run, es, today_year):
            c['program_role'] = 'program_list'; cands.append(c); n_c += 1
        for c in major_table_candidates(t, {'institution_key': key}, run, es, today_year):
            c['program_role'] = 'program_list'; cands.append(c); n_c += 1
        summary[key] = {'roles': {k: {**v, 'errors': dict(v['errors'])} for k, v in roles.items()},
                        'program_list_links': lists[key]['counts'], 'candidates': n_c,
                        'evidence': sum(1 for x in evidence if x['institution_key'] == key)}
    d = Path(run_dir)
    (d / 'program_lists.json').write_text(json.dumps(lists, indent=1, ensure_ascii=False) + '\n')
    with (d / 'candidates.jsonl').open('w') as f:
        for c in cands: f.write(json.dumps(c, sort_keys=True, ensure_ascii=False) + '\n')
    with (d / 'evidence.jsonl').open('w') as f:
        for x in evidence: f.write(json.dumps(x, sort_keys=True, ensure_ascii=False) + '\n')
    if inventory: (d / 'state_inventory.json').write_text(json.dumps(inventory, indent=1, ensure_ascii=False) + '\n')
    (d / 'summary.json').write_text(json.dumps(summary, indent=1, sort_keys=True) + '\n')
    (d / 'review.md').write_text(review_md(targets, summary, lists))
    return summary


def review_md(targets, summary, lists):
    names = {t['institution_key']: t['name'] for t in targets['institutions']}
    lines = [f"# Program-depth run: {targets['state']}", '',
             '| School | fetched | program links (bachelor) | program pages ok | candidates | evidence | top errors |', '|---|---|---|---|---|---|---|']
    for key, s in sorted(summary.items(), key=lambda kv: names.get(kv[0], kv[0])):
        fetched = sum(v['fetched'] for v in s['roles'].values())
        errs = defaultdict(int)
        for v in s['roles'].values():
            for k, n in v['errors'].items(): errs[k] += n
        top = ', '.join(f'{k}×{n}' for k, n in sorted(errs.items(), key=lambda x: -x[1])[:3])
        c = s['program_list_links']
        lines.append(f"| {names.get(key, key)} | {fetched} | {c.get('links', 0)} ({c.get('bachelor', 0)}) | "
                     f"{s['roles'].get('program_page', {}).get('ok', 0)} | {s['candidates']} | {s['evidence']} | {top} |")
    return '\n'.join(lines) + '\n'
