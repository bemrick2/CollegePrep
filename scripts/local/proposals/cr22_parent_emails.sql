-- CR-22 (issue #37) REFERENCE IMPLEMENTATION, proposed by Design. Applied ONLY to the local disposable database by
-- scripts/local/live_stack.sh; it is not a migration. Research owns the schema and may adopt, change or replace it.
--
-- Parent accountability emails need data for guardians who are not signed in (a scheduled sender). Rather than a
-- second copy of the dashboard rules, these service-role-only functions run the existing dashboard RPCs AS each
-- guardian (request.jwt.claims set to that guardian for the call, then restored), so every permission check and
-- every number is the one the parent dashboard shows.
--
--   alert_preferences.weekly_digest     guardian opt-in, per student (default off)
--   parent_email_deliveries             one row per sent email; makes sending idempotent
--   weekly_digest_payload(week_start)   recipients who opted in, with each student's week
--   inactivity_alert_payload()          guardians whose alert threshold is reached, not yet alerted this stretch
--   mark_parent_email_sent(...)         records a send; false if it was already recorded

alter table public.alert_preferences add column weekly_digest boolean not null default false;
grant insert (weekly_digest), update (weekly_digest) on public.alert_preferences to authenticated;

create table public.parent_email_deliveries (
  user_id uuid not null references auth.users(id) on delete cascade,
  kind text not null check (kind in ('weekly_digest', 'inactivity')),
  -- weekly_digest: the week's Monday; inactivity: student id + last practice time (once per stretch without practice)
  period_key text not null check (length(period_key) between 1 and 120),
  sent_at timestamptz not null default now(),
  primary key (user_id, kind, period_key)
);
alter table public.parent_email_deliveries enable row level security;
revoke all on public.parent_email_deliveries from anon, authenticated;
grant select, insert, delete on public.parent_email_deliveries to service_role;

create function public.weekly_digest_payload(p_week_start date) returns setof jsonb
language plpgsql volatile security definer set search_path = '' as $$
declare r record; v_old text; v_students jsonb; s record; v_prog jsonb; v_focus jsonb; v_check jsonb; v_days int;
  v_last timestamptz; v_inact jsonb; v_tz text;
begin
  if p_week_start is null or extract(isodow from p_week_start) <> 1 then
    raise exception 'week_start must be a Monday' using errcode = '22023';
  end if;
  v_old := current_setting('request.jwt.claims', true);
  for r in
    select u.id as user_id, u.email, p.display_name as guardian_name, h.time_zone, h.id as household_id
    from public.alert_preferences ap
    join auth.users u on u.id = ap.user_id
    join public.students st on st.id = ap.student_id and st.archived_at is null
    join public.households h on h.id = st.household_id
    join public.household_members m on m.household_id = h.id and m.user_id = ap.user_id and m.role = 'guardian' and m.can_view_progress
    left join public.profiles p on p.id = u.id
    where ap.channel = 'email' and ap.weekly_digest and u.email is not null
      and not exists (select 1 from public.parent_email_deliveries d where d.user_id = u.id and d.kind = 'weekly_digest' and d.period_key = p_week_start::text)
    group by u.id, u.email, p.display_name, h.time_zone, h.id
  loop
    perform set_config('request.jwt.claims', json_build_object('sub', r.user_id, 'role', 'authenticated')::text, true);
    v_students := '[]'::jsonb;
    for s in
      select st.id, st.display_name from public.alert_preferences ap join public.students st on st.id = ap.student_id
      where ap.user_id = r.user_id and ap.channel = 'email' and ap.weekly_digest and st.household_id = r.household_id
        and st.archived_at is null and public.can_view_student(st.id)
      order by st.display_name
    loop
      v_tz := public.student_time_zone(s.id);
      v_prog := public.student_weekly_progress(s.id, p_week_start);
      -- Practice days as on the dashboard strip: local dates with a submitted, non-benchmark answer.
      select count(distinct (a.submitted_at at time zone v_tz)::date) into v_days from public.practice_attempts a
      where a.student_id = s.id and a.benchmark_id is null and not a.skipped
        and a.submitted_at <@ public.local_week_bounds(p_week_start, v_tz);
      select max(a.submitted_at) into v_last from public.practice_attempts a where a.student_id = s.id and a.submitted_at is not null;
      -- Dashboard order: knowledge gaps (lowest accuracy first), then pacing (slowest first); at most three.
      select coalesce(jsonb_agg(f order by rn), '[]'::jsonb) into v_focus from (
        select jsonb_build_object('skill_name', k.name, 'section', e.section,
                 'reason', case when e.knowledge_weak then 'knowledge' else 'pacing' end,
                 'accuracy', e.accuracy, 'pacing_ratio', e.pacing_ratio) f,
               row_number() over (order by e.knowledge_weak desc, case when e.knowledge_weak then e.accuracy end asc nulls last,
                                  e.pacing_ratio desc nulls last) rn
        from public.student_skill_estimates(s.id) e join public.skills k on k.id = e.skill_id
        where e.knowledge_weak or e.pacing_weak) q
      where rn <= 3;
      select jsonb_build_object('kind', b.kind, 'completed_at', b.completed_at) into v_check from public.practice_benchmarks b
      where b.student_id = s.id and b.completed_at is not null order by b.completed_at desc limit 1;
      select jsonb_build_object('threshold_days', i.threshold_days, 'days_inactive', i.days_inactive) into v_inact
      from public.student_inactivity() i where i.student_id = s.id;
      v_students := v_students || jsonb_build_array(jsonb_build_object(
        'student_id', s.id, 'student_name', s.display_name, 'week_start', p_week_start,
        'goal_questions', v_prog->'goal'->'target_questions', 'questions_submitted', coalesce((v_prog->>'questions_submitted')::int, 0),
        'days_practised', v_days, 'last_practice_at', v_last,
        'focus', v_focus,
        'last_check', v_check, 'inactivity', v_inact));
    end loop;
    if jsonb_array_length(v_students) > 0 then
      return next jsonb_build_object('user_id', r.user_id, 'email', r.email, 'guardian_name', r.guardian_name,
        'time_zone', r.time_zone, 'students', v_students);
    end if;
  end loop;
  perform set_config('request.jwt.claims', coalesce(v_old, ''), true);
end $$;

create function public.inactivity_alert_payload() returns setof jsonb
language plpgsql volatile security definer set search_path = '' as $$
declare r record; v_old text; i record;
begin
  v_old := current_setting('request.jwt.claims', true);
  for r in
    select distinct ap.user_id, u.email, p.display_name as guardian_name from public.alert_preferences ap
    join auth.users u on u.id = ap.user_id left join public.profiles p on p.id = u.id
    where ap.channel = 'email' and ap.enabled and u.email is not null
  loop
    perform set_config('request.jwt.claims', json_build_object('sub', r.user_id, 'role', 'authenticated')::text, true);
    for i in select * from public.student_inactivity() loop
      if not exists (select 1 from public.parent_email_deliveries d where d.user_id = r.user_id and d.kind = 'inactivity'
                     and d.period_key = i.student_id::text || ':' || coalesce(i.last_submitted_at::text, 'never')) then
        return next jsonb_build_object('user_id', r.user_id, 'email', r.email, 'guardian_name', r.guardian_name,
          'student_id', i.student_id, 'student_name', i.display_name, 'threshold_days', i.threshold_days,
          'days_inactive', i.days_inactive, 'last_practice_at', i.last_submitted_at,
          'time_zone', public.student_time_zone(i.student_id),
          'period_key', i.student_id::text || ':' || coalesce(i.last_submitted_at::text, 'never'));
      end if;
    end loop;
  end loop;
  perform set_config('request.jwt.claims', coalesce(v_old, ''), true);
end $$;

create function public.mark_parent_email_sent(p_user uuid, p_kind text, p_period_key text) returns boolean
language plpgsql volatile security definer set search_path = '' as $$
begin
  insert into public.parent_email_deliveries(user_id, kind, period_key) values (p_user, p_kind, p_period_key) on conflict do nothing;
  return found;
end $$;

revoke all on function public.weekly_digest_payload(date) from public, anon, authenticated;
revoke all on function public.inactivity_alert_payload() from public, anon, authenticated;
revoke all on function public.mark_parent_email_sent(uuid, text, text) from public, anon, authenticated;
grant execute on function public.weekly_digest_payload(date) to service_role;
grant execute on function public.inactivity_alert_payload() to service_role;
grant execute on function public.mark_parent_email_sent(uuid, text, text) to service_role;
