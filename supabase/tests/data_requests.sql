-- A4 (#218 B8): data export and deletion by service role (docs/operations/DATA_REQUESTS.md).
-- Completeness (every table has a decision), no cross-household leaks, no secrets or answer keys, retention, the audit
-- row, the dry-run and scope safeguards, and no client access. Everything is rolled back.
-- Run with psql -v ON_ERROR_STOP=1.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql
grant usage on schema hp_test to service_role;
grant execute on all functions in schema hp_test to service_role;

-- ---------------------------------------------------------------------------------------------------------------
-- The decision for every table. A new table fails the completeness check below until it is added here AND, when it
-- holds personal data, to the export and delete functions (supabase/migrations/*_data_requests.sql) and the runbook.
--   personal      exported, and deleted with the student or household
--   retained      exported in summary, kept de-identified on deletion (billing records, tax law)
--   security      deleted with the account, not exported (rate-limit log)
--   request_log   written by this procedure (audit and retained email-sent records)
--   reference     not personal data (reference catalog, question content, server settings and secrets)
-- ---------------------------------------------------------------------------------------------------------------
create temp table dr_decisions(tbl text primary key, decision text not null
  check (decision in ('personal', 'retained', 'security', 'request_log', 'reference')));
insert into dr_decisions values
 ('public.households', 'personal'), ('public.household_members', 'personal'), ('public.household_invitations', 'personal'),
 ('public.household_saved_schools', 'personal'), ('public.profiles', 'personal'), ('public.students', 'personal'),
 ('public.weekly_practice_goals', 'personal'), ('public.practice_sessions', 'personal'),
 ('public.practice_session_items', 'personal'), ('public.practice_attempts', 'personal'),
 ('public.practice_attempt_events', 'personal'), ('public.ai_help_requests', 'personal'),
 ('public.practice_benchmarks', 'personal'), ('public.practice_benchmark_items', 'personal'),
 ('public.student_test_scores', 'personal'), ('public.student_exam_plan', 'personal'),
 ('public.student_planning_preferences', 'personal'), ('public.student_academic_interests', 'personal'),
 ('public.alert_preferences', 'personal'), ('public.subscriptions', 'personal'), ('public.billing_customers', 'personal'),
 ('public.billing_events', 'retained'),
 ('public.invitation_code_attempts', 'security'),
 ('public.data_request_log', 'request_log'), ('public.retained_email_records', 'request_log'),
 ('public.academic_programs', 'reference'), ('public.admissions_metrics', 'reference'), ('public.app_settings', 'reference'),
 ('public.appeal_policies', 'reference'), ('public.credit_equivalencies', 'reference'), ('public.credit_policies', 'reference'),
 ('public.data_verification_runs', 'reference'), ('public.degree_requirements', 'reference'),
 ('public.exam_catalog', 'reference'), ('public.exam_families', 'reference'), ('public.exam_versions', 'reference'),
 ('public.federal_aid_programs', 'reference'), ('public.institution_costs', 'reference'),
 ('public.institutional_awards', 'reference'), ('public.institutions', 'reference'),
 ('public.invitation_code_pepper', 'reference'), ('public.practice_benchmark_kinds', 'reference'),
 ('public.practice_benchmark_plan', 'reference'), ('public.practice_blueprints', 'reference'),
 ('public.practice_passages', 'reference'), ('public.practice_question_distractors', 'reference'),
 ('public.practice_question_skills', 'reference'), ('public.practice_question_strategies', 'reference'),
 ('public.practice_questions', 'reference'), ('public.practice_reserve_releases', 'reference'),
 ('public.program_catalogs', 'reference'), ('public.question_strategies', 'reference'), ('public.question_types', 'reference'),
 ('public.skills', 'reference'), ('public.sources', 'reference'), ('public.state_aid_programs', 'reference'),
 ('public.state_policies', 'reference'), ('public.transfer_policies', 'reference'), ('public.trap_types', 'reference'),
 ('ingestion.reference_records', 'reference'), ('ingestion.reference_revisions', 'reference');
grant select on dr_decisions to anon, authenticated, service_role;

-- 1. Completeness: every base table outside the platform schemas has a decision, and every decision names a table.
do $$
declare v_missing text; v_stale text;
begin
  select string_agg(t, ', ' order by t) into v_missing from (
    select table_schema || '.' || table_name t from information_schema.tables
    where table_type = 'BASE TABLE'
      and table_schema not in ('pg_catalog', 'information_schema', 'auth', 'hp_test')
      and table_schema not like 'pg_temp%' and table_schema not like 'pg_toast%') x
  where t not in (select tbl from dr_decisions);
  if v_missing is not null then
    raise exception 'Tables with no data-request decision (add to supabase/tests/data_requests.sql and, if personal, to the export/delete functions and docs/operations/DATA_REQUESTS.md): %', v_missing;
  end if;
  select string_agg(tbl, ', ') into v_stale from dr_decisions where to_regclass(tbl) is null;
  if v_stale is not null then raise exception 'Data-request decisions name tables that do not exist: %', v_stale; end if;
  -- A table that points at a person (auth.users, students, households) or at their activity cannot be "reference".
  select string_agg(distinct c.conrelid::regclass::text, ', ') into v_missing
  from pg_constraint c join dr_decisions d on d.tbl = (select n.nspname || '.' || r.relname from pg_class r
    join pg_namespace n on n.oid = r.relnamespace where r.oid = c.conrelid)
  where c.contype = 'f' and d.decision = 'reference'
    and c.confrelid in ('auth.users'::regclass, 'public.students'::regclass, 'public.households'::regclass,
      'public.practice_sessions'::regclass, 'public.practice_attempts'::regclass, 'public.practice_benchmarks'::regclass);
  if v_missing is not null then raise exception 'Tables referencing a person are marked reference: %', v_missing; end if;
  -- Likewise any column named like a person reference.
  select string_agg(distinct d.tbl, ', ') into v_missing from information_schema.columns c
  join dr_decisions d on d.tbl = c.table_schema || '.' || c.table_name
  where d.decision = 'reference' and c.column_name in ('student_id', 'household_id', 'user_id', 'owner_user_id', 'linked_user_id');
  if v_missing is not null then raise exception 'Reference tables carry person columns: %', v_missing; end if;
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- Fixtures. Household A: g1 (creator, a1), g2 (a2, also a guardian in B), S1 (linked login 51), S2 (guardian-managed).
-- Household B: gb (b1), S3 (linked login 53). Independent student I (login 52, no household).
-- ---------------------------------------------------------------------------------------------------------------
create schema dr_test;
grant usage on schema dr_test to anon, authenticated, service_role;
insert into public.sources(id, canonical_url, authority) values ('50000000-0000-0000-0000-0000000000d1', 'https://example.edu/dr', 'institution');
insert into public.institutions(id, institution_key, ipeds_name, display_name, state_code, source_id, verification_status, identity_academic_year)
values ('50000000-0000-0000-0000-0000000000d2', 'dr-school', 'DR School', 'DR School', 'TN', '50000000-0000-0000-0000-0000000000d1', 'verified', '2023-24');
insert into public.exam_catalog(exam_key, family, display_name) values ('ap:dr-calculus', 'ap', 'AP DR Calculus');
insert into public.profiles(id, display_name) values
 ('20000000-0000-0000-0000-0000000000a1', 'Alpha Guardian One'), ('20000000-0000-0000-0000-0000000000a2', 'Shared Guardian Two'),
 ('20000000-0000-0000-0000-0000000000b1', 'Bravo Guardian'), ('20000000-0000-0000-0000-000000000051', 'Alpha Kid Login'),
 ('20000000-0000-0000-0000-000000000052', 'Indy Login'), ('20000000-0000-0000-0000-000000000053', 'Bravo Kid Login');
insert into public.invitation_code_attempts(user_id) values
 ('20000000-0000-0000-0000-0000000000a1'), ('20000000-0000-0000-0000-0000000000a2'), ('20000000-0000-0000-0000-000000000051'),
 ('20000000-0000-0000-0000-0000000000b1'), ('20000000-0000-0000-0000-000000000052');

-- Rows in every per-student table.
create function dr_test.seed_student(p_student uuid, p_guardian uuid, p_tag text) returns void language plpgsql as $$
declare v_session uuid := gen_random_uuid(); v_attempt uuid := gen_random_uuid(); v_bench uuid := gen_random_uuid();
  v_goal uuid := gen_random_uuid();
begin
  insert into public.weekly_practice_goals(id, student_id, week_start, target_questions, goal_mode, set_by)
  values (v_goal, p_student, '2026-10-26', 20, 'fixed', p_guardian);
  insert into public.practice_sessions(id, student_id, target_minutes, goal_id) values (v_session, p_student, 10, v_goal);
  insert into public.practice_session_items(session_id, position, question_id, reason)
  values (v_session, 1, '30000000-0000-0000-0000-000000000001', 'review'), (v_session, 2, '30000000-0000-0000-0000-000000000003', 'new');
  insert into public.practice_attempts(id, session_id, student_id, question_id, selected_answer, is_correct, attempt_number, submitted_at)
  values (v_attempt, v_session, p_student, '30000000-0000-0000-0000-000000000001', 'A', false, 1, now());
  insert into public.practice_attempt_events(attempt_id, student_id, kind, answer) values
   (v_attempt, p_student, 'presented', null), (v_attempt, p_student, 'submitted', 'A');
  insert into public.ai_help_requests(attempt_id, student_id, requested_by, mode, status) values (v_attempt, p_student, p_guardian, 'hint', 'disabled');
  insert into public.practice_benchmarks(id, student_id, kind, exam_version_id) values (v_bench, p_student, 'initial', '40000000-0000-0000-0000-000000000001');
  insert into public.practice_benchmark_items(benchmark_id, student_id, exam_version_id, question_id, section, position, seen_before)
  values (v_bench, p_student, '40000000-0000-0000-0000-000000000001', '30000000-0000-0000-0000-000000000004', 'math', 1, false);
  insert into public.student_test_scores(student_id, exam_version_id, test_date, composite, section_scores, score_source, entered_by)
  values (p_student, '40000000-0000-0000-0000-000000000001', '2026-09-01', 1200, '{"math":600}', 'official', p_guardian);
  insert into public.student_exam_plan(student_id, exam_key, set_by) values (p_student, 'ap:dr-calculus', p_guardian);
  insert into public.student_planning_preferences(student_id, exam_family, target_score, goals, set_by)
  values (p_student, 'sat', 1400, '{merit}', p_guardian);
  insert into public.student_academic_interests(student_id, certainty, interests, set_by)
  values (p_student, 'few', jsonb_build_array(jsonb_build_object('kind', 'area', 'key', 'tag-' || p_tag)), p_guardian);
  if p_guardian is not null then
    insert into public.alert_preferences(user_id, student_id, channel, inactivity_days) values (p_guardian, p_student, 'email', 3);
  end if;
end $$;

do $$
declare ha uuid; hb uuid; s1 uuid; s2 uuid; s3 uuid; si uuid; c text;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  ha := public.create_household('Alpha Home', 'America/Chicago');
  s1 := public.add_student(ha, 'Alpha Kid One');
  s2 := public.add_student(ha, 'Alpha Kid Two');
  c := public.create_household_invitation(ha, 'student', s1);
  perform set_config('t.inv_s1', c, true);
  perform set_config('t.inv_g2', public.create_household_invitation(ha, 'guardian', null, 72, array['view_progress']), true);
  perform public.create_household_invitation(ha, 'student', s2);  -- emailed recently: retained
  perform public.create_household_invitation(ha, 'guardian', null, 72, array['view_progress']);  -- emailed 14 months ago
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv_s1'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform public.accept_household_invitation(current_setting('t.inv_g2'));

  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  hb := public.create_household('Bravo Home', 'America/New_York');
  s3 := public.add_student(hb, 'Bravo Kid');
  perform set_config('t.inv_s3', public.create_household_invitation(hb, 'student', s3), true);
  perform set_config('t.inv_bg', public.create_household_invitation(hb, 'guardian', null, 72, array['view_progress']), true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform public.accept_household_invitation(current_setting('t.inv_s3'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform public.accept_household_invitation(current_setting('t.inv_bg'));

  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  si := public.create_self_student_profile('Indy Kid');
  perform hp_test.as_owner();

  update public.household_invitations set recipient_email = 'alpha.kid.two@example.com', email_send_count = 2, last_emailed_at = now() - interval '1 day'
  where household_id = ha and student_id = s2;
  update public.household_invitations set recipient_email = 'old.guardian@example.com', email_send_count = 1, last_emailed_at = now() - interval '14 months'
  where household_id = ha and role = 'guardian' and accepted_by is null;
  update public.household_invitations set recipient_email = 'bravo.kid@example.com', email_send_count = 1, last_emailed_at = now()
  where household_id = hb and student_id = s3;

  perform dr_test.seed_student(s1, '20000000-0000-0000-0000-0000000000a1', 'alpha-one');
  perform dr_test.seed_student(s2, '20000000-0000-0000-0000-0000000000a2', 'alpha-two');
  perform dr_test.seed_student(s3, '20000000-0000-0000-0000-0000000000b1', 'bravo');
  perform dr_test.seed_student(si, null, 'indy');
  insert into public.household_saved_schools(household_id, institution_key, added_by) values
   (ha, 'dr-school', '20000000-0000-0000-0000-0000000000a1'), (hb, 'dr-school', '20000000-0000-0000-0000-0000000000b1');
  insert into public.subscriptions(owner_user_id, household_id, plan_key, status, provider, provider_customer_id, provider_subscription_id) values
   ('20000000-0000-0000-0000-0000000000a1', ha, 'family_annual', 'active', 'stripe', 'cus_ALPHA', 'sub_ALPHA'),
   ('20000000-0000-0000-0000-0000000000b1', hb, 'family_annual', 'active', 'stripe', 'cus_BRAVO', 'sub_BRAVO');
  insert into public.billing_customers(household_id, provider, provider_customer_id, created_by) values
   (ha, 'stripe', 'cus_ALPHA', '20000000-0000-0000-0000-0000000000a1'), (hb, 'stripe', 'cus_BRAVO', '20000000-0000-0000-0000-0000000000b1');
  insert into public.billing_events(provider, event_id, event_type, household_id, provider_subscription_id, payload) values
   ('stripe', 'evt_A1', 'invoice.paid', ha, 'sub_ALPHA', jsonb_build_object('id', 'evt_A1', 'data', jsonb_build_object('object',
     jsonb_build_object('id', 'in_A1', 'customer', 'cus_ALPHA', 'customer_email', 'g1@example.com', 'customer_name', 'Alpha Guardian One',
       'amount_paid', 4900, 'tax', 300, 'metadata', jsonb_build_object('household_id', ha),
       'customer_address', jsonb_build_object('line1', '1 Alpha St'),
       'lines', jsonb_build_array(jsonb_build_object('amount', 4900, 'description', 'Alpha family plan')))))),
   ('stripe', 'evt_A2', 'customer.subscription.updated', null, 'sub_ALPHA', '{"id":"evt_A2","data":{"object":{"id":"sub_ALPHA","customer":"cus_ALPHA"}}}'),
   ('stripe', 'evt_B1', 'invoice.paid', hb, 'sub_BRAVO', '{"id":"evt_B1","data":{"object":{"customer_email":"gb@example.com","amount_paid":4900}}}');
  perform set_config('t.ha', ha::text, true); perform set_config('t.hb', hb::text, true);
  perform set_config('t.s1', s1::text, true); perform set_config('t.s2', s2::text, true);
  perform set_config('t.s3', s3::text, true); perform set_config('t.si', si::text, true);
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 2. Clients can't call any of it, or read the request tables. (Before any request runs.)
-- ---------------------------------------------------------------------------------------------------------------
do $$
declare u uuid; f text;
begin
  foreach u in array array[null, '20000000-0000-0000-0000-0000000000a1', '20000000-0000-0000-0000-000000000051']::uuid[] loop
    if u is null then perform hp_test.as_anon(); else perform hp_test.as_user(u); end if;
    foreach f in array array[
      format('select public.admin_export_student(%L, %L, ''x'')', current_setting('t.s1'), current_setting('t.ha')),
      format('select public.admin_export_household(%L, ''x'')', current_setting('t.ha')),
      format('select public.admin_delete_student(%L, ''r'', %L, ''x'')', current_setting('t.s1'), current_setting('t.ha')),
      format('select public.admin_delete_household(%L, ''r'', ''x'')', current_setting('t.ha')),
      'select public.admin_record_auth_deletion(gen_random_uuid())',
      'select public.admin_purge_expired_retention()',
      format('select public.data_request_student_tables(%L, true)', current_setting('t.s1')),
      format('select public.data_request_household_tables(%L)', current_setting('t.ha')),
      format('select public.data_request_delete_student_internal(%L, true, null)', current_setting('t.s1')),
      format('select public.data_request_delete_household_internal(%L, true, null)', current_setting('t.ha')),
      'select * from public.data_request_log', 'select * from public.retained_email_records',
      'insert into public.data_request_log(action, subject_kind, subject_id, requested_by, channel, requested_at, performed_by) values (''export'', ''student'', gen_random_uuid(), ''x'', ''email'', now(), ''x'')'] loop
      perform hp_test.expect_error(f, '42501');
    end loop;
  end loop;
  perform hp_test.as_owner();
  -- The grants say the same: no client role holds EXECUTE on any admin_ or data_request_ function.
  perform hp_test.eq((select count(*) from pg_proc p join pg_namespace n on n.oid = p.pronamespace
    cross join (values ('anon'), ('authenticated'), ('public')) r(role)
    where n.nspname = 'public' and (p.proname like 'admin\_%' or p.proname like 'data\_request\_%')
      and case when r.role = 'public' then exists (select 1 from aclexplode(coalesce(p.proacl, acldefault('f', p.proowner))) a where a.grantee = 0 and a.privilege_type = 'EXECUTE')
               else has_function_privilege(r.role, p.oid, 'EXECUTE') end), 0::bigint, 'no client EXECUTE on data-request functions');
  perform hp_test.check(has_function_privilege('service_role', 'public.admin_delete_household(uuid, text, text, boolean, uuid, text, timestamptz)', 'EXECUTE'), 'service_role may delete');
  perform hp_test.check(not has_function_privilege('service_role', 'public.data_request_delete_household_internal(uuid, boolean, uuid)', 'EXECUTE'), 'internals are not service API');
  perform hp_test.check((select relrowsecurity from pg_class where oid = 'public.data_request_log'::regclass), 'RLS on data_request_log');
  perform hp_test.check((select relrowsecurity from pg_class where oid = 'public.retained_email_records'::regclass), 'RLS on retained_email_records');
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 3. Exports: complete, no other household's rows, no other person's ids in a student export, no secrets or keys.
-- ---------------------------------------------------------------------------------------------------------------
set local role service_role;
create temp table dr_exports as
select 'household_a'::text k, public.admin_export_household(current_setting('t.ha')::uuid, 'g1@example.com') doc
union all select 'household_b', public.admin_export_household(current_setting('t.hb')::uuid, 'gb@example.com')
union all select 's1', public.admin_export_student(current_setting('t.s1')::uuid, current_setting('t.ha')::uuid, 'g1@example.com')
union all select 'indy', public.admin_export_student(current_setting('t.si')::uuid, null, 'indy@example.com');
reset role;

do $$
declare a jsonb := (select doc from dr_exports where k = 'household_a'); s1 jsonb := (select doc from dr_exports where k = 's1');
  b jsonb := (select doc from dr_exports where k = 'household_b'); t text; v_bad text; secret text; e record;
begin
  -- Every personal or retained table is a key of the household export, with rows from the fixture.
  for t in select split_part(tbl, '.', 2) from dr_decisions where decision in ('personal', 'retained') loop
    perform hp_test.check(a->'tables' ? t, 'household export has table ' || t);
    perform hp_test.check(jsonb_array_length(a->'tables'->t) > 0, 'household export has rows for ' || t);
  end loop;
  -- And no key that is not a decided table.
  select string_agg(x, ', ') into v_bad from jsonb_object_keys(a->'tables') x
  where 'public.' || x not in (select tbl from dr_decisions where decision in ('personal', 'retained'));
  perform hp_test.check(v_bad is null, 'export keys are decided tables: ' || coalesce(v_bad, ''));
  -- Exact row counts against the tables.
  perform hp_test.eq(jsonb_array_length(a->'tables'->'students'), 2, 'A has two students');
  perform hp_test.eq(jsonb_array_length(a->'tables'->'practice_attempts'), 2, 'A attempts from both students');
  perform hp_test.eq(jsonb_array_length(a->'tables'->'practice_session_items'), 4, 'A session items');
  perform hp_test.eq(jsonb_array_length(a->'tables'->'household_members'), 3, 'A members: g1, g2, S1 login');
  perform hp_test.eq(jsonb_array_length(a->'tables'->'household_invitations'), 4, 'A invitations');
  perform hp_test.eq(jsonb_array_length(a->'tables'->'billing_events'), 1, 'A billing event (summary)');

  -- No cross-household leak: nothing of B (ids, names, emails, provider refs) in A, and the reverse.
  foreach secret in array array[current_setting('t.hb'), current_setting('t.s3'), '20000000-0000-0000-0000-0000000000b1',
    '20000000-0000-0000-0000-000000000053', 'Bravo', 'bravo', 'gb@example.com', current_setting('t.si'), 'Indy'] loop
    perform hp_test.check(position(secret in a::text) = 0, 'household A export leaks ' || secret);
    perform hp_test.check(position(secret in s1::text) = 0, 'S1 export leaks ' || secret);
  end loop;
  foreach secret in array array[current_setting('t.ha'), current_setting('t.s1'), current_setting('t.s2'), 'Alpha',
    '20000000-0000-0000-0000-0000000000a1', '20000000-0000-0000-0000-000000000051'] loop
    perform hp_test.check(position(secret in b::text) = 0, 'household B export leaks ' || secret);
  end loop;
  -- A student export carries no sibling and no other account's id (guardian actors, guardian alert settings).
  foreach secret in array array[current_setting('t.s2'), 'Alpha Kid Two', '20000000-0000-0000-0000-0000000000a1',
    '20000000-0000-0000-0000-0000000000a2', 'Alpha Guardian One', 'Shared Guardian'] loop
    perform hp_test.check(position(secret in s1::text) = 0, 'S1 export leaks other person ' || secret);
  end loop;
  perform hp_test.check(not (s1->'tables' ? 'alert_preferences'), 'student export has no guardian alert settings');
  perform hp_test.eq(jsonb_array_length(s1->'tables'->'profiles'), 1, 'student export has the student login profile');
  perform hp_test.eq(jsonb_array_length(s1->'tables'->'practice_attempts'), 1, 'S1 attempts only');
  perform hp_test.eq(s1->'tables'->'practice_attempts'->0->>'selected_answer', 'A', 'student answers are exported');

  -- No secrets, question content or answer keys, and no provider identifiers or raw payloads, anywhere.
  for e in select k, doc from dr_exports loop
    foreach secret in array array['code_hash', 'short_code_hash', 'pepper', 'accepted_answers', 'teaching_explanation',
      'Question 1', 'First hint', 'cus_ALPHA', 'cus_BRAVO', 'sub_ALPHA', 'sub_BRAVO', 'payload', '1 Alpha St', 'customer_email'] loop
      perform hp_test.check(position(secret in e.doc::text) = 0, e.k || ' export contains ' || secret);
    end loop;
    foreach secret in array (select array_agg(code_hash) || array_agg(short_code_hash) filter (where short_code_hash is not null)
      from public.household_invitations) loop
      perform hp_test.check(position(secret in e.doc::text) = 0, e.k || ' export contains an invitation digest');
    end loop;
  end loop;
  -- Exports are logged, with counts only.
  perform hp_test.eq((select count(*) from public.data_request_log where action = 'export'), 4::bigint, 'four export rows');
  perform hp_test.eq((select (exported->>'practice_attempts')::int from public.data_request_log
    where action = 'export' and subject_id = current_setting('t.ha')::uuid), 2, 'export row counts');
  perform hp_test.check((select requested_by from public.data_request_log where subject_id = current_setting('t.ha')::uuid) = 'g1@example.com', 'export requester');
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 4. Safeguards: scope, dry run by default, explicit confirmation for a live run, live subscription.
-- ---------------------------------------------------------------------------------------------------------------
create temp table dr_snapshot(tbl text primary key, n bigint);
create function dr_test.snapshot() returns void language plpgsql as $$
declare t text; n bigint;
begin
  delete from dr_snapshot;
  for t in select tbl from dr_decisions where decision <> 'reference' loop
    execute format('select count(*) from %s', t) into n;
    insert into dr_snapshot values (t, n);
  end loop;
end $$;
create function dr_test.unchanged(p_msg text) returns void language plpgsql as $$
declare t text; n bigint; want bigint;
begin
  for t, want in select tbl, s.n from dr_snapshot s loop
    execute format('select count(*) from %s', t) into n;
    perform hp_test.eq(n, want, p_msg || ': ' || t);
  end loop;
end $$;
grant all on dr_snapshot to service_role;
grant execute on all functions in schema dr_test to service_role;

do $$
declare r jsonb; ha uuid := current_setting('t.ha'); hb uuid := current_setting('t.hb'); s1 uuid := current_setting('t.s1');
  s3 uuid := current_setting('t.s3'); si uuid := current_setting('t.si');
begin
  perform dr_test.snapshot();
  perform set_config('role', 'service_role', true);
  -- A student of another household (or none) is refused, for export and delete.
  perform hp_test.expect_error(format('select public.admin_export_student(%L, %L, ''g1@example.com'')', s3, ha), '42501', '%not in household%');
  perform hp_test.expect_error(format('select public.admin_delete_student(%L, ''request'', %L, ''g1@example.com'')', s3, ha), '42501', '%not in household%');
  perform hp_test.expect_error(format('select public.admin_delete_student(%L, ''request'', %L, ''g1@example.com'')', si, ha), '42501');
  perform hp_test.expect_error(format('select public.admin_delete_student(%L, ''request'', null, ''g1@example.com'')', s1), '42501');
  -- Requester and reason are required.
  perform hp_test.expect_error(format('select public.admin_delete_household(%L, ''request'', '' '')', ha), '22023');
  perform hp_test.expect_error(format('select public.admin_delete_household(%L, null, ''g1@example.com'')', ha), '22023');
  -- A live run needs p_dry_run => false AND p_confirm => the same id.
  perform hp_test.expect_error(format('select public.admin_delete_household(%L, ''request'', ''g1@example.com'', p_dry_run => false)', ha), '22023', '%p_confirm%');
  perform hp_test.expect_error(format('select public.admin_delete_household(%L, ''request'', ''g1@example.com'', p_dry_run => false, p_confirm => %L)', ha, hb), '22023', '%p_confirm%');
  perform hp_test.expect_error(format('select public.admin_delete_student(%L, ''request'', %L, ''g1@example.com'', p_dry_run => false, p_confirm => %L)', s1, ha, ha), '22023');
  perform hp_test.expect_error(format('select public.admin_delete_household(%L, ''request'', ''g1@example.com'', p_dry_run => null)', ha), '22023');
  -- A live subscription is refused, even in a dry run.
  perform hp_test.expect_error(format('select public.admin_delete_household(%L, ''request'', ''g1@example.com'')', ha), '55000', '%cancel%');
  perform set_config('role', 'none', true);
  update public.subscriptions set status = 'canceled' where provider_subscription_id = 'sub_ALPHA';
  perform dr_test.snapshot();
  -- A dry run (the default) reports and changes nothing, and writes no log row.
  perform set_config('role', 'service_role', true);
  r := public.admin_delete_household(ha, 'request', 'g1@example.com');
  perform set_config('role', 'none', true);
  perform hp_test.check((r->>'dry_run')::boolean, 'dry run is the default');
  perform hp_test.eq((r->'removed'->>'practice_attempts')::int, 2, 'dry run counts attempts');
  perform hp_test.eq((r->'removed'->>'students')::int, 2, 'dry run counts students');
  perform hp_test.check(r->'auth_users_to_delete' @> '["20000000-0000-0000-0000-0000000000a1","20000000-0000-0000-0000-000000000051"]'
    and not r->'auth_users_to_delete' @> '["20000000-0000-0000-0000-0000000000a2"]', 'dry run auth list ' || (r->'auth_users_to_delete')::text);
  perform set_config('role', 'service_role', true);
  r := public.admin_delete_student(s1, 'request', ha, 'g1@example.com', p_dry_run => true);
  perform set_config('role', 'none', true);
  perform dr_test.unchanged('dry runs change nothing');
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 5. Delete one guardian-managed student (S2): their rows go, the household and sibling stay, email record kept.
-- ---------------------------------------------------------------------------------------------------------------
do $$
declare r jsonb; ha uuid := current_setting('t.ha'); s1 uuid := current_setting('t.s1'); s2 uuid := current_setting('t.s2'); l public.data_request_log;
begin
  perform set_config('role', 'service_role', true);
  r := public.admin_delete_student(s2, 'Parent asked by email to delete one student profile', ha, 'g1@example.com',
    p_dry_run => false, p_confirm => s2, p_requested_at => now() - interval '2 days');
  perform set_config('role', 'none', true);
  perform hp_test.check(not (r->>'dry_run')::boolean, 'live run');
  perform hp_test.eq(jsonb_array_length(r->'auth_users_to_delete'), 0, 'guardian-managed student has no login to delete');
  perform hp_test.check(not exists (select 1 from public.students where id = s2), 'S2 deleted');
  perform hp_test.eq((select count(*) from public.practice_attempts where student_id = s2), 0::bigint, 'S2 attempts deleted');
  perform hp_test.eq((select count(*) from public.alert_preferences where student_id = s2), 0::bigint, 'S2 alert settings deleted');
  perform hp_test.eq((select count(*) from public.household_invitations where student_id = s2), 0::bigint, 'S2 invitations deleted');
  perform hp_test.eq((select count(*) from public.practice_attempts where student_id = s1), 1::bigint, 'sibling kept');
  perform hp_test.check(exists (select 1 from public.households where id = ha), 'household kept');
  -- Retention: the recent invitation email record is kept, unlinked from any account.
  perform hp_test.eq((select count(*) from public.retained_email_records where recipient_email = 'alpha.kid.two@example.com'
    and send_count = 2 and retain_until > now() + interval '12 months'), 1::bigint, 'email-sent record kept 13 months');
  -- The audit row.
  select * into l from public.data_request_log where id = (r->>'request_id')::uuid;
  perform hp_test.eq(l.action, 'delete', 'audit action'); perform hp_test.eq(l.subject_kind, 'student', 'audit kind');
  perform hp_test.eq(l.subject_id, s2, 'audit subject'); perform hp_test.eq(l.household_id, ha, 'audit household');
  perform hp_test.eq(l.requested_by, 'g1@example.com', 'audit requester'); perform hp_test.eq(l.channel, 'email', 'audit channel');
  perform hp_test.check(l.reason like 'Parent asked%', 'audit reason');
  perform hp_test.check(l.requested_at < l.performed_at - interval '1 day', 'audit keeps when it was requested');
  perform hp_test.eq((l.removed->>'practice_attempts')::int, 1, 'audit removed attempts');
  perform hp_test.eq((l.removed->>'practice_attempt_events')::int, 2, 'audit removed events');
  perform hp_test.eq((l.kept->>'retained_email_records')::int, 1, 'audit kept email record');
  perform hp_test.check(position('Alpha Kid Two' in to_jsonb(l)::text) = 0, 'audit row holds no name');
  perform hp_test.check((select data_request_id from public.retained_email_records where recipient_email = 'alpha.kid.two@example.com') = l.id, 'retained row points at the request');
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 6. Delete household A: everything personal goes, B and g2's B membership stay, billing kept de-identified.
-- ---------------------------------------------------------------------------------------------------------------
do $$
declare r jsonb; x jsonb; ha uuid := current_setting('t.ha'); s1 uuid := current_setting('t.s1'); t text; l public.data_request_log;
begin
  perform set_config('role', 'service_role', true);
  x := public.admin_export_household(ha, 'g1@example.com');
  r := public.admin_delete_household(ha, 'Account holder asked by email to delete the household', 'g1@example.com',
    p_dry_run => false, p_confirm => ha);
  perform set_config('role', 'none', true);
  -- Removed counts match what the export held, table by table (g2's profile stays: g2 is still in household B).
  for t in select split_part(tbl, '.', 2) from dr_decisions where decision = 'personal' loop
    perform hp_test.eq(coalesce((r->'removed'->>t)::int, 0), jsonb_array_length(x->'tables'->t) - case when t = 'profiles' then 1 else 0 end,
      'removed matches export for ' || t);
  end loop;
  perform hp_test.check(not exists (select 1 from public.households where id = ha), 'household deleted');
  perform hp_test.check(not exists (select 1 from public.students where id = s1), 'S1 deleted');
  perform hp_test.check(not exists (select 1 from public.household_members where household_id = ha), 'memberships deleted');
  perform hp_test.check(not exists (select 1 from public.subscriptions where provider_subscription_id = 'sub_ALPHA'), 'subscription state deleted');
  perform hp_test.check(not exists (select 1 from public.billing_customers where provider_customer_id = 'cus_ALPHA'), 'customer map deleted');
  -- Accounts: g1 and S1's login are listed for the admin API, g2 (in B) is not; their profiles and rate-limit rows are gone.
  perform hp_test.check(r->'auth_users_to_delete' @> '["20000000-0000-0000-0000-0000000000a1","20000000-0000-0000-0000-000000000051"]'
    and jsonb_array_length(r->'auth_users_to_delete') = 2, 'auth list ' || (r->'auth_users_to_delete')::text);
  perform hp_test.check(not exists (select 1 from public.profiles where id in ('20000000-0000-0000-0000-0000000000a1', '20000000-0000-0000-0000-000000000051')), 'profiles deleted');
  perform hp_test.check(not exists (select 1 from public.invitation_code_attempts where user_id in ('20000000-0000-0000-0000-0000000000a1', '20000000-0000-0000-0000-000000000051')), 'rate-limit rows deleted');
  perform hp_test.check(exists (select 1 from public.profiles where id = '20000000-0000-0000-0000-0000000000a2'), 'g2 profile kept');
  perform hp_test.check(exists (select 1 from public.invitation_code_attempts where user_id = '20000000-0000-0000-0000-0000000000a2'), 'g2 rate-limit kept');
  perform hp_test.check(exists (select 1 from public.household_members where household_id = current_setting('t.hb')::uuid
    and user_id = '20000000-0000-0000-0000-0000000000a2'), 'g2 keeps B membership');
  -- Billing records kept, de-identified: no household link, no name/email/address/metadata, amounts and ids intact.
  perform hp_test.eq((select count(*) from public.billing_events where event_id in ('evt_A1', 'evt_A2') and household_id is null and deidentified_at is not null), 2::bigint, 'A billing events kept de-identified');
  perform hp_test.check((select payload::text from public.billing_events where event_id = 'evt_A1') not similar to '%(g1@example.com|Alpha Guardian|1 Alpha St|Alpha family plan|metadata|' || ha || ')%', 'A payload scrubbed');
  perform hp_test.eq((select payload->'data'->'object'->>'amount_paid' from public.billing_events where event_id = 'evt_A1'), '4900', 'amount kept');
  perform hp_test.eq((select payload->'data'->'object'->>'tax' from public.billing_events where event_id = 'evt_A1'), '300', 'tax kept');
  perform hp_test.eq((select payload->'data'->'object'->>'customer' from public.billing_events where event_id = 'evt_A1'), 'cus_ALPHA', 'provider ref kept');
  perform hp_test.eq((select payload->'data'->'object'->>'customer_email' from public.billing_events where event_id = 'evt_B1'), 'gb@example.com', 'B billing untouched');
  perform hp_test.eq((select household_id from public.billing_events where event_id = 'evt_B1'), current_setting('t.hb')::uuid, 'B billing linked');
  -- Email-sent records: the 14-month-old one is past its 13 months and not kept.
  perform hp_test.eq((select count(*) from public.retained_email_records where recipient_email = 'old.guardian@example.com'), 0::bigint, 'expired email record not kept');
  -- The audit row.
  select * into l from public.data_request_log where id = (r->>'request_id')::uuid;
  perform hp_test.eq(l.subject_kind, 'household', 'household audit kind');
  perform hp_test.eq((l.kept->>'billing_events')::int, 2, 'audit kept billing events');
  perform hp_test.eq(l.kept->'billing_customer_refs'->0->>'provider_customer_id', 'cus_ALPHA', 'audit keeps the provider customer ref');
  perform hp_test.eq(l.auth_users_to_delete, array['20000000-0000-0000-0000-000000000051', '20000000-0000-0000-0000-0000000000a1']::uuid[], 'audit auth list');
  perform hp_test.check(l.auth_users_deleted_at is null, 'auth deletion not yet recorded');
  perform hp_test.check(position('Alpha' in to_jsonb(l)::text) = 0, 'audit row holds no names');
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 7. Independent student (no household): their login is listed; recording the auth deletion waits for the admin API.
-- ---------------------------------------------------------------------------------------------------------------
do $$
declare r jsonb; si uuid := current_setting('t.si'); v uuid; rec jsonb;
begin
  perform set_config('role', 'service_role', true);
  r := public.admin_delete_student(si, 'Student (18+) asked by email', null, 'indy@example.com', p_dry_run => false, p_confirm => si);
  perform set_config('role', 'none', true);
  perform hp_test.eq(r->'auth_users_to_delete', '["20000000-0000-0000-0000-000000000052"]'::jsonb, 'independent login listed');
  perform hp_test.check(not exists (select 1 from public.profiles where id = '20000000-0000-0000-0000-000000000052'), 'independent profile deleted');
  -- Record the auth deletion: refused while the auth users exist.
  perform set_config('role', 'service_role', true);
  perform hp_test.expect_error(format('select public.admin_record_auth_deletion(%L)', r->>'request_id'), '55000', '%still exist%');
  perform set_config('role', 'none', true);
  delete from auth.users where id = '20000000-0000-0000-0000-000000000052';  -- stands in for the admin API
  perform set_config('role', 'service_role', true);
  rec := public.admin_record_auth_deletion((r->>'request_id')::uuid);
  perform set_config('role', 'none', true);
  perform hp_test.check((select auth_users_deleted_at is not null from public.data_request_log where id = (r->>'request_id')::uuid), 'auth deletion recorded');
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 8. After every deletion, each personal table holds exactly household B's rows: nothing of A or I is left.
-- ---------------------------------------------------------------------------------------------------------------
do $$
declare b jsonb; t text; n bigint;
begin
  perform set_config('role', 'service_role', true);
  b := public.admin_export_household(current_setting('t.hb')::uuid, 'gb@example.com');
  perform set_config('role', 'none', true);
  for t in select split_part(tbl, '.', 2) from dr_decisions where decision = 'personal' loop
    execute format('select count(*) from public.%I', t) into n;
    perform hp_test.eq(n, jsonb_array_length(b->'tables'->t)::bigint, 'only B rows remain in ' || t);
  end loop;
  perform hp_test.eq((select count(*) from public.invitation_code_attempts), 2::bigint, 'only g2 and gb rate-limit rows remain');
  -- Purge: email-sent records past 13 months are removed; current ones stay.
  insert into public.retained_email_records(kind, recipient_email, send_count, last_sent_at, retain_until)
  values ('household_invitation', 'expired@example.com', 1, now() - interval '14 months', now() - interval '1 month');
  perform set_config('role', 'service_role', true);
  perform hp_test.eq(public.admin_purge_expired_retention(), 1, 'purge removes one expired record');
  perform set_config('role', 'none', true);
  perform hp_test.eq((select count(*) from public.retained_email_records), 1::bigint, 'current email record stays');
  perform hp_test.eq((select count(*) from public.data_request_log where action = 'export'), 6::bigint, 'six exports logged');
  perform hp_test.eq((select count(*) from public.data_request_log where action = 'delete'), 3::bigint, 'three live deletions logged, no dry runs');
end $$;

rollback;
