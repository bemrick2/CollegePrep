-- Front-end contracts from issue #37: CR-4 cost projection, CR-1 planning preferences, CR-2 benchmarks, CR-5 question content,
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

-- CR-12 primary school: one per household, must be saved, cleared by null or by removing the school.
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((select count(*) from public.household_saved_schools where is_primary), 0::bigint, 'no primary by default');
  perform public.set_household_primary_school(current_setting('t.hh')::uuid, 'contract-four');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.set_household_primary_school(current_setting('t.hh')::uuid, 'contract-two');
  perform hp_test.eq((select string_agg(institution_key, ',') from public.household_saved_schools where is_primary), 'contract-two',
    'student moves the primary; only one remains');
  perform public.set_household_primary_school(current_setting('t.hh')::uuid, 'contract-two');  -- idempotent
  perform hp_test.expect_error(format('select public.set_household_primary_school(%L, %L)', current_setting('t.hh'), 'contract-extra-1'),
    '22023', '%Save%');
  perform hp_test.expect_error(format($q$update public.household_saved_schools set is_primary = true where institution_key = 'contract-four' and household_id = %L$q$,
    current_setting('t.hh')), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error(format('select public.set_household_primary_school(%L, %L)', current_setting('t.hh'), 'contract-four'), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.set_household_primary_school(current_setting('t.hh')::uuid, null);
  perform hp_test.eq((select count(*) from public.household_saved_schools where is_primary), 0::bigint, 'null clears the primary');
  perform public.set_household_primary_school(current_setting('t.hh')::uuid, 'contract-extra-7');
  perform public.remove_household_school(current_setting('t.hh')::uuid, 'contract-extra-7');
  perform hp_test.eq((select count(*) from public.household_saved_schools where is_primary), 0::bigint, 'removing the primary clears it');
  perform public.save_household_school(current_setting('t.hh')::uuid, 'contract-extra-7');
  perform hp_test.eq((select count(*) from public.household_saved_schools where is_primary), 0::bigint, 're-saving does not restore it');
  perform hp_test.as_owner();
  perform hp_test.expect_error(format($q$update public.household_saved_schools set is_primary = true where household_id = %L$q$,
    current_setting('t.hh')), '23505');
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

-- CR-4 cost_projection: verified, exact-year data only; only capped prior credits are counted.
insert into public.transfer_policies(institution_id, academic_year, policy_url, max_transfer_credits, source_id, verification_status, last_verified_at) values
 ('50000000-0000-0000-0000-000000000002', '2026-27', 'https://example.edu/transfer', 60, '50000000-0000-0000-0000-000000000001', 'verified', current_date);
insert into public.credit_policies(institution_id, policy_kind, academic_year, policy_url, general_limit_credits, source_id, verification_status, last_verified_at) values
 ('50000000-0000-0000-0000-000000000002', 'dual_enrollment', '2026-27', 'https://example.edu/dual', 24, '50000000-0000-0000-0000-000000000001', 'verified', current_date),
 ('50000000-0000-0000-0000-000000000002', 'AP', '2026-27', 'https://example.edu/ap', 6, '50000000-0000-0000-0000-000000000001', 'verified', current_date);
insert into public.institutional_awards(institution_id, award_name, academic_year, award_type, award_max, source_id, verification_status, last_verified_at) values
 ('50000000-0000-0000-0000-000000000002', 'Verified Merit', '2026-27', 'merit', 4000, '50000000-0000-0000-0000-000000000001', 'verified', current_date),
 ('50000000-0000-0000-0000-000000000002', 'Draft Merit', '2026-27', 'merit', 9000, '50000000-0000-0000-0000-000000000001', 'unverified', null),
 ('50000000-0000-0000-0000-000000000002', 'Old Merit', '2025-26', 'merit', 9000, '50000000-0000-0000-0000-000000000001', 'verified', current_date);
insert into public.institution_costs(institution_id, academic_year, residency, tuition, source_id, verification_status) values
 ('50000000-0000-0000-0000-000000000002', '2026-27', 'out_of_state', 30000, '50000000-0000-0000-0000-000000000001', 'unverified');
do $$
declare r jsonb; i jsonb; st uuid := current_setting('t.st')::uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  r := public.cost_projection(st, array['contract-four', 'contract-two', 'no-such-school'], '2026-27',
         '{"residency": "in_state", "prior_credits": 30}');
  perform hp_test.check((r->>'guaranteed')::boolean = false and (r->>'prices_held_constant')::boolean, 'projection is labelled');
  i := r->'institutions'->0;
  perform hp_test.check(i->>'status' = 'ok' and (i->>'years')::int = 4 and i->>'years_source' = 'level_default', 'four-year default');
  perform hp_test.eq((i->>'baseline_total')::numeric, 36000::numeric, 'baseline = annual x years');
  perform hp_test.eq((i->'levers'->0->>'accepted_upper_bound')::numeric, 24::numeric, 'lowest verified cap wins (AP limit ignored)');
  perform hp_test.check((i->'levers'->0->>'terms_saved')::int = 1 and (i->'levers'->0->>'counted')::boolean
    and (i->'levers'->0->>'requires_confirmation')::boolean, 'one term saved, needs confirmation');
  perform hp_test.eq((i->>'optimized_total')::numeric, 31500::numeric, 'optimized subtracts one term');
  perform hp_test.eq((i->>'savings_total')::numeric, 4500::numeric, 'savings');
  perform hp_test.eq(jsonb_array_length(i->'not_counted'->'awards'), 1, 'only verified exact-year awards are listed');
  perform hp_test.check(i->'not_counted'->'awards'->0->>'award_name' = 'Verified Merit', 'listed award');
  perform hp_test.check(r->'institutions'->1->>'status' = 'missing_cost', 'no fallback to another year');
  perform hp_test.check(r->'institutions'->2->>'status' = 'unknown_institution', 'unknown school is explicit');

  r := public.cost_projection(st, array['contract-four'], '2026-27', '{"residency": "out_of_state"}');
  perform hp_test.check(r->'institutions'->0->>'status' = 'missing_cost', 'unverified cost is not used');
  r := public.cost_projection(st, array['contract-two'], '2023-24', '{"residency": "in_state", "prior_credits": 30}');
  i := r->'institutions'->0;
  perform hp_test.check(i->'levers'->0->>'reason' = 'no_verified_cap' and (i->>'savings_total')::numeric = 0
    and (i->>'baseline_total')::numeric = 6000, 'no verified cap: nothing counted');
  r := public.cost_projection(st, array['contract-four'], '2026-27',
         '{"residency": "in_state", "prior_credits": 90, "years": 1, "credits_per_term": 6}');
  perform hp_test.eq((r->'institutions'->0->'levers'->0->>'terms_saved')::numeric, 1::numeric, 'at least one term is left');
  r := public.cost_projection(st, array['contract-four'], '2026-27', '{"residency": "in_state"}');
  perform hp_test.check(r->'institutions'->0->'levers'->0->>'reason' = 'no_prior_credits'
    and (r->'institutions'->0->>'optimized_total')::numeric = 36000, 'no lever without stated credits');

  perform hp_test.expect_error(format($q$select public.cost_projection(%L, array['contract-four'], '2026-27', '{}')$q$, st), '22023', '%residency%');
  perform hp_test.expect_error(format($q$select public.cost_projection(%L, array['contract-four'], '2026-27', '{"residency":"in_state","merit":1}')$q$, st), '22023');
  perform hp_test.expect_error(format($q$select public.cost_projection(%L, array['contract-four'], '2026-27', '{"residency":"in_state","years":7}')$q$, st), '22023');
  perform hp_test.expect_error(format($q$select public.cost_projection(%L, array['contract-four'], '2026-27', '{"residency":"in_state","years":"x"}')$q$, st), '22023');
  perform hp_test.expect_error(format($q$select public.cost_projection(%L, array['contract-four'], '2026', '{"residency":"in_state"}')$q$, st), '22023');

  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.check(public.cost_projection(st, array['contract-four'], '2026-27', '{"residency":"in_state"}') is not null, 'student can project');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.expect_error(format($q$select public.cost_projection(%L, array['contract-four'], '2026-27', '{"residency":"in_state"}')$q$, st), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error(format($q$select public.cost_projection(%L, array['contract-four'], '2026-27', '{"residency":"in_state"}')$q$, st), '42501');
  perform hp_test.as_anon();
  perform hp_test.expect_error(format($q$select public.cost_projection(%L, array['contract-four'], '2026-27', '{"residency":"in_state"}')$q$, st), '42501');
  perform hp_test.as_owner();
end $$;

-- CR-4 v2: one price for everyone, cost components, exam credit from the school's own table, residency rule.
insert into public.institutions(id, institution_key, ipeds_name, display_name, state_code, city, control, level, source_id,
  verification_status, last_verified_at, identity_academic_year) values
 ('50000000-0000-0000-0000-000000000004', 'contract-private', 'Private', 'Private U', 'TN', 'Nashville', 'private', 'four_year',
  '50000000-0000-0000-0000-000000000001', 'verified', current_date, '2023-24');
insert into public.institution_costs(institution_id, academic_year, residency, tuition, mandatory_fees, on_campus_food_housing,
  books_supplies, transportation, personal_misc, total_cost_of_attendance, source_id, verification_status, last_verified_at) values
 ('50000000-0000-0000-0000-000000000004', '2026-27', 'not_applicable', 40000, 1000, 12000, 1200, 1500, 2300, 58000,
  '50000000-0000-0000-0000-000000000001', 'verified', current_date);
insert into public.credit_policies(institution_id, policy_kind, academic_year, policy_url, general_limit_credits, source_id, verification_status, last_verified_at) values
 ('50000000-0000-0000-0000-000000000004', 'AP', '2026-27', 'https://example.edu/ap', 18, '50000000-0000-0000-0000-000000000001', 'verified', current_date);
insert into public.transfer_policies(institution_id, academic_year, policy_url, max_transfer_credits, residency_requirement_credits, source_id, verification_status, last_verified_at) values
 ('50000000-0000-0000-0000-000000000004', '2026-27', 'https://example.edu/transfer', 60, 100, '50000000-0000-0000-0000-000000000001', 'verified', current_date);
do $$
declare r jsonb; i jsonb; c jsonb; st uuid := current_setting('t.st')::uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  r := public.cost_projection(st, array['contract-private'], '2026-27', '{"residency": "in_state", "exam_credits": 24}');
  perform hp_test.check(r->>'definition' = 'v2', 'definition v2');
  i := r->'institutions'->0;
  perform hp_test.check(i->>'status' = 'ok' and i->'cost'->>'residency' = 'not_applicable'
    and i->'cost'->>'residency_requested' = 'in_state', 'one price for everyone is used, and said so');
  perform hp_test.eq((i->>'baseline_total')::numeric, 164000::numeric, 'tuition and fees x 4 years');
  c := i->'cost'->'components';
  perform hp_test.check((c->>'tuition')::numeric = 40000 and (c->>'mandatory_fees')::numeric = 1000
    and (c->>'housing_food')::numeric = 12000 and (c->>'living_and_other')::numeric = 17000, 'components kept apart ' || c::text);
  perform hp_test.check((i->'levers'->1->>'accepted_upper_bound')::numeric = 18 and i->'levers'->1->>'reason' = 'bounded_by_verified_limit',
    'exam credit bounded by the verified AP limit');
  c := i->'credit_savings';
  perform hp_test.check(c->>'certainty' = 'potential' and c->'assumes' ? 'schedule_allows_finishing_early',
    'credit savings are labelled potential, with their assumptions');
  perform hp_test.check(c->>'mechanism' = 'fewer_terms' and c->>'billing_structure' = 'unknown'
    and (c->>'terms_saved')::int = 1 and (c->>'remainder_credits')::numeric = 3, 'one term saved, three credits short of another ' || c::text);
  perform hp_test.eq((i->>'savings_total')::numeric, 20500::numeric, 'one term of tuition and fees');
  perform hp_test.check((c->'by_component'->>'tuition')::numeric = 20000 and (c->'by_component'->>'mandatory_fees')::numeric = 500
    and c->'by_component'->'living_and_other' = 'null'::jsonb, 'living costs are not in a tuition-and-fees saving');
  perform hp_test.check(i->'not_counted'->>'loans' = 'no_data', 'no loan data is claimed');

  r := public.cost_projection(st, array['contract-private'], '2026-27',
         '{"residency": "out_of_state", "cost_basis": "cost_of_attendance", "exam_credits": 24, "prior_credits": 30}');
  i := r->'institutions'->0;
  c := i->'credit_savings';
  perform hp_test.check((c->>'outside_credit_max')::numeric = 20 and (c->>'credits_counted')::numeric = 20,
    'residency rule: 120 planned credits minus 100 at the school leaves 20 ' || c::text);
  perform hp_test.check((i->'levers'->0->>'accepted_upper_bound')::numeric + (i->'levers'->1->>'accepted_upper_bound')::numeric = 20,
    'levers share the bounded total');
  perform hp_test.eq((i->>'savings_total')::numeric, 29000::numeric, 'one term of full cost of attendance');
  perform hp_test.eq((c->'by_component'->>'living_and_other')::numeric, 8500::numeric, 'a term saved includes its living costs');

  r := public.cost_projection(st, array['contract-private'], '2026-27', '{"residency": "in_state", "exam_credits": 10}');
  i := r->'institutions'->0;
  perform hp_test.check(i->'levers'->1->>'reason' = 'less_than_one_term' and (i->>'savings_total')::numeric = 0
    and (i->'credit_savings'->>'remainder_credits')::numeric = 10, 'under a term: nothing counted, remainder shown');

  r := public.cost_projection(st, array['contract-four'], '2026-27', '{"residency": "out_of_state", "exam_credits": 30}');
  perform hp_test.check(r->'institutions'->0->>'status' = 'missing_cost' and r->'institutions'->0->'cost' = 'null'::jsonb,
    'no fallback to an unverified price');
  r := public.cost_projection(st, array['contract-four'], '2026-27', '{"residency": "in_state", "exam_credits": 30}');
  perform hp_test.check((r->'institutions'->0->'levers'->1->>'accepted_upper_bound')::numeric = 6
    and r->'institutions'->0->'levers'->1->>'reason' = 'less_than_one_term', 'a 6-credit AP limit is under one term');
  r := public.cost_projection(st, array['contract-two'], '2023-24', '{"residency": "in_state", "exam_credits": 30}');
  i := r->'institutions'->0;
  perform hp_test.check(i->'levers'->1->>'reason' = 'from_school_table' and (i->'credit_savings'->>'terms_saved')::int = 2
    and (i->>'savings_total')::numeric = 3000, 'exam credit with no published limit: two terms ' || i::text);
  perform hp_test.expect_error(format($q$select public.cost_projection(%L, array['contract-four'], '2026-27', '{"residency":"in_state","exam_credits":91}')$q$, st), '22023');
  perform hp_test.as_owner();
end $$;

-- CR-11 award test criteria: shape is enforced, and compare_institutions serves the columns.
do $$ begin
  perform hp_test.as_owner();
  insert into public.institutional_awards(institution_id, award_name, academic_year, award_type, test_requirement,
    test_criteria_kind, act_min, sat_min, source_id, verification_status, last_verified_at)
  values ('50000000-0000-0000-0000-000000000002', 'Test Minimum Merit', '2026-27', 'merit', 'Minimum 31 ACT / 1390 SAT.',
    'single_minimum', 31, 1390, '50000000-0000-0000-0000-000000000001', 'verified', current_date);
  perform hp_test.expect_error($q$insert into public.institutional_awards(institution_id, award_name, academic_year, award_type, test_criteria_kind, act_min, act_max, source_id, verification_status)
    values ('50000000-0000-0000-0000-000000000002', 'Bad 1', '2026-27', 'merit', 'single_minimum', 30, 36, '50000000-0000-0000-0000-000000000001', 'unverified')$q$, '23514');
  perform hp_test.expect_error($q$insert into public.institutional_awards(institution_id, award_name, academic_year, award_type, test_criteria_kind, act_min, source_id, verification_status)
    values ('50000000-0000-0000-0000-000000000002', 'Bad 2', '2026-27', 'merit', 'range', 30, '50000000-0000-0000-0000-000000000001', 'unverified')$q$, '23514');
  perform hp_test.expect_error($q$insert into public.institutional_awards(institution_id, award_name, academic_year, award_type, act_min, source_id, verification_status)
    values ('50000000-0000-0000-0000-000000000002', 'Bad 3', '2026-27', 'merit', 30, '50000000-0000-0000-0000-000000000001', 'unverified')$q$, '23514');
  perform hp_test.expect_error($q$insert into public.institutional_awards(institution_id, award_name, academic_year, award_type, test_criteria_kind, sat_min, source_id, verification_status)
    values ('50000000-0000-0000-0000-000000000002', 'Bad 4', '2026-27', 'merit', 'single_minimum', 1700, '50000000-0000-0000-0000-000000000001', 'unverified')$q$, '23514');
  perform hp_test.eq((select a->>'act_min' from jsonb_array_elements(
      public.compare_institutions(array[(select institution_key from public.institutions where id = '50000000-0000-0000-0000-000000000002')], '2026-27')
        ->'institutions'->0->'domains'->'awards') a where a->>'award_name' = 'Test Minimum Merit'), '31', 'compare_institutions serves act_min');
  delete from public.institutional_awards where award_name = 'Test Minimum Merit';
end $$;

-- CR-10 exam plan: student and view_progress guardians read; guardians and the linked student write.
do $$ declare i int; begin
  perform hp_test.as_owner();
  insert into public.exam_catalog values ('ap:biology', 'ap', 'Biology'), ('clep:biology', 'clep', 'Biology');
  insert into public.exam_catalog select 'ap:extra-' || n, 'ap', 'Extra ' || n from generate_series(1, 20) n;
  perform hp_test.expect_error($q$insert into public.exam_catalog values ('clep:x', 'ap', 'X')$q$, '23514');
  perform hp_test.as_anon();
  perform hp_test.eq((select count(*) from public.exam_catalog where exam_key like '%biology'), 2::bigint, 'catalog is public');
  perform hp_test.expect_error('select count(*) from public.student_exam_plan', '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  insert into public.student_exam_plan(student_id, exam_key) values (current_setting('t.st')::uuid, 'ap:biology');
  update public.student_exam_plan set score = 4, taken_on = date '2026-05-12' where exam_key = 'ap:biology';
  perform hp_test.expect_error(format($q$update public.student_exam_plan set score = 6 where student_id = %L and exam_key = 'ap:biology'$q$, current_setting('t.st')), '23514');
  perform hp_test.expect_error(format($q$insert into public.student_exam_plan(student_id, exam_key) values (%L, 'ap:no-such')$q$, current_setting('t.st')), '23503');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  insert into public.student_exam_plan(student_id, exam_key, score) values (current_setting('t.st')::uuid, 'clep:biology', 55);
  perform hp_test.expect_error(format($q$update public.student_exam_plan set score = 5 where student_id = %L and exam_key = 'clep:biology'$q$, current_setting('t.st')), '23514');
  perform hp_test.eq((select count(*) from public.student_exam_plan), 2::bigint, 'student reads the plan');
  perform hp_test.check((select set_by from public.student_exam_plan where exam_key = 'clep:biology') = '20000000-0000-0000-0000-000000000051', 'set_by recorded');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq((select count(*) from public.student_exam_plan), 0::bigint, 'guardian without view_progress reads nothing');
  insert into public.student_exam_plan(student_id, exam_key) values (current_setting('t.st')::uuid, 'ap:extra-1');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error(format($q$insert into public.student_exam_plan(student_id, exam_key) values (%L, 'ap:extra-2')$q$, current_setting('t.st')), '42501');
  perform hp_test.eq((select count(*) from public.student_exam_plan), 0::bigint, 'outsider reads nothing');
  delete from public.student_exam_plan;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((select count(*) from public.student_exam_plan), 3::bigint, 'outsider deleted nothing');
  for i in 2..18 loop
    insert into public.student_exam_plan(student_id, exam_key) values (current_setting('t.st')::uuid, 'ap:extra-' || i);
  end loop;
  perform hp_test.expect_error(format($q$insert into public.student_exam_plan(student_id, exam_key) values (%L, 'ap:extra-19')$q$, current_setting('t.st')), '22023', '%up to 20%');
  delete from public.student_exam_plan where exam_key = 'ap:extra-18';
  insert into public.student_exam_plan(student_id, exam_key) values (current_setting('t.st')::uuid, 'ap:extra-19');
  perform hp_test.as_owner();
end $$;

-- CR-13 academic interests: student and view_progress guardians read; guardians and the linked student write.
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  insert into public.student_academic_interests(student_id, certainty, interests)
  values (current_setting('t.st')::uuid, 'few', '[{"kind":"major","key":"computer-science"},{"kind":"area","key":"engineering","focus":true}]');
  perform hp_test.expect_error(format($q$update public.student_academic_interests set certainty = 'maybe' where student_id = %L$q$, current_setting('t.st')), '23514');
  perform hp_test.expect_error(format($q$update public.student_academic_interests set interests = '[{"kind":"club","key":"chess"}]' where student_id = %L$q$, current_setting('t.st')), '23514');
  perform hp_test.expect_error(format($q$update public.student_academic_interests set interests = '[{"kind":"major","key":"Computer Science"}]' where student_id = %L$q$, current_setting('t.st')), '23514');
  perform hp_test.expect_error(format($q$update public.student_academic_interests set interests = '[{"kind":"major","key":"a"},{"kind":"major","key":"a"}]' where student_id = %L$q$, current_setting('t.st')), '23514');
  perform hp_test.expect_error(format($q$update public.student_academic_interests set interests = '[{"kind":"major","key":"a","focus":true},{"kind":"major","key":"b","focus":true}]' where student_id = %L$q$, current_setting('t.st')), '23514');
  perform hp_test.expect_error(format($q$update public.student_academic_interests set interests = '[{"kind":"major","key":"a","note":"x"}]' where student_id = %L$q$, current_setting('t.st')), '23514');
  perform hp_test.expect_error(format($q$update public.student_academic_interests set interests = (select jsonb_agg(jsonb_build_object('kind','major','key','k'||n)) from generate_series(1,9) n) where student_id = %L$q$, current_setting('t.st')), '23514');
  update public.student_academic_interests set interests = (select jsonb_agg(jsonb_build_object('kind','major','key','k'||n)) from generate_series(1,8) n) where student_id = current_setting('t.st')::uuid;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  update public.student_academic_interests set certainty = null, interests = '[]' where student_id = current_setting('t.st')::uuid;
  perform hp_test.eq((select count(*) from public.student_academic_interests where certainty is null and interests = '[]'), 1::bigint, 'student clears; nothing is required');
  perform hp_test.check((select set_by from public.student_academic_interests) = '20000000-0000-0000-0000-000000000051', 'set_by follows the writer');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq((select count(*) from public.student_academic_interests), 0::bigint, 'guardian without view_progress reads nothing');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.eq((select count(*) from public.student_academic_interests), 0::bigint, 'outsider reads nothing');
  update public.student_academic_interests set certainty = 'sure';
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((select count(*) from public.student_academic_interests where certainty = 'sure'), 0::bigint, 'outsider changed nothing');
  perform hp_test.as_anon();
  perform hp_test.expect_error('select count(*) from public.student_academic_interests', '42501');
  perform hp_test.as_owner();
end $$;

rollback;
\o
\echo frontend contract tests passed

