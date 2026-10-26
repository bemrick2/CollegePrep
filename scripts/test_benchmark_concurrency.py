"""Two real connections start the same student's progress check at once (#263): one check, one assignment.

Connection A calls start_benchmark and holds its transaction open for 2 seconds; connection B calls it 0.5 s later.
B must wait for A (the per-student lock), then resume A's check: both return the same id, B's call takes at least a
second, and there is exactly one check with one set of assigned items. Committed fixtures need their own database, so
this creates and drops <BENCHMARK_CONCURRENCY_DB, default benchmark_concurrency> using the PG* environment.

  python scripts/test_benchmark_concurrency.py
"""
import os, subprocess, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DB = os.environ.get('BENCHMARK_CONCURRENCY_DB', 'benchmark_concurrency')
SAT = '40000000-0000-0000-0000-000000000001'
SETUP = """
update public.practice_questions set pool = 'assessment' where section = 'math' and status = 'published';
do $$ declare hh uuid; st uuid; inv text;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Concurrency', 'America/Chicago'); st := public.add_student(hh, 'Concurrent');
  inv := public.create_household_invitation(hh, 'student', st);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(inv);
end $$;
"""


def psql(*args, db=DB, check=True):
    r = subprocess.run(['psql', '-X', '-q', '-v', 'ON_ERROR_STOP=1', '-d', db, *args], capture_output=True, text=True)
    if check and r.returncode:
        raise SystemExit(f'psql failed: {r.stderr.strip()}')
    return r


def expect(ok, msg):
    if not ok:
        raise SystemExit(f'FAILED: {msg}')
    print('ok -', msg)


def main():
    psql('-c', f'drop database if exists {DB} with (force)', '-c', f'create database {DB}', db='postgres')
    try:
        psql('-c', "do $$ begin if not exists (select from pg_roles where rolname = 'anon') then create role anon; end if;"
                   " if not exists (select from pg_roles where rolname = 'authenticated') then create role authenticated; end if;"
                   " if not exists (select from pg_roles where rolname = 'service_role') then create role service_role bypassrls; end if; end $$")
        psql('-f', str(ROOT / 'supabase/tests/support/auth_stub.sql'))
        for m in sorted((ROOT / 'supabase/migrations').glob('*.sql')):
            psql('-f', str(m))
        psql('-f', str(ROOT / 'supabase/tests/support/test_helpers.sql'))
        psql('-c', SETUP)
        st = psql('-At', '-c', 'select id from public.students').stdout.strip()
        call = (f"select hp_test.as_user('20000000-0000-0000-0000-000000000051');\n"
                f"select public.start_benchmark('{st}', 'initial', '{SAT}');\n")
        base = ['psql', '-X', '-At', '-v', 'ON_ERROR_STOP=1', '-d', DB, '-c']
        a = subprocess.Popen(base + ['begin;\n' + call + 'select pg_sleep(2);\ncommit;'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        time.sleep(0.5)
        t0 = time.monotonic()
        b = subprocess.run(base + ['begin;\n' + call + 'commit;'], capture_output=True, text=True)
        waited = time.monotonic() - t0
        out_a, err_a = a.communicate(timeout=30)
        ids = lambda out: [l for l in out.splitlines() if len(l) == 36 and l.count('-') == 4]
        expect(a.returncode == 0 and b.returncode == 0, f'both calls succeed {err_a.strip()} {b.stderr.strip()}')
        expect(ids(out_a) == ids(b.stdout) and len(ids(out_a)) == 1, f'both return the same check {ids(out_a)} {ids(b.stdout)}')
        expect(waited >= 1.0, f'the second call waited for the first ({waited:.2f}s)')
        expect(psql('-At', '-c', 'select count(*) from public.practice_benchmarks').stdout.strip() == '1', 'one check')
        expect(psql('-At', '-c', 'select count(*) || \':\' || count(distinct question_id) from public.practice_benchmark_items').stdout.strip()
               == '5:5', 'one assignment (initial plans 9: all 5 reserved math items), no double exposure')
    finally:
        psql('-c', f'drop database if exists {DB} with (force)', db='postgres', check=False)
    print('benchmark concurrency test passed')


if __name__ == '__main__':
    main()
