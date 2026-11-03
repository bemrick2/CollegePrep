-- CR-15 (#218 B4): the family's home state, for choosing a school's in-state or out-of-state published price.
--
-- * households.home_state: a two-letter USPS code for one of the 50 states or DC (uppercase), or null (not answered).
--   Readable by every household member with the household row (member_household_read); written like the household's
--   other settings (name, time_zone): a guardian with manage_members, through the existing manager_household_update
--   policy. Other members' updates reach no row.
-- * students.home_state: the same, for a student profile with no household (a self-managed student). Written through
--   the existing student_update policy: the linked student when the profile has no household or is independent, or a
--   guardian with manage_students. When the student belongs to a household, the household's value is the family's.
-- * Not a residency determination, and the server doesn't infer one: cost_projection keeps residency as a required
--   assumption the client chooses (it compares home_state with the school's state, and labels it as the family's
--   answer), and compare_institutions takes no residency input. Neither function changes.

create function public.is_us_state_code(p text) returns boolean
language sql immutable set search_path = '' as $$
  select p = any (array['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA',
    'ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD',
    'TN','TX','UT','VT','VA','WA','WV','WI','WY'])
$$;
revoke all on function public.is_us_state_code(text) from public, anon;
grant execute on function public.is_us_state_code(text) to authenticated, service_role;

alter table public.households add column home_state text check (home_state is null or public.is_us_state_code(home_state));
comment on column public.households.home_state is
  'CR-15: the family''s home state (USPS code, 50 states or DC), or null. The family''s answer, not a residency determination.';
grant update (home_state) on public.households to authenticated;

alter table public.students add column home_state text check (home_state is null or public.is_us_state_code(home_state));
comment on column public.students.home_state is
  'CR-15: home state for a student with no household (USPS code, 50 states or DC), or null; a household''s own value is the family''s.';
grant update (home_state) on public.students to authenticated;
