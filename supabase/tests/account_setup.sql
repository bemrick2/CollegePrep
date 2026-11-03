-- CR-26 setup on the account (20261102010000_account_setup.sql), tested role by role against tables and RPCs.
-- Every restricted operation is attempted by every role; an unauthorized success fails the test. Rolled back.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql
\ir support/counted_helpers.sql
\ir support/household_roles.sql

-- 1. Planning preferences: the new columns follow the existing rule (set_goals guardians; the student only when
--    independent or outside a household).
do $$
declare r record; st uuid := current_setting('t.st')::uuid; n integer; allowed boolean;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  insert into public.student_planning_preferences(student_id, exam_family, goals, daily_minutes, exam_intent, planned_test_date, study_days)
  values (st, 'sat', array['raise_score'], 30, 'both', '2027-03-06', array[2,4]::smallint[]);
  perform hp_test.is((select daily_minutes from public.student_planning_preferences where student_id = st), 30, 'a 30-minute day is stored');
  -- Values the schema refuses, whoever writes.
  perform hp_test.err(format($q$update public.student_planning_preferences set daily_minutes = 31 where student_id = %L$q$, st), '23514');
  perform hp_test.err(format($q$update public.student_planning_preferences set daily_minutes = 4 where student_id = %L$q$, st), '23514');
  perform hp_test.err(format($q$update public.student_planning_preferences set exam_intent = 'gre' where student_id = %L$q$, st), '23514');
  perform hp_test.err(format($q$update public.student_planning_preferences set study_days = '{}' where student_id = %L$q$, st), '23514');
  perform hp_test.err(format($q$update public.student_planning_preferences set study_days = '{1,1}' where student_id = %L$q$, st), '23514');
  perform hp_test.err(format($q$update public.student_planning_preferences set study_days = '{0,3}' where student_id = %L$q$, st), '23514');
  perform hp_test.err(format($q$update public.student_planning_preferences set study_days = '{1,2,3,4,5,6,7,8}' where student_id = %L$q$, st), '23514');
  perform hp_test.err(format($q$update public.student_planning_preferences set study_days = array[1,null]::smallint[] where student_id = %L$q$, st), '23514');
  perform hp_test.err(format($q$update public.student_planning_preferences set planned_test_date = '1999-12-31' where student_id = %L$q$, st), '23514');
  for r in select * from t_roles loop
    allowed := r.who in ('PARENT', 'CO', 'GOALS');
    perform hp_test.as_user(r.uid);
    update public.student_planning_preferences set study_days = array[1,3,5]::smallint[], exam_intent = 'act'
    where student_id = st;
    get diagnostics n = row_count;
    perform hp_test.is(n > 0, allowed, r.who || ' writes study_days / exam_intent');
    perform hp_test.as_owner();
    update public.student_planning_preferences set study_days = array[2,4]::smallint[], exam_intent = 'both' where student_id = st;
  end loop;
  -- Who reads them: the student and view_progress guardians, and the set_goals guardians who write them.
  for r in select * from t_roles loop
    perform hp_test.as_user(r.uid);
    select count(*) into n from public.student_planning_preferences where student_id = st and study_days = array[2,4]::smallint[];
    perform hp_test.is(n, case when r.who in ('PARENT', 'CO', 'VIEWER', 'GOALS', 'STUDENT') then 1 else 0 end, r.who || ' reads the plan');
  end loop;
  perform hp_test.as_anon();
  perform hp_test.err(format($q$select study_days from public.student_planning_preferences where student_id = %L$q$, st), '42501');
  -- A student outside any household writes their own plan.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  insert into public.student_planning_preferences(student_id, exam_family, goals, daily_minutes, exam_intent, planned_test_date, study_days)
  values (current_setting('t.solo')::uuid, 'sat', '{}', 15, 'sat', null, array[2,4,6]::smallint[]);
  perform hp_test.is((select study_days from public.student_planning_preferences where student_id = current_setting('t.solo')::uuid),
    array[2,4,6]::smallint[], 'a household-less student saves their own study days');
  perform hp_test.as_owner();
end $$;

-- 2. Sessions of 5 to 30 minutes.
do $$
declare st uuid := current_setting('t.st')::uuid; s uuid; n integer;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  s := public.start_practice_session(st, 30);
  perform hp_test.is((select target_minutes from public.practice_sessions where id = s), 30, 'a 30-minute session starts');
  perform hp_test.ok((select count(*) from public.practice_session_items where session_id = s) > 0, 'the 30-minute session has items');
  perform hp_test.err(format('select public.start_practice_session(%L, 31)', st), '22023', '%5 to 30%');
  perform hp_test.err(format('select public.start_practice_session(%L, 4)', st), '22023');
  perform hp_test.err(format('select public.start_practice_session(%L, null)', st), '22023');
  perform hp_test.err(format('insert into public.practice_sessions(student_id, target_minutes) values (%L, 20)', st), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  select count(*) into n from public.recommend_practice_set(st, 30);
  perform hp_test.ok(n > 0, 'a viewing guardian previews a 30-minute set');
  perform hp_test.err(format('select * from public.recommend_practice_set(%L, 31)', st), '22023');
  -- Guardians still cannot practise as the student.
  perform hp_test.err(format('select public.start_practice_session(%L, 20)', st), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.err(format('select * from public.recommend_practice_set(%L, 20)', st), '42501');
  perform hp_test.as_owner();
  perform hp_test.err(format('insert into public.practice_sessions(student_id, target_minutes) values (%L, 31)', st), '23514');
end $$;

-- 3. Practice-test scores: clients add them as they add self-reported scores; never official, never in official scores.
do $$
declare r record; st uuid := current_setting('t.st')::uuid; allowed boolean; ok boolean; n bigint;
  ev uuid := '40000000-0000-0000-0000-000000000001';
begin
  for r in select * from t_roles loop
    allowed := r.who in ('PARENT', 'CO', 'MANAGER', 'STUDENT');
    perform hp_test.as_user(r.uid);
    begin
      insert into public.student_test_scores(student_id, exam_version_id, test_date, composite, score_source)
      values (st, ev, '2026-06-06', 1180, 'practice_test');
      ok := true;
    exception when insufficient_privilege then ok := false;
    end;
    perform hp_test.is(ok, allowed, r.who || ' adds a practice-test score');
  end loop;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.err(format($q$insert into public.student_test_scores(student_id, exam_version_id, test_date, composite, score_source)
    values (%L, %L, '2026-06-06', 1500, 'official')$q$, st, ev), '42501');
  perform hp_test.err(format($q$insert into public.student_test_scores(student_id, exam_version_id, test_date, composite, score_source)
    values (%L, %L, '2026-06-06', 1500, 'practice_estimate')$q$, st, ev), '42501');
  -- Entered by someone else: not the student's to delete.
  insert into public.student_test_scores(student_id, exam_version_id, test_date, composite, score_source)
  values (st, ev, '2026-07-07', 1200, 'practice_test');
  perform hp_test.as_owner();
  perform hp_test.err(format($q$insert into public.student_test_scores(student_id, exam_version_id, test_date, composite, score_source)
    values (%L, %L, '2026-06-06', 1500, 'practice')$q$, st, ev), '23514');
  perform hp_test.is((select count(*) from public.student_test_scores where student_id = st and score_source = 'practice_test'), 5::bigint,
    'four writers plus one more score');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.is((select count(*) from public.student_official_scores where student_id = st), 0::bigint,
    'practice-test scores never appear as official');
  perform hp_test.is((select count(*) from public.student_test_scores where student_id = st and score_source = 'practice_test'), 5::bigint,
    'a viewing guardian reads every practice-test score');
  delete from public.student_test_scores where student_id = st and score_source = 'practice_test';
  get diagnostics n = row_count;
  perform hp_test.is(n, 1::bigint, 'the parent deletes only the score they entered');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.is((select count(*) from public.student_test_scores where student_id = st), 0::bigint, 'an outsider reads no scores');
  perform hp_test.as_owner();
end $$;

-- 4. Setup progress: written only through update_setup_progress, by the student's own login or a guardian with
--    manage_students or set_goals.
do $$
declare r record; st uuid := current_setting('t.st')::uuid; allowed boolean; ok boolean; n bigint;
begin
  for r in select * from t_roles loop
    allowed := r.who in ('PARENT', 'CO', 'GOALS', 'MANAGER', 'STUDENT');
    perform hp_test.as_user(r.uid);
    begin
      perform public.update_setup_progress(st, '{"starting_point_answered": true}');
      ok := true;
    exception when insufficient_privilege then ok := false;
    end;
    perform hp_test.is(ok, allowed, r.who || ' records setup progress');
  end loop;
  perform hp_test.as_anon();
  perform hp_test.err(format($q$select public.update_setup_progress(%L, '{"setup_completed": true}')$q$, st), '42501');
  perform hp_test.err(format('select setup_completed_at from public.student_setup_progress where student_id = %L', st), '42501');
  -- Direct writes are refused for every signed-in role, whatever their household permissions.
  for r in select * from t_roles loop
    perform hp_test.as_user(r.uid);
    perform hp_test.err(format($q$insert into public.student_setup_progress(student_id, setup_completed_at) values (%L, now())$q$,
      current_setting('t.st_b')), '42501');
    perform hp_test.err(format('update public.student_setup_progress set setup_completed_at = null where student_id = %L', st), '42501');
    perform hp_test.err(format('delete from public.student_setup_progress where student_id = %L', st), '42501');
  end loop;
  -- Readers: anyone who may view the student, and those who may write it.
  for r in select * from t_roles loop
    perform hp_test.as_user(r.uid);
    select count(*) into n from public.student_setup_progress where student_id = st;
    perform hp_test.is(n, case when r.who in ('OTHER', 'OUTSIDER') then 0::bigint else 1::bigint end, r.who || ' reads setup progress');
    -- Who last wrote it (a user id) is not exposed.
    perform hp_test.err(format('select updated_by from public.student_setup_progress where student_id = %L', st), '42501');
  end loop;
  perform hp_test.as_service();
  perform hp_test.is((select count(*) from public.student_setup_progress where student_id = st), 1::bigint, 'the service role reads setup progress');
  perform hp_test.as_owner();
end $$;

-- 5. Setup progress semantics: completion is kept, the schedule is set and cleared only when named, input is checked.
do $$
declare st uuid := current_setting('t.st')::uuid; v_done timestamptz; v_sp timestamptz; v_at timestamptz := date_trunc('second', now() + interval '3 days');
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.update_setup_progress(st, '{"setup_completed": false, "starting_point_answered": false}');
  perform hp_test.ok((select setup_completed_at is null from public.student_setup_progress where student_id = st), 'false records nothing');
  v_sp := (select starting_point_answered_at from public.student_setup_progress where student_id = st);
  perform hp_test.ok(v_sp is not null, 'the starting point answered earlier is kept');
  perform public.update_setup_progress(st, jsonb_build_object('setup_completed', true, 'benchmark_scheduled_for', v_at));
  v_done := (select setup_completed_at from public.student_setup_progress where student_id = st);
  perform hp_test.ok(v_done is not null, 'the student finishes setup');
  perform hp_test.is((select benchmark_scheduled_for from public.student_setup_progress where student_id = st), v_at, 'the benchmark is scheduled');
  -- Later writes, from another device or another person, never undo completion or move its time.
  perform public.update_setup_progress(st, '{"setup_completed": false}');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.update_setup_progress(st, '{"setup_completed": true, "starting_point_answered": true}');
  perform hp_test.as_owner();
  perform hp_test.is((select setup_completed_at from public.student_setup_progress where student_id = st), v_done, 'completion time is kept');
  perform hp_test.is((select starting_point_answered_at from public.student_setup_progress where student_id = st), v_sp, 'starting-point time is kept');
  perform hp_test.is((select benchmark_scheduled_for from public.student_setup_progress where student_id = st), v_at,
    'a patch without the schedule leaves it');
  perform hp_test.is((select count(*) from public.student_setup_progress where student_id = st), 1::bigint, 'one row per student');
  perform hp_test.is((select updated_by from public.student_setup_progress where student_id = st),
    '20000000-0000-0000-0000-0000000000a1'::uuid, 'the last writer is recorded server-side');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.update_setup_progress(st, '{"benchmark_scheduled_for": null}');
  perform hp_test.ok((select benchmark_scheduled_for is null from public.student_setup_progress where student_id = st), 'a named null clears the schedule');
  perform hp_test.err(format($q$select public.update_setup_progress(%L, jsonb_build_object('benchmark_scheduled_for', now() + interval '61 days'))$q$, st), '22023', '%60 days%');
  perform hp_test.err(format($q$select public.update_setup_progress(%L, '{"high_school": "Central"}')$q$, st), '22023', '%Unknown%');
  perform hp_test.err(format($q$select public.update_setup_progress(%L, jsonb_build_object('benchmark_scheduled_for', now() - interval '25 hours'))$q$, st), '22023', '%past%');
  perform public.update_setup_progress(st, jsonb_build_object('benchmark_scheduled_for', now() - interval '23 hours'));
  perform hp_test.ok((select benchmark_scheduled_for = now() - interval '23 hours' from public.student_setup_progress where student_id = st),
    'up to a day in the past is accepted (a check scheduled for earlier today)');
  perform hp_test.err(format($q$select public.update_setup_progress(%L, '{"setup_completed": "yes"}')$q$, st), '22023');
  perform hp_test.err(format($q$select public.update_setup_progress(%L, '{"benchmark_scheduled_for": 5}')$q$, st), '22023');
  perform hp_test.err(format($q$select public.update_setup_progress(%L, '{"benchmark_scheduled_for": "soon"}')$q$, st), '22007');
  perform hp_test.err(format($q$select public.update_setup_progress(%L, '[true]')$q$, st), '22023');
  perform hp_test.err(format($q$select public.update_setup_progress(%L, null)$q$, st), '22023');
  perform hp_test.err($q$select public.update_setup_progress(null, '{}')$q$, '42501');
  perform hp_test.err($q$select public.update_setup_progress(gen_random_uuid(), '{}')$q$, '42501');
  -- A student outside any household finishes their own setup; nobody else can.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.update_setup_progress(current_setting('t.solo')::uuid, '{"setup_completed": true, "starting_point_answered": true}');
  perform hp_test.is((select count(*) from public.student_setup_progress where student_id = current_setting('t.solo')::uuid and setup_completed_at is not null),
    1::bigint, 'a household-less student finishes setup');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.err(format($q$select public.update_setup_progress(%L, '{"setup_completed": true}')$q$, current_setting('t.solo')), '42501');
  perform hp_test.is((select count(*) from public.student_setup_progress where student_id = current_setting('t.solo')::uuid), 0::bigint,
    'a guardian of another household reads none of it');
  -- An archived student's setup is closed for everyone.
  update public.students set archived_at = now() where id = current_setting('t.st_b')::uuid;
  perform hp_test.err(format($q$select public.update_setup_progress(%L, '{"setup_completed": true}')$q$, current_setting('t.st_b')), '42501');
  perform hp_test.as_owner();
end $$;

-- 5b. The first time is kept, shown with times that differ (now() is constant inside this transaction).
do $$
declare st uuid := current_setting('t.st')::uuid;
begin
  perform hp_test.as_owner();
  update public.student_setup_progress set setup_completed_at = '2026-01-05 10:00+00', starting_point_answered_at = '2026-01-04 09:00+00'
  where student_id = st;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.update_setup_progress(st, '{"setup_completed": true, "starting_point_answered": true}');
  perform hp_test.as_owner();
  perform hp_test.is((select setup_completed_at from public.student_setup_progress where student_id = st), '2026-01-05 10:00+00'::timestamptz,
    'setup_completed_at keeps its first value');
  perform hp_test.is((select starting_point_answered_at from public.student_setup_progress where student_id = st), '2026-01-04 09:00+00'::timestamptz,
    'starting_point_answered_at keeps its first value');
  perform hp_test.ok((select updated_at = now() from public.student_setup_progress where student_id = st), 'the write itself is recorded');
end $$;

-- 6. Privileges: the function is the only write path; no anon grants anywhere.
do $$
begin
  perform hp_test.ok(not has_function_privilege('anon', 'public.update_setup_progress(uuid, jsonb)', 'execute'), 'anon cannot call update_setup_progress');
  perform hp_test.ok(not has_table_privilege('anon', 'public.student_setup_progress', 'select'), 'anon has no table grant');
  perform hp_test.ok(not has_table_privilege('authenticated', 'public.student_setup_progress', 'insert,update,delete'), 'no client write grant');
  perform hp_test.ok((select relrowsecurity from pg_class where oid = 'public.student_setup_progress'::regclass), 'RLS is on');
  perform hp_test.ok((select prosecdef and proconfig @> array['search_path=""'] from pg_proc
    where oid = 'public.update_setup_progress(uuid, jsonb)'::regprocedure), 'security definer with an empty search_path');
end $$;

\o
select format('account_setup: all %s assertions passed', last_value) from hp_test.assertions \gset
\echo :format
rollback;
