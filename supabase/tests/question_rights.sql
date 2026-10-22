-- CR-24 rights gate and the generated-item rule (#218 B2). Rolled back. Run with psql -v ON_ERROR_STOP=1.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql

do $$
declare q uuid := '30000000-0000-0000-0000-000000000005';  -- the fixture draft
  g uuid; lic text;
begin
  perform hp_test.as_owner();
  -- A draft needs nothing.
  update public.practice_questions set license = null, source_attribution = null, origin = null where id = q;
  -- Publishing needs an allowed license, attribution where required, and a recorded origin.
  perform hp_test.expect_error(format($s$update public.practice_questions set status = 'published' where id = %L$s$, q), '23514');
  foreach lic in array array['original', 'cc-by', 'CC-BY-4.0', 'licensed:', 'licensed:Acme', 'licensed:acme corp', 'public domain', ''] loop
    perform hp_test.expect_error(format($s$update public.practice_questions set status = 'published', license = %L,
      source_attribution = 'Someone', origin = 'authored' where id = %L$s$, lic, q), '23514');
  end loop;
  perform hp_test.expect_error(format($s$update public.practice_questions set status = 'published', license = 'original-owned' where id = %L$s$, q), '23514');  -- no origin
  foreach lic in array array['cc-by-4.0', 'cc-by-sa-4.0', 'licensed:acme-prep'] loop
    perform hp_test.expect_error(format($s$update public.practice_questions set status = 'published', license = %L,
      source_attribution = '  ', origin = 'licensed' where id = %L$s$, lic, q), '23514');  -- attribution required
    update public.practice_questions set status = 'published', license = lic, source_attribution = 'Example Author, CC BY 4.0', origin = 'licensed' where id = q;
    update public.practice_questions set status = 'draft' where id = q;
  end loop;
  foreach lic in array array['original-owned', 'public-domain', 'us-federal-pd'] loop
    update public.practice_questions set status = 'published', license = lic, source_attribution = null, origin = 'authored' where id = q;
    update public.practice_questions set status = 'draft' where id = q;
  end loop;
  -- A published row can't lose its rights.
  update public.practice_questions set status = 'published', license = 'cc-by-4.0', source_attribution = 'A. Author' where id = q;
  perform hp_test.expect_error(format($s$update public.practice_questions set source_attribution = null where id = %L$s$, q), '23514');
  perform hp_test.expect_error(format($s$update public.practice_questions set license = 'unknown' where id = %L$s$, q), '23514');
  perform hp_test.expect_error(format($s$update public.practice_questions set origin = null where id = %L$s$, q), '23514');
  perform hp_test.expect_error($s$insert into public.practice_questions(exam_version_id, question_type_id, section, stem, choices, answer_format,
      accepted_answers, status) values ('40000000-0000-0000-0000-000000000001', '41000000-0000-0000-0000-000000000001', 'math', 'New',
      '["A","B"]', 'choice', '["A"]', 'published')$s$, '23514');

  -- Generated items: an automated approval confers nothing; only a recorded human review does.
  insert into public.practice_questions(exam_version_id, question_type_id, section, stem, choices, answer_format, accepted_answers,
    expected_time_seconds, status, license, origin)
  values ('40000000-0000-0000-0000-000000000001', '41000000-0000-0000-0000-000000000001', 'math', 'Generated item', '["A","B"]',
    'choice', '["A"]', 60, 'draft', 'original-owned', 'generated') returning id into g;
  perform set_config('t.g', g::text, true);
  perform hp_test.expect_error(format($s$select public.approve_practice_question(%L, 'loader v2 checks')$s$, g), '22023', '%human%');
  perform hp_test.expect_error(format($s$select public.approve_practice_question(%L, 'model: self-check')$s$, g), '22023', '%human%');
  perform public.approve_practice_question(g, 'loader v2 checks', now(), 'changes_needed');  -- a non-approval may be recorded
  update public.practice_questions set status = 'published' where id = g;
  -- Writing an approval directly (bypassing the RPC) still doesn't make it servable.
  update public.practice_questions set review_status = 'approved', reviewed_at = now(), review_method = 'loader v2 checks',
    content_hash = public.practice_question_content_hash(practice_questions) where id = g;
  perform hp_test.check(not (select review_current from public.practice_questions where id = g), 'automated approval of a generated item is not current');
  -- Relabelling it doesn't launder it.
  perform hp_test.expect_error(format($s$update public.practice_questions set origin = 'authored' where id = %L$s$, g), '22023');
  -- 'fixture:' approvals count only where the database owner enabled them (the local stack); not here yet.
  perform hp_test.expect_error(format($s$select public.approve_practice_question(%L, 'fixture: demo')$s$, g), '22023', '%human%');
  execute format('alter database %I set collegeprep.fixture_approvals = %L', current_database(), 'on');
  perform public.approve_practice_question(g, 'fixture: demo');
  perform hp_test.check((select review_current from public.practice_questions where id = g), 'fixture approval counts where enabled');
  execute format('alter database %I reset collegeprep.fixture_approvals', current_database());
  perform public.approve_practice_question(g, 'loader v2 checks', now(), 'changes_needed');
  perform hp_test.expect_error(format($s$select public.approve_practice_question(%L, 'fixture: demo')$s$, g), '22023', '%human%');
  perform public.approve_practice_question(g, 'human: editorial ledger stages 3-8');
  perform hp_test.check((select review_current from public.practice_questions where id = g), 'human-reviewed generated item is current');
  -- An authored item keeps today's rule (the loader's recorded checks).
  perform hp_test.check((select review_current from public.practice_questions where id = '30000000-0000-0000-0000-000000000001'),
    'authored fixture approved by the loader stays current');
end $$;

-- Serving follows: a student sees the human-reviewed generated item, never an unreviewed one.
do $$
declare g uuid := current_setting('t.g')::uuid; g2 uuid;
begin
  perform hp_test.as_owner();
  insert into public.practice_questions(exam_version_id, question_type_id, section, stem, choices, answer_format, accepted_answers,
    expected_time_seconds, status, license, origin)
  values ('40000000-0000-0000-0000-000000000001', '41000000-0000-0000-0000-000000000001', 'math', 'Generated, unreviewed', '["A","B"]',
    'choice', '["A"]', 60, 'published', 'original-owned', 'generated') returning id into g2;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select count(*) from public.practice_questions where id = g), 1::bigint, 'reviewed generated item is served');
  perform hp_test.eq((select count(*) from public.practice_questions where id = g2), 0::bigint, 'unreviewed generated item is not served');
  -- Clients can't write rights or origin.
  perform hp_test.check(not has_column_privilege('public.practice_questions', 'origin', 'UPDATE'), 'clients cannot set origin');
  perform hp_test.check(not has_column_privilege('public.practice_questions', 'license', 'UPDATE'), 'clients cannot set license');
  perform hp_test.as_owner();
end $$;

rollback;
