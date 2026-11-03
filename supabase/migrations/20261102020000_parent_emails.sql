-- CR-22 (issue #37, #218 A3): parent accountability emails. Replaces Design's local reference SQL
-- (scripts/local/proposals/cr22_parent_emails.sql, removed in the same change).
--
-- Ordered before CR-27 (20261102030000_practice_reminders.sql), which adds the 'reminders_off' kind to
-- parent_email_deliveries and reads it from a SQL function, so this table must exist first.
--
-- A scheduled sender (supabase/functions/send-weekly-digest) has no signed-in user. It uses the service role and reads
-- only through the service-only functions below, which run the existing dashboard RPCs AS each guardian
-- (request.jwt.claims and request.jwt.claim.sub set to that guardian for the call, then restored), so recipients and
-- numbers follow the parent dashboard's own permission checks and rules, with no second copy of them.
--
--   alert_preferences.weekly_digest    guardian opt-in per student (default off); the guardian writes their own row
--   parent_email_deliveries            one row per email sent: makes sending idempotent; each guardian reads their own
--                                      kind / period_key / sent_at, so the app says what was emailed, never inferred
--   weekly_digest_payload(week_start)  one row per opted-in guardian not yet sent that week, with each student's week
--   inactivity_alert_payload()         guardians whose enabled email alert threshold is reached, once per stretch
--   mark_parent_email_sent(...)        records a send before it is made; false if already recorded
--
-- Recipients are guardians who currently have view_progress in the student's household; archived students are left
-- out. Payloads carry the recipient's own address and name and the students that guardian may view, nothing else.
--
-- Differences from the reference SQL (all intentional):
-- * Impersonation also sets request.jwt.claim.sub (and restores both). auth.uid() reads claim.sub first on Supabase
--   and only claim.sub in the CI auth stub; setting request.jwt.claims alone could leave auth.uid() as the caller.
-- * weekly_digest_payload returns ONE row per guardian across all their households (the reference returned one row
--   per guardian and household; the sender keys each send on guardian + week, so a second household's summary was
--   silently never sent). time_zone is that of the guardian's earliest-created household among the students listed.
-- * inactivity_alert_payload uses each enabled EMAIL preference's own inactivity_days (student_inactivity(p_days)) for
--   that one student. The reference used student_inactivity() with no argument, whose threshold is the smallest
--   enabled preference on any channel, so a push-only alert (or a shorter push threshold) could trigger an email.
-- * The inactivity period_key is '<student id>:<last practice time in UTC, ISO 8601 with microseconds>' (or ':never').
--   The reference used timestamptz::text, which depends on the session TimeZone, so two runs with different settings
--   could key the same stretch differently and email twice. The first segment is still the student id.
-- * parent_email_deliveries keeps its records when an account is deleted (user_id on delete set null, a surrogate id
--   primary key and a unique (user_id, kind, period_key) in place of the composite primary key), for the 13-month
--   retention of email-sent records (owner decision #5, #294). The reference cascaded the delete.
-- Objects are altered or replaced in place.

alter table public.alert_preferences add column weekly_digest boolean not null default false;
grant insert (weekly_digest), update (weekly_digest) on public.alert_preferences to authenticated;
comment on column public.alert_preferences.weekly_digest is
  'CR-22: this guardian''s opt-in to the Monday weekly summary for this student (channel email).';

-- Retention (owner decision #5, #294): email-sent records are kept for 13 months. Deleting an account therefore
-- de-identifies its records (user_id becomes null) instead of deleting them; nothing here purges them.
create table public.parent_email_deliveries (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id) on delete set null,
  kind text not null constraint parent_email_deliveries_kind_check check (kind in ('weekly_digest', 'inactivity')),
  -- weekly_digest: the week's Monday (YYYY-MM-DD); inactivity: '<student id>:<last practice, UTC ISO>' or ':never'.
  period_key text not null check (length(period_key) between 1 and 120),
  sent_at timestamptz not null default now(),
  -- One record per recipient, kind and period: what makes sending idempotent.
  constraint parent_email_deliveries_once unique (user_id, kind, period_key)
);
alter table public.parent_email_deliveries enable row level security;
revoke all on public.parent_email_deliveries from anon, authenticated;
-- The sender records a send through mark_parent_email_sent and deletes the record itself when the provider refuses,
-- so the next run retries.
grant select, insert, delete on public.parent_email_deliveries to service_role;
grant select (kind, period_key, sent_at) on public.parent_email_deliveries to authenticated;
create policy own_email_deliveries on public.parent_email_deliveries for select to authenticated
  using (user_id = (select auth.uid()));
comment on table public.parent_email_deliveries is
  'CR-22: one row per parent email sent (user, kind, period). Each guardian reads their own; written by the service role.';

create function public.weekly_digest_payload(p_week_start date) returns setof jsonb
language plpgsql volatile security definer set search_path = '' as $$
declare r record; s record; v_claims text; v_sub text; v_students jsonb; v_tz text; v_prog jsonb; v_focus jsonb;
  v_check jsonb; v_days integer; v_last timestamptz; v_inact jsonb; v_student_tz text;
begin
  if p_week_start is null or extract(isodow from p_week_start) <> 1 then
    raise exception 'week_start must be a Monday' using errcode = '22023';
  end if;
  v_claims := current_setting('request.jwt.claims', true);
  v_sub := current_setting('request.jwt.claim.sub', true);
  for r in
    select u.id as user_id, u.email, p.display_name as guardian_name
    from auth.users u
    left join public.profiles p on p.id = u.id
    where u.email is not null
      and exists (select 1 from public.alert_preferences ap
        join public.students st on st.id = ap.student_id and st.archived_at is null
        join public.household_members m on m.household_id = st.household_id and m.user_id = ap.user_id
          and m.role = 'guardian' and m.can_view_progress
        where ap.user_id = u.id and ap.channel = 'email' and ap.weekly_digest)
      and not exists (select 1 from public.parent_email_deliveries d
        where d.user_id = u.id and d.kind = 'weekly_digest' and d.period_key = p_week_start::text)
    order by u.id
  loop
    -- From here until the restore below, auth.uid() is this guardian.
    perform set_config('request.jwt.claims', json_build_object('sub', r.user_id, 'role', 'authenticated')::text, true);
    perform set_config('request.jwt.claim.sub', r.user_id::text, true);
    v_students := '[]'::jsonb;
    v_tz := null;
    for s in
      select st.id, st.display_name, h.time_zone as household_tz
      from public.alert_preferences ap
      join public.students st on st.id = ap.student_id
      join public.households h on h.id = st.household_id
      where ap.user_id = r.user_id and ap.channel = 'email' and ap.weekly_digest
        and st.archived_at is null and public.can_view_student(st.id)
      order by h.created_at, h.id, st.display_name, st.id
    loop
      v_tz := coalesce(v_tz, s.household_tz);
      v_student_tz := public.student_time_zone(s.id);
      v_prog := public.student_weekly_progress(s.id, p_week_start);
      -- Practice days as on the dashboard strip: local dates with a submitted, non-benchmark answer.
      select count(distinct (a.submitted_at at time zone v_student_tz)::date) into v_days from public.practice_attempts a
      where a.student_id = s.id and a.benchmark_id is null and not a.skipped
        and a.submitted_at <@ public.local_week_bounds(p_week_start, v_student_tz);
      select max(a.submitted_at) into v_last from public.practice_attempts a
      where a.student_id = s.id and a.submitted_at is not null;
      -- Dashboard order: knowledge gaps (lowest accuracy first), then pacing (slowest first); at most three.
      select coalesce(jsonb_agg(q.f order by q.rn), '[]'::jsonb) into v_focus from (
        select jsonb_build_object('skill_name', k.name, 'section', e.section,
                 'reason', case when e.knowledge_weak then 'knowledge' else 'pacing' end,
                 'accuracy', e.accuracy, 'pacing_ratio', e.pacing_ratio) as f,
               row_number() over (order by e.knowledge_weak desc, case when e.knowledge_weak then e.accuracy end asc nulls last,
                                  e.pacing_ratio desc nulls last) as rn
        from public.student_skill_estimates(s.id) e join public.skills k on k.id = e.skill_id
        where e.knowledge_weak or e.pacing_weak) q
      where q.rn <= 3;
      v_check := null;
      select jsonb_build_object('kind', b.kind, 'completed_at', b.completed_at) into v_check from public.practice_benchmarks b
      where b.student_id = s.id and b.completed_at is not null order by b.completed_at desc limit 1;
      v_inact := null;
      select jsonb_build_object('threshold_days', i.threshold_days, 'days_inactive', i.days_inactive) into v_inact
      from public.student_inactivity() i where i.student_id = s.id;
      v_students := v_students || jsonb_build_array(jsonb_build_object(
        'student_id', s.id, 'student_name', s.display_name, 'week_start', p_week_start,
        'goal_questions', v_prog->'goal'->'target_questions',
        'questions_submitted', coalesce((v_prog->>'questions_submitted')::integer, 0),
        'days_practised', v_days, 'last_practice_at', v_last,
        'focus', v_focus, 'last_check', v_check, 'inactivity', v_inact));
    end loop;
    if jsonb_array_length(v_students) > 0 then
      return next jsonb_build_object('user_id', r.user_id, 'email', r.email, 'guardian_name', r.guardian_name,
        'time_zone', v_tz, 'students', v_students);
    end if;
  end loop;
  perform set_config('request.jwt.claims', coalesce(v_claims, ''), true);
  perform set_config('request.jwt.claim.sub', coalesce(v_sub, ''), true);
end $$;

-- The period key of an inactivity stretch: the student and their last practice time, independent of session settings.
create function public.inactivity_period_key(p_student uuid, p_last timestamptz) returns text
language sql stable set search_path = '' as $$
  select p_student::text || ':' || coalesce(to_char(p_last at time zone 'UTC', 'YYYY-MM-DD"T"HH24:MI:SS.US"Z"'), 'never')
$$;

create function public.inactivity_alert_payload() returns setof jsonb
language plpgsql volatile security definer set search_path = '' as $$
declare r record; i record; v_claims text; v_sub text; v_key text;
begin
  v_claims := current_setting('request.jwt.claims', true);
  v_sub := current_setting('request.jwt.claim.sub', true);
  for r in
    select ap.user_id, ap.student_id, ap.inactivity_days, u.email, p.display_name as guardian_name
    from public.alert_preferences ap
    join auth.users u on u.id = ap.user_id
    left join public.profiles p on p.id = u.id
    where ap.channel = 'email' and ap.enabled and u.email is not null
    order by ap.user_id, ap.student_id
  loop
    perform set_config('request.jwt.claims', json_build_object('sub', r.user_id, 'role', 'authenticated')::text, true);
    perform set_config('request.jwt.claim.sub', r.user_id::text, true);
    -- The dashboard's rule (view_progress in the student's household, not archived), at this email alert's threshold.
    for i in select * from public.student_inactivity(r.inactivity_days) x where x.student_id = r.student_id loop
      v_key := public.inactivity_period_key(i.student_id, i.last_submitted_at);
      if not exists (select 1 from public.parent_email_deliveries d
                     where d.user_id = r.user_id and d.kind = 'inactivity' and d.period_key = v_key) then
        return next jsonb_build_object('user_id', r.user_id, 'email', r.email, 'guardian_name', r.guardian_name,
          'student_id', i.student_id, 'student_name', i.display_name, 'threshold_days', i.threshold_days,
          'days_inactive', i.days_inactive, 'last_practice_at', i.last_submitted_at,
          'time_zone', public.student_time_zone(i.student_id), 'period_key', v_key);
      end if;
    end loop;
  end loop;
  perform set_config('request.jwt.claims', coalesce(v_claims, ''), true);
  perform set_config('request.jwt.claim.sub', coalesce(v_sub, ''), true);
end $$;

create function public.mark_parent_email_sent(p_user uuid, p_kind text, p_period_key text) returns boolean
language plpgsql volatile security definer set search_path = '' as $$
begin
  insert into public.parent_email_deliveries(user_id, kind, period_key) values (p_user, p_kind, p_period_key)
  on conflict do nothing;
  return found;
end $$;

revoke all on function public.inactivity_period_key(uuid, timestamptz) from public, anon, authenticated;
revoke all on function public.weekly_digest_payload(date) from public, anon, authenticated;
revoke all on function public.inactivity_alert_payload() from public, anon, authenticated;
revoke all on function public.mark_parent_email_sent(uuid, text, text) from public, anon, authenticated;
grant execute on function public.weekly_digest_payload(date) to service_role;
grant execute on function public.inactivity_alert_payload() to service_role;
grant execute on function public.mark_parent_email_sent(uuid, text, text) to service_role;
comment on function public.weekly_digest_payload(date) is
  'CR-22, service role only: one row per opted-in guardian not yet sent the week of p_week_start (a Monday).';
comment on function public.inactivity_alert_payload() is
  'CR-22, service role only: guardians whose enabled email inactivity alert is due, once per stretch without practice.';
comment on function public.mark_parent_email_sent(uuid, text, text) is
  'CR-22, service role only: record a parent email before sending it; false when it was already recorded.';
