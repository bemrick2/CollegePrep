-- CR-15 (#218 B4): the family's home state, for choosing a school's in-state or out-of-state published price.
--
-- * households.home_state: a two-letter USPS code for one of the 50 states, DC, or the territories PR, GU, VI, AS and
--   MP (uppercase), or null (not answered). Readable by every household member with the household row
--   (member_household_read).
-- * Written only through set_household_home_state(p_household, p_state), by a guardian with set_goals or manage_members
--   ("editable by guardians"). It is the narrow path for this one column: set_goals gains no other household-settings
--   write (name and time_zone stay manage_members, through manager_household_update), and the column has no client
--   update grant. Anyone else, including another household and anon, gets 42501; a code outside the list is 22023;
--   null clears it. Returns the stored value.
-- * students.home_state: the same codes, for a student profile with no household (a self-managed student). Written
--   through the existing student_update policy: the linked student when the profile has no household or is
--   independent, or a guardian with manage_students. When the student belongs to a household, the household's value is
--   the family's.
-- * Not a residency determination, and the server doesn't infer one. Cost residency stays the client's input:
--   cost_projection keeps assumptions.residency as a required assumption the client chooses (the client compares
--   home_state with the school's state and labels it as the family's answer), and compare_institutions takes no
--   residency input. Neither function changes.

create function public.is_us_home_state_code(p text) returns boolean
language sql immutable set search_path = '' as $$
  select p = any (array['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA',
    'ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD',
    'TN','TX','UT','VT','VA','WA','WV','WI','WY',
    'PR','GU','VI','AS','MP'])
$$;
revoke all on function public.is_us_home_state_code(text) from public, anon;
grant execute on function public.is_us_home_state_code(text) to authenticated, service_role;
comment on function public.is_us_home_state_code(text) is
  'CR-15: USPS codes accepted as a home state: the 50 states, DC, PR, GU, VI, AS and MP.';

alter table public.households add column home_state text check (home_state is null or public.is_us_home_state_code(home_state));
comment on column public.households.home_state is
  'CR-15: the family''s home state (USPS code: 50 states, DC or a territory), or null. The family''s answer, not a residency determination. Set through set_household_home_state.';

create function public.set_household_home_state(p_household uuid, p_state text) returns text
language plpgsql security definer set search_path = '' as $$
begin
  if p_household is null or not (public.has_household_permission(p_household, 'set_goals')
                                  or public.has_household_permission(p_household, 'manage_members')) then
    raise exception 'Setting the home state needs a guardian with set-goals or manage-members' using errcode = '42501';
  end if;
  if p_state is not null and not public.is_us_home_state_code(p_state) then
    raise exception 'Home state must be a USPS code for a US state, DC or territory' using errcode = '22023';
  end if;
  update public.households h set home_state = p_state where h.id = p_household;
  return p_state;
end $$;
revoke all on function public.set_household_home_state(uuid, text) from public, anon;
grant execute on function public.set_household_home_state(uuid, text) to authenticated, service_role;
comment on function public.set_household_home_state(uuid, text) is
  'CR-15: set or clear the household''s home state; guardians with set_goals or manage_members.';

alter table public.students add column home_state text check (home_state is null or public.is_us_home_state_code(home_state));
comment on column public.students.home_state is
  'CR-15: home state for a student with no household (USPS code: 50 states, DC or a territory), or null; a household''s own value is the family''s.';
grant update (home_state) on public.students to authenticated;
