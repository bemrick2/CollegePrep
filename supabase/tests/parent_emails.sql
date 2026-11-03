-- CR-22 parent emails (20261102020000_parent_emails.sql): opt-in, the service-only digest and inactivity payloads,
-- and the delivery record. Tested role by role; rolled back.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql
\ir support/counted_helpers.sql
\ir support/household_roles.sql

-- The CI auth stub has no email column; Supabase Auth does.
alter table auth.users add column if not exists email text;
update auth.users set email = right(id::text, 2) || '@example.test';
insert into public.profiles(id, display_name) values ('20000000-0000-0000-0000-0000000000a1', 'Pat Parent');

-- PARENT also guards Cleo in the other household (view_progress), so one guardian spans two households.
-- Riley practised 2 days ago (3 answers) and took a progress check on another day that week (1 answer, not a
-- practice day); Ben never has; Cleo once, 20 days ago.
do $$
declare inv text; v_at timestamptz := now() - interval '2 days'; v_check timestamptz; v_bench uuid;
begin
  -- The other household is created after the first, explicitly: the summary's time zone is the earliest household's,
  -- and households created in one transaction share now().
  update public.households set created_at = created_at + interval '1 minute' where id = current_setting('t.hh2')::uuid;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000d1');
  inv := public.create_household_invitation(current_setting('t.hh2')::uuid, 'guardian', null, 72, array['view_progress']);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.accept_household_invitation(inv);
  perform hp_test.as_owner();
  insert into public.practice_attempts(student_id, question_id, presented_at, submitted_at, elapsed_ms, selected_answer, is_correct)
  select current_setting('t.st')::uuid, hp_test.q(n), v_at, v_at + make_interval(secs => n), 30000, 'A', n = 4
  from unnest(array[1, 3, 4]) n;
  insert into public.practice_attempts(student_id, question_id, presented_at, submitted_at, elapsed_ms, selected_answer, is_correct)
  values (current_setting('t.st2')::uuid, hp_test.q(1), now() - interval '20 days', now() - interval '20 days', 30000, 'B', true);
  perform set_config('t.week', (date_trunc('week', (v_at at time zone 'America/Chicago'))::date)::text, true);
  v_check := case when (v_at at time zone 'America/Chicago')::date > current_setting('t.week')::date
                  then v_at - interval '1 day' else v_at + interval '1 day' end;
  insert into public.practice_benchmarks(student_id, kind, exam_version_id, started_at, completed_at)
  values (current_setting('t.st')::uuid, 'initial', '40000000-0000-0000-0000-000000000001', v_check, v_check + interval '5 minutes')
  returning id into v_bench;
  insert into public.practice_attempts(student_id, question_id, benchmark_id, presented_at, submitted_at, elapsed_ms, selected_answer, is_correct)
  values (current_setting('t.st')::uuid, hp_test.q(6), v_bench, v_check, v_check + interval '1 minute', 30000, 'D', true);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  insert into public.weekly_practice_goals(student_id, week_start, target_questions) values (current_setting('t.st')::uuid, current_setting('t.week')::date, 10);
  perform hp_test.as_owner();
end $$;

-- 1. Opt-in: each guardian writes their own row, for a student they may view.
do $$
declare st uuid := current_setting('t.st')::uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  insert into public.alert_preferences(student_id, channel, inactivity_days, enabled, weekly_digest) values
    (st, 'email', 5, true, true), (current_setting('t.st_b')::uuid, 'email', 3, true, true),
    (current_setting('t.st2')::uuid, 'email', 3, false, true), (st, 'push', 1, true, false);
  perform hp_test.is((select count(*) from public.alert_preferences where weekly_digest), 3::bigint, 'the parent opts in for three students');
  perform hp_test.err(format($q$insert into public.alert_preferences(user_id, student_id, channel, weekly_digest)
    values ('20000000-0000-0000-0000-0000000000b1', %L, 'email', true)$q$, st), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  insert into public.alert_preferences(student_id, channel, enabled, weekly_digest) values (st, 'email', false, true);
  perform hp_test.is((select count(*) from public.alert_preferences), 1::bigint, 'the viewer sees only their own preference');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  insert into public.alert_preferences(student_id, channel, inactivity_days, enabled) values (st, 'push', 1, true);
  update public.alert_preferences set weekly_digest = true where user_id = '20000000-0000-0000-0000-0000000000a1';
  perform hp_test.as_owner();
  perform hp_test.is((select count(*) from public.alert_preferences where user_id = '20000000-0000-0000-0000-0000000000a1' and channel = 'push' and not weekly_digest),
    1::bigint, 'nobody changes another guardian''s opt-in');
  -- A guardian who cannot view the student (set_goals only), another household, an outsider: refused.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform hp_test.err(format($q$insert into public.alert_preferences(student_id, channel, weekly_digest) values (%L, 'email', true)$q$, st), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000d1');
  perform hp_test.err(format($q$insert into public.alert_preferences(student_id, channel, weekly_digest) values (%L, 'email', true)$q$, st), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.err(format($q$insert into public.alert_preferences(student_id, channel, weekly_digest) values (%L, 'email', true)$q$, st), '42501');
  perform hp_test.as_owner();
end $$;

-- 2. Only the service role may call the payload and marking functions.
do $$
declare r record; f text;
begin
  foreach f in array array[format('select * from public.weekly_digest_payload(%L)', current_setting('t.week')),
      'select * from public.inactivity_alert_payload()',
      $q$select public.mark_parent_email_sent('20000000-0000-0000-0000-0000000000a1', 'weekly_digest', '2026-01-05')$q$] loop
    for r in select * from t_roles loop
      perform hp_test.as_user(r.uid);
      perform hp_test.err(f, '42501');
    end loop;
    perform hp_test.as_anon();
    perform hp_test.err(f, '42501');
  end loop;
  perform hp_test.as_owner();
  perform hp_test.ok(not has_function_privilege('authenticated', 'public.inactivity_period_key(uuid, timestamptz)', 'execute'), 'period-key helper is internal');
end $$;

-- 3. The weekly summary: one row per opted-in guardian across households, with the dashboard's numbers.
do $$
declare week date := current_setting('t.week')::date; st uuid := current_setting('t.st')::uuid; rows jsonb; a1 jsonb; b1 jsonb; prog jsonb;
begin
  perform hp_test.as_service();
  perform set_config('request.jwt.claims', '{"role":"service_role"}', true);
  select jsonb_agg(p order by p->>'user_id') into rows from public.weekly_digest_payload(week) p;
  perform hp_test.is(current_setting('request.jwt.claims'), '{"role":"service_role"}', 'the caller''s claims are restored');
  perform hp_test.is(current_setting('request.jwt.claim.sub'), '', 'the caller''s sub is restored');
  perform hp_test.is(jsonb_array_length(rows), 2, 'two recipients: the parent and the viewer');
  a1 := rows->0; b1 := rows->1;
  perform hp_test.is(a1->>'user_id', '20000000-0000-0000-0000-0000000000a1', 'the parent first');
  perform hp_test.is(a1->>'email', 'a1@example.test', 'the parent''s own address');
  perform hp_test.is(a1->>'guardian_name', 'Pat Parent', 'the parent''s name');
  perform hp_test.is(a1->>'time_zone', 'America/Chicago', 'the time zone of the parent''s earliest household');
  perform hp_test.is((select array_agg(s->>'student_name' order by o) from jsonb_array_elements(a1->'students') with ordinality x(s, o)),
    array['Ben', 'Riley', 'Cleo'], 'all three students, from both households, in one email');
  perform hp_test.is(b1->>'email', 'b1@example.test', 'the viewer''s own address');
  perform hp_test.is((select array_agg(s->>'student_name') from jsonb_array_elements(b1->'students') s), array['Riley'], 'the viewer gets Riley only');
  perform hp_test.ok(b1::text not like '%Cleo%' and b1::text not like '%Ben%' and b1::text not like '%a1@%', 'nothing of another household or guardian leaks');
  -- Riley's numbers are the dashboard's (student_weekly_progress, as the parent).
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  prog := public.student_weekly_progress(st, week);
  perform hp_test.as_owner();
  select s into a1 from jsonb_array_elements(a1->'students') s where s->>'student_name' = 'Riley';
  perform hp_test.is((a1->>'questions_submitted')::integer, coalesce((prog->>'questions_submitted')::integer, 0), 'questions match the dashboard');
  perform hp_test.is((a1->>'questions_submitted')::integer, 4, 'four answers that week (the check counts, as on the dashboard)');
  perform hp_test.is((a1->>'goal_questions')::integer, 10, 'the weekly goal');
  perform hp_test.is((a1->>'days_practised')::integer, 1, 'one practice day: the progress check''s day is not a practice day');
  perform hp_test.is((a1->'last_check'->>'kind'), 'initial', 'the last progress check');
  perform hp_test.ok(a1->>'last_practice_at' is not null, 'last practice time');
  -- The summary shows inactivity as the dashboard does (student_inactivity(): the guardian's smallest enabled threshold
  -- on any channel, here the 1-day push alert); only the separate inactivity EMAIL uses the email preference's own.
  perform hp_test.is((a1->'inactivity'->>'threshold_days')::integer, 1, 'inactivity as on the dashboard');
  -- Refusals: not a Monday.
  perform hp_test.as_service();
  perform hp_test.err(format('select * from public.weekly_digest_payload(%L)', week + 1), '22023');
  perform hp_test.err('select * from public.weekly_digest_payload(null)', '22023');
  perform hp_test.as_owner();
end $$;

-- 4. Who is left out: a guardian who lost view_progress, an archived student, a guardian already sent that week.
do $$
declare week date := current_setting('t.week')::date; n bigint; ok boolean;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.update_member_permissions(current_setting('t.hh')::uuid, '20000000-0000-0000-0000-0000000000b1', p_view_progress => false);
  perform hp_test.as_service();
  perform hp_test.ok(not exists (select 1 from public.weekly_digest_payload(week) p where p->>'user_id' = '20000000-0000-0000-0000-0000000000b1'),
    'a guardian without view_progress gets no summary, opt-in or not');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.update_member_permissions(current_setting('t.hh')::uuid, '20000000-0000-0000-0000-0000000000b1', p_view_progress => true);
  -- Marking is idempotent: the second mark is refused, and that guardian drops out of the week.
  perform hp_test.as_service();
  perform hp_test.is(public.mark_parent_email_sent('20000000-0000-0000-0000-0000000000b1', 'weekly_digest', week::text), true, 'first mark records');
  perform hp_test.is(public.mark_parent_email_sent('20000000-0000-0000-0000-0000000000b1', 'weekly_digest', week::text), false, 'second mark is refused');
  perform hp_test.is((select count(*) from public.parent_email_deliveries where user_id = '20000000-0000-0000-0000-0000000000b1'), 1::bigint, 'one record');
  select count(*) into n from public.weekly_digest_payload(week);
  perform hp_test.is(n, 1::bigint, 'the viewer is not sent the same week again');
  perform hp_test.is((select count(*) from public.weekly_digest_payload(week - 7)), 2::bigint, 'another week is its own');
  perform hp_test.err($q$select public.mark_parent_email_sent('20000000-0000-0000-0000-0000000000b1', 'newsletter', 'x')$q$, '23514');
  -- The sender's retry path deletes its own record (service role only).
  delete from public.parent_email_deliveries where user_id = '20000000-0000-0000-0000-0000000000b1' and kind = 'weekly_digest' and period_key = (week - 7)::text;
  perform hp_test.as_owner();
  update public.students set archived_at = now() where id = current_setting('t.st_b')::uuid;
  perform hp_test.as_service();
  perform hp_test.ok(not exists (select 1 from public.weekly_digest_payload(week) p, jsonb_array_elements(p->'students') s
    where s->>'student_name' = 'Ben'), 'an archived student is left out');
  perform hp_test.as_owner();
  update public.students set archived_at = null where id = current_setting('t.st_b')::uuid;
end $$;

-- 4b. The two permission checks, each on its own.
do $$
declare week date := current_setting('t.week')::date; rows jsonb;
begin
  -- Per student (can_view_student, as the guardian): the parent loses view_progress in the other household only. They
  -- are still a recipient through the first household, but Cleo leaves their summary.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000d1');
  perform public.update_member_permissions(current_setting('t.hh2')::uuid, '20000000-0000-0000-0000-0000000000a1', p_view_progress => false);
  perform hp_test.as_service();
  select p into rows from public.weekly_digest_payload(week) p where p->>'user_id' = '20000000-0000-0000-0000-0000000000a1';
  perform hp_test.is((select array_agg(s->>'student_name' order by o) from jsonb_array_elements(rows->'students') with ordinality x(s, o)),
    array['Ben', 'Riley'], 'a student the guardian may no longer view leaves the summary');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000d1');
  perform public.update_member_permissions(current_setting('t.hh2')::uuid, '20000000-0000-0000-0000-0000000000a1', p_view_progress => true);
  -- Per recipient (a guardian with view_progress): the linked student may opt in about themselves (they can view
  -- their own data), but is no guardian, so gets no summary.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  insert into public.alert_preferences(student_id, channel, enabled, weekly_digest) values (current_setting('t.st')::uuid, 'email', false, true);
  perform hp_test.as_service();
  perform hp_test.ok(not exists (select 1 from public.weekly_digest_payload(week) p where p->>'user_id' = '20000000-0000-0000-0000-000000000051'),
    'the student is not a recipient of their own summary');
  perform hp_test.as_owner();
  delete from public.alert_preferences where user_id = '20000000-0000-0000-0000-000000000051';
end $$;

-- 5. Inactivity: the email preference's own threshold, once per stretch, with a key independent of session settings.
do $$
declare rows jsonb; k1 text; k2 text; ben uuid := current_setting('t.st_b')::uuid;
begin
  perform hp_test.as_service();
  perform set_config('request.jwt.claims', '{"role":"service_role","n":1}', true);
  select jsonb_agg(p) into rows from public.inactivity_alert_payload() p;
  perform hp_test.is(current_setting('request.jwt.claims'), '{"role":"service_role","n":1}', 'inactivity: the caller''s claims are restored');
  perform hp_test.is(current_setting('request.jwt.claim.sub'), '', 'inactivity: the caller''s sub is restored');
  -- Riley: email alert at 5 days (2 days without practice: not due), push alert at 1 day (not an email). Cleo: email
  -- alert off. Ben: never practised, email alert at 3 days. CO and the viewer have no enabled email alert.
  perform hp_test.is(jsonb_array_length(rows), 1, 'one alert is due');
  perform hp_test.is(rows->0->>'student_name', 'Ben', 'for Ben');
  perform hp_test.is(rows->0->>'user_id', '20000000-0000-0000-0000-0000000000a1', 'to the parent');
  perform hp_test.is(rows->0->>'email', 'a1@example.test', 'at the parent''s own address');
  perform hp_test.is(rows->0->>'period_key', ben::text || ':never', 'keyed on the stretch');
  perform hp_test.is((rows->0->>'threshold_days')::integer, 3, 'at the email preference''s threshold');
  perform hp_test.is(public.mark_parent_email_sent('20000000-0000-0000-0000-0000000000a1', 'inactivity', ben::text || ':never'), true, 'sent');
  perform hp_test.is((select count(*) from public.inactivity_alert_payload()), 0::bigint, 'never repeated for the same stretch');
  -- Ben practises once, long ago: a new stretch, a new key, in UTC whatever the session's time zone.
  perform hp_test.as_owner();
  insert into public.practice_attempts(student_id, question_id, presented_at, submitted_at, elapsed_ms, selected_answer, is_correct)
  values (ben, hp_test.q(1), '2026-10-20 15:04:05.123456+00', '2026-10-20 15:04:05.123456+00', 1000, 'B', true);
  perform hp_test.as_service();
  perform set_config('timezone', 'Asia/Tokyo', true);
  select p->>'period_key' into k1 from public.inactivity_alert_payload() p;
  perform set_config('timezone', 'America/Los_Angeles', true);
  select p->>'period_key' into k2 from public.inactivity_alert_payload() p;
  perform set_config('timezone', 'UTC', true);
  perform hp_test.is(k1, ben::text || ':2026-10-20T15:04:05.123456Z', 'a new stretch gets a UTC ISO key');
  perform hp_test.is(k2, k1, 'the key does not depend on the session time zone');
  -- The alert follows view_progress too.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.update_member_permissions(current_setting('t.hh')::uuid, '20000000-0000-0000-0000-0000000000a1', p_view_progress => false);
  perform hp_test.as_service();
  perform hp_test.is((select count(*) from public.inactivity_alert_payload()), 0::bigint, 'no alert without view_progress');
  perform hp_test.as_owner();
  update public.household_members set can_view_progress = true where user_id = '20000000-0000-0000-0000-0000000000a1';
end $$;

-- 6. The delivery record: each guardian reads their own kind / period / time; nobody writes it from a client.
do $$
declare r record; n bigint;
begin
  for r in select * from t_roles loop
    perform hp_test.as_user(r.uid);
    select count(*) into n from public.parent_email_deliveries;
    perform hp_test.is(n, case r.who when 'PARENT' then 1::bigint when 'VIEWER' then 1::bigint else 0::bigint end, r.who || ' reads only their own deliveries');
    perform hp_test.err('select user_id from public.parent_email_deliveries', '42501');
    perform hp_test.err($q$insert into public.parent_email_deliveries(user_id, kind, period_key) values (auth.uid(), 'weekly_digest', '2030-01-07')$q$, '42501');
    perform hp_test.err($q$delete from public.parent_email_deliveries$q$, '42501');
    perform hp_test.err($q$update public.parent_email_deliveries set sent_at = now()$q$, '42501');
  end loop;
  perform hp_test.as_anon();
  perform hp_test.err('select kind from public.parent_email_deliveries', '42501');
  perform hp_test.as_owner();
  -- Retention (decision #5): deleting an account de-identifies its email records rather than deleting them.
  delete from auth.users where id = '20000000-0000-0000-0000-0000000000b1';
  perform hp_test.is((select count(*) from public.parent_email_deliveries where user_id is null and kind = 'weekly_digest'), 1::bigint,
    'a deleted account''s email record is kept, de-identified');
  perform hp_test.ok((select relrowsecurity from pg_class where oid = 'public.parent_email_deliveries'::regclass), 'RLS is on');
  perform hp_test.ok(not has_table_privilege('anon', 'public.parent_email_deliveries', 'select,insert,update,delete'), 'anon has no grant');
end $$;

\o
select format('parent_emails: all %s assertions passed', last_value) from hp_test.assertions \gset
\echo :format
rollback;
