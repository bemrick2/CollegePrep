"""Two real connections race on practice reminders (CR-27, 20261102030000_practice_reminders.sql).

1. Claim-then-send: two sender runs claim the same reminder at once. Connection A claims and holds its transaction
   open for 2 seconds; B claims the same key 0.5 s later. B must wait for A (the unique index), then lose: one claim
   returns true, the other false, and there is one claimed row. Only the winner sends, so nothing is sent twice.
2. The guardian notice: the student's two devices turn reminders off at once. The second waits for the first (the
   per-student advisory lock) and sees reminders already off, so exactly one change is flagged and guardians get one
   notice each.
3. Knowing a device is not enough (20261103010000_device_claims.sql): a login that registered a browser holds its
   transaction open while another login reports the same device id and endpoint. The second waits (the advisory lock
   on the device id), then sees the first login's row: it gets 'verification_pending' and nothing moves.
4. The same for an FCM token reported under another device id (the lock on the token).
5. The same for a web endpoint reported under another device id (the lock on the endpoint). Without that lock the
   second report wouldn't see the first row and both logins would hold the endpoint.
6. Two confirmations of one nonce at once: the first moves the device, the second waits (the claim row lock), then
   gets 'invalid'. The device moves once.

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

        # 3-5. Two logins report one browser or install at once: the second waits, then only makes a claim.
        rep = lambda dev, uid, ep, key: (f"select hp_test.as_user('{uid}');\nselect public.report_notification_device('{dev}', 'granted', "
                                         f"'{{\"endpoint\":\"https://fcm.googleapis.com/fcm/send/{ep}\",\"keys\":{{\"p256dh\":\"k-{key}\",\"auth\":\"a-{key}\"}}}}', 'android');")
        fcm = lambda dev, uid, tok: (f"select hp_test.as_user('{uid}');\nselect public.report_notification_device('{dev}', 'granted', null, 'ios', 'fcm', '{tok}');")
        row_of = lambda where: psql('-At', '-c', f"select count(*) || ' ' || coalesce(string_agg(id || ' ' || user_id || ' ' || coalesce(endpoint, push_token) || ' ' || coalesce(p256dh, '-'), ';'), '') "
                                                 f"from public.notification_devices where {where}").stdout.strip()
        statuses = lambda out: [l for l in out.splitlines() if l in ('registered', 'verification_pending', 'verification_limited', 'device_held', 'confirmed', 'invalid', 'expired', 'declined', 'locked')]
        cases = [
            ('same device id and endpoint', rep('5f000000-0000-4000-a000-0000000000aa', STUDENT, 'shared', 'student'),
             rep('5f000000-0000-4000-a000-0000000000aa', OUTSIDER, 'shared', 'outsider'),
             "endpoint = 'https://fcm.googleapis.com/fcm/send/shared'",
             f'1 5f000000-0000-4000-a000-0000000000aa {STUDENT} https://fcm.googleapis.com/fcm/send/shared k-student'),
            ('same FCM token, another device id', fcm('5f000000-0000-4000-a000-0000000000b1', STUDENT, 'fcm-registration-token-shared-0001'),
             fcm('5f000000-0000-4000-a000-0000000000b2', OUTSIDER, 'fcm-registration-token-shared-0001'),
             "push_token = 'fcm-registration-token-shared-0001'",
             f'1 5f000000-0000-4000-a000-0000000000b1 {STUDENT} fcm-registration-token-shared-0001 -'),
            ('same web endpoint, another device id', rep('5f000000-0000-4000-a000-0000000000c1', STUDENT, 'browser', 'student'),
             rep('5f000000-0000-4000-a000-0000000000c2', OUTSIDER, 'browser', 'outsider'),
             "endpoint = 'https://fcm.googleapis.com/fcm/send/browser'",
             f'1 5f000000-0000-4000-a000-0000000000c1 {STUDENT} https://fcm.googleapis.com/fcm/send/browser k-student'),
        ]
        for name, first, second, where, want in cases:
            (ra, oa, ea), (rb, ob, eb), waited = race(first, second)
            expect(ra == 0 and rb == 0, f'{name}: both reports run {ea.strip()} {eb.strip()[:200]}')
            expect(statuses(oa) == ['registered'] and statuses(ob) == ['verification_pending'],
                   f'{name}: the first registers, the second only claims ({statuses(oa)}, {statuses(ob)})')
            expect(waited >= 1.0, f'{name}: the second report waited for the first ({waited:.2f}s)')
            row = row_of(where)
            expect(row == want, f'{name}: one row, the first login\'s, its keys unchanged ({row})')

        # 6. Two confirmations of one nonce at once.
        nonce = psql('-At', '-c', f"set role service_role; select p->>'nonce' from public.issue_device_claim_challenges('{OUTSIDER}') p "
                                  f"where p->'device'->>'id' = '5f000000-0000-4000-a000-0000000000aa'").stdout.strip().splitlines()[-1]
        expect(len(nonce) == 64, 'the sender gets the nonce once')
        conf = f"select hp_test.as_user('{OUTSIDER}');\nselect public.confirm_device_claim('{nonce}');"
        (ra, oa, ea), (rb, ob, eb), waited = race(conf, conf)
        expect(ra == 0 and rb == 0, f'both confirmations run {ea.strip()} {eb.strip()[:200]}')
        expect(statuses(oa) == ['confirmed'] and statuses(ob) == ['invalid'], f'one nonce moves the device once ({statuses(oa)}, {statuses(ob)})')
        expect(waited >= 1.0, f'the second confirmation waited for the first ({waited:.2f}s)')
        row = row_of("id = '5f000000-0000-4000-a000-0000000000aa'")
        expect(row == f'1 5f000000-0000-4000-a000-0000000000aa {OUTSIDER} https://fcm.googleapis.com/fcm/send/shared k-outsider',
               f'the device is the claimant\'s, with the claimant\'s keys ({row})')
    finally:
        psql('-c', f'drop database if exists {DB} with (force)', db='postgres', check=False)
    print('reminder concurrency test passed')


if __name__ == '__main__':
    main()
