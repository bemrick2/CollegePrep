-- CR-23 part 2 (#218 B1): seen_before on served practice items, and first-answer skill metrics (repeats never count).
-- Rolled back. Run with psql -v ON_ERROR_STOP=1.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql
-- One row per item of a session: "q<n>:<seen_before>", in position order.
create function hp_test.session_seen(p_session uuid) returns text language sql as $f$
  select string_agg('q' || right(question_id::text, 1) || ':' || seen_before, ',' order by right(question_id::text, 1))
  from public.practice_session_items where session_id = p_session
$f$;
grant execute on function hp_test.session_seen(uuid) to authenticated;
grant usage on schema hp_test to service_role;
grant execute on all functions in schema hp_test to service_role;

-- PARENT a1 (creator), GOALS c1 (set_goals only, no view_progress), STUDENT 51 (linked); OTHER guardian b1 with
-- STUDENT2 52; OUTSIDER 99.
insert into auth.users(id) values ('20000000-0000-0000-0000-0000000000c1');
do $$
declare hh uuid; st uuid; hh2 uuid; st2 uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Seen', 'America/Chicago');
  st := public.add_student(hh, 'Seen Student');
  perform set_config('t.st', st::text, true);
  perform set_config('t.inv', public.create_household_invitation(hh, 'student', st), true);
  perform set_config('t.inv_goals', public.create_household_invitation(hh, 'guardian', null, 72, array['set_goals']), true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform public.accept_household_invitation(current_setting('t.inv_goals'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  hh2 := public.create_household('Other', 'America/Chicago');
  st2 := public.add_student(hh2, 'Other Student');
  perform set_config('t.st2', st2::text, true);
  perform set_config('t.inv2', public.create_household_invitation(hh2, 'student', st2), true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.accept_household_invitation(current_setting('t.inv2'));
  perform hp_test.as_owner();
end $$;

-- seen_before on served sessions.
do $$
declare st uuid := current_setting('t.st')::uuid; st2 uuid := current_setting('t.st2')::uuid; s uuid; a uuid; v_at timestamptz;
begin
  perform hp_test.check(has_column_privilege('authenticated', 'public.practice_session_items', 'seen_before', 'SELECT'), 'clients read seen_before');
  perform hp_test.check(not has_column_privilege('authenticated', 'public.practice_session_items', 'seen_before', 'INSERT,UPDATE'), 'clients never write it');
  perform hp_test.check(not has_column_privilege('anon', 'public.practice_session_items', 'seen_before', 'SELECT'), 'anon reads nothing');

  -- A new student: nothing was seen before.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  s := public.start_practice_session(st, 15);
  perform hp_test.eq(hp_test.session_seen(s), 'q1:false,q2:false,q3:false,q4:false,q6:false,q7:false,q8:false', 'first session: all fresh');
  perform hp_test.eq((select count(*) from public.practice_session_items where session_id = s and last_seen is not null), 0::bigint, 'no last_seen');
  -- q1 answered, q2 opened and abandoned, q3 skipped: all three were shown.
  perform public.submit_practice_attempt(public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000001', s), 'A');
  perform public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000002', s);
  perform public.submit_practice_attempt(public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000003', s), null, p_skipped => true);
  perform public.end_practice_session(s);
  s := public.start_practice_session(st, 15);
  perform set_config('t.s2', s::text, true);
  perform hp_test.eq(hp_test.session_seen(s), 'q1:true,q2:true,q3:true,q4:false,q6:false,q7:false,q8:false', 'answered, abandoned and skipped items are seen');
  select max(presented_at) into v_at from public.practice_attempts where student_id = st and question_id = '30000000-0000-0000-0000-000000000001';
  perform hp_test.eq((select last_seen from public.practice_session_items where session_id = s and question_id = '30000000-0000-0000-0000-000000000001'), v_at, 'last_seen is the last presentation');
  -- Another student's history is not this student's.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  s := public.start_practice_session(st2, 15);
  perform hp_test.eq(hp_test.session_seen(s), 'q1:false,q2:false,q3:false,q4:false,q6:false,q7:false,q8:false', 'per student');
  perform hp_test.as_owner();
end $$;

-- Assignment to a check is exposure: an item a check assigned, then returned to practice, is served as seen.
do $$
declare st uuid := current_setting('t.st')::uuid; b uuid; s uuid;
begin
  perform hp_test.as_owner();
  update public.practice_questions set pool = 'assessment' where id in ('30000000-0000-0000-0000-000000000004', '30000000-0000-0000-0000-000000000008');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  b := public.start_benchmark(st, 'initial', '40000000-0000-0000-0000-000000000001');
  perform set_config('t.bm', b::text, true);
  perform hp_test.eq((select count(*) from public.practice_benchmark_items where benchmark_id = b), 2::bigint, 'the check assigned q4 and q8');
  -- q4 is answered in the check (correct); q8 is never attempted.
  perform public.submit_practice_attempt(public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000004', p_benchmark => b), 'A');
  perform public.complete_benchmark(b);
  s := public.start_practice_session(st, 15);
  perform hp_test.eq(hp_test.session_seen(s), 'q1:true,q2:true,q3:true,q6:false,q7:false', 'reserved items stay out of practice');
  perform hp_test.as_owner();
  update public.practice_questions set pool = 'practice' where id in ('30000000-0000-0000-0000-000000000004', '30000000-0000-0000-0000-000000000008');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.end_practice_session(s);
  s := public.start_practice_session(st, 15);
  perform set_config('t.s3', s::text, true);
  perform hp_test.eq(hp_test.session_seen(s), 'q1:true,q2:true,q3:true,q4:true,q6:false,q7:false,q8:true', 'a check''s assigned items are seen, attempted or not');
  perform hp_test.as_owner();
end $$;

-- Served values are frozen and the trigger decides them, whatever an insert says.
do $$
declare st uuid := current_setting('t.st')::uuid; s uuid;
begin
  perform hp_test.as_owner();
  insert into public.practice_sessions(student_id, target_minutes) values (st, 10) returning id into s;
  insert into public.practice_session_items(session_id, position, question_id, reason, seen_before, last_seen) values
    (s, 1, '30000000-0000-0000-0000-000000000006', 'review', true, now()),
    (s, 2, '30000000-0000-0000-0000-000000000001', 'review', false, null);
  perform hp_test.eq(hp_test.session_seen(s), 'q1:true,q6:false', 'inserted values are recomputed');
  perform hp_test.eq((select last_seen from public.practice_session_items where session_id = s and position = 1), null::timestamptz, 'and last_seen with them');
  -- Answering q6 later doesn't change what an earlier session served.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.submit_practice_attempt(public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000006'), 'D');
  perform hp_test.eq(hp_test.session_seen(s), 'q1:true,q6:false', 'served values are frozen');
  perform hp_test.as_owner();
end $$;

-- Who reads served items: the student and view_progress guardians; nobody writes them.
do $$
declare s uuid := current_setting('t.s3')::uuid; who record;
begin
  for who in select * from (values ('20000000-0000-0000-0000-000000000051'::uuid, 'STUDENT', 7::bigint),
      ('20000000-0000-0000-0000-0000000000a1'::uuid, 'PARENT', 7::bigint), ('20000000-0000-0000-0000-0000000000c1'::uuid, 'GOALS', 0::bigint),
      ('20000000-0000-0000-0000-0000000000b1'::uuid, 'OTHER guardian', 0::bigint), ('20000000-0000-0000-0000-000000000052'::uuid, 'OTHER student', 0::bigint),
      ('20000000-0000-0000-0000-000000000099'::uuid, 'OUTSIDER', 0::bigint)) v(uid, label, want) loop
    perform hp_test.as_user(who.uid);
    perform hp_test.eq((select count(*) from public.practice_session_items where session_id = s), who.want, who.label || ' reads served items');
    perform hp_test.expect_error(format('update public.practice_session_items set seen_before = false where session_id = %L', s), '42501');
    perform hp_test.expect_error(format($q$insert into public.practice_session_items(session_id, position, question_id, reason) values (%L, 99, '30000000-0000-0000-0000-000000000005', 'x')$q$, s), '42501');
  end loop;
  perform hp_test.as_anon();
  perform hp_test.expect_error('select seen_before from public.practice_session_items', '42501');
  perform hp_test.as_owner();
end $$;

-- The recommender ranks by the same exposure rule: q8 (assigned to a check, never attempted, returned to practice) is not
-- fresh. qN, a never-seen item of the same skill, comes first, though by id alone q8 would (attempts-only ranking).
do $$
declare st uuid := current_setting('t.st')::uuid; p8 integer; pn integer; s uuid;
begin
  perform hp_test.as_owner();
  insert into public.practice_questions(id, exam_version_id, question_type_id, section, difficulty, difficulty_label, stem, choices,
    answer_format, accepted_answers, expected_time_seconds, status, license, origin)
  values ('3b000000-0000-0000-0000-000000000001', '40000000-0000-0000-0000-000000000001', '41000000-0000-0000-0000-000000000001', 'math',
    2, 'medium', 'Fresh data item', '["A","B","C","D"]', 'choice', '["A"]', 60, 'published', 'original-owned', 'authored');
  insert into public.practice_question_skills(question_id, skill_id, is_primary)
    values ('3b000000-0000-0000-0000-000000000001', '42000000-0000-0000-0000-00000000000c', true);
  perform public.approve_practice_question('3b000000-0000-0000-0000-000000000001', 'test fixture');
  perform hp_test.eq((select count(*) from public.practice_attempts where student_id = st and question_id = '30000000-0000-0000-0000-000000000008'), 0::bigint,
    'q8 was never attempted');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  select item_position into p8 from public.recommend_practice_set(st, 15) where question_id = '30000000-0000-0000-0000-000000000008';
  select item_position into pn from public.recommend_practice_set(st, 15) where question_id = '3b000000-0000-0000-0000-000000000001';
  perform hp_test.check(pn is not null and p8 is not null and pn < p8, format('a never-seen item ranks before a check-assigned one (fresh %s, assigned %s)', pn, p8));
  s := public.start_practice_session(st, 15);
  perform hp_test.check((select position from public.practice_session_items where session_id = s and question_id = '3b000000-0000-0000-0000-000000000001')
    < (select position from public.practice_session_items where session_id = s and question_id = '30000000-0000-0000-0000-000000000008'), 'sessions follow the same order');
  perform hp_test.eq((select string_agg(seen_before::text, ',' order by position) from public.practice_session_items where session_id = s
    and question_id in ('3b000000-0000-0000-0000-000000000001', '30000000-0000-0000-0000-000000000008')), 'false,true', 'and mark it seen');
  perform public.end_practice_session(s);
  perform hp_test.as_owner();
end $$;

-- First answers. History so far (student 51): q1 wrong (A), q2 opened, q3 skipped, q4 right in its own check (fresh),
-- q8 assigned to that check and never attempted, q6 right. Now: q1 right (a repeat), q2 right (shown before), q3 right
-- (shown before), q8 right (assigned before), q7 right (fresh).
do $$
declare st uuid := current_setting('t.st')::uuid; got text;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.submit_practice_attempt(public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000001'), 'B');
  perform public.submit_practice_attempt(public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000002'), '0.5');
  perform public.submit_practice_attempt(public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000003'), 'C');
  perform public.submit_practice_attempt(public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000008'), 'B');
  perform public.submit_practice_attempt(public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000007'), 'A');
  -- linear_equations: q1 wrong, q1 right, q2 right, q6 right -> 4 answers, 3 right; first answers q1 (wrong), q6 (right).
  -- inference: q3 right (skipped first, not a first answer), q7 right (fresh). ratios: q4 right in its check (fresh).
  -- data_analysis: q8 right after its check assignment (not a first answer).
  select string_agg(skill_key || ':' || attempts || '/' || correct || ':' || first_answers || ':' || coalesce(first_answer_accuracy::text, 'null'), ',' order by skill_key)
    into got from public.student_skill_estimates(st);
  perform hp_test.eq(got, 'data_analysis:1/1:0:null,inference:2/2:1:1.0000,linear_equations:4/3:2:0.5000,ratios:1/1:1:1.0000',
    'first answers exclude repeats, abandoned and skipped first showings, and check-assigned items; a fresh check answer counts');
  -- A correct repeat raises accuracy but never first-answer accuracy.
  perform public.submit_practice_attempt(public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000001'), 'B');
  select string_agg(skill_key || ':' || accuracy || ':' || first_answer_accuracy, ',') into got
    from public.student_skill_estimates(st) where skill_key = 'linear_equations';
  perform hp_test.eq(got, 'linear_equations:0.8000:0.5000', 'a repeat is not improvement');
  -- The existing columns are exactly what they were (skill_estimates_internal, same order).
  select string_agg(row(skill_id, skill_key, section, attempts, correct, accuracy, median_elapsed_ms, pacing_ratio, knowledge_weak, pacing_weak)::text, ';')
    into got from public.student_skill_estimates(st);
  perform hp_test.as_owner();
  perform hp_test.eq((select string_agg(row(e.skill_id, e.skill_key, e.section, e.attempts, e.correct, e.accuracy, e.median_elapsed_ms, e.pacing_ratio,
        e.knowledge_weak, e.pacing_weak)::text, ';' order by e.section, e.skill_key) from public.skill_estimates_internal(st) e),
    got, 'existing columns unchanged');
  perform hp_test.eq(pg_get_function_result('public.student_skill_estimates(uuid)'::regprocedure),
    'TABLE(skill_id uuid, skill_key text, section text, attempts bigint, correct bigint, accuracy numeric, median_elapsed_ms bigint, pacing_ratio numeric, knowledge_weak boolean, pacing_weak boolean, first_answers bigint, first_answer_accuracy numeric)',
    'new columns come last');
end $$;
-- The window, and who may read first answers.
do $$
declare st uuid := current_setting('t.st')::uuid; who record; v_n bigint;
begin
  -- First answers keep the 30-most-recent window: 31 fresh answers on one skill count 30.
  perform hp_test.as_owner();
  insert into public.practice_questions(id, exam_version_id, question_type_id, section, difficulty, stem, choices, answer_format, accepted_answers,
    expected_time_seconds, status, license, origin)
  select ('3a000000-0000-0000-0000-' || lpad(n::text, 12, '0'))::uuid, '40000000-0000-0000-0000-000000000001', '41000000-0000-0000-0000-000000000001',
    'reading', 2, 'Window ' || n, '["A","B"]', 'choice', '["A"]', 30, 'published', 'original-owned', 'authored'
  from generate_series(1, 31) n;
  insert into public.practice_question_skills(question_id, skill_id, is_primary)
  select ('3a000000-0000-0000-0000-' || lpad(n::text, 12, '0'))::uuid, '42000000-0000-0000-0000-00000000000b', true from generate_series(1, 31) n;
  perform public.approve_practice_question(('3a000000-0000-0000-0000-' || lpad(n::text, 12, '0'))::uuid, 'test fixture') from generate_series(1, 31) n;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.submit_practice_attempt(public.start_practice_attempt(st, ('3a000000-0000-0000-0000-' || lpad(n::text, 12, '0'))::uuid), 'A')
  from generate_series(1, 31) n;
  select first_answers into v_n from public.student_skill_estimates(st) where skill_key = 'inference';
  perform hp_test.eq(v_n, 30::bigint, 'first answers use the 30 most recent');

  for who in select * from (values ('20000000-0000-0000-0000-0000000000a1'::uuid, 'PARENT', true), ('20000000-0000-0000-0000-000000000051'::uuid, 'STUDENT', true),
      ('20000000-0000-0000-0000-0000000000c1'::uuid, 'GOALS', false), ('20000000-0000-0000-0000-0000000000b1'::uuid, 'OTHER guardian', false),
      ('20000000-0000-0000-0000-000000000052'::uuid, 'OTHER student', false), ('20000000-0000-0000-0000-000000000099'::uuid, 'OUTSIDER', false)) v(uid, label, ok) loop
    perform hp_test.as_user(who.uid);
    if who.ok then
      perform hp_test.eq((select count(*) from public.student_skill_estimates(st) where first_answers > 0), 3::bigint, who.label || ' reads first answers');
    else
      perform hp_test.expect_error(format('select * from public.student_skill_estimates(%L)', st), '42501');
    end if;
  end loop;
  perform hp_test.as_anon();
  perform hp_test.expect_error(format('select * from public.student_skill_estimates(%L)', st), '42501');
  -- The service role has no user, so can_view_student refuses it, as before this migration.
  perform set_config('role', 'service_role', true);
  perform hp_test.expect_error(format('select * from public.student_skill_estimates(%L)', st), '42501');
  perform hp_test.as_owner();
  perform hp_test.check(not has_function_privilege('authenticated', 'public.first_answer_estimates_internal(uuid)', 'EXECUTE'), 'internal helper not client-callable');
  perform hp_test.check(not has_function_privilege('authenticated', 'public.practice_session_item_seen()', 'EXECUTE'), 'trigger function not client-callable');
end $$;
\o
\echo practice_seen: all assertions passed
rollback;
