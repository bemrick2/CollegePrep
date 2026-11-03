"""Two real connections race a household deletion against a Stripe webhook event (A4, 20261102070000_data_requests.sql).

The deletion de-identifies the household's payment events and records its provider references; record_billing_event
stores an event about those references already de-identified. Without serialising the two, an event recorded while
the deletion is in progress is invisible to the deletion (not yet committed) and cannot see the deletion's references
(not yet committed), so it would stay raw, with the payer's name and email, forever. Both take the billing advisory
lock (data_request_billing_lock_key: exclusive for a live deletion, shared for record_billing_event).

1. Deletion first: connection A runs the live household deletion and holds its transaction open for 2 seconds; B
   records an invoice.paid for the household's subscription 0.5 s later. B must wait for A, then see the references
   and store the event de-identified.
2. Event first: A records an event for another household's customer and holds its transaction open; B starts that
   household's live deletion 0.5 s later. B must wait for A, then collect and de-identify the event.

Committed fixtures need their own database, so this creates and drops <DATA_REQUEST_CONCURRENCY_DB, default
data_request_concurrency> using the PG* environment.

  python scripts/test_data_request_concurrency.py
"""
import os, subprocess, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DB = os.environ.get('DATA_REQUEST_CONCURRENCY_DB', 'data_request_concurrency')
G1 = '20000000-0000-0000-0000-0000000000a1'
GB = '20000000-0000-0000-0000-0000000000b1'
SETUP = f"""
do $$ declare h1 uuid; h2 uuid;
begin
  perform hp_test.as_user('{G1}'); h1 := public.create_household('Race One', 'America/Chicago');
  perform hp_test.as_user('{GB}'); h2 := public.create_household('Race Two', 'America/Chicago');
  perform hp_test.as_owner();
  insert into public.subscriptions(owner_user_id, household_id, plan_key, status, provider, provider_customer_id, provider_subscription_id) values
   ('{G1}', h1, 'family_annual', 'canceled', 'stripe', 'cus_RACE1', 'sub_RACE1'),
   ('{GB}', h2, 'family_annual', 'canceled', 'stripe', 'cus_RACE2', 'sub_RACE2');
  insert into public.billing_customers(household_id, provider, provider_customer_id) values (h1, 'stripe', 'cus_RACE1'), (h2, 'stripe', 'cus_RACE2');
end $$;
"""


def psql(*args, db=DB, check=True):
    r = subprocess.run(['psql', '-X', '-q', '-v', 'ON_ERROR_STOP=1', '-d', db, *args], capture_output=True, text=True)
    if check and r.returncode:
        raise SystemExit(f'psql failed: {r.stderr.strip()}')
    return r


def one(sql):
    return psql('-At', '-c', sql).stdout.strip()


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


def event(event_id, customer, sub):
    return ("'{\"id\":\"%s\",\"type\":\"invoice.paid\",\"data\":{\"object\":{\"id\":\"in_%s\",\"object\":\"invoice\",\"customer\":\"%s\","
            "\"subscription\":\"%s\",\"amount_paid\":4900,\"customer_email\":\"payer@example.com\",\"customer_name\":\"Pat Payer\"}}}'"
            % (event_id, event_id, customer, sub))


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
        h1 = one("select id from public.households where name = 'Race One'")
        h2 = one("select id from public.households where name = 'Race Two'")
        service = "select set_config('role', 'service_role', false);\n"
        delete = lambda h: service + (f"select public.admin_delete_household('{h}', 'race test', 'owner@example.com', p_dry_run => false, "
                                      f"p_confirm => '{h}', p_operator => 'ci')->>'request_id';")
        record = lambda e, c, s: service + f"select public.record_billing_event('stripe', '{e}', 'invoice.paid', '{s}', {event(e, c, s)}, true);"
        state = lambda e: one(f"select (deidentified_at is not null) || ' ' || (household_id is null) || ' ' || "
                              f"(position('payer@example.com' in payload::text) = 0 and position('Pat Payer' in payload::text) = 0) "
                              f"from public.billing_events where event_id = '{e}'")

        # 1. The webhook records an event while the deletion is in progress.
        (ra, oa, ea), (rb, ob, eb), waited = race(delete(h1), record('evt_RACE1', 'cus_RACE1', 'sub_RACE1'))
        expect(ra == 0 and rb == 0, f'deletion and event both succeed {ea.strip()} {eb.strip()}')
        expect(state('evt_RACE1') == 'true true true', f'the event recorded during the deletion is stored de-identified ({state("evt_RACE1")})')
        expect(waited >= 1.0, f'the event waited for the deletion to commit ({waited:.2f}s)')
        expect(one(f"select count(*) from public.households where id = '{h1}'") == '0', 'the household is deleted')

        # 2. The webhook's event is uncommitted when the deletion starts.
        (ra, oa, ea), (rb, ob, eb), waited = race(record('evt_RACE2', 'cus_RACE2', 'sub_RACE2'), delete(h2))
        expect(ra == 0 and rb == 0, f'event and deletion both succeed {ea.strip()} {eb.strip()}')
        expect(state('evt_RACE2') == 'true true true', f'the deletion collected and de-identified the event ({state("evt_RACE2")})')
        expect(waited >= 1.0, f'the deletion waited for the event to commit ({waited:.2f}s)')
        req = [l for l in ob.splitlines() if len(l) == 36][-1]
        expect(one(f"select kept->>'billing_events' from public.data_request_log where id = '{req}'") == '1', 'the deletion counted the event it kept')
    finally:
        psql('-c', f'drop database if exists {DB} with (force)', db='postgres', check=False)


if __name__ == '__main__':
    main()
