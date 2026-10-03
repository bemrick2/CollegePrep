-- CR-2 and CR-6 (issue #37): benchmark sessions over ordinary attempts, and a diversified, difficulty-aware
-- recommender. Benchmarks run 20-40 minutes, so they group attempts directly rather than through a 5-15 minute
-- practice session. See docs/HOUSEHOLD_PRACTICE.md.

create table public.practice_benchmarks (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references public.students(id) on delete cascade,
  kind text not null check (kind in ('initial','mini','full')),
  exam_version_id uuid references public.exam_versions(id),
  started_at timestamptz not null default now(),
  completed_at timestamptz check (completed_at >= started_at),
  metrics jsonb check (metrics is null or jsonb_typeof(metrics) = 'object')
);
create index practice_benchmarks_student_idx on public.practice_benchmarks(student_id, started_at desc);
create index practice_benchmarks_exam_version_idx on public.practice_benchmarks(exam_version_id);

alter table public.practice_attempts add column benchmark_id uuid references public.practice_benchmarks(id) on delete set null;
create index practice_attempts_benchmark_idx on public.practice_attempts(benchmark_id) where benchmark_id is not null;

alter table public.practice_benchmarks enable row level security;
revoke all on public.practice_benchmarks from anon, authenticated;
grant select, insert, update, delete on public.practice_benchmarks to service_role;
grant select on public.practice_benchmarks to authenticated;
create policy student_data_read on public.practice_benchmarks for select to authenticated using (public.can_view_student(student_id));

create function public.start_benchmark(p_student uuid, p_kind text, p_exam_version uuid default null) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_id uuid;
begin
  perform public.require_linked_student(p_student);
  if p_kind is null or p_kind not in ('initial','mini','full') then
    raise exception 'Benchmark kind must be initial, mini or full' using errcode = '22023';
  end if;
  if p_exam_version is not null and not exists (select 1 from public.exam_versions e where e.id = p_exam_version) then
    raise exception 'Unknown exam version' using errcode = '22023';
  end if;
  insert into public.practice_benchmarks(student_id, kind, exam_version_id) values (p_student, p_kind, p_exam_version)
  returning id into v_id;
  return v_id;
end $$;

-- start_practice_attempt gains p_benchmark (an open benchmark of the same student); a session and a benchmark
-- are alternatives. Recreated because the signature changes.
drop function public.start_practice_attempt(uuid, uuid, uuid);
create function public.start_practice_attempt(p_student uuid, p_question uuid, p_session uuid default null,
  p_benchmark uuid default null) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_id uuid;
begin
  -- Locking the student row serialises attempt numbering.
  perform 1 from public.students s where s.id = p_student and s.linked_user_id = auth.uid() and s.archived_at is null for update;
  if not found then raise exception 'Only the student''s own login can practise' using errcode = '42501'; end if;
  if not exists (select 1 from public.practice_questions q where q.id = p_question and q.status = 'published') then
    raise exception 'Question is not available' using errcode = '22023';
  end if;
  if p_session is not null and p_benchmark is not null then
    raise exception 'An attempt belongs to a session or a benchmark, not both' using errcode = '22023';
  end if;
  if p_session is not null and not exists (select 1 from public.practice_sessions ps
      where ps.id = p_session and ps.student_id = p_student and ps.ended_at is null) then
    raise exception 'Session is not an open session of this student' using errcode = '22023';
  end if;
  if p_benchmark is not null and not exists (select 1 from public.practice_benchmarks b
      where b.id = p_benchmark and b.student_id = p_student and b.completed_at is null) then
    raise exception 'Benchmark is not an open benchmark of this student' using errcode = '22023';
  end if;
  insert into public.practice_attempts(session_id, benchmark_id, student_id, question_id, presented_at, attempt_number)
  select p_session, p_benchmark, p_student, p_question, now(), count(*) + 1
  from public.practice_attempts a where a.student_id = p_student and a.question_id = p_question
  returning id into v_id;
  insert into public.practice_attempt_events(attempt_id, student_id, kind) values (v_id, p_student, 'presented');
  return v_id;
end $$;

-- Server-computed summary over the benchmark's attempts:
--   by_section: submitted, correct, accuracy, median pacing ratio (elapsed / expected time)
--   skips (final skips), returns and answer_changes (event log), unsubmitted (presented, never submitted)
--   calibration: accuracy by confidence (1-3) and the share of high-confidence answers that were wrong
--   traps: how often a wrong answer chose a distractor tagged with each trap type
create function public.benchmark_metrics_internal(p_benchmark uuid) returns jsonb
language sql stable set search_path = '' as $$
  with a as (
    select a.*, q.section, q.expected_time_seconds from public.practice_attempts a
    join public.practice_questions q on q.id = a.question_id where a.benchmark_id = p_benchmark
  ), sub as (select * from a where submitted_at is not null and not skipped),
  ev as (
    select count(*) filter (where e.kind = 'returned') as returns, count(*) filter (where e.kind = 'changed_answer') as changes
    from public.practice_attempt_events e where e.attempt_id in (select id from a)
  )
  select jsonb_build_object(
    'attempts', (select count(*) from a),
    'submitted', (select count(*) from sub),
    'skips', (select count(*) from a where skipped),
    'unsubmitted', (select count(*) from a where submitted_at is null),
    'returns', ev.returns, 'answer_changes', ev.changes,
    'accuracy', (select case when count(*) > 0 then round(count(*) filter (where is_correct)::numeric / count(*), 4) end from sub),
    'pacing_ratio', (select round((percentile_cont(0.5) within group (order by elapsed_ms / (expected_time_seconds * 1000.0))
        filter (where expected_time_seconds is not null))::numeric, 3) from sub),
    'by_section', coalesce((select jsonb_object_agg(section, jsonb_build_object('submitted', n, 'correct', c,
        'accuracy', round(c::numeric / n, 4), 'pacing_ratio', pace))
      from (select section, count(*) n, count(*) filter (where is_correct) c,
              round((percentile_cont(0.5) within group (order by elapsed_ms / (expected_time_seconds * 1000.0))
                filter (where expected_time_seconds is not null))::numeric, 3) as pace
            from sub group by section) s), '{}'::jsonb),
    'calibration', jsonb_build_object(
      'by_confidence', coalesce((select jsonb_object_agg(confidence::text, jsonb_build_object('submitted', n,
          'accuracy', round(c::numeric / n, 4)))
        from (select confidence, count(*) n, count(*) filter (where is_correct) c from sub
              where confidence is not null group by confidence) s), '{}'::jsonb),
      'confident_wrong_share', (select case when count(*) > 0 then round(count(*) filter (where not is_correct)::numeric / count(*), 4) end
        from sub where confidence = 3)),
    'traps', coalesce((select jsonb_object_agg(trap_key, n) from (
        select t.trap_key, count(*) n from sub
        join public.practice_question_distractors d on d.question_id = sub.question_id and d.choice_key = sub.selected_answer
        join public.trap_types t on t.id = d.trap_type_id
        where not sub.is_correct group by t.trap_key) s), '{}'::jsonb),
    'definition', 'v1')
  from ev
$$;

create function public.complete_benchmark(p_benchmark uuid) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare v public.practice_benchmarks; v_metrics jsonb;
begin
  select b.* into v from public.practice_benchmarks b join public.students s on s.id = b.student_id
  where b.id = p_benchmark and s.linked_user_id = auth.uid() for update of b;
  if not found then raise exception 'Only the student who started this benchmark can complete it' using errcode = '42501'; end if;
  if v.completed_at is not null then raise exception 'Benchmark was already completed' using errcode = '22023'; end if;
  v_metrics := public.benchmark_metrics_internal(p_benchmark);
  update public.practice_benchmarks set completed_at = now(), metrics = v_metrics where id = p_benchmark;
  return v_metrics;
end $$;

-- v2 recommender. Buckets and reasons are unchanged (weak_knowledge, weak_pacing, new_skill, review, untagged),
-- but a session is spread out: questions are dealt round-robin across skills (a skill's second question comes
-- after every other skill's first), so a new student sees every section and skill in the bank, and within a skill
-- the question nearest the skill's target difficulty comes first. Target difficulty (1-5) from the skill's recent
-- accuracy: < 60% -> 2, 60-85% -> 3, > 85% -> 4, no history -> 3. Unrated questions count as 3.
-- Greedy fill of the time budget as before.
create or replace function public.recommend_internal(p_student uuid, p_target_minutes integer, p_exam_version uuid)
returns table (item_position integer, question_id uuid, skill_id uuid, expected_time_seconds integer, reason text)
language plpgsql stable set search_path = '' as $$
declare v_budget integer := p_target_minutes * 60; v_used integer := 0; r record;
begin
  item_position := 0;
  for r in
    with est as (select * from public.skill_estimates_internal(p_student)),
    seen as (select a.question_id as qid, max(a.presented_at) as last_seen
      from public.practice_attempts a where a.student_id = p_student group by a.question_id),
    cand as (
      select q.id, qs.skill_id as sid, q.section, q.expected_time_seconds as secs, s.last_seen,
        case when e.knowledge_weak then 'weak_knowledge' when e.pacing_weak then 'weak_pacing'
          when qs.skill_id is null then 'untagged' when e.skill_id is null then 'new_skill' else 'review' end as why,
        case when e.knowledge_weak then 0 when e.pacing_weak then 1
          when qs.skill_id is null then 4 when e.skill_id is null then 2 else 3 end as bucket,
        abs(coalesce(q.difficulty, 3) - case when e.accuracy is null then 3 when e.accuracy < 0.6 then 2
          when e.accuracy <= 0.85 then 3 else 4 end) as gap
      from public.practice_questions q
      left join public.practice_question_skills qs on qs.question_id = q.id and qs.is_primary
      left join est e on e.skill_id = qs.skill_id
      left join seen s on s.qid = q.id
      where q.status = 'published' and q.expected_time_seconds is not null
        and (p_exam_version is null or q.exam_version_id = p_exam_version)
    ), ranked as (
      select c.*, row_number() over (partition by coalesce(c.sid::text, 'untagged:' || c.section)
        order by c.last_seen nulls first, c.gap, c.id) as turn
      from cand c
    )
    select * from ranked
    order by turn, bucket, section, gap, last_seen nulls first, id
  loop
    exit when v_used >= v_budget;
    continue when v_used + r.secs > v_budget;
    v_used := v_used + r.secs;
    item_position := item_position + 1;
    question_id := r.id; skill_id := r.sid; expected_time_seconds := r.secs; reason := r.why;
    return next;
  end loop;
end $$;

revoke all on function public.benchmark_metrics_internal(uuid) from public, anon, authenticated;
revoke all on function public.recommend_internal(uuid, integer, uuid) from public, anon, authenticated;
do $$
declare f regprocedure;
begin
  foreach f in array array['public.start_benchmark(uuid,text,uuid)'::regprocedure,
                           'public.complete_benchmark(uuid)'::regprocedure,
                           'public.start_practice_attempt(uuid,uuid,uuid,uuid)'::regprocedure] loop
    execute format('revoke all on function %s from public, anon', f);
    execute format('grant execute on function %s to authenticated, service_role', f);
  end loop;
end $$;
