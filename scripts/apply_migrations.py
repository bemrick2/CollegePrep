#!/usr/bin/env python3
"""Apply pending repository migrations to the live database, recording each under its own version.

Each pending file runs in one transaction together with its row in
supabase_migrations.schema_migrations. The whole file text is stored as a single statement, which
is how the Supabase connector recorded the earlier migrations, so `check_migration_history.py --live`
compares content the same way for every version. Pending means: in the repository, not live, and
newer than the newest live version (older pending files are refused by the history check).

  DATABASE_URL=... python scripts/apply_migrations.py            # apply
  DATABASE_URL=... python scripts/apply_migrations.py --dry-run  # list only
"""
from __future__ import annotations
import argparse, os, re, secrets, subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_migration_history as h
from live_write_guard import require_live_writes


TRANSACTION_CONTROL = re.compile(r'^\s*(begin|commit|rollback|start\s+transaction|end)\s*;', re.I | re.M)


def transaction_sql(path: Path, version: str, name: str) -> str:
    text = path.read_text(encoding='utf-8').replace('\r', '')
    if TRANSACTION_CONTROL.search(text):
        raise ValueError(f'{path.name} controls its own transaction; the applier wraps each migration in one')
    tag = 'm' + secrets.token_hex(8)
    while f'${tag}$' in text:
        tag = 'm' + secrets.token_hex(8)
    return (f"begin;\n\\i '{path.as_posix()}'\n"
            f"insert into supabase_migrations.schema_migrations(version, name, statements)\n"
            f"values ('{version}', '{name}', array[${tag}${text}${tag}$]);\ncommit;\n")


def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument('--dry-run', action='store_true'); a = p.parse_args()
    if not a.dry_run:
        require_live_writes()
    url = os.environ.get('DATABASE_URL') or sys.exit('DATABASE_URL is required')
    local, errors = h.local_migrations()
    errors += h.offline_errors(local)
    if not errors:
        more, pending_files = h.live_errors(local, h.live_rows()); errors += more
    if errors:
        print('\n'.join(errors)); return 1
    if not pending_files:
        print('No pending migrations'); return 0
    by_file = {v['file']: (k, v['name']) for k, v in local.items()}
    for f in pending_files:
        version, name = by_file[f]
        if a.dry_run:
            print('pending', f); continue
        with tempfile.NamedTemporaryFile('w', suffix='.sql', delete=False) as tmp:
            tmp.write(transaction_sql(h.MIGRATIONS / f, version, name))
        if subprocess.run(['psql', url, '-X', '-q', '-v', 'ON_ERROR_STOP=1', '-f', tmp.name]).returncode:
            print(f'{f} failed and was rolled back; nothing after it was applied'); return 1
        print('applied', f)
    if not a.dry_run:
        more, still = h.live_errors(local, h.live_rows())
        if more or still:
            print('\n'.join(more + [f'still pending: {s}' for s in still])); return 1
        print('Live history matches the repository')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
