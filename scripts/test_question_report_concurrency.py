"""Two real connections file question reports for one reporter at once (CR-25): the rate limit and the one-open-report
rule hold under concurrency.

1. Rate limit. The student has 9 reports in the last hour (the limit is 10). Connection A reports one question and holds
   its transaction open for 2 seconds; connection B reports another question 0.5 s later. B must wait for A (the
   per-reporter advisory lock), then see A's report and be refused as rate-limited: 10 reports, never 11.
2. Duplicates. A guardian reports the same attempt from two connections the same way: one report is created, the other
   call returns it (created false) instead of failing or filing a second one.

Committed fixtures need their own database, so this creates and drops <QUESTION_REPORT_CONCURRENCY_DB, default
question_report_concurrency> using the PG* environment.

  python scripts/test_question_report_concurrency.py
"""
import os, subprocess, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DB = os.environ.get('QUESTION_REPORT_CONCURRENCY_DB', 'question_report_concurrency')
STUDENT = '20000000-0000-0000-0000-000000000051'
GUARDIAN = '20000000-0000-0000-0000-0000000000a1'
SETUP = f"""
do $$ declare hh uuid; st uuid; inv text; a uuid;
begin
  perform hp_test.as_user('{GUARDIAN}');
  hh := public.create_household('Reports', 'UTC'); st := public.add_student(hh, 'Reporter');
  inv := public.create_household_invitation(hh, 'student', st);
  perform hp_test.as_user('{STUDENT}');
  perform public.accept_household_invitation(inv);
  a := public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000001'); perform public.submit_practice_attempt(a, 'B');
  a := public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000002'); perform public.submit_practice_attempt(a, '1/2');
  a := public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000003'); perform public.submit_practice_attempt(a, 'C');
  perform hp_test.as_owner();
  insert into public.question_reports(question_id, content_hash, question_pool, student_id, reporter_user_id, reporter_role, reason, created_at)
  select '30000000-0000-0000-0000-000000000004', lpad(to_hex(n), 64, '0'), 'practice', st, '{STUDENT}', 'student', 'typo',
    now() - interval '5 minutes'
  from generate_series(1, 9) n;
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


def race(first, second):
    """Runs first in a transaction held open 2 s, and second 0.5 s later; returns both results and second's wait."""
    base = ['psql', '-X', '-At', '-v', 'ON_ERROR_STOP=1', '-d', DB, '-c']
    a = subprocess.Popen(base + ['begin;\n' + first + 'select pg_sleep(2);\ncommit;'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    time.sleep(0.5)
    t0 = time.monotonic()
    b = subprocess.run(base + ['begin;\n' + second + 'commit;'], capture_output=True, text=True)
    waited = time.monotonic() - t0
    out_a, err_a = a.communicate(timeout=30)
    return (a.returncode, out_a, err_a), (b.returncode, b.stdout, b.stderr), waited


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
        attempt = lambda q: psql('-At', '-c', f"select id from public.practice_attempts where question_id = '30000000-0000-0000-0000-00000000000{q}'").stdout.strip()
        call = lambda uid, att: f"select hp_test.as_user('{uid}');\nselect public.report_question_problem('{att}', 'typo');\n"
        count = lambda uid: psql('-At', '-c', f"select count(*) from public.question_reports where reporter_user_id = '{uid}'").stdout.strip()

        (rc_a, out_a, err_a), (rc_b, out_b, err_b), waited = race(call(STUDENT, attempt(1)), call(STUDENT, attempt(2)))
        expect(rc_a == 0 and '"created": true' in out_a, f'the 10th report is created {err_a.strip()}')
        expect(rc_b != 0 and 'Too many reports' in err_b, f'the concurrent 11th is refused as rate-limited {out_b.strip()} {err_b.strip()[:200]}')
        expect(waited >= 1.0, f'the second call waited for the first ({waited:.2f}s)')
        expect(count(STUDENT) == '10', f'10 reports, not 11 ({count(STUDENT)})')

        (rc_a, out_a, err_a), (rc_b, out_b, err_b), waited = race(call(GUARDIAN, attempt(3)), call(GUARDIAN, attempt(3)))
        expect(rc_a == 0 and '"created": true' in out_a, f'the first identical report is created {err_a.strip()}')
        expect(rc_b == 0 and '"created": false' in out_b, f'the concurrent identical report returns it {out_b.strip()} {err_b.strip()[:200]}')
        expect(waited >= 1.0, f'the second identical call waited for the first ({waited:.2f}s)')
        expect(count(GUARDIAN) == '1', f'one report ({count(GUARDIAN)})')
    finally:
        psql('-c', f'drop database if exists {DB} with (force)', db='postgres', check=False)
    print('question report concurrency test passed')


if __name__ == '__main__':
    main()
