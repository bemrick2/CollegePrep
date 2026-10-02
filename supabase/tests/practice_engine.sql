-- Practice engine: hidden content, grading, hints, events, skips, AI-help hooks, sessions, recommender,
-- skill estimates, adaptive goals, streaks, weekly progress, inactivity and test scores. Everything is rolled back.
-- Run with psql -v ON_ERROR_STOP=1; any failed assertion raises an exception.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql

-- Inserts a finished attempt as the test owner (deterministic timing for analytics fixtures).
create function hp_test.add_attempt(p_student uuid, p_q int, p_submitted timestamptz, p_elapsed_ms int,
  p_correct boolean, p_skipped boolean default false) returns void language sql as $$
  insert into public.practice_attempts(student_id, question_id, presented_at, submitted_at, elapsed_ms, is_correct, skipped,
    selected_answer, attempt_number)
  select p_student, q, p_submitted - make_interval(secs => p_elapsed_ms / 1000.0), p_submitted, p_elapsed_ms,
    case when p_skipped then null else p_correct end, p_skipped, case when p_skipped then null else 'X' end,
    (select count(*) + 1 from public.practice_attempts a where a.student_id = p_student and a.question_id = q)
  from (select ('30000000-0000-0000-0000-00000000000' || p_q)::uuid as q) x
$$;
create function hp_test.q(p_n int) returns uuid language sql immutable as $$ select ('30000000-0000-0000-0000-00000000000' || p_n)::uuid $$;
grant execute on all functions in schema hp_test to anon, authenticated;

-- Household in America/Los_Angeles: st (claimed by s1), fixture students st_e, st_z, st_g, st_new; g2 may only set goals.
do $$
declare hh uuid; st uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Practice household', 'America/Los_Angeles');
  st := public.add_student(hh, 'Practiser');
  perform set_config('t.hh', hh::text, true);
  perform set_config('t.st', st::text, true);
  perform set_config('t.st_e', public.add_student(hh, 'Estimates')::text, true);
  perform set_config('t.st_z', public.add_student(hh, 'Streaks')::text, true);
  perform set_config('t.st_g', public.add_student(hh, 'Goals')::text, true);
  perform set_config('t.st_new', public.add_student(hh, 'Never practised')::text, true);
  perform set_config('t.inv_s', public.create_household_invitation(hh, 'student', st), true);
  perform set_config('t.inv_g', public.create_household_invitation(hh, 'guardian', null, 72, array['set_goals']), true);
  insert into public.weekly_practice_goals(student_id, week_start, target_questions, target_minutes) values (st, '2026-09-07', 10, 10);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv_s'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform public.accept_household_invitation(current_setting('t.inv_g'));
  perform hp_test.as_owner();
end $$;

-- Content visibility: published only, answers/hints/explanations/rationales never selectable.
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select count(*) from public.practice_questions), 7::bigint, 'drafts hidden');
  perform hp_test.eq((select count(*) from public.practice_question_strategies), 2::bigint, 'draft strategy links hidden');
  perform hp_test.eq((select count(*) from public.practice_question_skills), 8::bigint, 'draft skill links hidden');
  perform hp_test.eq((select count(*) from public.exam_versions), 2::bigint, 'exam versions readable');
  perform hp_test.check((select rules->'scale'->>'max' from public.exam_versions where version_key = 'act_enhanced_2025') = '36', 'exam rules are data');
  perform hp_test.expect_error('select accepted_answers from public.practice_questions', '42501');
  perform hp_test.expect_error('select hints from public.practice_questions', '42501');
  perform hp_test.expect_error('select teaching_explanation from public.practice_questions', '42501');
  perform hp_test.expect_error('select strategy_explanation from public.practice_questions', '42501');
  perform hp_test.expect_error('select * from public.practice_questions', '42501');
  perform hp_test.expect_error('select rationale from public.practice_question_distractors', '42501');
  perform hp_test.expect_error('select strategy_explanation from public.practice_question_strategies', '42501');
  perform hp_test.expect_error('select value from public.app_settings', '42501');
  perform hp_test.check((select is_fastest from public.practice_question_strategies where strategy_id = '31000000-0000-0000-0000-000000000002'), 'fastest flag visible');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L)', current_setting('t.st'), hp_test.q(5)), '22023', '%not available%');
  perform hp_test.as_owner();
  -- Numeric questions must store parseable accepted answers.
  perform hp_test.expect_error($q$insert into public.practice_questions(exam_version_id, question_type_id, section, stem, answer_format, accepted_answers)
    values ('40000000-0000-0000-0000-000000000001', '41000000-0000-0000-0000-000000000002', 'math', 'Bad', 'numeric', '["one half"]')$q$, '23514');
  perform hp_test.expect_error($q$insert into public.practice_questions(exam_version_id, question_type_id, section, stem, answer_format, accepted_answers)
    values ('40000000-0000-0000-0000-000000000002', '41000000-0000-0000-0000-000000000001', 'math', 'Wrong version type', 'choice', '["A"]')$q$, '23503');
end $$;

-- Practice flow as s1.
do $$
declare a uuid; h jsonb; r record;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.expect_error(format($q$insert into public.practice_attempts(student_id, question_id, is_correct) values (%L, %L, true)$q$,
    current_setting('t.st'), hp_test.q(1)), '42501');
  -- a1 (q1): hints one at a time, then a correct answer with the fastest strategy revealed.
  a := public.start_practice_attempt(current_setting('t.st')::uuid, hp_test.q(1));
  perform set_config('t.a1', a::text, true);
  h := public.request_hint(a);
  perform hp_test.check(h = '{"hint_number":1,"hint":"First hint","remaining":1}', 'first hint ' || h::text);
  h := public.request_hint(a);
  perform hp_test.check(h = '{"hint_number":2,"hint":"Second hint","remaining":0}', 'second hint ' || h::text);
  perform hp_test.expect_error(format('select public.request_hint(%L)', a), '22023', '%No more hints%');
  perform hp_test.eq((select hint_count from public.practice_attempts where id = a), 2, 'hint_count incremented');
  perform hp_test.expect_error('select hints from public.practice_questions', '42501');
  perform hp_test.expect_error(format('select public.submit_practice_attempt(%L, ''B'', p_confidence => 4)', a), '22023', '%Confidence%');
  perform hp_test.expect_error(format('select public.submit_practice_attempt(%L, ''B'', -1)', a), '22023');
  perform hp_test.expect_error(format('select public.submit_practice_attempt(%L, ''B'', 5)', a), '22023', '%exceeds%');
  perform hp_test.expect_error(format('select public.submit_practice_attempt(%L, ''B'', p_strategy_key => ''no_such'')', a), '22023');
  select * into r from public.submit_practice_attempt(a, 'B', p_confidence => 3, p_strategy_key => 'backsolve');
  perform hp_test.check(r.is_correct and not r.skipped and r.accepted_answers = '["B"]' and r.teaching_explanation = 'Teaching 1'
    and r.strategy_explanation = 'Strategy 1', 'submit reveal');
  perform hp_test.check(r.distractors = '[{"choice":"A","rationale":"Dropped the negative sign.","trap":"sign_error"},
    {"choice":"C","rationale":"Stopped after the first step.","trap":"partial_answer"}]', 'distractor reveal ' || r.distractors::text);
  perform hp_test.check(r.strategies->0->>'strategy_key' = 'backsolve' and (r.strategies->0->>'is_fastest')::boolean, 'fastest strategy first');
  perform hp_test.expect_error(format('select public.submit_practice_attempt(%L, ''B'')', a), '22023', '%already submitted%');
  perform hp_test.expect_error(format('select public.request_hint(%L)', a), '22023', '%already submitted%');
  -- a2/a3 (q2, numeric): '0.5' and '.5' match '1/2'; '0.6' does not.
  a := public.start_practice_attempt(current_setting('t.st')::uuid, hp_test.q(2));
  perform set_config('t.a2', a::text, true);
  perform hp_test.check((select is_correct from public.submit_practice_attempt(a, '0.5', p_confidence => 2)), '0.5 = 1/2');
  a := public.start_practice_attempt(current_setting('t.st')::uuid, hp_test.q(2));
  perform set_config('t.a3', a::text, true);
  perform hp_test.check(not (select is_correct from public.submit_practice_attempt(a, '0.6', p_confidence => 1)), '0.6 <> 1/2');
  perform hp_test.eq((select attempt_number from public.practice_attempts where id = a), 2, 'attempt numbering');
  perform hp_test.check(public.grade_answer('numeric', '["1/2"]', '.5') and public.grade_answer('numeric', '["0.5"]', '2/4')
    and public.grade_answer('numeric', '["-3"]', '-3.0') and not public.grade_answer('numeric', '["1/2"]', '1/0')
    and public.grade_answer('choice', '["B"]', ' B ') and not public.grade_answer('choice', '["B"]', 'b')
    and not public.grade_answer('choice', '["0.5"]', '.5'), 'grading equivalence rules');
  -- a4 (q3): answer, unchanged, change, skip, return, then final answer (another change).
  a := public.start_practice_attempt(current_setting('t.st')::uuid, hp_test.q(3));
  perform set_config('t.a4', a::text, true);
  perform hp_test.eq(public.record_attempt_event(a, 'answered', 'A'), 'answered', 'first answer');
  perform hp_test.eq(public.record_attempt_event(a, 'answered', 'A'), 'unchanged', 'same answer not logged');
  perform hp_test.eq(public.record_attempt_event(a, 'answered', 'B'), 'changed_answer', 'answer change');
  perform hp_test.eq(public.record_attempt_event(a, 'skipped'), 'skipped', 'skip event');
  perform hp_test.eq(public.record_attempt_event(a, 'returned'), 'returned', 'return event');
  perform hp_test.expect_error(format('select public.record_attempt_event(%L, ''submitted'')', a), '22023');
  perform hp_test.expect_error(format('select public.record_attempt_event(%L, ''skipped'', ''A'')', a), '22023');
  perform hp_test.check((select is_correct from public.submit_practice_attempt(a, 'C', p_confidence => 2)), 'final answer graded');
  perform hp_test.check((select array_agg(kind order by id) from public.practice_attempt_events where attempt_id = a)
    = array['presented','answered','changed_answer','skipped','returned','changed_answer','submitted'], 'event log order');
  perform hp_test.eq((select confidence from public.practice_attempts where id = a), 2::smallint, 'confidence stored');
  perform hp_test.expect_error(format($q$insert into public.practice_attempt_events(attempt_id, student_id, kind) values (%L, %L, 'returned')$q$,
    a, current_setting('t.st')), '42501');
  perform hp_test.expect_error('update public.practice_attempt_events set kind = ''submitted''', '42501');
  perform hp_test.expect_error('delete from public.practice_attempt_events', '42501');
  -- a5 (q4): final skip.
  a := public.start_practice_attempt(current_setting('t.st')::uuid, hp_test.q(4));
  perform set_config('t.a5', a::text, true);
  perform hp_test.expect_error(format('select public.submit_practice_attempt(%L, ''A'', p_skipped => true)', a), '22023');
  perform hp_test.expect_error(format('select public.submit_practice_attempt(%L, null)', a), '22023', '%answer is required%');
  select * into r from public.submit_practice_attempt(a, null, p_skipped => true);
  perform hp_test.check(r.skipped and r.is_correct is null and r.accepted_answers = '["A"]', 'skip result');
  -- a6 (q6): AI help is recorded as disabled until the flag is on; answer_reveal only after submission.
  a := public.start_practice_attempt(current_setting('t.st')::uuid, hp_test.q(6));
  perform set_config('t.a6', a::text, true);
  perform hp_test.expect_error(format('select public.request_ai_help(%L, ''answer_reveal'')', a), '22023', '%after submission%');
  perform hp_test.expect_error(format('select public.request_ai_help(%L, ''essay'')', a), '22023');
  perform hp_test.eq(public.request_ai_help(a, 'concept')->>'status', 'disabled', 'ai help disabled by default');
  perform hp_test.check(not (select ai_help_used from public.practice_attempts where id = a), 'disabled help is not help used');
  perform hp_test.expect_error($q$insert into public.ai_help_requests(attempt_id, student_id, mode, status) values (current_setting('t.a6')::uuid, current_setting('t.st')::uuid, 'hint', 'completed')$q$, '42501');
  perform hp_test.as_owner();
  insert into public.app_settings(key, value) values ('ai_help_enabled', 'true');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq(public.request_ai_help(a, 'hint')->>'status', 'pending', 'ai help pending when enabled');
  perform hp_test.check((select ai_help_used from public.practice_attempts where id = a), 'pending help marks attempt');
  perform public.submit_practice_attempt(a, 'A');
  perform hp_test.eq(public.request_ai_help(a, 'answer_reveal')->>'status', 'pending', 'answer_reveal allowed after submission');
  perform hp_test.eq((select count(*) from public.ai_help_requests), 3::bigint, 'student reads own help requests');
  perform hp_test.as_owner();
end $$;

-- Guardians cannot practise as the student; view_progress guardians read help requests and events; g2 cannot.
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L)', current_setting('t.st'), hp_test.q(1)), '42501', '%own login%');
  perform hp_test.expect_error(format('select public.start_practice_session(%L)', current_setting('t.st')), '42501');
  perform hp_test.expect_error(format('select public.request_ai_help(%L, ''concept'')', current_setting('t.a6')), '42501');
  perform hp_test.expect_error(format('select public.record_attempt_event(%L, ''returned'')', current_setting('t.a6')), '42501');
  perform hp_test.eq((select count(*) from public.ai_help_requests), 3::bigint, 'guardian reads help requests');
  perform hp_test.eq((select count(*) from public.practice_attempt_events where student_id = current_setting('t.st')::uuid), 21::bigint, 'guardian reads events');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq((select count(*) from public.ai_help_requests), 0::bigint, 'set-goals-only guardian cannot read help requests');
  perform hp_test.eq((select count(*) from public.practice_attempt_events), 0::bigint, 'set-goals-only guardian cannot read events');
  perform hp_test.as_owner();
end $$;

-- Weekly progress for st: pin the flow to Tue 2026-09-08 09:00 Los Angeles (16:00Z).
update public.practice_attempts set submitted_at = '2026-09-08 16:00Z', presented_at = '2026-09-08 15:59Z', elapsed_ms = 60000,
  active_ms = case when id = current_setting('t.a1')::uuid then 30000 end
where student_id = current_setting('t.st')::uuid;
update public.practice_attempt_events set occurred_at = '2026-09-08 16:00Z' where student_id = current_setting('t.st')::uuid;
do $$
declare p jsonb;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  p := public.student_weekly_progress(current_setting('t.st')::uuid, '2026-09-07');
  perform hp_test.check(p @> jsonb_build_object(
    'time_zone', 'America/Los_Angeles', 'questions_attempted', 6, 'questions_submitted', 5, 'skipped', 1,
    'skip_events', 2, 'returns', 1, 'answer_changes', 2, 'correct', 3, 'accuracy', 0.6,
    'total_elapsed_ms', 360000, 'total_active_ms', 30000, 'median_elapsed_ms', 60000, 'avg_confidence', 2.00,
    'ai_help_attempts', 1, 'hints_used', 2,
    'goal', '{"target_questions":10,"target_minutes":10,"goal_mode":"fixed"}'::jsonb,
    'goal_progress', '{"questions_pct":50.0,"minutes_pct":60.0}'::jsonb,
    'streak', '{"current":0,"longest":1}'::jsonb,
    'skill_summary', '{"knowledge_weak":[],"pacing_weak":[],"insufficient_data":2}'::jsonb,
    'by_strategy', '[{"strategy_key":"backsolve","submitted":1,"correct":1}]'::jsonb,
    'by_skill', '[{"section":"math","skill":"linear_equations","submitted":4,"correct":2,"median_elapsed_ms":60000},
                  {"section":"reading","skill":"inference","submitted":1,"correct":1,"median_elapsed_ms":60000}]'::jsonb), 'weekly progress ' || p::text);
  -- The same instant falls in the previous local week when the boundary moves: Monday 00:30 LA = Monday 07:30Z.
  perform hp_test.as_owner();
  update public.practice_attempts set submitted_at = '2026-09-14 06:30Z' where id = current_setting('t.a1')::uuid;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((public.student_weekly_progress(current_setting('t.st')::uuid, '2026-09-07')->>'questions_submitted')::int, 5, 'Sunday 23:30 local stays in week');
  perform hp_test.as_owner();
  update public.practice_attempts set submitted_at = '2026-09-14 07:30Z' where id = current_setting('t.a1')::uuid;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((public.student_weekly_progress(current_setting('t.st')::uuid, '2026-09-07')->>'questions_submitted')::int, 4, 'Monday 00:30 local is next week');
  p := public.student_weekly_progress(current_setting('t.st_new')::uuid, '2026-09-07');
  perform hp_test.check(p->'accuracy' = 'null' and p->'median_elapsed_ms' = 'null' and p->'avg_confidence' = 'null'
    and p->'goal_progress' = 'null' and (p->>'questions_submitted')::int = 0 and p->'by_skill' = '[]', 'empty progress ' || p::text);
  perform hp_test.expect_error(format('select public.student_weekly_progress(%L, ''2026-09-08'')', current_setting('t.st')), '22023', '%Monday%');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((public.student_weekly_progress(current_setting('t.st')::uuid, '2026-09-07')->>'correct')::int, 2, 'student reads own progress');
  perform hp_test.as_owner();
end $$;

-- Skill estimate fixture (st_e):
--   linear_equations: 6 attempts, 2 correct, at expected pace -> knowledge_weak, not pacing_weak
--   inference:        5 attempts, all correct, 1.5x expected time -> pacing_weak, not knowledge_weak
--   ratios:           2 attempts -> insufficient data (flags null); data_analysis: never seen
select hp_test.add_attempt(current_setting('t.st_e')::uuid, q, ts::timestamptz, ms, ok) from (values
  (6, '2026-09-01 10:00Z', 120000, true), (6, '2026-09-01 10:05Z', 120000, false),
  (2, '2026-09-02 10:00Z', 90000, false), (2, '2026-09-02 10:05Z', 90000, true),
  (1, '2026-09-03 10:00Z', 60000, false), (1, '2026-09-03 10:05Z', 60000, false),
  (7, '2026-09-01 11:00Z', 90000, true), (7, '2026-09-01 11:05Z', 90000, true),
  (3, '2026-09-02 11:00Z', 90000, true), (3, '2026-09-02 11:05Z', 90000, true), (3, '2026-09-02 11:10Z', 90000, true),
  (4, '2026-09-03 12:00Z', 30000, true), (4, '2026-09-03 12:05Z', 30000, true)) v(q, ts, ms, ok);
do $$
declare e record; n int := 0;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  for e in select * from public.student_skill_estimates(current_setting('t.st_e')::uuid) loop
    n := n + 1;
    if e.skill_key = 'linear_equations' then
      perform hp_test.check(e.attempts = 6 and e.correct = 2 and e.accuracy = 0.3333 and e.median_elapsed_ms = 90000
        and e.pacing_ratio = 1.000 and e.knowledge_weak and not e.pacing_weak, 'linear estimate ' || row_to_json(e));
    elsif e.skill_key = 'inference' then
      perform hp_test.check(e.attempts = 5 and e.accuracy = 1 and e.pacing_ratio = 1.500 and not e.knowledge_weak and e.pacing_weak,
        'inference estimate ' || row_to_json(e));
    elsif e.skill_key = 'ratios' then
      perform hp_test.check(e.attempts = 2 and e.knowledge_weak is null and e.pacing_weak is null, 'ratios estimate ' || row_to_json(e));
    else
      perform hp_test.check(false, 'unexpected skill ' || e.skill_key);
    end if;
  end loop;
  perform hp_test.eq(n, 3, 'three estimated skills');
  -- Recommender: weak knowledge first (least recently seen first), then weak pacing, new skill, review; drafts excluded.
  perform hp_test.check((select array_agg(question_id order by item_position) from public.recommend_practice_set(current_setting('t.st_e')::uuid, 10))
    = array[hp_test.q(6), hp_test.q(2), hp_test.q(1), hp_test.q(7), hp_test.q(3), hp_test.q(8), hp_test.q(4)], 'recommendation order');
  perform hp_test.check((select array_agg(reason order by item_position) from public.recommend_practice_set(current_setting('t.st_e')::uuid, 10))
    = array['weak_knowledge','weak_knowledge','weak_knowledge','weak_pacing','weak_pacing','new_skill','review'], 'recommendation reasons');
  perform hp_test.check((select sum(expected_time_seconds) from public.recommend_practice_set(current_setting('t.st_e')::uuid, 10)) <= 600, 'within budget');
  -- 5 minutes: 120 + 90 + 60 = 270s; any further 60s item would exceed 300s.
  perform hp_test.check((select array_agg(question_id order by item_position) from public.recommend_practice_set(current_setting('t.st_e')::uuid, 5))
    = array[hp_test.q(6), hp_test.q(2), hp_test.q(1)], '5-minute set');
  perform hp_test.expect_error(format('select * from public.recommend_practice_set(%L, 20)', current_setting('t.st_e')), '22023');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.expect_error(format('select * from public.recommend_practice_set(%L, 10)', current_setting('t.st_e')), '42501');
  perform hp_test.as_owner();
end $$;

-- Session plan for the linked student is generated by the recommender and readable by the student.
do $$
declare s uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.expect_error(format('select public.start_practice_session(%L, 4)', current_setting('t.st')), '22023');
  s := public.start_practice_session(current_setting('t.st')::uuid, 5);
  perform hp_test.check((select count(*) between 1 and 5 and sum(q.expected_time_seconds) <= 300 and bool_and(q.status = 'published')
    from public.practice_session_items i join public.practice_questions q on q.id = i.question_id where i.session_id = s), 'session plan');
  perform hp_test.eq((select target_minutes from public.practice_sessions where id = s), 5, 'session target stored');
  perform public.end_practice_session(s);
  perform hp_test.as_owner();
end $$;

-- Streak (st_z): submissions near midnight UTC are on different local days in Los Angeles (UTC-7 in September).
--   UTC days: 09-01, 09-03 (longest 1).  LA days: 08-31, 09-01, 09-02, 09-03 (longest 4).
select hp_test.add_attempt(current_setting('t.st_z')::uuid, 1, ts::timestamptz, 60000, true) from (values
  ('2026-09-01 03:00Z'), ('2026-09-01 20:00Z'), ('2026-09-03 05:00Z'), ('2026-09-03 18:00Z')) v(ts);
select hp_test.add_attempt(current_setting('t.st_z')::uuid, 2, '2026-09-10 18:00Z', 60000, null, true);
do $$
declare z uuid := current_setting('t.st_z')::uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.check(public.student_streak(z, 'UTC', '2026-09-03') @> '{"current_streak":1,"longest_streak":1}', 'UTC streak');
  perform hp_test.check(public.student_streak(z, 'America/Los_Angeles', '2026-09-03') @> '{"current_streak":4,"longest_streak":4,"last_practice_day":"2026-09-03"}', 'LA streak');
  perform hp_test.check(public.student_streak(z, null, '2026-09-04') @> '{"time_zone":"America/Los_Angeles","current_streak":4}', 'streak alive through yesterday');
  perform hp_test.check(public.student_streak(z, null, '2026-09-05') @> '{"current_streak":0,"longest_streak":4}', 'streak broken; skips do not count');
  perform hp_test.expect_error(format('select public.student_streak(%L, ''Not/AZone'')', z), '22023', '%time zone%');
  perform hp_test.as_owner();
end $$;

-- Adaptive goals (st_g): question targets 10, 10, 20 completed 12, 10, 16 -> mean(1.2, 1.0, 0.8) = 1.0 -> 20 * 1.10 = 22.
-- Minute targets 30, 60 completed 10, 16 minutes -> mean(0.333, 0.267) = 0.3 < 0.7 -> 60 * 0.85 = 51.
insert into public.weekly_practice_goals(student_id, week_start, target_questions, target_minutes, goal_mode) values
 (current_setting('t.st_g')::uuid, '2026-09-07', 10, null, 'adaptive'),
 (current_setting('t.st_g')::uuid, '2026-09-14', 10, 30, 'adaptive'),
 (current_setting('t.st_g')::uuid, '2026-09-21', 20, 60, 'adaptive');
select hp_test.add_attempt(current_setting('t.st_g')::uuid, 1 + (i % 4), (wk::date + 2 + time '12:00' + make_interval(mins => i))::timestamp at time zone 'America/Los_Angeles', 60000, true)
from (values ('2026-09-07', 12), ('2026-09-14', 10), ('2026-09-21', 16)) v(wk, n), generate_series(1, n) i;
do $$
declare s jsonb; g uuid := current_setting('t.st_g')::uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  s := public.suggest_next_week_goal(g, '2026-09-28');
  perform hp_test.check(s @> '{"weeks_considered":3,"questions_completion":1.000,"minutes_completion":0.300,"target_questions":22,"target_minutes":51,"basis":"history"}', 'adaptive suggestion ' || s::text);
  -- g2 (can_set_goals) applies the suggestion.
  insert into public.weekly_practice_goals(student_id, week_start, target_questions, target_minutes, goal_mode)
  values (g, '2026-09-28', (s->>'target_questions')::int, (s->>'target_minutes')::int, 'adaptive');
  perform hp_test.as_owner();
  update public.weekly_practice_goals set target_questions = 14 where student_id = g and week_start < '2026-09-28';
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  -- 12/14, 10/14, 16/14 -> mean 0.905 -> hold at 14.
  perform hp_test.eq((public.suggest_next_week_goal(g, '2026-09-28')->>'target_questions')::int, 14, 'hold band');
  perform hp_test.as_owner();
  update public.weekly_practice_goals set target_questions = 4 where student_id = g and week_start < '2026-09-28';
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  -- Completion capped at 1.5 each -> +10% of 4 = 4.4 -> floor of 5 questions.
  perform hp_test.eq((public.suggest_next_week_goal(g, '2026-09-28')->>'target_questions')::int, 5, 'floor applied');
  s := public.suggest_next_week_goal(current_setting('t.st_z')::uuid, '2026-09-28');
  perform hp_test.check(s @> '{"basis":"insufficient_history","weeks_considered":0}' and s->'target_questions' = 'null', 'no history ' || s::text);
  perform hp_test.expect_error(format('select public.suggest_next_week_goal(%L, ''2026-09-29'')', g), '22023');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error(format('select public.suggest_next_week_goal(%L)', g), '42501');
  perform hp_test.as_owner();
end $$;

-- Inactivity: st_z practised yesterday; st_new never practised; others last practised in September fixtures.
select hp_test.add_attempt(current_setting('t.st_z')::uuid, 3, now() - interval '1 day', 60000, true);
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.check((select array_agg(student_id order by student_id) from public.student_inactivity(3))
    = (select array_agg(x order by x) from unnest(array[current_setting('t.st')::uuid, current_setting('t.st_e')::uuid,
      current_setting('t.st_g')::uuid, current_setting('t.st_new')::uuid]) x), 'inactive students for 3 days');
  perform hp_test.check((select last_submitted_at is null from public.student_inactivity(3) where student_id = current_setting('t.st_new')::uuid), 'never practised listed first-class');
  perform hp_test.eq((select count(*) from public.student_inactivity()), 0::bigint, 'no preferences, no default alerts');
  insert into public.alert_preferences(student_id, channel, inactivity_days) values (current_setting('t.st_e')::uuid, 'email', 7),
    (current_setting('t.st_z')::uuid, 'push', 2);
  perform hp_test.check((select array_agg(student_id) from public.student_inactivity()) = array[current_setting('t.st_e')::uuid]
    and (select threshold_days from public.student_inactivity()) = 7, 'preference thresholds');
  perform hp_test.expect_error('select * from public.student_inactivity(0)', '22023');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq((select count(*) from public.student_inactivity(3)), 0::bigint, 'set-goals-only guardian sees no inactivity');
  perform hp_test.expect_error(format($q$insert into public.alert_preferences(student_id, channel) values (%L, 'email')$q$, current_setting('t.st_e')), '42501');
  perform hp_test.eq((select count(*) from public.alert_preferences), 0::bigint, 'alert preferences are private');
  perform hp_test.as_owner();
end $$;

-- Test scores: clients add self-reported only; practice estimates are labeled and never official.
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  insert into public.student_test_scores(student_id, exam_version_id, test_date, composite, score_source)
  values (current_setting('t.st')::uuid, '40000000-0000-0000-0000-000000000001', '2026-08-23', 1310, 'self_reported');
  perform hp_test.expect_error(format($q$insert into public.student_test_scores(student_id, exam_version_id, test_date, composite, score_source)
    values (%L, '40000000-0000-0000-0000-000000000001', '2026-08-23', 1600, 'official')$q$, current_setting('t.st')), '42501');
  perform hp_test.expect_error(format($q$insert into public.student_test_scores(student_id, exam_version_id, test_date, composite, score_source)
    values (%L, '40000000-0000-0000-0000-000000000001', '2026-08-23', 1500, 'practice_estimate')$q$, current_setting('t.st')), '42501');
  perform hp_test.expect_error(format($q$insert into public.student_test_scores(student_id, exam_version_id, test_date, composite, score_source)
    values (%L, '40000000-0000-0000-0000-000000000001', '2026-08-23', 1500, 'self_reported')$q$, current_setting('t.st_e')), '42501');
  perform hp_test.as_owner();
end $$;
set local role service_role;
insert into public.student_test_scores(student_id, exam_version_id, test_date, composite, score_source) values
 (current_setting('t.st')::uuid, '40000000-0000-0000-0000-000000000001', '2026-09-20', 1450, 'practice_estimate'),
 (current_setting('t.st')::uuid, '40000000-0000-0000-0000-000000000001', '2026-06-06', 1280, 'official');
reset role;
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((select count(*) from public.student_test_scores), 3::bigint, 'guardian reads all labeled scores');
  perform hp_test.check((select array_agg(composite) from public.student_official_scores) = array[1280], 'only official scores in official view');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq((select count(*) from public.student_official_scores), 0::bigint, 'set-goals-only guardian cannot read scores');
  perform hp_test.as_owner();
end $$;
\o
\echo practice_engine: all assertions passed
rollback;
