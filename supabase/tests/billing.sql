-- CR-16 household billing: entitlement from any provider, billing tables server-only, sandbox never grants
-- access. Everything is rolled back. Run with psql -v ON_ERROR_STOP=1.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql

-- Household: g1 (creator, manages billing), g2 (guardian without billing), s1 (linked student), x (outsider).
do $$
declare hh uuid; st uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Billing', 'America/Chicago');
  st := public.add_student(hh, 'Kid');
  perform set_config('t.hh', hh::text, true);
  perform set_config('t.inv_s', public.create_household_invitation(hh, 'student', st), true);
  perform set_config('t.inv_g', public.create_household_invitation(hh, 'guardian', null, 72, array['view_progress']), true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv_s'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform public.accept_household_invitation(current_setting('t.inv_g'));
  perform hp_test.as_owner();
end $$;

-- Billing tables are invisible to clients.
do $$
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.expect_error('select * from public.billing_customers', '42501');
  perform hp_test.expect_error('select * from public.billing_events', '42501');
  perform hp_test.expect_error($q$insert into public.billing_events(provider, event_id, event_type, payload) values ('stripe','evt','x','{}')$q$, '42501');
  perform hp_test.as_anon();
  perform hp_test.expect_error('select public.household_entitlement(gen_random_uuid())', '42501');
  perform hp_test.as_owner();
end $$;

-- No subscription: not active; the billing guardian may buy, the student and the other guardian may not.
do $$
declare e jsonb;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  e := public.household_entitlement(current_setting('t.hh')::uuid);
  perform hp_test.check((e->>'active')::boolean = false and (e->>'can_manage_billing')::boolean, 'no plan yet; owner can buy');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  e := public.household_entitlement(current_setting('t.hh')::uuid);
  perform hp_test.check((e->>'active')::boolean = false and not (e->>'can_manage_billing')::boolean, 'student cannot buy');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error('select public.household_entitlement(current_setting(''t.hh'')::uuid)', '42501');
  perform hp_test.as_owner();
end $$;

-- A sandbox (test-store) purchase never grants production access.
set local role service_role;
insert into public.subscriptions(owner_user_id, household_id, plan_key, status, provider, provider_subscription_id, environment)
values ('20000000-0000-0000-0000-0000000000a1', current_setting('t.hh')::uuid, 'family', 'active', 'apple', 'orig_sandbox', 'sandbox');
reset role;
do $$
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.check(not (public.household_entitlement(current_setting('t.hh')::uuid)->>'active')::boolean, 'sandbox purchase is not access');
  perform hp_test.as_owner();
end $$;

-- Web (Stripe) subscription: every member sees access; only billing members see where it is managed.
set local role service_role;
insert into public.subscriptions(owner_user_id, household_id, plan_key, status, provider, provider_customer_id,
  provider_subscription_id, current_period_end, cancel_at_period_end)
values ('20000000-0000-0000-0000-0000000000a1', current_setting('t.hh')::uuid, 'family', 'active', 'stripe', 'cus_1', 'sub_1', '2026-11-06Z', false);
reset role;
do $$
declare e jsonb;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  e := public.household_entitlement(current_setting('t.hh')::uuid);
  perform hp_test.check((e->>'active')::boolean and e->>'plan_key' = 'family' and e->>'managed_by' = 'web' and (e->>'is_owner')::boolean, 'owner sees web plan');
  perform hp_test.check(not (e ? 'provider_customer_id') and not (e ? 'provider_subscription_id'), 'no provider ids leave the server');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  e := public.household_entitlement(current_setting('t.hh')::uuid);
  perform hp_test.check((e->>'active')::boolean and e->>'managed_by' is null and not (e->>'can_manage_billing')::boolean, 'student has access, no billing details');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  e := public.household_entitlement(current_setting('t.hh')::uuid);
  perform hp_test.check((e->>'active')::boolean and e->>'managed_by' is null, 'guardian without billing flag: access only');
  perform hp_test.as_owner();
end $$;

-- Payment failure keeps access during retries (grace); cancellation ends it; an Apple purchase is equivalent.
set local role service_role;
update public.subscriptions set status = 'past_due' where provider_subscription_id = 'sub_1';
reset role;
do $$
declare e jsonb;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  e := public.household_entitlement(current_setting('t.hh')::uuid);
  perform hp_test.check((e->>'active')::boolean and (e->>'in_grace')::boolean, 'past_due keeps access in grace');
  perform hp_test.as_owner();
end $$;
set local role service_role;
update public.subscriptions set status = 'canceled' where provider_subscription_id = 'sub_1';
insert into public.subscriptions(owner_user_id, household_id, plan_key, status, provider, provider_subscription_id, current_period_end)
values ('20000000-0000-0000-0000-0000000000a1', current_setting('t.hh')::uuid, 'family', 'active', 'apple', 'orig_1', '2026-12-01Z');
reset role;
do $$
declare e jsonb;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  e := public.household_entitlement(current_setting('t.hh')::uuid);
  perform hp_test.check((e->>'active')::boolean and e->>'managed_by' = 'apple', 'an Apple subscription unlocks the same household');
  perform hp_test.as_owner();
end $$;

-- Statuses outside the normalised set are rejected; one event id is stored once.
do $$
begin
  perform hp_test.expect_error($q$update public.subscriptions set status = 'gold' where provider_subscription_id = 'orig_1'$q$, '23514');
  insert into public.billing_events(provider, event_id, event_type, payload) values ('stripe', 'evt_1', 'invoice.paid', '{}');
  perform hp_test.expect_error($q$insert into public.billing_events(provider, event_id, event_type, payload) values ('stripe', 'evt_1', 'invoice.paid', '{}')$q$, '23505');
end $$;

rollback;
