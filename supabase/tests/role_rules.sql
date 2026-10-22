-- Role rules (issue #218 C1, C6, C7): every check here fails if an unauthorised write or read succeeds.
-- Rolled back. Run with psql -v ON_ERROR_STOP=1 after the migrations.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql

-- a1: creator (every flag). a2: view_progress only. c1: set_goals only. c2: manage_students only.
-- c3: manage_members only. 51: the linked student. 99: outsider.
insert into auth.users(id) values ('20000000-0000-0000-0000-0000000000c1'), ('20000000-0000-0000-0000-0000000000c2'),
  ('20000000-0000-0000-0000-0000000000c3');
insert into public.sources(id, canonical_url, authority) values ('50000000-0000-0000-0000-000000000101', 'https://example.edu/roles', 'institution');
insert into public.institutions(institution_key, ipeds_name, display_name, state_code, source_id, verification_status, identity_academic_year)
select 'roles-' || n, 'R', 'R', 'TN', '50000000-0000-0000-0000-000000000101', 'verified', '2023-24' from generate_series(1, 6) n;
insert into public.exam_catalog values ('ap:roles-a', 'ap', 'Roles A'), ('ap:roles-b', 'ap', 'Roles B'),
  ('ap:roles-c', 'ap', 'Roles C'), ('ap:roles-d', 'ap', 'Roles D');

do $$
declare hh uuid; st uuid; inv_a2 text; inv_c1 text; inv_c2 text; inv_c3 text; inv_s text;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Roles', 'America/Chicago');
  st := public.add_student(hh, 'Planner');
  perform set_config('t.hh', hh::text, true);
  perform set_config('t.st', st::text, true);
  inv_s := public.create_household_invitation(hh, 'student', st);
  inv_a2 := public.create_household_invitation(hh, 'guardian', null, 72, array['view_progress']);
  inv_c1 := public.create_household_invitation(hh, 'guardian', null, 72, array['set_goals']);
  inv_c2 := public.create_household_invitation(hh, 'guardian', null, 72, array['manage_students']);
  inv_c3 := public.create_household_invitation(hh, 'guardian', null, 72, array['manage_members']);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051'); perform public.accept_household_invitation(inv_s);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2'); perform public.accept_household_invitation(inv_a2);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1'); perform public.accept_household_invitation(inv_c1);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c2'); perform public.accept_household_invitation(inv_c2);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c3'); perform public.accept_household_invitation(inv_c3);
  perform hp_test.as_owner();
end $$;

-- C1: exam plan and academic interests.
do $$
declare st text := current_setting('t.st');
begin
  -- Allowed writers.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  insert into public.student_exam_plan(student_id, exam_key) values (st::uuid, 'ap:roles-a');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  insert into public.student_exam_plan(student_id, exam_key) values (st::uuid, 'ap:roles-b');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  insert into public.student_exam_plan(student_id, exam_key) values (st::uuid, 'ap:roles-c');
  update public.student_exam_plan set score = 4 where student_id = st::uuid and exam_key = 'ap:roles-b';

  -- View-only, manage-students-only and manage-members-only guardians can't insert, update or delete.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.eq((select count(*) from public.student_exam_plan), 3::bigint, 'view-only guardian reads the plan');
  perform hp_test.expect_error(format($q$insert into public.student_exam_plan(student_id, exam_key) values (%L, 'ap:roles-d')$q$, st), '42501');
  update public.student_exam_plan set score = 1 where student_id = st::uuid;
  delete from public.student_exam_plan where student_id = st::uuid;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c2');
  perform hp_test.expect_error(format($q$insert into public.student_exam_plan(student_id, exam_key) values (%L, 'ap:roles-d')$q$, st), '42501');
  update public.student_exam_plan set score = 1 where student_id = st::uuid;
  delete from public.student_exam_plan where student_id = st::uuid;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c3');
  perform hp_test.expect_error(format($q$insert into public.student_exam_plan(student_id, exam_key) values (%L, 'ap:roles-d')$q$, st), '42501');
  delete from public.student_exam_plan where student_id = st::uuid;
  perform hp_test.as_owner();
  perform hp_test.eq((select count(*) from public.student_exam_plan where student_id = st::uuid), 3::bigint, 'no guardian without set_goals deleted an exam');
  perform hp_test.eq((select score from public.student_exam_plan where exam_key = 'ap:roles-b'), 4, 'no guardian without set_goals changed a score');
  perform hp_test.eq((select count(*) from public.student_exam_plan where score = 1), 0::bigint, 'no score set to 1');

  -- Interests: the same rule.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.expect_error(format($q$insert into public.student_academic_interests(student_id, certainty, interests) values (%L, 'few', '[]')$q$, st), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  insert into public.student_academic_interests(student_id, certainty, interests) values (st::uuid, 'few', '[{"kind":"major","key":"biology"}]');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  update public.student_academic_interests set certainty = 'sure', interests = '[]' where student_id = st::uuid;
  delete from public.student_academic_interests where student_id = st::uuid;
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c2');
  update public.student_academic_interests set certainty = 'sure' where student_id = st::uuid;
  perform hp_test.as_owner();
  perform hp_test.check((select certainty = 'few' and interests = '[{"kind":"major","key":"biology"}]'::jsonb
    from public.student_academic_interests where student_id = st::uuid), 'interests unchanged by guardians without set_goals');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  update public.student_academic_interests set certainty = 'sure' where student_id = st::uuid;
  perform hp_test.as_owner();
  perform hp_test.eq((select certainty from public.student_academic_interests where student_id = st::uuid), 'sure', 'the student edits their interests');
end $$;

-- C6: saved-school removal.
do $$
declare hh text := current_setting('t.hh');
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform public.save_household_school(hh::uuid, 'roles-1');
  perform public.save_household_school(hh::uuid, 'roles-2');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.save_household_school(hh::uuid, 'roles-3');   -- saving stays open to members
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform public.save_household_school(hh::uuid, 'roles-4');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c3');
  perform public.save_household_school(hh::uuid, 'roles-5');

  -- Refused: removing a school someone else saved, without manage_students or set_goals.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.expect_error(format('select public.remove_household_school(%L, %L)', hh, 'roles-1'), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.expect_error(format('select public.remove_household_school(%L, %L)', hh, 'roles-1'), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c3');
  perform hp_test.expect_error(format('select public.remove_household_school(%L, %L)', hh, 'roles-3'), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error(format('select public.remove_household_school(%L, %L)', hh, 'roles-5'), '42501');
  perform hp_test.as_owner();
  perform hp_test.eq((select count(*) from public.household_saved_schools where household_id = hh::uuid), 5::bigint, 'nothing removed without the right');

  -- Allowed: the member who saved it; a guardian with set_goals; a guardian with manage_students.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform public.remove_household_school(hh::uuid, 'roles-4');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.remove_household_school(hh::uuid, 'roles-3');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform public.remove_household_school(hh::uuid, 'roles-1');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c2');
  perform public.remove_household_school(hh::uuid, 'roles-5');
  perform hp_test.as_owner();
  perform hp_test.eq((select string_agg(institution_key, ',') from public.household_saved_schools where household_id = hh::uuid), 'roles-2', 'allowed removals applied');
end $$;

-- C7: invitation recipient email.
do $$
declare hh uuid := current_setting('t.hh')::uuid; st uuid; r record;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  st := public.add_student(hh, 'Second');
  select * into r from public.create_student_invitation(hh, st, 'second@example.com');
  perform set_config('t.inv', r.invitation_id::text, true);
  perform hp_test.eq((select recipient_email from public.household_invitation_recipients(hh) where invitation_id = r.invitation_id),
    'second@example.com', 'creator reads the recipient');

  -- No guardian reads the column directly any more, whatever their flags.
  perform hp_test.expect_error('select recipient_email from public.household_invitations', '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform hp_test.expect_error('select recipient_email from public.household_invitations', '42501');
  perform hp_test.check((select count(*) from public.household_invitations where id = r.invitation_id) = 1,
    'view-only guardian still sees the invitation itself');
  perform hp_test.eq((select count(*) from public.household_invitation_recipients(hh)), 0::bigint, 'view-only guardian gets no recipients');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform hp_test.eq((select count(*) from public.household_invitation_recipients(hh)), 0::bigint, 'set-goals guardian gets no recipients');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c2');
  perform hp_test.eq((select count(*) from public.household_invitation_recipients(hh)), 1::bigint, 'manage-students guardian reads student recipients');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c3');
  perform hp_test.eq((select count(*) from public.household_invitation_recipients(hh)), 1::bigint, 'manage-members guardian reads recipients');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.expect_error(format('select * from public.household_invitation_recipients(%L)', hh), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error(format('select * from public.household_invitation_recipients(%L)', hh), '42501');
  perform hp_test.as_anon();
  perform hp_test.expect_error(format('select * from public.household_invitation_recipients(%L)', hh), '42501');
  perform hp_test.as_owner();
end $$;

\o
\echo role_rules: all assertions passed
rollback;
