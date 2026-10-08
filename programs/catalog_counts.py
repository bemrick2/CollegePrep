"""Catalog completeness entries from a reviewed decision (the rule used in review since #175).

    python3 -m programs.catalog_counts --run programs/runs/<ST>/<RUN> --decision programs/decisions/<ST>-<RUN>.json
                                       --out entries.json [--year 2026-2027] [--reviewed 2026-10-08] ik [ik ...]

Every bachelor's entry on the official program list is accounted for: counted, or excluded by name as a combined
bachelor's/master's entry, a department / roadmap / general / commissioning link, a concentration or option of a degree
whose own line the list also prints (VCU 'Chemistry, Bachelor of Science (B.S.) with a concentration in biochemistry' beside
'Chemistry, Bachelor of Science (B.S.)': one program, as programs.extract.listed_emphasis_pages reads it), or an entry
printing no award.
A listed program is verified only when an approved record of the reviewed decision prints the same name, or sits on
that program's own page (http and https are one page) when no other listed name shares that page and the listed
name is not the record's name plus a qualifier ('X: Concentration in Y' is never credited through X's page).
Counts come from the reviewed decision's approvals, never from the autoreview file."""
import argparse, json, re
from collections import defaultdict
from pathlib import Path

from programs import extract as X

ZWSP = '​'
COMB = re.compile(r"Accelerated.*(\bM\.?[AS]\b\.?|\bMBA\b|\bMPA\b|Master)|Scholars Roadmap|\s\+\s.*\b(M[A-Z]{1,3}|MPA|MBA)\b|\(3\+2\)|\b3-2\b|4\+1|"
                  r"Dual Acceptance|and MBA\b|to MBA|\bB\.?[AS]\.?/\s?M\.?[AS]\b|\bM\.[AS]\.|/\s?(DDS|MD|PharmD|DPT|OTD)\b|\(B[AS]/D", re.I)
GENERIC = re.compile(r"^(Bachelor's (Degree|Concentration|Degree Programs)|Department of .*)$|: Bachelor's Degree\b|Minor, Certificate|Graduate Certificate|\bRoadmap\b", re.I)
ROTC = re.compile(r'\bROTC\b')
LABELED = {'labeled_in_title', 'labeled_in_heading', 'labeled_in_source'}
# UTEP 2026-27 cards run the name into the card's category labels: 'BBA in AccountingBusiness, Management, & Marketing
# BachelorsUndergraduateBusiness Administration' (the labels name the level 'Bachelors' and 'Undergraduate')
CATEGORY_RUN = re.compile(r'(?:[A-Z].*)?Bachelors(?:Online|Fast Track|Professional|Undergraduate|[A-Z]|$)')
AWARD_ONLY = re.compile(r'^(?:(?-i:B[A-Z]{0,4}[a-z]{0,3})|B\.\s?[A-Z][A-Za-z]{0,4}\.?(?:\s?[A-Z][a-z]{0,3}\.?)*|Bachelor of [A-Z][a-z]+(?: [A-Z][a-z]+)*)\**$')  # Missouri lists 'BA', 'BS*', 'BSAcc' under each department; never an all-caps name ('BIOLOGY')


def page_key(u):
    """One key per page: scheme, '/index.html', trailing slashes and repeated slashes do not make another page."""
    u = re.sub(r'(?<!:)//+', '/', (u or '').split('#')[0])
    return re.sub(r'^https?://', '', re.sub(r'(/index\.html?)?/*$', '', u)).lower()


def name_key(n):
    return re.sub(r'\W+', '', re.sub(r'Toggle.*', '', n or '')).lower()


def card_name(printed):
    """A list card that prints the name twice ('Anthropology, BAAnthropology, BA'; UW-Madison), or a shortened title
    then the name ('Nutritional Sciences, BS Nutritio...Nutritional Sciences, BS Nutrition and Dietetics'): the name."""
    pr = (printed or '').replace(ZWSP, '').strip()
    h = len(pr) // 2
    if len(pr) % 2 == 0 and h and pr[:h] == pr[h:]: return pr[:h], True
    if '...' in pr:
        head, tail = pr.split('...', 1)
        if head and tail.startswith(head): return tail, True
    return pr, False


def entries(run_dir, decision, iks, year='2026-2027', reviewed=''):
    run_dir = Path(run_dir)
    cands = {}
    for line in open(run_dir / 'candidates.jsonl'):
        v = json.loads(line); cands.setdefault(v['candidate_id'], v)
    approved = {a['candidate_id'] for a in json.load(open(decision))['approve']}
    lists = json.load(open(run_dir / 'program_lists.json'))
    manifest = {}
    for line in open(run_dir / 'manifest.jsonl'):
        m = json.loads(line); manifest.setdefault(m['url'], m)
    out = []
    for ik in iks:
        # only a record whose catalog year is printed in its source verifies a listed program (an unlabeled Coursedog API
        # record is promoted as partially verified and never counted)
        progs = [v for v in cands.values() if v['institution_key'] == ik and v['domain'] == 'academic_programs' and v['candidate_id'] in approved
                 and v.get('year_basis', 'labeled_in_source') in LABELED]
        names = {name_key(v['record']['program_name']): v for v in progs}
        listing = lists[ik]['programs']
        # an entry the list reader left unclassified but that prints an undotted bachelor's award ('Marketing, BSBA') is a bachelor's entry
        raw = [x for x in listing if x['listed_as'] == 'bachelor' or (x['listed_as'] is None and X.UNDOTTED_LIST_AWARD.search(x['printed'].replace(ZWSP, '')))]
        unlabeled = sorted({card_name(x['printed'])[0] for x in listing if x['listed_as'] in ('major', 'major_unlabeled_degree')})
        seen, b, doubled = set(), [], 0
        for x in raw:
            k = (name_key(x['printed']), page_key(x['url']))
            if k in seen: continue
            seen.add(k)
            pr, dbl = card_name(x['printed']); doubled += dbl
            b.append(dict(x, printed=pr))
        glued = labelled = 0
        for x in b:  # Coursedog lists run the description on to the name: 'Accounting - BSThe B.S. in Accounting ...'
            if name_key(x['printed']) in names: continue
            g = [v['record']['program_name'] for v in progs if x['printed'].startswith(v['record']['program_name'])
                 and re.match(r'[A-Z][a-z]+\s', x['printed'][len(v['record']['program_name']):])
                 and len(x['printed']) - len(v['record']['program_name']) >= 30]  # a sentence, not the 'E' of 'BSE'
            c = [v['record']['program_name'] for v in progs if x['printed'].startswith(v['record']['program_name'])
                 and CATEGORY_RUN.match(x['printed'][len(v['record']['program_name']):])]
            if c: x['printed'] = max(c, key=len); labelled += 1
            elif g: x['printed'] = max(g, key=len); glued += 1
        # an entry printing only an award ('BS' under a department heading, Missouri) is identified by its page, not its text
        ident = lambda x: 'page:' + page_key(x['url']) if AWARD_ONLY.match(x['printed'].strip()) else name_key(x['printed'])
        comb = [x for x in b if COMB.search(x['printed'])]
        gen = [x for x in b if x not in comb and (GENERIC.search(x['printed']) or ROTC.search(x['printed']))]
        rest = [x for x in b if x not in comb and x not in gen]
        shape = [X.emphasis_entry(X.list_line(x['printed'])) for x in rest]
        degrees = {X._degree_key(X.list_line(x['printed'])) for x, m in zip(rest, shape) if not m} - {None}
        opts = [x for x, m in zip(rest, shape) if m and (X.name_key_of(m.group('base')), X._award_key(m.group('award'))) in degrees]
        deg = [x for x in rest if x not in opts]
        by_page = defaultdict(set)
        for x in deg: by_page[page_key(x['url'])].add(ident(x))
        rec_pages = defaultdict(list)
        for v in progs: rec_pages[page_key(v['source']['requested_url'])].append(v)
        verified = {}
        for x in deg:
            k = ident(x); hit = None if k.startswith('page:') else names.get(k)
            if not hit and len(by_page[page_key(x['url'])]) == 1 and len(rec_pages.get(page_key(x['url']), [])) == 1:
                hit = rec_pages[page_key(x['url'])][0]
                rk = name_key(hit['record']['program_name']); pk = name_key(x['printed'])
                if pk != rk and pk.startswith(rk): hit = None  # 'X: Concentration in Y' is not credited through X's page
            if hit: verified[k] = hit['record']['program_key']
            else: verified.setdefault(k, None)
        n = len(verified); ver = sum(1 for v in verified.values() if v)
        missing = {ident(x): x['printed'] + (f" ({x['url']})" if ident(x).startswith('page:') else '') for x in deg if not verified[ident(x)]}
        miss = sorted(set(missing.values()))
        pages = sorted({x['listed_on'] for x in raw}); lo = pages[0]
        parts = [f"{len(raw)} linked entries on the official {year} program list" + (f" ({len(pages)} pages)" if len(pages) > 1 else '') + " print a bachelor's award"]
        if len(b) < len(raw): parts.append(f"{len(raw) - len(b)} repeat an entry already counted")
        if doubled: parts.append(f"{doubled} print the program name twice (a card title, sometimes shortened, then the name) and are read once")
        award_only = sum(1 for x in deg if ident(x).startswith('page:'))
        if award_only: parts.append(f"{award_only} print only an award under a department heading and are identified by their own page")
        if labelled: parts.append(f"{labelled} run the card's category labels on to the name and are matched by the name printed before them")
        if glued: parts.append(f"{glued} run the program description on to the name and are matched by the name printed before it")
        if comb: parts.append(f"not counted, {len(comb)} combined or accelerated bachelor's/master's entries: " + ' | '.join(sorted({x['printed'] for x in comb})))
        if gen: parts.append(f"not counted, {len(gen)} department, roadmap, general or commissioning links that are not a single bachelor's program: " + ' | '.join(sorted({x['printed'] for x in gen})))
        if opts: parts.append(f"not counted, {len(opts)} concentrations or options of a degree whose own line is listed: " + ' | '.join(sorted({x['printed'] for x in opts})))
        if unlabeled: parts.append(f"{len(unlabeled)} further list entries print no award and are not counted: " + ' | '.join(unlabeled))
        if len(deg) - n: parts.append(f"{len(deg) - n} remaining entries repeat a program name listed under another link and are counted once")
        basis = '; '.join(parts) + f". {n} bachelor's programs, {ver} with a verified record printing that name or on that program's own page." \
            + (f" Not recorded (names separated by ' | '): {' | '.join(miss)}." if miss else '')
        e = {'institution_key': ik, 'catalog_url': 'https://' + lo.split('/')[2] + '/', 'catalog_year_label': year,
             'source_evidence': {'url': lo, 'sha256': manifest[lo]['sha256'], 'fetched_at': manifest[lo]['fetched_at']},
             'listed_bachelor_programs': n, 'verified_listed_programs': ver, 'programs_complete': ver == n,
             'completeness_basis': basis, 'reason': f'Reviewed: official current-catalog program list (Research session{", " + reviewed if reviewed else ""}).'}
        if ver == n: e['listed_program_keys'] = sorted(set(verified.values()))
        if n - ver != len(missing) or len(miss) != len(missing): raise ValueError(f'{ik}: {n - ver} unverified but {len(miss)} names')
        out.append(e)
    return out


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument('--run', required=True); a.add_argument('--decision', required=True); a.add_argument('--out', required=True)
    a.add_argument('--year', default='2026-2027'); a.add_argument('--reviewed', default=''); a.add_argument('iks', nargs='+')
    args = a.parse_args(argv)
    es = entries(args.run, args.decision, args.iks, args.year, args.reviewed)
    json.dump(es, open(args.out, 'w'), indent=1)
    for e in es: print(e['institution_key'], e['verified_listed_programs'], '/', e['listed_bachelor_programs'], 'complete' if e['programs_complete'] else '')


if __name__ == '__main__':
    main()
