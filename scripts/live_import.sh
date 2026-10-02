#!/usr/bin/env bash
# Import every repository record into a live (already-migrated) database, reconcile, then
# prove idempotence with a second pass. Requires DATABASE_URL (admin connection string).
# Never echo the URL; psql reads it from the environment.
set -euo pipefail
: "${DATABASE_URL:?DATABASE_URL must be set to an admin connection string}"
cd "$(dirname "$0")/.."
work="$(mktemp -d)"; trap 'rm -rf "$work"' EXIT
run() { psql "$DATABASE_URL" -X -q -v ON_ERROR_STOP=1 "$@"; }
scalar() { psql "$DATABASE_URL" -X -q -A -t -v ON_ERROR_STOP=1 -c "$1"; }

python scripts/validate_data.py
python scripts/check_migration_history.py --live
run -f supabase/checks/live_preflight.sql
echo "Preflight passed"
python scripts/import_supabase.py --output "$work/batches" --reconcile-sql "$work/reconcile.sql" --existing-database

for f in "$work"/batches/*.sql; do run -f "$f"; done
echo "Import pass 1 applied"
run -f "$work/reconcile.sql"
echo "Reconciliation passed: ledger and normalized counts match the repository"

before="$(scalar "select (select count(*) from ingestion.reference_revisions)||':'||coalesce((select max(imported_at)::text from ingestion.reference_records),'')")"
for f in "$work"/batches/*.sql; do run -f "$f"; done
after="$(scalar "select (select count(*) from ingestion.reference_revisions)||':'||coalesce((select max(imported_at)::text from ingestion.reference_records),'')")"
if [ "$before" != "$after" ]; then
  echo "Idempotence check failed: revision count / last import changed ($before -> $after)" >&2
  exit 1
fi
run -f "$work/reconcile.sql"
echo "Import pass 2 changed nothing (revisions and last import time unchanged); reconciliation passed again"
