-- Household accounts, permission flags, student account flows and subscriptions. Everything is rolled back.
-- Run with psql -v ON_ERROR_STOP=1; any failed assertion raises an exception.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql

-- g1 = 20..a1 (household A creator), g2 = 20..a2, gb = 20..b1, s1/s2/s3 = 20..51/52/53, x = 20..99.
do $$
declare t text;
begin
  perform hp_test.as_anon();
  foreach t in array array['profiles','households','household_members','students','household_invitations',
    'subscriptions','app_settings','exam_families','exam_versions','question_types','skills','trap_types',
    'question_strategies','practice_questions','practice_question_skills','practice_question_distractors',
    'practice_question_strategies','weekly_practice_goals','practice_sessions','practice_session_items',
    'practice_attempts','practice_attempt_events','ai_help_requests','alert_preferences','student_test_scores',
    'student_official_scores'] loop
    perform hp_test.check(not has_any_column_privilege('public.' || t, 'SELECT,INSERT,UPDATE'), 'anon has privilege on ' || t);
    perform hp_test.check(not has_table_privilege('public.' || t, 'DELETE'), 'anon can delete ' || t);
  end loop;
  perform hp_test.expect_error('select public.create_household(''x'')', '42501');
  perform hp_test.expect_error('select public.create_self_student_profile(''x'')', '42501');
  perform hp_test.expect_error('select public.can_view_student(gen_random_uuid())', '42501');
  perform hp_test.expect_error('select public.household_entitlements(gen_random_uuid())', '42501');
  perform hp_test.as_user('00000000-0000-0000-0000-000000000000');
  perform set_config('request.jwt.claim.sub', '', true);
  perform hp_test.expect_error('select public.create_household(''No user'')', '42501', 'Authentication required');
  -- Internal helpers are not callable by clients at all.
  perform hp_test.expect_error('select public.detach_member(gen_random_uuid(), gen_random_uuid())', '42501');
  perform hp_test.expect_error('select * from public.skill_estimates_internal(gen_random_uuid())', '42501');
end $$;

-- Guardian g1 creates household A with every permission; invites g2 with set_goals only.
do $$
declare hh uuid; st1 uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.expect_error('select public.create_household(''Bad tz'', ''Mars/Olympus'')', '22023');
  hh := public.create_household('Household A', 'America/Chicago');
  st1 := public.add_student(hh, 'Student One', 2028, 10);
  perform set_config('t.hh_a', hh::text, true);
  perform set_config('t.st1', st1::text, true);
  perform hp_test.check((select can_manage_students and can_set_goals and can_view_progress and can_manage_members and can_manage_billing
    from public.household_members where user_id = auth.uid()), 'creator holds every permission');
  perform set_config('t.inv_g2', public.create_household_invitation(hh, 'guardian', null, 72, array['set_goals']), true);
  perform set_config('t.inv_s1', public.create_household_invitation(hh, 'student', st1), true);
  perform set_config('t.inv_open', public.create_household_invitation(hh, 'student'), true);
  perform set_config('t.inv_open2', public.create_household_invitation(hh, 'student'), true);
  perform set_config('t.inv_exp', public.create_household_invitation(hh, 'guardian'), true);
  perform hp_test.check(current_setting('t.inv_g2') ~ '^[0-9a-f]{64}$', 'invitation code format');
  perform hp_test.expect_error('select code_hash from public.household_invitations', '42501');
  perform hp_test.expect_error(format('select public.create_household_invitation(%L, ''guardian'', null, 337)', hh), '22023');
  perform hp_test.expect_error(format('select public.create_household_invitation(%L, ''guardian'', null, 72, array[''own_everything''])', hh), '22023');
  perform hp_test.expect_error(format('select public.create_household_invitation(%L, ''student'', null, 72, array[''set_goals''])', hh), '22023');
  -- Clients cannot write memberships, students or permission flags directly.
  perform hp_test.expect_error(format('insert into public.household_members(household_id, user_id, role) values (%L, %L, ''guardian'')',
    hh, '20000000-0000-0000-0000-000000000099'), '42501');
  perform hp_test.expect_error(format('insert into public.students(household_id, display_name) values (%L, ''x'')', hh), '42501');
  perform hp_test.expect_error('update public.household_members set can_manage_billing = true', '42501');
  perform hp_test.expect_error('update public.students set linked_user_id = auth.uid()', '42501');
  perform hp_test.expect_error('update public.students set household_id = null', '42501');
  perform hp_test.as_owner();
end $$;

-- Invitations are single-use and expiry-checked; the guardian invitation carries its flags.
update public.household_invitations set expires_at = now() - interval '1 second'
where code_hash = encode(sha256(convert_to(current_setting('t.inv_exp'), 'UTF8')), 'hex');
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error('select public.accept_household_invitation(current_setting(''t.inv_exp''))', '22023', '%expired%');
  perform hp_test.expect_error('select public.accept_household_invitation(''not-a-code'')', '22023', '%Invalid%');
  perform hp_test.expect_error('select public.accept_household_invitation(current_setting(''t.inv_open''))', '22023', '%Create your student profile%');
  perform hp_test.eq((select count(*) from public.households), 0::bigint, 'outsider sees no households');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq(public.accept_household_invitation(current_setting('t.inv_g2')), current_setting('t.hh_a')::uuid, 'g2 joins A');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error('select public.accept_household_invitation(current_setting(''t.inv_g2''))', '22023', '%already been used%');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv_s1'));
  perform hp_test.check((select linked_user_id = auth.uid() and account_mode = 'student_login' and household_id = current_setting('t.hh_a')::uuid
    from public.students where id = current_setting('t.st1')::uuid), 'guardian-created profile claimed by student');
  perform hp_test.expect_error('select public.accept_household_invitation(current_setting(''t.inv_s1''))', '22023', '%already been used%');
  perform hp_test.as_owner();
  -- The claimed invitation is persisted with its 72-hour lifetime and who accepted it; claiming adds no profile.
  perform hp_test.check((select abs(extract(epoch from (expires_at - created_at)) - 72 * 3600) < 5
      and accepted_by = '20000000-0000-0000-0000-000000000051' and accepted_at is not null
    from public.household_invitations where code_hash = encode(sha256(convert_to(current_setting('t.inv_s1'), 'UTF8')), 'hex')),
    'student invitation persisted: 72h lifetime, accepted_at/accepted_by set');
  perform hp_test.eq((select count(*) from public.students where household_id = current_setting('t.hh_a')::uuid
      and linked_user_id = '20000000-0000-0000-0000-000000000051'), 1::bigint, 'claim links one profile, no duplicate');
  perform hp_test.check((select not can_manage_students and can_set_goals and not can_view_progress and not can_manage_members and not can_manage_billing
    from public.household_members where user_id = '20000000-0000-0000-0000-0000000000a2'), 'g2 flags from invitation');
end $$;

-- Student s1 practises once so progress-gated data exists.
do $$
declare a uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  a := public.start_practice_attempt(current_setting('t.st1')::uuid, '30000000-0000-0000-0000-000000000001');
  perform public.submit_practice_attempt(a, 'B');
  perform hp_test.as_owner();
end $$;

-- g2 (set_goals only): sees the roster, sets goals, but cannot manage students or view progress.
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq((select count(*) from public.students), 1::bigint, 'g2 sees roster');
  perform hp_test.expect_error('select public.add_student(current_setting(''t.hh_a'')::uuid, ''Nope'')', '42501', '%manage-students%');
  update public.students set display_name = 'Renamed by g2';
  perform hp_test.expect_error('select public.student_weekly_progress(current_setting(''t.st1'')::uuid, ''2026-09-07'')', '42501');
  perform hp_test.expect_error('select * from public.student_skill_estimates(current_setting(''t.st1'')::uuid)', '42501');
  perform hp_test.eq((select count(*) from public.practice_attempts), 0::bigint, 'g2 cannot read attempts');
  perform hp_test.expect_error('select public.create_household_invitation(current_setting(''t.hh_a'')::uuid, ''guardian'')', '42501');
  perform hp_test.expect_error('select public.create_household_invitation(current_setting(''t.hh_a'')::uuid, ''student'')', '42501');
  perform hp_test.expect_error(format('select public.update_member_permissions(%L, %L, p_view_progress => true)',
    current_setting('t.hh_a'), auth.uid()), '42501');
  insert into public.weekly_practice_goals(student_id, week_start, target_questions) values (current_setting('t.st1')::uuid, '2026-09-07', 10);
  perform hp_test.eq((select count(*) from public.weekly_practice_goals), 1::bigint, 'g2 reads goals it may set');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((select display_name from public.students where id = current_setting('t.st1')::uuid), 'Student One', 'g2 edited student');
  perform hp_test.eq((select count(*) from public.practice_attempts), 1::bigint, 'g1 reads attempts');
  perform hp_test.as_owner();
end $$;

-- Last-manager protection.
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.expect_error('select public.leave_household(current_setting(''t.hh_a'')::uuid)', '42501', '%at least one member%');
  perform hp_test.expect_error(format('select public.update_member_permissions(%L, %L, p_manage_members => false)',
    current_setting('t.hh_a'), auth.uid()), '42501', '%at least one member%');
  perform hp_test.expect_error(format('select public.update_member_permissions(%L, %L, p_view_progress => true)',
    current_setting('t.hh_a'), '20000000-0000-0000-0000-000000000051'), '22023', '%No guardian%');
  perform public.update_member_permissions(current_setting('t.hh_a')::uuid, '20000000-0000-0000-0000-0000000000a2', p_manage_members => true);
  perform public.update_member_permissions(current_setting('t.hh_a')::uuid, auth.uid(), p_manage_members => false);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.expect_error(format('select public.remove_household_member(%L, %L)', current_setting('t.hh_a'), auth.uid()), '42501', '%at least one member%');
  perform hp_test.expect_error('select public.leave_household(current_setting(''t.hh_a'')::uuid)', '42501', '%at least one member%');
  perform public.update_member_permissions(current_setting('t.hh_a')::uuid, '20000000-0000-0000-0000-0000000000a1', p_manage_members => true);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.update_member_permissions(current_setting('t.hh_a')::uuid, '20000000-0000-0000-0000-0000000000a2', p_manage_members => false);
  perform hp_test.as_owner();
end $$;

-- Subscriptions: provider webhooks write as service_role; owner and billing-flag members read; members see entitlements.
set local role service_role;
insert into public.subscriptions(owner_user_id, household_id, plan_key, status, provider, provider_customer_id, provider_subscription_id, current_period_end)
values ('20000000-0000-0000-0000-0000000000a1', current_setting('t.hh_a')::uuid, 'family_plus', 'active', 'stripe', 'cus_test', 'sub_test', '2026-11-01Z'),
       ('20000000-0000-0000-0000-0000000000b1', null, 'solo', 'trialing', 'stripe', 'cus_b', 'sub_b', null);
reset role;
do $$
declare e record;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((select count(*) from public.subscriptions), 1::bigint, 'owner reads own subscription only');
  perform hp_test.expect_error('select provider_customer_id from public.subscriptions', '42501');
  perform hp_test.expect_error('select provider_subscription_id from public.subscriptions', '42501');
  perform hp_test.expect_error($q$insert into public.subscriptions(owner_user_id, plan_key, status) values (auth.uid(), 'free_upgrade', 'active')$q$, '42501');
  perform hp_test.expect_error($q$update public.subscriptions set status = 'active'$q$, '42501');
  perform hp_test.expect_error('delete from public.subscriptions', '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq((select count(*) from public.subscriptions), 0::bigint, 'member without billing flag cannot read subscription');
  select * into e from public.household_entitlements(current_setting('t.hh_a')::uuid);
  perform hp_test.check(e.plan_key = 'family_plus' and e.status = 'active' and e.current_period_end = '2026-11-01Z', 'member reads entitlements');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select count(*) from public.household_entitlements(current_setting('t.hh_a')::uuid)), 1::bigint, 'student member reads entitlements');
  perform hp_test.eq((select count(*) from public.subscriptions), 0::bigint, 'student cannot read subscription');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error('select * from public.household_entitlements(current_setting(''t.hh_a'')::uuid)', '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.update_member_permissions(current_setting('t.hh_a')::uuid, '20000000-0000-0000-0000-0000000000a2', p_manage_billing => true);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq((select plan_key from public.subscriptions), 'family_plus', 'billing-flag member reads subscription');
  perform hp_test.as_owner();
end $$;

-- Self-created student profile joins a household, gets guardian visibility, then leaves with its history.
do $$
declare st2 uuid; a uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  st2 := public.create_self_student_profile('Student Two', 2029, 11);
  perform set_config('t.st2', st2::text, true);
  perform hp_test.expect_error('select public.create_self_student_profile(''Second'')', '22023', '%already linked%');
  perform hp_test.check((select household_id is null and not is_independent and account_mode = 'student_login'
    from public.students where id = st2), 'self profile has no household');
  update public.students set grade_level = 12 where id = st2;
  insert into public.weekly_practice_goals(student_id, week_start, target_minutes) values (st2, '2026-09-07', 30);
  a := public.start_practice_attempt(st2, '30000000-0000-0000-0000-000000000003');
  perform public.submit_practice_attempt(a, 'C');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((select count(*) from public.students where id = st2), 0::bigint, 'guardian cannot see unjoined profile');
  perform hp_test.expect_error(format('select public.create_household_invitation(%L, ''student'', %L)', current_setting('t.hh_a'), st2), '22023');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.accept_household_invitation(current_setting('t.inv_open'));
  perform hp_test.check((select household_id = current_setting('t.hh_a')::uuid and grade_level = 12 from public.students where id = st2), 'profile moved into household');
  perform hp_test.expect_error('select public.accept_household_invitation(current_setting(''t.inv_open2''))', '22023', '%already a member%');
  -- Inside a household a non-independent student no longer edits their own profile or goals.
  update public.students set grade_level = 9 where id = st2;
  perform hp_test.expect_error(format($q$insert into public.weekly_practice_goals(student_id, week_start, target_minutes) values (%L, '2026-09-14', 5)$q$, st2), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((select grade_level from public.students where id = st2), 12, 'student edited profile while managed');
  perform hp_test.eq((select count(*) from public.practice_attempts where student_id = st2), 1::bigint, 'guardian sees joined student history');
  perform hp_test.eq((public.student_weekly_progress(st2, '2026-09-28')->>'student_id')::uuid, st2, 'guardian reads joined student progress');
  insert into public.alert_preferences(student_id, channel) values (st2, 'email');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.leave_household(current_setting('t.hh_a')::uuid);
  perform hp_test.check((select household_id is null from public.students where id = st2), 'profile left with student');
  perform hp_test.eq((select count(*) from public.practice_attempts), 1::bigint, 'history stays with student');
  perform hp_test.eq((select count(*) from public.weekly_practice_goals), 1::bigint, 'goals stay with student');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((select count(*) from public.students where id = st2), 0::bigint, 'guardian loses roster access');
  perform hp_test.eq((select count(*) from public.practice_attempts where student_id = st2), 0::bigint, 'guardian loses attempt access');
  perform hp_test.eq((select count(*) from public.weekly_practice_goals where student_id = st2), 0::bigint, 'guardian loses goal access');
  perform hp_test.expect_error(format('select public.student_weekly_progress(%L, ''2026-09-07'')', st2), '42501');
  perform hp_test.as_owner();
  perform hp_test.eq((select count(*) from public.alert_preferences where student_id = st2), 0::bigint, 'guardian alert preferences removed on leave');
end $$;

-- Independent adult student: no guardian can target, edit or pull the profile; only the student's own acceptance moves it.
do $$
declare st3 uuid; hb uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  st3 := public.create_self_student_profile('Adult Learner', null, 13, true, 'America/New_York');
  perform set_config('t.st3', st3::text, true);
  insert into public.weekly_practice_goals(student_id, week_start, target_questions) values (st3, '2026-09-07', 20);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  hb := public.create_household('Household B');
  perform set_config('t.hh_b', hb::text, true);
  perform hp_test.expect_error(format('select public.create_household_invitation(%L, ''student'', %L)', hb, st3), '22023', '%unlinked student of this household%');
  perform hp_test.expect_error(format('update public.students set household_id = %L where id = %L', hb, st3), '42501');
  update public.students set display_name = 'Taken over' where id = st3;
  perform hp_test.expect_error(format('select public.add_student(%L, ''Intruder'')', current_setting('t.hh_a')), '42501');
  perform hp_test.expect_error(format('select public.create_household_invitation(%L, ''guardian'')', current_setting('t.hh_a')), '42501');
  perform hp_test.expect_error(format('select public.student_weekly_progress(%L, ''2026-09-07'')', current_setting('t.st1')), '42501');
  perform hp_test.eq((select count(*) from public.students), 0::bigint, 'guardian B sees no students');
  perform hp_test.eq((select count(*) from public.weekly_practice_goals), 0::bigint, 'guardian B sees no goals');
  perform set_config('t.inv_b', public.create_household_invitation(hb, 'student'), true);
  perform hp_test.as_owner();
  perform hp_test.check((select household_id is null and display_name = 'Adult Learner' from public.students where id = st3), 'guardian changed independent student');
  -- The student consents by accepting; independence is kept and the student still sets their own goals.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform public.accept_household_invitation(current_setting('t.inv_b'));
  perform hp_test.check((select household_id = hb and is_independent from public.students where id = st3), 'independent student joined by consent');
  update public.weekly_practice_goals set target_questions = 25 where student_id = st3;
  perform hp_test.eq((select target_questions from public.weekly_practice_goals where student_id = st3), 25, 'independent student sets own goal');
  perform hp_test.as_owner();
end $$;

-- Removing a student member detaches their claimed profile; removing a guardian revokes their access.
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.remove_household_member(current_setting('t.hh_a')::uuid, '20000000-0000-0000-0000-0000000000a2');
  perform hp_test.expect_error(format('select public.remove_household_member(%L, %L)', current_setting('t.hh_a'), '20000000-0000-0000-0000-000000000099'), '22023');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq((select count(*) from public.households), 0::bigint, 'removed guardian loses household');
  perform hp_test.eq((select count(*) from public.students), 0::bigint, 'removed guardian loses roster');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.remove_household_member(current_setting('t.hh_a')::uuid, '20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select count(*) from public.students), 0::bigint, 'removed student profile leaves household');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select count(*) from public.practice_attempts), 1::bigint, 'removed student keeps history');
  perform hp_test.eq((select count(*) from public.profiles), 0::bigint, 'no profile yet');
  insert into public.profiles(id, display_name) values (auth.uid(), 'Sam');
  perform hp_test.expect_error($q$insert into public.profiles(id) values ('20000000-0000-0000-0000-000000000052')$q$, '42501');
  perform hp_test.as_owner();
end $$;

-- Deleting the creating guardian's account keeps the household (created_by set null) and removes the membership.
do $$
declare st uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  st := public.add_student(current_setting('t.hh_a')::uuid, 'Student Four');
  perform hp_test.as_owner();
  delete from auth.users where id = '20000000-0000-0000-0000-0000000000a1';
  perform hp_test.check((select h.created_by is null from public.households h join public.students s on s.household_id = h.id where s.id = st),
    'household survives creator account deletion');
  perform hp_test.check(not exists (select 1 from public.household_members where user_id = '20000000-0000-0000-0000-0000000000a1'), 'deleted account membership removed');
end $$;
\o
\echo household_access: all assertions passed
rollback;
