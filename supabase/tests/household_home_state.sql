-- CR-15 (#218 B4): the family's home state on the household (and on a student profile with no household).
-- Who reads and writes it, the allowed codes, and that the cost views are unchanged. Rolled back.
-- Run with psql -v ON_ERROR_STOP=1.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql
grant usage on schema hp_test to service_role;
grant execute on all functions in schema hp_test to service_role;

-- PARENT a1 (creator: every permission), CO a2 (default guardian: no manage_members), VIEWER c1 (view_progress only),
-- STUDENT 51 (linked); OTHER guardian b1 (another household); SOLO 53 (a self-created profile, no household); OUTSIDER 99.
insert into auth.users(id) values ('20000000-0000-0000-0000-0000000000c1');
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
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a2');
  perform public.accept_household_invitation(current_setting('t.inv_co'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000c1');
  perform public.accept_household_invitation(current_setting('t.inv_view'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  hh2 := public.create_household('Other', 'America/Chicago');
  perform set_config('t.hh2', hh2::text, true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform set_config('t.solo', public.create_self_student_profile('Solo Student')::text, true);
  perform hp_test.as_owner();
end $$;

-- Privileges and the default.
do $$
begin
  perform hp_test.check(not has_column_privilege('anon', 'public.households', 'home_state', 'SELECT,UPDATE'), 'anon: no household home_state');
  perform hp_test.check(not has_column_privilege('anon', 'public.students', 'home_state', 'SELECT,UPDATE'), 'anon: no student home_state');
  perform hp_test.check(not has_column_privilege('authenticated', 'public.households', 'home_state', 'INSERT'), 'home_state is not set by insert');
  perform hp_test.eq((select home_state from public.households where id = current_setting('t.hh')::uuid), null::text, 'unanswered by default');
end $$;

-- Writes: a guardian with manage_members; every other member's update reaches no row.
do $$
declare hh uuid := current_setting('t.hh')::uuid; who record; k int;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  update public.households set home_state = 'TN' where id = hh;
  get diagnostics k = row_count; perform hp_test.eq(k, 1, 'PARENT (manage_members) sets the home state');
  for who in select * from (values ('20000000-0000-0000-0000-0000000000a2'::uuid, 'CO (no manage_members)'),
      ('20000000-0000-0000-0000-0000000000c1'::uuid, 'VIEWER'), ('20000000-0000-0000-0000-000000000051'::uuid, 'STUDENT'),
      ('20000000-0000-0000-0000-0000000000b1'::uuid, 'OTHER guardian'), ('20000000-0000-0000-0000-000000000099'::uuid, 'OUTSIDER')) v(uid, label) loop
    perform hp_test.as_user(who.uid);
    update public.households set home_state = 'OR' where id = hh;
    get diagnostics k = row_count; perform hp_test.eq(k, 0, who.label || ' cannot set the home state');
  end loop;
  perform hp_test.as_anon();
  perform hp_test.expect_error(format($q$update public.households set home_state = 'OR' where id = %L$q$, hh), '42501');
  perform hp_test.as_owner();
  perform hp_test.eq((select home_state from public.households where id = hh), 'TN', 'only PARENT''s write landed');
  -- The service role (server tooling) may set it.
  perform set_config('role', 'service_role', true);
  update public.households set home_state = 'DC' where id = hh;
  get diagnostics k = row_count; perform hp_test.eq(k, 1, 'service role sets it');
  perform hp_test.as_owner();
end $$;

-- Reads: every member of the household with the household row; nobody outside it.
do $$
declare hh uuid := current_setting('t.hh')::uuid; who record;
begin
  for who in select * from (values ('20000000-0000-0000-0000-0000000000a1'::uuid, 'PARENT', 'DC'),
      ('20000000-0000-0000-0000-0000000000a2'::uuid, 'CO', 'DC'), ('20000000-0000-0000-0000-0000000000c1'::uuid, 'VIEWER', 'DC'),
      ('20000000-0000-0000-0000-000000000051'::uuid, 'STUDENT', 'DC'), ('20000000-0000-0000-0000-0000000000b1'::uuid, 'OTHER guardian', null),
      ('20000000-0000-0000-0000-000000000099'::uuid, 'OUTSIDER', null)) v(uid, label, want) loop
    perform hp_test.as_user(who.uid);
    perform hp_test.eq((select home_state from public.households where id = hh), who.want, who.label || ' reads the home state');
  end loop;
  perform hp_test.as_anon();
  perform hp_test.expect_error('select home_state from public.households', '42501');
  perform hp_test.as_owner();
end $$;

-- Codes: the 50 states and DC, uppercase; null clears. Territories, lowercase and padding are refused.
do $$
declare hh uuid := current_setting('t.hh')::uuid; c text; k int;
begin
  perform hp_test.eq((select count(*) from unnest(array['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY',
    'LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT',
    'VT','VA','WA','WV','WI','WY']) s where public.is_us_state_code(s)), 51::bigint, '51 codes');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  foreach c in array array['PR', 'GU', 'VI', 'AS', 'MP', 'tn', 'Tn', 'T', 'TN ', ' TN', 'TEN', 'XX', ''] loop
    perform hp_test.expect_error(format('update public.households set home_state = %L where id = %L', c, hh), '23514');
  end loop;
  update public.households set home_state = 'OR' where id = hh;
  perform hp_test.eq((select home_state from public.households where id = hh), 'OR', 'OR accepted');
  update public.households set home_state = null where id = hh;
  get diagnostics k = row_count; perform hp_test.eq(k, 1, 'null clears it');
  perform hp_test.eq((select home_state from public.households where id = hh), null::text, 'cleared');
  perform hp_test.as_owner();
end $$;

-- A student with no household keeps their own; a household student can't set one on their profile.
do $$
declare solo uuid := current_setting('t.solo')::uuid; st uuid := current_setting('t.st')::uuid; k int;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  update public.students set home_state = 'WA' where id = solo;
  get diagnostics k = row_count; perform hp_test.eq(k, 1, 'a self-managed student sets their home state');
  perform hp_test.eq((select home_state from public.students where id = solo), 'WA', 'and reads it');
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
  perform hp_test.eq((select home_state from public.students where id = solo), 'WA', 'nobody else changed it');
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
