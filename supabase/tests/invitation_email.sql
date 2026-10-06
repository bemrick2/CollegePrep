-- Student invitations: link token + invite code, emailing, revoke/replace, rate limiting, outcomes. Rolled back.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql

-- gb = 20..b1 guardian; s2 = 20..52 and s3 = 20..53 student logins; x = 20..99 outsider.
do $$
declare hh uuid; st uuid; r record; first_code text; first_id uuid; first_short text;
begin
  perform hp_test.as_anon();
  perform hp_test.expect_error('select * from public.create_student_invitation(gen_random_uuid(), gen_random_uuid())', '42501');
  perform hp_test.expect_error('select * from public.prepare_invitation_email(''x'', ''a@b.co'')', '42501');
  perform hp_test.expect_error('select public.revoke_household_invitation(gen_random_uuid())', '42501');
  perform hp_test.expect_error('select * from public.redeem_household_invitation(''x'')', '42501');

  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  -- Internals and secrets are out of reach for clients.
  perform hp_test.expect_error('select pepper from public.invitation_code_pepper', '42501');
  perform hp_test.expect_error('select * from public.invitation_code_attempts', '42501');
  perform hp_test.expect_error('select public.invite_code_digest(''ABCDE-FGHJK'')', '42501');
  perform hp_test.expect_error('select public.claim_household_invitation(gen_random_uuid())', '42501');
  perform hp_test.expect_error('select short_code_hash from public.household_invitations', '42501');

  insert into public.profiles(id, display_name) values (auth.uid(), 'Jordan');
  hh := public.create_household('Household B', 'America/Chicago');
  -- A student profile needs no email; the invitation's recipient is never copied onto it.
  st := public.add_student(hh, 'Riley', 2030, 8);
  perform set_config('t.hh', hh::text, true);
  perform set_config('t.st', st::text, true);

  select * into r from public.create_student_invitation(hh, st, ' Riley@Example.COM ');
  first_code := r.code; first_id := r.invitation_id; first_short := r.invite_code;
  perform hp_test.check(r.code ~ '^[0-9a-f]{64}$', 'link token: 64 hex');
  perform hp_test.check(r.invite_code ~ '^[2-9A-HJKMNP-TW-Z]{5}-[2-9A-HJKMNP-TW-Z]{5}$', 'invite code: XXXXX-XXXXX, unambiguous alphabet');
  perform hp_test.check(abs(extract(epoch from (r.expires_at - now())) - 72 * 3600) < 5, '72-hour lifetime');
  perform hp_test.eq((select recipient_email from public.household_invitations where id = r.invitation_id), 'riley@example.com', 'recipient stored normalised');

  -- Preparing an email checks both credentials, returns names and expiry, never a digest, and counts the send.
  perform hp_test.expect_error(format('select * from public.prepare_invitation_email(%L, ''riley@example.com'', ''ZZZZZ-ZZZZZ'')', first_code), '22023', '%Invalid%');
  select * into r from public.prepare_invitation_email(first_code, 'riley@example.com', lower(first_short));
  perform hp_test.eq(r.student_name, 'Riley', 'email names the student');
  perform hp_test.eq(r.inviter_name, 'Jordan', 'email names the guardian');
  perform hp_test.expect_error(format('select * from public.prepare_invitation_email(%L, ''riley@example.com'')', first_code), '22023', '%wait a moment%');
  perform hp_test.expect_error(format('select * from public.prepare_invitation_email(%L, ''not an email'')', first_code), '22023', '%valid email%');
  perform hp_test.expect_error('select * from public.prepare_invitation_email(''deadbeef'', ''riley@example.com'')', '22023', '%Invalid%');

  -- A replacement cancels the earlier outstanding invitation; still one student profile.
  select * into r from public.create_student_invitation(hh, st, 'riley@example.com');
  perform set_config('t.code', r.code, true);
  perform set_config('t.short', r.invite_code, true);
  perform set_config('t.old', first_code, true);
  perform set_config('t.old_short', first_short, true);
  perform hp_test.check(r.invite_code <> first_short, 'replacement has a new code');
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

-- Outcomes are distinct and returned (not raised), so wrong guesses are counted; then rate limiting.
do $$
declare r record; i int;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.eq((select outcome from public.redeem_household_invitation(current_setting('t.old'))), 'revoked', 'old link token: revoked');
  perform hp_test.eq((select outcome from public.redeem_household_invitation(current_setting('t.old_short'))), 'revoked', 'old invite code: revoked');
  perform hp_test.eq((select outcome from public.redeem_household_invitation(repeat('ab', 32))), 'invalid', 'unknown token: invalid');
  perform hp_test.eq((select outcome from public.redeem_household_invitation('not a code')), 'invalid', 'malformed code: invalid');
  for i in 1 .. 8 loop
    perform hp_test.eq((select outcome from public.redeem_household_invitation('ZZZZZ-ZZZZ' || substr('23456789', i, 1))), 'invalid', 'wrong guess: invalid');
  end loop;
  -- 9 failures recorded (revoked is a right code, not a guess); the 10th failure trips the limit.
  perform hp_test.eq((select outcome from public.redeem_household_invitation('ZZZZZ-ZZZZA')), 'invalid', '10th wrong guess');
  perform hp_test.eq((select outcome from public.redeem_household_invitation(current_setting('t.short'))), 'rate_limited', 'even a right code is refused while limited');
  -- Link tokens are not rate limited (unguessable), and only failures count against the account.
  perform hp_test.as_owner();
  perform hp_test.eq((select count(*) from public.invitation_code_attempts where user_id = '20000000-0000-0000-0000-000000000099'), 10::bigint, 'ten failures recorded');
end $$;

-- The student joins with the human code (any case, dash optional); then it is single-use.
do $$ begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.eq((select outcome from public.redeem_household_invitation(lower(replace(current_setting('t.short'), '-', ' ')))), 'joined', 'student joins by invite code');
  perform hp_test.check((select linked_user_id = auth.uid() from public.students where id = current_setting('t.st')::uuid), 'same guardian-created profile linked');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform hp_test.eq((select outcome from public.redeem_household_invitation(current_setting('t.short'))), 'used', 'code reuse: used');
  perform hp_test.eq((select outcome from public.redeem_household_invitation(current_setting('t.code'))), 'used', 'link token of a used invite: used');
  perform hp_test.expect_error('select public.accept_household_invitation(current_setting(''t.code''))', '22023', '%already been used%');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.check((select accepted_by = '20000000-0000-0000-0000-000000000052' and accepted_at is not null
    from public.household_invitations where id = (select id from public.household_invitations where revoked_at is null and accepted_at is not null)), 'accepted_at/by recorded');
  perform hp_test.eq((select count(*) from public.students where household_id = current_setting('t.hh')::uuid), 1::bigint, 'no duplicate student');
  perform hp_test.check(not exists (select 1 from public.students s where s.id = current_setting('t.st')::uuid
    and row_to_json(s)::text ilike '%riley@example.com%'), 'recipient email not on the student profile');
  perform hp_test.expect_error(format('select public.revoke_household_invitation(%L)',
    (select id from public.household_invitations where accepted_at is not null)), '22023', '%already been used%');
  perform hp_test.expect_error('select * from public.prepare_invitation_email(current_setting(''t.code''), ''riley@example.com'')', '22023', '%already been used%');
  perform hp_test.expect_error(format('select * from public.create_student_invitation(%L, %L)', current_setting('t.hh'), current_setting('t.st')), '22023', '%unlinked%');
  perform hp_test.as_owner();
end $$;

-- Revoke works on an outstanding invitation; an expired one reads as expired, by link and by code.
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
  perform set_config('t.exp_short', r.invite_code, true);
  perform hp_test.as_owner();
  update public.household_invitations set expires_at = now() - interval '1 second' where id = r.invitation_id;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000053');
  perform hp_test.eq((select outcome from public.redeem_household_invitation(current_setting('t.exp'))), 'expired', 'expired link: expired');
  perform hp_test.eq((select outcome from public.redeem_household_invitation(current_setting('t.exp_short'))), 'expired', 'expired code: expired');
  perform hp_test.as_owner();
end $$;
\o
\echo invitation_email: all assertions passed
rollback;
