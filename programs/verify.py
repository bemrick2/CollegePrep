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
    subj, num = code.split(' ', 1)
    return re.search(rf'\b{re.escape(subj)}\s?{re.escape(num)}\b', text, re.I) is not None


def check_candidate(c, text):
    probs = []
    r = c['record']; t = norm(text); squashed = squash(text)
    if c['domain'] == 'academic_programs':
        if norm(r['program_name']) not in t: probs.append('program_name not verbatim')
        cy = r.get('catalog_year') or ''
        y = re.match(r'(20\d{2})-(20\d{2})', cy)
        if y and not re.search(rf'{y.group(1)}\s*[-–]\s*({y.group(2)}|{y.group(2)[2:]})', text): probs.append('catalog year not printed')
        n = int(r['total_credits']) if r.get('total_credits') is not None else None
        if n is not None and not re.search(rf'total[^0-9]{{0,40}}\b{n}\b|\b{n}\s+(total|hours\s+total)', text, re.I):
            probs.append('total_credits not printed next to a total label')
    else:
        rd = r.get('rule_details', {})
        items = list(rd.get('courses', []))
        for term in rd.get('terms', []) or []:
            items += [i for i in term.get('items', []) if isinstance(i, dict)]
        for i in items:
            if 'code' in i and not code_in(text, i['code']): probs.append(f"course {i['code']} not in source")
            elif i.get('title') and not all(squash(part) in squashed for part in re.split(r'\s*\(', i['title'][:80]) if squash(part)):
                # PDF plans print a gen-ed tag such as "(Quantitative Reasoning)" on the next line; each part must be printed
                probs.append(f"title of {i.get('code')} not verbatim")
        if r.get('minimum_credits') is not None and not re.search(rf'\b{int(r["minimum_credits"])}\b', text): probs.append('minimum_credits not printed')
    return probs


def main(run_dir, keys=None):
    run = Run(Path(run_dir)); d = Path(run_dir)
    pages = {e.get('sha256'): e['page_file'] for e in run.entries() if e.get('page_file')}
    cache, report, bad = {}, {}, 0
    for line in (d / 'candidates.jsonl').read_text().splitlines():
        c = json.loads(line)
        if keys and c['institution_key'] not in keys: continue
        pf = pages.get(c['source'].get('sha256'))
        if pf not in cache: cache[pf] = run.load_page(pf)[0].text if pf else ''
        probs = check_candidate(c, cache[pf]) if pf else ['source document not in run']
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
