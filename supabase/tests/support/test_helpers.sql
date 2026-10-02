-- Assertion and impersonation helpers for the household/practice tests. Include inside the test transaction.
create schema hp_test;
-- Runs p_sql and requires it to fail with p_state (and, if given, a message matching p_like).
create function hp_test.expect_error(p_sql text, p_state text, p_like text default null) returns void
language plpgsql as $$
begin
  begin
    execute p_sql;
  exception when others then
    if sqlstate <> p_state or (p_like is not null and sqlerrm not ilike p_like) then
      raise exception 'Expected % (%) from [%], got %: %', p_state, coalesce(p_like, '*'), p_sql, sqlstate, sqlerrm;
    end if;
    return;
  end;
  raise exception 'Expected % from [%], but it succeeded', p_state, p_sql;
end $$;
create function hp_test.check(p_ok boolean, p_msg text) returns void language plpgsql as $$
begin if p_ok is not true then raise exception 'Assertion failed: %', p_msg; end if; end $$;
create function hp_test.eq(p_got anycompatible, p_want anycompatible, p_msg text) returns void language plpgsql as $$
begin
  if p_got is distinct from p_want then raise exception 'Assertion failed: % (got %, want %)', p_msg, p_got, p_want; end if;
end $$;
-- Become an authenticated user (or anon) for the rest of the transaction, or return to the test owner.
create function hp_test.as_user(p_user uuid) returns void language plpgsql as $$
begin
  perform set_config('role', 'authenticated', true);
  perform set_config('request.jwt.claim.sub', p_user::text, true);
end $$;
create function hp_test.as_anon() returns void language plpgsql as $$
begin
  perform set_config('role', 'anon', true);
  perform set_config('request.jwt.claim.sub', '', true);
end $$;
create function hp_test.as_owner() returns void language plpgsql as $$
begin
  perform set_config('role', 'none', true);
  perform set_config('request.jwt.claim.sub', '', true);
end $$;
grant usage on schema hp_test to anon, authenticated;
grant execute on all functions in schema hp_test to anon, authenticated;

-- Fixed users: guardians g1/g2 (household A), gb (household B), students s1..s3, outsider x.
insert into auth.users(id) values
 ('20000000-0000-0000-0000-0000000000a1'), ('20000000-0000-0000-0000-0000000000a2'),
 ('20000000-0000-0000-0000-0000000000b1'), ('20000000-0000-0000-0000-000000000051'),
 ('20000000-0000-0000-0000-000000000052'), ('20000000-0000-0000-0000-000000000053'),
 ('20000000-0000-0000-0000-000000000099');

-- Synthetic catalog: SAT digital with two question types, a skill tree, traps and strategies.
insert into public.exam_families(key, name) values ('sat', 'SAT'), ('act', 'ACT');
insert into public.exam_versions(id, exam_family, version_key, name, effective_from, rules) values
 ('40000000-0000-0000-0000-000000000001', 'sat', 'sat_digital_2024', 'Digital SAT', '2024-03-01',
  '{"sections":[{"key":"math","modules":2,"minutes":70,"questions":44,"calculator":"allowed"}],"scale":{"min":400,"max":1600}}'),
 ('40000000-0000-0000-0000-000000000002', 'act', 'act_enhanced_2025', 'Enhanced ACT', '2025-04-01',
  '{"sections":[{"key":"math","minutes":50,"questions":45}],"scale":{"min":1,"max":36},"science_optional":true}');
insert into public.question_types(id, exam_version_id, type_key, name) values
 ('41000000-0000-0000-0000-000000000001', '40000000-0000-0000-0000-000000000001', 'multiple_choice', 'Multiple choice'),
 ('41000000-0000-0000-0000-000000000002', '40000000-0000-0000-0000-000000000001', 'student_produced_response', 'Student-produced response');
insert into public.skills(id, parent_id, exam_family, section, domain, skill_key, name) values
 ('42000000-0000-0000-0000-000000000000', null, 'sat', 'math', 'algebra', 'algebra', 'Algebra'),
 ('42000000-0000-0000-0000-00000000000a', '42000000-0000-0000-0000-000000000000', 'sat', 'math', 'algebra', 'linear_equations', 'Linear equations'),
 ('42000000-0000-0000-0000-00000000000b', null, 'sat', 'reading', 'information', 'inference', 'Inference'),
 ('42000000-0000-0000-0000-00000000000c', null, 'sat', 'math', 'data', 'data_analysis', 'Data analysis'),
 ('42000000-0000-0000-0000-00000000000d', '42000000-0000-0000-0000-000000000000', 'sat', 'math', 'algebra', 'ratios', 'Ratios');
insert into public.trap_types(id, trap_key, name) values
 ('43000000-0000-0000-0000-000000000001', 'sign_error', 'Sign error'),
 ('43000000-0000-0000-0000-000000000002', 'partial_answer', 'Answers an intermediate step');
insert into public.question_strategies(id, strategy_key, name) values
 ('31000000-0000-0000-0000-000000000001', 'process_of_elimination', 'Process of elimination'),
 ('31000000-0000-0000-0000-000000000002', 'backsolve', 'Backsolve'),
 ('31000000-0000-0000-0000-000000000003', 'plug_in_numbers', 'Plug in numbers');
-- q1..q8: id suffix = question number. q5 is a draft.
insert into public.practice_questions(id, exam_version_id, question_type_id, section, difficulty, difficulty_label, stem, choices,
  answer_format, accepted_answers, hints, teaching_explanation, strategy_explanation, expected_time_seconds, status)
select ('30000000-0000-0000-0000-00000000000' || n)::uuid, '40000000-0000-0000-0000-000000000001',
  case when fmt = 'numeric' then '41000000-0000-0000-0000-000000000002' else '41000000-0000-0000-0000-000000000001' end::uuid,
  section, 2, 'medium', 'Question ' || n, case when fmt = 'numeric' then '[]' else '["A","B","C","D"]' end::jsonb,
  fmt, answers::jsonb, hints::jsonb, 'Teaching ' || n, 'Strategy ' || n, secs, status
from (values
  (1, 'math', 'choice', '["B"]', '["First hint","Second hint"]', 60, 'published'),
  (2, 'math', 'numeric', '["1/2"]', '[]', 90, 'published'),
  (3, 'reading', 'choice', '["C"]', '[]', 60, 'published'),
  (4, 'math', 'choice', '["A"]', '[]', 60, 'published'),
  (5, 'math', 'choice', '["A"]', '[]', 30, 'draft'),
  (6, 'math', 'choice', '["D"]', '[]', 120, 'published'),
  (7, 'reading', 'choice', '["A"]', '[]', 60, 'published'),
  (8, 'math', 'choice', '["B"]', '[]', 60, 'published')) v(n, section, fmt, answers, hints, secs, status);
insert into public.practice_question_skills(question_id, skill_id, is_primary) values
 ('30000000-0000-0000-0000-000000000001', '42000000-0000-0000-0000-00000000000a', true),
 ('30000000-0000-0000-0000-000000000002', '42000000-0000-0000-0000-00000000000a', true),
 ('30000000-0000-0000-0000-000000000003', '42000000-0000-0000-0000-00000000000b', true),
 ('30000000-0000-0000-0000-000000000004', '42000000-0000-0000-0000-00000000000d', true),
 ('30000000-0000-0000-0000-000000000005', '42000000-0000-0000-0000-00000000000a', true),
 ('30000000-0000-0000-0000-000000000006', '42000000-0000-0000-0000-00000000000a', true),
 ('30000000-0000-0000-0000-000000000007', '42000000-0000-0000-0000-00000000000b', true),
 ('30000000-0000-0000-0000-000000000008', '42000000-0000-0000-0000-00000000000c', true),
 ('30000000-0000-0000-0000-000000000001', '42000000-0000-0000-0000-00000000000d', false);
insert into public.practice_question_distractors(question_id, choice_key, rationale, trap_type_id) values
 ('30000000-0000-0000-0000-000000000001', 'A', 'Dropped the negative sign.', '43000000-0000-0000-0000-000000000001'),
 ('30000000-0000-0000-0000-000000000001', 'C', 'Stopped after the first step.', '43000000-0000-0000-0000-000000000002');
insert into public.practice_question_strategies(question_id, strategy_id, role, is_fastest, strategy_explanation) values
 ('30000000-0000-0000-0000-000000000001', '31000000-0000-0000-0000-000000000002', 'primary', true, 'Try each choice in the equation.'),
 ('30000000-0000-0000-0000-000000000001', '31000000-0000-0000-0000-000000000001', 'secondary', false, 'Two choices have the wrong sign.'),
 ('30000000-0000-0000-0000-000000000005', '31000000-0000-0000-0000-000000000001', 'primary', false, null);
