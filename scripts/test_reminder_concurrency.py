"""Two real connections race on practice reminders (CR-27, 20261102030000_practice_reminders.sql).

1. Claim-then-send: two sender runs claim the same reminder at once. Connection A claims and holds its transaction
   open for 2 seconds; B claims the same key 0.5 s later. B must wait for A (the unique index), then lose: one claim
   returns true, the other false, and there is one claimed row. Only the winner sends, so nothing is sent twice.
2. The guardian notice: the student's two devices turn reminders off at once. The second waits for the first (the
   per-student advisory lock) and sees reminders already off, so exactly one change is flagged and guardians get one
   notice each.
3. A device id first reported by two logins at once: the second waits for the first's row, then is refused, and the
   first login's endpoint and keys are untouched.

Committed fixtures need their own database, so this creates and drops <REMINDER_CONCURRENCY_DB, default
reminder_concurrency> using the PG* environment.

  python scripts/test_reminder_concurrency.py
"""
import os, subprocess, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DB = os.environ.get('REMINDER_CONCURRENCY_DB', 'reminder_concurrency')
PARENT = '20000000-0000-0000-0000-0000000000a1'
STUDENT = '20000000-0000-0000-0000-000000000051'
OUTSIDER = '20000000-0000-0000-0000-000000000099'
SETTINGS = ('{"times":["16:30"],"days":[1,2,3,4,5,6,7],"quiet_start":"21:00","quiet_end":"07:00","school_days":[1,2,3,4,5],'
            '"school_start":"08:00","school_end":"15:00","max_per_day":1,"max_per_week":5,"enabled":%s}')
SETUP = f"""
-- The CI auth stub has no email column; Supabase Auth does.
alter table auth.users add column if not exists email text;
update auth.users set email = right(id::text, 2) || '@example.test';
do $$ declare hh uuid; st uuid; inv text;
begin
  perform hp_test.as_user('{PARENT}');
  hh := public.create_household('Concurrency', 'America/Chicago'); st := public.add_student(hh, 'Riley');
  inv := public.create_household_invitation(hh, 'student', st);
  perform hp_test.as_user('{STUDENT}');
  perform public.accept_household_invitation(inv);
  perform public.set_practice_reminders(st, '{SETTINGS % 'true'}');
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
    """Run `first` in a transaction held open 2 s, and `second` 0.5 s later; return both results and B's wait."""
    base = ['psql', '-X', '-q', '-At', '-v', 'ON_ERROR_STOP=1', '-d', DB, '-c']
    a = subprocess.Popen(base + ['begin;\n' + first + '\nselect pg_sleep(2);\ncommit;'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    time.sleep(0.5)
    t0 = time.monotonic()
    b = subprocess.run(base + ['begin;\n' + second + '\ncommit;'], capture_output=True, text=True)
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
        st = psql('-At', '-c', 'select id from public.students').stdout.strip()
        service = "select set_config('role', 'service_role', false);\n"

        # 1. Two sender runs claim one reminder.
        claim = lambda: service + f"select public.claim_practice_reminder(gen_random_uuid(), '{st}', '2026-11-02:16:30', '16:30');"
        (ra, oa, ea), (rb, ob, eb), waited = race(claim(), claim())
        results = [l for l in (oa + ob).splitlines() if l in ('t', 'f')]
        expect(ra == 0 and rb == 0, f'both claims run {ea.strip()} {eb.strip()}')
        expect(sorted(results) == ['f', 't'], f'one claim wins, the other loses {results}')
        expect([l for l in ob.splitlines() if l in ('t', 'f')] == ['f'], 'the second claim is the one that loses')
        expect(waited >= 1.0, f'the second claim waited for the first ({waited:.2f}s)')
        expect(psql('-At', '-c', "select count(*) from public.practice_reminder_deliveries where reminder_key = '2026-11-02:16:30'").stdout.strip() == '1',
               'one claimed row: the reminder is sent once')

        # 2. Two devices of the student turn reminders off at once.
        off = f"select hp_test.as_user('{STUDENT}');\nselect public.set_practice_reminders('{st}', '{SETTINGS % 'false'}')->>'guardians_notified';"
        (ra, oa, ea), (rb, ob, eb), waited = race(off, off)
        expect(ra == 0 and rb == 0, f'both saves succeed {ea.strip()} {eb.strip()}')
        flags = lambda out: [l for l in out.splitlines() if l in ('true', 'false')]
        expect(flags(oa) == ['true'] and flags(ob) == ['false'], f'only the first save tells guardians ({flags(oa)}, {flags(ob)})')
        expect(waited >= 1.0, f'the second save waited for the first ({waited:.2f}s)')
        expect(psql('-At', '-c', 'select count(*) from public.practice_reminder_changes where notify_guardians').stdout.strip() == '1', 'one flagged change')
        expect(psql('-At', '-c', 'set role service_role; select count(*) from public.reminder_opt_out_payload()').stdout.strip().splitlines()[-1] == '1',
               'one notice for the one guardian')

        # 3. One device id reported first by two logins at once.
        dev = '5f000000-0000-4000-a000-0000000000aa'
        rep = lambda uid, ep: (f"select hp_test.as_user('{uid}');\nselect public.report_notification_device('{dev}', 'granted', "
                               f"'{{\"endpoint\":\"https://fcm.googleapis.com/fcm/send/{ep}\",\"keys\":{{\"p256dh\":\"k-{ep}\",\"auth\":\"a-{ep}\"}}}}', 'android');")
        (ra, oa, ea), (rb, ob, eb), waited = race(rep(STUDENT, 'student'), rep(OUTSIDER, 'outsider'))
        expect(ra == 0, f'the first report succeeds {ea.strip()}')
        expect(rb != 0 and 'Not your device' in eb, f'the concurrent second report is refused {eb.strip()[:200]}')
        row = psql('-At', '-c', f"select user_id || ' ' || endpoint || ' ' || p256dh from public.notification_devices where id = '{dev}'").stdout.strip()
        expect(row == f'{STUDENT} https://fcm.googleapis.com/fcm/send/student k-student', f'the first login keeps its endpoint and keys ({row})')
    finally:
        psql('-c', f'drop database if exists {DB} with (force)', db='postgres', check=False)
    print('reminder concurrency test passed')


if __name__ == '__main__':
    main()
