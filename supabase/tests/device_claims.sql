-- Device registrations move only with proof (20261103010000_device_claims.sql): knowing a device id, token or endpoint
-- makes a claim; the device must return the nonce pushed to it. Tested role by role; rolled back. Two-connection races:
-- scripts/test_reminder_concurrency.py.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql
\ir support/counted_helpers.sql
\ir support/household_roles.sql

-- Devices: the student's browser (endpoint E) and family tablet (FCM token TK); student 2's browser (endpoint E2).
create function hp_test.web(p_endpoint text) returns jsonb language sql immutable as $$
  select jsonb_build_object('endpoint', p_endpoint, 'keys', jsonb_build_object('p256dh', 'key-' || md5(p_endpoint), 'auth', 'auth-' || md5(p_endpoint)))
$$;
-- The nonce the sender would push for p_claimant's newest claim (service role, as the edge function).
create function hp_test.nonce_for(p_claimant uuid) returns text language plpgsql as $$
declare v text;
begin
  perform hp_test.as_service();
  select p->>'nonce' into v from public.issue_device_claim_challenges(p_claimant) p;
  return v;
end $$;
grant execute on all functions in schema hp_test to anon, authenticated, service_role;
do $$
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000e1', 'granted', hp_test.web('https://fcm.googleapis.com/fcm/send/E'), 'android');
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000a1', 'granted', null, 'android', 'fcm', 'fcm-token-family-tablet-TK');
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000d0', 'denied', null, 'ios');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000e2', 'granted', hp_test.web('https://web.push.apple.com/E2'), 'desktop');
  perform hp_test.as_owner();
end $$;

-- 1. Knowing a device id, token or endpoint moves nothing: every role gets at most a claim.
do $$
declare r record; v text; n bigint;
begin
  for r in select * from t_roles where who <> 'STUDENT' loop
    perform hp_test.as_user(r.uid);
    v := public.report_notification_device('6d000000-0000-4000-a000-0000000000e1', 'denied', null, 'desktop');
    perform hp_test.ok(v in ('verification_pending', 'verification_limited'), r.who || ': a report of the student''s device id is only a claim (' || v || ')');
    perform public.report_notification_device(gen_random_uuid(), 'granted', hp_test.web('https://fcm.googleapis.com/fcm/send/E'), 'desktop');
    perform public.report_notification_device(gen_random_uuid(), 'granted', null, 'ios', 'fcm', 'fcm-token-family-tablet-TK');
  end loop;
  perform hp_test.as_owner();
  perform hp_test.is((select string_agg(id::text || ' ' || user_id::text || ' ' || coalesce(endpoint, push_token, permission), ',' order by id) from public.notification_devices
    where user_id = '20000000-0000-0000-0000-000000000051'),
    '6d000000-0000-4000-a000-0000000000a1 20000000-0000-0000-0000-000000000051 fcm-token-family-tablet-TK,'
    || '6d000000-0000-4000-a000-0000000000d0 20000000-0000-0000-0000-000000000051 denied,'
    || '6d000000-0000-4000-a000-0000000000e1 20000000-0000-0000-0000-000000000051 https://fcm.googleapis.com/fcm/send/E', 'the student''s devices are unchanged');
  perform hp_test.ok(not exists (select 1 from public.notification_devices where endpoint = 'https://fcm.googleapis.com/fcm/send/E' or push_token = 'fcm-token-family-tablet-TK'
    group by coalesce(endpoint, push_token) having count(*) > 1), 'nobody else holds the endpoint or token');
  select count(*) into n from public.notification_device_claims where status = 'pending';
  perform hp_test.ok(n > 0, 'the reports made pending claims (' || n || ')');
  perform hp_test.ok(not exists (select 1 from public.notification_device_claims where nonce_hash is not null), 'no nonce before a challenge is issued');
  -- At most 3 pending claims per device: the rest of the roles were limited, not queued.
  perform hp_test.ok((select max(k) from (select count(*) k from public.notification_device_claims where status = 'pending' group by target_device_id) x) <= 3,
    'at most three pending claims per device');
  -- A device id without push credentials can't be verified: held.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.is(public.report_notification_device('6d000000-0000-4000-a000-0000000000d0', 'granted', hp_test.web('https://fcm.googleapis.com/fcm/send/viewer'), 'desktop'),
    'device_held', 'a device with no push target is held');
  perform hp_test.as_owner();
  perform hp_test.is((select user_id from public.notification_devices where id = '6d000000-0000-4000-a000-0000000000d0'), '20000000-0000-0000-0000-000000000051'::uuid, 'and stays the student''s');
  perform hp_test.ok(not exists (select 1 from public.notification_devices where endpoint = 'https://fcm.googleapis.com/fcm/send/viewer'), 'nothing registered for the viewer');
  delete from public.notification_device_claims;
end $$;

-- 2. The challenge: issued once, to the HELD device's push target; only the hash is stored. A view-only guardian's
--    claim is answered by the student's device, which declines it.
do $$
declare c jsonb; v_nonce text; n bigint;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.is(public.report_notification_device('6d000000-0000-4000-a000-0000000000e1', 'granted', hp_test.web('https://fcm.googleapis.com/fcm/send/E'), 'desktop'),
    'verification_pending', 'the viewer, with the student''s endpoint, gets a claim');
  perform hp_test.is(public.report_notification_device('6d000000-0000-4000-a000-0000000000e1', 'denied', null, 'desktop'), 'verification_pending', 'reporting again keeps one claim');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.notification_device_claims where status = 'pending'), 1::bigint, 'one pending claim');
  perform hp_test.as_service();
  select p into c from public.issue_device_claim_challenges('20000000-0000-0000-0000-0000000000b1') p;
  v_nonce := c->>'nonce';
  perform hp_test.ok(v_nonce ~ '^[0-9a-f]{64}$', 'a 256-bit nonce');
  perform hp_test.is(c->'device'->>'endpoint', 'https://fcm.googleapis.com/fcm/send/E', 'pushed to the held device''s own endpoint');
  perform hp_test.is(c->'device'->>'p256dh', 'key-' || md5('https://fcm.googleapis.com/fcm/send/E'), 'with the held device''s keys');
  perform hp_test.is((select count(*) from public.issue_device_claim_challenges('20000000-0000-0000-0000-0000000000b1')), 0::bigint, 'issued once');
  perform hp_test.as_owner();
  perform hp_test.ok((select nonce_hash = sha256(convert_to(v_nonce, 'UTF8')) and issued_at is not null from public.notification_device_claims where status = 'pending'),
    'only the nonce''s SHA-256 is stored');
  perform hp_test.ok(not exists (select 1 from public.notification_device_claims x where x::text like '%' || v_nonce || '%'), 'the nonce itself is nowhere in the claim');
  -- The student's device receives the push and returns the nonce under the student's own login: declined.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.is(public.confirm_device_claim(v_nonce), 'declined', 'the owner''s device declines the claim');
  -- The nonce is spent: nobody, the viewer included, can use it afterwards.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.is(public.confirm_device_claim(v_nonce), 'invalid', 'a declined nonce moves nothing');
  perform hp_test.as_owner();
  perform hp_test.is((select user_id from public.notification_devices where id = '6d000000-0000-4000-a000-0000000000e1'), '20000000-0000-0000-0000-000000000051'::uuid,
    'a view-only guardian never moves the student''s device');
  -- Someone else presenting a live nonce: refused, counted, and the claim stays for its claimant.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000e1', 'denied', null, 'desktop');
  v_nonce := hp_test.nonce_for('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000d1');
  perform hp_test.is(public.confirm_device_claim(v_nonce), 'invalid', 'another login''s nonce is refused');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.notification_device_claim_failures where user_id = '20000000-0000-0000-0000-0000000000d1'), 1::bigint, 'and counted');
  perform hp_test.is((select user_id from public.notification_devices where id = '6d000000-0000-4000-a000-0000000000e1'), '20000000-0000-0000-0000-000000000051'::uuid, 'nothing moved');
  delete from public.notification_device_claims;
  delete from public.notification_device_claim_failures;
end $$;

-- 3. A shared tablet: the student never signed out; a new login reports the tablet's install. The tablet receives the
--    push and returns the nonce under the new login: the registration moves, and the student's reminders stop there.
do $$
declare v_nonce text; c jsonb;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform hp_test.is(public.report_notification_device('6d000000-0000-4000-a000-0000000000a1', 'granted', null, 'android', 'fcm', 'fcm-token-family-tablet-TK'),
    'verification_pending', 'the new login''s report waits for the tablet');
  perform hp_test.as_service();
  select p into c from public.issue_device_claim_challenges('20000000-0000-0000-0000-000000000053') p;
  v_nonce := c->>'nonce';
  perform hp_test.is(c->'device'->>'token', 'fcm-token-family-tablet-TK', 'pushed to the tablet''s token');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform hp_test.is(public.confirm_device_claim('0000000000000000000000000000000000000000000000000000000000000000'), 'invalid', 'a wrong nonce is refused');
  perform hp_test.as_owner();
  perform hp_test.is((select user_id from public.notification_devices where id = '6d000000-0000-4000-a000-0000000000a1'), '20000000-0000-0000-0000-000000000051'::uuid,
    'a wrong nonce moves nothing');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform hp_test.is(public.confirm_device_claim(v_nonce), 'confirmed', 'the right nonce, from the claimant');
  perform hp_test.as_owner();
  perform hp_test.is((select user_id::text || ' ' || push_token from public.notification_devices where id = '6d000000-0000-4000-a000-0000000000a1'),
    '20000000-0000-0000-0000-000000000053 fcm-token-family-tablet-TK', 'the tablet is the new login''s');
  perform hp_test.is((select status from public.notification_device_claims where claimant_user_id = '20000000-0000-0000-0000-000000000053'), null::text,
    'the confirmed claim went with the old registration');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform hp_test.is(public.confirm_device_claim(v_nonce), 'invalid', 'a nonce works once');
  perform hp_test.is(public.report_notification_device('6d000000-0000-4000-a000-0000000000a1', 'granted', null, 'android', 'fcm', 'fcm-token-family-tablet-TK'),
    'registered', 'the tablet now reports as the new login''s own');
  perform hp_test.as_owner();
  perform hp_test.ok(not exists (select 1 from public.notification_devices where push_token = 'fcm-token-family-tablet-TK'
    and user_id = '20000000-0000-0000-0000-000000000051'), 'the student no longer holds the tablet');
end $$;

-- 4. Two held rows: proof is needed for each. The claimant's report of the student's browser id with student 2's
--    endpoint makes two claims; one confirmation is not enough.
do $$
declare v1 text; v2 text; c record;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.is(public.report_notification_device('6d000000-0000-4000-a000-0000000000e1', 'granted', hp_test.web('https://web.push.apple.com/E2'), 'desktop'),
    'verification_pending', 'two held rows, two claims');
  perform hp_test.as_service();
  for c in select p from public.issue_device_claim_challenges('20000000-0000-0000-0000-0000000000a2') p loop
    if c.p->'device'->>'id' = '6d000000-0000-4000-a000-0000000000e1' then v1 := c.p->>'nonce'; else v2 := c.p->>'nonce'; end if;
  end loop;
  perform hp_test.ok(v1 is not null and v2 is not null and v1 <> v2, 'one nonce per held device');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.is(public.confirm_device_claim(v1), 'verification_pending', 'one proof: the other row still blocks the report');
  perform hp_test.as_owner();
  perform hp_test.ok(not exists (select 1 from public.notification_devices where id = '6d000000-0000-4000-a000-0000000000e1'), 'the proven row is released');
  perform hp_test.is((select user_id from public.notification_devices where endpoint = 'https://web.push.apple.com/E2'), '20000000-0000-0000-0000-000000000052'::uuid,
    'the unproven row stays');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.is(public.confirm_device_claim(v2), 'confirmed', 'both proven');
  perform hp_test.as_owner();
  perform hp_test.is((select user_id::text || ' ' || endpoint from public.notification_devices where id = '6d000000-0000-4000-a000-0000000000e1'),
    '20000000-0000-0000-0000-0000000000a2 https://web.push.apple.com/E2', 'the report is applied');
  perform hp_test.is((select count(*) from public.notification_devices where endpoint = 'https://web.push.apple.com/E2'), 1::bigint, 'one row holds the endpoint');
end $$;

-- 5. Expiry and attempt limits.
do $$
declare v_nonce text; i integer; v text;
begin
  -- An issued nonce that expired.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000f1', 'granted', hp_test.web('https://fcm.googleapis.com/fcm/send/F'), 'android');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000f1', 'granted', hp_test.web('https://fcm.googleapis.com/fcm/send/F'), 'desktop');
  v_nonce := hp_test.nonce_for('20000000-0000-0000-0000-000000000052');
  perform hp_test.as_owner();
  perform hp_test.ok((select expires_at <= created_at + interval '10 minutes' from public.notification_device_claims where status = 'pending'), 'claims expire within 10 minutes');
  update public.notification_device_claims set created_at = now() - interval '11 minutes', expires_at = now() - interval '1 minute' where status = 'pending';
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.is(public.confirm_device_claim(v_nonce), 'expired', 'an expired nonce is refused');
  perform hp_test.as_owner();
  perform hp_test.is((select user_id from public.notification_devices where id = '6d000000-0000-4000-a000-0000000000f1'), '20000000-0000-0000-0000-000000000051'::uuid,
    'and moves nothing');
  -- A claim that expired before its challenge was issued is closed by the sender, never challenged.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000f1', 'denied', null, 'desktop');
  perform hp_test.as_owner();
  update public.notification_device_claims set created_at = now() - interval '11 minutes', expires_at = now() - interval '1 minute' where status = 'pending';
  perform hp_test.as_service();
  perform hp_test.is((select count(*) from public.issue_device_claim_challenges(null)), 0::bigint, 'no challenge for an expired claim');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.notification_device_claims where status = 'pending'), 0::bigint, 'it is closed as expired');
  -- Five invalid attempts in an hour lock the caller out, even with a right nonce.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000f1', 'denied', null, 'desktop');
  v_nonce := hp_test.nonce_for('20000000-0000-0000-0000-000000000099');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.is(public.confirm_device_claim(null), 'invalid', 'no nonce');
  perform hp_test.is(public.confirm_device_claim('short'), 'invalid', 'too short');
  for i in 1..3 loop
    perform hp_test.is(public.confirm_device_claim(md5(i::text) || md5(i::text)), 'invalid', 'wrong nonce ' || i);
  end loop;
  perform hp_test.is(public.confirm_device_claim(v_nonce), 'locked', 'after five invalid attempts, locked');
  perform hp_test.as_owner();
  perform hp_test.is((select user_id from public.notification_devices where id = '6d000000-0000-4000-a000-0000000000f1'), '20000000-0000-0000-0000-000000000051'::uuid,
    'a locked caller moves nothing');
  delete from public.notification_device_claim_failures;
  -- At most 5 claims per caller per hour.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  for i in 1..6 loop
    perform hp_test.as_owner();
    insert into public.notification_devices(id, user_id, permission, channel, endpoint, p256dh, auth_secret)
    values (('6d000000-0000-4000-a000-00000000010' || i)::uuid, '20000000-0000-0000-0000-000000000052', 'granted', 'webpush',
      'https://fcm.googleapis.com/fcm/send/many' || i, 'k', 'a');
    perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
    v := public.report_notification_device(('6d000000-0000-4000-a000-00000000010' || i)::uuid, 'denied', null, 'desktop');
  end loop;
  perform hp_test.is(v, 'verification_limited', 'the sixth claim in an hour is refused');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.notification_device_claims where claimant_user_id = '20000000-0000-0000-0000-000000000099'
    and created_at > now() - interval '1 hour'), 5::bigint, 'five claims recorded');
end $$;

-- 6. Unregister on sign-out: the owner only; the next login on that device registers without a challenge.
do $$
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000f1', 'denied', null, 'desktop');
  perform hp_test.as_owner();
  perform hp_test.ok(exists (select 1 from public.notification_device_claims where target_device_id = '6d000000-0000-4000-a000-0000000000f1' and status = 'pending'),
    'a pending claim on the device');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.is(public.unregister_notification_device('6d000000-0000-4000-a000-0000000000f1'), false, 'another login can''t unregister it');
  perform hp_test.as_anon();
  perform hp_test.err($q$select public.unregister_notification_device('6d000000-0000-4000-a000-0000000000f1')$q$, '42501');
  perform hp_test.as_owner();
  perform hp_test.ok(exists (select 1 from public.notification_devices where id = '6d000000-0000-4000-a000-0000000000f1'), 'still registered');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.is(public.unregister_notification_device('6d000000-0000-4000-a000-0000000000f1'), true, 'the owner unregisters on sign-out');
  perform hp_test.is(public.unregister_notification_device('6d000000-0000-4000-a000-0000000000f1'), false, 'twice is a no-op');
  perform hp_test.is(public.unregister_notification_device(null), false, 'no id, no-op');
  perform hp_test.as_owner();
  perform hp_test.ok(not exists (select 1 from public.notification_devices where id = '6d000000-0000-4000-a000-0000000000f1'), 'gone at once');
  perform hp_test.ok(not exists (select 1 from public.notification_device_claims where target_device_id = '6d000000-0000-4000-a000-0000000000f1'), 'its claims went with it');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.is(public.report_notification_device('6d000000-0000-4000-a000-0000000000f1', 'granted', hp_test.web('https://fcm.googleapis.com/fcm/send/F'), 'desktop'),
    'registered', 'the next login on the device registers without a challenge');
  perform hp_test.as_owner();
end $$;

-- 7. Privileges: claims are server-only; the challenge is service-only; no anon grants.
do $$
declare r record;
begin
  for r in select * from t_roles loop
    perform hp_test.as_user(r.uid);
    perform hp_test.err('select id from public.notification_device_claims', '42501');
    perform hp_test.err('select id from public.notification_device_claim_failures', '42501');
    perform hp_test.err('select * from public.issue_device_claim_challenges(null)', '42501');
    perform hp_test.err($q$delete from public.notification_device_claims$q$, '42501');
  end loop;
  perform hp_test.as_anon();
  perform hp_test.err($q$select public.confirm_device_claim('x')$q$, '42501');
  perform hp_test.err($q$select public.report_notification_device(gen_random_uuid(), 'denied')$q$, '42501');
  perform hp_test.err('select * from public.issue_device_claim_challenges(null)', '42501');
  perform hp_test.as_owner();
  perform hp_test.ok((select bool_and(relrowsecurity) from pg_class where oid in ('public.notification_device_claims'::regclass,
    'public.notification_device_claim_failures'::regclass)), 'RLS on both tables');
  perform hp_test.ok(not exists (select 1 from pg_proc p where p.pronamespace = 'public'::regnamespace and p.prosecdef
    and p.proname in ('report_notification_device', 'confirm_device_claim', 'unregister_notification_device', 'issue_device_claim_challenges')
    and not coalesce(p.proconfig @> array['search_path=""'], false)), 'every security definer function pins an empty search_path');
  perform hp_test.ok(not has_function_privilege('authenticated', 'public.notification_device_register_internal(uuid, uuid, text, text, text, text, text, text, text)', 'execute')
    and not has_function_privilege('authenticated', 'public.notification_device_conflicts_internal(uuid, uuid, text, text)', 'execute')
    and not has_function_privilege('authenticated', 'public.device_nonce_hash(text)', 'execute'), 'internal helpers are not client-callable');
end $$;

\o
select format('device_claims: all %s assertions passed', last_value) from hp_test.assertions \gset
\echo :format
rollback;
