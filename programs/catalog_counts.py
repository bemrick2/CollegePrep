"""Catalog completeness entries from a reviewed decision (the rule used in review since #175).

    python3 -m programs.catalog_counts --run programs/runs/<ST>/<RUN> --decision programs/decisions/<ST>-<RUN>.json
                                       --out entries.json [--year 2026-2027] [--reviewed 2026-10-08] ik [ik ...]

Every bachelor's entry on the official program list is accounted for: counted, or excluded by name as a combined
bachelor's/master's entry, a department / roadmap / general / commissioning link, or an entry printing no award.
A listed program is verified only when an approved record of the reviewed decision prints the same name, or sits on
that program's own page (http and https are one page) when no other listed name shares that page and the listed
name is not the record's name plus a qualifier ('X: Concentration in Y' is never credited through X's page).
Counts come from the reviewed decision's approvals, never from the autoreview file."""
import argparse, json, re
from collections import defaultdict
from pathlib import Path

ZWSP = '​'
COMB = re.compile(r"Accelerated.*(\bM\.?[AS]\b\.?|\bMBA\b|\bMPA\b|Master)|Scholars Roadmap|\s\+\s.*\b(M[A-Z]{1,3}|MPA|MBA)\b|\(3\+2\)|\b3-2\b|4\+1|"
                  r"Dual Acceptance|and MBA\b|to MBA|\bB\.?[AS]\.?/\s?M\.?[AS]\b|\bM\.[AS]\.|/\s?(DDS|MD|PharmD|DPT|OTD)\b|\(B[AS]/D", re.I)
GENERIC = re.compile(r"^(Bachelor's (Degree|Concentration)|Department of .*)$|: Bachelor's Degree\b|Minor, Certificate|Graduate Certificate|\bRoadmap\b", re.I)
ROTC = re.compile(r'\bROTC\b')


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
        progs = [v for v in cands.values() if v['institution_key'] == ik and v['domain'] == 'academic_programs' and v['candidate_id'] in approved]
        names = {name_key(v['record']['program_name']): v for v in progs}
        listing = lists[ik]['programs']
        raw = [x for x in listing if x['listed_as'] == 'bachelor']
        unlabeled = sorted({card_name(x['printed'])[0] for x in listing if x['listed_as'] in ('major', 'major_unlabeled_degree')})
        seen, b, doubled = set(), [], 0
        for x in raw:
            k = (name_key(x['printed']), page_key(x['url']))
            if k in seen: continue
            seen.add(k)
            pr, dbl = card_name(x['printed']); doubled += dbl
            b.append(dict(x, printed=pr))
        glued = 0
        for x in b:  # Coursedog lists run the description on to the name: 'Accounting - BSThe B.S. in Accounting ...'
            if name_key(x['printed']) in names: continue
            g = [v['record']['program_name'] for v in progs if x['printed'].startswith(v['record']['program_name'])
                 and re.match(r'[A-Z][a-z]+\s', x['printed'][len(v['record']['program_name']):])
                 and len(x['printed']) - len(v['record']['program_name']) >= 30]  # a sentence, not the 'E' of 'BSE'
            if g: x['printed'] = max(g, key=len); glued += 1
        comb = [x for x in b if COMB.search(x['printed'])]
        gen = [x for x in b if x not in comb and (GENERIC.search(x['printed']) or ROTC.search(x['printed']))]
        deg = [x for x in b if x not in comb and x not in gen]
        by_page = defaultdict(set)
        for x in deg: by_page[page_key(x['url'])].add(name_key(x['printed']))
        rec_pages = defaultdict(list)
        for v in progs: rec_pages[page_key(v['source']['requested_url'])].append(v)
        verified = {}
        for x in deg:
            k = name_key(x['printed']); hit = names.get(k)
            if not hit and len(by_page[page_key(x['url'])]) == 1 and len(rec_pages.get(page_key(x['url']), [])) == 1:
                hit = rec_pages[page_key(x['url'])][0]
                if k.startswith(name_key(hit['record']['program_name'])): hit = None
            if hit: verified[k] = hit['record']['program_key']
            else: verified.setdefault(k, None)
        n = len(verified); ver = sum(1 for v in verified.values() if v)
        miss = sorted({x['printed'] for x in deg if not verified[name_key(x['printed'])]})
        pages = sorted({x['listed_on'] for x in raw}); lo = pages[0]
        parts = [f"{len(raw)} linked entries on the official {year} program list" + (f" ({len(pages)} pages)" if len(pages) > 1 else '') + " print a bachelor's award"]
        if len(b) < len(raw): parts.append(f"{len(raw) - len(b)} repeat an entry already counted")
        if doubled: parts.append(f"{doubled} print the program name twice (a card title, sometimes shortened, then the name) and are read once")
        if glued: parts.append(f"{glued} run the program description on to the name and are matched by the name printed before it")
        if comb: parts.append(f"not counted, {len(comb)} combined or accelerated bachelor's/master's entries: " + ' | '.join(sorted({x['printed'] for x in comb})))
        if gen: parts.append(f"not counted, {len(gen)} department, roadmap, general or commissioning links that are not a single bachelor's program: " + ' | '.join(sorted({x['printed'] for x in gen})))
        if unlabeled: parts.append(f"{len(unlabeled)} further list entries print no award and are not counted: " + ' | '.join(unlabeled))
        if len(deg) - n: parts.append(f"{len(deg) - n} remaining entries repeat a program name listed under another link and are counted once")
        basis = '; '.join(parts) + f". {n} bachelor's programs, {ver} with a verified record printing that name or on that program's own page." \
            + (f" Not recorded (names separated by ' | '): {' | '.join(miss)}." if miss else '')
        e = {'institution_key': ik, 'catalog_url': 'https://' + lo.split('/')[2] + '/', 'catalog_year_label': year,
             'source_evidence': {'url': lo, 'sha256': manifest[lo]['sha256'], 'fetched_at': manifest[lo]['fetched_at']},
             'listed_bachelor_programs': n, 'verified_listed_programs': ver, 'programs_complete': ver == n,
             'completeness_basis': basis, 'reason': f'Reviewed: official current-catalog program list (Research session{", " + reviewed if reviewed else ""}).'}
        if ver == n: e['listed_program_keys'] = sorted(set(verified.values()))
        if n - ver != len({name_key(m) for m in miss}): raise ValueError(f'{ik}: {n - ver} unverified but {len(miss)} names')
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
