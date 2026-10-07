#!/usr/bin/env bash
# A disposable local copy of the CollegePrep backend: plain PostgreSQL with every repository migration, the app's
# original demo question bank, and PostgREST serving it at http://127.0.0.1:${PGRST_PORT:-54321}/rest/v1 the way
# Supabase does. Used to run the web app's LiveSource against real RPCs while the hosted project is unavailable.
#
#   scripts/local/live_stack.sh up      # (re)create the database and start PostgREST + the /rest/v1 proxy
#   scripts/local/live_stack.sh down    # stop them
#   scripts/local/live_stack.sh test    # fresh database, then the LiveSource end-to-end test against it
#
# Needs: a local PostgreSQL superuser (PGHOST/PGUSER/PGPASSWORD, default postgres@localhost) and a PostgREST binary
# (POSTGREST_BIN). Nothing here talks to the hosted project. Auth is not emulated: tests sign JWTs for fixture
# users with LOCAL_JWT_SECRET, as Supabase Auth would.
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/../.." && pwd)
export PGHOST=${PGHOST:-localhost} PGUSER=${PGUSER:-postgres} PGPASSWORD=${PGPASSWORD:-postgres}
DB=${LOCAL_DB:-cp_local}
PORT=${PGRST_PORT:-54321}
SECRET=${LOCAL_JWT_SECRET:-local-only-jwt-secret-at-least-32-characters}
RUN=${LOCAL_RUN_DIR:-/tmp/cp-local}
mkdir -p "$RUN"

down() {
  [ -f "$RUN/pgrst.pid" ] && kill "$(cat "$RUN/pgrst.pid")" 2>/dev/null || true
  [ -f "$RUN/proxy.pid" ] && kill "$(cat "$RUN/proxy.pid")" 2>/dev/null || true
  rm -f "$RUN"/*.pid
}

up() {
  down
  psql -q -X -v ON_ERROR_STOP=1 -d postgres -c "drop database if exists $DB with (force)" -c "create database $DB" >/dev/null
  export PGDATABASE=$DB
  psql -q -X -v ON_ERROR_STOP=1 >/dev/null <<'SQL'
do $$ begin
  if not exists (select 1 from pg_roles where rolname = 'anon') then create role anon nologin; end if;
  if not exists (select 1 from pg_roles where rolname = 'authenticated') then create role authenticated nologin; end if;
  if not exists (select 1 from pg_roles where rolname = 'service_role') then create role service_role nologin bypassrls; end if;
  if not exists (select 1 from pg_roles where rolname = 'authenticator') then
    create role authenticator login noinherit password 'authenticator';
  end if;
end $$;
grant anon, authenticated, service_role to authenticator;
-- auth.uid() as Supabase defines it: the JWT's sub claim (PostgREST 12 sets request.jwt.claims).
create schema if not exists auth;
grant usage on schema auth to anon, authenticated, service_role;
create table if not exists auth.users (id uuid primary key, email text);
create or replace function auth.uid() returns uuid language sql stable as $f$
  select coalesce(nullif(current_setting('request.jwt.claim.sub', true), ''),
                  nullif(current_setting('request.jwt.claims', true), '')::jsonb ->> 'sub')::uuid
$f$;
grant execute on function auth.uid() to anon, authenticated, service_role;
SQL
  psql -q -X -v ON_ERROR_STOP=1 -f "$ROOT/supabase/tests/support/auth_stub.sql" >/dev/null
  for m in "$ROOT"/supabase/migrations/*.sql; do
    psql -q -X -v ON_ERROR_STOP=1 -f "$m" >/dev/null || { echo "migration failed: $m" >&2; exit 1; }
  done
  psql -q -X -v ON_ERROR_STOP=1 -c "grant usage on schema public to anon, authenticated, service_role" >/dev/null
  (cd "$ROOT/web" && npx vite-node scripts/local/seedFromFixtures.ts) > "$RUN/seed.sql"
  psql -q -X -v ON_ERROR_STOP=1 -f "$RUN/seed.sql" >/dev/null
  # Fixture accounts for local tests: parent, student, second guardian, outsider.
  psql -q -X -v ON_ERROR_STOP=1 >/dev/null <<'SQL'
insert into auth.users(id, email) values
  ('00000000-0000-4000-a000-0000000000a1', 'parent@local.test'),
  ('00000000-0000-4000-a000-000000000051', 'student@local.test'),
  ('00000000-0000-4000-a000-0000000000a2', 'guardian2@local.test'),
  ('00000000-0000-4000-a000-000000000099', 'outsider@local.test')
on conflict do nothing;
-- Two obviously fictional, unverified schools so saved-school flows can run. Not research data.
insert into public.institutions(ipeds_name, display_name, state_code, institution_key) values
  ('Local Test University', 'Local Test University', 'TN', 'local-test-university'),
  ('Local Test College', 'Local Test College', 'TN', 'local-test-college')
on conflict do nothing;
-- Fictional verified prices and policies for those two schools, so cost_projection runs on real SQL locally.
insert into public.sources(id, canonical_url, authority) values
  ('5e000000-0000-4000-a000-000000000001', 'https://example.test/local-fixtures', 'institution')
on conflict do nothing;
update public.institutions set source_id = '5e000000-0000-4000-a000-000000000001', verification_status = 'verified',
  level = case institution_key when 'local-test-college' then 'two_year' else 'four_year' end
where institution_key in ('local-test-university', 'local-test-college');
insert into public.institution_costs(institution_id, academic_year, residency, tuition, mandatory_fees, room, board,
  books_supplies, transportation, personal_misc, total_cost_of_attendance, source_id, verification_status, last_verified_at)
select i.id, '2026-27', r.residency, r.tuition, r.fees, r.room, r.board, 1200, 1500, 2300, r.coa,
  '5e000000-0000-4000-a000-000000000001', 'verified', now()
from public.institutions i
join (values ('local-test-university', 'in_state', 11000, 2000, 6000, 5000, 29000),
             ('local-test-university', 'out_of_state', 30000, 2000, 6000, 5000, 48000),
             ('local-test-college', 'not_applicable', 4000, 500, null, null, null)) r(k, residency, tuition, fees, room, board, coa)
  on r.k = i.institution_key;
insert into public.credit_policies(institution_id, policy_kind, academic_year, policy_url, general_limit_credits, source_id, verification_status, last_verified_at)
select id, 'AP', '2026-27', 'https://example.test/ap', 30, '5e000000-0000-4000-a000-000000000001', 'verified', now()
from public.institutions where institution_key = 'local-test-university';
insert into public.transfer_policies(institution_id, academic_year, policy_url, max_transfer_credits, residency_requirement_credits, source_id, verification_status, last_verified_at)
select id, '2026-27', 'https://example.test/transfer', 45, 90, '5e000000-0000-4000-a000-000000000001', 'verified', now()
from public.institutions where institution_key = 'local-test-university';
SQL

  cat > "$RUN/pgrst.conf" <<CONF
db-uri = "postgres://authenticator:authenticator@${PGHOST}:5432/${DB}"
db-schemas = "public"
db-anon-role = "anon"
jwt-secret = "${SECRET}"
server-host = "127.0.0.1"
server-port = $((PORT + 1))
CONF
  "${POSTGREST_BIN:?set POSTGREST_BIN to a PostgREST binary}" "$RUN/pgrst.conf" > "$RUN/pgrst.log" 2>&1 &
  echo $! > "$RUN/pgrst.pid"
  # Supabase clients call <url>/rest/v1/...; strip that prefix in front of PostgREST.
  node "$ROOT/scripts/local/rest_proxy.mjs" "$PORT" "$((PORT + 1))" > "$RUN/proxy.log" 2>&1 &
  echo $! > "$RUN/proxy.pid"
  for _ in $(seq 1 50); do
    curl -fsS "http://127.0.0.1:$PORT/rest/v1/" -o /dev/null 2>/dev/null && { echo "local backend ready at http://127.0.0.1:$PORT (db $DB)"; return 0; }
    sleep 0.2
  done
  echo "PostgREST did not start; see $RUN/pgrst.log" >&2
  exit 1
}

case "${1:-up}" in
  up) up ;;
  down) down ;;
  test)
    up
    (cd "$ROOT/web" && LOCAL_BACKEND_URL="http://127.0.0.1:$PORT" LOCAL_JWT_SECRET="$SECRET" npx vitest run scripts/local/liveSource.local.test.ts)
    ;;
  *) echo "usage: $0 up|down|test" >&2; exit 2 ;;
esac
