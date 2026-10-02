#!/usr/bin/env python3
"""Keep repository migrations aligned with the live Supabase migration history.

Offline (default): every file in supabase/migrations must be named <14-digit version>_<name>.sql,
versions must be unique, and every migration recorded in supabase/migration_history.json must
still exist with unchanged content (normalized for line endings and trailing whitespace).

Live (--live, needs DATABASE_URL): compares supabase_migrations.schema_migrations with the
repository. It fails if a live migration is missing locally, if a version's content differs, or
if a migration name is recorded live under a different version than the local file -- the exact
condition that makes `supabase db push` try to re-apply an already-applied migration.
Unapplied local migrations are reported as pending, not as errors.
"""
from __future__ import annotations
import argparse, base64, hashlib, json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MIGRATIONS = ROOT / 'supabase/migrations'
HISTORY = ROOT / 'supabase/migration_history.json'
NAME = re.compile(r'^(\d{14})_([a-z0-9_]+)\.sql$')


def normalized_md5(text: str) -> str:
    return hashlib.md5(text.replace('\r', '').rstrip('\n ').encode('utf-8')).hexdigest()


def canonical(text: str) -> str:
    """Content compared independently of how it was recorded: Supabase's own migration tooling stores one
    array element per statement (semicolons dropped, comments kept on the first), this repository's
    applier stores the whole file as one element. Comments, semicolons and whitespace are not compared."""
    text = re.sub(r'--[^\n]*', '', text.replace('\r', ''))
    return re.sub(r'\s+', ' ', text.replace(';', ' ')).strip()


def canonical_md5(text: str) -> str:
    return hashlib.md5(canonical(text).encode('utf-8')).hexdigest()


def local_migrations():
    found, errors = {}, []
    for path in sorted(MIGRATIONS.glob('*')):
        m = NAME.match(path.name)
        if not m:
            errors.append(f'{path.name}: migration files must be named <14-digit version>_<snake_name>.sql')
            continue
        version, name = m.groups()
        if version in found:
            errors.append(f'{path.name}: duplicate version {version}')
        text = path.read_text(encoding='utf-8')
        found[version] = {'name': name, 'file': path.name, 'md5': normalized_md5(text), 'canonical_md5': canonical_md5(text)}
    return found, errors


def offline_errors(local):
    errors = []
    history = json.loads(HISTORY.read_text(encoding='utf-8'))
    for entry in history['applied']:
        here = local.get(entry['version'])
        if not here:
            errors.append(f"applied migration {entry['version']}_{entry['name']} is missing from supabase/migrations")
        elif here['name'] != entry['name'] or here['md5'] != entry['normalized_md5']:
            errors.append(f"applied migration {here['file']} was renamed or edited after it was applied live")
    names = [v['name'] for v in local.values()]
    for dup in sorted({n for n in names if names.count(n) > 1}):
        errors.append(f'migration name {dup} appears under more than one version')
    return errors


def live_rows():
    url = os.environ.get('DATABASE_URL')
    if not url:
        sys.exit('DATABASE_URL is required for --live')
    sql = ("select version||'|'||name||'|'||md5(rtrim(replace(array_to_string(statements,E'\\n'),E'\\r',''),E'\\n '))||'|'||"
           "translate(encode(convert_to(array_to_string(statements,E'\\n'),'UTF8'),'base64'),E'\\n','') "
           "from supabase_migrations.schema_migrations order by version")
    out = subprocess.run(['psql', url, '-X', '-A', '-t', '-v', 'ON_ERROR_STOP=1', '-c', sql],
                         check=True, capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines():
        if not line.strip(): continue
        version, name, md5, b64 = line.split('|')
        rows.append([version, name, md5, canonical_md5(base64.b64decode(b64).decode('utf-8'))])
    return rows


def live_errors(local, rows):
    errors, by_name = [], {v['name']: k for k, v in local.items()}
    live_versions = set()
    for version, name, md5, *rest in rows:
        live_canonical = rest[0] if rest else None
        live_versions.add(version)
        here = local.get(version)
        if here is None:
            if name in by_name:
                errors.append(f'live {version}_{name} is stored locally as {local[by_name[name]]["file"]}; rename the file to the live version')
            else:
                errors.append(f'live migration {version}_{name} has no local file')
        elif here['name'] != name:
            errors.append(f'version {version}: live name {name} differs from local {here["file"]}')
        elif here['md5'] != md5 and here['canonical_md5'] != live_canonical:
            errors.append(f'version {version}: local {here["file"]} content differs from what was applied live')
    pending = [v['file'] for k, v in sorted(local.items()) if k not in live_versions]
    if pending and max(live_versions or {''}) > min(k for k, v in local.items() if v['file'] in pending):
        errors.append('pending local migrations are older than the newest live migration; give them a newer version: ' + ', '.join(pending))
    return errors, pending


def main():
    p = argparse.ArgumentParser(); p.add_argument('--live', action='store_true'); a = p.parse_args()
    local, errors = local_migrations()
    errors += offline_errors(local)
    pending = []
    if a.live and not errors:
        more, pending = live_errors(local, live_rows())
        errors += more
    if errors:
        print('\n'.join(errors)); return 1
    msg = f'Migration history OK: {len(local)} local migrations'
    if a.live:
        msg += f'; live history matches; pending: {", ".join(pending) or "none"}'
    print(msg); return 0


if __name__ == '__main__':
    raise SystemExit(main())
