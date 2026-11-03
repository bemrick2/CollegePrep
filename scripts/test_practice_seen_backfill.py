"""The CR-23 part 2 backfill (20261102050000) marks pre-existing session items from exposure before their session started.

Applies every migration before 20261102050000 to its own database, seeds sessions, attempts and a progress-check
assignment there (with timestamps set around each session's start), then applies 20261102050000 and the migrations after
it, and checks practice_session_items.seen_before / last_seen row by row:

  * S1 (started 10 minutes ago) was served before anything: every item is fresh.
  * q1 was answered 8 minutes ago, inside S1; q8 was assigned to a check 7 minutes ago, never attempted.
  * S2 (started 6 minutes ago) is after both: q1 and q8 are seen, with last_seen the answer and the assignment times.
  * Another student's answer (q2, 9 minutes ago) never counts for this student.

Committed fixtures need their own database, so this creates and drops <PRACTICE_SEEN_BACKFILL_DB, default
practice_seen_backfill> using the PG* environment.

  python scripts/test_practice_seen_backfill.py
"""
import os, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DB = os.environ.get('PRACTICE_SEEN_BACKFILL_DB', 'practice_seen_backfill')
CUTOFF = '20261102050000'
SAT = '40000000-0000-0000-0000-000000000001'
SEED = f"""
do $$ declare hh uuid; st uuid; hh2 uuid; st2 uuid; inv text; s1 uuid; s2 uuid; a uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Backfill', 'UTC'); st := public.add_student(hh, 'Backfill');
  inv := public.create_household_invitation(hh, 'student', st);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(inv);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  hh2 := public.create_household('Other', 'UTC'); st2 := public.add_student(hh2, 'Other');
  inv := public.create_household_invitation(hh2, 'student', st2);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.accept_household_invitation(inv);
  perform public.submit_practice_attempt(public.start_practice_attempt(st2, '30000000-0000-0000-0000-000000000002'), '1/2');

  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  s1 := public.start_practice_session(st, 15);
  a := public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000001', s1);
  perform public.submit_practice_attempt(a, 'B');
  perform public.end_practice_session(s1);
  s2 := public.start_practice_session(st, 15);
  perform public.end_practice_session(s2);
  -- A check assigns q8 (the only reserved item); it is never attempted, and returns to practice afterwards.
  perform hp_test.as_owner();
  update public.practice_questions set pool = 'assessment' where id = '30000000-0000-0000-0000-000000000008';
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.start_benchmark(st, 'initial', '{SAT}');
  perform hp_test.as_owner();
  update public.practice_questions set pool = 'practice' where id = '30000000-0000-0000-0000-000000000008';

  update public.practice_sessions set started_at = now() - interval '10 minutes' where id = s1;
  update public.practice_sessions set started_at = now() - interval '6 minutes' where id = s2;
  update public.practice_attempts set presented_at = now() - interval '8 minutes' where id = a;
  update public.practice_attempts set presented_at = now() - interval '9 minutes' where student_id = st2;
  update public.practice_benchmark_items set assigned_at = now() - interval '7 minutes' where student_id = st;
  execute format('create table public.backfill_fixture as select %L::uuid as s1, %L::uuid as s2', s1, s2);
end $$;
"""
CHECK = """
select case i.session_id when f.s1 then 'S1' else 'S2' end || ':q' || right(i.question_id::text, 1) || ':' || i.seen_before || ':' ||
  (case
    when i.last_seen is null then 'never'
    when i.last_seen = (select a.presented_at from public.practice_attempts a join public.students s on s.id = a.student_id
                        where a.question_id = i.question_id and s.linked_user_id = '20000000-0000-0000-0000-000000000051') then 'answer'
    when i.last_seen = (select b.assigned_at from public.practice_benchmark_items b where b.question_id = i.question_id) then 'assignment'
    else 'other' end)
from public.practice_session_items i cross join public.backfill_fixture f
where i.session_id in (f.s1, f.s2) and right(i.question_id::text, 1) in ('1', '2', '8')
order by 1
"""
WANT = ['S1:q1:false:never', 'S1:q2:false:never', 'S1:q8:false:never',
        'S2:q1:true:answer', 'S2:q2:false:never', 'S2:q8:true:assignment']


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
        migrations = sorted((ROOT / 'supabase/migrations').glob('*.sql'))
        before = [m for m in migrations if m.name[:14] < CUTOFF]
        after = [m for m in migrations if m.name[:14] >= CUTOFF]
        expect(after and after[0].name.startswith(CUTOFF), f'{CUTOFF} is in the chain')
        for m in before:
            psql('-f', str(m))
        expect(psql('-At', '-c', "select count(*) from information_schema.columns where table_name = 'practice_session_items' "
                                 "and column_name = 'seen_before'").stdout.strip() == '0', 'seeded before the column exists')
        psql('-f', str(ROOT / 'supabase/tests/support/test_helpers.sql'))
        psql('-c', SEED)
        for m in after:
            psql('-f', str(m))
        got = psql('-At', '-c', CHECK).stdout.split()
        expect(got == WANT, f'backfilled seen_before and last_seen per session item: {got}')
        expect(psql('-At', '-c', 'select count(*) from public.practice_session_items where seen_before <> (last_seen is not null)').stdout.strip() == '0',
               'seen_before agrees with last_seen on every row')
    finally:
        psql('-c', f'drop database if exists {DB} with (force)', db='postgres', check=False)
    print('practice seen backfill test passed')


if __name__ == '__main__':
    main()
