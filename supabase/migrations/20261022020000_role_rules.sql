-- Role rules for three household writes and one read (issue #218 findings C1, C6, C7).
-- Each brings the server in line with the rule the app and docs/HOUSEHOLD_PRACTICE.md already use.
--
-- C1  student_exam_plan and student_academic_interests: written by the linked student or a guardian with
--     set_goals (the same rule as weekly goals and planning preferences). Before: any guardian, view-only included.
-- C6  remove_household_school: a guardian with manage_students or set_goals, or the member who saved the school.
--     Saving stays open to every household member (the student can still add schools).
-- C7  household_invitations.recipient_email: no longer readable by column grant. household_invitation_recipients()
--     returns it only to guardians with manage_members, or with manage_students for student invitations.
--     Other invitation columns stay readable by any guardian, as before.

-- C1: every policy on both tables calls this helper, so redefining it changes insert, update and delete together.
create or replace function public.can_edit_student_plans(p_student uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.students s where s.id = p_student
    and (s.linked_user_id = auth.uid()
         or (s.household_id is not null and public.has_household_permission(s.household_id, 'set_goals'))))
$$;
comment on function public.can_edit_student_plans(uuid) is
  'Exam plan (CR-10) and academic interests (CR-13) writes: the linked student or a guardian with set_goals.';

-- C6
create or replace function public.remove_household_school(p_household uuid, p_institution_key text) returns void
language plpgsql security definer set search_path = '' as $$
begin
  if not public.is_household_member(p_household) then
    raise exception 'Not a member of this household' using errcode = '42501';
  end if;
  if not (public.has_household_permission(p_household, 'manage_students')
          or public.has_household_permission(p_household, 'set_goals')
          or exists (select 1 from public.household_saved_schools s
                     where s.household_id = p_household and s.institution_key = p_institution_key
                       and s.added_by = auth.uid())) then
    raise exception 'Only a parent who can manage students or set goals, or the person who saved this school, can remove it'
      using errcode = '42501';
  end if;
  delete from public.household_saved_schools s where s.household_id = p_household and s.institution_key = p_institution_key;
end $$;
comment on function public.remove_household_school(uuid, text) is
  'CR-9: remove a saved school. Needs manage_students or set_goals, or to be the member who saved it.';

-- C7
revoke select (recipient_email) on public.household_invitations from authenticated;

create function public.household_invitation_recipients(p_household uuid)
returns table (invitation_id uuid, recipient_email text)
language plpgsql stable security definer set search_path = '' as $$
begin
  if p_household is null or not public.is_household_guardian(p_household) then
    raise exception 'Not a guardian of this household' using errcode = '42501';
  end if;
  -- A guardian without the right flag gets no rows (not an error): they still see the invitations, not who they went to.
  return query
  select i.id, i.recipient_email from public.household_invitations i
  where i.household_id = p_household and i.recipient_email is not null
    and (public.has_household_permission(p_household, 'manage_members')
         or (i.role = 'student' and public.has_household_permission(p_household, 'manage_students')));
end $$;
revoke all on function public.household_invitation_recipients(uuid) from public, anon;
grant execute on function public.household_invitation_recipients(uuid) to authenticated, service_role;
comment on function public.household_invitation_recipients(uuid) is
  'Who each invitation was emailed to: guardians with manage_members (all), or manage_students (student invitations).';
