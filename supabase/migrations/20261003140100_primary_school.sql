-- CR-12 (issue #37): one primary target school per household.
-- The flag lives on the saved-school row, so removing that school (remove_household_school, or the
-- institution cascade) clears the primary with it. The saved-schools read returns is_primary as a column.

alter table public.household_saved_schools add column is_primary boolean not null default false;
create unique index household_saved_schools_one_primary
  on public.household_saved_schools (household_id) where is_primary;
comment on column public.household_saved_schools.is_primary is
  'The household''s primary target school; at most one per household. Set through set_household_primary_school.';

-- Same write rule as save_household_school (any household member). A null key clears the primary.
create function public.set_household_primary_school(p_household uuid, p_institution_key text default null) returns void
language plpgsql security definer set search_path = '' as $$
begin
  if p_household is null or not public.is_household_member(p_household) then
    raise exception 'Not a member of this household' using errcode = '42501';
  end if;
  -- Serialise with save/remove for this household.
  perform 1 from public.households h where h.id = p_household for update;
  if p_institution_key is not null and not exists (select 1 from public.household_saved_schools s
       where s.household_id = p_household and s.institution_key = p_institution_key) then
    raise exception 'Save % before making it the primary school', p_institution_key using errcode = '22023';
  end if;
  update public.household_saved_schools s set is_primary = false
  where s.household_id = p_household and s.is_primary
    and s.institution_key is distinct from p_institution_key;
  if p_institution_key is not null then
    update public.household_saved_schools s set is_primary = true
    where s.household_id = p_household and s.institution_key = p_institution_key and not s.is_primary;
  end if;
end $$;

revoke all on function public.set_household_primary_school(uuid, text) from public, anon;
grant execute on function public.set_household_primary_school(uuid, text) to authenticated, service_role;
comment on function public.set_household_primary_school(uuid, text) is
  'CR-12: make a saved school the household''s primary target school, or clear it with a null key.';
