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
import json, re
from collections import defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

from pipeline import text as T
from pipeline.crawl import Run
from pipeline.extractors import catalog as CAT, programmap as PM, common
from .crawl import program_rule

GRAD = re.compile(r'\b(M\.?\s?S\.?|M\.?\s?A\.?|MBA|M\.?\s?Ed|M\.?\s?F\.?A|Ph\.?\s?D|Ed\.?\s?D|DNP|D\.?\s?P\.?\s?T|J\.?\s?D|'
                  r'Master|Doctor|Graduate|Post[- ]?bacc|Certificate|Minor|Endorsement)\b', re.I)
BACHELOR = re.compile(r'\b(B\.?\s?(A|S|F\.?A|M|S\.?N|S\.?W|B\.?A|S\.?E|S\.?E\.?E|S\.?M\.?E|S\.?C\.?E|Arch|Mus|A\.?S|A\.?A\.?S|S\.?Ed|I\.?S)\b\.?|'
                      r'Bachelor|\bH?BA\b|\bH?BS\b)', re.I)
ASSOCIATE = re.compile(r'\b(A\.?\s?(A|S|A\.?S|A\.?T|S\.?T|F\.?A)\b\.?|Associate)', re.I)

EVIDENCE = [
    ('direct_admission', re.compile(r'\bdirect(ly)?[\s-]+admi(t|ts|tted|ssion|ssions)\b|\badmitted\s+directly\b', re.I)),
    ('apply_to_major', re.compile(r'\b(apply|application|applying)\s+(for|to)\s+(admission\s+(to|into)\s+)?(the\s+|a\s+)?'
                                  r'(major|program|professional|upper[\s-]*division|nursing|school|college|bba|bsn|engineering)|'
                                  r'\badmission\s+(to|into)\s+the\s+(major|program|professional|upper[\s-]*division|nursing|school)|'
                                  r'\b(competitive|selective)\s+admission|\bspace[\s-]+limited\b|\blimited\s+enrollment\b', re.I)),
    ('pre_major', re.compile(r'\bpre[\s-](major|nursing|engineering|business|professional|health|computer)', re.I)),
    ('progression', re.compile(r'\b(progression|progress\s+to|continu(e|ation)\s+in\s+the\s+(major|program)|good\s+standing\s+in\s+the\s+major)\b', re.I)),
    ('gpa_requirement', re.compile(r'\b(minimum|cumulative|overall|combined|institutional)\b[^.]{0,60}\bG\.?P\.?A\.?\b[^.]{0,30}\b[1-4]\.\d{1,2}\b|'
                                   r'\b[1-4]\.\d{1,2}\b[^.]{0,30}\b(cumulative|overall|minimum)?\s*G\.?P\.?A', re.I)),
    ('undeclared', re.compile(r'\b(undeclared|undecided|exploratory|explor(e|ing)\s+(majors|options|studies)|academic\s+focus)\b', re.I)),
    ('declare_by', re.compile(r'\bdeclare\s+(a|their|your)?\s*major\b[^.]{0,80}\b(by|before|no\s+later|prior\s+to|within|upon)\b', re.I)),
    ('change_major', re.compile(r'\b(change\s+(of\s+)?(a\s+|their\s+|your\s+)?majors?|changing\s+(their\s+|your\s+)?majors?|'
                                r'internal\s+transfer|intra[\s-]*university\s+transfer|transfer\s+(into|to)\s+(the|another)\s+(major|college|school))\b', re.I)),
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


def collect_lists(target, run, entries):
    """Program links on the current catalog's list/navigation pages, deduplicated by URL."""
    is_program = program_rule(target)
    out, years = {}, set()
    for e in entries:
        if e.get('role') not in ('catalog_home', 'catalog_nav', 'program_list') or not e.get('page_file'): continue
        page, d = run.load_page(e['page_file'])
        y, printed = CAT.catalog_year(page)
        if printed: years.add(printed)
        for href, anchor in d.get('links', []):
            name = re.sub(r'\s+', ' ', anchor or '').strip()
            if not is_program(href) or not name or len(name) > 200: continue
            if href not in out:
                out[href] = {'name': name, 'url': href, 'credential_level': credential_of(name),
                             'listed_on': e['url'], 'listed_on_sha256': e.get('sha256'), 'listed_on_title': e.get('title', '')}
    progs = sorted(out.values(), key=lambda p: p['name'].lower())
    return {'printed_years': sorted(years), 'programs': progs,
            'counts': {'links': len(progs), 'bachelor': sum(p['credential_level'] == 'bachelor' for p in progs),
                       'associate': sum(p['credential_level'] == 'associate' for p in progs),
                       'unclassified': sum(p['credential_level'] is None for p in progs)}}


def extract_run(targets, run_dir, today=None):
    run = Run(Path(run_dir)); today = today or date.today()
    today_year = T.current_academic_year(today)
    entries = run.entries()
    by_inst = defaultdict(list)
    for e in entries: by_inst[e.get('institution_key')].append(e)
    tmap = {t['institution_key']: t for t in targets['institutions']}
    lists, cands, evidence, summary = {}, [], [], {}
    for key, es in sorted(by_inst.items()):
        t = tmap.get(key, {'institution_key': key, 'catalog': {}})
        roles = defaultdict(lambda: {'fetched': 0, 'ok': 0, 'errors': defaultdict(int)})
        for e in es:
            r = roles[e.get('role') or '?']; r['fetched'] += 1
            if e.get('page_file'): r['ok'] += 1
            elif e.get('error'): r['errors'][e['error'][:40]] += 1
        lists[key] = collect_lists(t, run, es) if t.get('catalog') else {'programs': [], 'counts': {}}
        n_c = 0; seen_ev = set()
        for e in es:
            if not e.get('page_file'): continue
            page, _ = run.load_page(e['page_file'])
            inst = {'institution_key': key}
            if e.get('role') == 'program_page':
                for c in CAT.extract(inst, e, page, today_year):
                    c['program_role'] = 'program_page'; cands.append(c); n_c += 1
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
                            evidence.append({'institution_key': key, 'category': cat, 'sentence': s,
                                             'url': common.source_of(e)['url'], 'sha256': e.get('sha256'),
                                             'fetched_at': e.get('fetched_at'), 'page_title': e.get('title', ''),
                                             'role': e.get('role'), 'year_labels': sorted(T.year_labels(page.title + ' ' + page.text[:3000]))})
        summary[key] = {'roles': {k: {**v, 'errors': dict(v['errors'])} for k, v in roles.items()},
                        'program_list_links': lists[key]['counts'], 'candidates': n_c,
                        'evidence': sum(1 for x in evidence if x['institution_key'] == key)}
    d = Path(run_dir)
    (d / 'program_lists.json').write_text(json.dumps(lists, indent=1, ensure_ascii=False) + '\n')
    with (d / 'candidates.jsonl').open('w') as f:
        for c in cands: f.write(json.dumps(c, sort_keys=True, ensure_ascii=False) + '\n')
    with (d / 'evidence.jsonl').open('w') as f:
        for x in evidence: f.write(json.dumps(x, sort_keys=True, ensure_ascii=False) + '\n')
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
