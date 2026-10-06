-- Email delivery for student invitations, plus revoke and replace.
--
-- The invitation code is still generated and hashed by create_household_invitation (single use, 72 hours by
-- default, only the SHA-256 digest stored). This adds:
--   * recipient_email: who the parent chose to email. Stored on the invitation only; never copied to the student.
--   * revoked_at/revoked_by: a guardian can cancel an outstanding invitation; accepting a revoked one fails.
--   * email_send_count/last_emailed_at: bounds resends so the sender can't be used to spam an address.
--   * create_student_invitation: create (and, by default, replace earlier outstanding invitations for the same
--     student) in one call, as the signed-in guardian, so the existing permission checks apply unchanged.
--   * prepare_invitation_email: the server-side email function calls this, as the guardian, to check the code is
--     theirs and still usable and to record the send. It returns what the email needs, never the hash.
--   * revoke_household_invitation.
-- Nothing here grants a student or a recipient anything; the email only carries the link and code.

alter table public.household_invitations
  add column recipient_email text check (recipient_email is null or (length(recipient_email) <= 320 and recipient_email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$')),
  add column revoked_at timestamptz,
  add column revoked_by uuid references auth.users(id) on delete set null,
  add column email_send_count integer not null default 0 check (email_send_count >= 0),
  add column last_emailed_at timestamptz;

grant select (recipient_email, revoked_at, last_emailed_at) on public.household_invitations to authenticated;

-- Same rules and order as before, with one addition: a revoked invitation is refused.
create or replace function public.accept_household_invitation(p_code text) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_uid uuid := auth.uid(); v_inv public.household_invitations; v_student public.students; v_own public.students;
begin
  if v_uid is null then raise exception 'Authentication required' using errcode = '42501'; end if;
  select * into v_inv from public.household_invitations i
  where i.code_hash = encode(sha256(convert_to(lower(btrim(coalesce(p_code, ''))), 'UTF8')), 'hex')
  for update;
  if not found then raise exception 'Invalid invitation code' using errcode = '22023'; end if;
  if v_inv.accepted_at is not null then raise exception 'Invitation has already been used' using errcode = '22023'; end if;
  if v_inv.revoked_at is not null then raise exception 'Invitation has been revoked' using errcode = '22023'; end if;
  if v_inv.expires_at <= now() then raise exception 'Invitation has expired' using errcode = '22023'; end if;
  if exists (select 1 from public.household_members m where m.household_id = v_inv.household_id and m.user_id = v_uid) then
    raise exception 'You are already a member of this household' using errcode = '22023';
  end if;
  select * into v_own from public.students s where s.linked_user_id = v_uid for update;
  if v_inv.role = 'student' and v_inv.student_id is not null then
    select * into v_student from public.students s where s.id = v_inv.student_id for update;
    if v_student.archived_at is not null then raise exception 'This student profile is archived' using errcode = '22023'; end if;
    if v_student.linked_user_id is not null then
      raise exception 'This student profile is already linked to another account' using errcode = '22023';
    end if;
    if v_own.id is not null then
      raise exception 'Your account is already linked to another student profile' using errcode = '22023';
    end if;
    update public.students set linked_user_id = v_uid, account_mode = 'student_login' where id = v_student.id;
  elsif v_inv.role = 'student' then
    if v_own.id is null then raise exception 'Create your student profile before joining a household' using errcode = '22023'; end if;
    if v_own.household_id is not null then raise exception 'Leave your current household first' using errcode = '22023'; end if;
    if v_own.archived_at is not null then raise exception 'This student profile is archived' using errcode = '22023'; end if;
    update public.students set household_id = v_inv.household_id where id = v_own.id;
  end if;
  insert into public.household_members(household_id, user_id, role, can_manage_students, can_set_goals,
    can_view_progress, can_manage_members, can_manage_billing)
  values (v_inv.household_id, v_uid, v_inv.role, 'manage_students' = any(v_inv.permissions), 'set_goals' = any(v_inv.permissions),
    'view_progress' = any(v_inv.permissions), 'manage_members' = any(v_inv.permissions), 'manage_billing' = any(v_inv.permissions));
  update public.household_invitations set accepted_by = v_uid, accepted_at = now() where id = v_inv.id;
  return v_inv.household_id;
end $$;

-- Create a student invitation, optionally addressed, revoking that student's earlier outstanding ones.
create function public.create_student_invitation(p_household uuid, p_student uuid, p_recipient_email text default null,
  p_replace boolean default true)
returns table (code text, invitation_id uuid, expires_at timestamptz)
language plpgsql security definer set search_path = '' as $$
declare v_code text; v_id uuid; v_exp timestamptz; v_email text := nullif(lower(btrim(coalesce(p_recipient_email, ''))), '');
begin
  if p_student is null then raise exception 'Choose the student to invite' using errcode = '22023'; end if;
  if not public.has_household_permission(p_household, 'manage_students') then
    raise exception 'Not allowed to invite student members to this household' using errcode = '42501';
  end if;
  -- create_household_invitation checks manage_students and that the profile is active and unlinked.
  if (select count(*) from public.household_invitations i where i.household_id = p_household
      and i.created_at > now() - interval '1 day') >= 30 then
    raise exception 'Too many invitations today; try again tomorrow' using errcode = '22023';
  end if;
  v_code := public.create_household_invitation(p_household, 'student', p_student, 72);
  update public.household_invitations i set recipient_email = v_email
  where i.code_hash = encode(sha256(convert_to(v_code, 'UTF8')), 'hex')
  returning i.id, i.expires_at into v_id, v_exp;
  if coalesce(p_replace, true) then
    update public.household_invitations i set revoked_at = now(), revoked_by = auth.uid()
    where i.household_id = p_household and i.student_id = p_student and i.id <> v_id
      and i.accepted_at is null and i.revoked_at is null and i.expires_at > now();
  end if;
  return query select v_code, v_id, v_exp;
end $$;

-- Called by the email function as the guardian: confirms the code belongs to an invitation they may manage and
-- that it can still be used, records the send, and returns what the email shows. Never returns the hash.
create function public.prepare_invitation_email(p_code text, p_recipient_email text)
returns table (invitation_id uuid, student_name text, inviter_name text, expires_at timestamptz, recipient_email text)
language plpgsql security definer set search_path = '' as $$
declare v_inv public.household_invitations; v_email text := lower(btrim(coalesce(p_recipient_email, '')));
begin
  if auth.uid() is null then raise exception 'Authentication required' using errcode = '42501'; end if;
  if v_email !~ '^[^@\s]+@[^@\s]+\.[^@\s]+$' or length(v_email) > 320 then
    raise exception 'Enter a valid email address' using errcode = '22023';
  end if;
  select * into v_inv from public.household_invitations i
  where i.code_hash = encode(sha256(convert_to(lower(btrim(coalesce(p_code, ''))), 'UTF8')), 'hex')
  for update;
  if not found or not public.has_household_permission(v_inv.household_id,
      case v_inv.role when 'guardian' then 'manage_members' else 'manage_students' end) then
    raise exception 'Invalid invitation code' using errcode = '22023';
  end if;
  if v_inv.accepted_at is not null then raise exception 'Invitation has already been used' using errcode = '22023'; end if;
  if v_inv.revoked_at is not null then raise exception 'Invitation has been revoked' using errcode = '22023'; end if;
  if v_inv.expires_at <= now() then raise exception 'Invitation has expired' using errcode = '22023'; end if;
  if v_inv.email_send_count >= 5 then raise exception 'This invitation has been emailed too many times; create a new one' using errcode = '22023'; end if;
  if v_inv.last_emailed_at > now() - interval '30 seconds' then
    raise exception 'Please wait a moment before sending again' using errcode = '22023';
  end if;
  update public.household_invitations i set recipient_email = v_email, email_send_count = i.email_send_count + 1,
    last_emailed_at = now() where i.id = v_inv.id;
  return query select v_inv.id,
    (select s.display_name from public.students s where s.id = v_inv.student_id),
    (select p.display_name from public.profiles p where p.id = auth.uid()),
    v_inv.expires_at, v_email;
end $$;

create function public.revoke_household_invitation(p_invitation uuid) returns void
language plpgsql security definer set search_path = '' as $$
declare v_inv public.household_invitations;
begin
  select * into v_inv from public.household_invitations i where i.id = p_invitation for update;
  if not found or not public.has_household_permission(v_inv.household_id,
      case v_inv.role when 'guardian' then 'manage_members' else 'manage_students' end) then
    raise exception 'Not allowed to revoke this invitation' using errcode = '42501';
  end if;
  if v_inv.accepted_at is not null then raise exception 'Invitation has already been used' using errcode = '22023'; end if;
  update public.household_invitations set revoked_at = coalesce(revoked_at, now()), revoked_by = coalesce(revoked_by, auth.uid())
  where id = v_inv.id;
end $$;

-- prepare_invitation_email is for the signed-in guardian (via the email function), like the others.
revoke all on function public.create_student_invitation(uuid, uuid, text, boolean) from public, anon;
revoke all on function public.prepare_invitation_email(text, text) from public, anon;
revoke all on function public.revoke_household_invitation(uuid) from public, anon;
grant execute on function public.create_student_invitation(uuid, uuid, text, boolean) to authenticated, service_role;
grant execute on function public.prepare_invitation_email(text, text) to authenticated, service_role;
grant execute on function public.revoke_household_invitation(uuid) to authenticated, service_role;
