"""End-to-end test of the CR-23 reserve release transaction, on throwaway local databases.

Builds the exact SQL that `scripts/apply_migrations.py --until 20261023010000 --reserve <script>` runs (its
combined_transaction_sql) and runs it with psql against a database holding every migration before the assessment pool
plus fixture questions:
  * a qualifying reserve: the pool migration, the check-assignment migration and the reserve commit together (both
    schema_migrations rows recorded, exactly the listed items marked);
  * a reserve listing one unqualified item: the whole transaction rolls back (no pool column, no assignment table, no
    schema_migrations row, nothing marked).
Uses the PG* environment (CI's database job, or a local socket) and creates/drops its own databases named
<prefix>_ok and <prefix>_bad (RESERVE_RELEASE_DB_PREFIX, default reserve_release). Never touches any other database.

  python scripts/test_reserve_release.py
"""
import hashlib, os, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import apply_migrations as a
from make_reserve_migration import reserve_sql

PREFIX = os.environ.get('RESERVE_RELEASE_DB_PREFIX', 'reserve_release')
SPLIT = '20261022050000'
SCHEMA = [(a.h.MIGRATIONS / '20261022050000_assessment_pool.sql', '20261022050000', 'assessment_pool'),
          (a.h.MIGRATIONS / '20261023010000_benchmark_item_assignment.sql', '20261023010000', 'benchmark_item_assignment')]
Q = lambda n: f'30000000-0000-0000-0000-00000000000{n}'
FIXTURE = """
insert into public.exam_families(key, name) values ('sat', 'SAT');
insert into public.exam_versions(id, exam_family, version_key, name, effective_from, rules) values
 ('40000000-0000-0000-0000-000000000001', 'sat', 'sat_digital_2024', 'Digital SAT', '2024-03-01', '{"sections":[]}');
insert into public.question_types(id, exam_version_id, type_key, name) values
 ('41000000-0000-0000-0000-000000000001', '40000000-0000-0000-0000-000000000001', 'multiple_choice', 'Multiple choice');
insert into public.practice_questions(id, exam_version_id, question_type_id, section, stem, choices, answer_format, accepted_answers,
  expected_time_seconds, status, license, origin)
select ('30000000-0000-0000-0000-00000000000' || n)::uuid, '40000000-0000-0000-0000-000000000001', '41000000-0000-0000-0000-000000000001',
  'math', 'Question ' || n, '["A","B"]', 'choice', '["A"]', 60, 'published', 'original-owned', 'authored'
from generate_series(1, 4) n;
select public.approve_practice_question(('30000000-0000-0000-0000-00000000000' || n)::uuid, 'human: content lead (fixture)') from generate_series(1, 3) n;
select public.approve_practice_question('30000000-0000-0000-0000-000000000004', 'loader checks');
"""


def psql(db, *args, check=True, capture=False):
    r = subprocess.run(['psql', '-X', '-q', '-v', 'ON_ERROR_STOP=1', '-d', db, *args], capture_output=True, text=True)
    if check and r.returncode:
        raise SystemExit(f'psql failed on {db}: {r.stderr.strip()}')
    return r


def scalar(db, sql):
    return psql(db, '-At', '-c', sql).stdout.strip()


def fresh(db):
    psql('postgres', '-c', f'drop database if exists {db} with (force)', '-c', f'create database {db}')
    psql(db, '-c', "do $$ begin if not exists (select from pg_roles where rolname = 'anon') then create role anon; end if;"
                   " if not exists (select from pg_roles where rolname = 'authenticated') then create role authenticated; end if;"
                   " if not exists (select from pg_roles where rolname = 'service_role') then create role service_role bypassrls; end if; end $$")
    psql(db, '-f', str(ROOT / 'supabase/tests/support/auth_stub.sql'))
    psql(db, '-c', 'create schema supabase_migrations; create table supabase_migrations.schema_migrations'
                   '(version text primary key, name text, statements text[])')
    for m in sorted(a.h.MIGRATIONS.glob('*.sql')):
        if m.name[:14] >= SPLIT:
            break
        psql(db, '-f', str(m))
    psql(db, '-c', FIXTURE)


def release(db, items, rehearsal=False, blocks=SCHEMA):
    d = Path(tempfile.mkdtemp())
    reserve = d / 'reserve.sql'; reserve.write_text(reserve_sql('sat_digital_2024', items))
    assert a.check_reserve(reserve) == []
    tx = d / 'tx.sql'; tx.write_text(a.combined_transaction_sql(blocks, reserve, rehearsal=rehearsal))
    r = psql(db, '-f', str(tx), check=False)
    r.sha = hashlib.sha256(reserve.read_bytes()).hexdigest()
    return r


def expect(ok, msg):
    if not ok:
        raise SystemExit(f'FAILED: {msg}')
    print('ok -', msg)


def main():
    good, bad = f'{PREFIX}_ok', f'{PREFIX}_bad'
    try:
        fresh(good)
        # The dry-run rehearsal runs everything and rolls back: eligibility is checked, nothing is kept.
        r = release(good, [(Q(1), 'math'), (Q(2), 'math'), (Q(3), 'math')], rehearsal=True)
        expect(r.returncode == 0, f'the rehearsal passes {r.stderr.strip()}')
        expect(scalar(good, 'select count(*) from supabase_migrations.schema_migrations') == '0'
               and scalar(good, "select to_regclass('public.practice_benchmark_items') is null") == 't', 'the rehearsal kept nothing')
        r = release(good, [(Q(1), 'math'), (Q(4), 'math')], rehearsal=True)
        expect(r.returncode != 0 and 'Reserve refused' in r.stderr, 'a rehearsal with an unqualified item fails')
        r = release(good, [(Q(1), 'math'), (Q(2), 'math'), (Q(3), 'math')])
        expect(r.returncode == 0, f'qualifying reserve and both schema migrations apply in one transaction {r.stderr.strip()}')
        expect(scalar(good, 'select string_agg(version, \',\' order by version) from supabase_migrations.schema_migrations')
               == '20261022050000,20261023010000', 'both migrations recorded')
        expect(scalar(good, "select string_agg(right(id::text, 1), ',' order by id) from public.practice_questions where pool = 'assessment'")
               == '1,2,3', 'exactly the listed items marked')
        expect(scalar(good, 'select script_sha256 from public.practice_reserve_releases') == r.sha, 'the release is recorded with the file sha256')
        r = release(good, [(Q(1), 'math'), (Q(2), 'math'), (Q(3), 'math')], blocks=[])  # the reserve alone, schema now live
        expect(r.returncode != 0 and 'already applied' in r.stderr, 'the same reserve is refused a second time')
        fresh(bad)
        r = release(bad, [(Q(1), 'math'), (Q(4), 'math')])
        expect(r.returncode != 0 and 'Reserve refused' in r.stderr and Q(4) in r.stderr, 'an unqualified item fails the transaction')
        expect(scalar(bad, 'select count(*) from supabase_migrations.schema_migrations') == '0', 'no migration recorded')
        expect(scalar(bad, "select count(*) from information_schema.columns where table_schema = 'public' and table_name = 'practice_questions'"
                           " and column_name = 'pool'") == '0', 'the pool migration rolled back')
        expect(scalar(bad, "select to_regclass('public.practice_benchmark_items') is null") == 't', 'the assignment migration rolled back')
    finally:
        for db in (good, bad):
            psql('postgres', '-c', f'drop database if exists {db} with (force)', check=False)
    print('reserve release tests passed')


if __name__ == '__main__':
    main()
