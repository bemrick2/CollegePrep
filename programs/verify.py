"""Mechanical verbatim check of program-depth candidates against their stored source documents.

For each candidate: the program name, printed catalog year and every course code (and title) must occur in the
document text; a printed total must occur next to a total label; every evidence sentence must occur verbatim.
Used before promotion and by the independent review. python -m programs.verify RUN_DIR [INSTITUTION_KEY ...]
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

from pipeline.crawl import Run


def norm(s):
    return re.sub(r'\s+', ' ', (s or '').replace('​', '')).strip().lower()


def squash(s):
    """Letters and digits only: PDF plan columns wrap titles across lines and hyphenate them."""
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())


def code_in(text, code):
    m = re.match(r'^([A-Z]{1,5}(?:/[A-Z]{1,5})*)\s?(\d.*)$', code.strip())  # 'IT222' (no space), 'ENG/FILM 366' (cross-listed)
    if not m: return re.search(rf'\b{re.escape(code)}\b', text, re.I) is not None
    subj, num = m.groups()
    return re.search(rf'\b{re.escape(subj)}\s?{re.escape(num)}\b', text, re.I) is not None


def segmented(s, squashed, min_piece=6):
    """True when s (letters and digits only) splits into consecutive pieces of at least min_piece characters (or the
    whole remainder) that each occur in the squashed document text: a title wrapped across lines of a two-column page
    is printed in pieces between the other column's text."""
    i = 0
    while i < len(s):
        j = len(s)
        while j > i and s[i:j] not in squashed: j -= 1
        if j == i or (j - i < min_piece and j < len(s)): return False
        i = j
    return True


def check_candidate(c, text, other=None):
    probs = []
    r = c['record']; t = norm(text); squashed = squash(text)
    if c.get('extractor') in ('thec_inventory/v1', 'coursedog_api/v1'):  # structured rows: every quoted field value is in the response
        for ev in c.get('evidence', []):
            if ev.get('sha256') and ev['sha256'] != c['source'].get('sha256') and other:  # evidence from another stored document (catalog year)
                if norm(ev.get('snippet', '')) not in norm(other(ev['sha256'])) and not all(norm(x) in norm(other(ev['sha256'])) for x in ev.get('snippet', '').split(' ', 1)):
                    probs.append(f"{ev['field']} snippet not in its source document")
                continue
            if ev.get('value') not in (None, '') and json.dumps(ev['value'], ensure_ascii=False) not in text and str(ev['value']) not in text:
                probs.append(f"{ev['field']} value not in source response")
        return probs
    if c['domain'] == 'academic_programs':
        nev = next((ev for ev in c.get('evidence', []) if ev.get('field') == 'program_name' and ev.get('sha256') and ev['sha256'] != c['source'].get('sha256')), None)
        if nev:  # named on the catalog's program list (department_major/v1): printed there; the page must print the tying heading
            if not other or norm(r['program_name']) not in norm(other(nev['sha256'])): probs.append('program_name not verbatim on its list page')
            for ev in c.get('evidence', []):
                if ev.get('field') == 'program_page_heading' and norm(ev.get('value', '')) not in t: probs.append('program page heading not printed')
        elif norm(r['program_name']) not in t: probs.append('program_name not verbatim')
        for ev in c.get('evidence', []):
            # a degree level read from a state program inventory: the row is printed in that stored document
            if ev.get('field') == 'award' and norm(ev.get('snippet', '')) not in t: probs.append('award sentence not verbatim')
            if ev.get('field') == 'credential_level' and ev.get('sha256') and ev['sha256'] != c['source'].get('sha256') and c.get('extractor') == 'inventory_level/v1':
                if not other or norm(ev.get('snippet', '')) not in norm(other(ev['sha256'])): probs.append('credential level row not in its inventory document')
        cy = r.get('catalog_year') or ''
        y = re.match(r'(20\d{2})-(20\d{2})', cy)
        yev = next((ev for ev in c.get('evidence', []) if ev.get('field') == 'catalog_year' and ev.get('sha256') and ev['sha256'] != c['source'].get('sha256')), None)
        ytext = other(yev['sha256']) if (yev and other) else text  # the year printed on another stored page of the catalog (its home)
        if y and not re.search(rf'{y.group(1)}\s*[-–]\s*({y.group(2)}|{y.group(2)[2:]})', ytext): probs.append('catalog year not printed')
        n = int(r['total_credits']) if r.get('total_credits') is not None else None
        if n is not None and not re.search(rf'total[^0-9]{{0,40}}\b{n}\b|\b{n}\s+(total|hours\s+total)', text, re.I):
            probs.append('total_credits not printed next to a total label')
    elif c.get('extractor') == 'courseleaf_plangrid/v1':
        # roadmap grid items are checked against the grid's own cells (the layout document): each item, its options and
        # their '(*)' and footnote markers must be one printed cell exactly
        cells = set()
        lay = (c.get('layout_source') or {}).get('sha256')
        doc = json.loads(other(lay)) if (lay and other and other(lay)) else {}
        for t in doc.get('grids') or []:
            for row in t.get('rows') or []:
                cells |= {re.sub(r'\s+', ' ', x.get('text') or '').strip() for x in row.get('cells') or []}
        if not cells: probs.append('roadmap grid document not in run')
        for term in r.get('rule_details', {}).get('terms', []) or []:
            for it in term.get('items', []):
                for i in [it, *it.get('options', [])]:
                    printed = (i.get('code') or i.get('text') or '') + (' (*)' if i.get('recommended') else '')
                    marks = ''.join(i.get('footnotes', []))
                    if not any(x.startswith(printed) and re.sub(r'[\s,]', '', x[len(printed):]) == re.sub(r'[\s,]', '', marks) for x in cells):
                        probs.append(f'roadmap item not printed as one cell: {printed[:60]}')
    else:
        rd = r.get('rule_details', {})
        wrapped = c.get('extractor') == 'clearpath_plan/v1'  # two-column PDF: wrapped titles are printed in pieces
        items = list(rd.get('courses', []))
        for term in rd.get('terms', []) or []:
            items += [i for i in term.get('items', []) if isinstance(i, dict)]
        for i in items:
            for f in ('text', 'milestone'):  # printed text rows and milestone cells (UO degree maps)
                if i.get(f) and squash(i[f]) not in squashed and not (wrapped and segmented(squash(i[f]), squashed)):
                    probs.append(f"{f} of an item not verbatim")
            if 'code' in i and not code_in(text, i['code']): probs.append(f"course {i['code']} not in source")
            elif i.get('title') and not all(squash(part) in squashed for part in re.split(r'\s*\(', i['title'][:80]) if squash(part)) \
                    and not (wrapped and segmented(squash(i['title']), squashed)):
                # PDF plans print a gen-ed tag such as "(Quantitative Reasoning)" on the next line; each part must be printed
                probs.append(f"title of {i.get('code')} not verbatim")
        if r.get('minimum_credits') is not None and not re.search(rf'\b{int(r["minimum_credits"])}\b', text): probs.append('minimum_credits not printed')
    return probs


_ELSEWHERE = {}


def elsewhere(sha, root=None):
    """Text of a document with this sha256 stored by any local run of the same tree ('' when none holds it)."""
    if sha in _ELSEWHERE: return _ELSEWHERE[sha]
    base = Path(root) if root else Path(__file__).resolve().parents[1] / 'programs' / 'runs'
    text = ''
    for man in sorted(base.glob('*/*/manifest.jsonl')):
        for line in man.read_text().splitlines():
            if sha in line:
                e = json.loads(line)
                if e.get('sha256') == sha and e.get('page_file'):
                    text = Run(man.parent).load_page(e['page_file'])[0].text; break
        if text: break
    _ELSEWHERE[sha] = text
    return text


def main(run_dir, keys=None):
    run = Run(Path(run_dir)); d = Path(run_dir)
    pages = {e.get('sha256'): e['page_file'] for e in run.entries() if e.get('page_file')}
    cache, report, bad = {}, {}, 0
    for line in (d / 'candidates.jsonl').read_text().splitlines():
        c = json.loads(line)
        if keys and c['institution_key'] not in keys: continue
        pf = pages.get(c['source'].get('sha256'))
        if pf not in cache: cache[pf] = run.load_page(pf)[0].text if pf else ''
        def other(sha):
            f = pages.get(sha)
            if f is None:  # a document stored by another run of the same state (a state program inventory, a discovery list)
                return elsewhere(sha)
            if f not in cache: cache[f] = run.load_page(f)[0].text if f else ''
            return cache[f]
        probs = check_candidate(c, cache[pf], other) if pf else ['source document not in run']
        report[c['candidate_id']] = probs
        bad += bool(probs)
    for line in (d / 'evidence.jsonl').read_text().splitlines():
        e = json.loads(line)
        if keys and e['institution_key'] not in keys: continue
        pf = pages.get(e['sha256'])
        if pf not in cache: cache[pf] = run.load_page(pf)[0].text if pf else ''
        if norm(e['sentence']) not in norm(cache[pf]):
            report['evidence:' + e['evidence_id']] = ['sentence not verbatim']; bad += 1
    (d / 'verify.json').write_text(json.dumps(report, indent=1, sort_keys=True) + '\n')
    print(f'{len(report)} checked, {bad} with problems -> {d / "verify.json"}')
    return report


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:] or None)
