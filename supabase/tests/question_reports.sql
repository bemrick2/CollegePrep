-- CR-25 (#218 B3): report a problem with a question. Who may report, refusals, one open report per reporter, question
-- and content version, the rate limit, the reserved-item rule, service-only reads and review, and no leaks.
-- Rolled back. Run with psql -v ON_ERROR_STOP=1.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql
-- The error a call raises, or null when it succeeds.
create function hp_test.error_of(p_sql text) returns text language plpgsql as $f$
begin
  execute p_sql;
  return null;
exception when others then
  return sqlstate || ' ' || sqlerrm;
end $f$;
grant execute on function hp_test.error_of(text) to authenticated, anon, service_role;
grant usage on schema hp_test to service_role;
grant execute on all functions in schema hp_test to service_role;
create function hp_test.as_service() returns void language plpgsql as $f$
begin
  perform set_config('role', 'service_role', true);
  perform set_config('request.jwt.claim.sub', '', true);
end $f$;
grant execute on function hp_test.as_service() to authenticated, anon, service_role;

-- PARENT a1 (creator), CO a2 (default guardian: view_progress), GOALS c1 (set_goals only, no view_progress),
-- STUDENT 51 (linked); OTHER guardian b1 with STUDENT2 52 (another household); OUTSIDER 99.
insert into auth.users(id) values ('20000000-0000-0000-0000-0000000000c1');
do $$
declare hh uuid; st uuid; hh2 uuid; st2 uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Reports', 'America/Chicago');
  st := public.add_student(hh, 'Report Student');
  perform set_config('t.st', st::text, true);
  perform set_config('t.inv', public.create_household_invitation(hh, 'student', st), true);
  perform set_config('t.inv_co', public.create_household_invitation(hh, 'guardian'), true);
  perform set_config('t.inv_goals', public.create_household_invitation(hh, 'guardian', null, 72, array['set_goals']), true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform public.accept_household_invitation(current_setting('t.inv_co'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform public.accept_household_invitation(current_setting('t.inv_goals'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  hh2 := public.create_household('Other', 'America/Chicago');
  st2 := public.add_student(hh2, 'Other Student');
  perform set_config('t.st2', st2::text, true);
  perform set_config('t.inv2', public.create_household_invitation(hh2, 'student', st2), true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.accept_household_invitation(current_setting('t.inv2'));

  -- Practice: q1 answered, q2 opened and never submitted, q3 skipped. Student 52 answers q1 too.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform set_config('t.a1', public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000001')::text, true);
  perform public.submit_practice_attempt(current_setting('t.a1')::uuid, 'A');
  perform set_config('t.a2', public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000002')::text, true);
  perform set_config('t.a3', public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000003')::text, true);
  perform public.submit_practice_attempt(current_setting('t.a3')::uuid, null, p_skipped => true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform set_config('t.b1', public.start_practice_attempt(st2, '30000000-0000-0000-0000-000000000001')::text, true);
  perform public.submit_practice_attempt(current_setting('t.b1')::uuid, 'B');

  -- Reserve q4 and q8 (math) and q7 (reading); student 51 opens an initial check, which assigns all three.
  perform hp_test.as_owner();
  update public.practice_questions set pool = 'assessment' where id in ('30000000-0000-0000-0000-000000000004',
    '30000000-0000-0000-0000-000000000007', '30000000-0000-0000-0000-000000000008');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform set_config('t.bm', public.start_benchmark(st, 'initial', '40000000-0000-0000-0000-000000000001')::text, true);
  perform set_config('t.r4', public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000004', p_benchmark => current_setting('t.bm')::uuid)::text, true);
  perform set_config('t.r8', public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000008', p_benchmark => current_setting('t.bm')::uuid)::text, true);
  perform hp_test.as_owner();
end $$;

-- Access to the table and the review function: service role only.
do $$
declare who text;
begin
  perform hp_test.check(not has_table_privilege('anon', 'public.question_reports', 'SELECT,INSERT,UPDATE,DELETE'), 'anon has no table privilege');
  perform hp_test.check(not has_table_privilege('authenticated', 'public.question_reports', 'SELECT,INSERT,UPDATE,DELETE'), 'authenticated has no table privilege');
  perform hp_test.check(not has_any_column_privilege('authenticated', 'public.question_reports', 'SELECT,INSERT,UPDATE'), 'authenticated has no column privilege');
  perform hp_test.check(has_table_privilege('service_role', 'public.question_reports', 'SELECT'), 'service role reads reports');
  perform hp_test.check((select relrowsecurity from pg_class where oid = 'public.question_reports'::regclass), 'reports have RLS');
  perform hp_test.check(not has_function_privilege('anon', 'public.report_question_problem(uuid, text, text)', 'EXECUTE'), 'anon cannot report');
  perform hp_test.check(has_function_privilege('authenticated', 'public.report_question_problem(uuid, text, text)', 'EXECUTE'), 'signed-in users can call report');
  foreach who in array array['anon', 'authenticated'] loop
    perform hp_test.check(not has_function_privilege(who, 'public.resolve_question_report(uuid, text, text, text)', 'EXECUTE'), who || ' cannot resolve');
  end loop;
  perform hp_test.check(has_function_privilege('service_role', 'public.resolve_question_report(uuid, text, text, text)', 'EXECUTE'), 'service role resolves');
end $$;

-- Who may report: the student and view_progress guardians of the household; nobody else.
do $$
declare r jsonb; a1 uuid := current_setting('t.a1')::uuid; who record; n bigint;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  r := public.report_question_problem(a1, 'wrong_key', '  The key says B but A is right.  ');
  perform hp_test.eq((select array_agg(k order by k) from jsonb_object_keys(r) k), array['created', 'report_id', 'status'], 'the result carries only id, created and status');
  perform hp_test.eq(r->>'created', 'true', 'student report created');
  perform hp_test.eq(r->>'status', 'open', 'a new report is open');
  perform set_config('t.rep_student', r->>'report_id', true);

  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq(public.report_question_problem(a1, 'unclear')->>'created', 'true', 'PARENT (view_progress) reports');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq(public.report_question_problem(a1, 'two_answers', '   ')->>'created', 'true', 'CO (default guardian) reports');

  for who in select * from (values ('20000000-0000-0000-0000-0000000000c1'::uuid, 'GOALS without view_progress'),
      ('20000000-0000-0000-0000-0000000000b1'::uuid, 'another household''s guardian'),
      ('20000000-0000-0000-0000-000000000052'::uuid, 'another household''s student'),
      ('20000000-0000-0000-0000-000000000099'::uuid, 'an outsider')) v(uid, label) loop
    perform hp_test.as_user(who.uid);
    perform hp_test.eq(left(hp_test.error_of(format($q$select public.report_question_problem(%L, 'typo')$q$, a1)), 5), '42501', who.label || ' is refused');
  end loop;
  -- A missing attempt reads exactly like someone else's.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.eq(hp_test.error_of(format($q$select public.report_question_problem(%L, 'typo')$q$, gen_random_uuid())),
    hp_test.error_of(format($q$select public.report_question_problem(%L, 'typo')$q$, a1)), 'missing and foreign attempts look the same');
  perform hp_test.as_anon();
  perform hp_test.expect_error(format($q$select public.report_question_problem(%L, 'typo')$q$, a1), '42501');
  perform hp_test.as_service();
  perform hp_test.expect_error(format($q$select public.report_question_problem(%L, 'typo')$q$, a1), '42501', 'Authentication required');

  perform hp_test.as_owner();
  select count(*) into n from public.question_reports where question_id = '30000000-0000-0000-0000-000000000001';
  perform hp_test.eq(n, 3::bigint, 'three reports: student, PARENT, CO');
  perform hp_test.eq((select note from public.question_reports where id = current_setting('t.rep_student')::uuid), 'The key says B but A is right.', 'note trimmed');
  perform hp_test.eq((select note from public.question_reports where reporter_user_id = '20000000-0000-0000-0000-0000000000a2'), null::text, 'a blank note is no note');
  perform hp_test.eq((select string_agg(reporter_role, ',' order by reporter_role) from public.question_reports), 'guardian,guardian,student', 'reporter roles');
  perform hp_test.eq((select count(*) from public.question_reports q join public.practice_questions p on p.id = q.question_id
    where q.content_hash = public.practice_question_content_hash(p) and q.question_pool = 'practice' and q.student_id = current_setting('t.st')::uuid), 3::bigint,
    'each report records the content version, pool and student');
end $$;

-- Refusals: reason and note.
do $$
declare a1 uuid := current_setting('t.a1')::uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.expect_error(format($q$select public.report_question_problem(%L, 'spam')$q$, a1), '22023', '%Reason%');
  perform hp_test.expect_error(format($q$select public.report_question_problem(%L, null)$q$, a1), '22023', '%Reason%');
  perform hp_test.expect_error(format($q$select public.report_question_problem(%L, 'WRONG_KEY')$q$, a1), '22023', '%Reason%');
  perform hp_test.expect_error(format($q$select public.report_question_problem(%L, 'other', %L)$q$, a1, repeat('x', 501)), '22023', '%500%');
  perform hp_test.as_owner();
  perform hp_test.eq((select count(*) from public.question_reports), 3::bigint, 'refused calls store nothing');
end $$;

-- Idempotence: one open report per reporter, question and content version.
do $$
declare r jsonb; a1 uuid := current_setting('t.a1')::uuid; v_hash text;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  r := public.report_question_problem(a1, 'typo', 'a different note');
  perform hp_test.eq(r->>'created', 'false', 'a repeat is not a new report');
  perform hp_test.eq(r->>'report_id', current_setting('t.rep_student'), 'a repeat returns the open report');
  -- A 500-character note is the maximum and is accepted (on a repeat, nothing changes).
  perform hp_test.eq(public.report_question_problem(a1, 'other', repeat('y', 500))->>'created', 'false', '500 characters is allowed');
  perform hp_test.as_owner();
  perform hp_test.eq((select reason || '|' || note from public.question_reports where id = current_setting('t.rep_student')::uuid),
    'wrong_key|The key says B but A is right.', 'a repeat changes nothing');
  perform hp_test.eq((select count(*) from public.question_reports where reporter_user_id = '20000000-0000-0000-0000-000000000051'), 1::bigint, 'still one report');

  -- Another attempt at the same question is the same question: still the same open report.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform set_config('t.a1b', public.start_practice_attempt(current_setting('t.st')::uuid, '30000000-0000-0000-0000-000000000001')::text, true);
  perform hp_test.eq(public.report_question_problem(current_setting('t.a1b')::uuid, 'typo')->>'report_id', current_setting('t.rep_student'), 'a second attempt finds the same open report');

  -- New content is a new version: the same person may report it again.
  perform hp_test.as_owner();
  select content_hash into v_hash from public.question_reports where id = current_setting('t.rep_student')::uuid;
  update public.practice_questions set stem = 'Question 1, corrected' where id = '30000000-0000-0000-0000-000000000001';
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  r := public.report_question_problem(a1, 'unclear');
  perform hp_test.eq(r->>'created', 'true', 'a new content version takes a new report');
  perform hp_test.as_owner();
  perform hp_test.check((select content_hash from public.question_reports where id = (r->>'report_id')::uuid) <> v_hash, 'the new report names the new version');
  update public.practice_questions set stem = 'Question 1' where id = '30000000-0000-0000-0000-000000000001';
  perform hp_test.eq((select content_hash from public.question_reports where id = current_setting('t.rep_student')::uuid), v_hash, 'restored content');
end $$;

-- Review: service role only; closing a report lets the reporter report that version again.
do $$
declare r jsonb; a1 uuid := current_setting('t.a1')::uuid; rep uuid := current_setting('t.rep_student')::uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.expect_error(format($q$select public.resolve_question_report(%L, 'resolved', 'Editor')$q$, rep), '42501');
  perform hp_test.as_anon();
  perform hp_test.expect_error(format($q$select public.resolve_question_report(%L, 'resolved', 'Editor')$q$, rep), '42501');
  perform hp_test.as_service();
  perform hp_test.eq((select count(*) from public.question_reports), 4::bigint, 'service role reads every report');
  perform hp_test.expect_error(format($q$select public.resolve_question_report(%L, 'open', 'Editor')$q$, rep), '22023');
  perform hp_test.expect_error(format($q$select public.resolve_question_report(%L, 'resolved', '  ')$q$, rep), '22023');
  perform hp_test.expect_error(format($q$select public.resolve_question_report(%L, 'resolved', 'Editor')$q$, gen_random_uuid()), '22023');
  perform public.resolve_question_report(rep, 'resolved', 'Editor', 'Key confirmed correct.');
  perform hp_test.expect_error(format($q$select public.resolve_question_report(%L, 'dismissed', 'Editor')$q$, rep), '22023', '%No open report%');
  perform hp_test.eq((select status || '|' || reviewed_by || '|' || (reviewed_at is not null) from public.question_reports where id = rep), 'resolved|Editor|true', 'resolved once');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  r := public.report_question_problem(a1, 'wrong_key');
  perform hp_test.eq(r->>'created', 'true', 'after review, the same version can be reported again');
  perform hp_test.check(r->>'report_id' <> rep::text, 'as a new report');
end $$;

-- Families never read reports, their own included.
do $$
declare u uuid;
begin
  foreach u in array array['20000000-0000-0000-0000-000000000051', '20000000-0000-0000-0000-0000000000a1', '20000000-0000-0000-0000-0000000000a2',
      '20000000-0000-0000-0000-0000000000b1', '20000000-0000-0000-0000-000000000052', '20000000-0000-0000-0000-000000000099']::uuid[] loop
    perform hp_test.as_user(u);
    perform hp_test.expect_error('select count(*) from public.question_reports', '42501');
    perform hp_test.expect_error($q$update public.question_reports set status = 'dismissed', reviewed_at = now(), reviewed_by = 'x'$q$, '42501');
    perform hp_test.expect_error($q$delete from public.question_reports$q$, '42501');
  end loop;
  perform hp_test.as_anon();
  perform hp_test.expect_error('select count(*) from public.question_reports', '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.expect_error(format($q$insert into public.question_reports(question_id, content_hash, question_pool, student_id, reporter_user_id, reporter_role, reason)
    values ('30000000-0000-0000-0000-000000000001', %L, 'practice', %L, '20000000-0000-0000-0000-000000000051', 'student', 'typo')$q$,
    repeat('a', 64), current_setting('t.st')), '42501');
end $$;

-- Practice items: an unsubmitted or skipped attempt is reportable too.
do $$
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq(public.report_question_problem(current_setting('t.a2')::uuid, 'unclear')->>'created', 'true', 'an opened practice item');
  perform hp_test.eq(public.report_question_problem(current_setting('t.a3')::uuid, 'typo')->>'created', 'true', 'a skipped practice item');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq(public.report_question_problem(current_setting('t.a2')::uuid, 'unclear')->>'created', 'true', 'a guardian, on an opened practice item');
end $$;

-- Reserved items: by the student during the live check; by anyone allowed once attempted; otherwise refused, without
-- naming the pool.
do $$
declare r4 uuid := current_setting('t.r4')::uuid; r8 uuid := current_setting('t.r8')::uuid; e text; r jsonb;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  e := hp_test.error_of(format($q$select public.report_question_problem(%L, 'typo')$q$, r4));
  perform hp_test.eq(left(e, 5), '42501', 'a guardian cannot report an unanswered check item');
  perform hp_test.check(e not ilike '%reserv%' and e not ilike '%assessment%' and e not ilike '%check%', 'the refusal does not name the reserve: ' || e);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  r := public.report_question_problem(r4, 'two_answers');
  perform hp_test.eq(r->>'created', 'true', 'the student reports a check item during the live check');
  perform hp_test.eq((select array_agg(k order by k) from jsonb_object_keys(r) k), array['created', 'report_id', 'status'], 'still only id, created and status');
  perform public.submit_practice_attempt(r4, 'A');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq(public.report_question_problem(r4, 'two_answers')->>'created', 'true', 'a guardian reports a check item once answered');
  -- The check expires with q8 opened and unanswered: nobody may report it now.
  perform hp_test.as_owner();
  update public.practice_benchmarks set started_at = now() - interval '5 hours' where id = current_setting('t.bm')::uuid;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  e := hp_test.error_of(format($q$select public.report_question_problem(%L, 'typo')$q$, r8));
  perform hp_test.eq(left(e, 5), '42501', 'an unanswered item of an expired check is refused');
  perform hp_test.check(e not ilike '%reserv%' and e not ilike '%assessment%', 'without naming the reserve');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.expect_error(format($q$select public.report_question_problem(%L, 'typo')$q$, r8), '42501');
  -- The answered one stays reportable after expiry (idempotent here: it is already open).
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq(public.report_question_problem(r4, 'typo')->>'created', 'false', 'an answered check item, after expiry');
  -- Another household can't use a reserved attempt either.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.expect_error(format($q$select public.report_question_problem(%L, 'typo')$q$, r4), '42501');
  perform hp_test.as_owner();
  perform hp_test.eq((select count(*) from public.question_reports where question_pool = 'assessment'), 2::bigint, 'two reserved-item reports');
end $$;

-- Rate limit: 10 new reports per reporter per hour, 30 per 24 hours. Repeats of an open report still answer.
do $$
declare st2 uuid := current_setting('t.st2')::uuid; b1 uuid := current_setting('t.b1')::uuid; e text; v_hash text;
begin
  perform hp_test.as_owner();
  -- Student 52's earlier reports, on another student's question versions (the limit counts reports, not questions).
  insert into public.question_reports(question_id, content_hash, question_pool, student_id, reporter_user_id, reporter_role, reason, created_at)
  select '30000000-0000-0000-0000-000000000003', lpad(to_hex(n), 64, '0'), 'practice', st2, '20000000-0000-0000-0000-000000000052', 'student', 'typo',
    now() - interval '10 minutes'
  from generate_series(1, 9) n;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.eq(public.report_question_problem(b1, 'typo')->>'created', 'true', 'the 10th report in an hour is allowed');
  perform set_config('t.a52', public.start_practice_attempt(st2, '30000000-0000-0000-0000-000000000002')::text, true);
  e := hp_test.error_of(format($q$select public.report_question_problem(%L, 'typo')$q$, current_setting('t.a52')));
  perform hp_test.eq(left(e, 5), '22023', 'the 11th in an hour is refused');
  perform hp_test.check(e ilike '%Too many reports%', 'with the rate-limit message');
  -- The hint is what the client reads.
  begin
    perform public.report_question_problem(current_setting('t.a52')::uuid, 'typo');
    raise exception 'rate limit did not apply';
  exception when sqlstate '22023' then
    declare h text; begin get stacked diagnostics h = pg_exception_hint; perform hp_test.eq(h, 'rate_limited', 'hint rate_limited'); end;
  end;
  perform hp_test.eq(public.report_question_problem(b1, 'unclear')->>'created', 'false', 'a repeat of an open report still answers when limited');
  -- Another reporter is unaffected.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.eq(public.report_question_problem(current_setting('t.a52')::uuid, 'typo')->>'created', 'true', 'the limit is per reporter');

  -- Older than an hour, the hourly limit lifts; the daily one still counts them.
  perform hp_test.as_owner();
  update public.question_reports set created_at = now() - interval '2 hours' where reporter_user_id = '20000000-0000-0000-0000-000000000052';
  insert into public.question_reports(question_id, content_hash, question_pool, student_id, reporter_user_id, reporter_role, reason, created_at)
  select '30000000-0000-0000-0000-000000000003', lpad(to_hex(100 + n), 64, '0'), 'practice', st2, '20000000-0000-0000-0000-000000000052', 'student', 'typo',
    now() - interval '20 hours'
  from generate_series(1, 19) n;
  -- 10 + 19 = 29 in 24 hours: one more is allowed, then the daily limit applies.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.eq(public.report_question_problem(current_setting('t.a52')::uuid, 'typo')->>'created', 'true', 'the 30th in a day is allowed');
end $$;
do $$
declare st2 uuid := current_setting('t.st2')::uuid;
begin
  perform hp_test.as_owner();
  -- q6 is a practice item student 52 opens; with 30 reports in 24 hours the next is refused.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform set_config('t.a52c', public.start_practice_attempt(st2, '30000000-0000-0000-0000-000000000006')::text, true);
  perform hp_test.expect_error(format($q$select public.report_question_problem(%L, 'typo')$q$, current_setting('t.a52c')), '22023', '%Too many reports%');
  perform hp_test.as_owner();
  update public.question_reports set created_at = now() - interval '25 hours' where reporter_user_id = '20000000-0000-0000-0000-000000000052';
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.eq(public.report_question_problem(current_setting('t.a52c')::uuid, 'typo')->>'created', 'true', 'after 24 hours the limit lifts');
end $$;

-- Deleting a student deletes their reports; the review history of other students stays.
do $$
declare n bigint;
begin
  perform hp_test.as_owner();
  select count(*) into n from public.question_reports where student_id <> current_setting('t.st2')::uuid;
  delete from public.students where id = current_setting('t.st2')::uuid;
  perform hp_test.eq((select count(*) from public.question_reports where student_id = current_setting('t.st2')::uuid), 0::bigint, 'reports follow the student');
  perform hp_test.eq((select count(*) from public.question_reports), n, 'other reports stay');
end $$;
\o
\echo question_reports: all assertions passed
rollback;
