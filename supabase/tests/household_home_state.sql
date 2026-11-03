-- CR-15 (#218 B4): the family's home state on the household (and on a student profile with no household).
-- Who reads and writes it, the allowed codes, the narrow write path, and that the cost views are unchanged. Rolled back.
-- Run with psql -v ON_ERROR_STOP=1.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql
grant usage on schema hp_test to service_role;
grant execute on all functions in schema hp_test to service_role;

-- PARENT a1 (creator: every permission), CO a2 (default guardian: set_goals, no manage_members), MEMBERS c2
-- (manage_members only), VIEWER c1 (view_progress only), STUDENT 51 (linked); OTHER guardian b1 (another household);
-- SOLO 53 (a self-created profile, no household); OUTSIDER 99.
insert into auth.users(id) values ('20000000-0000-0000-0000-0000000000c1'), ('20000000-0000-0000-0000-0000000000c2');
do $$
declare hh uuid; st uuid; hh2 uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Home', 'America/Chicago');
  st := public.add_student(hh, 'Home Student');
  perform set_config('t.hh', hh::text, true);
  perform set_config('t.st', st::text, true);
  perform set_config('t.inv', public.create_household_invitation(hh, 'student', st), true);
  perform set_config('t.inv_co', public.create_household_invitation(hh, 'guardian'), true);
  perform set_config('t.inv_view', public.create_household_invitation(hh, 'guardian', null, 72, array['view_progress']), true);
  perform set_config('t.inv_mem', public.create_household_invitation(hh, 'guardian', null, 72, array['manage_members']), true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform public.accept_household_invitation(current_setting('t.inv_co'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform public.accept_household_invitation(current_setting('t.inv_view'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c2');
  perform public.accept_household_invitation(current_setting('t.inv_mem'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  hh2 := public.create_household('Other', 'America/Chicago');
  perform set_config('t.hh2', hh2::text, true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform set_config('t.solo', public.create_self_student_profile('Solo Student')::text, true);
  perform hp_test.as_owner();
  perform hp_test.check((select can_set_goals and not can_manage_members from public.household_members where user_id = '20000000-0000-0000-0000-0000000000a2'),
    'CO has set_goals without manage_members');
  perform hp_test.check((select can_manage_members and not can_set_goals from public.household_members where user_id = '20000000-0000-0000-0000-0000000000c2'),
    'MEMBERS has manage_members without set_goals');
end $$;

-- Privileges and the default. The column has no client write grant: the RPC is the only client path.
do $$
begin
  perform hp_test.check(not has_column_privilege('anon', 'public.households', 'home_state', 'SELECT,UPDATE'), 'anon: no household home_state');
  perform hp_test.check(not has_column_privilege('anon', 'public.students', 'home_state', 'SELECT,UPDATE'), 'anon: no student home_state');
  perform hp_test.check(not has_column_privilege('authenticated', 'public.households', 'home_state', 'INSERT,UPDATE'), 'no direct client write');
  perform hp_test.check(has_column_privilege('authenticated', 'public.households', 'home_state', 'SELECT'), 'clients read it');
  perform hp_test.check(not has_function_privilege('anon', 'public.set_household_home_state(uuid, text)', 'EXECUTE'), 'anon cannot call the RPC');
  perform hp_test.eq((select home_state from public.households where id = current_setting('t.hh')::uuid), null::text, 'unanswered by default');
end $$;

-- Writes: guardians with set_goals or manage_members, through the RPC; nobody else, and never by a direct update.
do $$
declare hh uuid := current_setting('t.hh')::uuid; who record; k int;
begin
  for who in select * from (values ('20000000-0000-0000-0000-0000000000a1'::uuid, 'PARENT', 'TN'),
      ('20000000-0000-0000-0000-0000000000a2'::uuid, 'CO (set_goals)', 'OR'), ('20000000-0000-0000-0000-0000000000c2'::uuid, 'MEMBERS (manage_members)', 'PR')) v(uid, label, code) loop
    perform hp_test.as_user(who.uid);
    perform hp_test.eq(public.set_household_home_state(hh, who.code), who.code, who.label || ' sets the home state');
    perform hp_test.eq((select home_state from public.households where id = hh), who.code, who.label || '''s value is stored');
    perform hp_test.expect_error(format($q$update public.households set home_state = 'WA' where id = %L$q$, hh), '42501');
  end loop;
  for who in select * from (values ('20000000-0000-0000-0000-0000000000c1'::uuid, 'VIEWER'), ('20000000-0000-0000-0000-000000000051'::uuid, 'STUDENT'),
      ('20000000-0000-0000-0000-0000000000b1'::uuid, 'OTHER guardian'), ('20000000-0000-0000-0000-000000000099'::uuid, 'OUTSIDER')) v(uid, label) loop
    perform hp_test.as_user(who.uid);
    perform hp_test.expect_error(format($q$select public.set_household_home_state(%L, 'WA')$q$, hh), '42501');
    perform hp_test.expect_error(format($q$update public.households set home_state = 'WA' where id = %L$q$, hh), '42501');
  end loop;
  -- A household that doesn't exist reads like someone else's.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.expect_error(format($q$select public.set_household_home_state(%L, 'WA')$q$, gen_random_uuid()), '42501');
  perform hp_test.expect_error($q$select public.set_household_home_state(null, 'WA')$q$, '42501');
  perform hp_test.as_anon();
  perform hp_test.expect_error(format($q$select public.set_household_home_state(%L, 'WA')$q$, hh), '42501');
  -- The service role has no user for the RPC; server tooling writes the column directly.
  perform set_config('role', 'service_role', true);
  perform hp_test.expect_error(format($q$select public.set_household_home_state(%L, 'WA')$q$, hh), '42501');
  update public.households set home_state = 'DC' where id = hh;
  get diagnostics k = row_count; perform hp_test.eq(k, 1, 'service role sets it directly');
  perform hp_test.as_owner();
  perform hp_test.eq((select home_state from public.households where id = hh), 'DC', 'only allowed writes landed');
end $$;

-- set_goals gains no other household-settings write: name and time_zone stay manage_members.
do $$
declare hh uuid := current_setting('t.hh')::uuid; k int;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  update public.households set name = 'Renamed by CO' where id = hh;
  get diagnostics k = row_count; perform hp_test.eq(k, 0, 'CO (set_goals) still cannot rename the household');
  update public.households set time_zone = 'UTC' where id = hh;
  get diagnostics k = row_count; perform hp_test.eq(k, 0, 'CO (set_goals) still cannot change the time zone');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c2');
  update public.households set name = 'Renamed by MEMBERS' where id = hh;
  get diagnostics k = row_count; perform hp_test.eq(k, 1, 'manage_members still renames');
  perform hp_test.as_owner();
end $$;

-- Reads: every member of the household with the household row; nobody outside it.
do $$
declare hh uuid := current_setting('t.hh')::uuid; who record;
begin
  for who in select * from (values ('20000000-0000-0000-0000-0000000000a1'::uuid, 'PARENT', 'DC'),
      ('20000000-0000-0000-0000-0000000000a2'::uuid, 'CO', 'DC'), ('20000000-0000-0000-0000-0000000000c1'::uuid, 'VIEWER', 'DC'),
      ('20000000-0000-0000-0000-0000000000c2'::uuid, 'MEMBERS', 'DC'),
      ('20000000-0000-0000-0000-000000000051'::uuid, 'STUDENT', 'DC'), ('20000000-0000-0000-0000-0000000000b1'::uuid, 'OTHER guardian', null),
      ('20000000-0000-0000-0000-000000000099'::uuid, 'OUTSIDER', null)) v(uid, label, want) loop
    perform hp_test.as_user(who.uid);
    perform hp_test.eq((select home_state from public.households where id = hh), who.want, who.label || ' reads the home state');
  end loop;
  perform hp_test.as_anon();
  perform hp_test.expect_error('select home_state from public.households', '42501');
  perform hp_test.as_owner();
end $$;

-- Codes: the 50 states, DC and the territories PR, GU, VI, AS and MP, uppercase; null clears. Anything else is refused,
-- by the RPC (22023) and by the column check (23514).
do $$
declare hh uuid := current_setting('t.hh')::uuid; c text;
begin
  perform hp_test.eq((select count(*) from unnest(array['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY',
    'LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT',
    'VT','VA','WA','WV','WI','WY','PR','GU','VI','AS','MP']) s where public.is_us_home_state_code(s)), 56::bigint, '56 codes');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  foreach c in array array['PR', 'GU', 'VI', 'AS', 'MP'] loop
    perform hp_test.eq(public.set_household_home_state(hh, c), c, c || ' (territory) accepted');
  end loop;
  foreach c in array array['tn', 'Tn', 'T', 'TN ', ' TN', 'TEN', 'XX', 'UM', 'FM', 'AA', ''] loop
    perform hp_test.expect_error(format('select public.set_household_home_state(%L, %L)', hh, c), '22023');
  end loop;
  perform hp_test.eq(public.set_household_home_state(hh, null), null::text, 'null clears it');
  perform hp_test.eq((select home_state from public.households where id = hh), null::text, 'cleared');
  perform hp_test.as_owner();
  perform hp_test.expect_error(format($q$update public.households set home_state = 'XX' where id = %L$q$, hh), '23514');
end $$;

-- A student with no household keeps their own; a household student can't set one on their profile.
do $$
declare solo uuid := current_setting('t.solo')::uuid; st uuid := current_setting('t.st')::uuid; k int;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  update public.students set home_state = 'WA' where id = solo;
  get diagnostics k = row_count; perform hp_test.eq(k, 1, 'a self-managed student sets their home state');
  perform hp_test.eq((select home_state from public.students where id = solo), 'WA', 'and reads it');
  update public.students set home_state = 'GU' where id = solo;
  perform hp_test.eq((select home_state from public.students where id = solo), 'GU', 'territories here too');
  perform hp_test.expect_error(format($q$update public.students set home_state = 'pr' where id = %L$q$, solo), '23514');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  update public.students set home_state = 'WA' where id = st;
  get diagnostics k = row_count; perform hp_test.eq(k, 0, 'a household student cannot set it on their profile');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((select count(*) from public.students where id = solo), 0::bigint, 'another family cannot see a solo profile');
  update public.students set home_state = 'TX' where id = solo;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  update public.students set home_state = 'TX' where id = solo;
  perform hp_test.as_owner();
  perform hp_test.eq((select home_state from public.students where id = solo), 'GU', 'nobody else changed it');
end $$;

-- The cost views are unchanged: residency stays the client's explicit input; the server infers none.
do $$
begin
  perform hp_test.eq(pg_get_function_identity_arguments('public.cost_projection(uuid, text[], text, jsonb)'::regprocedure),
    'p_student uuid, p_institution_keys text[], p_academic_year text, p_assumptions jsonb', 'cost_projection signature unchanged');
  perform hp_test.check(position('home_state' in pg_get_functiondef('public.cost_projection(uuid, text[], text, jsonb)'::regprocedure)) = 0,
    'cost_projection does not read home_state');
  perform hp_test.check(position('home_state' in pg_get_functiondef('public.compare_institutions(text[], text)'::regprocedure)) = 0,
    'compare_institutions does not read home_state');
end $$;
\o
\echo household_home_state: all assertions passed
rollback;
