-- Emailed student invitations: create/replace, prepare-for-email, revoke, and acceptance rules. Rolled back.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql

-- gb = 20..b1 guardian; s2 = 20..52 student login; x = 20..99 outsider; s3 = 20..53 second student login.
do $$
declare hh uuid; st uuid; r record; first_code text; first_id uuid;
begin
  perform hp_test.as_anon();
  perform hp_test.expect_error('select * from public.create_student_invitation(gen_random_uuid(), gen_random_uuid())', '42501');
  perform hp_test.expect_error('select * from public.prepare_invitation_email(''x'', ''a@b.co'')', '42501');
  perform hp_test.expect_error('select public.revoke_household_invitation(gen_random_uuid())', '42501');

  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  insert into public.profiles(id, display_name) values (auth.uid(), 'Jordan');
  hh := public.create_household('Household B', 'America/Chicago');
  -- A student profile needs no email; the invitation's recipient is never copied onto it.
  st := public.add_student(hh, 'Riley', 2030, 8);
  perform set_config('t.hh', hh::text, true);
  perform set_config('t.st', st::text, true);

  select * into r from public.create_student_invitation(hh, st, ' Riley@Example.COM ');
  first_code := r.code; first_id := r.invitation_id;
  perform hp_test.check(r.code ~ '^[0-9a-f]{64}$', 'code format unchanged');
  perform hp_test.check(abs(extract(epoch from (r.expires_at - now())) - 72 * 3600) < 5, '72-hour lifetime');
  perform hp_test.eq((select recipient_email from public.household_invitations where id = r.invitation_id), 'riley@example.com', 'recipient stored normalised');
  perform hp_test.expect_error('select code_hash from public.household_invitations', '42501');

  -- Preparing an email returns the names and expiry, never the hash, and counts the send.
  select * into r from public.prepare_invitation_email(first_code, 'riley@example.com');
  perform hp_test.eq(r.student_name, 'Riley', 'email names the student');
  perform hp_test.eq(r.inviter_name, 'Jordan', 'email names the guardian');
  perform hp_test.expect_error(format('select * from public.prepare_invitation_email(%L, ''riley@example.com'')', first_code), '22023', '%wait a moment%');
  perform hp_test.expect_error(format('select * from public.prepare_invitation_email(%L, ''not an email'')', first_code), '22023', '%valid email%');
  perform hp_test.expect_error('select * from public.prepare_invitation_email(''deadbeef'', ''riley@example.com'')', '22023', '%Invalid%');

  -- A replacement revokes the earlier outstanding invitation for the same student; still one student profile.
  select * into r from public.create_student_invitation(hh, st, 'riley@example.com');
  perform set_config('t.code', r.code, true);
  perform set_config('t.old', first_code, true);
  perform hp_test.check((select revoked_at is not null from public.household_invitations where id = first_id), 'replacement revokes the old invite');
  perform hp_test.check((select revoked_at is null from public.household_invitations where id = r.invitation_id), 'replacement is live');
  perform hp_test.eq((select count(*) from public.students where household_id = hh), 1::bigint, 'replacement adds no student');
  perform hp_test.check((select true from public.students where id = st and linked_user_id is null), 'profile unlinked until accepted');

  -- An outsider can't prepare, revoke or create invitations for this household.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error(format('select * from public.prepare_invitation_email(%L, ''x@y.co'')', r.code), '22023', '%Invalid%');
  perform hp_test.expect_error(format('select public.revoke_household_invitation(%L)', r.invitation_id), '42501');
  perform hp_test.expect_error(format('select * from public.create_student_invitation(%L, %L)', hh, st), '42501');
  perform hp_test.eq((select count(*) from public.household_invitations), 0::bigint, 'outsider sees no invitations');
  perform hp_test.as_owner();
end $$;

-- The student: revoked code refused; live code claims the guardian-created profile once; reuse refused.
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.expect_error('select public.accept_household_invitation(current_setting(''t.old''))', '22023', '%revoked%');
  perform hp_test.eq(public.accept_household_invitation(current_setting('t.code')), current_setting('t.hh')::uuid, 'student joins');
  perform hp_test.check((select linked_user_id = auth.uid() from public.students where id = current_setting('t.st')::uuid), 'same profile linked');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform hp_test.expect_error('select public.accept_household_invitation(current_setting(''t.code''))', '22023', '%already been used%');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.check((select accepted_by = '20000000-0000-0000-0000-000000000052' and accepted_at is not null
    from public.household_invitations where recipient_email = 'riley@example.com' and revoked_at is null), 'accepted_at/by recorded');
  perform hp_test.eq((select count(*) from public.students where household_id = current_setting('t.hh')::uuid), 1::bigint, 'no duplicate student');
  -- The recipient email is not copied anywhere on the student.
  perform hp_test.check(not exists (select 1 from public.students s where s.id = current_setting('t.st')::uuid
    and row_to_json(s)::text ilike '%riley@example.com%'), 'recipient email not on the student profile');
  -- Used invitations can't be revoked, emailed, or replaced for a linked student.
  perform hp_test.expect_error(format('select public.revoke_household_invitation(%L)',
    (select id from public.household_invitations where accepted_at is not null)), '22023', '%already been used%');
  perform hp_test.expect_error('select * from public.prepare_invitation_email(current_setting(''t.code''), ''riley@example.com'')', '22023', '%already been used%');
  perform hp_test.expect_error(format('select * from public.create_student_invitation(%L, %L)', current_setting('t.hh'), current_setting('t.st')), '22023', '%unlinked%');
  perform hp_test.as_owner();
end $$;

-- Revoke works on an outstanding invitation; an expired one reads as expired.
do $$
declare hh uuid := current_setting('t.hh')::uuid; st uuid; r record;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  st := public.add_student(hh, 'Avery', 2032, 6);
  select * into r from public.create_student_invitation(hh, st);
  perform public.revoke_household_invitation(r.invitation_id);
  perform hp_test.expect_error(format('select * from public.prepare_invitation_email(%L, ''a@b.co'')', r.code), '22023', '%revoked%');
  select * into r from public.create_student_invitation(hh, st);
  perform set_config('t.exp', r.code, true);
  perform hp_test.as_owner();
  update public.household_invitations set expires_at = now() - interval '1 second' where id = r.invitation_id;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error('select public.accept_household_invitation(current_setting(''t.exp''))', '22023', '%expired%');
  perform hp_test.as_owner();
end $$;
\o
\echo invitation_email: all assertions passed
rollback;
