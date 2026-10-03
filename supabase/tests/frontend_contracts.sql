-- Front-end contracts from issue #37: CR-1 planning preferences, CR-2 benchmarks, CR-5 question content,
-- CR-7 verified-record school list, CR-8 answer-free help fields, CR-9 institution level and saved schools.
-- Everything is rolled back. Run with psql -v ON_ERROR_STOP=1.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql

-- Reference fixtures: one verified 2026-27 school with a level, one with only a 2023-24 record.
insert into public.sources(id, canonical_url, authority) values
 ('50000000-0000-0000-0000-000000000001', 'https://example.edu/contracts', 'institution');
insert into public.institutions(id, institution_key, ipeds_name, display_name, state_code, city, control, level, source_id,
  verification_status, last_verified_at, identity_academic_year) values
 ('50000000-0000-0000-0000-000000000002', 'contract-four', 'Four', 'Four Year U', 'TN', 'Nashville', 'public', 'four_year',
  '50000000-0000-0000-0000-000000000001', 'verified', current_date, '2023-24'),
 ('50000000-0000-0000-0000-000000000003', 'contract-two', 'Two', 'Two Year CC', 'GA', 'Atlanta', 'public', 'two_year',
  '50000000-0000-0000-0000-000000000001', 'verified', current_date, '2023-24');
insert into public.institution_costs(institution_id, academic_year, residency, tuition, source_id, verification_status, last_verified_at) values
 ('50000000-0000-0000-0000-000000000002', '2026-27', 'in_state', 9000, '50000000-0000-0000-0000-000000000001', 'verified', current_date),
 ('50000000-0000-0000-0000-000000000003', '2023-24', 'in_state', 3000, '50000000-0000-0000-0000-000000000001', 'verified', current_date);
do $$ begin
  perform hp_test.expect_error($q$update public.institutions set level = 'graduate' where institution_key = 'contract-four'$q$, '23514');
end $$;

-- CR-7 and CR-9 (level) through the public reference RPCs.
set local role anon;
do $$
declare r record; n int;
begin
  select count(*) into n from public.institutions_with_verified_records('2026-27');
  perform hp_test.eq(n, 1, 'only schools with a verified record for exactly this year');
  select * into r from public.institutions_with_verified_records('2026-27', 'TN');
  perform hp_test.check(r.institution_key = 'contract-four' and r.level = 'four_year' and r.domains = array['costs'], 'verified list row');
  perform hp_test.eq((select count(*) from public.institutions_with_verified_records('2026-27', 'GA')), 0::bigint, 'state filter');
  perform hp_test.expect_error($q$select * from public.institutions_with_verified_records('2026')$q$, '22023');
  perform hp_test.check(public.compare_institutions(array['contract-two'], '2023-24')->'institutions'->0->'institution'->>'level' = 'two_year',
    'compare_institutions returns the level');
end $$;
reset role;

-- Household A (g1 manages, g2 only sets goals); student s1 claims st; outsider x.
do $$
declare hh uuid; st uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Contracts', 'America/Chicago');
  st := public.add_student(hh, 'Planner');
  perform set_config('t.hh', hh::text, true);
  perform set_config('t.st', st::text, true);
  perform set_config('t.inv_s', public.create_household_invitation(hh, 'student', st), true);
  perform set_config('t.inv_g', public.create_household_invitation(hh, 'guardian', null, 72, array['set_goals']), true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv_s'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform public.accept_household_invitation(current_setting('t.inv_g'));
  perform hp_test.as_owner();
end $$;

-- CR-9 saved schools: members write through RPCs, readers need view_progress or to be the household's student.
do $$
declare i int;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.save_household_school(current_setting('t.hh')::uuid, 'contract-four');
  perform public.save_household_school(current_setting('t.hh')::uuid, 'contract-four');  -- idempotent
  perform hp_test.expect_error(format('select public.save_household_school(%L, %L)', current_setting('t.hh'), 'no-such-school'), '22023');
  perform hp_test.expect_error(format($q$insert into public.household_saved_schools(household_id, institution_key) values (%L, 'contract-two')$q$,
    current_setting('t.hh')), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.save_household_school(current_setting('t.hh')::uuid, 'contract-two');
  perform hp_test.eq((select count(*) from public.household_saved_schools), 2::bigint, 'student sees the household list');
  perform hp_test.check((select added_by from public.household_saved_schools where institution_key = 'contract-two')
    = '20000000-0000-0000-0000-000000000051', 'added_by recorded');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq((select count(*) from public.household_saved_schools), 0::bigint, 'guardian without view_progress reads nothing');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error(format('select public.save_household_school(%L, %L)', current_setting('t.hh'), 'contract-four'), '42501');
  perform hp_test.eq((select count(*) from public.household_saved_schools), 0::bigint, 'outsider reads nothing');
  -- Limit of 8 (two saved above).
  perform hp_test.as_owner();
  insert into public.institutions(institution_key, ipeds_name, display_name, state_code, source_id, verification_status, identity_academic_year)
  select 'contract-extra-' || n, 'X', 'X', 'TN', '50000000-0000-0000-0000-000000000001', 'verified', '2023-24' from generate_series(1, 7) n;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  for i in 1..6 loop perform public.save_household_school(current_setting('t.hh')::uuid, 'contract-extra-' || i); end loop;
  perform hp_test.expect_error(format('select public.save_household_school(%L, %L)', current_setting('t.hh'), 'contract-extra-7'), '22023', '%up to 8%');
  perform public.remove_household_school(current_setting('t.hh')::uuid, 'contract-extra-1');
  perform public.save_household_school(current_setting('t.hh')::uuid, 'contract-extra-7');
  perform hp_test.eq((select count(*) from public.household_saved_schools), 8::bigint, 'room after removal');
  perform hp_test.as_owner();
end $$;

-- CR-1 planning preferences: guardians with set_goals write; the household's student reads but cannot write.
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  insert into public.student_planning_preferences(student_id, exam_family, target_score, goals, daily_minutes)
  values (current_setting('t.st')::uuid, 'act', 30, array['raise_score','merit'], 10);
  perform hp_test.expect_error(format($q$update public.student_planning_preferences set target_score = 40 where student_id = %L$q$, current_setting('t.st')), '23514');
  perform hp_test.expect_error(format($q$update public.student_planning_preferences set exam_family = 'sat', target_score = 1205 where student_id = %L$q$, current_setting('t.st')), '23514');
  update public.student_planning_preferences set exam_family = 'sat', target_score = 1350 where student_id = current_setting('t.st')::uuid;
  perform hp_test.expect_error(format($q$update public.student_planning_preferences set goals = array['win'] where student_id = %L$q$, current_setting('t.st')), '23514');
  perform hp_test.expect_error(format($q$update public.student_planning_preferences set daily_minutes = 30 where student_id = %L$q$, current_setting('t.st')), '23514');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.check((select target_score = 1350 and set_by = '20000000-0000-0000-0000-0000000000a2' from public.student_planning_preferences),
    'student reads what the guardian set');
  update public.student_planning_preferences set daily_minutes = 5;  -- RLS: no rows for a household student
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((select daily_minutes from public.student_planning_preferences), 10, 'household student cannot change preferences');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.eq((select count(*) from public.student_planning_preferences), 0::bigint, 'outsider reads nothing');
  perform hp_test.as_owner();
end $$;

-- CR-5 and CR-8 content fields (owner writes content; clients read through grants and RPCs).
insert into public.practice_passages(id, exam_version_id, title, body) values
 ('51000000-0000-0000-0000-000000000001', '40000000-0000-0000-0000-000000000001', 'Shared passage', 'The [underlined] text. [1] First sentence.'),
 ('51000000-0000-0000-0000-000000000002', '40000000-0000-0000-0000-000000000001', 'Unused passage', 'Not used by a published question.');
update public.practice_questions set passage_id = '51000000-0000-0000-0000-000000000001', remember_text = 'Check the sign before choosing.',
  choices = '[{"key":"A","text":"-2"},{"key":"B","text":"2"},{"key":"C","text":"4"},{"key":"D","text":"8"}]'
where id = '30000000-0000-0000-0000-000000000001';
update public.skills set concept_summary = 'Isolate the variable by undoing operations in reverse order.' where skill_key = 'linear_equations';
update public.question_strategies set sections = array['math'] where strategy_key = 'backsolve';
do $$
declare r record; a uuid;
begin
  perform hp_test.expect_error($q$update public.practice_questions set remember_text = 'one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen'
    where id = '30000000-0000-0000-0000-000000000001'$q$, '23514');
  perform hp_test.expect_error($q$update public.practice_questions set choices = '[{"key":"A","text":"1"},{"key":"A","text":"2"}]'
    where id = '30000000-0000-0000-0000-000000000003'$q$, '23514');
  perform hp_test.expect_error($q$update public.practice_questions set choices = '[{"key":"A","text":"1"},{"key":"B","text":"2"}]'
    where id = '30000000-0000-0000-0000-000000000003'$q$, '23514');  -- accepted answer C is not a key
  perform hp_test.expect_error($q$update public.practice_questions set choices = '[{"key":"A"}]'
    where id = '30000000-0000-0000-0000-000000000003'$q$, '23514');
  perform hp_test.expect_error($q$update public.question_strategies set sections = array['art'] where strategy_key = 'backsolve'$q$, '23514');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  select passage_id, hint_count, choices into r from public.practice_questions where id = '30000000-0000-0000-0000-000000000001';
  perform hp_test.check(r.passage_id = '51000000-0000-0000-0000-000000000001' and r.hint_count = 2 and r.choices->0->>'key' = 'A',
    'passage id, hint count and keyed choices visible');
  perform hp_test.eq((select hint_count from public.practice_questions where id = '30000000-0000-0000-0000-000000000003'), 0, 'no hints');
  perform hp_test.expect_error('select remember_text from public.practice_questions', '42501');
  perform hp_test.eq((select count(*) from public.practice_passages), 1::bigint, 'only passages of published questions');
  perform hp_test.check((select body from public.practice_passages) like 'The [underlined]%', 'passage body readable');
  perform hp_test.check((select concept_summary from public.skills where skill_key = 'linear_equations') like 'Isolate%', 'concept summary readable');
  perform hp_test.check((select sections from public.question_strategies where strategy_key = 'backsolve') = array['math'], 'strategy sections readable');
  a := public.start_practice_attempt(current_setting('t.st')::uuid, '30000000-0000-0000-0000-000000000001');
  select * into r from public.submit_practice_attempt(a, 'B');
  perform hp_test.check(r.is_correct and r.remember_text = 'Check the sign before choosing.', 'remember_text returned on submit');
  perform hp_test.as_owner();
end $$;

-- CR-2 benchmarks: the student starts, attaches attempts and completes; guardians with view_progress read the summary.
do $$
declare b uuid; a uuid; m jsonb;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'initial')$q$, current_setting('t.st')), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'huge')$q$, current_setting('t.st')), '22023');
  b := public.start_benchmark(current_setting('t.st')::uuid, 'initial', '40000000-0000-0000-0000-000000000001');
  perform set_config('t.b', b::text, true);
  -- q1 wrong with confidence 3 (trap sign_error), q3 right, q4 presented and never submitted, q7 skipped.
  a := public.start_practice_attempt(current_setting('t.st')::uuid, '30000000-0000-0000-0000-000000000001', p_benchmark => b);
  perform public.record_attempt_event(a, 'answered', 'B');
  perform public.record_attempt_event(a, 'returned');
  perform public.submit_practice_attempt(a, 'A', p_confidence => 3);
  a := public.start_practice_attempt(current_setting('t.st')::uuid, '30000000-0000-0000-0000-000000000003', p_benchmark => b);
  perform public.submit_practice_attempt(a, 'C', p_confidence => 2);
  perform public.start_practice_attempt(current_setting('t.st')::uuid, '30000000-0000-0000-0000-000000000004', p_benchmark => b);
  a := public.start_practice_attempt(current_setting('t.st')::uuid, '30000000-0000-0000-0000-000000000007', p_benchmark => b);
  perform public.submit_practice_attempt(a, null, p_skipped => true);
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, %L, %L)', current_setting('t.st'),
    '30000000-0000-0000-0000-000000000008', public.start_practice_session(current_setting('t.st')::uuid, 5), b), '22023', '%not both%');
  m := public.complete_benchmark(b);
  perform hp_test.check((m->>'attempts')::int = 4 and (m->>'submitted')::int = 2 and (m->>'skips')::int = 1
    and (m->>'unsubmitted')::int = 1 and (m->>'returns')::int = 1 and (m->>'answer_changes')::int = 1
    and (m->>'accuracy')::numeric = 0.5, 'benchmark counts ' || m::text);
  perform hp_test.check(m->'by_section'->'math'->>'accuracy' = '0.0000' and m->'by_section'->'reading'->>'accuracy' = '1.0000', 'by section');
  perform hp_test.check((m->'calibration'->>'confident_wrong_share')::numeric = 1 and m->'traps'->>'sign_error' = '1', 'calibration and traps');
  perform hp_test.expect_error(format('select public.complete_benchmark(%L)', b), '22023', '%already completed%');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, p_benchmark => %L)', current_setting('t.st'),
    '30000000-0000-0000-0000-000000000008', b), '22023', '%open benchmark%');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.check((select completed_at is not null and metrics->>'definition' = 'v1' from public.practice_benchmarks where id = b),
    'guardian reads the benchmark');
  perform hp_test.eq((select count(*) from public.practice_attempts where benchmark_id = b), 4::bigint, 'attempts grouped');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq((select count(*) from public.practice_benchmarks), 0::bigint, 'guardian without view_progress reads nothing');
  perform hp_test.as_owner();
end $$;

rollback;
\o
\echo frontend contract tests passed
