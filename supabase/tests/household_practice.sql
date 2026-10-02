-- Household, student-access and practice-progress tests. Synthetic fixtures; everything is rolled back.
-- Users are simulated with `set local role authenticated` plus request.jwt.claim.sub (see support/auth_stub.sql).
-- Any failed assertion raises an exception; run with psql -v ON_ERROR_STOP=1.
\set QUIET on
\o /dev/null
begin;
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
grant usage on schema hp_test to anon, authenticated;
grant execute on all functions in schema hp_test to anon, authenticated;

-- Guardian A, guardian B, student users 1 and 2 (siblings in household A), an unrelated user.
insert into auth.users(id) values
 ('20000000-0000-0000-0000-0000000000a1'), ('20000000-0000-0000-0000-0000000000b1'),
 ('20000000-0000-0000-0000-000000000051'), ('20000000-0000-0000-0000-000000000052'),
 ('20000000-0000-0000-0000-000000000099');
insert into public.question_strategies(id, strategy_key, name) values
 ('31000000-0000-0000-0000-000000000001', 'process_of_elimination', 'Process of elimination'),
 ('31000000-0000-0000-0000-000000000002', 'backsolve', 'Backsolve');
insert into public.practice_questions(id, exam_family, subject, domain, skill, difficulty, stem, choices, correct_answer, explanation, distractor_rationales, status) values
 ('30000000-0000-0000-0000-000000000001', 'SAT', 'math', 'algebra', 'linear_equations', 'easy', 'Solve 2x = 4', '["A","B","C","D"]', 'B', 'Divide by 2.', '{"A":"sign error"}', 'published'),
 ('30000000-0000-0000-0000-000000000002', 'SAT', 'reading', 'information', 'inference', 'medium', 'Passage...', '["A","B","C","D"]', 'C', 'Line 4.', '{}', 'published'),
 ('30000000-0000-0000-0000-000000000003', 'SAT', 'math', 'algebra', 'linear_equations', 'hard', 'Draft question', '["A","B"]', 'A', 'Draft.', '{}', 'draft');
insert into public.practice_question_strategies(question_id, strategy_id) values
 ('30000000-0000-0000-0000-000000000001', '31000000-0000-0000-0000-000000000002'),
 ('30000000-0000-0000-0000-000000000003', '31000000-0000-0000-0000-000000000001');

-- Anon gets nothing.
set local role anon;
do $$
declare t text;
begin
  foreach t in array array['profiles','households','household_members','students','household_invitations',
    'question_strategies','practice_questions','practice_question_strategies','weekly_practice_goals',
    'practice_sessions','practice_attempts'] loop
    perform hp_test.check(not has_any_column_privilege('public.' || t, 'SELECT,INSERT,UPDATE'), 'anon has privilege on ' || t);
    perform hp_test.check(not has_table_privilege('public.' || t, 'DELETE'), 'anon can delete ' || t);
  end loop;
  perform hp_test.expect_error('select public.create_household(''x'')', '42501');
  perform hp_test.expect_error('select public.student_weekly_progress(gen_random_uuid(), ''2026-09-07'')', '42501');
  perform hp_test.expect_error('select public.can_view_student(gen_random_uuid())', '42501');
end $$;
reset role;

set local role authenticated;
select set_config('request.jwt.claim.sub', '', true);
select hp_test.expect_error('select public.create_household(''No user'')', '42501', 'Authentication required');

-- Guardian A: household, two students, student invitations.
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-0000000000a1', true);
select set_config('t.hh_a', public.create_household('Household A')::text, true);
select set_config('t.st1', public.add_student(current_setting('t.hh_a')::uuid, 'Student One', 2028, 10)::text, true);
select set_config('t.st2', public.add_student(current_setting('t.hh_a')::uuid, 'Student Two', 2030, 8)::text, true);
select set_config('t.inv1', public.create_household_invitation(current_setting('t.hh_a')::uuid, 'student', current_setting('t.st1')::uuid), true);
select set_config('t.inv2', public.create_household_invitation(current_setting('t.hh_a')::uuid, 'student', current_setting('t.st2')::uuid, 1), true);
select set_config('t.inv_g', public.create_household_invitation(current_setting('t.hh_a')::uuid, 'guardian'), true);
do $$ begin
  perform hp_test.check(current_setting('t.inv1') ~ '^[0-9a-f]{64}$', 'invitation code format');
  perform hp_test.check((select count(*) from public.household_invitations) = 3, 'guardian reads own invitations');
  perform hp_test.check((select bool_and(s.account_mode = 'guardian_managed' and s.linked_user_id is null) from public.students s), 'new students are guardian managed');
  perform hp_test.expect_error('select code_hash from public.household_invitations', '42501');
  perform hp_test.expect_error('select public.create_household_invitation(current_setting(''t.hh_a'')::uuid, ''student'')', '22023');
  perform hp_test.expect_error('select public.create_household_invitation(current_setting(''t.hh_a'')::uuid, ''guardian'', null, 337)', '22023');
  perform hp_test.expect_error('select public.create_household_invitation(current_setting(''t.hh_a'')::uuid, ''owner'')', '22023');
  -- Clients cannot write households/members/students directly.
  perform hp_test.expect_error('insert into public.household_members values (current_setting(''t.hh_a'')::uuid, ''20000000-0000-0000-0000-000000000099'', ''guardian'')', '42501');
  perform hp_test.expect_error('insert into public.students(household_id, display_name) values (current_setting(''t.hh_a'')::uuid, ''x'')', '42501');
  perform hp_test.expect_error('update public.students set linked_user_id = auth.uid()', '42501');
end $$;
-- Goals: Monday only, guardian-managed.
insert into public.weekly_practice_goals(student_id, week_start, target_questions, target_minutes)
values (current_setting('t.st1')::uuid, '2026-09-07', 4, 10);
select hp_test.expect_error($$insert into public.weekly_practice_goals(student_id, week_start, target_questions)
  values (current_setting('t.st1')::uuid, '2026-09-08', 4)$$, '23514');
select hp_test.expect_error($$insert into public.weekly_practice_goals(student_id, week_start) values (current_setting('t.st1')::uuid, '2026-09-14')$$, '23514');
select hp_test.expect_error($$insert into public.weekly_practice_goals(student_id, week_start, target_questions)
  values (current_setting('t.st1')::uuid, '2026-09-07', 9)$$, '23505');

-- Guardian B: separate household; no reach into household A.
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-0000000000b1', true);
select set_config('t.hh_b', public.create_household('Household B')::text, true);
select set_config('t.st3', public.add_student(current_setting('t.hh_b')::uuid, 'Student Three')::text, true);
select set_config('t.inv3', public.create_household_invitation(current_setting('t.hh_b')::uuid, 'student', current_setting('t.st3')::uuid), true);
insert into public.weekly_practice_goals(student_id, week_start, target_minutes) values (current_setting('t.st3')::uuid, '2026-09-07', 30);
do $$ begin
  perform hp_test.check((select count(*) from public.students) = 1, 'guardian B sees only own student');
  perform hp_test.check((select count(*) from public.households) = 1, 'guardian B sees only own household');
  perform hp_test.check((select count(*) from public.weekly_practice_goals) = 1, 'guardian B sees only own goals');
  perform hp_test.check((select count(*) from public.household_invitations) = 1, 'guardian B sees only own invitations');
  perform hp_test.expect_error('select public.add_student(current_setting(''t.hh_a'')::uuid, ''Intruder'')', '42501');
  perform hp_test.expect_error('select public.create_household_invitation(current_setting(''t.hh_a'')::uuid, ''guardian'')', '42501');
  perform hp_test.expect_error($q$insert into public.weekly_practice_goals(student_id, week_start, target_questions)
    values (current_setting('t.st1')::uuid, '2026-09-14', 1)$q$, '42501');
  perform hp_test.expect_error('select public.student_weekly_progress(current_setting(''t.st1'')::uuid, ''2026-09-07'')', '42501');
end $$;
update public.weekly_practice_goals set target_questions = 99 where student_id = current_setting('t.st1')::uuid;
reset role;
select hp_test.check((select target_questions from public.weekly_practice_goals where student_id = current_setting('t.st1')::uuid) = 4, 'guardian B changed household A goal');

-- Invitations: accept links the student, single use, expiry checked.
set local role authenticated;
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-000000000051', true);
select hp_test.check(public.accept_household_invitation(current_setting('t.inv1')) = current_setting('t.hh_a')::uuid, 'student 1 joins household A');
select hp_test.expect_error('select public.accept_household_invitation(current_setting(''t.inv1''))', '22023', '%already been used%');
select hp_test.expect_error('select public.accept_household_invitation(''not-a-code'')', '22023', '%Invalid%');
select hp_test.expect_error('select public.accept_household_invitation(current_setting(''t.inv3''))', '22023', '%already linked to another student%');
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-000000000052', true);
select hp_test.expect_error('select public.accept_household_invitation(current_setting(''t.inv1''))', '22023', '%already been used%');
reset role;
update public.household_invitations set expires_at = now() - interval '1 second'
where code_hash = encode(sha256(convert_to(current_setting('t.inv_g'), 'UTF8')), 'hex');
set local role authenticated;
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-000000000099', true);
select hp_test.expect_error('select public.accept_household_invitation(current_setting(''t.inv_g''))', '22023', '%expired%');
do $$ begin
  perform hp_test.check((select count(*) from public.households) = 0, 'outsider sees no households');
  perform hp_test.check((select count(*) from public.students) = 0, 'outsider sees no students');
end $$;
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-000000000052', true);
select public.accept_household_invitation(current_setting('t.inv2'));
reset role;
do $$ begin
  perform hp_test.check((select linked_user_id = '20000000-0000-0000-0000-000000000051' and account_mode = 'student_login'
    from public.students where id = current_setting('t.st1')::uuid), 'student 1 linked');
  perform hp_test.check((select role from public.household_members where user_id = '20000000-0000-0000-0000-000000000051') = 'student', 'student membership role');
  perform hp_test.check((select accepted_by = '20000000-0000-0000-0000-000000000051' from public.household_invitations
    where code_hash = encode(sha256(convert_to(current_setting('t.inv1'), 'UTF8')), 'hex')), 'invitation marked accepted');
  perform hp_test.check(not exists (select 1 from public.household_members where user_id = '20000000-0000-0000-0000-000000000099'), 'expired invitation added member');
end $$;

-- Student 1: question visibility, own goal, practice flow.
set local role authenticated;
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-000000000051', true);
do $$
declare v_attempt uuid; r record;
begin
  perform hp_test.check((select count(*) from public.practice_questions) = 2, 'drafts hidden');
  perform hp_test.check((select count(*) from public.practice_question_strategies) = 1, 'draft strategy links hidden');
  perform hp_test.expect_error('select correct_answer from public.practice_questions', '42501');
  perform hp_test.expect_error('select explanation from public.practice_questions', '42501');
  perform hp_test.expect_error('select distractor_rationales from public.practice_questions', '42501');
  perform hp_test.expect_error('select * from public.practice_questions', '42501');
  perform hp_test.check((select count(*) from public.students) = 1, 'student sees only own student profile');
  perform hp_test.check((select count(*) from public.weekly_practice_goals) = 1, 'student reads own goal');
  perform hp_test.check((select count(*) from public.household_invitations) = 0, 'student cannot read invitations');
  perform hp_test.check((select count(*) from public.household_members) = 1, 'student sees only own membership');
  perform hp_test.expect_error($q$insert into public.weekly_practice_goals(student_id, week_start, target_questions)
    values (current_setting('t.st1')::uuid, '2026-09-14', 100)$q$, '42501');
  perform hp_test.expect_error($q$insert into public.practice_attempts(student_id, question_id, is_correct)
    values (current_setting('t.st1')::uuid, '30000000-0000-0000-0000-000000000001', true)$q$, '42501');
  perform hp_test.expect_error('select public.start_practice_attempt(current_setting(''t.st2'')::uuid, ''30000000-0000-0000-0000-000000000001'')', '42501');
  perform hp_test.expect_error('select public.start_practice_attempt(current_setting(''t.st1'')::uuid, ''30000000-0000-0000-0000-000000000003'')', '22023', '%not available%');
  insert into public.profiles(id, display_name) values (auth.uid(), 'Sam');
  perform hp_test.expect_error($q$insert into public.profiles(id) values ('20000000-0000-0000-0000-000000000052')$q$, '42501');
end $$;
select set_config('t.session', public.start_practice_session(current_setting('t.st1')::uuid)::text, true);
select set_config('t.a1', public.start_practice_attempt(current_setting('t.st1')::uuid, '30000000-0000-0000-0000-000000000001', current_setting('t.session')::uuid)::text, true);
select hp_test.expect_error($$update public.practice_attempts set is_correct = true$$, '42501');
select hp_test.expect_error($$delete from public.practice_attempts$$, '42501');

-- Guardian A cannot practise as the student or submit for them.
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-0000000000a1', true);
select hp_test.expect_error('select public.start_practice_attempt(current_setting(''t.st1'')::uuid, ''30000000-0000-0000-0000-000000000001'')', '42501', '%own login%');
select hp_test.expect_error('select public.submit_practice_attempt(current_setting(''t.a1'')::uuid, ''B'')', '42501');
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-000000000052', true);
select hp_test.expect_error('select public.submit_practice_attempt(current_setting(''t.a1'')::uuid, ''B'')', '42501');
select set_config('t.a_sib', public.start_practice_attempt(current_setting('t.st2')::uuid, '30000000-0000-0000-0000-000000000002')::text, true);
reset role;

-- now() is fixed within this transaction, so backdate presentation to get a measurable server elapsed time.
update public.practice_attempts set presented_at = now() - interval '90 seconds';
set local role authenticated;
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-000000000051', true);
do $$
declare r record;
begin
  perform hp_test.expect_error('select public.submit_practice_attempt(current_setting(''t.a1'')::uuid, ''B'', -1)', '22023');
  perform hp_test.expect_error('select public.submit_practice_attempt(current_setting(''t.a1'')::uuid, ''B'', null, null, -1)', '22023');
  perform hp_test.expect_error('select public.submit_practice_attempt(current_setting(''t.a1'')::uuid, ''B'', 90001)', '22023', '%exceeds%');
  perform hp_test.expect_error('select public.submit_practice_attempt(current_setting(''t.a1'')::uuid, ''B'', null, null, 0, false, ''no_such'')', '22023');
  select * into r from public.submit_practice_attempt(current_setting('t.a1')::uuid, 'B', 60000, 1500, 0, false, 'process_of_elimination');
  perform hp_test.check(r.is_correct and r.correct_answer = 'B' and r.explanation = 'Divide by 2.' and r.elapsed_ms = 90000, 'submit result ' || row_to_json(r)::text);
  perform hp_test.check((select is_correct and elapsed_ms = 90000 and active_ms = 60000 and submitted_at = now()
    from public.practice_attempts where id = current_setting('t.a1')::uuid), 'server-computed grading and timing stored');
  perform hp_test.expect_error('select public.submit_practice_attempt(current_setting(''t.a1'')::uuid, ''B'')', '22023', '%already submitted%');
end $$;
select set_config('t.a2', public.start_practice_attempt(current_setting('t.st1')::uuid, '30000000-0000-0000-0000-000000000001')::text, true);
select set_config('t.a3', public.start_practice_attempt(current_setting('t.st1')::uuid, '30000000-0000-0000-0000-000000000002')::text, true);
select set_config('t.a4', public.start_practice_attempt(current_setting('t.st1')::uuid, '30000000-0000-0000-0000-000000000002')::text, true);
reset role;
select hp_test.check((select attempt_number from public.practice_attempts where id = current_setting('t.a2')::uuid) = 2, 'attempt numbering');
update public.practice_attempts set presented_at = now() - interval '10 minutes' where submitted_at is null;
set local role authenticated;
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-000000000051', true);
select is_correct from public.submit_practice_attempt(current_setting('t.a2')::uuid, 'A', 50000, null, 0, false, 'backsolve');
select is_correct from public.submit_practice_attempt(current_setting('t.a3')::uuid, ' C ', null, null, 2, true);
select is_correct from public.submit_practice_attempt(current_setting('t.a4')::uuid, 'C');
do $$ begin
  perform hp_test.check((select count(*) from public.practice_attempts) = 4, 'student sees own attempts only, not sibling');
  perform hp_test.check((select count(*) from public.practice_sessions) = 1, 'student sees own session');
  perform hp_test.expect_error('select public.student_weekly_progress(current_setting(''t.st2'')::uuid, ''2026-09-07'')', '42501');
end $$;
reset role;

-- Deterministic fixture week 2026-09-07 (Monday); a4 lands exactly on the next week boundary and is excluded.
update public.practice_attempts set presented_at = '2026-09-08 10:00Z', submitted_at = '2026-09-08 10:00:30Z', elapsed_ms = 30000, active_ms = 20000 where id = current_setting('t.a1')::uuid;
update public.practice_attempts set presented_at = '2026-09-09 10:00Z', submitted_at = '2026-09-09 10:01Z', elapsed_ms = 60000, active_ms = 50000 where id = current_setting('t.a2')::uuid;
update public.practice_attempts set presented_at = '2026-09-13 23:57:59Z', submitted_at = '2026-09-13 23:59:59Z', elapsed_ms = 120000 where id = current_setting('t.a3')::uuid;
update public.practice_attempts set presented_at = '2026-09-13 23:59:00Z', submitted_at = '2026-09-14 00:00:00Z', elapsed_ms = 60000, active_ms = 1 where id = current_setting('t.a4')::uuid;

set local role authenticated;
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-0000000000a1', true);
do $$
declare p jsonb; expected jsonb;
begin
  perform hp_test.check((select count(*) from public.practice_attempts) = 5, 'guardian sees both children''s attempts');
  perform hp_test.check((select count(*) from public.students) = 2, 'guardian A sees both students');
  p := public.student_weekly_progress(current_setting('t.st1')::uuid, '2026-09-07');
  expected := jsonb_build_object(
    'student_id', current_setting('t.st1'), 'week_start', '2026-09-07',
    'goal', '{"target_questions": 4, "target_minutes": 10}'::jsonb,
    'questions_attempted', 4, 'questions_submitted', 3, 'correct', 2, 'accuracy', 0.6667,
    'total_elapsed_ms', 210000, 'total_active_ms', 70000, 'median_elapsed_ms', 60000,
    'ai_help_attempts', 1, 'hints_used', 2,
    'goal_progress', '{"questions_pct": 75.0, "minutes_pct": 35.0}'::jsonb,
    'by_skill', '[{"subject":"math","skill":"linear_equations","submitted":2,"correct":1,"median_elapsed_ms":45000},
                  {"subject":"reading","skill":"inference","submitted":1,"correct":1,"median_elapsed_ms":120000}]'::jsonb,
    'by_strategy', '[{"strategy_key":"backsolve","submitted":1,"correct":0},
                     {"strategy_key":"process_of_elimination","submitted":1,"correct":1}]'::jsonb);
  perform hp_test.check(p = expected, 'progress mismatch: ' || p::text);
  -- Zero submissions: no division by zero, nulls rather than fake zeros.
  p := public.student_weekly_progress(current_setting('t.st2')::uuid, '2026-09-07');
  perform hp_test.check(p->'accuracy' = 'null' and p->'median_elapsed_ms' = 'null' and p->'total_active_ms' = 'null'
    and p->'goal' = 'null' and p->'goal_progress' = 'null' and (p->>'questions_submitted')::int = 0
    and (p->>'total_elapsed_ms')::int = 0 and p->'by_skill' = '[]' and p->'by_strategy' = '[]', 'empty progress: ' || p::text);
  perform hp_test.expect_error('select public.student_weekly_progress(current_setting(''t.st1'')::uuid, ''2026-09-08'')', '22023', '%Monday%');
  update public.weekly_practice_goals set target_questions = 3 where student_id = current_setting('t.st1')::uuid;
  perform hp_test.check((public.student_weekly_progress(current_setting('t.st1')::uuid, '2026-09-07')->'goal_progress'->>'questions_pct')::numeric = 100.0, 'goal update');
  perform hp_test.check((select set_by from public.weekly_practice_goals where student_id = current_setting('t.st1')::uuid) = auth.uid(), 'goal set_by');
end $$;

select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-000000000051', true);
do $$ begin
  perform hp_test.check((public.student_weekly_progress(current_setting('t.st1')::uuid, '2026-09-07')->>'correct')::int = 2, 'student reads own progress');
  perform hp_test.check((select count(*) from public.profiles) = 1, 'own profile only');
end $$;
-- Student cannot edit the goal guardians set (RLS filters the update to zero rows).
update public.weekly_practice_goals set target_questions = 1;

select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-0000000000b1', true);
do $$ begin
  perform hp_test.check((select count(*) from public.practice_attempts) = 0, 'guardian B sees no household A attempts');
  perform hp_test.check((select count(*) from public.practice_sessions) = 0, 'guardian B sees no household A sessions');
  perform hp_test.check((select count(*) from public.weekly_practice_goals where student_id = current_setting('t.st1')::uuid) = 0, 'guardian B sees no household A goals');
  perform hp_test.check((select count(*) from public.profiles) = 0, 'guardian B sees no other profiles');
end $$;
reset role;
select hp_test.check((select target_questions from public.weekly_practice_goals where student_id = current_setting('t.st1')::uuid) = 3, 'student changed goal');
-- Deleting the creating guardian's account keeps the household and the students' data.
delete from auth.users where id = '20000000-0000-0000-0000-0000000000a1';
select hp_test.check((select count(*) from public.households h join public.students s on s.household_id = h.id
  where h.created_by is null) = 2, 'household survives creator account deletion');
select hp_test.check(not exists (select 1 from public.household_members where user_id = '20000000-0000-0000-0000-0000000000a1'), 'deleted account membership removed');
rollback;
