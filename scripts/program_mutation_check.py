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
