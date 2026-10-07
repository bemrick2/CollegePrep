"""Standing review rules for production states (`python -m programs autoreview --state XX --run <run dir>`).

The TN/OR pilots were reviewed candidate by candidate. For production states, the same acceptance criteria are written
down here and applied mechanically; this module writes a decisions file (programs/decisions/<ST>-<run>-auto.json)
that `python -m programs promote` applies like any reviewed decision, and a held-candidate summary for the reviewer.
Nothing is promoted that a pilot review would have held:

  * only extractors whose output was independently reviewed in the pilots (TRUSTED below);
  * no open issues (a stale year label, an option page, a held layout rule and so on are issues);
  * every value verbatim in its stored source (programs.verify: no problems for the candidate);
  * a program, not an option/track/concentration/emphasis of one, nor a combined/accelerated path into a graduate degree;
  * when one program name is printed on several pages, only the base page's record and requirement rows (the page whose
    URL slug the others extend); with no base page, none;
  * a bachelor's credential and a catalog year label of the current academic year or later, printed in the source;
  * requirement rows only for a program approved in the same decision or already on file.

Catalog records: a list page set that prints one current catalog-year label yields a program_catalogs record whose
listed_bachelor_programs counts every distinct linked list entry printing a bachelor's award. Options and tracks are
counted too, which errs high; a printed list line without a link is not counted, which can err low (UO 2026-27: 73
linked entries against 78 printed lines), so each state's covered schools get a sampled hand check of the count. No record is written when the list
names majors without their award, or names fewer bachelor's programs than the run verified (the list is then not the
whole picture). programs_complete is never set here.

New platforms and extractors are not added to TRUSTED without an independent accuracy review of a sample (see the
SmartCatalog review recorded in programs/queue/OR.json).
"""
from __future__ import annotations
import json, re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from pipeline import text as T

ROOT = Path(__file__).resolve().parent.parent
TRUSTED_PROGRAMS = {'catalog_program/v1', 'coursedog_api/v1', 'coursedog_page/v1', 'smartcatalog_program/v1', 'award_heading/v1',
                    'department_major/v1', 'stated_major/v1', 'listed_location/v1', 'major_table/v1',
                    # independent review 2026-10-06 (Auburn, 30 sampled): 26/30 right; the 4 errors were duplicate list links
                    # (fixed: one list entry per page, the awarded line kept) and entry-path variants are now held
                    'listed_program/v1',
                    # independent review 2026-10-06 (MSState and Arkansas department pages, 36 sampled): 35/36 right; the error
                    # was a branch-campus copy of a main-campus program, held by the several-pages rule (no base page)
                    'department_section/v1',
                    # independent review 2026-10-06 (UNI award-headed pages, 25 sampled): 21/25 right; the 4 errors (three
                    # 'Major: Emphasis' names, one dual major) are now excluded by the reader. Drupal pilots reviewed by hand.
                    'static_program/v1',
                    # independent review 2026-10-06 (UF 'Degree: Bachelor of ...' pages, 25 sampled): 25/25 right
                    'degree_line/v1'}
# extractors whose programs share one page by design (several degree sections on a department page)
SHARED_PAGE = {'department_section/v1'}
OPTION = re.compile(r'\b(track|option|concentration|emphasis|specialization)\b', re.I)  # an option is not a program
# combined and accelerated pathways into a graduate degree are not bachelor's programs of their own
COMBINED = re.compile(r'\+|\b(accelerated|combined|dual|concurrent|double)\b|\bwith\s+(an?\s+)?((?-i:M\.?\s?[A-Z]{1,4})\b|Master)|\b(B\.?[AS]\.?|BBA|B\.B\.A\.)\s*/\s*(M|J\.?D)|program for', re.I)
# a graduate award inside a name ('Business Administration, M.B.A.') also contains 'B.A.' for the bachelor's pattern
GRADUATE = re.compile(r'\bM\.\s?B\.\s?A\b|\bMBA\b|\bM\.\s?(A|S|Ed|F\.?A)\.|\bMaster|\bPh\.?\s?D\b|\bDoctor', re.I)
TRUSTED_REQUIREMENTS = {('major', 'courselist_html/v1'), ('program_plan', 'courseleaf_plan/v1'), ('program_plan', 'acalog_plan/v1'),
                        ('program_plan', 'clearpath_plan/v1'), ('program_plan', 'program_map/v1')}


AWARD_SLUG = re.compile(r'[-_](b-?a|b-?s|bfa|bm|bba|bsn|bas|bsw|bae|bse|bme|bm?e|ba-bs|bachelor-of-[a-z-]+)$', re.I)  # UF 'AEC_BS'


def page_stem(url):
    """A program page's identity for comparing pages that print one program name: the last path segment without an
    award suffix ('asian-studies-ba' -> 'asian-studies'), so a cross-listed copy under another college path, and a
    Coursedog default pathway view ('/programs/BFA.AA/general-aoYks' -> '/programs/BFA.AA'), are the same page."""
    url = re.sub(r'/general-[A-Za-z0-9]+$', '', url)
    return AWARD_SLUG.sub('', url.rsplit('/', 1)[-1])


def base_stem(urls):
    """When one program name is printed on several pages, the stem of the base page (the one every other page's stem
    extends: 'biology-bs' / 'biology-bs-pre-professional'), or None when there is no such page."""
    stems = {page_stem(u) for u in urls}
    base = [b for b in stems if all(o == b or o.startswith((b + '-', b + '_')) for o in stems)]
    return base[0] if len(base) == 1 else None


DEGREE_SLUG = re.compile(r'[-_](bachelor-(arts|science|fine-arts|music)|bachelors?-degrees?|b-?a|b-?s|bfa|bm)$', re.I)


def degree_page(urls):
    """JHU 2026-27 prints a degree on its department page ('.../archaeology-ugrad-major/'), on an Engineering for
    Professionals page ('.../engineering-professionals/civil-engineering/') and on the degree's own page
    ('.../archaeology-bachelor-arts/', '.../civil-engineering-bachelor-science/'): when exactly one of the pages names an
    award in its last path segment, it is the program's page and the others are variants."""
    out = [u for u in urls if DEGREE_SLUG.search(u.rstrip('/').rsplit('/', 1)[-1])]
    return out[0] if len(out) == 1 else None


def variant_pages_of(groups):
    """Pages that print a program name another page of the same program also prints, and are not that program's page:
    the degree page when there is one (degree_page), else the base page (base_stem)."""
    out = set()
    for us in groups:
        if len(us) < 2: continue
        base = base_stem(us)
        canon = degree_page(us) if base is None else None  # only where no page is the others' base page
        out |= {u for u in us if u != canon} if canon else {u for u in us if page_stem(u) != base}
    return out


def load(run):
    run = Path(run)
    cands = [json.loads(l) for l in (run / 'candidates.jsonl').read_text().splitlines()]
    verify = json.loads((run / 'verify.json').read_text()) if (run / 'verify.json').exists() else None
    if verify is None: raise SystemExit(f'run programs.verify on {run} first')
    lists = json.loads((run / 'program_lists.json').read_text()) if (run / 'program_lists.json').exists() else {}
    return cands, verify, lists


def current_year(c, today_year):
    y = c.get('academic_year') or ''
    return bool(y) and y >= today_year


def review(state, run, today=None):
    today_year = T.current_academic_year(today or date.today())
    cands, verify, lists = load(run)
    approve, held = [], Counter()
    program_keys = defaultdict(set)
    seen, seen_url = set(), set()
    # entry-path variants of one degree ('Architecture (Foundation Unit) – BArch' / '(Summer Design)') are held together
    from .extract import AWARDS
    drop = lambda m: '' if not AWARDS.fullmatch(m.group(1).strip()) else m.group(0)  # keep '(BS)', drop '(Summer Design)'
    plain = lambda c: re.sub(r'\s+', ' ', re.sub(r'\s*\(([^()]*)\)', drop, c['record'].get('program_name', ''))).strip()
    base = lambda c: plain(c).lower()  # the variant-free name is approved; '(Jeffco 2+SLU)' style variants are held
    variants = defaultdict(set)
    for c in cands:
        if c['domain'] == 'academic_programs': variants[(c['institution_key'], base(c))].add(c['record'].get('program_name'))
    # one program name printed on several pages (NSU 'Biology-BS' / 'Biology-BS-Pre-Professional', Liberty's online tracks):
    # the record and its requirement rows come only from the base page (base_stem); no base page, no record
    norm = lambda u: re.sub(r'(/index\.html?)?/?$', '', (u or '').split('#')[0])
    url_of = lambda c, f: norm(c['record'].get(f) or (c.get('source') or {}).get('url'))
    pages = defaultdict(set)
    for c in cands:
        u = url_of(c, 'program_url')
        if c['domain'] == 'academic_programs' and u and not u.lower().endswith('.pdf'): pages[(c['institution_key'], c['record'].get('program_key'))].add(u)
    variant_pages = variant_pages_of(pages.values())
    from .extract import listed_emphasis_pages, _degree_key
    offered = defaultdict(set)  # degrees with a program candidate of their own (not an option page)
    for c in cands:
        n = c['record'].get('program_name', '') if c['domain'] == 'academic_programs' else ''
        if n and not OPTION.search(n) and _degree_key(n): offered[c['institution_key']].add(_degree_key(n))
    listed_emphases = listed_emphasis_pages(lists, norm, offered)
    for c in cands:
        if c['domain'] != 'academic_programs': continue
        k = (c['institution_key'], c['record'].get('program_key'))
        u = (c['institution_key'], re.sub(r'(/index\.html?)?/?$', '', c['record'].get('program_url') or c['candidate_id']))
        why = ('untrusted_extractor' if c['extractor'] not in TRUSTED_PROGRAMS else 'issues' if c['issues'] else
               'not_verbatim' if verify.get(c['candidate_id']) else 'not_bachelor' if c['record'].get('credential_level') != 'bachelor' else
               'graduate_name' if GRADUATE.search(c['record'].get('program_name', '')) else
               'option_name' if OPTION.search(c['record'].get('program_name', '')) and (c['institution_key'], url_of(c, 'program_url')) not in listed_emphases else
               'combined_program' if COMBINED.search(c['record'].get('program_name', '')) else
               'entry_path_variant' if len(variants[(c['institution_key'], base(c))]) > 1 and plain(c) != c['record'].get('program_name', '').strip()
               and (c['institution_key'], url_of(c, 'program_url')) not in listed_emphases else
               'variant_page' if url_of(c, 'program_url') in variant_pages else
               'not_current_year' if not current_year(c, today_year) else
               'duplicate' if k in seen or (u in seen_url and c['extractor'] not in SHARED_PAGE) else None)
        if why: held[why] += 1; continue
        seen.add(k); seen_url.add(u); program_keys[c['institution_key']].add(k[1])
        approve.append({'candidate_id': c['candidate_id'], 'reason': f"Standing review ({c['extractor']}): name, award and {c['record'].get('catalog_year')} catalog year verbatim in the stored official page."})
    for c in cands:
        if c['domain'] != 'degree_requirements': continue
        kind = c['record'].get('requirement_kind')
        why = ('untrusted_extractor' if (kind, c['extractor']) not in TRUSTED_REQUIREMENTS else 'issues' if c['issues'] else
               'not_verbatim' if verify.get(c['candidate_id']) else 'not_current_year' if not current_year(c, today_year) else
               'variant_page' if url_of(c, 'source_url') in variant_pages else
               'program_not_approved' if c['record'].get('program_key') not in program_keys[c['institution_key']] else None)
        if why: held['req_' + why] += 1; continue
        approve.append({'candidate_id': c['candidate_id'], 'reason': f"Standing review ({c['extractor']}): rows verbatim in the stored official page; passed the layout hold rules."})
    approved_urls = defaultdict(set)
    for a in approve:
        c = next(x for x in cands if x['candidate_id'] == a['candidate_id'])
        if c['domain'] == 'academic_programs': approved_urls[c['institution_key']].add(re.sub(r'(/index\.html?)?/?$', '', c['record'].get('program_url') or ''))
    catalogs = [c for c in catalog_records(state, run, lists, today_year, approved_urls)
                # a list that names fewer bachelor's programs than are verified, or lists majors without their award, cannot bound the count
                if c['listed_bachelor_programs'] >= max(5, len(program_keys[c['institution_key']])) and not lists[c['institution_key']]['counts'].get('major_unlabeled_degree')]
    return approve, catalogs, held


def catalog_records(state, run, lists, today_year, approved_urls=None):
    out = []
    manifest = {}
    for line in (Path(run) / 'manifest.jsonl').read_text().splitlines():
        m = json.loads(line)
        if m.get('page_file'): manifest.setdefault(m['url'], m)
    targets = {t['institution_key']: t for t in json.loads((ROOT / 'programs/targets' / f'{state}.json').read_text())['institutions']}
    for key, pl in lists.items():
        years = {int(y[:4]) for y in pl.get('printed_years', []) if y[:4].isdigit()}
        progs = [p for p in pl.get('programs', []) if p.get('credential_level') == 'bachelor']
        if len(years) != 1 or not progs or key not in targets: continue
        y = years.pop()
        if f'{y}-{str(y + 1)[2:]}' < today_year: continue
        src = Counter(p['listed_on'] for p in progs).most_common(1)[0][0]
        m = manifest.get(src)
        if not m: continue
        n = len({p['printed'].strip().lower() for p in progs})
        on_list = {re.sub(r'(/index\.html?)?/?$', '', p['url']) for p in progs} & (approved_urls or {}).get(key, set())
        out.append({'institution_key': key, 'catalog_url': targets[key]['catalog']['home'], 'catalog_year_label': f'{y}-{y + 1}',
                    'source_evidence': {'url': src, 'sha256': m['sha256'], 'fetched_at': m['fetched_at']},
                    'listed_bachelor_programs': n, 'verified_listed_programs': len(on_list), 'programs_complete': False,
                    'completeness_basis': (f'{n} distinct linked entries on the official {y}-{y + 1} program list pages print a bachelor\'s '
                                           'award (options, tracks and concentrations listed with an award are counted; unlinked lines are not). '
                                           'Not checked as complete.'),
                    'reason': 'Standing review: official current-catalog program list pages.'})
    return out


def main(state, run, today=None):
    approve, catalogs, held = review(state, run, today)
    rid = Path(run).name
    d = {'run': str(Path(run).relative_to(ROOT)) if Path(run).is_absolute() else str(run), 'run_branch': f'program-run/{state.lower()}-*',
         'reviewer': f'programs/autoreview.py standing rules, {date.today().isoformat()}', 'notes': f'Held: {dict(held)}',
         'approve': approve, 'catalogs': catalogs}
    p = ROOT / 'programs/decisions' / f'{state}-{rid}-auto.json'
    p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
    print(f'{state} {rid}: approve {len(approve)}, catalogs {len(catalogs)}, held {dict(held)} -> {p.relative_to(ROOT)}')
    return 0
