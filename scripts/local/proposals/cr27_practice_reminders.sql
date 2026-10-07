-- CR-27 (issue #37) REFERENCE IMPLEMENTATION, proposed by Design. Applied ONLY to the local disposable database by
-- scripts/local/live_stack.sh, after CR-22; it is not a migration. Research owns the schema and may adopt, change or
-- replace it.
--
-- Practice reminders (web push) and the guardian notice when a linked student turns them off.
--
--   practice_reminder_settings      the family's reminder times, days, quiet and school hours, limits; snooze
--   practice_reminder_changes       every on/off change, who made it, and whether guardians are to be told
--   notification_devices            each signed-in browser/device: permission as last seen on app open, push keys
--   practice_reminder_deliveries    one row per reminder (claimed before sending: never two per reminder, whatever the
--                                   number of devices or overlapping sender runs) and what the student did with it
--
-- Rules the server enforces:
--   - settings: readable by anyone who can view the student; writable by a guardian with set_goals or by the
--     student's own login (the family chooses together);
--   - a snooze ("Remind me later") is the student's own and never notifies anyone;
--   - when the student's own login turns reminders OFF, and the student belongs to a household and isn't independent,
--     the change is flagged for guardians: one email per guardian with view permission, at most one per student
--     per 24 hours (later changes are still recorded and shown in the app);
--   - an independent or household-less student is never reported to anyone;
--   - device permission is what the app saw the last time it opened on that device. Turning notifications off in
--     phone settings is not visible until then, so nothing here claims immediate detection.

create table public.practice_reminder_settings (
  student_id uuid primary key references public.students(id) on delete cascade,
  enabled boolean not null default false,
  times text[] not null default array['16:30'],
  days smallint[] not null default array[1,2,3,4,5,6,7]::smallint[],
  quiet_start text not null default '21:00',
  quiet_end text not null default '07:00',
  school_days smallint[] not null default array[1,2,3,4,5]::smallint[],
  school_start text default '08:00',
  school_end text default '15:00',
  max_per_day smallint not null default 1 check (max_per_day between 1 and 3),
  max_per_week smallint not null default 5 check (max_per_week between 1 and 14),
  snoozed_until timestamptz,
  updated_by uuid references auth.users(id) on delete set null,
  updated_at timestamptz not null default now(),
  check (cardinality(times) between 1 and 3),
  check (cardinality(days) between 1 and 7 and days <@ array[1,2,3,4,5,6,7]::smallint[]),
  check (school_days <@ array[1,2,3,4,5,6,7]::smallint[]),
  check (quiet_start ~ '^([01]\d|2[0-3]):[0-5]\d$' and quiet_end ~ '^([01]\d|2[0-3]):[0-5]\d$'),
  check ((school_start is null) = (school_end is null)),
  check (school_start is null or (school_start ~ '^([01]\d|2[0-3]):[0-5]\d$' and school_end ~ '^([01]\d|2[0-3]):[0-5]\d$'))
);

create function public.reminder_times_valid(p_times text[]) returns boolean
language sql immutable set search_path = '' as $$
  select coalesce(bool_and(t ~ '^([01]\d|2[0-3]):(00|15|30|45)$'), false) and count(*) = count(distinct t)
  from unnest(p_times) t
$$;
alter table public.practice_reminder_settings add constraint practice_reminder_times_valid check (public.reminder_times_valid(times));

alter table public.practice_reminder_settings enable row level security;
revoke all on public.practice_reminder_settings from anon, authenticated;
grant select on public.practice_reminder_settings to authenticated;
grant all on public.practice_reminder_settings to service_role;
create policy reminder_settings_read on public.practice_reminder_settings for select to authenticated using (public.can_view_student(student_id));

create table public.practice_reminder_changes (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references public.students(id) on delete cascade,
  enabled boolean not null,
  changed_by uuid references auth.users(id) on delete set null,
  changed_by_role text not null check (changed_by_role in ('student', 'guardian')),
  changed_at timestamptz not null default now(),
  notify_guardians boolean not null default false
);
create index practice_reminder_changes_student_idx on public.practice_reminder_changes(student_id, changed_at desc);
alter table public.practice_reminder_changes enable row level security;
revoke all on public.practice_reminder_changes from anon, authenticated;
grant select on public.practice_reminder_changes to authenticated;
grant all on public.practice_reminder_changes to service_role;
create policy reminder_changes_read on public.practice_reminder_changes for select to authenticated using (public.can_view_student(student_id));

create table public.notification_devices (
  id uuid primary key,                        -- generated by the app, kept in that browser
  user_id uuid not null references auth.users(id) on delete cascade,
  permission text not null check (permission in ('granted', 'denied', 'default', 'unsupported')),
  platform text check (platform in ('ios', 'android', 'desktop', 'other')),
  -- webpush: a browser (endpoint + keys); fcm: the native iPhone/Android app (FCM registration token).
  channel text not null default 'webpush' check (channel in ('webpush', 'fcm')),
  push_token text check (push_token is null or length(push_token) between 20 and 4096),
  endpoint text check (endpoint is null or (endpoint ~ '^https://' and length(endpoint) <= 2048)),
  p256dh text check (p256dh is null or length(p256dh) <= 200),
  auth_secret text check (auth_secret is null or length(auth_secret) <= 100),
  checked_at timestamptz not null default now(),
  gone_at timestamptz,                         -- the push service said the subscription no longer exists
  created_at timestamptz not null default now(),
  check ((endpoint is null) = (p256dh is null) and (endpoint is null) = (auth_secret is null)),
  check (channel = 'webpush' or endpoint is null),
  check (channel = 'fcm' or push_token is null)
);
create index notification_devices_user_idx on public.notification_devices(user_id);
alter table public.notification_devices enable row level security;
revoke all on public.notification_devices from anon, authenticated;
grant all on public.notification_devices to service_role;
-- No direct client access: devices are written through report_notification_device and summarized without keys.

create table public.practice_reminder_deliveries (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references public.students(id) on delete cascade,
  device_id uuid references public.notification_devices(id) on delete set null,
  slot text not null check (length(slot) <= 10),
  -- One reminder = one key (local date + slot, or the snooze's end). At most one claimed-or-sent row per key.
  reminder_key text not null check (length(reminder_key) <= 80),
  channel text check (channel in ('webpush', 'fcm')),
  status text not null check (status in ('claimed', 'sent', 'failed', 'gone')),
  sent_at timestamptz not null default now(),
  opened_at timestamptz,
  snoozed_at timestamptz
);
create index practice_reminder_deliveries_student_idx on public.practice_reminder_deliveries(student_id, sent_at desc);
create unique index practice_reminder_once on public.practice_reminder_deliveries(student_id, reminder_key) where status in ('claimed', 'sent');
alter table public.practice_reminder_deliveries enable row level security;
revoke all on public.practice_reminder_deliveries from anon, authenticated;
grant select (id, student_id, slot, channel, status, sent_at, opened_at, snoozed_at) on public.practice_reminder_deliveries to authenticated;
grant all on public.practice_reminder_deliveries to service_role;
create policy reminder_deliveries_read on public.practice_reminder_deliveries for select to authenticated using (public.can_view_student(student_id));

-- CR-22's delivery record also covers the reminders-off notice (period_key = the change id).
alter table public.parent_email_deliveries drop constraint parent_email_deliveries_kind_check;
alter table public.parent_email_deliveries add constraint parent_email_deliveries_kind_check check (kind in ('weekly_digest', 'inactivity', 'reminders_off'));

-- ---------------------------------------------------------------------------------------------------------------
-- Client RPCs
-- ---------------------------------------------------------------------------------------------------------------

create function public.set_practice_reminders(p_student uuid, p_settings jsonb) returns jsonb
language plpgsql volatile security definer set search_path = '' as $$
declare v_student public.students; v_old public.practice_reminder_settings; v_role text; v_enabled boolean; v_notify boolean := false;
begin
  select * into v_student from public.students where id = p_student and archived_at is null;
  if not found then raise exception 'Not allowed to change reminders for this student' using errcode = '42501'; end if;
  if v_student.linked_user_id = auth.uid() then v_role := 'student';
  elsif public.has_household_permission(v_student.household_id, 'set_goals') then v_role := 'guardian';
  else raise exception 'Not allowed to change reminders for this student' using errcode = '42501';
  end if;
  select * into v_old from public.practice_reminder_settings where student_id = p_student;
  v_enabled := coalesce((p_settings->>'enabled')::boolean, v_old.enabled, false);

  insert into public.practice_reminder_settings as s (student_id, enabled, times, days, quiet_start, quiet_end, school_days,
      school_start, school_end, max_per_day, max_per_week, updated_by, updated_at)
  values (p_student, v_enabled,
    coalesce(array(select jsonb_array_elements_text(p_settings->'times')), array['16:30']),
    coalesce(array(select (jsonb_array_elements_text(p_settings->'days'))::smallint), array[1,2,3,4,5,6,7]::smallint[]),
    coalesce(p_settings->>'quiet_start', '21:00'), coalesce(p_settings->>'quiet_end', '07:00'),
    coalesce(array(select (jsonb_array_elements_text(p_settings->'school_days'))::smallint), array[1,2,3,4,5]::smallint[]),
    case when p_settings ? 'school_start' then p_settings->>'school_start' else '08:00' end,
    case when p_settings ? 'school_end' then p_settings->>'school_end' else '15:00' end,
    coalesce((p_settings->>'max_per_day')::smallint, 1), coalesce((p_settings->>'max_per_week')::smallint, 5),
    auth.uid(), now())
  on conflict (student_id) do update set enabled = excluded.enabled, times = excluded.times, days = excluded.days,
    quiet_start = excluded.quiet_start, quiet_end = excluded.quiet_end, school_days = excluded.school_days,
    school_start = excluded.school_start, school_end = excluded.school_end, max_per_day = excluded.max_per_day,
    max_per_week = excluded.max_per_week, updated_by = excluded.updated_by, updated_at = excluded.updated_at,
    -- Turning reminders back on (or changing them) ends any snooze.
    snoozed_until = case when excluded.enabled and not s.enabled then null else s.snoozed_until end;

  if v_old.student_id is null or v_old.enabled is distinct from v_enabled then
    -- Only the student's own login turning reminders off, in a household, not independent, tells guardians; at most
    -- once per student per 24 hours.
    v_notify := v_role = 'student' and not v_enabled and coalesce(v_old.enabled, false)
      and v_student.household_id is not null and not v_student.is_independent
      and not exists (select 1 from public.practice_reminder_changes c where c.student_id = p_student and c.notify_guardians
                      and c.changed_at > now() - interval '24 hours');
    if v_old.student_id is not null or v_enabled then
      insert into public.practice_reminder_changes(student_id, enabled, changed_by, changed_by_role, notify_guardians)
      values (p_student, v_enabled, auth.uid(), v_role, v_notify);
    end if;
  end if;
  return jsonb_build_object('enabled', v_enabled, 'guardians_notified', v_notify);
end $$;

create function public.snooze_practice_reminders(p_student uuid, p_minutes integer default 60) returns timestamptz
language plpgsql volatile security definer set search_path = '' as $$
declare v timestamptz;
begin
  perform public.require_linked_student(p_student);
  if p_minutes is null or p_minutes not between 15 and 1440 then raise exception 'Snooze is 15 minutes to 24 hours' using errcode = '22023'; end if;
  update public.practice_reminder_settings set snoozed_until = now() + make_interval(mins => p_minutes)
  where student_id = p_student and enabled returning snoozed_until into v;
  if not found then raise exception 'Reminders are off' using errcode = '22023'; end if;
  update public.practice_reminder_deliveries set snoozed_at = now()
  where id = (select id from public.practice_reminder_deliveries where student_id = p_student order by sent_at desc limit 1);
  return v;
end $$;

create function public.report_notification_device(p_device uuid, p_permission text, p_subscription jsonb default null, p_platform text default null,
  p_channel text default 'webpush', p_token text default null)
returns void language plpgsql volatile security definer set search_path = '' as $$
declare v_owner uuid; v_granted boolean := p_permission = 'granted';
begin
  if auth.uid() is null then raise exception 'Sign in first' using errcode = '42501'; end if;
  select user_id into v_owner from public.notification_devices where id = p_device;
  if v_owner is not null and v_owner <> auth.uid() then raise exception 'Not your device' using errcode = '42501'; end if;
  -- A native token belongs to one install: if another login reported it before (shared phone), it moves here.
  if p_channel = 'fcm' and p_token is not null then
    delete from public.notification_devices where push_token = p_token and id <> p_device;
  end if;
  insert into public.notification_devices as d (id, user_id, permission, platform, channel, push_token, endpoint, p256dh, auth_secret, checked_at, gone_at)
  values (p_device, auth.uid(), p_permission, p_platform, coalesce(p_channel, 'webpush'),
          case when v_granted and p_channel = 'fcm' then p_token end,
          case when v_granted and coalesce(p_channel, 'webpush') = 'webpush' then p_subscription->>'endpoint' end,
          case when v_granted and coalesce(p_channel, 'webpush') = 'webpush' then p_subscription->'keys'->>'p256dh' end,
          case when v_granted and coalesce(p_channel, 'webpush') = 'webpush' then p_subscription->'keys'->>'auth' end, now(), null)
  on conflict (id) do update set permission = excluded.permission, platform = coalesce(excluded.platform, d.platform),
    channel = excluded.channel, push_token = excluded.push_token,
    endpoint = excluded.endpoint, p256dh = excluded.p256dh, auth_secret = excluded.auth_secret, checked_at = now(),
    gone_at = case when excluded.endpoint is distinct from d.endpoint or excluded.push_token is distinct from d.push_token then null else d.gone_at end;
end $$;

-- What a family may see about a student's devices: permission as last seen, never endpoints or keys.
create function public.student_notification_devices(p_student uuid)
returns table (device_id uuid, permission text, platform text, can_receive boolean, checked_at timestamptz)
language plpgsql stable security definer set search_path = '' as $$
begin
  if not public.can_view_student(p_student) then raise exception 'Not allowed to view this student' using errcode = '42501'; end if;
  return query select d.id, d.permission, d.platform, d.permission = 'granted' and (d.endpoint is not null or d.push_token is not null) and d.gone_at is null, d.checked_at
    from public.notification_devices d join public.students s on s.linked_user_id = d.user_id
    where s.id = p_student order by d.checked_at desc;
end $$;

-- On/off history with, for the calling guardian, whether the notice was actually emailed to them.
create function public.practice_reminder_history(p_student uuid)
returns table (id uuid, enabled boolean, changed_by_role text, changed_at timestamptz, notify_guardians boolean, emailed_to_me_at timestamptz)
language plpgsql stable security definer set search_path = '' as $$
begin
  if not public.can_view_student(p_student) then raise exception 'Not allowed to view this student' using errcode = '42501'; end if;
  return query select c.id, c.enabled, c.changed_by_role, c.changed_at, c.notify_guardians,
      (select d.sent_at from public.parent_email_deliveries d where d.user_id = auth.uid() and d.kind = 'reminders_off' and d.period_key = c.id::text)
    from public.practice_reminder_changes c where c.student_id = p_student order by c.changed_at desc limit 20;
end $$;

create function public.mark_practice_reminder_opened(p_delivery uuid) returns void
language plpgsql volatile security definer set search_path = '' as $$
declare v uuid;
begin
  select student_id into v from public.practice_reminder_deliveries where id = p_delivery;
  if v is null then return; end if;
  perform public.require_linked_student(v);
  update public.practice_reminder_deliveries set opened_at = coalesce(opened_at, now()) where id = p_delivery;
end $$;

-- ---------------------------------------------------------------------------------------------------------------
-- Service-only: the scheduled push sender, the notification "Remind me later" action, the guardian notice email
-- ---------------------------------------------------------------------------------------------------------------

create function public.practice_reminder_candidates(p_now timestamptz default now()) returns setof jsonb
language plpgsql stable security definer set search_path = '' as $$
declare r record; v_tz text; v_today date; v_monday date; v_week tstzrange; v_goal integer; v_week_done integer;
  v_today_done integer; v_sent_today integer; v_sent_week integer; v_last timestamptz; v_devices jsonb;
begin
  for r in
    select s.*, st.linked_user_id from public.practice_reminder_settings s
    join public.students st on st.id = s.student_id and st.archived_at is null and st.linked_user_id is not null
    where s.enabled
  loop
    select coalesce(jsonb_agg(jsonb_build_object('id', d.id, 'channel', d.channel, 'checkedAt', d.checked_at, 'endpoint', d.endpoint,
             'p256dh', d.p256dh, 'auth', d.auth_secret, 'token', d.push_token) order by d.checked_at desc), '[]'::jsonb)
      into v_devices from public.notification_devices d
      where d.user_id = r.linked_user_id and d.permission = 'granted' and d.gone_at is null
        and (d.endpoint is not null or d.push_token is not null);
    continue when jsonb_array_length(v_devices) = 0;
    v_tz := public.student_time_zone(r.student_id);
    v_today := (p_now at time zone v_tz)::date;
    v_monday := v_today - (extract(isodow from v_today)::int - 1);
    v_week := public.local_week_bounds(v_monday, v_tz);
    select g.target_questions into v_goal from public.weekly_practice_goals g
      where g.student_id = r.student_id and g.week_start = v_monday and g.subject is null;
    select count(*) into v_week_done from public.practice_attempts a
      where a.student_id = r.student_id and not a.skipped and a.submitted_at <@ v_week;
    select count(*) into v_today_done from public.practice_attempts a
      where a.student_id = r.student_id and not a.skipped and a.benchmark_id is null and a.submitted_at is not null
        and (a.submitted_at at time zone v_tz)::date = v_today;
    select count(distinct date_trunc('minute', d.sent_at)) filter (where (d.sent_at at time zone v_tz)::date = v_today),
           count(distinct date_trunc('minute', d.sent_at)) filter (where d.sent_at <@ v_week), max(d.sent_at)
      into v_sent_today, v_sent_week, v_last
      from public.practice_reminder_deliveries d where d.student_id = r.student_id and d.status = 'sent';
    return next jsonb_build_object(
      'student_id', r.student_id, 'time_zone', v_tz,
      'settings', jsonb_build_object('enabled', r.enabled, 'times', to_jsonb(r.times), 'days', to_jsonb(r.days),
        'quietStart', r.quiet_start, 'quietEnd', r.quiet_end, 'schoolDays', to_jsonb(r.school_days),
        'schoolStart', r.school_start, 'schoolEnd', r.school_end, 'maxPerDay', r.max_per_day, 'maxPerWeek', r.max_per_week,
        'snoozedUntil', r.snoozed_until),
      'context', jsonb_build_object('sentToday', v_sent_today, 'sentThisWeek', v_sent_week, 'lastSentAt', v_last,
        'practisedToday', v_today_done, 'weekDone', v_week_done, 'weeklyGoal', v_goal),
      'devices', v_devices);
  end loop;
end $$;

-- Claim a reminder before sending: false when this key was already claimed or sent (another run, a retry).
create function public.claim_practice_reminder(p_id uuid, p_student uuid, p_key text, p_slot text, p_at timestamptz default now())
returns boolean language plpgsql volatile security definer set search_path = '' as $$
begin
  insert into public.practice_reminder_deliveries(id, student_id, slot, reminder_key, status, sent_at)
  values (p_id, p_student, p_slot, p_key, 'claimed', p_at) on conflict do nothing;
  return found;
end $$;

-- The outcome on the one device tried last. 'gone' retires that device; a sent snooze is used up.
create function public.finish_practice_reminder(p_id uuid, p_device uuid, p_channel text, p_status text)
returns void language plpgsql volatile security definer set search_path = '' as $$
declare v public.practice_reminder_deliveries;
begin
  update public.practice_reminder_deliveries set device_id = p_device, channel = p_channel, status = p_status
  where id = p_id and status = 'claimed' returning * into v;
  if v.id is null then return; end if;
  if p_status = 'sent' and v.slot = 'snooze' then
    update public.practice_reminder_settings set snoozed_until = null where student_id = v.student_id;
  end if;
end $$;

create function public.retire_notification_device(p_device uuid) returns void
language sql volatile security definer set search_path = '' as $$
  update public.notification_devices set gone_at = now() where id = p_device
$$;

-- The notification's "Remind me later" button, after the action endpoint has verified its signed token.
create function public.snooze_practice_reminder_delivery(p_delivery uuid, p_minutes integer default 60) returns timestamptz
language plpgsql volatile security definer set search_path = '' as $$
declare v_student uuid; v timestamptz;
begin
  update public.practice_reminder_deliveries set snoozed_at = coalesce(snoozed_at, now()) where id = p_delivery and snoozed_at is null
  returning student_id into v_student;
  if v_student is null then return null; end if;  -- unknown or already used
  update public.practice_reminder_settings set snoozed_until = now() + make_interval(mins => p_minutes)
  where student_id = v_student and enabled returning snoozed_until into v;
  return v;
end $$;

-- Guardians to tell, one email each per flagged change, until a delivery is recorded.
create function public.reminder_opt_out_payload() returns setof jsonb
language sql stable security definer set search_path = '' as $$
  select jsonb_build_object('user_id', u.id, 'email', u.email, 'guardian_name', p.display_name,
    'student_id', st.id, 'student_name', st.display_name, 'changed_at', c.changed_at,
    'time_zone', public.student_time_zone(st.id), 'period_key', c.id::text)
  from public.practice_reminder_changes c
  join public.students st on st.id = c.student_id and st.archived_at is null and not st.is_independent
  join public.household_members m on m.household_id = st.household_id and m.role = 'guardian' and m.can_view_progress
  join auth.users u on u.id = m.user_id and u.email is not null
  left join public.profiles p on p.id = u.id
  where c.notify_guardians and not c.enabled and c.changed_at > now() - interval '14 days'
    and not exists (select 1 from public.parent_email_deliveries d where d.user_id = u.id and d.kind = 'reminders_off' and d.period_key = c.id::text)
$$;

revoke all on function public.set_practice_reminders(uuid, jsonb) from public, anon;
revoke all on function public.snooze_practice_reminders(uuid, integer) from public, anon;
revoke all on function public.report_notification_device(uuid, text, jsonb, text, text, text) from public, anon;
revoke all on function public.student_notification_devices(uuid) from public, anon;
revoke all on function public.practice_reminder_history(uuid) from public, anon;
revoke all on function public.mark_practice_reminder_opened(uuid) from public, anon;
grant execute on function public.set_practice_reminders(uuid, jsonb) to authenticated;
grant execute on function public.snooze_practice_reminders(uuid, integer) to authenticated;
grant execute on function public.report_notification_device(uuid, text, jsonb, text, text, text) to authenticated;
grant execute on function public.student_notification_devices(uuid) to authenticated;
grant execute on function public.practice_reminder_history(uuid) to authenticated;
grant execute on function public.mark_practice_reminder_opened(uuid) to authenticated;
revoke all on function public.practice_reminder_candidates(timestamptz) from public, anon, authenticated;
revoke all on function public.claim_practice_reminder(uuid, uuid, text, text, timestamptz) from public, anon, authenticated;
revoke all on function public.finish_practice_reminder(uuid, uuid, text, text) from public, anon, authenticated;
revoke all on function public.retire_notification_device(uuid) from public, anon, authenticated;
revoke all on function public.snooze_practice_reminder_delivery(uuid, integer) from public, anon, authenticated;
revoke all on function public.reminder_opt_out_payload() from public, anon, authenticated;
grant execute on function public.practice_reminder_candidates(timestamptz) to service_role;
grant execute on function public.claim_practice_reminder(uuid, uuid, text, text, timestamptz) to service_role;
grant execute on function public.finish_practice_reminder(uuid, uuid, text, text) to service_role;
grant execute on function public.retire_notification_device(uuid) to service_role;
grant execute on function public.snooze_practice_reminder_delivery(uuid, integer) to service_role;
grant execute on function public.reminder_opt_out_payload() to service_role;
