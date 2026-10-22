-- CR-23 (issue #37, #218 B1): a reserved assessment pool, server-side.
--
--   practice_questions.pool  'practice' (default) | 'assessment'
--
-- * Practice (sessions, the recommender behind recommend_practice_set / start_practice_session, and attempts outside a
--   benchmark) never uses assessment items; an attempt on one outside a benchmark is refused.
-- * Benchmark (progress-check) attempts accept assessment items only, so practice never lends items to checks.
-- * benchmark_questions(benchmark) lists the reserved items for an open benchmark of the caller: unseen first (mid
--   difficulty first), then repeats (least recently shown first), each with seen_before. When the reserved pool is too
--   small the check repeats items; a section with no reserved items gets none and is not measured.
-- * complete_benchmark adds, per section and overall, `repeats` (attempts on a question the student was shown before the
--   benchmark started) and `comparable` (no repeats). A section with any repeat gets no verdict; the app reads
--   `comparable`. metrics.definition becomes 'v2'.
-- Replaces the app's interim client-side holdout (#221). Objects are altered or replaced in place.

alter table public.practice_questions
  add column pool text not null default 'practice' check (pool in ('practice', 'assessment'));
comment on column public.practice_questions.pool is
  'CR-23: practice items serve sessions and the recommender; assessment items serve progress checks only.';
grant select (pool) on public.practice_questions to authenticated;
create index practice_questions_assessment_idx on public.practice_questions(exam_version_id, section) where pool = 'assessment';

-- From 20261007140000; the change is the pool rule.
create or replace function public.start_practice_attempt(p_student uuid, p_question uuid, p_session uuid default null,
  p_benchmark uuid default null) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_id uuid;
begin
  -- Locking the student row serialises attempt numbering.
  perform 1 from public.students s where s.id = p_student and s.linked_user_id = auth.uid() and s.archived_at is null for update;
  if not found then raise exception 'Only the student''s own login can practise' using errcode = '42501'; end if;
  if not exists (select 1 from public.practice_questions q where q.id = p_question and q.status = 'published' and q.review_current) then
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
  -- CR-23: checks use reserved (assessment) items only; practice never uses them, and never lends items to checks.
  if p_benchmark is not null and not exists (select 1 from public.practice_questions q where q.id = p_question and q.pool = 'assessment') then
    raise exception 'Progress checks use reserved questions only' using errcode = '22023';
  end if;
  if p_benchmark is null and not exists (select 1 from public.practice_questions q where q.id = p_question and q.pool = 'practice') then
    raise exception 'Reserved progress-check questions are not used in practice' using errcode = '22023';
  end if;
  insert into public.practice_attempts(session_id, benchmark_id, student_id, question_id, presented_at, attempt_number)
  select p_session, p_benchmark, p_student, p_question, now(), count(*) + 1
  from public.practice_attempts a where a.student_id = p_student and a.question_id = p_question
  returning id into v_id;
  insert into public.practice_attempt_events(attempt_id, student_id, kind) values (v_id, p_student, 'presented');
  return v_id;
end $$;


-- From 20261007140000; the change is pool = 'practice' on candidates.
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
      where q.status = 'published' and q.review_current and q.pool = 'practice' and q.expected_time_seconds is not null
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

-- Reserved items for one open benchmark of the caller, in the order a check should use them.
create function public.benchmark_questions(p_benchmark uuid)
returns table (section text, question_id uuid, difficulty integer, expected_time_seconds integer, seen_before boolean, last_seen timestamptz)
language plpgsql stable security definer set search_path = '' as $$
declare v public.practice_benchmarks;
begin
  select b.* into v from public.practice_benchmarks b join public.students s on s.id = b.student_id
  where b.id = p_benchmark and s.linked_user_id = auth.uid() and b.completed_at is null;
  if not found then raise exception 'No open benchmark of yours with that id' using errcode = '42501'; end if;
  return query
    with seen as (select a.question_id as qid, max(a.presented_at) as last_seen
      from public.practice_attempts a where a.student_id = v.student_id
        and (a.benchmark_id is distinct from p_benchmark) group by a.question_id)
    select q.section::text, q.id, q.difficulty::integer, q.expected_time_seconds::integer, s.qid is not null, s.last_seen
    from public.practice_questions q left join seen s on s.qid = q.id
    where q.pool = 'assessment' and q.status = 'published' and q.review_current
      and (v.exam_version_id is null or q.exam_version_id = v.exam_version_id)
    order by q.section, (s.qid is not null), s.last_seen nulls first, abs(coalesce(q.difficulty, 3) - 3), q.id;
end $$;

-- Repeats per section: attempts in the benchmark whose question the student had been shown before (outside it).
create function public.benchmark_repeats_internal(p_benchmark uuid) returns jsonb
language sql stable set search_path = '' as $$
  -- "Shown before" is an earlier attempt (lower attempt_number) on the same question outside this benchmark; timestamps
  -- can tie within one transaction, attempt numbers can't.
  with a as (select a.*, q.section from public.practice_attempts a join public.practice_questions q on q.id = a.question_id
        where a.benchmark_id = p_benchmark),
  r as (select a.section, count(*) filter (where exists (select 1 from public.practice_attempts p
          where p.student_id = a.student_id and p.question_id = a.question_id and p.attempt_number < a.attempt_number
            and p.benchmark_id is distinct from p_benchmark)) as n
        from a group by a.section)
  select coalesce(jsonb_object_agg(section, n), '{}'::jsonb) from r
$$;

create or replace function public.complete_benchmark(p_benchmark uuid) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare v public.practice_benchmarks; v_metrics jsonb; v_rep jsonb; k text; v_total bigint := 0;
begin
  select b.* into v from public.practice_benchmarks b join public.students s on s.id = b.student_id
  where b.id = p_benchmark and s.linked_user_id = auth.uid() for update of b;
  if not found then raise exception 'Only the student who started this benchmark can complete it' using errcode = '42501'; end if;
  if v.completed_at is not null then raise exception 'Benchmark was already completed' using errcode = '22023'; end if;
  v_metrics := public.benchmark_metrics_internal(p_benchmark);
  v_rep := public.benchmark_repeats_internal(p_benchmark);
  for k in select jsonb_object_keys(v_metrics->'by_section') loop
    v_metrics := jsonb_set(v_metrics, array['by_section', k], (v_metrics->'by_section'->k)
      || jsonb_build_object('repeats', coalesce((v_rep->>k)::bigint, 0), 'comparable', coalesce((v_rep->>k)::bigint, 0) = 0));
  end loop;
  select coalesce(sum(value::bigint), 0) into v_total from jsonb_each_text(v_rep);
  v_metrics := v_metrics || jsonb_build_object('repeats', v_total, 'comparable', v_total = 0, 'definition', 'v2');
  update public.practice_benchmarks set completed_at = now(), metrics = v_metrics where id = p_benchmark;
  return v_metrics;
end $$;

revoke all on function public.benchmark_repeats_internal(uuid) from public, anon, authenticated;
revoke all on function public.benchmark_questions(uuid) from public, anon;
grant execute on function public.benchmark_questions(uuid) to authenticated, service_role;
revoke all on function public.complete_benchmark(uuid) from public, anon;
grant execute on function public.complete_benchmark(uuid) to authenticated, service_role;
comment on function public.benchmark_questions(uuid) is
  'CR-23: reserved items for an open benchmark of the caller: unseen first (mid difficulty first), then repeats, with seen_before.';
