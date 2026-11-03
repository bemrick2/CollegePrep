-- CR-27 practice reminders (20261102030000_practice_reminders.sql): settings, the guardian notice, devices, and the
-- claim-then-send record. Tested role by role; rolled back. Two-connection races: scripts/test_reminder_concurrency.py.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql
\ir support/counted_helpers.sql
\ir support/household_roles.sql

alter table auth.users add column if not exists email text;
update auth.users set email = right(id::text, 2) || '@example.test';
create function hp_test.reminders(p_enabled boolean) returns jsonb language sql immutable as $$
  select jsonb_build_object('enabled', p_enabled, 'times', array['16:30'], 'days', array[1,2,3,4,5,6,7], 'quiet_start', '21:00',
    'quiet_end', '07:00', 'school_days', array[1,2,3,4,5], 'school_start', '08:00', 'school_end', '15:00', 'max_per_day', 1, 'max_per_week', 5)
$$;
grant execute on function hp_test.reminders(boolean) to anon, authenticated, service_role;

-- 1. Who may change reminders: the student's own login, or a guardian with set_goals in the student's household.
do $$
declare r record; st uuid := current_setting('t.st')::uuid; ok boolean; s jsonb := hp_test.reminders(false);
begin
  for r in select * from t_roles loop
    perform hp_test.as_user(r.uid);
    begin
      perform public.set_practice_reminders(st, s);
      ok := true;
    exception when insufficient_privilege then ok := false;
    end;
    perform hp_test.is(ok, r.who in ('PARENT', 'CO', 'GOALS', 'STUDENT'), r.who || ' saves reminder settings');
  end loop;
  perform hp_test.as_anon();
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', st, s), '42501');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.practice_reminder_changes), 0::bigint, 'saving "off" first records no change');
  -- What the schema refuses.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', st, s || '{"times":["16:10"]}'), '23514');
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', st, s || '{"times":["08:00","09:00","10:00","11:00"]}'), '23514');
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', st, s || '{"times":["08:00","08:00"]}'), '23514');
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', st, s || '{"days":[8]}'), '23514');
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', st, s || '{"days":[1,1]}'), '23514');
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', st, s || '{"days":[]}'), '23514');
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', st, s || '{"school_days":[0]}'), '23514');
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', st, s || '{"max_per_day":4}'), '23514');
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', st, s || '{"max_per_week":15}'), '23514');
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', st, s || '{"quiet_start":"25:00"}'), '23514');
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', st, s || '{"school_end":null}'), '23514');
  perform hp_test.err(format($q$select public.set_practice_reminders(%L, '[true]')$q$, st), '22023');
  perform hp_test.err(format('select public.set_practice_reminders(%L, null)', st), '22023');
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', gen_random_uuid(), s), '42501');
  perform hp_test.as_owner();
  update public.students set archived_at = now() where id = current_setting('t.st_b')::uuid;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.err(format('select public.set_practice_reminders(%L, %L)', current_setting('t.st_b'), s), '42501');
  perform hp_test.as_owner();
  update public.students set archived_at = null where id = current_setting('t.st_b')::uuid;
end $$;

-- 2. Reads, and nothing written or read around the RPCs.
do $$
declare r record; st uuid := current_setting('t.st')::uuid; n bigint; t text;
begin
  for r in select * from t_roles loop
    perform hp_test.as_user(r.uid);
    select count(*) into n from public.practice_reminder_settings where student_id = st;
    perform hp_test.is(n, case when r.who in ('PARENT', 'CO', 'VIEWER', 'GOALS', 'STUDENT') then 1::bigint else 0::bigint end,
      r.who || ' reads reminder settings');
    perform hp_test.err('select updated_by from public.practice_reminder_settings', '42501');
    perform hp_test.err('select changed_by from public.practice_reminder_changes', '42501');
    perform hp_test.err('select household_id from public.practice_reminder_changes', '42501');
    perform hp_test.err('select reminder_key from public.practice_reminder_deliveries', '42501');
    perform hp_test.err('select device_id from public.practice_reminder_deliveries', '42501');
    perform hp_test.err('select id from public.notification_devices', '42501');
    foreach t in array array['practice_reminder_settings', 'practice_reminder_changes', 'practice_reminder_deliveries', 'notification_devices'] loop
      perform hp_test.err(format('delete from public.%I', t), '42501');
      perform hp_test.err(format('update public.%I set %I = %I', t, case t when 'practice_reminder_settings' then 'student_id' else 'id' end,
        case t when 'practice_reminder_settings' then 'student_id' else 'id' end), '42501');
    end loop;
    perform hp_test.err(format($q$insert into public.practice_reminder_settings(student_id, enabled) values (%L, true)$q$, st), '42501');
    perform hp_test.err(format($q$insert into public.practice_reminder_changes(student_id, enabled, changed_by_role) values (%L, false, 'student')$q$, st), '42501');
    perform hp_test.err(format($q$insert into public.practice_reminder_deliveries(student_id, slot, reminder_key, status) values (%L, '16:30', 'x', 'sent')$q$, st), '42501');
    perform hp_test.err($q$insert into public.notification_devices(id, user_id, permission) values (gen_random_uuid(), auth.uid(), 'granted')$q$, '42501');
  end loop;
  perform hp_test.as_anon();
  perform hp_test.err('select enabled from public.practice_reminder_settings', '42501');
  perform hp_test.err('select enabled from public.practice_reminder_changes', '42501');
  perform hp_test.err('select status from public.practice_reminder_deliveries', '42501');
  perform hp_test.as_owner();
  perform hp_test.err(format($q$insert into public.practice_reminder_changes(student_id, enabled, changed_by_role, notify_guardians)
    values (%L, false, 'student', true)$q$, st), '23514');  -- a notice needs the household it goes to
end $$;

-- 3. Turning reminders off: only the student's own login, in a household, not independent, tells guardians; once per
--    24 hours; each guardian with view_progress in that household gets one notice, until it is recorded.
do $$
declare st uuid := current_setting('t.st')::uuid; on_ jsonb := hp_test.reminders(true); off_ jsonb := hp_test.reminders(false);
  rows jsonb; v_change uuid; n bigint;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.is(public.set_practice_reminders(st, on_), '{"enabled": true, "guardians_notified": false}'::jsonb, 'the parent turns them on');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.is(public.set_practice_reminders(st, off_), '{"enabled": false, "guardians_notified": true}'::jsonb, 'the student turns them off: guardians are told');
  perform hp_test.as_owner();
  select id into v_change from public.practice_reminder_changes where notify_guardians;
  perform hp_test.is((select household_id from public.practice_reminder_changes where id = v_change), current_setting('t.hh')::uuid, 'the household is recorded');
  perform hp_test.as_service();
  select jsonb_agg(p order by p->>'user_id') into rows from public.reminder_opt_out_payload() p;
  perform hp_test.is((select array_agg(x->>'email' order by x->>'user_id') from jsonb_array_elements(rows) x),
    array['a1@example.test', 'a2@example.test', 'b1@example.test'], 'each guardian with view_progress, at their own address');
  perform hp_test.ok((select bool_and(x->>'student_name' = 'Riley' and x->>'period_key' = v_change::text and x->>'time_zone' = 'America/Chicago')
    from jsonb_array_elements(rows) x), 'about Riley, keyed on the change');
  -- Later changes within a day are recorded, not emailed again; a guardian turning them off tells nobody.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.set_practice_reminders(st, on_);
  perform hp_test.is(public.set_practice_reminders(st, off_)->'guardians_notified', 'false'::jsonb, 'a second "off" within 24 hours is not emailed');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform public.set_practice_reminders(st, on_);
  perform hp_test.is(public.set_practice_reminders(st, off_)->'guardians_notified', 'false'::jsonb, 'a guardian turning them off tells nobody');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.practice_reminder_changes where student_id = st), 6::bigint, 'every change is recorded');
  perform hp_test.is((select count(*) from public.practice_reminder_changes where notify_guardians), 1::bigint, 'one is flagged');
  -- Recording the notice for one guardian removes only that guardian; the app shows "emailed" from that record alone.
  perform hp_test.as_service();
  perform hp_test.is(public.mark_parent_email_sent('20000000-0000-0000-0000-0000000000a1', 'reminders_off', v_change::text), true, 'recorded');
  perform hp_test.is((select count(*) from public.reminder_opt_out_payload()), 2::bigint, 'the other two remain');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.ok((select emailed_to_me_at is not null from public.practice_reminder_history(st) h where h.id = v_change), 'the parent sees it was emailed to them');
  perform hp_test.is((select count(*) from public.practice_reminder_history(st)), 6::bigint, 'the parent sees the history');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.ok((select emailed_to_me_at is null and notify_guardians from public.practice_reminder_history(st) h where h.id = v_change), 'the viewer''s own notice is not sent yet');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.is((select count(*) from public.practice_reminder_history(st)), 6::bigint, 'the student sees the history');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c2');
  perform hp_test.err(format('select * from public.practice_reminder_history(%L)', st), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.err(format('select * from public.practice_reminder_history(%L)', st), '42501');
  -- A snooze tells nobody.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.set_practice_reminders(st, on_);
  perform hp_test.ok(public.snooze_practice_reminders(st, 60) > now(), 'the student snoozes');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.practice_reminder_changes where notify_guardians), 1::bigint, 'a snooze flags nothing');
  -- An independent student and a student outside any household are never reported.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform public.set_practice_reminders(current_setting('t.adult')::uuid, on_);
  perform hp_test.is(public.set_practice_reminders(current_setting('t.adult')::uuid, off_)->'guardians_notified', 'false'::jsonb, 'independent: never reported');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.set_practice_reminders(current_setting('t.solo')::uuid, on_);
  perform hp_test.is(public.set_practice_reminders(current_setting('t.solo')::uuid, off_)->'guardians_notified', 'false'::jsonb, 'no household: never reported');
  perform hp_test.as_service();
  perform hp_test.is((select count(*) from public.reminder_opt_out_payload()), 2::bigint, 'still only the two pending notices');
  perform hp_test.as_owner();
end $$;

-- 3b. Each rule of the notice on its own: a guardian's "off" and an independent student's "off" are never reported,
--     even with no earlier notice that day; a student who is neither is reported; only guardians receive it.
do $$
declare hh uuid := current_setting('t.hh')::uuid; ben uuid := current_setting('t.st_b')::uuid; on_ jsonb := hp_test.reminders(true);
  off_ jsonb := hp_test.reminders(false); inv text; rows jsonb;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.set_practice_reminders(ben, on_);
  perform hp_test.is(public.set_practice_reminders(ben, off_)->'guardians_notified', 'false'::jsonb, 'a guardian turning them off is not reported');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.practice_reminder_changes where student_id = ben and notify_guardians), 0::bigint, 'nothing flagged');
  -- Ben gets his own login, and is independent.
  insert into auth.users(id, email) values ('20000000-0000-0000-0000-0000000000e1', 'e1@example.test');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  inv := public.create_household_invitation(hh, 'student', ben);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000e1');
  perform public.accept_household_invitation(inv);
  perform hp_test.as_owner();
  update public.students set is_independent = true where id = ben;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000e1');
  perform public.set_practice_reminders(ben, on_);
  perform hp_test.is(public.set_practice_reminders(ben, off_)->'guardians_notified', 'false'::jsonb, 'an independent student in a household is not reported');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.practice_reminder_changes where student_id = ben and notify_guardians), 0::bigint, 'still nothing flagged');
  -- Not independent: the same "off" is reported.
  update public.students set is_independent = false where id = ben;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000e1');
  perform public.set_practice_reminders(ben, on_);
  perform hp_test.is(public.set_practice_reminders(ben, off_)->'guardians_notified', 'true'::jsonb, 'the same student, not independent, is reported');
  perform hp_test.as_service();
  select jsonb_agg(p order by p->>'user_id') into rows from public.reminder_opt_out_payload() p where p->>'student_id' = ben::text;
  perform hp_test.is((select array_agg(x->>'user_id' order by x->>'user_id') from jsonb_array_elements(rows) x),
    array['20000000-0000-0000-0000-0000000000a1', '20000000-0000-0000-0000-0000000000a2', '20000000-0000-0000-0000-0000000000b1'],
    'only guardians with view_progress are told: not the students, not set-goals-only or manage-students-only guardians');
  -- A student who becomes independent before the notice goes is not reported.
  perform hp_test.as_owner();
  update public.students set is_independent = true where id = ben;
  perform hp_test.as_service();
  perform hp_test.is((select count(*) from public.reminder_opt_out_payload() p where p->>'student_id' = ben::text), 0::bigint,
    'a notice pending for a student now independent is dropped');
  perform hp_test.as_owner();
  update public.students set is_independent = false where id = ben;
  -- The guardian-only rule holds by construction: a student member can never hold view_progress.
  perform hp_test.err($q$update public.household_members set can_view_progress = true where user_id = '20000000-0000-0000-0000-000000000051'$q$, '23514');
end $$;

-- 4. Devices: reported by their own login; only known push services; families see state, never endpoints or keys.
do $$
declare st uuid := current_setting('t.st')::uuid; d1 uuid := '5f000000-0000-4000-a000-000000000001'; d5 uuid := '5f000000-0000-4000-a000-000000000005';
  d6 uuid := '5f000000-0000-4000-a000-000000000006'; keys jsonb := '{"p256dh":"BPUBLICKEYSECRET","auth":"AUTHSECRET"}'; t text; n bigint; v text;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.report_notification_device(d1, 'granted', jsonb_build_object('endpoint', 'https://fcm.googleapis.com/fcm/send/abc', 'keys', keys), 'android');
  foreach t in array array['https://updates.push.services.mozilla.com/wpush/v2/x', 'https://wns2-par02p.notify.windows.com/w/?token=x',
      'https://web.push.apple.com/QXbc'] loop
    perform public.report_notification_device(gen_random_uuid(), 'granted', jsonb_build_object('endpoint', t, 'keys', keys), 'desktop');
  end loop;
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.notification_devices where user_id = '20000000-0000-0000-0000-000000000051' and endpoint is not null), 4::bigint,
    'four known push services are accepted');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  foreach t in array array['https://evil.example/x', 'https://127.0.0.1:8443/x', 'https://fcm.googleapis.com.evil.example/x',
      'http://fcm.googleapis.com/fcm/send/x', 'https://localhost/x'] loop
    perform hp_test.err(format('select public.report_notification_device(gen_random_uuid(), %L, %L, %L)', 'granted',
      jsonb_build_object('endpoint', t, 'keys', keys), 'desktop'), '22023', '%push service%');
  end loop;
  perform hp_test.err($q$select public.report_notification_device(null, 'granted')$q$, '22023');
  perform hp_test.err($q$select public.report_notification_device(gen_random_uuid(), 'granted', null, null, 'sms')$q$, '22023');
  perform hp_test.err($q$select public.report_notification_device(gen_random_uuid(), 'maybe')$q$, '22023');
  -- A denied device is stored without keys, whatever the app sends.
  perform public.report_notification_device('5f000000-0000-4000-a000-000000000002', 'denied',
    jsonb_build_object('endpoint', 'https://fcm.googleapis.com/fcm/send/denied', 'keys', keys), 'ios');
  perform hp_test.as_owner();
  perform hp_test.ok((select endpoint is null and p256dh is null from public.notification_devices where id = '5f000000-0000-4000-a000-000000000002'), 'denied: no keys kept');
  -- Knowing a device id, or even the device's endpoint, is not enough to take it over (20261103010000): every report by
  -- another login leaves the student's row as it was, and at most makes a claim the device itself must confirm
  -- (supabase/tests/device_claims.sql).
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.is(public.report_notification_device(d1, 'denied', null, 'desktop'), 'verification_pending', 'a report of another login''s device only makes a claim');
  perform public.report_notification_device(d1, 'unsupported');
  perform public.report_notification_device(d1, 'granted', jsonb_build_object('endpoint', 'https://fcm.googleapis.com/fcm/send/mine',
    'keys', '{"p256dh":"PARENTKEY","auth":"PARENTAUTH"}'::jsonb), 'desktop');
  perform public.report_notification_device(d1, 'granted', jsonb_build_object('endpoint', 'https://fcm.googleapis.com/fcm/send/abc',
    'keys', '{"p256dh":"PARENTKEY","auth":"PARENTAUTH"}'::jsonb), 'desktop');
  perform public.report_notification_device(d1, 'granted', null, 'ios', 'fcm', 'fcm-registration-token-guess-0001');
  perform hp_test.as_owner();
  perform hp_test.is((select user_id::text || ' ' || permission || ' ' || endpoint || ' ' || p256dh from public.notification_devices where id = d1),
    '20000000-0000-0000-0000-000000000051 granted https://fcm.googleapis.com/fcm/send/abc BPUBLICKEYSECRET', 'not even with the device''s own endpoint');
  -- A row with no endpoint or token can't be verified, so it stays where it is too.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.is(public.report_notification_device('5f000000-0000-4000-a000-000000000002', 'default', null, 'ios'), 'device_held',
    'a device without push credentials is held, not moved');
  perform hp_test.as_owner();
  perform hp_test.is((select user_id from public.notification_devices where id = '5f000000-0000-4000-a000-000000000002'),
    '20000000-0000-0000-0000-000000000051'::uuid, 'and stays the student''s');
  perform hp_test.as_anon();
  perform hp_test.err(format($q$select public.report_notification_device(%L, 'granted')$q$, gen_random_uuid()), '42501');
  -- What the family sees: a handle, never the device id (a viewer who knew the id could report it).
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  select count(*), string_agg(x::text, ' ') into n, v from public.student_notification_devices(st) x;
  perform hp_test.is(n, 5::bigint, 'the parent sees the student''s five devices');
  perform hp_test.ok(v not like '%' || d1::text || '%' and v not like '%5f000000-%', 'no device id in what the family sees');
  perform set_config('t.handles', (select string_agg(x.device_handle::text, ',') from public.student_notification_devices(st) x), true);
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.notification_devices d where d.handle::text = any (string_to_array(current_setting('t.handles'), ','))
    and d.user_id = '20000000-0000-0000-0000-000000000051'), 5::bigint, 'each handle names one of the student''s devices');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.is((select array_agg(x.device_handle order by x.device_handle) from public.student_notification_devices(st) x),
    (select array_agg(x.device_handle order by x.device_handle) from public.student_notification_devices(st) x), 'handles are stable between calls');
  perform hp_test.err('select handle from public.notification_devices', '42501');
  perform hp_test.ok(v not like '%googleapis%' and v not like '%SECRET%' and v not like '%mozilla%', 'no endpoint or key in what the family sees');
  perform hp_test.is((select count(*) from public.student_notification_devices(st) x where x.can_receive), 4::bigint, 'four can receive');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.is((select count(*) from public.student_notification_devices(st)), 5::bigint, 'the viewer sees them too');
  -- A view-only guardian (who may not change reminders) can't silence the student through a device: reporting a handle
  -- 'denied' touches none of the student's devices, nor does reporting a device id without its endpoint.
  for v in select x.device_handle::text from public.student_notification_devices(st) x loop
    perform public.report_notification_device(v::uuid, 'denied', null, 'desktop');
  end loop;
  perform public.report_notification_device(d1, 'denied', null, 'desktop');
  perform hp_test.is((select count(*) from public.student_notification_devices(st) x where x.can_receive), 4::bigint,
    'a view-only guardian who knows the handles can''t silence the student');
  perform hp_test.as_service();
  perform hp_test.ok((select jsonb_array_length(p->'devices') = 4 from public.practice_reminder_candidates(now()) p where p->>'student_id' = st::text) is not false,
    'the sender still has the student''s four devices');
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.notification_devices where user_id = '20000000-0000-0000-0000-000000000051' and permission = 'granted' and endpoint is not null),
    4::bigint, 'the student''s devices are unchanged');
  foreach v in array array['20000000-0000-0000-0000-0000000000c2', '20000000-0000-0000-0000-0000000000c1', '20000000-0000-0000-0000-0000000000d1',
      '20000000-0000-0000-0000-000000000099'] loop
    perform hp_test.as_user(v::uuid);
    perform hp_test.err(format('select * from public.student_notification_devices(%L)', st), '42501');
  end loop;
  -- A native token or a web endpoint another login holds does not move on a report either.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.is(public.report_notification_device(d5, 'granted', null, 'ios', 'fcm', 'fcm-registration-token-000000001'), 'registered', 'the student''s own install');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.is(public.report_notification_device(d6, 'granted', null, 'ios', 'fcm', 'fcm-registration-token-000000001'), 'verification_pending',
    'a known token only makes a claim');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.report_notification_device('5f000000-0000-4000-a000-000000000007', 'granted',
    jsonb_build_object('endpoint', 'https://web.push.apple.com/shared-browser', 'keys', keys), 'desktop');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000d1');
  perform hp_test.is(public.report_notification_device('5f000000-0000-4000-a000-000000000008', 'granted',
    jsonb_build_object('endpoint', 'https://web.push.apple.com/shared-browser', 'keys', keys), 'desktop'), 'verification_pending', 'a known endpoint only makes a claim');
  perform hp_test.as_owner();
  perform hp_test.is((select string_agg(user_id::text || ' ' || id::text, ',') from public.notification_devices
    where push_token = 'fcm-registration-token-000000001' or endpoint = 'https://web.push.apple.com/shared-browser'),
    '20000000-0000-0000-0000-000000000051 5f000000-0000-4000-a000-000000000005,20000000-0000-0000-0000-000000000052 5f000000-0000-4000-a000-000000000007',
    'the token and the endpoint stay with their logins');
  perform hp_test.ok(not exists (select 1 from public.notification_devices where id in (d6, '5f000000-0000-4000-a000-000000000008')), 'no row for the claimants');
  -- At most 20 devices per login: the least recently seen go.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  for n in 1..22 loop
    perform set_config('t.dummy', n::text, true);
    perform public.report_notification_device(gen_random_uuid(), 'default', null, 'other');
  end loop;
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.notification_devices where user_id = '20000000-0000-0000-0000-000000000099'), 20::bigint, 'twenty devices kept');
  -- The local stack's fake push service is accepted only where the database owner allows it.
  execute format('alter database %I set collegeprep.local_push_endpoints = %L', current_database(), 'on');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.report_notification_device(gen_random_uuid(), 'granted', jsonb_build_object('endpoint', 'https://127.0.0.1:54345/sub/x', 'keys', keys), 'desktop');
  -- Local mode is exactly 127.0.0.1 or localhost, not a host that starts with them.
  foreach t in array array['https://localhost.evil.com/x', 'https://127.0.0.1.evil.com/x', 'https://localhost@evil.com/x', 'https://127.0.0.1:99999999/x'] loop
    perform hp_test.err(format('select public.report_notification_device(gen_random_uuid(), %L, %L, %L)', 'granted',
      jsonb_build_object('endpoint', t, 'keys', keys), 'desktop'), '22023', '%push service%');
  end loop;
  perform hp_test.as_owner();
  execute format('alter database %I reset collegeprep.local_push_endpoints', current_database());
  perform hp_test.is((select count(*) from public.notification_devices where endpoint like 'https://127.0.0.1:%'), 1::bigint, 'local endpoint accepted only with the setting');
  perform hp_test.ok(not has_function_privilege('authenticated', 'public.push_endpoint_allowed(text)', 'execute'), 'endpoint rule is internal');
  perform hp_test.ok(not has_function_privilege('authenticated', 'public.local_push_endpoints_enabled()', 'execute'), 'local switch is internal');
end $$;

-- 5. The sender: candidates, claim-then-send (one claimed-or-sent row per reminder key), outcomes, snoozes.
do $$
declare st uuid := current_setting('t.st')::uuid; c jsonb; i1 uuid := gen_random_uuid(); i2 uuid := gen_random_uuid(); i3 uuid := gen_random_uuid();
  i4 uuid := gen_random_uuid(); d1 uuid := '5f000000-0000-4000-a000-000000000001'; d6 uuid := '5f000000-0000-4000-a000-000000000006'; v timestamptz;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.set_practice_reminders(st, hp_test.reminders(true));
  perform hp_test.as_service();
  select p into c from public.practice_reminder_candidates(now()) p where p->>'student_id' = st::text;
  perform hp_test.is(jsonb_array_length(c->'devices'), 5, 'the sender sees the student''s five receiving devices (four browsers, one app)');
  perform hp_test.ok(c->'devices'->0 ? 'p256dh' and c->>'time_zone' = 'America/Chicago', 'with keys (service role only) and the time zone');
  perform hp_test.ok(not exists (select 1 from public.practice_reminder_candidates(now()) p where p->>'student_id' = current_setting('t.adult')),
    'a student with reminders off, or no device, is not a candidate');
  -- Claim before send.
  perform hp_test.is(public.claim_practice_reminder(i1, st, '2026-11-02:16:30', '16:30', now() - interval '10 minutes'), true, 'the first claim of a reminder wins');
  perform hp_test.is(public.claim_practice_reminder(i2, st, '2026-11-02:16:30', '16:30'), false, 'a second claim of the same reminder loses');
  perform hp_test.is(public.claim_practice_reminder(i1, st, '2026-11-03:16:30', '16:30'), false, 'a reused id loses');
  perform hp_test.is(public.claim_practice_reminder(i3, st, '2026-11-02:17:00', '17:00'), true, 'another slot is its own reminder');
  perform public.finish_practice_reminder(i1, d1, 'webpush', 'sent');
  perform hp_test.is(public.claim_practice_reminder(gen_random_uuid(), st, '2026-11-02:16:30', '16:30'), false, 'a sent reminder is never claimed again');
  perform public.finish_practice_reminder(i3, d6, 'fcm', 'failed');
  perform hp_test.ok((select device_id is null and status = 'failed' from public.practice_reminder_deliveries where id = i3),
    'another login''s device is not recorded; the outcome is');
  perform hp_test.is(public.claim_practice_reminder(i4, st, '2026-11-02:17:00', '17:00'), true, 'a failed reminder may be retried');
  perform public.finish_practice_reminder(i4, d1, 'webpush', 'sent');
  perform public.finish_practice_reminder(i4, d1, 'webpush', 'failed');
  perform hp_test.is((select status from public.practice_reminder_deliveries where id = i4), 'sent', 'a finished reminder is not finished again');
  perform hp_test.err(format($q$select public.finish_practice_reminder(%L, null, null, 'claimed')$q$, gen_random_uuid()), '22023');
  perform hp_test.err(format($q$select public.claim_practice_reminder(gen_random_uuid(), %L, null, '16:30')$q$, st), '22023');
  perform hp_test.is((select count(*) from public.practice_reminder_deliveries where student_id = st and reminder_key = '2026-11-02:16:30' and status in ('claimed', 'sent')),
    1::bigint, 'one claimed-or-sent row per reminder');
  -- No claim for a student whose reminders are off, or who is archived.
  perform hp_test.is(public.claim_practice_reminder(gen_random_uuid(), current_setting('t.adult')::uuid, '2026-11-02:16:30', '16:30'), false, 'reminders off: no claim');
  perform hp_test.as_owner();
  update public.students set archived_at = now() where id = st;
  perform hp_test.as_service();
  perform hp_test.is(public.claim_practice_reminder(gen_random_uuid(), st, '2026-11-09:16:30', '16:30'), false, 'archived: no claim');
  perform hp_test.as_owner();
  update public.students set archived_at = null where id = st;
  -- Who sees deliveries: the family, without keys or devices.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.is((select count(*) from public.practice_reminder_deliveries where student_id = st and status = 'sent'), 2::bigint, 'the viewer sees sent reminders');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.is((select count(*) from public.practice_reminder_deliveries), 0::bigint, 'an outsider sees none');
  -- Opened, by the student only.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.err(format('select public.mark_practice_reminder_opened(%L)', i1), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.mark_practice_reminder_opened(i1);
  perform public.mark_practice_reminder_opened(gen_random_uuid());
  perform hp_test.ok((select opened_at is not null from public.practice_reminder_deliveries where id = i1), 'the student opened it');
  -- In-app snooze: the student only, 15 minutes to 24 hours, marks the latest sent reminder.
  perform hp_test.err(format('select public.snooze_practice_reminders(%L, 10)', st), '22023');
  perform hp_test.ok(public.snooze_practice_reminders(st, 30) > now(), 'the student snoozes for 30 minutes');
  perform hp_test.ok((select snoozed_at is not null from public.practice_reminder_deliveries where id = i4), 'the latest sent reminder is marked');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.err(format('select public.snooze_practice_reminders(%L, 60)', st), '42501');
  -- "Remind me later" from the notification (service role, after the signed token is verified): works once.
  perform hp_test.as_service();
  perform hp_test.err(format('select public.snooze_practice_reminder_delivery(%L, 5)', i1), '22023');
  perform hp_test.ok(public.snooze_practice_reminder_delivery(i1, 60) > now(), 'the notification''s snooze works');
  perform hp_test.is(public.snooze_practice_reminder_delivery(i1, 60), null::timestamptz, 'once');
  perform hp_test.is(public.snooze_practice_reminder_delivery(i3, 60), null::timestamptz, 'not for a reminder that was never delivered');
  perform hp_test.is(public.snooze_practice_reminder_delivery(gen_random_uuid(), 60), null::timestamptz, 'not for an unknown one');
  -- A sent snooze reminder uses the snooze up.
  perform hp_test.is(public.claim_practice_reminder(i2, st, 'snooze:x', 'snooze'), true, 'a snooze reminder is claimed');
  perform public.finish_practice_reminder(i2, d1, 'webpush', 'sent');
  perform hp_test.ok((select snoozed_until is null from public.practice_reminder_settings where student_id = st), 'and the snooze is used up');
  perform public.retire_notification_device(d1);
  perform hp_test.ok((select gone_at is not null from public.notification_devices where id = d1), 'a gone device is retired');
  -- Reporting the device again with a new endpoint brings it back.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.report_notification_device(d1, 'granted', '{"endpoint":"https://fcm.googleapis.com/fcm/send/new","keys":{"p256dh":"k","auth":"a"}}');
  perform hp_test.as_owner();
  perform hp_test.ok((select gone_at is null from public.notification_devices where id = d1), 'a new subscription is live again');
  -- Snoozing by token while reminders are off is refused, and the token is not used up.
  perform hp_test.is(public.claim_practice_reminder(i3, st, '2026-11-02:18:00', '18:00'), false, 'a used id is not claimed again');
  v := null;
  perform hp_test.as_owner();
  insert into public.practice_reminder_deliveries(id, student_id, slot, reminder_key, status) values ('5e000000-0000-4000-a000-0000000000f1', st, '18:00', 'off-test', 'sent');
  update public.practice_reminder_settings set enabled = false where student_id = st;
  perform hp_test.as_service();
  perform hp_test.is(public.snooze_practice_reminder_delivery('5e000000-0000-4000-a000-0000000000f1', 60), null::timestamptz, 'no snooze while reminders are off');
  perform hp_test.as_owner();
  perform hp_test.ok((select snoozed_at is null from public.practice_reminder_deliveries where id = '5e000000-0000-4000-a000-0000000000f1'), 'and the token is not used up');
  update public.practice_reminder_settings set enabled = true where student_id = st;
  perform hp_test.as_service();
  perform hp_test.ok(public.snooze_practice_reminder_delivery('5e000000-0000-4000-a000-0000000000f1', 60) is not null, 'it works once reminders are on again');
  -- Signing out on a shared browser unregisters it: no longer a candidate device at once, and the delivery history
  -- stays the student's without pointing at the device.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.is(public.unregister_notification_device(d1), true, 'the student unregisters the browser on sign-out');
  perform hp_test.as_service();
  select p into c from public.practice_reminder_candidates(now()) p where p->>'student_id' = st::text;
  perform hp_test.ok(not exists (select 1 from jsonb_array_elements(c->'devices') x where x->>'id' = d1::text), 'the browser gets none of the student''s reminders');
  perform hp_test.ok(c::text not like '%send/new%', 'its endpoint is not in the student''s candidates');
  perform hp_test.is((select count(*) from public.practice_reminder_deliveries where device_id = d1), 0::bigint, 'the student''s deliveries no longer point at it');
  perform hp_test.as_owner();
end $$;

-- 5b. Lost claims: claimed_at is the claim's own clock time. A recent unfinished claim counts toward the limits and the
--     gap; an old one expires as failed; a sender that finishes an expired claim as sent still records the send.
do $$
declare st uuid := current_setting('t.st')::uuid; base integer; c jsonb; n integer; old_id uuid := gen_random_uuid();
  young uuid := gen_random_uuid(); late uuid := gen_random_uuid(); again uuid := gen_random_uuid(); t0 timestamptz;
begin
  perform hp_test.as_service();
  select (p->'context'->>'sentThisWeek')::integer into base from public.practice_reminder_candidates(now()) p where p->>'student_id' = st::text;
  -- The claim time is the clock at the claim, whatever the run's start time (p_at) says.
  t0 := clock_timestamp();
  perform hp_test.is(public.claim_practice_reminder(young, st, 'lost:young', '16:45', now() - interval '1 hour'), true, 'a claim in flight');
  perform hp_test.ok((select claimed_at >= t0 and claimed_at <= clock_timestamp() from public.practice_reminder_deliveries where id = young),
    'claimed_at is the clock at the claim, not the run''s start');
  select p into c from public.practice_reminder_candidates(now()) p where p->>'student_id' = st::text;
  perform hp_test.is((c->'context'->>'sentThisWeek')::integer, base + 1, 'a claim younger than the timeout counts toward the weekly limit');
  perform hp_test.is((c->'context'->>'lastSentAt')::timestamptz, (select max(sent_at) from public.practice_reminder_deliveries
    where student_id = st and (status = 'sent' or id = young)), 'and toward the minimum gap');
  -- An old claim: made 20 minutes ago by the clock.
  perform hp_test.is(public.claim_practice_reminder(old_id, st, 'lost:old', '16:30', now()), true, 'another claim, left unfinished');
  perform hp_test.as_owner();
  update public.practice_reminder_deliveries set claimed_at = clock_timestamp() - interval '20 minutes' where id = old_id;
  perform hp_test.as_service();
  select p into c from public.practice_reminder_candidates(now()) p where p->>'student_id' = st::text;
  perform hp_test.is((c->'context'->>'sentThisWeek')::integer, base + 1, 'a claim older than the timeout does not count');
  -- Claiming expires the student's lost claims; the lost reminder may be claimed again; a claim in flight may not.
  perform hp_test.is(public.claim_practice_reminder(again, st, 'lost:old', '16:30'), true, 'an expired claim frees its reminder');
  perform hp_test.ok((select status = 'failed' and failure_reason = 'claim_expired' from public.practice_reminder_deliveries where id = old_id),
    'the lost claim expired as failed');
  perform hp_test.is(public.claim_practice_reminder(gen_random_uuid(), st, 'lost:young', '16:45'), false, 'a claim in flight still holds its reminder');
  -- The expired claim's sender did send, and finishes now: recorded, but the reminder was claimed again meanwhile, so
  -- it stays failed as 'claim_expired_resent', and still counts as sent.
  select (p->'context'->>'sentThisWeek')::integer into base from public.practice_reminder_candidates(now()) p where p->>'student_id' = st::text;
  perform public.finish_practice_reminder(old_id, null, 'webpush', 'sent');
  perform hp_test.ok((select status = 'failed' and failure_reason = 'claim_expired_resent' from public.practice_reminder_deliveries where id = old_id),
    'a late send after a re-claim is kept as history');
  perform public.finish_practice_reminder(again, null, 'webpush', 'failed');
  select p into c from public.practice_reminder_candidates(now()) p where p->>'student_id' = st::text;
  perform hp_test.is((c->'context'->>'sentThisWeek')::integer, base, 'it still counts as sent (the re-claim it replaces does not)');
  -- The sweep expires every lost claim. A sender finishing an expired claim as sent records it as sent, keeping the
  -- reason as history; finishing one as failed changes nothing.
  perform hp_test.as_owner();
  update public.practice_reminder_deliveries set claimed_at = clock_timestamp() - interval '20 minutes' where id = young;
  perform hp_test.as_service();
  perform hp_test.is(public.claim_practice_reminder(late, st, 'lost:late', '17:15'), true, 'a third claim');
  n := public.expire_practice_reminder_claims(clock_timestamp() + interval '20 minutes');
  perform hp_test.ok((select status = 'failed' and failure_reason = 'claim_expired' from public.practice_reminder_deliveries where id = young),
    'the third claim expired the old one');
  perform hp_test.is(n, 1, 'the sweep expires the remaining unfinished claim');
  perform hp_test.ok((select status = 'failed' and failure_reason = 'claim_expired' from public.practice_reminder_deliveries where id = late), 'swept');
  perform hp_test.is(public.expire_practice_reminder_claims(clock_timestamp() + interval '20 minutes'), 0, 'a second sweep finds none');
  perform public.finish_practice_reminder(young, null, 'fcm', 'sent');
  perform hp_test.ok((select status = 'sent' and failure_reason = 'claim_expired' and channel = 'fcm' from public.practice_reminder_deliveries where id = young),
    'an expired claim that did send is recorded as sent, with its history');
  perform hp_test.is(public.claim_practice_reminder(gen_random_uuid(), st, 'lost:young', '16:45'), false, 'and its reminder is not claimed again');
  perform public.finish_practice_reminder(late, null, null, 'failed');
  perform hp_test.ok((select status = 'failed' and failure_reason = 'claim_expired' from public.practice_reminder_deliveries where id = late),
    'an expired claim finished as failed stays failed');
  perform hp_test.as_owner();
  perform hp_test.err($q$insert into public.practice_reminder_deliveries(student_id, slot, reminder_key, status, failure_reason)
    values (current_setting('t.st')::uuid, 's', 'k', 'claimed', 'claim_expired')$q$, '23514');
end $$;

-- 5c. Partial settings: a key left out keeps its stored value.
do $$
declare st uuid := current_setting('t.adult')::uuid; r public.practice_reminder_settings;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform public.set_practice_reminders(st, '{"enabled":true,"times":["07:30","18:00"],"days":[1,3,5],"quiet_start":"22:00","quiet_end":"06:00","school_days":[2,4],"school_start":"09:00","school_end":"14:00","max_per_day":2,"max_per_week":9}');
  perform public.set_practice_reminders(st, '{"enabled":false}');
  perform hp_test.as_owner();
  select * into r from public.practice_reminder_settings where student_id = st;
  perform hp_test.is(r.enabled, false, '{"enabled":false} turns them off');
  perform hp_test.is(r.times, array['07:30','18:00'], 'and keeps the times');
  perform hp_test.is(r.days, array[1,3,5]::smallint[], 'the days');
  perform hp_test.is(r.quiet_start || '-' || r.quiet_end, '22:00-06:00', 'quiet hours');
  perform hp_test.is(r.school_days, array[2,4]::smallint[], 'school days');
  perform hp_test.is(r.school_start || '-' || r.school_end, '09:00-14:00', 'school hours');
  perform hp_test.is(r.max_per_day::text || '/' || r.max_per_week::text, '2/9', 'and the limits');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform public.set_practice_reminders(st, '{"enabled":true,"times":["19:00"],"max_per_day":1}');
  perform hp_test.as_owner();
  select * into r from public.practice_reminder_settings where student_id = st;
  perform hp_test.is(r.times, array['19:00'], 'a patch replaces what it names');
  perform hp_test.is(r.school_days, array[2,4]::smallint[], 'leaving out school_days keeps them');
  perform hp_test.is(r.school_start || '-' || r.school_end, '09:00-14:00', 'leaving out school_start / school_end keeps them');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform public.set_practice_reminders(st, '{"school_start":null,"school_end":null,"school_days":[]}');
  perform public.set_practice_reminders(st, '{"days":[6,7]}');
  perform hp_test.as_owner();
  select * into r from public.practice_reminder_settings where student_id = st;
  perform hp_test.ok(r.school_start is null and r.school_end is null and r.school_days = '{}', 'no school hours stay none when left out');
  perform hp_test.is(r.days, array[6,7]::smallint[], 'days replaced');
  perform hp_test.is(r.enabled, true, 'enabled kept when left out');
  -- A first save fills defaults for what it leaves out.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000d1');
  perform public.set_practice_reminders(current_setting('t.st2')::uuid, '{"enabled":true}');
  perform hp_test.as_owner();
  select * into r from public.practice_reminder_settings where student_id = current_setting('t.st2')::uuid;
  perform hp_test.ok(r.times = array['16:30'] and r.days = array[1,2,3,4,5,6,7]::smallint[] and r.school_start = '08:00' and r.max_per_day = 1, 'a first save uses the defaults');
end $$;

-- 6. Service-only functions are refused to every signed-in role and to anon.
do $$
declare r record; f text;
begin
  foreach f in array array['select * from public.practice_reminder_candidates(now())',
      $q$select public.claim_practice_reminder(gen_random_uuid(), gen_random_uuid(), 'k', 's')$q$,
      $q$select public.finish_practice_reminder(gen_random_uuid(), null, null, 'sent')$q$,
      'select public.retire_notification_device(gen_random_uuid())',
      'select public.snooze_practice_reminder_delivery(gen_random_uuid(), 60)',
      'select public.expire_practice_reminder_claims()',
      'select * from public.reminder_opt_out_payload()'] loop
    for r in select * from t_roles loop
      perform hp_test.as_user(r.uid);
      perform hp_test.err(f, '42501');
    end loop;
    perform hp_test.as_anon();
    perform hp_test.err(f, '42501');
  end loop;
  perform hp_test.as_owner();
  perform hp_test.ok((select bool_and(c.relrowsecurity) from pg_class c where c.oid in ('public.practice_reminder_settings'::regclass,
    'public.practice_reminder_changes'::regclass, 'public.notification_devices'::regclass, 'public.practice_reminder_deliveries'::regclass)), 'RLS on every table');
  perform hp_test.ok(not exists (select 1 from information_schema.role_table_grants where grantee = 'anon' and table_name in
    ('practice_reminder_settings', 'practice_reminder_changes', 'notification_devices', 'practice_reminder_deliveries')), 'no anon grant');
  perform hp_test.ok(not exists (select 1 from pg_proc p where p.pronamespace = 'public'::regnamespace and p.prosecdef
    and p.proname in ('set_practice_reminders', 'snooze_practice_reminders', 'report_notification_device', 'student_notification_devices',
      'practice_reminder_history', 'mark_practice_reminder_opened', 'practice_reminder_candidates', 'claim_practice_reminder',
      'finish_practice_reminder', 'retire_notification_device', 'snooze_practice_reminder_delivery', 'reminder_opt_out_payload',
      'expire_practice_reminder_claims')
    and not coalesce(p.proconfig @> array['search_path=""'], false)), 'every security definer function pins an empty search_path');
end $$;

-- 7. A student who has since left the household is not reported to anyone for an earlier change.
do $$
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.remove_household_member(current_setting('t.hh')::uuid, '20000000-0000-0000-0000-000000000051');
  perform hp_test.as_service();
  perform hp_test.is((select count(*) from public.reminder_opt_out_payload() p where p->>'student_id' = current_setting('t.st')), 0::bigint,
    'a student who left the household is not reported');
  perform hp_test.as_owner();
end $$;

\o
select format('practice_reminders: all %s assertions passed', last_value) from hp_test.assertions \gset
\echo :format
rollback;
