-- One household with every guardian permission shape, plus the people who must be refused. Include after
-- support/test_helpers.sql, inside the test transaction. Sets t.hh, t.st (Riley, linked to STUDENT), t.st_b (Ben,
-- unlinked), t.hh2 / t.st2 (another household's student), t.solo (STUDENT2's own profile, no household) and t.adult
-- (STUDENT3's independent profile).
--
--   PARENT   20..a1  created the household: every permission
--   CO       20..a2  default guardian invitation: manage_students, set_goals, view_progress
--   VIEWER   20..b1  view_progress only
--   GOALS    20..c1  set_goals only
--   MANAGER  20..c2  manage_students only
--   STUDENT  20..51  Riley's own login, linked by invitation
--   OTHER    20..d1  a guardian of another household (every permission there)
--   STUDENT2 20..52  a student who signed up alone (no household, not independent)
--   STUDENT3 20..53  an independent adult student (no household)
--   OUTSIDER 20..99  no relation
insert into auth.users(id) values ('20000000-0000-0000-0000-0000000000c1'), ('20000000-0000-0000-0000-0000000000c2'),
  ('20000000-0000-0000-0000-0000000000d1');
do $$
declare hh uuid; st uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Roles', 'America/Chicago');
  st := public.add_student(hh, 'Riley');
  perform set_config('t.hh', hh::text, true);
  perform set_config('t.st', st::text, true);
  perform set_config('t.st_b', public.add_student(hh, 'Ben')::text, true);
  perform set_config('t.inv_co', public.create_household_invitation(hh, 'guardian'), true);
  perform set_config('t.inv_view', public.create_household_invitation(hh, 'guardian', null, 72, array['view_progress']), true);
  perform set_config('t.inv_goals', public.create_household_invitation(hh, 'guardian', null, 72, array['set_goals']), true);
  perform set_config('t.inv_mgr', public.create_household_invitation(hh, 'guardian', null, 72, array['manage_students']), true);
  perform set_config('t.inv_st', public.create_household_invitation(hh, 'student', st), true);
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform public.accept_household_invitation(current_setting('t.inv_co'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform public.accept_household_invitation(current_setting('t.inv_view'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform public.accept_household_invitation(current_setting('t.inv_goals'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c2');
  perform public.accept_household_invitation(current_setting('t.inv_mgr'));
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv_st'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000d1');
  perform set_config('t.hh2', public.create_household('Other', 'UTC')::text, true);
  perform set_config('t.st2', public.add_student(current_setting('t.hh2')::uuid, 'Cleo')::text, true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform set_config('t.solo', public.create_self_student_profile('Casey', 2028, 11, false, 'America/New_York')::text, true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform set_config('t.adult', public.create_self_student_profile('Alex', null, null, true, 'America/Chicago')::text, true);
  perform hp_test.as_owner();
  perform hp_test.check((select can_view_progress and not (can_set_goals or can_manage_students) from public.household_members
    where user_id = '20000000-0000-0000-0000-0000000000b1'), 'VIEWER holds view_progress only');
  perform hp_test.check((select can_set_goals and not (can_view_progress or can_manage_students) from public.household_members
    where user_id = '20000000-0000-0000-0000-0000000000c1'), 'GOALS holds set_goals only');
  perform hp_test.check((select can_manage_students and not (can_view_progress or can_set_goals) from public.household_members
    where user_id = '20000000-0000-0000-0000-0000000000c2'), 'MANAGER holds manage_students only');
  perform hp_test.check((select linked_user_id = '20000000-0000-0000-0000-000000000051' from public.students where id = st),
    'STUDENT is linked to Riley');
end $$;

-- Everyone, for per-role loops: (uid, who). anon is tested separately.
create temp table t_roles(uid uuid, who text) on commit drop;
insert into t_roles values
  ('20000000-0000-0000-0000-0000000000a1', 'PARENT'), ('20000000-0000-0000-0000-0000000000a2', 'CO'),
  ('20000000-0000-0000-0000-0000000000b1', 'VIEWER'), ('20000000-0000-0000-0000-0000000000c1', 'GOALS'),
  ('20000000-0000-0000-0000-0000000000c2', 'MANAGER'), ('20000000-0000-0000-0000-000000000051', 'STUDENT'),
  ('20000000-0000-0000-0000-0000000000d1', 'OTHER'), ('20000000-0000-0000-0000-000000000099', 'OUTSIDER');
grant select on t_roles to anon, authenticated, service_role;
