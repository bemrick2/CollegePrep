-- A4 (#218 B8): data export and deletion by service role (docs/operations/DATA_REQUESTS.md).
-- Completeness (every table has a decision), no cross-household leaks, no secrets or answer keys, retention and
-- payment-event de-identification (realistic Stripe payloads), late webhooks, the audit row, the dry-run and scope
-- safeguards, and exact privileges (no client access; service_role only on the entry points). Everything is rolled back.
-- Run with psql -v ON_ERROR_STOP=1. CI runs it twice: on plain PostgreSQL, and on a database created with Supabase's
-- default privileges (new tables and functions granted to anon, authenticated and service_role), as hosted is.
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
--   request_log   written by this procedure (audit, provider references, retained email-sent records)
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
 ('public.student_setup_progress', 'personal'), ('public.practice_reminder_settings', 'personal'),
 ('public.practice_reminder_changes', 'personal'), ('public.practice_reminder_deliveries', 'personal'),
 ('public.question_reports', 'personal'),
 ('public.billing_events', 'retained'), ('public.parent_email_deliveries', 'retained'),
 ('public.invitation_code_attempts', 'security'), ('public.notification_devices', 'security'),
 ('public.notification_device_claims', 'security'), ('public.notification_device_claim_failures', 'security'),
 ('public.data_request_log', 'request_log'), ('public.data_request_billing_refs', 'request_log'),
 ('public.retained_email_records', 'request_log'),
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

-- The decision for every COLUMN of every personal, retained and security table, as the household export shows it:
-- 'export' columns appear in every exported row, 'omit' columns in none (secrets, provider ids, device keys, raw
-- payloads). A new column on these tables fails the completeness check until it is listed here.
create temp table dr_columns(tbl text not null, col text not null, decision text not null check (decision in ('export', 'omit')),
  primary key (tbl, col));
insert into dr_columns select t, c, d from (values
  ('public.households', array['id', 'name', 'created_by', 'time_zone', 'created_at', 'home_state'], array['export', 'export', 'export', 'export', 'export', 'export']),
  ('public.household_members', array['household_id', 'user_id', 'role', 'can_manage_students', 'can_set_goals', 'can_view_progress', 'can_manage_members', 'can_manage_billing', 'created_at'], array['export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.household_invitations', array['id', 'household_id', 'role', 'student_id', 'permissions', 'code_hash', 'created_by', 'created_at', 'expires_at', 'accepted_by', 'accepted_at', 'short_code_hash', 'recipient_email', 'revoked_at', 'revoked_by', 'email_send_count', 'last_emailed_at'], array['export', 'export', 'export', 'export', 'export', 'omit', 'export', 'export', 'export', 'export', 'export', 'omit', 'export', 'export', 'export', 'export', 'export']),
  ('public.household_saved_schools', array['household_id', 'institution_key', 'added_by', 'added_at', 'is_primary'], array['export', 'export', 'export', 'export', 'export']),
  ('public.profiles', array['id', 'display_name', 'created_at'], array['export', 'export', 'export']),
  ('public.students', array['id', 'household_id', 'display_name', 'graduation_year', 'grade_level', 'account_mode', 'is_independent', 'linked_user_id', 'time_zone', 'created_at', 'archived_at', 'home_state'], array['export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.weekly_practice_goals', array['id', 'student_id', 'week_start', 'target_questions', 'target_minutes', 'subject', 'goal_mode', 'set_by', 'created_at', 'updated_at'], array['export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.practice_sessions', array['id', 'student_id', 'target_minutes', 'started_at', 'ended_at', 'goal_id'], array['export', 'export', 'export', 'export', 'export', 'export']),
  ('public.practice_session_items', array['session_id', 'position', 'question_id', 'reason', 'seen_before', 'last_seen'], array['export', 'export', 'export', 'export', 'export', 'export']),
  ('public.question_reports', array['id', 'question_id', 'content_hash', 'question_pool', 'attempt_id', 'student_id', 'reporter_user_id',
     'reporter_role', 'reason', 'note', 'status', 'created_at', 'updated_at', 'revision', 'reviewed_at', 'reviewed_by', 'resolution_note'],
   array['export', 'export', 'export', 'omit', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export',
     'export', 'export', 'omit', 'omit']),
  ('public.practice_attempts', array['id', 'session_id', 'student_id', 'question_id', 'presented_at', 'first_interaction_ms', 'submitted_at', 'elapsed_ms', 'active_ms', 'selected_answer', 'is_correct', 'skipped', 'confidence', 'hint_count', 'ai_help_used', 'strategy_used_id', 'attempt_number', 'benchmark_id'], array['export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.practice_attempt_events', array['id', 'attempt_id', 'student_id', 'kind', 'occurred_at', 'answer', 'detail'], array['export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.ai_help_requests', array['id', 'attempt_id', 'student_id', 'requested_by', 'requested_at', 'mode', 'status', 'response', 'provider', 'model', 'tokens'], array['export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.practice_benchmarks', array['id', 'student_id', 'kind', 'exam_version_id', 'started_at', 'completed_at', 'metrics', 'items_assigned_at'], array['export', 'export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.practice_benchmark_items', array['benchmark_id', 'student_id', 'exam_version_id', 'question_id', 'section', 'position', 'seen_before', 'last_seen', 'assigned_at'], array['export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.student_test_scores', array['id', 'student_id', 'exam_version_id', 'test_date', 'composite', 'section_scores', 'score_source', 'entered_by', 'created_at'], array['export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.student_exam_plan', array['student_id', 'exam_key', 'score', 'taken_on', 'set_by', 'created_at', 'updated_at'], array['export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.student_planning_preferences', array['student_id', 'exam_family', 'target_score', 'goals', 'daily_minutes', 'set_by', 'created_at', 'updated_at', 'exam_intent', 'planned_test_date', 'study_days'], array['export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.student_academic_interests', array['student_id', 'certainty', 'interests', 'set_by', 'created_at', 'updated_at'], array['export', 'export', 'export', 'export', 'export', 'export']),
  ('public.alert_preferences', array['user_id', 'student_id', 'channel', 'inactivity_days', 'enabled', 'created_at', 'weekly_digest'], array['export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.subscriptions', array['id', 'owner_user_id', 'household_id', 'plan_key', 'status', 'provider', 'provider_customer_id', 'provider_subscription_id', 'current_period_end', 'created_at', 'current_period_start', 'cancel_at_period_end', 'environment', 'last_event_at', 'updated_at'], array['export', 'export', 'export', 'export', 'export', 'export', 'omit', 'omit', 'export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.billing_customers', array['household_id', 'provider', 'provider_customer_id', 'created_by', 'created_at', 'environment'], array['export', 'export', 'omit', 'export', 'export', 'export']),
  ('public.student_setup_progress', array['student_id', 'setup_completed_at', 'starting_point_answered_at', 'benchmark_scheduled_for', 'updated_by', 'updated_at'], array['export', 'export', 'export', 'export', 'export', 'export']),
  ('public.practice_reminder_settings', array['student_id', 'enabled', 'times', 'days', 'quiet_start', 'quiet_end', 'school_days', 'school_start', 'school_end', 'max_per_day', 'max_per_week', 'snoozed_until', 'updated_by', 'updated_at'], array['export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.practice_reminder_changes', array['id', 'student_id', 'household_id', 'enabled', 'changed_by', 'changed_by_role', 'changed_at', 'notify_guardians'], array['export', 'export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.practice_reminder_deliveries', array['id', 'student_id', 'device_id', 'slot', 'reminder_key', 'channel', 'status', 'sent_at', 'claimed_at', 'opened_at', 'snoozed_at', 'failure_reason'], array['export', 'export', 'omit', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export', 'export']),
  ('public.billing_events', array['id', 'provider', 'event_id', 'event_type', 'household_id', 'provider_subscription_id', 'payload', 'received_at', 'processed_at', 'error', 'deidentified_at'], array['export', 'export', 'omit', 'export', 'omit', 'omit', 'omit', 'export', 'export', 'omit', 'omit']),
  ('public.parent_email_deliveries', array['id', 'user_id', 'kind', 'period_key', 'sent_at'], array['export', 'export', 'export', 'export', 'export']),
  ('public.invitation_code_attempts', array['user_id', 'attempted_at'], array['omit', 'omit']),
  ('public.notification_devices', array['id', 'user_id', 'permission', 'platform', 'channel', 'push_token', 'endpoint', 'p256dh', 'auth_secret', 'checked_at', 'gone_at', 'created_at', 'handle'], array['omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit']),
  -- Device claims and failed confirmations (20261103010000): security records, never exported.
  ('public.notification_device_claims', array['id', 'target_device_id', 'claimant_user_id', 'device_id', 'permission', 'platform', 'channel', 'push_token',
    'endpoint', 'p256dh', 'auth_secret', 'nonce_hash', 'status', 'created_at', 'expires_at', 'issued_at', 'resolved_at'],
    array['omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit', 'omit']),
  ('public.notification_device_claim_failures', array['id', 'user_id', 'failed_at'], array['omit', 'omit', 'omit'])) v(t, cs, ds), unnest(cs, ds) u(c, d);
grant select on dr_columns to anon, authenticated, service_role;

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
  -- Every column of every personal, retained and security table has a decision, and every decision names a column.
  select string_agg(c.table_schema || '.' || c.table_name || '.' || c.column_name, ', ') into v_missing
  from information_schema.columns c join dr_decisions d on d.tbl = c.table_schema || '.' || c.table_name
  where d.decision in ('personal', 'retained', 'security')
    and not exists (select 1 from dr_columns k where k.tbl = d.tbl and k.col = c.column_name);
  if v_missing is not null then
    raise exception 'Columns with no data-request decision (add to dr_columns in supabase/tests/data_requests.sql and, if exported, check the export functions): %', v_missing;
  end if;
  select string_agg(k.tbl || '.' || k.col, ', ') into v_stale from dr_columns k
  where not exists (select 1 from information_schema.columns c where c.table_schema || '.' || c.table_name = k.tbl and c.column_name = k.col)
     or k.tbl not in (select tbl from dr_decisions where decision in ('personal', 'retained', 'security'));
  if v_stale is not null then raise exception 'Column decisions name columns that do not exist: %', v_stale; end if;
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 2. Exact privileges, checked from the ACLs themselves (so they hold under Supabase's default privileges too):
-- entry points EXECUTE for service_role only; internals for nobody but the owner; request tables SELECT for
-- service_role only. Then every client role, and service_role on what it must not touch, is refused.
-- ---------------------------------------------------------------------------------------------------------------
do $$
declare v_bad text;
begin
  -- On the Supabase-defaults run, show that the defaults really are in force (else the run proves nothing).
  if current_setting('dr.expect_supabase_defaults', true) = 'on' then
    perform hp_test.check(exists (select 1 from pg_default_acl d cross join aclexplode(d.defaclacl) a
      where d.defaclobjtype = 'f' and a.grantee = 'service_role'::regrole and a.privilege_type = 'EXECUTE'),
      'Supabase default privileges grant functions to service_role');
    perform hp_test.check(exists (select 1 from pg_default_acl d cross join aclexplode(d.defaclacl) a
      where d.defaclobjtype = 'r' and a.grantee = 'service_role'::regrole and a.privilege_type = 'INSERT'),
      'Supabase default privileges grant tables to service_role');
  end if;
  select string_agg(format('%s: %s', f, got), '; ') into v_bad from (
    select p.oid::regprocedure::text f,
      coalesce((select string_agg(case when a.grantee = 0 then 'public' else pg_get_userbyid(a.grantee) end, ',' order by 1)
        from aclexplode(coalesce(p.proacl, acldefault('f', p.proowner))) a
        where a.privilege_type = 'EXECUTE' and a.grantee <> p.proowner), '') got,
      case when p.proname like 'admin\_%' or p.proname in ('record_billing_event', 'deidentify_billing_event')
        then 'service_role' else '' end want
    from pg_proc p join pg_namespace n on n.oid = p.pronamespace
    where n.nspname = 'public' and (p.proname like 'admin\_%' or p.proname like 'data\_request\_%'
      or p.proname in ('record_billing_event', 'deidentify_billing_event'))) x
  where got <> want;
  perform hp_test.check(v_bad is null, 'function EXECUTE grants: ' || coalesce(v_bad, ''));
  perform hp_test.eq((select count(*) from pg_proc p join pg_namespace n on n.oid = p.pronamespace
    where n.nspname = 'public' and (p.proname like 'admin\_%' or p.proname in ('record_billing_event', 'deidentify_billing_event'))), 9::bigint,
    'nine service entry points');
  select string_agg(format('%s: %s', t, got), '; ') into v_bad from (
    select c.oid::regclass::text t,
      coalesce((select string_agg(pg_get_userbyid(a.grantee) || '=' || a.privilege_type, ',' order by 1)
        from aclexplode(coalesce(c.relacl, acldefault('r', c.relowner))) a where a.grantee <> c.relowner), '') got
    from pg_class c where c.oid in ('public.data_request_log'::regclass, 'public.data_request_billing_refs'::regclass,
      'public.retained_email_records'::regclass)) x
  where got <> 'service_role=SELECT';
  perform hp_test.check(v_bad is null, 'request table grants: ' || coalesce(v_bad, ''));
  perform hp_test.check((select bool_and(relrowsecurity) from pg_class where oid in ('public.data_request_log'::regclass,
    'public.data_request_billing_refs'::regclass, 'public.retained_email_records'::regclass)), 'RLS on the request tables');
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
-- Push devices (security records: endpoint, keys): g1, g2, gb, S1's login and I's login.
insert into public.notification_devices(id, user_id, permission, platform, channel, endpoint, p256dh, auth_secret)
select ('60000000-0000-0000-0000-0000000000' || right(u::text, 2))::uuid, u, 'granted', 'desktop', 'webpush',
  'https://push.example/ep-' || right(u::text, 2), 'p256-' || right(u::text, 2), 'secret-' || right(u::text, 2)
from unnest(array['20000000-0000-0000-0000-0000000000a1', '20000000-0000-0000-0000-0000000000a2',
  '20000000-0000-0000-0000-0000000000b1', '20000000-0000-0000-0000-000000000051', '20000000-0000-0000-0000-000000000052']::uuid[]) u;
-- Device claims (security records): S1's login claims gb's device; gb claims g1's device; g2 claims gb's device; g1
-- claims gb's device (a claim only the household path removes: no device of A is its target).
-- Failed confirmations: g1, gb, S1's login and I's login (the last two only the student path removes).
insert into public.notification_device_claims(target_device_id, claimant_user_id, device_id, permission, platform, channel,
  endpoint, p256dh, auth_secret, expires_at)
values ('60000000-0000-0000-0000-0000000000b1', '20000000-0000-0000-0000-000000000051', gen_random_uuid(), 'granted', 'desktop', 'webpush',
        'https://push.example/ep-b1', 'p256-claim-51', 'secret-claim-51', now() + interval '10 minutes'),
       ('60000000-0000-0000-0000-0000000000a1', '20000000-0000-0000-0000-0000000000b1', gen_random_uuid(), 'granted', 'desktop', 'webpush',
        'https://push.example/ep-a1', 'p256-claim-b1', 'secret-claim-b1', now() + interval '10 minutes'),
       ('60000000-0000-0000-0000-0000000000b1', '20000000-0000-0000-0000-0000000000a2', gen_random_uuid(), 'granted', 'desktop', 'webpush',
        'https://push.example/ep-b1', 'p256-claim-a2', 'secret-claim-a2', now() + interval '10 minutes'),
       ('60000000-0000-0000-0000-0000000000b1', '20000000-0000-0000-0000-0000000000a1', gen_random_uuid(), 'granted', 'desktop', 'webpush',
        'https://push.example/ep-b1', 'p256-claim-a1', 'secret-claim-a1', now() + interval '10 minutes');
insert into public.notification_device_claim_failures(user_id) values
 ('20000000-0000-0000-0000-0000000000a1'), ('20000000-0000-0000-0000-0000000000b1'), ('20000000-0000-0000-0000-000000000051'),
 ('20000000-0000-0000-0000-000000000052');

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
    insert into public.alert_preferences(user_id, student_id, channel, inactivity_days, weekly_digest) values (p_guardian, p_student, 'email', 3, true);
  end if;
  update public.student_planning_preferences set exam_intent = 'sat', planned_test_date = '2027-03-13', study_days = '{1,3,5}'
  where student_id = p_student;
  insert into public.student_setup_progress(student_id, setup_completed_at, updated_by) values (p_student, now(), p_guardian);
  insert into public.practice_reminder_settings(student_id, enabled, updated_by) values (p_student, true, p_guardian);
  insert into public.practice_reminder_changes(student_id, household_id, enabled, changed_by, changed_by_role)
  select p_student, x.household_id, false, p_guardian, case when p_guardian is null then 'student' else 'guardian' end
  from public.students x where x.id = p_student;
  insert into public.practice_reminder_deliveries(student_id, device_id, slot, reminder_key, channel, status)
  values (p_student, (select d.id from public.notification_devices d where d.user_id = p_guardian), '16:30', '2026-11-02/16:30', 'webpush', 'sent');
end $$;

-- Realistic Stripe event payloads (API 2025 shapes), with every kind of personal field Stripe sends.
create function dr_test.invoice_paid(p_event text, p_customer text, p_sub text, p_household uuid) returns jsonb language sql as $$
  select jsonb_build_object('id', p_event, 'object', 'event', 'api_version', '2025-03-31.basil', 'created', 1790000000,
    'livemode', true, 'pending_webhooks', 1, 'type', 'invoice.paid',
    'request', jsonb_build_object('id', null, 'idempotency_key', 'idem-' || p_household),
    'data', jsonb_build_object('object', jsonb_build_object(
      'id', 'in_' || p_event, 'object', 'invoice', 'account_country', 'US', 'account_name', 'Prep & Price',
      'amount_due', 4900, 'amount_paid', 4900, 'amount_remaining', 0, 'attempt_count', 1, 'attempted', true,
      'billing_reason', 'subscription_cycle', 'collection_method', 'charge_automatically', 'created', 1790000000,
      'currency', 'usd', 'customer', p_customer,
      'customer_address', jsonb_build_object('city', 'Franklin', 'country', 'US', 'line1', '1 Alpha St', 'postal_code', '37064', 'state', 'TN'),
      'customer_email', 'g1@example.com', 'customer_name', 'Alpha Guardian One', 'customer_phone', '+16155550100',
      'customer_shipping', jsonb_build_object('name', 'Alpha Guardian One', 'address', jsonb_build_object('line1', '1 Alpha St')),
      'customer_tax_ids', jsonb_build_array(jsonb_build_object('type', 'us_ein', 'value', '12-3456789')),
      'hosted_invoice_url', 'https://invoice.stripe.com/i/acct_X/live_SECRETTOKEN',
      'invoice_pdf', 'https://pay.stripe.com/invoice/acct_X/live_SECRETTOKEN/pdf',
      'number', 'PP-0001', 'receipt_number', '2345-6789', 'status', 'paid', 'subtotal', 4600, 'tax', 300, 'total', 4900,
      'total_tax_amounts', jsonb_build_array(jsonb_build_object('amount', 300, 'inclusive', false, 'tax_rate', 'txr_1')),
      'period_start', 1787000000, 'period_end', 1790000000,
      'status_transitions', jsonb_build_object('paid_at', 1790000100, 'finalized_at', 1790000000),
      'metadata', jsonb_build_object('household_id', p_household),
      'parent', jsonb_build_object('type', 'subscription_details', 'subscription_details', jsonb_build_object(
        'subscription', p_sub, 'metadata', jsonb_build_object('household_id', p_household, 'owner_user_id', '20000000-0000-0000-0000-0000000000a1'))),
      'lines', jsonb_build_object('object', 'list', 'has_more', false, 'url', '/v1/invoices/in_' || p_event || '/lines',
        'data', jsonb_build_array(jsonb_build_object('id', 'il_1', 'object', 'line_item', 'amount', 4600, 'currency', 'usd',
          'description', '1 × Prep & Price Family (at $46.00 / year)', 'quantity', 1,
          'period', jsonb_build_object('start', 1787000000, 'end', 1790000000),
          'pricing', jsonb_build_object('type', 'price_details', 'unit_amount_decimal', '4600',
            'price_details', jsonb_build_object('price', 'price_1', 'product', 'prod_1')),
          'metadata', jsonb_build_object('student', 'Alpha Kid One')))),
      'custom_fields', jsonb_build_array(jsonb_build_object('name', 'Student', 'value', 'Alpha Kid One')),
      'footer', 'Alpha household', 'description', 'Alpha family plan')))
$$;
create function dr_test.checkout_completed(p_event text, p_customer text, p_sub text, p_household uuid) returns jsonb language sql as $$
  select jsonb_build_object('id', p_event, 'object', 'event', 'created', 1789990000, 'livemode', true,
    'type', 'checkout.session.completed', 'data', jsonb_build_object('object', jsonb_build_object(
      'id', 'cs_' || p_event, 'object', 'checkout.session', 'amount_subtotal', 4600, 'amount_total', 4900, 'currency', 'usd',
      'customer', p_customer, 'customer_email', 'g1@example.com', 'client_reference_id', p_household::text,
      'customer_details', jsonb_build_object('email', 'g1@example.com', 'name', 'Alpha Guardian One', 'phone', '+16155550100',
        'address', jsonb_build_object('line1', '1 Alpha St', 'postal_code', '37064', 'city', 'Franklin'),
        'tax_exempt', 'none', 'tax_ids', jsonb_build_array()),
      'collected_information', jsonb_build_object('individual_name', 'Alpha Guardian One', 'business_name', 'Alpha LLC',
        'shipping_details', jsonb_build_object('name', 'Alpha Guardian One', 'address', jsonb_build_object('line1', '1 Alpha St'))),
      'shipping_details', jsonb_build_object('name', 'Alpha Guardian One', 'address', jsonb_build_object('line1', '1 Alpha St')),
      'metadata', jsonb_build_object('household_id', p_household), 'mode', 'subscription', 'payment_status', 'paid',
      'status', 'complete', 'subscription', p_sub, 'invoice', 'in_1',
      'success_url', 'https://app.example/billing?hh=' || p_household, 'url', null,
      'custom_fields', jsonb_build_array(jsonb_build_object('key', 'student', 'text', jsonb_build_object('value', 'Alpha Kid One'))),
      'total_details', jsonb_build_object('amount_discount', 0, 'amount_shipping', 0, 'amount_tax', 300),
      'created', 1789990000, 'expires_at', 1790076400)))
$$;
create function dr_test.charge_succeeded(p_event text, p_customer text) returns jsonb language sql as $$
  select jsonb_build_object('id', p_event, 'object', 'event', 'created', 1790000050, 'livemode', true, 'type', 'charge.succeeded',
    'data', jsonb_build_object('object', jsonb_build_object('id', 'ch_' || p_event, 'object', 'charge', 'amount', 4900,
      'currency', 'usd', 'customer', p_customer, 'invoice', 'in_1', 'paid', true, 'status', 'succeeded', 'created', 1790000050,
      'receipt_email', 'g1@example.com', 'receipt_number', '2345-6789', 'receipt_url', 'https://pay.stripe.com/receipts/SECRETTOKEN',
      'billing_details', jsonb_build_object('email', 'g1@example.com', 'name', 'Alpha Guardian One', 'phone', null,
        'address', jsonb_build_object('line1', '1 Alpha St', 'postal_code', '37064')),
      'payment_method_details', jsonb_build_object('type', 'card', 'card', jsonb_build_object('brand', 'visa', 'last4', '4242',
        'exp_month', 12, 'exp_year', 2030, 'fingerprint', 'FPRINTxyz', 'country', 'US')))))
$$;
-- Every personal value the fixtures put in a payment payload.
create function dr_test.billing_pii() returns text[] language sql as $$
  select array['g1@example.com', 'Alpha Guardian', 'Alpha Kid', 'Alpha LLC', 'Alpha household', 'Alpha family', '1 Alpha St',
    '37064', 'Franklin', '+1615', '12-3456789', 'SECRETTOKEN', '4242', 'FPRINT', 'exp_month', 'exp_year', '2345-6789',
    'hosted_invoice_url', 'invoice_pdf', 'receipt_url', 'receipt_number', 'receipt_email', 'payment_method_details',
    'billing_details', 'customer_details', 'collected_information', 'shipping_details', 'customer_shipping', 'metadata',
    'custom_fields', 'description', 'success_url', 'idem-', '/v1/invoices', 'Prep & Price',
    '20000000-0000-0000-0000-0000000000a1', current_setting('t.ha')]
$$;
create function dr_test.has_pii(p jsonb) returns text language sql as $$
  select string_agg(s, ', ') from unnest(dr_test.billing_pii()) s where position(s in p::text) > 0
$$;
-- Every personal, retained and security table that still holds anything of household A (ids, names, emails, address).
create function dr_test.residue() returns text language plpgsql as $$
declare t text; v text; out text; needles text[] := array[current_setting('t.ha'), current_setting('t.s1'), current_setting('t.s2'),
  '20000000-0000-0000-0000-0000000000a1', '20000000-0000-0000-0000-000000000051', 'g1@example.com', 'Alpha Guardian',
  'Alpha Kid', 'Alpha Home', '1 Alpha St', 'secret-a1', 'secret-51'];
begin
  for t in select tbl from dr_decisions where decision in ('personal', 'retained', 'security') order by tbl loop
    execute format('select string_agg(n, %L) from unnest($1) n where exists (select 1 from %s x where position(n in x::text) > 0)', '|', t)
      into v using needles;
    if v is not null then out := coalesce(out || '; ', '') || t || ': ' || v; end if;
  end loop;
  return out;
end $$;

do $$
declare ha uuid; hb uuid; s1 uuid; s2 uuid; s3 uuid; si uuid; c text;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  ha := public.create_household('Alpha Home', 'America/Chicago');
  s1 := public.add_student(ha, 'Alpha Kid One');
  s2 := public.add_student(ha, 'Alpha Kid Two');
  perform set_config('t.s4', public.add_student(ha, 'Moved Kid')::text, true);
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
  perform set_config('t.ha', ha::text, true); perform set_config('t.hb', hb::text, true);
  perform set_config('t.s1', s1::text, true); perform set_config('t.s2', s2::text, true);
  perform set_config('t.s3', s3::text, true); perform set_config('t.si', si::text, true);

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
  -- S4 practised in A (goals, scores, reminder changes and alerts set by g1, with A as the household), then moved to B.
  perform dr_test.seed_student(current_setting('t.s4')::uuid, '20000000-0000-0000-0000-0000000000a1', 'moved');
  update public.students set household_id = hb where id = current_setting('t.s4')::uuid;
  insert into public.household_saved_schools(household_id, institution_key, added_by) values
   (ha, 'dr-school', '20000000-0000-0000-0000-0000000000a1'), (hb, 'dr-school', '20000000-0000-0000-0000-0000000000b1');
  -- A: a Stripe subscription, a complimentary one, and g1's personal (no-household) past subscription. B: one live.
  insert into public.subscriptions(owner_user_id, household_id, plan_key, status, provider, provider_customer_id, provider_subscription_id) values
   ('20000000-0000-0000-0000-0000000000a1', ha, 'family_annual', 'active', 'stripe', 'cus_ALPHA', 'sub_ALPHA'),
   ('20000000-0000-0000-0000-0000000000a1', ha, 'family', 'active', 'comp', null, null),
   ('20000000-0000-0000-0000-0000000000a1', null, 'family_monthly', 'canceled', 'stripe', 'cus_PERSONAL', 'sub_PERSONAL'),
   ('20000000-0000-0000-0000-0000000000b1', hb, 'family_annual', 'active', 'stripe', 'cus_BRAVO', 'sub_BRAVO');
  insert into public.billing_customers(household_id, provider, provider_customer_id, created_by) values
   (ha, 'stripe', 'cus_ALPHA', '20000000-0000-0000-0000-0000000000a1'), (hb, 'stripe', 'cus_BRAVO', '20000000-0000-0000-0000-0000000000b1');
  insert into public.billing_events(provider, event_id, event_type, household_id, provider_subscription_id, payload) values
   ('stripe', 'evt_A1', 'invoice.paid', ha, 'sub_ALPHA', dr_test.invoice_paid('evt_A1', 'cus_ALPHA', 'sub_ALPHA', ha)),
   ('stripe', 'evt_A2', 'customer.subscription.updated', null, 'sub_ALPHA', '{"id":"evt_A2","data":{"object":{"id":"sub_ALPHA","customer":"cus_ALPHA"}}}'),
   ('stripe', 'evt_A3', 'charge.succeeded', null, null, dr_test.charge_succeeded('evt_A3', 'cus_ALPHA')),
   ('stripe', 'evt_A4', 'checkout.session.completed', ha, 'sub_ALPHA', dr_test.checkout_completed('evt_A4', 'cus_ALPHA', 'sub_ALPHA', ha)),
   ('stripe', 'evt_P1', 'invoice.paid', null, 'sub_PERSONAL', dr_test.invoice_paid('evt_P1', 'cus_PERSONAL', 'sub_PERSONAL', ha)),
   ('stripe', 'evt_B1', 'invoice.paid', hb, 'sub_BRAVO', '{"id":"evt_B1","data":{"object":{"customer":"cus_BRAVO","customer_email":"gb@example.com","amount_paid":4900}}}');
  -- Parent emails (CR-22/27). Inactivity keys are '<student id>:<last practice>'; g1 and g2 each had alerts for S1
  -- and S2 at the same moment, so the rewritten keys must stay unique. g2 also had one about B's S3, a digest that
  -- covers B too, and a digest from 14 months ago (purged).
  insert into public.parent_email_deliveries(user_id, kind, period_key, sent_at) values
   ('20000000-0000-0000-0000-0000000000a1', 'weekly_digest', '2026-10-26', now()),
   ('20000000-0000-0000-0000-0000000000a1', 'inactivity', public.inactivity_period_key(s1, '2026-10-01T00:00:00Z'), now()),
   ('20000000-0000-0000-0000-0000000000a1', 'inactivity', public.inactivity_period_key(s2, '2026-10-01T00:00:00Z'), now()),
   ('20000000-0000-0000-0000-0000000000a2', 'inactivity', public.inactivity_period_key(s1, '2026-10-01T00:00:00Z'), now()),
   ('20000000-0000-0000-0000-0000000000a2', 'inactivity', public.inactivity_period_key(s2, '2026-10-01T00:00:00Z'), now()),
   ('20000000-0000-0000-0000-0000000000a2', 'inactivity', public.inactivity_period_key(s3, null), now()),
   ('20000000-0000-0000-0000-0000000000a2', 'weekly_digest', '2026-10-26', now()),
   ('20000000-0000-0000-0000-0000000000a2', 'weekly_digest', '2025-08-25', now() - interval '14 months'),
   ('20000000-0000-0000-0000-0000000000b1', 'weekly_digest', '2026-10-26', now()),
   ('20000000-0000-0000-0000-0000000000a1', 'reminders_off', (select c.id::text from public.practice_reminder_changes c where c.student_id = s1), now());
  -- Home state (CR-15).
  update public.households set home_state = case when id = ha then 'TN' else 'NY' end where id in (ha, hb);
  update public.students set home_state = case when household_id = ha then 'TN' else 'NY' end where household_id in (ha, hb);
  -- Question reports (CR-25): S1's own (open), g1's on S1 (closed, reviewed), and g1's two on B's S3 (one closed):
  -- S3 stays when A is deleted, so those two keep no reporter and no note. gb's on S3 is untouched.
  insert into public.question_reports(question_id, content_hash, question_pool, attempt_id, student_id, reporter_user_id,
    reporter_role, reason, note, status, reviewed_at, reviewed_by, resolution_note) values
   ('30000000-0000-0000-0000-000000000001', repeat('a', 64), 'practice', (select a.id from public.practice_attempts a where a.student_id = s1),
    s1, '20000000-0000-0000-0000-000000000051', 'student', 'typo', 'S1 own note', 'open', null, null, null),
   ('30000000-0000-0000-0000-000000000001', repeat('b', 64), 'practice', null, s1, '20000000-0000-0000-0000-0000000000a1',
    'guardian', 'unclear', 'Alpha Guardian One thinks this is unclear', 'resolved', now(), 'Editor Ed', 'Key is B because of the sign'),
   ('30000000-0000-0000-0000-000000000001', repeat('c', 64), 'practice', null, s3, '20000000-0000-0000-0000-0000000000a1',
    'guardian', 'wrong_key', 'Alpha Guardian One on the Bravo question', 'resolved', now(), 'Editor Ed', 'Key is B because of the sign'),
   ('30000000-0000-0000-0000-000000000003', repeat('d', 64), 'practice', null, s3, '20000000-0000-0000-0000-0000000000a1',
    'guardian', 'other', 'Alpha Guardian open note', 'open', null, null, null),
   ('30000000-0000-0000-0000-000000000001', repeat('e', 64), 'assessment', null, s3, '20000000-0000-0000-0000-0000000000b1',
    'guardian', 'typo', 'Bravo guardian note', 'open', null, null, null);
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 3. Nobody but service_role reaches the entry points, and nobody reaches the internals or writes the request tables.
-- ---------------------------------------------------------------------------------------------------------------
do $$
declare u text; f text; v_internal text[]; v_entry text[];
begin
  v_entry := array[
    format('select public.admin_export_student(%L, %L, ''x'', ''op'')', current_setting('t.s1'), current_setting('t.ha')),
    format('select public.admin_export_household(%L, ''x'', ''op'')', current_setting('t.ha')),
    format('select public.admin_delete_student(%L, ''r'', %L, ''x'')', current_setting('t.s1'), current_setting('t.ha')),
    format('select public.admin_delete_household(%L, ''r'', ''x'')', current_setting('t.ha')),
    'select public.admin_record_auth_deletion(gen_random_uuid())',
    'select public.admin_rescrub_billing_events(gen_random_uuid())',
    'select public.admin_purge_expired_retention()',
    'select public.record_billing_event(''stripe'', ''evt_x'', ''x'', null, ''{}'', true)',
    'select public.deidentify_billing_event(''stripe'', ''evt_x'')'];
  v_internal := array[
    format('select public.data_request_student_tables(%L, true)', current_setting('t.s1')),
    format('select public.data_request_household_tables(%L)', current_setting('t.ha')),
    format('select public.data_request_household_billing(%L, ''{}'')', current_setting('t.ha')),
    format('select public.data_request_delete_student_internal(%L, true, null)', current_setting('t.s1')),
    format('select public.data_request_delete_household_internal(%L, true, null)', current_setting('t.ha')),
    'select public.data_request_scrub_billing_payload(''{}'')',
    'insert into public.data_request_log(action, subject_kind, subject_id, requested_by, channel, requested_at, operator, performed_by) values (''export'', ''student'', gen_random_uuid(), ''x'', ''email'', now(), ''x'', ''x'')',
    'insert into public.retained_email_records(kind, recipient_email, send_count, last_sent_at, retain_until) values (''household_invitation'', ''a@b.c'', 1, now(), now())',
    'insert into public.data_request_billing_refs(request_id, provider, kind, ref) values (gen_random_uuid(), ''stripe'', ''customer'', ''cus_x'')',
    'update public.data_request_log set operator = ''x''', 'delete from public.data_request_log'];
  foreach u in array array['anon', '20000000-0000-0000-0000-0000000000a1', '20000000-0000-0000-0000-000000000051'] loop
    if u = 'anon' then perform hp_test.as_anon(); else perform hp_test.as_user(u::uuid); end if;
    foreach f in array v_entry || v_internal || array['select * from public.data_request_log',
      'select * from public.retained_email_records', 'select * from public.data_request_billing_refs'] loop
      perform hp_test.expect_error(f, '42501');
    end loop;
  end loop;
  perform set_config('role', 'service_role', true);
  foreach f in array v_internal loop
    perform hp_test.expect_error(f, '42501');
  end loop;
  perform count(*) from public.data_request_log;  -- service_role may read
  perform hp_test.as_owner();
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 4. Exports: complete, no other household's rows, no other person's ids in a student export, no secrets or keys.
-- ---------------------------------------------------------------------------------------------------------------
set local role service_role;
create temp table dr_exports as
select 'household_a'::text k, public.admin_export_household(current_setting('t.ha')::uuid, 'g1@example.com', 'ops@example.com') doc
union all select 'household_b', public.admin_export_household(current_setting('t.hb')::uuid, 'gb@example.com', 'ops@example.com')
union all select 's1', public.admin_export_student(current_setting('t.s1')::uuid, current_setting('t.ha')::uuid, 'g1@example.com', 'ops@example.com')
union all select 'indy', public.admin_export_student(current_setting('t.si')::uuid, null, 'indy@example.com', 'ops@example.com');
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
  select string_agg(x, ', ') into v_bad from jsonb_object_keys(a->'tables') x
  where 'public.' || x not in (select tbl from dr_decisions where decision in ('personal', 'retained'));
  perform hp_test.check(v_bad is null, 'export keys are decided tables: ' || coalesce(v_bad, ''));
  -- Column by column: every 'export' column is in every row of its table, every 'omit' column in none, in the
  -- household and the student exports alike.
  for e in select k, doc from dr_exports loop
    select string_agg(distinct k.tbl || '.' || k.col || ' (' || k.decision || ')', ', ') into v_bad
    from dr_columns k cross join jsonb_array_elements(coalesce(e.doc->'tables'->split_part(k.tbl, '.', 2), '[]')) r
    where (k.decision = 'export' and e.k like 'household%' and not r ? k.col) or (k.decision = 'omit' and r ? k.col);
    perform hp_test.check(v_bad is null, e.k || ' export columns: ' || coalesce(v_bad, ''));
  end loop;
  perform hp_test.eq(jsonb_array_length(a->'tables'->'parent_email_deliveries'), 6, 'A parent emails: g1 digest, four alerts on A students, reminders-off');
  perform hp_test.eq(jsonb_array_length(b->'tables'->'parent_email_deliveries'), 2, 'B parent emails: gb digest, g2 alert on S3 (not g2''s digest)');
  perform hp_test.check(a->'tables'->'students'->0 ? 'id' and a->'tables'->'student_planning_preferences'->0->>'exam_intent' = 'sat'
    and a->'tables'->'alert_preferences'->0->>'weekly_digest' = 'true', 'new #298 columns exported');
  -- #295: home state, seen-before, question reports, and the derived first-answer metrics.
  perform hp_test.check(a->'tables'->'households'->0->>'home_state' = 'TN' and a->'tables'->'students'->0->>'home_state' = 'TN'
    and a->'tables'->'practice_session_items'->0 ? 'seen_before' and a->'tables'->'practice_session_items'->0 ? 'last_seen', '#295 columns exported');
  perform hp_test.eq(jsonb_array_length(a->'tables'->'question_reports'), 2, 'A reports: S1 own and g1 on S1');
  perform hp_test.check((select bool_and(r->>'note' is not null and r->>'reporter_user_id' is not null) from jsonb_array_elements(a->'tables'->'question_reports') r),
    'household export shows its own members'' reports in full');
  perform hp_test.eq((select array_agg(coalesce(r->>'note', '(none)') order by r->>'created_at', r->>'id') from jsonb_array_elements(s1->'tables'->'question_reports') r)
    @> array['S1 own note', '(none)'], true, 'student export: own note shown, guardian''s note not');
  perform hp_test.check((select bool_and((r->>'reporter_user_id' is null) = (r->>'note' is null)) from jsonb_array_elements(s1->'tables'->'question_reports') r),
    'student export hides the guardian reporter with the note');
  perform hp_test.eq(jsonb_array_length(b->'tables'->'question_reports'), 3, 'B reports on S3');
  -- The student who moved from A to B: B's export shows their history without A's household id or A's people.
  perform hp_test.check((select bool_and(r->>'household_id' is null and r->>'changed_by' is null) from jsonb_array_elements(b->'tables'->'practice_reminder_changes') r
      where r->>'student_id' = current_setting('t.s4'))
    and (select bool_and(r->>'set_by' is null) from jsonb_array_elements(b->'tables'->'weekly_practice_goals') r where r->>'student_id' = current_setting('t.s4'))
    and (select bool_and(r->>'entered_by' is null) from jsonb_array_elements(b->'tables'->'student_test_scores') r where r->>'student_id' = current_setting('t.s4'))
    and (select bool_and(r->>'requested_by' is null) from jsonb_array_elements(b->'tables'->'ai_help_requests') r where r->>'student_id' = current_setting('t.s4'))
    and (select bool_and(r->>'user_id' is null) from jsonb_array_elements(b->'tables'->'alert_preferences') r where r->>'student_id' = current_setting('t.s4'))
    and (select bool_and(r->>'updated_by' is null) from jsonb_array_elements(b->'tables'->'practice_reminder_settings') r where r->>'student_id' = current_setting('t.s4')),
    'moved student: A''s household and people masked in B''s export');
  perform hp_test.check((select bool_and(r->>'household_id' = current_setting('t.hb') and r->>'changed_by' = '20000000-0000-0000-0000-0000000000b1')
      from jsonb_array_elements(b->'tables'->'practice_reminder_changes') r where r->>'student_id' = current_setting('t.s3')),
    'B''s own student keeps B''s ids');
  perform hp_test.eq((select count(*) from jsonb_array_elements(b->'tables'->'question_reports') r where r->>'reporter_user_id' is null and r->>'note' is null), 2::bigint,
    'B export: g1 (not a B member) shown without id or note');
  perform hp_test.check(jsonb_array_length(a->'derived'->'skill_estimates') > 0 and jsonb_array_length(s1->'derived'->'skill_estimates') > 0
    and (select bool_and(z ? 'first_answers' and z ? 'first_answer_accuracy' and z ? 'student_id') from jsonb_array_elements(a->'derived'->'skill_estimates') z),
    'derived skill estimates with first-answer metrics exported');
  perform hp_test.eq(jsonb_array_length(a->'tables'->'students'), 2, 'A has two students');
  perform hp_test.eq(jsonb_array_length(a->'tables'->'practice_attempts'), 2, 'A attempts from both students');
  perform hp_test.eq(jsonb_array_length(a->'tables'->'practice_session_items'), 4, 'A session items');
  perform hp_test.eq(jsonb_array_length(a->'tables'->'household_members'), 3, 'A members: g1, g2, S1 login');
  perform hp_test.eq(jsonb_array_length(a->'tables'->'household_invitations'), 4, 'A invitations');
  perform hp_test.eq(jsonb_array_length(a->'tables'->'subscriptions'), 3, 'A subscriptions: Stripe, comp, g1 personal');
  -- Billing events: linked to A, to A's or g1's personal subscription, or naming A's customer (the charge).
  perform hp_test.eq((select array_agg(x->>'event_type' order by x->>'event_type') from jsonb_array_elements(a->'tables'->'billing_events') x),
    array['charge.succeeded', 'checkout.session.completed', 'customer.subscription.updated', 'invoice.paid', 'invoice.paid'], 'A billing events (summary)');
  perform hp_test.eq(jsonb_array_length(b->'tables'->'billing_events'), 1, 'B billing event');

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
      'Question 1', 'First hint', 'cus_ALPHA', 'cus_BRAVO', 'cus_PERSONAL', 'sub_ALPHA', 'sub_BRAVO', 'sub_PERSONAL',
      'payload', '1 Alpha St', 'customer_email', 'evt_', 'secret-', 'p256-', 'push.example', '60000000-0000-0000-0000-0000000000', 'Editor Ed', 'Key is B', 'assessment'] loop
      perform hp_test.check(position(secret in e.doc::text) = 0, e.k || ' export contains ' || secret);
    end loop;
    foreach secret in array (select array_agg(code_hash) || array_agg(short_code_hash) filter (where short_code_hash is not null)
      from public.household_invitations) loop
      perform hp_test.check(position(secret in e.doc::text) = 0, e.k || ' export contains an invitation digest');
    end loop;
  end loop;
  -- Exports are logged, with counts only, the operator and the role they ran as.
  perform hp_test.eq((select count(*) from public.data_request_log where action = 'export'), 4::bigint, 'four export rows');
  perform hp_test.eq((select (exported->>'practice_attempts')::int from public.data_request_log
    where action = 'export' and subject_id = current_setting('t.ha')::uuid), 2, 'export row counts');
  perform hp_test.check((select requested_by = 'g1@example.com' and operator = 'ops@example.com'
    and performed_by like 'jwt_role=%; session_user=%' from public.data_request_log where subject_id = current_setting('t.ha')::uuid),
    'export requester, operator, role');
end $$;

-- performed_by reads the API's JWT claims (request.jwt.claims), then the older single claim, with the session user.
do $$
begin
  perform set_config('request.jwt.claims', '{"role":"service_role","sub":""}', true);
  perform hp_test.eq(public.data_request_performed_by(), 'jwt_role=service_role; session_user=' || session_user, 'role from request.jwt.claims');
  perform set_config('request.jwt.claims', '', true);
  perform set_config('request.jwt.claim.role', 'service_role', true);
  perform hp_test.eq(public.data_request_performed_by(), 'jwt_role=service_role; session_user=' || session_user, 'role from the older claim');
  perform set_config('request.jwt.claim.role', '', true);
  perform hp_test.eq(public.data_request_performed_by(), 'jwt_role=(none); session_user=' || session_user, 'SQL editor / psql');
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 5. Safeguards: scope, dry run by default, explicit confirmation and operator for a live run, live subscriptions.
-- A dry run must leave every personal, retained, security and request table byte-for-byte unchanged.
-- ---------------------------------------------------------------------------------------------------------------
create temp table dr_snapshot(tbl text primary key, digest text);
create function dr_test.snapshot() returns void language plpgsql as $$
declare t text; d text;
begin
  delete from dr_snapshot;
  for t in select tbl from dr_decisions where decision <> 'reference' loop
    execute format('select md5(coalesce(string_agg(x::text, %L order by x::text), %L)) from %s x', E'\n', '', t) into d;
    insert into dr_snapshot values (t, d);
  end loop;
end $$;
create function dr_test.unchanged(p_msg text) returns void language plpgsql as $$
declare t text; d text; want text;
begin
  for t, want in select tbl, s.digest from dr_snapshot s loop
    execute format('select md5(coalesce(string_agg(x::text, %L order by x::text), %L)) from %s x', E'\n', '', t) into d;
    perform hp_test.eq(d, want, p_msg || ': ' || t);
  end loop;
end $$;
grant all on dr_snapshot to service_role;
grant execute on all functions in schema dr_test to service_role;

do $$
declare r jsonb; ha uuid := current_setting('t.ha'); hb uuid := current_setting('t.hb'); s1 uuid := current_setting('t.s1');
  s3 uuid := current_setting('t.s3'); si uuid := current_setting('t.si'); st text;
begin
  perform set_config('role', 'service_role', true);
  -- A student of another household (or none) is refused, for export and delete.
  perform hp_test.expect_error(format('select public.admin_export_student(%L, %L, ''g1@example.com'', ''ops'')', s3, ha), '42501', '%not in household%');
  perform hp_test.expect_error(format('select public.admin_delete_student(%L, ''request'', %L, ''g1@example.com'')', s3, ha), '42501', '%not in household%');
  perform hp_test.expect_error(format('select public.admin_delete_student(%L, ''request'', %L, ''g1@example.com'')', si, ha), '42501');
  perform hp_test.expect_error(format('select public.admin_delete_student(%L, ''request'', null, ''g1@example.com'')', s1), '42501');
  -- Requester, reason and operator are required.
  perform hp_test.expect_error(format('select public.admin_delete_household(%L, ''request'', '' '')', ha), '22023');
  perform hp_test.expect_error(format('select public.admin_delete_household(%L, null, ''g1@example.com'')', ha), '22023');
  perform hp_test.expect_error(format('select public.admin_export_household(%L, ''g1@example.com'', null)', ha), '22023', '%p_operator%');
  perform hp_test.expect_error(format('select public.admin_export_student(%L, %L, ''g1@example.com'', '' '')', s1, ha), '22023', '%p_operator%');
  -- A live run needs p_dry_run => false, p_confirm => the same id, and p_operator.
  perform hp_test.expect_error(format('select public.admin_delete_household(%L, ''request'', ''g1@example.com'', p_dry_run => false)', ha), '22023', '%p_confirm%');
  perform hp_test.expect_error(format('select public.admin_delete_household(%L, ''request'', ''g1@example.com'', p_dry_run => false, p_confirm => %L, p_operator => ''ops'')', ha, hb), '22023', '%p_confirm%');
  perform hp_test.expect_error(format('select public.admin_delete_household(%L, ''request'', ''g1@example.com'', p_dry_run => false, p_confirm => %L)', ha, ha), '22023', '%p_operator%');
  perform hp_test.expect_error(format('select public.admin_delete_student(%L, ''request'', %L, ''g1@example.com'', p_dry_run => false, p_confirm => %L, p_operator => ''ops'')', s1, ha, ha), '22023');
  perform hp_test.expect_error(format('select public.admin_delete_student(%L, ''request'', %L, ''g1@example.com'', p_dry_run => false, p_confirm => %L)', s1, ha, s1), '22023', '%p_operator%');
  perform hp_test.expect_error(format('select public.admin_delete_household(%L, ''request'', ''g1@example.com'', p_dry_run => null)', ha), '22023');
  -- Every billing or access status of a paid subscription refuses, even in a dry run; a comp subscription does not.
  perform set_config('role', 'none', true);
  foreach st in array array['trialing', 'active', 'past_due', 'unpaid', 'paused', 'incomplete', 'grace', 'billing_retry'] loop
    update public.subscriptions set status = st where provider_subscription_id = 'sub_ALPHA';
    perform set_config('role', 'service_role', true);
    perform hp_test.expect_error(format('select public.admin_delete_household(%L, ''request'', ''g1@example.com'')', ha), '55000', '%cancel%');
    perform set_config('role', 'none', true);
  end loop;
  update public.subscriptions set status = 'canceled' where provider_subscription_id = 'sub_ALPHA';
  -- g1's personal subscription live again: refused too (g1's account would be deleted).
  update public.subscriptions set status = 'active' where provider_subscription_id = 'sub_PERSONAL';
  perform set_config('role', 'service_role', true);
  perform hp_test.expect_error(format('select public.admin_delete_household(%L, ''request'', ''g1@example.com'')', ha), '55000', '%member account%');
  perform set_config('role', 'none', true);
  update public.subscriptions set status = 'canceled' where provider_subscription_id = 'sub_PERSONAL';
  perform hp_test.check(exists (select 1 from public.subscriptions where household_id = ha and provider = 'comp' and status = 'active'), 'comp still active');

  perform dr_test.snapshot();
  -- A dry run (the default) reports, changes no row's content, and writes no log row.
  perform set_config('role', 'service_role', true);
  r := public.admin_delete_household(ha, 'request', 'g1@example.com');
  perform set_config('role', 'none', true);
  perform hp_test.check((r->>'dry_run')::boolean, 'dry run is the default');
  perform hp_test.eq((r->'removed'->>'practice_attempts')::int, 2, 'dry run counts attempts');
  perform hp_test.eq((r->'removed'->>'students')::int, 2, 'dry run counts students');
  perform hp_test.eq((r->'kept'->>'billing_events')::int, 5, 'dry run counts kept billing events');
  perform hp_test.check(r->'auth_users_to_delete' @> '["20000000-0000-0000-0000-0000000000a1","20000000-0000-0000-0000-000000000051"]'
    and not r->'auth_users_to_delete' @> '["20000000-0000-0000-0000-0000000000a2"]', 'dry run auth list ' || (r->'auth_users_to_delete')::text);
  perform set_config('role', 'service_role', true);
  r := public.admin_delete_student(s1, 'request', ha, 'g1@example.com', p_dry_run => true);
  r := public.admin_delete_student(si, 'request', null, 'indy@example.com');
  perform set_config('role', 'none', true);
  perform dr_test.unchanged('dry runs change nothing');
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 6. Delete one guardian-managed student (S2): their rows go, the household and sibling stay, email record kept.
-- ---------------------------------------------------------------------------------------------------------------
do $$
declare r jsonb; ha uuid := current_setting('t.ha'); s1 uuid := current_setting('t.s1'); s2 uuid := current_setting('t.s2'); l public.data_request_log;
begin
  perform set_config('role', 'service_role', true);
  r := public.admin_delete_student(s2, 'Parent asked by email to delete one student profile', ha, 'g1@example.com',
    p_dry_run => false, p_confirm => s2, p_operator => 'ops@example.com', p_requested_at => now() - interval '2 days');
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
  perform hp_test.eq(l.operator, 'ops@example.com', 'audit operator');
  perform hp_test.check(l.performed_by like 'jwt_role=%; session_user=%', 'audit role and session');
  perform hp_test.check(l.reason like 'Parent asked%', 'audit reason');
  perform hp_test.check(l.requested_at < l.performed_at - interval '1 day', 'audit keeps when it was requested');
  perform hp_test.eq((l.removed->>'practice_attempts')::int, 1, 'audit removed attempts');
  perform hp_test.eq((l.removed->>'practice_attempt_events')::int, 2, 'audit removed events');
  perform hp_test.eq((l.kept->>'retained_email_records')::int, 1, 'audit kept email record');
  perform hp_test.check(position('Alpha Kid Two' in to_jsonb(l)::text) = 0, 'audit row holds no name');
  perform hp_test.check((select data_request_id from public.retained_email_records where recipient_email = 'alpha.kid.two@example.com') = l.id, 'retained row points at the request');
  -- Parent emails about S2: kept, still the guardians', but the key no longer holds S2's id.
  perform hp_test.eq((l.kept->>'parent_email_deliveries')::int, 2, 'two alerts about S2 de-identified');
  perform hp_test.check(not exists (select 1 from public.parent_email_deliveries where position(s2::text in period_key) > 0), 'no key holds S2');
  perform hp_test.eq((select count(*) from public.parent_email_deliveries where kind = 'inactivity' and period_key like 'deleted-%:2026-10-01T00:00:00.000000Z'
    and user_id in ('20000000-0000-0000-0000-0000000000a1', '20000000-0000-0000-0000-0000000000a2')), 2::bigint, 'keys rewritten, recipients kept');
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 7. Delete household A: everything personal goes, B and g2's B membership stay, billing kept de-identified with
-- exactly the events the export listed.
-- ---------------------------------------------------------------------------------------------------------------
do $$
declare r jsonb; x jsonb; ha uuid := current_setting('t.ha'); s1 uuid := current_setting('t.s1'); t text; l public.data_request_log;
  e record; o jsonb;
begin
  perform set_config('role', 'service_role', true);
  x := public.admin_export_household(ha, 'g1@example.com', 'ops@example.com');
  r := public.admin_delete_household(ha, 'Account holder asked by email to delete the household', 'g1@example.com',
    p_dry_run => false, p_confirm => ha, p_operator => 'ops@example.com');
  perform set_config('role', 'none', true);
  perform set_config('t.req_a', r->>'request_id', true);
  -- Removed counts match what the export held, table by table (g2's profile stays: g2 is still in household B).
  for t in select split_part(tbl, '.', 2) from dr_decisions where decision = 'personal' loop
    perform hp_test.eq(coalesce((r->'removed'->>t)::int, 0), jsonb_array_length(x->'tables'->t) - case when t = 'profiles' then 1 else 0 end,
      'removed matches export for ' || t);
  end loop;
  -- Export and delete cover the same payment events.
  perform hp_test.eq((select array_agg((v->>'id')::bigint order by (v->>'id')::bigint) from jsonb_array_elements(x->'tables'->'billing_events') v),
    (select array_agg(v::bigint order by v::bigint) from jsonb_array_elements_text(r->'kept'->'billing_event_ids') v), 'export and delete event ids');
  perform hp_test.eq((select array_agg(event_id order by event_id) from public.billing_events
    where id in (select v::bigint from jsonb_array_elements_text(r->'kept'->'billing_event_ids') v)),
    array['evt_A1', 'evt_A2', 'evt_A3', 'evt_A4', 'evt_P1'], 'kept events: household, subscription, customer, personal');
  perform hp_test.check(not exists (select 1 from public.households where id = ha), 'household deleted');
  perform hp_test.check(not exists (select 1 from public.students where id = s1), 'S1 deleted');
  perform hp_test.check(not exists (select 1 from public.household_members where household_id = ha), 'memberships deleted');
  perform hp_test.check(not exists (select 1 from public.subscriptions where owner_user_id = '20000000-0000-0000-0000-0000000000a1'), 'subscription state deleted (Stripe, comp, personal)');
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
  -- Billing records kept, de-identified: no household link and no personal value left, in any of the payloads.
  for e in select event_id, household_id, deidentified_at, payload from public.billing_events
           where event_id in ('evt_A1', 'evt_A2', 'evt_A3', 'evt_A4', 'evt_P1') loop
    perform hp_test.check(e.household_id is null and e.deidentified_at is not null, e.event_id || ' unlinked and marked');
    perform hp_test.check(dr_test.has_pii(e.payload) is null, e.event_id || ' still holds ' || coalesce(dr_test.has_pii(e.payload), ''));
  end loop;
  -- What is kept, exactly: invoice.paid.
  select payload->'data'->'object' into o from public.billing_events where event_id = 'evt_A1';
  perform hp_test.eq((select array_agg(k order by k) from jsonb_object_keys(o) k),
    array['amount_due', 'amount_paid', 'amount_remaining', 'attempt_count', 'attempted', 'billing_reason', 'collection_method',
      'created', 'currency', 'customer', 'id', 'lines', 'number', 'object', 'parent', 'period_end', 'period_start', 'status',
      'status_transitions', 'subtotal', 'tax', 'total', 'total_tax_amounts'], 'invoice keys kept');
  perform hp_test.eq(o->>'amount_paid', '4900', 'amount kept'); perform hp_test.eq(o->>'tax', '300', 'tax kept');
  perform hp_test.eq(o->>'number', 'PP-0001', 'invoice number kept'); perform hp_test.eq(o->>'customer', 'cus_ALPHA', 'customer ref kept');
  perform hp_test.eq(o->'total_tax_amounts'->0, '{"amount": 300, "inclusive": false, "tax_rate": "txr_1"}'::jsonb, 'tax lines kept');
  perform hp_test.eq(o->'lines'->'data'->0, '{"id": "il_1", "amount": 4600, "object": "line_item", "period": {"end": 1790000000, "start": 1787000000}, "pricing": {"type": "price_details", "price_details": {"price": "price_1", "product": "prod_1"}, "unit_amount_decimal": "4600"}, "currency": "usd", "quantity": 1}'::jsonb, 'line kept without description or metadata');
  perform hp_test.eq(o->'parent', '{"type": "subscription_details", "subscription_details": {"subscription": "sub_ALPHA"}}'::jsonb, 'parent kept without metadata');
  perform hp_test.eq((select payload - 'data' from public.billing_events where event_id = 'evt_A1'),
    '{"id": "evt_A1", "type": "invoice.paid", "object": "event", "created": 1790000000, "request": {"id": null}, "livemode": true, "api_version": "2025-03-31.basil", "pending_webhooks": 1}'::jsonb, 'event envelope kept');
  -- checkout.session.completed.
  select payload->'data'->'object' into o from public.billing_events where event_id = 'evt_A4';
  perform hp_test.eq(o, '{"id": "cs_evt_A4", "url": null, "mode": "subscription", "object": "checkout.session", "status": "complete", "created": 1789990000, "invoice": "in_1", "currency": "usd", "customer": "cus_ALPHA", "expires_at": 1790076400, "amount_total": 4900, "subscription": "sub_ALPHA", "total_details": {"amount_tax": 300, "amount_discount": 0, "amount_shipping": 0}, "payment_status": "paid", "amount_subtotal": 4600}'::jsonb - 'url', 'checkout kept exactly');
  -- charge.succeeded: no card or billing details.
  select payload->'data'->'object' into o from public.billing_events where event_id = 'evt_A3';
  perform hp_test.eq(o, '{"id": "ch_evt_A3", "paid": true, "amount": 4900, "object": "charge", "status": "succeeded", "created": 1790000050, "invoice": "in_1", "currency": "usd", "customer": "cus_ALPHA"}'::jsonb, 'charge kept exactly');
  perform hp_test.eq((select payload->'data'->'object'->>'customer_email' from public.billing_events where event_id = 'evt_B1'), 'gb@example.com', 'B billing untouched');
  perform hp_test.eq((select household_id from public.billing_events where event_id = 'evt_B1'), current_setting('t.hb')::uuid, 'B billing linked');
  -- Email-sent records: the 14-month-old one is past its 13 months and not kept.
  perform hp_test.eq((select count(*) from public.retained_email_records where recipient_email = 'old.guardian@example.com'), 0::bigint, 'expired email record not kept');
  -- The audit row and the provider references.
  select * into l from public.data_request_log where id = (r->>'request_id')::uuid;
  perform hp_test.eq(l.subject_kind, 'household', 'household audit kind');
  perform hp_test.eq((l.kept->>'billing_events')::int, 5, 'audit kept billing events');
  perform hp_test.eq(l.kept->'billing_refs', '{"customers": ["cus_ALPHA", "cus_PERSONAL"], "subscriptions": ["sub_ALPHA", "sub_PERSONAL"]}'::jsonb, 'audit billing refs');
  perform hp_test.eq((select array_agg(kind || ':' || ref order by kind, ref) from public.data_request_billing_refs where request_id = l.id),
    array['customer:cus_ALPHA', 'customer:cus_PERSONAL', 'subscription:sub_ALPHA', 'subscription:sub_PERSONAL'], 'refs stored for late events');
  perform hp_test.eq(l.auth_users_to_delete, array['20000000-0000-0000-0000-000000000051', '20000000-0000-0000-0000-0000000000a1']::uuid[], 'audit auth list');
  perform hp_test.check(l.auth_users_deleted_at is null, 'auth deletion not yet recorded');
  perform hp_test.check(position('Alpha' in to_jsonb(l)::text) = 0, 'audit row holds no names');
  -- Parent emails: g1's records kept without g1; alerts about S1 keep their recipient (g2) but not S1's id; g2's two
  -- alerts with the same moment for S1 and S2 stay distinct; B's records untouched.
  perform hp_test.eq((l.kept->>'parent_email_deliveries')::int, 5, 'five parent emails de-identified');
  perform hp_test.check(not exists (select 1 from public.parent_email_deliveries where user_id = '20000000-0000-0000-0000-0000000000a1'), 'g1 records unlinked');
  perform hp_test.eq((select count(*) from public.parent_email_deliveries where user_id is null), 4::bigint, 'g1 four records kept unlinked');
  perform hp_test.check(not exists (select 1 from public.parent_email_deliveries
    where position(s1::text in period_key) > 0 or position(current_setting('t.s2') in period_key) > 0), 'no key holds S1 or S2');
  perform hp_test.eq((select count(distinct period_key) from public.parent_email_deliveries where user_id = '20000000-0000-0000-0000-0000000000a2'
    and kind = 'inactivity' and period_key like 'deleted-%:2026-10-01T00:00:00.000000Z'), 2::bigint, 'g2 keeps two distinct de-identified alerts');
  perform hp_test.check(exists (select 1 from public.parent_email_deliveries where user_id = '20000000-0000-0000-0000-0000000000a2'
    and period_key = current_setting('t.s3') || ':never'), 'g2 alert on S3 untouched');
  perform hp_test.check(exists (select 1 from public.parent_email_deliveries where user_id = '20000000-0000-0000-0000-0000000000b1'), 'gb record untouched');
  -- Question reports: S1's went with S1; g1's two on S3 stay for the editors without reporter or note, the closed one
  -- through the guard's data-request exemption; reason, revision, review and status unchanged; gb's untouched.
  perform hp_test.eq((r->'removed'->>'question_reports')::int, 2, 'S1 reports removed');
  perform hp_test.eq((l.kept->>'question_reports')::int, 2, 'g1 reports on S3 de-identified');
  perform hp_test.eq((select array_agg(status || '/' || reason || '/' || revision || '/' || coalesce(reviewed_by, '-') order by content_hash)
    from public.question_reports where reporter_user_id is null and note is null), array['resolved/wrong_key/1/Editor Ed', 'open/other/1/-'], 'kept reports');
  perform hp_test.check(exists (select 1 from public.question_reports where note = 'Bravo guardian note'
    and reporter_user_id = '20000000-0000-0000-0000-0000000000b1'), 'gb report untouched');
  perform hp_test.eq(coalesce(current_setting('collegeprep.data_request_deidentify', true), ''), '', 'exemption not left on');
  -- The guard still holds outside the exemption, and the exemption allows only clearing the note.
  perform hp_test.expect_error($q$update public.question_reports set note = 'x' where status = 'resolved'$q$, '22023', '%closed%');
  perform set_config('collegeprep.data_request_deidentify', 'on', true);
  perform hp_test.expect_error($q$update public.question_reports set reason = 'typo' where status = 'resolved'$q$, '22023', '%closed%');
  perform hp_test.expect_error($q$update public.question_reports set note = 'x' where status = 'resolved'$q$, '22023', '%closed%');
  perform set_config('collegeprep.data_request_deidentify', '', true);
  -- Devices: g1's and S1's login's push devices deleted; g2's kept.
  perform hp_test.eq((r->'removed'->>'notification_devices')::int, 2, 'two devices removed');
  -- Device claims made by or on g1 and S1's login (S1's claim on gb's device, gb's claim on g1's device, g1's claim on
  -- gb's device) and their failed confirmations (g1's from the household path, S1's login's from the student path) go
  -- with them; g2's claim on gb's device and gb's and I's failures stay.
  perform hp_test.eq((r->'removed'->>'notification_device_claims')::int, 3, 'three device claims removed');
  perform hp_test.eq((r->'removed'->>'notification_device_claim_failures')::int, 2, 'two failed confirmations removed');
  perform hp_test.check(not exists (select 1 from public.notification_device_claims where claimant_user_id = '20000000-0000-0000-0000-0000000000a1'),
    'the household path deleted g1''s claim on a device outside the household');
  perform hp_test.check(not exists (select 1 from public.notification_device_claim_failures where user_id = '20000000-0000-0000-0000-000000000051'),
    'the student path deleted S1''s login''s failed confirmation');
  perform hp_test.eq((select array_agg(claimant_user_id::text || '>' || target_device_id::text) from public.notification_device_claims),
    array['20000000-0000-0000-0000-0000000000a2>60000000-0000-0000-0000-0000000000b1'], 'claims left');
  perform hp_test.eq((select array_agg(user_id order by user_id) from public.notification_device_claim_failures),
    array['20000000-0000-0000-0000-000000000052', '20000000-0000-0000-0000-0000000000b1']::uuid[], 'failures left');
  perform hp_test.eq((select array_agg(user_id order by user_id) from public.notification_devices),
    array['20000000-0000-0000-0000-000000000052', '20000000-0000-0000-0000-0000000000a2', '20000000-0000-0000-0000-0000000000b1']::uuid[], 'devices left');
  -- The runbook's next step, straight away: the listed accounts are deleted through the admin API (here: the stub's
  -- auth.users), which also clears what other households' rows still say about them (e.g. the moved student's
  -- set_by). Then nothing of A is left anywhere.
  delete from auth.users where id in ('20000000-0000-0000-0000-0000000000a1', '20000000-0000-0000-0000-000000000051');
  perform set_config('role', 'service_role', true);
  perform public.admin_record_auth_deletion((r->>'request_id')::uuid);
  perform set_config('role', 'none', true);
  perform hp_test.check(dr_test.residue() is null, 'nothing of A left: ' || coalesce(dr_test.residue(), ''));
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 8. Late webhooks: events about a deleted household arrive de-identified; an unknown household's event is
-- de-identified by the webhook's second call; anything stored raw is caught by the re-scrub after the retry window.
-- ---------------------------------------------------------------------------------------------------------------
do $$
declare v bigint; req uuid := current_setting('t.req_a');
begin
  perform set_config('role', 'service_role', true);
  -- Stripe retries an invoice for the deleted subscription; a customer.updated names the deleted customer only.
  v := public.record_billing_event('stripe', 'evt_L1', 'invoice.paid', 'sub_ALPHA',
    dr_test.invoice_paid('evt_L1', 'cus_ALPHA', 'sub_ALPHA', current_setting('t.ha')::uuid), true);
  perform hp_test.check(v is not null, 'late event recorded');
  perform hp_test.check(public.record_billing_event('stripe', 'evt_L1', 'invoice.paid', 'sub_ALPHA', '{}', true) is null, 'duplicate event returns null');
  v := public.record_billing_event('stripe', 'evt_L2', 'customer.updated', null,
    '{"id":"evt_L2","type":"customer.updated","data":{"object":{"id":"cus_ALPHA","object":"customer","email":"g1@example.com","name":"Alpha Guardian One"},"previous_attributes":{"email":"old@example.com"}}}', true);
  -- B's events and never-seen customers are stored as sent.
  v := public.record_billing_event('stripe', 'evt_B2', 'invoice.paid', 'sub_BRAVO', '{"data":{"object":{"customer":"cus_BRAVO","customer_email":"gb@example.com"}}}', true);
  -- An event type the webhook does not act on (a dispute names the cardholder, not the customer or subscription):
  -- the webhook passes p_store_raw false, so it is stored de-identified even for a live household.
  v := public.record_billing_event('stripe', 'evt_D1', 'charge.dispute.created', null,
    '{"id":"evt_D1","type":"charge.dispute.created","data":{"object":{"id":"dp_1","object":"dispute","amount":4900,"currency":"usd","charge":"ch_9","status":"needs_response","evidence":{"customer_name":"Bravo Guardian","customer_email_address":"gb@example.com","billing_address":"9 Bravo Rd"}}}}', false);
  perform hp_test.expect_error($q$select public.record_billing_event('stripe', 'evt_D2', 'x', null, '{}', null)$q$, '22023');
  v := public.record_billing_event('stripe', 'evt_U1', 'invoice.paid', 'sub_UNKNOWN',
    dr_test.invoice_paid('evt_U1', 'cus_UNKNOWN', 'sub_UNKNOWN', gen_random_uuid()), true);
  perform hp_test.check(public.deidentify_billing_event('stripe', 'evt_U1'), 'webhook de-identifies an unknown household event');
  perform hp_test.check(not public.deidentify_billing_event('stripe', 'evt_missing'), 'no such event');
  perform set_config('role', 'none', true);
  perform hp_test.check((select deidentified_at is not null and household_id is null and dr_test.has_pii(payload) is null
    from public.billing_events where event_id = 'evt_L1'), 'late invoice stored de-identified');
  perform hp_test.check((select deidentified_at is not null and position('g1@example.com' in payload::text) = 0
    and position('old@example.com' in payload::text) = 0 and payload->'data'->'object'->>'id' = 'cus_ALPHA'
    from public.billing_events where event_id = 'evt_L2'), 'late customer event stored de-identified');
  perform hp_test.check((select deidentified_at is null and position('gb@example.com' in payload::text) > 0
    from public.billing_events where event_id = 'evt_B2'), 'B event stored as sent');
  perform hp_test.check((select deidentified_at is not null and payload->'data'->'object' = '{"id": "dp_1", "amount": 4900, "charge": "ch_9", "object": "dispute", "status": "needs_response", "currency": "usd"}'::jsonb
    from public.billing_events where event_id = 'evt_D1'), 'unhandled event type stored de-identified');
  perform hp_test.check((select deidentified_at is not null and dr_test.has_pii(payload) is null
    from public.billing_events where event_id = 'evt_U1'), 'unknown household event de-identified');
  -- Late events through the webhook restore nothing of A, before any re-scrub, and recreate no account rows.
  perform hp_test.check(dr_test.residue() is null, 'late webhook events restore nothing: ' || coalesce(dr_test.residue(), ''));
  perform hp_test.check(not exists (select 1 from public.subscriptions where provider_subscription_id = 'sub_ALPHA')
    and not exists (select 1 from public.billing_customers where provider_customer_id = 'cus_ALPHA'), 'no billing rows recreated');
  -- A raw copy stored by an older webhook (or before the refs existed): the re-scrub catches it, once.
  insert into public.billing_events(provider, event_id, event_type, household_id, provider_subscription_id, payload) values
   ('stripe', 'evt_L3', 'invoice.payment_failed', current_setting('t.ha')::uuid, null,
    dr_test.invoice_paid('evt_L3', 'cus_ALPHA', 'sub_ALPHA', current_setting('t.ha')::uuid)),
   ('stripe', 'evt_L4', 'charge.refunded', null, null, dr_test.charge_succeeded('evt_L4', 'cus_PERSONAL'));
  perform set_config('role', 'service_role', true);
  perform set_config('role', 'none', true);
  perform hp_test.eq(dr_test.residue(), 'public.billing_events: ' || current_setting('t.ha') || '|20000000-0000-0000-0000-0000000000a1|g1@example.com|Alpha Guardian|Alpha Kid|1 Alpha St',
    'a raw late event is the only residue before the re-scrub');
  perform set_config('role', 'service_role', true);
  perform hp_test.eq(public.admin_rescrub_billing_events(req), 2, 're-scrub fixes the two raw late events');
  perform hp_test.eq(public.admin_rescrub_billing_events(req), 0, 're-scrub is idempotent');
  perform hp_test.expect_error(format('select public.admin_rescrub_billing_events(%L)', gen_random_uuid()), 'P0002');
  perform set_config('role', 'none', true);
  perform hp_test.check((select bool_and(household_id is null and dr_test.has_pii(payload) is null) from public.billing_events
    where event_id in ('evt_L3', 'evt_L4')), 're-scrubbed events clean');
  perform hp_test.check((select billing_rescrubbed_at is not null from public.data_request_log where id = req), 're-scrub recorded');
  perform hp_test.check((select position('gb@example.com' in payload::text) > 0 from public.billing_events where event_id = 'evt_B1'), 'B untouched by re-scrub');
  perform hp_test.check(dr_test.residue() is null, 'nothing of A after the re-scrub: ' || coalesce(dr_test.residue(), ''));
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- 9. Independent student (no household): their login is listed; recording the auth deletion waits for the admin API.
-- ---------------------------------------------------------------------------------------------------------------
do $$
declare r jsonb; si uuid := current_setting('t.si'); rec jsonb;
begin
  perform set_config('role', 'service_role', true);
  r := public.admin_delete_student(si, 'Student (18+) asked by email', null, 'indy@example.com', p_dry_run => false,
    p_confirm => si, p_operator => 'ops@example.com');
  perform set_config('role', 'none', true);
  perform hp_test.eq(r->'auth_users_to_delete', '["20000000-0000-0000-0000-000000000052"]'::jsonb, 'independent login listed');
  perform hp_test.check(not exists (select 1 from public.profiles where id = '20000000-0000-0000-0000-000000000052'), 'independent profile deleted');
  perform hp_test.check(not exists (select 1 from public.notification_devices where user_id = '20000000-0000-0000-0000-000000000052'), 'independent device deleted');
  perform hp_test.eq((r->'removed'->>'notification_device_claim_failures')::int, 1, 'the independent login''s failed confirmation counted');
  perform hp_test.check(not exists (select 1 from public.notification_device_claim_failures where user_id = '20000000-0000-0000-0000-000000000052'),
    'and deleted by the student path');
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
-- 10. After every deletion, each personal table holds exactly household B's rows: nothing of A or I is left.
-- ---------------------------------------------------------------------------------------------------------------
do $$
declare b jsonb; t text; n bigint;
begin
  perform set_config('role', 'service_role', true);
  b := public.admin_export_household(current_setting('t.hb')::uuid, 'gb@example.com', 'ops@example.com');
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
  perform hp_test.eq(public.admin_purge_expired_retention(), '{"retained_email_records": 1, "parent_email_deliveries": 1}'::jsonb,
    'purge removes the expired invitation record and g2''s 14-month-old digest record');
  perform hp_test.eq(public.admin_purge_expired_retention(), '{"retained_email_records": 0, "parent_email_deliveries": 0}'::jsonb, 'purge is idempotent');
  perform set_config('role', 'none', true);
  perform hp_test.eq((select count(*) from public.retained_email_records), 1::bigint, 'current email record stays');
  perform hp_test.check(not exists (select 1 from public.parent_email_deliveries where sent_at <= now() - interval '13 months'), 'no parent email older than 13 months');
  perform hp_test.eq((select count(*) from public.parent_email_deliveries), 9::bigint, 'current parent email records stay');
  perform hp_test.eq((select count(*) from public.notification_devices), 2::bigint, 'only g2 and gb devices remain');
  perform hp_test.eq((select count(*) from public.notification_device_claims), 1::bigint, 'only g2''s device claim remains');
  perform hp_test.eq((select count(*) from public.notification_device_claim_failures), 1::bigint, 'only gb''s failed confirmation remains');
  perform hp_test.eq((select count(*) from public.data_request_log where action = 'export'), 6::bigint, 'six exports logged');
  perform hp_test.eq((select count(*) from public.data_request_log where action = 'delete'), 3::bigint, 'three live deletions logged, no dry runs');
end $$;

rollback;
