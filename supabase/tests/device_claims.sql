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
-- A subscription for p_endpoint with someone's own keys (a different browser, or a forged report).
create function hp_test.web_keys(p_endpoint text, p_who text) returns jsonb language sql immutable as $$
  select jsonb_build_object('endpoint', p_endpoint, 'keys', jsonb_build_object('p256dh', 'key-' || p_who, 'auth', 'auth-' || p_who))
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
    perform hp_test.ok(v in ('verification_pending', 'verification_limited', 'device_held'), r.who || ': a report of the student''s device id moves nothing (' || v || ')');
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
  perform hp_test.is(public.report_notification_device('6d000000-0000-4000-a000-0000000000e1', 'denied', null, 'desktop'), 'device_held',
    'without keys of its own, a claim on a browser can''t be verified: held');
  perform hp_test.is(public.report_notification_device('6d000000-0000-4000-a000-0000000000e1', 'granted', hp_test.web_keys('https://fcm.googleapis.com/fcm/send/E', 'viewer'), 'desktop'),
    'verification_pending', 'the viewer, with the student''s endpoint and the viewer''s own keys, gets a claim');
  perform hp_test.is(public.report_notification_device('6d000000-0000-4000-a000-0000000000e1', 'granted', hp_test.web_keys('https://fcm.googleapis.com/fcm/send/E', 'viewer'), 'desktop'),
    'verification_pending', 'reporting again keeps one claim');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.notification_device_claims where status = 'pending'), 1::bigint, 'one pending claim');
  perform hp_test.as_service();
  select p into c from public.issue_device_claim_challenges('20000000-0000-0000-0000-0000000000b1') p;
  v_nonce := c->>'nonce';
  perform hp_test.ok(v_nonce ~ '^[0-9a-f]{64}$', 'a 256-bit nonce');
  -- The push goes to the student's endpoint, which only the student's browser receives, encrypted to the viewer's keys,
  -- which that browser can't decrypt: nobody reads it (the edge function test shows the encryption side).
  perform hp_test.is(c->'device'->>'endpoint', 'https://fcm.googleapis.com/fcm/send/E', 'pushed to the held endpoint, never to the claimant');
  perform hp_test.is(c->'device'->>'p256dh' || ' ' || (c->'device'->>'auth'), 'key-viewer auth-viewer', 'encrypted to the claimant''s presented keys');
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
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000e1', 'granted', hp_test.web_keys('https://fcm.googleapis.com/fcm/send/E', 'viewer'), 'desktop');
  perform hp_test.as_owner();
  update public.notification_device_claims set issued_at = issued_at - interval '61 minutes' where issued_at is not null;  -- an hour later
  v_nonce := hp_test.nonce_for('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000d1');
  perform hp_test.is(public.confirm_device_claim(v_nonce), 'invalid', 'another login''s nonce is refused');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.notification_device_claim_failures where user_id = '20000000-0000-0000-0000-0000000000d1'), 0::bigint,
    'but not counted: a live claim of another login builds no lockout');
  perform hp_test.is((select count(*) from public.notification_device_claims where claimant_user_id = '20000000-0000-0000-0000-0000000000b1' and status = 'pending'),
    1::bigint, 'and the claim stays for its claimant');
  perform hp_test.ok((select bool_and(endpoint is null and p256dh is null and auth_secret is null and push_token is null)
    from public.notification_device_claims where status <> 'pending'), 'a resolved claim keeps none of the claimant''s push credentials');
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
  perform hp_test.is((select count(*) from public.notification_device_claim_failures where user_id = '20000000-0000-0000-0000-000000000052'), 1::bigint,
    'and counted');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.is(public.confirm_device_claim(v_nonce), 'invalid', 'an expired nonce stays dead');
  perform hp_test.as_owner();
  perform hp_test.is((select user_id from public.notification_devices where id = '6d000000-0000-4000-a000-0000000000f1'), '20000000-0000-0000-0000-000000000051'::uuid,
    'and moves nothing');
  -- A claim that expired before its challenge was issued is closed by the sender, never challenged.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000f1', 'granted', hp_test.web('https://fcm.googleapis.com/fcm/send/F'), 'desktop');
  perform hp_test.as_owner();
  update public.notification_device_claims set created_at = now() - interval '11 minutes', expires_at = now() - interval '1 minute' where status = 'pending';
  perform hp_test.as_service();
  perform hp_test.is((select count(*) from public.issue_device_claim_challenges(null)), 0::bigint, 'no challenge for an expired claim');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.notification_device_claims where status = 'pending'), 0::bigint, 'it is closed as expired');
  -- Five invalid attempts in an hour lock the caller out, even with a right nonce.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000f1', 'granted', hp_test.web_keys('https://fcm.googleapis.com/fcm/send/F', 'outsider'), 'desktop');
  v_nonce := hp_test.nonce_for('20000000-0000-0000-0000-000000000099');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  -- Not a code at all: refused with 22023, uncounted.
  perform hp_test.err('select public.confirm_device_claim(null)', '22023');
  perform hp_test.err($q$select public.confirm_device_claim('short')$q$, '22023');
  perform hp_test.err(format('select public.confirm_device_claim(%L)', upper(v_nonce)), '22023');
  perform hp_test.err(format('select public.confirm_device_claim(%L)', v_nonce || 'a'), '22023');
  perform hp_test.err(format('select public.confirm_device_claim(%L)', repeat('a', 100000)), '22023');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.notification_device_claim_failures where user_id = '20000000-0000-0000-0000-000000000099'), 0::bigint,
    'malformed codes are not counted');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  for i in 1..5 loop
    perform hp_test.is(public.confirm_device_claim(md5(i::text) || md5(i::text)), 'invalid', 'unknown nonce ' || i);
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
    v := public.report_notification_device(('6d000000-0000-4000-a000-00000000010' || i)::uuid, 'granted',
      hp_test.web_keys('https://fcm.googleapis.com/fcm/send/many' || i, 'outsider'), 'desktop');
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
  perform public.report_notification_device('6d000000-0000-4000-a000-0000000000f1', 'granted', hp_test.web_keys('https://fcm.googleapis.com/fcm/send/F', 'student2'), 'desktop');
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
    perform hp_test.err('select public.purge_device_claims(now())', '42501');
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

-- 8. Endpoint squatting. While the student is signed out of a browser, a squatter registers that browser's endpoint
--    with fake keys. The student's browser reports its real subscription: the challenge goes to the endpoint encrypted
--    to the REAL keys the student presents, so the student reclaims it. The squatter, presenting fake keys, gets a
--    challenge nobody can read; and presenting its own keys for the student's endpoint never sends anything to the
--    squatter's device.
do $$
declare g uuid := '6d000000-0000-4000-a000-0000000000c9'; eg text := 'https://web.push.apple.com/G'; c jsonb; v_nonce text;
begin
  perform hp_test.as_owner();
  delete from public.notification_device_claim_failures;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.report_notification_device(g, 'granted', hp_test.web_keys(eg, 'real'), 'desktop');
  perform public.unregister_notification_device(g);  -- signed out
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.is(public.report_notification_device(gen_random_uuid(), 'granted', hp_test.web_keys(eg, 'squatter'), 'desktop'), 'registered',
    'a squatter can register a free endpoint with fake keys');
  -- The squatter's own claim on it (from another id) would be encrypted to the squatter's keys, and sent to the endpoint.
  -- The student's browser reports its real subscription on sign-in: a claim on the squatter's row.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.is(public.report_notification_device(g, 'granted', hp_test.web_keys(eg, 'real'), 'desktop'), 'verification_pending',
    'the real browser claims its endpoint back');
  perform hp_test.as_service();
  select p into c from public.issue_device_claim_challenges('20000000-0000-0000-0000-000000000051') p;
  perform hp_test.is(c->'device'->>'endpoint', eg, 'pushed to the endpoint');
  perform hp_test.is(c->'device'->>'p256dh' || ' ' || (c->'device'->>'auth'), 'key-real auth-real', 'encrypted to the real browser''s keys, not the squatter''s');
  v_nonce := c->>'nonce';
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.is(public.confirm_device_claim(v_nonce), 'confirmed', 'the real browser reads it and confirms');
  perform hp_test.as_owner();
  perform hp_test.is((select string_agg(user_id::text || ' ' || p256dh, ',') from public.notification_devices where endpoint = eg),
    '20000000-0000-0000-0000-000000000051 key-real', 'the student holds the endpoint again, with the real keys');
  -- Turned around: the squatter presents its own keys for the student's endpoint. The challenge is encrypted to the
  -- squatter's keys but goes only to the student's endpoint; nothing goes to any device of the squatter's.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform public.report_notification_device(gen_random_uuid(), 'granted', hp_test.web_keys('https://web.push.apple.com/squatter-own', 'squatter'), 'desktop');
  perform hp_test.is(public.report_notification_device(gen_random_uuid(), 'granted', hp_test.web_keys(eg, 'squatter'), 'desktop'), 'verification_pending',
    'the squatter''s report is only a claim');
  perform hp_test.as_service();
  select p into c from public.issue_device_claim_challenges('20000000-0000-0000-0000-000000000099') p;
  perform hp_test.is(c->'device'->>'endpoint', eg, 'its challenge goes to the student''s endpoint only');
  perform hp_test.ok(c::text not like '%squatter-own%', 'never to the squatter''s own endpoint');
  perform hp_test.as_owner();
  perform hp_test.is((select user_id from public.notification_devices where endpoint = eg), '20000000-0000-0000-0000-000000000051'::uuid, 'the student keeps it');
  delete from public.notification_device_claims;
end $$;

-- 9. One login holds at most one of a device's 3 pending slots: its newest report replaces its older claim once that
--    was challenged or expired (a pending, unchallenged claim is refreshed instead).
do $$
declare t uuid := '6d000000-0000-4000-a000-0000000000c7'; e2 text := 'https://web.push.apple.com/H'; first_id uuid; second_id uuid; i integer;
begin
  -- Student 2's browser H, the device every login claims below.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.is(public.report_notification_device(t, 'granted', hp_test.web_keys(e2, 'student2'), 'desktop'), 'registered', 'student 2''s browser');
  perform hp_test.as_owner();
  delete from public.notification_device_claims;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform public.report_notification_device(t, 'granted', hp_test.web_keys(e2, 'goals'), 'desktop');
  perform hp_test.as_owner();
  select id into first_id from public.notification_device_claims where status = 'pending';
  -- An expired, never challenged claim is not refreshed: the next report replaces it.
  update public.notification_device_claims set created_at = now() - interval '11 minutes', expires_at = now() - interval '1 minute' where id = first_id;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform public.report_notification_device(t, 'granted', hp_test.web_keys(e2, 'goals'), 'desktop');
  perform hp_test.as_owner();
  select id into second_id from public.notification_device_claims where status = 'pending';
  perform hp_test.ok(second_id <> first_id and (select status from public.notification_device_claims where id = first_id) = 'expired'
    and (select expires_at > now() from public.notification_device_claims where id = second_id), 'an expired claim is replaced by a fresh one, not refreshed');
  -- A challenged claim is replaced by the newest report; the same login keeps one slot however often it reports.
  perform hp_test.ok(hp_test.nonce_for('20000000-0000-0000-0000-0000000000c1') is not null, 'challenged');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform public.report_notification_device(t, 'granted', hp_test.web_keys(e2, 'goals'), 'desktop');
  perform hp_test.as_owner();
  perform hp_test.is((select status from public.notification_device_claims where id = second_id), 'replaced', 'a challenged claim is replaced by the newest report');
  perform hp_test.is((select count(*) from public.notification_device_claims where target_device_id = t and status = 'pending'), 1::bigint, 'one slot for that login');
  -- Two more logins fill the cap; a fourth is limited; the first login's next report still takes only its own slot.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c2');
  perform hp_test.is(public.report_notification_device(t, 'granted', hp_test.web_keys(e2, 'manager'), 'desktop'), 'verification_pending', 'second login');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000d1');
  perform hp_test.is(public.report_notification_device(t, 'granted', hp_test.web_keys(e2, 'other'), 'desktop'), 'verification_pending', 'third login');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.is(public.report_notification_device(t, 'granted', hp_test.web_keys(e2, 'co'), 'desktop'), 'verification_limited', 'a fourth login waits');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform hp_test.is(public.report_notification_device(t, 'granted', hp_test.web_keys(e2, 'goals'), 'desktop'), 'verification_pending',
    'the first login''s newest report replaces its own claim');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.notification_device_claims where target_device_id = t and status = 'pending'), 3::bigint, 'still three slots, one per login');
  delete from public.notification_device_claims;
end $$;

-- 10. Per device and hour, verify pushes go to at most 3 distinct claimants.
do $$
declare t uuid := '6d000000-0000-4000-a000-0000000000c7'; e2 text := 'https://web.push.apple.com/H'; r record; n bigint;
begin
  for r in select * from (values ('20000000-0000-0000-0000-0000000000c1'::uuid, 'a'), ('20000000-0000-0000-0000-0000000000c2'::uuid, 'b'),
      ('20000000-0000-0000-0000-0000000000d1'::uuid, 'c')) v(uid, k) loop
    perform hp_test.as_user(r.uid);
    perform public.report_notification_device(t, 'granted', hp_test.web_keys(e2, r.k), 'desktop');
  end loop;
  perform hp_test.as_service();
  perform hp_test.is((select count(*) from public.issue_device_claim_challenges(null)), 3::bigint, 'three pushes');
  -- The owner declines all three; a fourth login claims within the hour: no fourth push.
  perform hp_test.as_owner();
  update public.notification_device_claims set status = 'declined' where status = 'pending';
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.is(public.report_notification_device(t, 'granted', hp_test.web_keys(e2, 'd'), 'desktop'), 'verification_pending', 'a fourth claim is recorded');
  perform hp_test.as_service();
  perform hp_test.is((select count(*) from public.issue_device_claim_challenges(null)), 0::bigint, 'but no fourth push to that device within the hour');
  perform hp_test.as_owner();
  update public.notification_device_claims set issued_at = issued_at - interval '61 minutes' where issued_at is not null;
  perform hp_test.as_service();
  perform hp_test.is((select count(*) from public.issue_device_claim_challenges(null)), 1::bigint, 'an hour later it goes');
  perform hp_test.as_owner();
  delete from public.notification_device_claims;
end $$;

-- 10b. One login can never use more than its own slot: an attacker re-reporting a device gets one verify push an hour,
--      and a second login's push still goes.
do $$
declare t uuid := '6d000000-0000-4000-a000-0000000000c7'; e2 text := 'https://web.push.apple.com/H'; i integer; n bigint := 0; k bigint;
begin
  for i in 1..4 loop
    perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
    perform hp_test.is(public.report_notification_device(t, 'granted', hp_test.web_keys(e2, 'attacker'), 'desktop'), 'verification_pending', 'attacker report ' || i);
    perform hp_test.as_service();
    select count(*) into k from public.issue_device_claim_challenges('20000000-0000-0000-0000-000000000099');
    n := n + k;
  end loop;
  perform hp_test.is(n, 1::bigint, 'the attacker''s repeated reports get one verify push in the hour');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c2');
  perform hp_test.is(public.report_notification_device(t, 'granted', hp_test.web_keys(e2, 'manager'), 'desktop'), 'verification_pending', 'a second login claims');
  perform hp_test.as_service();
  perform hp_test.is((select count(*) from public.issue_device_claim_challenges('20000000-0000-0000-0000-0000000000c2')), 1::bigint,
    'and its push still goes');
  perform hp_test.as_owner();
  delete from public.notification_device_claims;
end $$;

-- 11. Retention: unregister withdraws the caller's own claims from that device; purge closes and deletes old rows.
do $$
declare t uuid := '6d000000-0000-4000-a000-0000000000c7'; e2 text := 'https://web.push.apple.com/H'; mine uuid := '6d000000-0000-4000-a000-0000000000c8'; v jsonb;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform public.report_notification_device(mine, 'granted', hp_test.web_keys(e2, 'goals'), 'desktop');
  perform hp_test.is(public.unregister_notification_device(mine), false, 'nothing of the caller''s was registered under that id');
  perform hp_test.as_owner();
  perform hp_test.ok((select status = 'withdrawn' and endpoint is null and p256dh is null and auth_secret is null
    from public.notification_device_claims where claimant_user_id = '20000000-0000-0000-0000-0000000000c1'), 'but its pending claim from that device is withdrawn, credentials cleared');
  -- purge_device_claims: pending past expiry close; resolved claims over 30 days and failures over a day go.
  insert into public.notification_device_claims(target_device_id, claimant_user_id, device_id, permission, channel, endpoint, p256dh, auth_secret, created_at, expires_at)
  values (t, '20000000-0000-0000-0000-0000000000c2', gen_random_uuid(), 'granted', 'webpush', e2, 'k', 'a', now() - interval '20 minutes', now() - interval '10 minutes');
  insert into public.notification_device_claims(target_device_id, claimant_user_id, device_id, permission, channel, status, created_at, expires_at, resolved_at)
  values (t, '20000000-0000-0000-0000-0000000000d1', gen_random_uuid(), 'granted', 'webpush', 'confirmed', now() - interval '40 days', now() - interval '40 days' + interval '10 minutes', now() - interval '31 days'),
         (t, '20000000-0000-0000-0000-0000000000a2', gen_random_uuid(), 'granted', 'webpush', 'declined', now() - interval '50 days', now() - interval '50 days' + interval '10 minutes', now() - interval '45 days');
  insert into public.notification_device_claim_failures(user_id, failed_at) values
    ('20000000-0000-0000-0000-0000000000d1', now() - interval '2 days'), ('20000000-0000-0000-0000-0000000000d1', now() - interval '5 minutes');
  perform hp_test.as_service();
  v := public.purge_device_claims(now());
  perform hp_test.is(v, '{"expired": 1, "claims_deleted": 2, "failures_deleted": 1}'::jsonb, 'purge: one expired, two old claims, one old failure');
  perform hp_test.ok(not exists (select 1 from public.notification_device_claims where resolved_at < now() - interval '30 days'), 'no resolved claim over 30 days remains');
  perform hp_test.as_owner();
  perform hp_test.ok((select status = 'expired' and endpoint is null and p256dh is null from public.notification_device_claims
    where claimant_user_id = '20000000-0000-0000-0000-0000000000c2'), 'the expired claim keeps no credentials');
  perform hp_test.is((select count(*) from public.notification_device_claim_failures), 1::bigint, 'the recent failure stays');
  perform hp_test.is((select count(*) from public.notification_device_claims where claimant_user_id = '20000000-0000-0000-0000-0000000000c1'), 1::bigint,
    'a recent resolved claim stays (30 days)');
  perform hp_test.as_service();
  perform hp_test.is(public.purge_device_claims(now()), '{"expired": 0, "claims_deleted": 0, "failures_deleted": 0}'::jsonb, 'a second purge finds nothing');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform hp_test.err('select public.purge_device_claims(now())', '42501');
  perform hp_test.as_owner();
  -- Credentials can't be kept on a resolved claim, written either way.
  update public.notification_device_claims set status = 'confirmed', endpoint = 'https://web.push.apple.com/x', p256dh = 'k', auth_secret = 'a'
  where claimant_user_id = '20000000-0000-0000-0000-0000000000c1';
  perform hp_test.ok((select endpoint is null and p256dh is null from public.notification_device_claims where claimant_user_id = '20000000-0000-0000-0000-0000000000c1'),
    'resolving clears them');
  perform hp_test.err(format($q$insert into public.notification_device_claims(target_device_id, claimant_user_id, device_id, permission, channel, endpoint, p256dh,
    auth_secret, status, expires_at, resolved_at) values (%L, '20000000-0000-0000-0000-0000000000d1', gen_random_uuid(), 'granted', 'webpush',
    'https://web.push.apple.com/x', 'k', 'a', 'confirmed', now() + interval '1 minute', now())$q$, t), '23514');
  delete from public.notification_device_claims;
  delete from public.notification_device_claim_failures;
end $$;

-- 12. Guards: a challenge never goes to a device marked gone; the registration helper never writes another login's row.
do $$
declare t uuid := '6d000000-0000-4000-a000-0000000000c7'; e2 text := 'https://web.push.apple.com/H';
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform hp_test.is(public.report_notification_device(t, 'granted', hp_test.web_keys(e2, 'goals'), 'desktop'), 'verification_pending', 'a claim');
  perform hp_test.as_owner();
  update public.notification_devices set gone_at = now() where id = t;  -- the push service said it is gone, after the claim
  perform hp_test.as_service();
  perform hp_test.is((select count(*) from public.issue_device_claim_challenges(null)), 0::bigint, 'no challenge to a device marked gone');
  perform hp_test.as_owner();
  update public.notification_devices set gone_at = null where id = t;
  perform hp_test.err(format($q$select public.notification_device_register_internal('20000000-0000-0000-0000-0000000000c1', %L, 'granted', 'desktop', 'webpush',
    null, 'https://web.push.apple.com/other', 'k', 'a')$q$, t), '40001');
  perform hp_test.is((select user_id from public.notification_devices where id = t), '20000000-0000-0000-0000-000000000052'::uuid, 'another login''s row is never written');
  delete from public.notification_device_claims;
end $$;

\o
select format('device_claims: all %s assertions passed', last_value) from hp_test.assertions \gset
\echo :format
rollback;
