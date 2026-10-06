#!/usr/bin/env python3
"""Mutation checks for the Program & Degree Deep Dive safety rules (programs/, backend/program_fields.py).

Kept separate from scripts/mutation_check.py (the national pipeline's) so the two workstreams never edit
the same file. Each mutant breaks one rule; tests/test_programs_deep_dive.py must then fail ("KILLED").
"""
import shutil, subprocess, sys

MUTS = [
    ('programs/crawl.py', "return registrable_domain(h) in set(target.get('domains', []))", 'return True'),
    ('programs/crawl.py', "keep = '&'.join(f'{k}={q[k][0]}' for k in ('catoid', 'poid', 'navoid') if k in q)", "keep = p.query"),
    ('programs/crawl.py', "rx = re.compile(r'preview_program\\.php\\?catoid=%s&poid=\\d+' % re.escape(str(cat.get('catoid'))))",
     "rx = re.compile(r'preview_program\\.php\\?catoid=\\d+&poid=\\d+')"),
    ('programs/crawl.py', "if url in seen or not in_scope(target, url): return", 'if url in seen: return'),
    ('programs/crawl.py', "seen = {e['url'] for e in run.entries() if e.get('institution_key') == key}", 'seen = set()'),
    ('programs/extract.py', "if GRAD.search(name) and not BACHELOR.search(name): return None", 'pass'),
    ('programs/extract.py', "if 25 <= len(s) <= 600: yield s", 'yield s'),
    ('backend/program_fields.py', "errs += _evidence_errors(r.get('admission_details'), 'admission_details')", 'pass'),
    ('backend/program_fields.py', "if not str(r.get('cip_source_url', '')).startswith('https://'): errs.append('cip_code needs cip_source_url (official https)')", 'pass'),
    ('backend/program_fields.py', "if missing: errs.append(", 'if False: errs.append('),
    ('backend/program_fields.py', "if not isinstance(keys, list) or len(keys) != n or len(set(keys)) != len(keys):", 'if False:'),
    ('backend/program_fields.py', "if (r.get('program_keys') or r.get('cip_codes')) and not (r.get('major_requirement') or '').strip():", 'if False:'),
    ('programs/smartcatalog.py', "if not name or not BACHELOR.search(name) or NOT_PROGRAM.search(name): return []", "if not name or not BACHELOR.search(name): return []"),
    ('programs/smartcatalog.py', "'group_type': 'all_required' if (REQUIRED.search(heading) and not CHOOSE.search(heading)) else 'elective_pool'", "'group_type': 'elective_pool' if CHOOSE.search(heading) else 'all_required'"),
    ('programs/thec.py', "        if (PROGRAMS, json.dumps(payload, sort_keys=True)) in done: continue", "        pass"),
    ('backend/program_fields.py', "        if k in cat:", "        if False:"),
    ('programs/status.py', "complete = not unaccounted and not pending and not errors and share >= COVERAGE_SHARE", "complete = not pending and not errors and share >= COVERAGE_SHARE"),
    ('programs/status.py', "complete = not unaccounted and not pending and not errors and share >= COVERAGE_SHARE", "complete = not unaccounted and not pending and not errors"),
    ('programs/status.py', "complete = not unaccounted and not pending and not errors and share >= COVERAGE_SHARE", "complete = not unaccounted and not errors and share >= COVERAGE_SHARE"),
    ('programs/status.py', "covered = complete or (share is not None and share >= CATALOG_SHARE)", "covered = complete or (share is not None and share > 0)"),
    ('programs/status.py', "folders = {f.parts[-3] for f in (ROOT / 'data/institutions').glob('*/program_catalogs/*.json')}", "folders = set()"),
    ('programs/status.py', "verified = [r for r in progs if r.get('verification_status') == 'verified' and r.get('credential_level') == 'bachelor']", "verified = [r for r in progs if r.get('credential_level') == 'bachelor']"),
    ('programs/status.py', "covered = [r for r in rows if r['status'] in ('covered', 'covered_open_items')]", "covered = [r for r in rows if r['status'] != 'not_started']"),
    ('programs/status.py', "four = [i for i in reg['institutions'] if i.get('level') == 'four_year']", "four = list(reg['institutions'])"),
    ('programs/status.py', "if not (e.get('next_action') or '').strip(): errs.append", "if False: errs.append"),
    ('programs/status.py', "'degree_maps': 'met' if verified and len(plans & vkeys) >= PLAN_SHARE * len(verified)", "'degree_maps': 'met' if plans"),
    ('programs/status.py', "if cur != j: print(", "if False: print("),
    ('programs/extract.py', "    if heading not in [h.strip() for h in page.headings]: return []", "    pass"),
    ('programs/extract.py', "    if printed == name or OPTION_NAME.search(printed): return []", "    pass"),
    ('programs/verify.py', "if not other or norm(r['program_name']) not in norm(other(nev['sha256'])): probs.append", "if False: probs.append"),
    ('programs/verify.py', "if ev.get('field') == 'program_page_heading' and norm(ev.get('value', '')) not in t: probs.append", "if False: probs.append"),
    ('pipeline/crawl.py', "        return 'robots_unreachable' if getattr(rp, 'unreachable', False) else 'disallowed_by_robots'", "        return 'disallowed_by_robots'"),
    ('programs/queue_suggest.py', "            if f['challenged'] and not f['program_pages']:", "            if f['challenged'] or f['robots']:"),
    ('programs/queue_suggest.py', "            if n and hit == 0:", "            if hit == 0:"),
    ('programs/queue_suggest.py', "        if (k, gap) in have or (k, 'institution') in have: return", "        pass"),
]


def main():
    survived = []
    for path, old, new in MUTS:
        src = open(path, encoding='utf-8').read()
        if src.count(old) != 1:
            print(f'STALE mutant (pattern not found once) in {path}: {old[:70]}'); survived.append(path); continue
        shutil.copy(path, path + '.bak')
        try:
            open(path, 'w', encoding='utf-8').write(src.replace(old, new))
            r = subprocess.run([sys.executable, '-m', 'unittest', 'tests.test_programs_deep_dive'], capture_output=True)
            status = 'KILLED' if r.returncode else 'SURVIVED'
            print(f'{status}: {path}: {old[:70]}')
            if r.returncode == 0: survived.append(path)
        finally:
            shutil.move(path + '.bak', path)
    print(f'{len(MUTS) - len(survived)}/{len(MUTS)} mutants killed')
    return 1 if survived else 0


if __name__ == '__main__':
    raise SystemExit(main())
