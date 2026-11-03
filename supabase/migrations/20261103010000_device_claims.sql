-- Device registrations move only with proof that the caller controls the device (owner requirement 2026-11-03,
-- follow-up to CR-27 / #298). Knowing another login's device id, FCM token or web push endpoint is not enough.
--
-- Before: report_notification_device moved a device id, token or endpoint held by another login when the caller
-- presented the same endpoint or token. An endpoint or token can leak (logs, a shared screenshot, a copied
-- subscription), so presenting one is no longer proof.
--
-- Now:
-- * report_notification_device(...) returns a status instead of void:
--     'registered'            the caller's own device (new, or already theirs) was recorded, as before;
--     'verification_pending'  the device id, token or endpoint is held by another login: nothing moves; a pending
--                             claim is recorded and a silent "verify device" push will go to that device;
--     'verification_limited'  as above, but the caller made too many claims in the last hour (5), or the device
--                             already has 3 pending claims from other logins: nothing is recorded;
--     'device_held'           the device id is held by another login and that row has no live endpoint or token
--                             (none, or the push service said it is gone), so no push can verify it: nothing moves;
--                             the app should generate a new device id and report again.
-- * notification_device_claims: one pending claim per (device held by another login, claimant). It keeps the
--   claimant's report, a hash of the nonce (never the nonce), and expires 10 minutes after it was made. A report while
--   the caller's claim is pending and not yet challenged refreshes it; once challenged or expired, the newest report
--   replaces it (status 'replaced'), so one login never holds more than one of a device's 3 pending slots. Once a
--   claim is resolved, the claimant's endpoint, keys and token are cleared. No client access.
-- * issue_device_claim_challenges(p_claimant) (service role only, for supabase/functions/verify-notification-device):
--   for each pending, unexpired claim not yet challenged, makes a random nonce, stores only its SHA-256, and returns the
--   nonce once, with where to push it:
--     - a web push target: the HELD row's endpoint, encrypted with the CLAIMANT's presented p256dh/auth. Only a
--       browser that both receives that endpoint's pushes and holds the private key for those keys can read it, i.e.
--       the real browser, re-reporting its own subscription. A squatter who registered the endpoint with fake keys
--       can't block the real browser (its claim is encrypted to the real keys); an attacker who presents their own
--       keys for someone else's endpoint can't read the push either (it goes to the endpoint, which only the real
--       browser receives, and that browser can't decrypt it with its own key);
--     - an FCM target: the HELD row's token (FCM delivers only to the install that holds it).
--   A web push claim whose claimant presented no keys can't be verified: the report returns 'device_held'.
--   At most 3 verify pushes per held device per hour, whoever claims; further claims wait (and may expire).
-- * confirm_device_claim(p_nonce) (signed-in caller) returns:
--     'confirmed'             the caller made the claim: the held row is removed and the caller's report is applied;
--     'verification_pending'  confirmed, but the caller's report still conflicts with another login's device (each
--                             held row needs its own proof);
--     'declined'              the device's current owner received the push (they are still signed in there): the
--                             claim is closed and nothing moves;
--     'expired'               the claim had expired: nothing moves, and the attempt counts;
--     'invalid'               unknown, used or closed nonce (the attempt counts), or another login's live claim
--                             (not counted: nobody can build up a lockout from nonces they didn't guess);
--     'locked'                5 counted attempts in the last hour: refused without looking at the nonce.
--   A nonce that is not 64 lowercase hex characters is refused with 22023, uncounted.
--   A wrong or expired nonce never moves anything; a view-only guardian (or anyone) who reports a student's device
--   only creates a claim whose nonce goes to the student's device.
-- * unregister_notification_device(p_device) (the device's owner): removes the registration at once, so a shared
--   device stops getting this login's reminders. Client contract: call it on sign-out and on account switch, then
--   report on the next sign-in; the challenge applies only when the previous owner never signed out. It also closes
--   the caller's own pending claims made from that device id. Returns whether a registration of the caller's was removed.
-- * purge_device_claims(p_now) (service role only; implemented, not scheduled): closes expired pending claims, deletes
--   resolved claims older than 30 days and failure rows older than 1 day. Returns the counts.
-- * Reports and confirmations of one device id, token or endpoint are serialised by the same transaction advisory
--   locks as before (ids in sorted order, then token, then endpoint).
-- Objects are altered or replaced in place. device_handle (student_notification_devices) is unchanged.

create table public.notification_device_claims (
  id uuid primary key default gen_random_uuid(),
  -- The row another login holds (by id, token or endpoint). The claim goes with it.
  target_device_id uuid not null references public.notification_devices(id) on delete cascade,
  claimant_user_id uuid not null references auth.users(id) on delete cascade,
  -- The claimant's report, applied only after a confirmed nonce.
  device_id uuid not null,
  permission text not null check (permission in ('granted', 'denied', 'default', 'unsupported')),
  platform text check (platform in ('ios', 'android', 'desktop', 'other')),
  channel text not null check (channel in ('webpush', 'fcm')),
  push_token text check (push_token is null or length(push_token) between 20 and 4096),
  endpoint text check (endpoint is null or (endpoint ~ '^https://' and length(endpoint) <= 2048)),
  p256dh text check (p256dh is null or length(p256dh) <= 200),
  auth_secret text check (auth_secret is null or length(auth_secret) <= 100),
  -- SHA-256 of the nonce, set when the challenge is issued. The nonce itself is never stored.
  nonce_hash bytea check (nonce_hash is null or length(nonce_hash) = 32),
  status text not null default 'pending' check (status in ('pending', 'confirmed', 'declined', 'expired', 'replaced', 'withdrawn')),
  created_at timestamptz not null default now(),
  expires_at timestamptz not null,
  issued_at timestamptz,
  resolved_at timestamptz,
  check (expires_at > created_at),
  check ((status = 'pending') = (resolved_at is null)),
  -- A resolved claim keeps no push credentials of the claimant.
  check (status = 'pending' or (push_token is null and endpoint is null and p256dh is null and auth_secret is null))
);
create index notification_device_claims_target_idx on public.notification_device_claims(target_device_id, issued_at desc);
create unique index notification_device_claims_once on public.notification_device_claims(target_device_id, claimant_user_id)
  where status = 'pending';
create unique index notification_device_claims_nonce on public.notification_device_claims(nonce_hash) where nonce_hash is not null;
create index notification_device_claims_claimant_idx on public.notification_device_claims(claimant_user_id, created_at desc);
alter table public.notification_device_claims enable row level security;
revoke all on public.notification_device_claims from anon, authenticated;
grant select, insert, update, delete on public.notification_device_claims to service_role;
comment on table public.notification_device_claims is
  'Pending moves of a device registration held by another login; applied only after the device returns the nonce.';

-- Resolving a claim clears the claimant's push credentials (the report is applied from the row first, when it is).
create function public.device_claim_resolve_trigger() returns trigger
language plpgsql set search_path = '' as $$
begin
  if new.status <> 'pending' then
    new.push_token := null; new.endpoint := null; new.p256dh := null; new.auth_secret := null;
    new.resolved_at := coalesce(new.resolved_at, now());
  end if;
  return new;
end $$;
create trigger notification_device_claims_resolve before update of status on public.notification_device_claims
  for each row execute function public.device_claim_resolve_trigger();

-- Invalid confirmations, for the attempt limit. No client access.
create table public.notification_device_claim_failures (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  failed_at timestamptz not null default now()
);
create index notification_device_claim_failures_user_idx on public.notification_device_claim_failures(user_id, failed_at desc);
alter table public.notification_device_claim_failures enable row level security;
revoke all on public.notification_device_claim_failures from anon, authenticated;
grant select, insert, update, delete on public.notification_device_claim_failures to service_role;

-- ---------------------------------------------------------------------------------------------------------------
-- Internal helpers (owner only)
-- ---------------------------------------------------------------------------------------------------------------

create function public.device_claim_ttl() returns interval
language sql immutable set search_path = '' as $$ select interval '10 minutes' $$;

create function public.device_nonce_hash(p_nonce text) returns bytea
language sql immutable set search_path = '' as $$ select pg_catalog.sha256(pg_catalog.convert_to(p_nonce, 'UTF8')) $$;

-- Rows of OTHER logins that a report of (device id, token, endpoint) by p_me would touch.
create function public.notification_device_conflicts_internal(p_me uuid, p_device uuid, p_token text, p_endpoint text)
returns setof public.notification_devices
language sql stable set search_path = '' as $$
  select d.* from public.notification_devices d
  where d.user_id <> p_me
    and (d.id = p_device or (p_token is not null and d.push_token = p_token) or (p_endpoint is not null and d.endpoint = p_endpoint))
  order by d.id
$$;

-- Records the caller's own device. Callers check first that no other login holds the id, token or endpoint.
create function public.notification_device_register_internal(p_me uuid, p_device uuid, p_permission text, p_platform text,
  p_channel text, p_token text, p_endpoint text, p_p256dh text, p_auth text)
returns void language plpgsql set search_path = '' as $$
begin
  -- The caller's own subscription under another of their device ids is this device now.
  if p_token is not null then
    delete from public.notification_devices d where d.user_id = p_me and d.push_token = p_token and d.id <> p_device;
  end if;
  if p_endpoint is not null then
    delete from public.notification_devices d where d.user_id = p_me and d.endpoint = p_endpoint and d.id <> p_device;
  end if;
  insert into public.notification_devices as d (id, user_id, permission, platform, channel, push_token, endpoint, p256dh,
      auth_secret, checked_at, gone_at)
  values (p_device, p_me, p_permission, p_platform, p_channel, p_token, p_endpoint, p_p256dh, p_auth, now(), null)
  on conflict (id) do update set permission = excluded.permission, platform = coalesce(excluded.platform, d.platform),
    channel = excluded.channel, push_token = excluded.push_token,
    endpoint = excluded.endpoint, p256dh = excluded.p256dh, auth_secret = excluded.auth_secret, checked_at = now(),
    gone_at = case when excluded.endpoint is not distinct from d.endpoint and excluded.push_token is not distinct from d.push_token
                   then d.gone_at end
  where d.user_id = p_me;  -- never another login's row
  if not found then
    raise exception 'Device registration conflict' using errcode = '40001';
  end if;
  -- At most 20 devices per login: the least recently seen go first.
  delete from public.notification_devices d where d.user_id = p_me and d.id in (
    select x.id from public.notification_devices x where x.user_id = p_me order by x.checked_at desc, x.id offset 20);
end $$;

create function public.notification_device_lock_internal(p_ids uuid[], p_token text, p_endpoint text) returns void
language plpgsql set search_path = '' as $$
declare v uuid;
begin
  for v in select distinct x from unnest(p_ids) x where x is not null order by 1 loop
    perform pg_catalog.pg_advisory_xact_lock(pg_catalog.hashtextextended('notification_device:' || v::text, 0));
  end loop;
  if p_token is not null then
    perform pg_catalog.pg_advisory_xact_lock(pg_catalog.hashtextextended('notification_token:' || p_token, 0));
  end if;
  if p_endpoint is not null then
    perform pg_catalog.pg_advisory_xact_lock(pg_catalog.hashtextextended('notification_endpoint:' || p_endpoint, 0));
  end if;
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- Client RPCs
-- ---------------------------------------------------------------------------------------------------------------

drop function public.report_notification_device(uuid, text, jsonb, text, text, text);
create function public.report_notification_device(p_device uuid, p_permission text, p_subscription jsonb default null,
  p_platform text default null, p_channel text default 'webpush', p_token text default null)
returns text language plpgsql volatile security definer set search_path = '' as $$
declare v_me uuid := auth.uid(); v_channel text := coalesce(p_channel, 'webpush'); v_granted boolean := p_permission = 'granted';
  v_endpoint text; v_token text; v_p256dh text; v_auth text; r record; v_conflicts integer := 0; v_held integer := 0;
  v_pending integer := 0; v_limited boolean := false;
begin
  if v_me is null then raise exception 'Sign in first' using errcode = '42501'; end if;
  if p_device is null then raise exception 'A device id is required' using errcode = '22023'; end if;
  if v_channel not in ('webpush', 'fcm') then raise exception 'Unknown push channel' using errcode = '22023'; end if;
  if p_permission is null or p_permission not in ('granted', 'denied', 'default', 'unsupported') then
    raise exception 'Unknown notification permission' using errcode = '22023';
  end if;
  v_endpoint := case when v_granted and v_channel = 'webpush' then p_subscription->>'endpoint' end;
  v_token := case when v_granted and v_channel = 'fcm' then p_token end;
  if v_endpoint is not null and not public.push_endpoint_allowed(v_endpoint) then
    raise exception 'Unsupported push service' using errcode = '22023';
  end if;
  v_p256dh := case when v_endpoint is not null then p_subscription->'keys'->>'p256dh' end;
  v_auth := case when v_endpoint is not null then p_subscription->'keys'->>'auth' end;
  perform public.notification_device_lock_internal(array[p_device], v_token, v_endpoint);

  for r in select * from public.notification_device_conflicts_internal(v_me, p_device, v_token, v_endpoint) loop
    v_conflicts := v_conflicts + 1;
    if (r.endpoint is null and r.push_token is null) or r.gone_at is not null
       or (r.push_token is null and v_endpoint is null) then
      -- No live push target, or a browser target and no keys of the caller's to encrypt the challenge to.
      v_held := v_held + 1;
      continue;
    end if;
    -- The caller's pending, not yet challenged claim on this device: refresh the report it will apply.
    update public.notification_device_claims c set device_id = p_device, permission = p_permission, platform = p_platform,
      channel = v_channel, push_token = v_token, endpoint = v_endpoint, p256dh = v_p256dh, auth_secret = v_auth
    where c.target_device_id = r.id and c.claimant_user_id = v_me and c.status = 'pending'
      and c.nonce_hash is null and c.expires_at > now();
    if found then v_pending := v_pending + 1; continue; end if;
    -- Otherwise the newest report replaces the caller's older pending claim (challenged or expired).
    update public.notification_device_claims c set status = case when c.expires_at > now() then 'replaced' else 'expired' end
    where c.target_device_id = r.id and c.claimant_user_id = v_me and c.status = 'pending';
    if (select count(*) from public.notification_device_claims c
        where c.claimant_user_id = v_me and c.created_at > now() - interval '1 hour') >= 5
       or (select count(*) from public.notification_device_claims c
           where c.target_device_id = r.id and c.status = 'pending' and c.expires_at > now()) >= 3 then
      v_limited := true;
      continue;
    end if;
    insert into public.notification_device_claims(target_device_id, claimant_user_id, device_id, permission, platform, channel,
        push_token, endpoint, p256dh, auth_secret, expires_at)
    values (r.id, v_me, p_device, p_permission, p_platform, v_channel, v_token, v_endpoint, v_p256dh, v_auth,
        now() + public.device_claim_ttl());
    v_pending := v_pending + 1;
  end loop;

  if v_conflicts = 0 then
    perform public.notification_device_register_internal(v_me, p_device, p_permission, p_platform, v_channel, v_token,
      v_endpoint, v_p256dh, v_auth);
    return 'registered';
  end if;
  if v_pending > 0 then return 'verification_pending'; end if;
  if v_limited then return 'verification_limited'; end if;
  return 'device_held';
end $$;

create function public.confirm_device_claim(p_nonce text) returns text
language plpgsql volatile security definer set search_path = '' as $$
declare v_me uuid := auth.uid(); c public.notification_device_claims; v_owner uuid; v_left integer;
  v_device uuid; v_permission text; v_platform text; v_channel text; v_token text; v_endpoint text; v_p256dh text; v_auth text;
begin
  if v_me is null then raise exception 'Sign in first' using errcode = '42501'; end if;
  if p_nonce is null or p_nonce !~ '^[0-9a-f]{64}$' then
    raise exception 'Not a verification code' using errcode = '22023';
  end if;
  if (select count(*) from public.notification_device_claim_failures f
      where f.user_id = v_me and f.failed_at > now() - interval '1 hour') >= 5 then
    return 'locked';
  end if;
  select * into c from public.notification_device_claims x where x.nonce_hash = public.device_nonce_hash(p_nonce) for update;
  if c.id is null or c.status <> 'pending' then
    insert into public.notification_device_claim_failures(user_id) values (v_me);
    return 'invalid';
  end if;
  if c.expires_at <= now() then
    update public.notification_device_claims set status = 'expired' where id = c.id;
    insert into public.notification_device_claim_failures(user_id) values (v_me);
    return 'expired';
  end if;
  perform public.notification_device_lock_internal(array[c.device_id, c.target_device_id], c.push_token, c.endpoint);
  select d.user_id into v_owner from public.notification_devices d where d.id = c.target_device_id;
  if v_owner is null then
    -- The held row is gone (its owner unregistered): close the claim; the claimant's next report registers.
    update public.notification_device_claims set status = 'expired' where id = c.id;
    return 'expired';
  end if;
  if v_owner = v_me and c.claimant_user_id <> v_me then
    -- The push reached the device while its owner is still signed in there: the device stays theirs.
    update public.notification_device_claims set status = 'declined' where id = c.id;
    return 'declined';
  end if;
  if c.claimant_user_id <> v_me then
    return 'invalid';  -- a live claim of another login: refused, not counted, and the claim stays for its claimant
  end if;
  v_device := c.device_id; v_permission := c.permission; v_platform := c.platform; v_channel := c.channel;
  v_token := c.push_token; v_endpoint := c.endpoint; v_p256dh := c.p256dh; v_auth := c.auth_secret;
  update public.notification_device_claims set status = 'confirmed' where id = c.id;
  -- The held row goes (its delivery history stays with its student, unattributed); other claims on it go with it.
  delete from public.notification_devices d where d.id = c.target_device_id;
  select count(*) into v_left from public.notification_device_conflicts_internal(v_me, v_device, v_token, v_endpoint);
  if v_left > 0 then return 'verification_pending'; end if;
  perform public.notification_device_register_internal(v_me, v_device, v_permission, v_platform, v_channel, v_token,
    v_endpoint, v_p256dh, v_auth);
  return 'confirmed';
end $$;

create function public.unregister_notification_device(p_device uuid) returns boolean
language plpgsql volatile security definer set search_path = '' as $$
declare v_me uuid := auth.uid();
begin
  if v_me is null then raise exception 'Sign in first' using errcode = '42501'; end if;
  if p_device is null then return false; end if;
  perform public.notification_device_lock_internal(array[p_device], null, null);
  -- The caller's own pending claims made from this device end with the sign-out.
  update public.notification_device_claims c set status = 'withdrawn'
  where c.claimant_user_id = v_me and c.device_id = p_device and c.status = 'pending';
  delete from public.notification_devices d where d.id = p_device and d.user_id = v_me;
  return found;
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- Service only: the verify-device push
-- ---------------------------------------------------------------------------------------------------------------

-- Challenges to send now: one per pending, unexpired, not yet challenged claim (of p_claimant, or all). The nonce is
-- returned once, here, and stored only as a hash. The target is the HELD device's stored endpoint or token.
create function public.issue_device_claim_challenges(p_claimant uuid default null) returns setof jsonb
language plpgsql volatile security definer set search_path = '' as $$
declare r record; v_nonce text;
begin
  update public.notification_device_claims c set status = 'expired'
  where c.status = 'pending' and c.expires_at <= now() and (p_claimant is null or c.claimant_user_id = p_claimant);
  for r in
    select c.id, c.expires_at, c.target_device_id, d.channel, d.endpoint, d.push_token,
      c.p256dh as claimant_p256dh, c.auth_secret as claimant_auth
    from public.notification_device_claims c
    join public.notification_devices d on d.id = c.target_device_id
    where c.status = 'pending' and c.nonce_hash is null and c.expires_at > now()
      and (p_claimant is null or c.claimant_user_id = p_claimant)
      and d.gone_at is null
      and ((d.channel = 'fcm' and d.push_token is not null)
           or (d.channel = 'webpush' and d.endpoint is not null and c.p256dh is not null and c.auth_secret is not null))
    order by c.created_at
    for update of c skip locked
  loop
    -- At most 3 verify pushes per device per hour, whoever claims (counted under the device's row lock).
    perform 1 from public.notification_devices d where d.id = r.target_device_id for update;
    continue when (select count(*) from public.notification_device_claims x
                   where x.target_device_id = r.target_device_id and x.issued_at > now() - interval '1 hour') >= 3;
    v_nonce := pg_catalog.encode(pg_catalog.sha256(pg_catalog.convert_to(
      gen_random_uuid()::text || gen_random_uuid()::text || pg_catalog.clock_timestamp()::text, 'UTF8')), 'hex');
    update public.notification_device_claims set nonce_hash = public.device_nonce_hash(v_nonce), issued_at = now() where id = r.id;
    -- Web push: to the held endpoint, encrypted to the claimant's keys. FCM: to the held token.
    return next jsonb_build_object('claim_id', r.id, 'nonce', v_nonce, 'expires_at', r.expires_at,
      'device', jsonb_build_object('id', r.target_device_id, 'channel', r.channel,
        'endpoint', case when r.channel = 'webpush' then r.endpoint end,
        'p256dh', case when r.channel = 'webpush' then r.claimant_p256dh end,
        'auth', case when r.channel = 'webpush' then r.claimant_auth end,
        'token', case when r.channel = 'fcm' then r.push_token end));
  end loop;
end $$;

-- Retention (service role only; implemented, not scheduled): pending claims past expiry close, resolved claims older
-- than 30 days and failure rows older than a day are deleted (the attempt limit looks back one hour).
create function public.purge_device_claims(p_now timestamptz default now()) returns jsonb
language plpgsql volatile security definer set search_path = '' as $$
declare v_expired integer; v_claims integer; v_failures integer; v_at timestamptz := coalesce(p_now, now());
begin
  update public.notification_device_claims c set status = 'expired', resolved_at = v_at
  where c.status = 'pending' and c.expires_at <= v_at;
  get diagnostics v_expired = row_count;
  delete from public.notification_device_claims c where c.status <> 'pending' and c.resolved_at < v_at - interval '30 days';
  get diagnostics v_claims = row_count;
  delete from public.notification_device_claim_failures f where f.failed_at < v_at - interval '1 day';
  get diagnostics v_failures = row_count;
  return jsonb_build_object('expired', v_expired, 'claims_deleted', v_claims, 'failures_deleted', v_failures);
end $$;

revoke all on function public.device_claim_ttl() from public, anon, authenticated;
revoke all on function public.device_nonce_hash(text) from public, anon, authenticated;
revoke all on function public.notification_device_conflicts_internal(uuid, uuid, text, text) from public, anon, authenticated;
revoke all on function public.notification_device_register_internal(uuid, uuid, text, text, text, text, text, text, text) from public, anon, authenticated;
revoke all on function public.notification_device_lock_internal(uuid[], text, text) from public, anon, authenticated;
revoke all on function public.report_notification_device(uuid, text, jsonb, text, text, text) from public, anon;
revoke all on function public.confirm_device_claim(text) from public, anon;
revoke all on function public.unregister_notification_device(uuid) from public, anon;
grant execute on function public.report_notification_device(uuid, text, jsonb, text, text, text) to authenticated;
grant execute on function public.confirm_device_claim(text) to authenticated;
grant execute on function public.unregister_notification_device(uuid) to authenticated;
revoke all on function public.issue_device_claim_challenges(uuid) from public, anon, authenticated;
revoke all on function public.purge_device_claims(timestamptz) from public, anon, authenticated;
grant execute on function public.purge_device_claims(timestamptz) to service_role;
revoke all on function public.device_claim_resolve_trigger() from public, anon, authenticated;
grant execute on function public.issue_device_claim_challenges(uuid) to service_role;
comment on function public.report_notification_device(uuid, text, jsonb, text, text, text) is
  'Record this login''s device. A device id, token or endpoint held by another login moves only after confirm_device_claim.';
comment on function public.confirm_device_claim(text) is
  'Return the nonce from a verify-device push; moves the claimed device to the caller only if the caller made the claim.';
comment on function public.unregister_notification_device(uuid) is
  'Remove this login''s registration of a device (sign-out, account switch).';
comment on function public.issue_device_claim_challenges(uuid) is
  'Service role only: nonces for pending device claims, returned once, with the held device''s push target.';
