#!/usr/bin/env python3
"""Apply pending repository migrations to the live database, recording each under its own version.

Each pending file runs in one transaction together with its row in
supabase_migrations.schema_migrations. The whole file text is stored as a single statement, which
is how the Supabase connector recorded the earlier migrations, so `check_migration_history.py --live`
compares content the same way for every version. Pending means: in the repository, not live, and
newer than the newest live version (older pending files are refused by the history check).

  DATABASE_URL=... python scripts/apply_migrations.py            # apply
  DATABASE_URL=... python scripts/apply_migrations.py --dry-run  # list only
  DATABASE_URL=... python scripts/apply_migrations.py --until 20261022040000 [--dry-run]
      # apply (or list) pending files up to and including that version, then stop; later files stay pending.
      # The version must be a repository migration; an unknown version is refused before anything is applied.
  DATABASE_URL=... python scripts/apply_migrations.py --until 20261023010000 --reserve supabase/reserve/<file>.sql [--dry-run]
      # CR-23 reserve release: the selected pending migrations and the reserve script (scripts/make_reserve_migration.py)
      # run in ONE transaction, so the assessment pool, check assignment and reserve commit together or not at all.

The assessment-pool migration (20261022050000) is refused without --reserve: applying it alone would leave every
progress check unmeasured, and a push-triggered run must never apply it early. A reserve script must live outside
supabase/migrations/, start with the generator's marker, and needs 20261023010000 live or in the same run.
"""
from __future__ import annotations
import argparse, os, re, secrets, subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_migration_history as h
from live_write_guard import require_live_writes


TRANSACTION_CONTROL = re.compile(r'^\s*(begin|commit|rollback|start\s+transaction|end)\s*;', re.I | re.M)


def migration_block(path: Path, version: str, name: str) -> str:
    """One migration and its schema_migrations row, for use inside a transaction."""
    text = path.read_text(encoding='utf-8').replace('\r', '')
    if TRANSACTION_CONTROL.search(text):
        raise ValueError(f'{path.name} controls its own transaction; the applier wraps each migration in one')
    tag = 'm' + secrets.token_hex(8)
    while f'${tag}$' in text:
        tag = 'm' + secrets.token_hex(8)
    return (f"\\i '{path.as_posix()}'\n"
            f"insert into supabase_migrations.schema_migrations(version, name, statements)\n"
            f"values ('{version}', '{name}', array[${tag}${text}${tag}$]);\n")


def transaction_sql(path: Path, version: str, name: str) -> str:
    return 'begin;\n' + migration_block(path, version, name) + 'commit;\n'


# Migrations that may only be applied together with a reserve script (CR-23 paired release).
REQUIRES_RESERVE = {'20261022050000'}
# The reserve script reads tables this migration creates.
RESERVE_NEEDS = '20261023010000'


def check_reserve(path: Path) -> list[str]:
    """Errors for a --reserve script: outside supabase/migrations/, generated (marker), no own transaction control."""
    from make_reserve_migration import MARKER, inside_migrations
    if inside_migrations(path, h.MIGRATIONS):
        return [f'--reserve {path}: a reserve script must not live under supabase/migrations/']
    try:
        text = path.read_text(encoding='utf-8').replace('\r', '')
    except OSError as e:
        return [f'--reserve {path}: {e}']
    if not text.startswith(MARKER):
        return [f'--reserve {path}: not a reserve script from scripts/make_reserve_migration.py']
    if TRANSACTION_CONTROL.search(text):
        return [f'--reserve {path}: controls its own transaction']
    return []


def combined_transaction_sql(blocks: list[tuple[Path, str, str]], reserve: Path) -> str:
    """The selected migrations and the reserve script in one transaction: all commit, or none does."""
    return ('begin;\n' + ''.join(migration_block(p, v, n) for p, v, n in blocks)
            + f"\\i '{reserve.resolve().as_posix()}'\ncommit;\n")


VERSION = re.compile(r'^\d{14}$')


def check_until(until: str | None, local: dict) -> list[str]:
    """Errors for an --until value: it must name a repository migration version."""
    if until is None:
        return []
    if not VERSION.match(until):
        return [f'--until {until!r} is not a 14-digit migration version']
    if until not in local:
        return [f'--until {until}: no repository migration has that version; nothing was applied']
    return []


def select_until(pending_files: list[str], local: dict, until: str | None) -> list[str]:
    """The pending files to apply: all of them, or those up to and including version `until`."""
    if until is None:
        return list(pending_files)
    version_of = {v['file']: k for k, v in local.items()}
    return [f for f in pending_files if version_of[f] <= until]


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--until', metavar='VERSION', help='apply pending migrations up to and including this version, then stop')
    p.add_argument('--reserve', metavar='FILE', type=Path,
                   help='CR-23 reserve script to run in the same single transaction as the selected migrations')
    a = p.parse_args(argv)
    local, errors = h.local_migrations()
    pre = check_until(a.until, local) + (check_reserve(a.reserve) if a.reserve else [])
    if pre:
        print('\n'.join(pre)); return 1
    if not a.dry_run:
        require_live_writes()
    url = os.environ.get('DATABASE_URL') or sys.exit('DATABASE_URL is required')
    errors += h.offline_errors(local)
    if not errors:
        more, pending_files = h.live_errors(local, h.live_rows()); errors += more
    if errors:
        print('\n'.join(errors)); return 1
    all_pending = list(pending_files)
    later = []
    if a.until is not None:
        chosen = select_until(pending_files, local, a.until)
        later = pending_files[len(chosen):]
        pending_files = chosen
    by_file = {v['file']: (k, v['name']) for k, v in local.items()}
    chosen_versions = {by_file[f][0] for f in pending_files}
    if chosen_versions & REQUIRES_RESERVE and not a.reserve:
        print('Refused, nothing applied: ' + ', '.join(sorted(chosen_versions & REQUIRES_RESERVE))
              + ' (assessment pool) applies only with --reserve, in one transaction with the reserve script'
              + ' (docs/DEPLOYING.md, CR-23 reserve release). Use --until to stop before it.')
        return 1
    if a.reserve:
        live = {k for k, v in local.items() if v['file'] not in all_pending}
        if RESERVE_NEEDS not in live | chosen_versions:
            print(f'Refused, nothing applied: the reserve script needs {RESERVE_NEEDS} live or in this run'); return 1
    if not pending_files and not a.reserve:
        print('No pending migrations' + (f' up to {a.until}' if a.until else '')); return 0
    if a.reserve:
        for f in pending_files:
            print('pending', f, '(same transaction as the reserve)' if a.dry_run else '')
        print('reserve', a.reserve, '(one transaction with the migrations above)')
        if not a.dry_run:
            sql = combined_transaction_sql([(h.MIGRATIONS / f, *by_file[f]) for f in pending_files], a.reserve)
            with tempfile.NamedTemporaryFile('w', suffix='.sql', delete=False) as tmp:
                tmp.write(sql)
            if subprocess.run(['psql', url, '-X', '-q', '-v', 'ON_ERROR_STOP=1', '-f', tmp.name]).returncode:
                print('The transaction failed and was rolled back: no migration was applied and nothing was marked'); return 1
            for f in pending_files:
                print('applied', f)
            print('applied reserve', a.reserve)
    else:
        for f in pending_files:
            version, name = by_file[f]
            if a.dry_run:
                print('pending', f); continue
            with tempfile.NamedTemporaryFile('w', suffix='.sql', delete=False) as tmp:
                tmp.write(transaction_sql(h.MIGRATIONS / f, version, name))
            if subprocess.run(['psql', url, '-X', '-q', '-v', 'ON_ERROR_STOP=1', '-f', tmp.name]).returncode:
                print(f'{f} failed and was rolled back; nothing after it was applied'); return 1
            print('applied', f)
    for f in later:
        print('not applied (after --until):', f)
    if not a.dry_run:
        more, still = h.live_errors(local, h.live_rows())
        if more or still != later:
            print('\n'.join(more + [f'still pending: {s}' for s in still if s not in later])); return 1
        print('Live history matches the repository' + (f' up to {a.until}' if a.until else ''))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
