-- Household role rules (#218 C1, C6, C7), tested directly against tables and RPCs with each role's identity.
-- Every restricted operation is attempted by every role; an unauthorized success fails the test. Rolled back.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql

insert into public.sources(id, canonical_url, authority) values
 ('51000000-0000-0000-0000-000000000001', 'https://example.edu/role-rules', 'institution');
insert into public.institutions(institution_key, ipeds_name, display_name, state_code, source_id, verification_status, identity_academic_year)
select 'role-rules-' || n, 'R', 'R', 'TN', '51000000-0000-0000-0000-000000000001', 'verified', '2023-24' from generate_series(1, 6) n;
-- Two more guardians: GOALS c1 (set_goals only) and MANAGER c2 (manage_students only).
insert into auth.users(id) values ('20000000-0000-0000-0000-0000000000c1'), ('20000000-0000-0000-0000-0000000000c2');
insert into public.exam_catalog values ('ap:role-rules-1', 'ap', 'Role Rules One'), ('ap:role-rules-2', 'ap', 'Role Rules Two');

-- PARENT a1 (creator, every permission); CO a2 (default guardian invitation); VIEWER b1 (view_progress only);
-- STUDENT 51 (linked by invitation); OUTSIDER 99.
do $$
declare hh uuid; st uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Role rules', 'America/Chicago');
  st := public.add_student(hh, 'Rule Student');
  perform set_config('t.hh', hh::text, true);
  perform set_config('t.st', st::text, true);
  perform set_config('t.inv_co', public.create_household_invitation(hh, 'guardian'), true);
  perform set_config('t.inv_view', public.create_household_invitation(hh, 'guardian', null, 72, array['view_progress']), true);
  perform set_config('t.inv_st', public.create_household_invitation(hh, 'student', st), true);
  perform set_config('t.inv_goals', public.create_household_invitation(hh, 'guardian', null, 72, array['set_goals']), true);
  perform set_config('t.inv_mgr', public.create_household_invitation(hh, 'guardian', null, 72, array['manage_students']), true);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform public.accept_household_invitation(current_setting('t.inv_co'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform public.accept_household_invitation(current_setting('t.inv_view'));
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv_st'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform public.accept_household_invitation(current_setting('t.inv_goals'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c2');
  perform public.accept_household_invitation(current_setting('t.inv_mgr'));
  perform hp_test.as_owner();
  perform hp_test.check((select can_set_goals and can_manage_students and not can_manage_members from public.household_members
    where user_id = '20000000-0000-0000-0000-0000000000a2'), 'CO holds the default guardian permissions');
  perform hp_test.check((select can_view_progress and not (can_set_goals or can_manage_students or can_manage_members) from public.household_members
    where user_id = '20000000-0000-0000-0000-0000000000b1'), 'VIEWER holds view_progress only');
end $$;

-- C1: exam plan and academic interests. Writers: the linked student and set_goals guardians.
do $$
declare r record; st uuid := current_setting('t.st')::uuid; n bigint; k int;
begin
  for r in select * from (values
      ('20000000-0000-0000-0000-0000000000a1'::uuid, 'PARENT', true), ('20000000-0000-0000-0000-0000000000a2'::uuid, 'CO', true),
      ('20000000-0000-0000-0000-0000000000b1'::uuid, 'VIEWER', false), ('20000000-0000-0000-0000-000000000051'::uuid, 'STUDENT', true),
      ('20000000-0000-0000-0000-0000000000c1'::uuid, 'GOALS', true), ('20000000-0000-0000-0000-0000000000c2'::uuid, 'MANAGER', false),
      ('20000000-0000-0000-0000-000000000099'::uuid, 'OUTSIDER', false)) v(uid, who, allowed) loop
    perform hp_test.as_owner();
    delete from public.student_exam_plan where student_id = st;
    delete from public.student_academic_interests where student_id = st;
    perform hp_test.as_user(r.uid);
    if r.allowed then
      -- Each write must reach exactly one row (a writer who can't see its rows would update or delete nothing).
      insert into public.student_exam_plan(student_id, exam_key, score) values (st, 'ap:role-rules-1', 3);
      perform hp_test.eq((select count(*) from public.student_exam_plan where student_id = st), 1::bigint, r.who || ' reads the exam plan it writes');
      update public.student_exam_plan set score = 4 where student_id = st and exam_key = 'ap:role-rules-1';
      get diagnostics k = row_count; perform hp_test.eq(k, 1, r.who || ' updates the exam plan');
      delete from public.student_exam_plan where student_id = st and exam_key = 'ap:role-rules-1';
      get diagnostics k = row_count; perform hp_test.eq(k, 1, r.who || ' deletes from the exam plan');
      insert into public.student_academic_interests(student_id, certainty, interests) values (st, 'few', '[{"kind":"area","key":"business"}]');
      update public.student_academic_interests set certainty = 'sure' where student_id = st;
      get diagnostics k = row_count; perform hp_test.eq(k, 1, r.who || ' updates interests');
      delete from public.student_academic_interests where student_id = st;
      get diagnostics k = row_count; perform hp_test.eq(k, 1, r.who || ' deletes interests');
    else
      perform hp_test.expect_error(format($q$insert into public.student_exam_plan(student_id, exam_key, score) values (%L, 'ap:role-rules-1', 3)$q$, st), '42501');
      -- Reads: VIEWER has view_progress; nobody else refused here may read.
      perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
      insert into public.student_exam_plan(student_id, exam_key, score) values (st, 'ap:role-rules-1', 1);
      insert into public.student_academic_interests(student_id, certainty, interests) values (st, 'unsure', '[]');
      perform hp_test.as_user(r.uid);
      perform hp_test.eq((select count(*) from public.student_exam_plan where student_id = st), (r.who = 'VIEWER')::int::bigint, r.who || ' exam-plan read');
      perform hp_test.eq((select count(*) from public.student_academic_interests where student_id = st), (r.who = 'VIEWER')::int::bigint, r.who || ' interests read');
      perform hp_test.as_owner();
      delete from public.student_exam_plan where student_id = st;
      delete from public.student_academic_interests where student_id = st;
      perform hp_test.as_user(r.uid);
      perform hp_test.expect_error(format($q$insert into public.student_academic_interests(student_id, certainty, interests) values (%L, 'few', '[{"kind":"area","key":"business"}]')$q$, st), '42501');
      -- Rows another member wrote: update and delete reach nothing.
      perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
      insert into public.student_exam_plan(student_id, exam_key, score) values (st, 'ap:role-rules-2', 2);
      insert into public.student_academic_interests(student_id, certainty, interests) values (st, 'few', '[{"kind":"area","key":"business"}]');
      perform hp_test.as_user(r.uid);
      update public.student_exam_plan set score = 5 where student_id = st;
      delete from public.student_exam_plan where student_id = st;
      update public.student_academic_interests set certainty = 'sure' where student_id = st;
      delete from public.student_academic_interests where student_id = st;
      perform hp_test.as_owner();
      select count(*) into n from public.student_exam_plan where student_id = st and score = 2;
      perform hp_test.eq(n, 1::bigint, r.who || ' changed or removed an exam-plan row');
      select count(*) into n from public.student_academic_interests where student_id = st and certainty = 'few';
      perform hp_test.eq(n, 1::bigint, r.who || ' changed or removed academic interests');
    end if;
    perform hp_test.as_owner();
  end loop;
end $$;

-- C6: saving stays open to members; removal needs manage_students or set_goals, or having saved it.
do $$
declare r record; hh uuid := current_setting('t.hh')::uuid; n bigint;
begin
  for r in select * from (values
      ('20000000-0000-0000-0000-0000000000a1'::uuid, 'PARENT', true, true), ('20000000-0000-0000-0000-0000000000a2'::uuid, 'CO', true, true),
      ('20000000-0000-0000-0000-0000000000b1'::uuid, 'VIEWER', true, false), ('20000000-0000-0000-0000-000000000051'::uuid, 'STUDENT', true, false),
      ('20000000-0000-0000-0000-0000000000c1'::uuid, 'GOALS', true, true), ('20000000-0000-0000-0000-0000000000c2'::uuid, 'MANAGER', true, true),
      ('20000000-0000-0000-0000-000000000099'::uuid, 'OUTSIDER', false, false)) v(uid, who, may_save, may_remove_others) loop
    -- A school the parent saved.
    perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
    perform public.save_household_school(hh, 'role-rules-1');
    perform hp_test.as_user(r.uid);
    if r.may_remove_others then
      perform public.remove_household_school(hh, 'role-rules-1');
    else
      perform hp_test.expect_error(format('select public.remove_household_school(%L, %L)', hh, 'role-rules-1'), '42501');
      perform hp_test.as_owner();
      select count(*) into n from public.household_saved_schools where household_id = hh and institution_key = 'role-rules-1';
      perform hp_test.eq(n, 1::bigint, r.who || ' removed a school someone else saved');
    end if;
    -- A school this role saves itself: it may remove its own.
    perform hp_test.as_user(r.uid);
    if r.may_save then
      perform public.save_household_school(hh, 'role-rules-2');
      perform public.remove_household_school(hh, 'role-rules-2');
      if r.may_remove_others then
        perform public.remove_household_school(hh, 'role-rules-2');  -- again: a no-op
      else
        -- Without removal rights, a key that isn't saved is refused like one that is (no existence oracle).
        perform hp_test.expect_error(format('select public.remove_household_school(%L, %L)', hh, 'role-rules-2'), '42501');
      end if;
    else
      perform hp_test.expect_error(format('select public.save_household_school(%L, %L)', hh, 'role-rules-2'), '42501');
      perform hp_test.expect_error(format('select public.remove_household_school(%L, %L)', hh, 'role-rules-2'), '42501');
    end if;
    perform hp_test.as_owner();
    delete from public.household_saved_schools where household_id = hh;
  end loop;
  -- A school whose saver's account is gone (added_by null) is removable only by guardians with removal rights.
  perform hp_test.as_owner();
  insert into public.household_saved_schools(household_id, institution_key, added_by) values (hh, 'role-rules-3', null);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.expect_error(format('select public.remove_household_school(%L, %L)', hh, 'role-rules-3'), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.expect_error(format('select public.remove_household_school(%L, %L)', hh, 'role-rules-3'), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform public.remove_household_school(hh, 'role-rules-3');
  perform hp_test.as_owner();
  perform hp_test.eq((select count(*) from public.household_saved_schools where household_id = hh), 0::bigint, 'set-goals guardian removed it');
  -- The table itself stays write-protected for every client role.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.expect_error(format($q$delete from public.household_saved_schools where household_id = %L$q$, hh), '42501');
  perform hp_test.as_owner();
end $$;

-- C7: recipient emails only through the RPC, to manage_members guardians (all) and manage_students guardians (students).
do $$
declare hh uuid := current_setting('t.hh')::uuid; st2 uuid; got text; n bigint;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  insert into public.profiles(id, display_name) values (auth.uid(), 'Role Parent') on conflict do nothing;
  st2 := public.add_student(hh, 'Second Student');
  perform 1 from public.create_student_invitation(hh, st2, 'second@example.com');
  perform hp_test.as_owner();
  -- A guardian invitation carrying an address (the column exists on every invitation).
  insert into public.household_invitations(household_id, role, permissions, code_hash, created_by, expires_at, recipient_email)
  values (hh, 'guardian', '{}', repeat('e', 64), '20000000-0000-0000-0000-0000000000a1', now() + interval '1 day', 'guardian@example.com');

  -- Another household's invitation with an address: never returned for this household.
  insert into public.households(id, name, time_zone) values ('52000000-0000-0000-0000-000000000001', 'Other household', 'America/Chicago');
  insert into public.household_invitations(household_id, role, permissions, code_hash, created_by, expires_at, recipient_email)
  values ('52000000-0000-0000-0000-000000000001', 'student', '{}', repeat('f', 64), null, now() + interval '1 day', 'elsewhere@example.com');

  -- No client role reads the column directly.
  foreach got in array array['20000000-0000-0000-0000-0000000000a1', '20000000-0000-0000-0000-0000000000a2',
                             '20000000-0000-0000-0000-0000000000b1', '20000000-0000-0000-0000-000000000051',
                             '20000000-0000-0000-0000-000000000099'] loop
    perform hp_test.as_user(got::uuid);
    perform hp_test.expect_error(format('select recipient_email from public.household_invitations where household_id = %L', hh), '42501');
  end loop;

  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');  -- manage_members: every address
  select string_agg(recipient_email, ',' order by recipient_email) into got from public.household_invitation_recipients(hh);
  perform hp_test.eq(got, 'guardian@example.com,second@example.com', 'manage-members guardian sees every recipient');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');  -- manage_students only: student invitations
  select string_agg(recipient_email, ',' order by recipient_email) into got from public.household_invitation_recipients(hh);
  perform hp_test.eq(got, 'second@example.com', 'manage-students guardian sees student recipients only');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c2');  -- manage_students only: student invitations
  select string_agg(recipient_email, ',' order by recipient_email) into got from public.household_invitation_recipients(hh);
  perform hp_test.eq(got, 'second@example.com', 'manage-students-only guardian sees student recipients only');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');  -- set_goals only: none
  select count(*) into n from public.household_invitation_recipients(hh);
  perform hp_test.eq(n, 0::bigint, 'set-goals-only guardian sees no recipient');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');  -- view only: none
  select count(*) into n from public.household_invitation_recipients(hh);
  perform hp_test.eq(n, 0::bigint, 'view-only guardian sees no recipient');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.expect_error(format('select * from public.household_invitation_recipients(%L)', hh), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error(format('select * from public.household_invitation_recipients(%L)', hh), '42501');
  perform hp_test.as_anon();
  perform hp_test.expect_error(format('select * from public.household_invitation_recipients(%L)', hh), '42501');
  -- The rest of the invitation list stays readable to guardians.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  select count(*) into n from public.household_invitations where household_id = hh;
  perform hp_test.check(n > 0, 'guardians still list invitations without addresses');
  perform hp_test.as_owner();
end $$;

rollback;
