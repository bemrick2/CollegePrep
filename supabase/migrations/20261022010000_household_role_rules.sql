-- Household role rules (#218 C1, C6, C7): the server enforces the established permission flags.
--
-- C1  The exam plan (CR-10) and academic interests (CR-13) are written by the linked student or by a guardian
--     with set_goals: the same guardian rule as plans and goals. Before this, any guardian of the household
--     could write them, including a guardian invited with view_progress only.
-- C6  Saving a school stays open to household members. Removing one needs a guardian with manage_students or
--     set_goals, or the member who saved it. Before this, any member (a view-only guardian, the student) could
--     remove the family's saved schools.
-- C7  An invitation's recipient_email is no longer readable through the table. It is served by
--     household_invitation_recipients() to guardians with manage_members, and, for student invitations, to
--     guardians with manage_students (the people who may create those invitations). Before this, any guardian
--     could read it by column grant.

-- C1
create or replace function public.can_edit_student_plans(p_student uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.students s where s.id = p_student
    and (s.linked_user_id = auth.uid()
      or (s.household_id is not null and public.has_household_permission(s.household_id, 'set_goals'))))
$$;
comment on function public.can_edit_student_plans(uuid) is
  'Exam plan and academic interests writes: the linked student, or a guardian of the student''s household with set_goals.';

-- C6
create or replace function public.remove_household_school(p_household uuid, p_institution_key text) returns void
language plpgsql security definer set search_path = '' as $$
declare v_added_by uuid;
begin
  if p_household is null or not public.is_household_member(p_household) then
    raise exception 'Not a member of this household' using errcode = '42501';
  end if;
  -- Serialise with save and set-primary for this household.
  perform 1 from public.households h where h.id = p_household for update;
  select s.added_by into v_added_by from public.household_saved_schools s
  where s.household_id = p_household and s.institution_key = p_institution_key;
  if not found then
    return;  -- nothing saved under that key: removing it again is a no-op
  end if;
  if not (public.has_household_permission(p_household, 'manage_students')
          or public.has_household_permission(p_household, 'set_goals')
          or v_added_by = auth.uid()) then
    raise exception 'Removing a saved school needs manage-students or set-goals, or saving it yourself'
      using errcode = '42501';
  end if;
  delete from public.household_saved_schools s where s.household_id = p_household and s.institution_key = p_institution_key;
end $$;
revoke all on function public.remove_household_school(uuid, text) from public, anon;
grant execute on function public.remove_household_school(uuid, text) to authenticated, service_role;
comment on function public.remove_household_school(uuid, text) is
  'Remove a saved school: guardians with manage_students or set_goals, or the member who saved it.';

-- C7
revoke select (recipient_email) on public.household_invitations from authenticated;

create function public.household_invitation_recipients(p_household uuid)
returns table (invitation_id uuid, recipient_email text)
language plpgsql stable security definer set search_path = '' as $$
begin
  if p_household is null or not public.is_household_guardian(p_household) then
    raise exception 'Only guardians of this household can list invitations' using errcode = '42501';
  end if;
  return query
    select i.id, i.recipient_email from public.household_invitations i
    where i.household_id = p_household and i.recipient_email is not null
      and (public.has_household_permission(p_household, 'manage_members')
           or (i.role = 'student' and public.has_household_permission(p_household, 'manage_students')));
end $$;
revoke all on function public.household_invitation_recipients(uuid) from public, anon;
grant execute on function public.household_invitation_recipients(uuid) to authenticated, service_role;
comment on function public.household_invitation_recipients(uuid) is
  'Recipient emails of a household''s invitations: all of them for guardians with manage_members; student invitations for guardians with manage_students.';
