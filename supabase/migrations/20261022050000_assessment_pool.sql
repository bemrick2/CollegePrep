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
-- * complete_benchmark adds, per section and overall, `repeats` (scored attempts, i.e. submitted and not skipped, on a
--   question the student had already been shown outside this benchmark) and `comparable` (no repeats). A section with
--   any repeat gets no verdict; the app reads `comparable`. metrics.definition becomes 'v2'.
-- * A check has an exam version, and its items must be that version's reserved items; an item is used at most once per
--   check (a second attempt on it in the same benchmark is refused, and benchmark_questions leaves used items out).
-- * Reserved items' content is readable only by a student with a live check for that exam version, and by those who
--   may view a student who has attempted the item (so "unseen" doesn't depend on the client behaving).
-- * A check is live for 4 hours from its start (benchmark_is_live). An abandoned check stops unlocking the reserve and
--   takes no more attempts; complete_benchmark still scores what was answered.
-- * start_benchmark requires an exam version, and returns the student's live open check of the same exam version and
--   kind, when nothing has been answered in it yet, instead of opening a second one.
-- * assessment_pool_status(student, exam version): reserved items per section and how many the student hasn't been shown
--   (counts only, no content), for anyone who may view the student.
-- Scope: CR-23 part 1 (the pool, checks, repeats). seen_before on practice items and first-answer estimates
-- (CONTRACT_REQUESTS CR-23 items 1 and 3) are not in this migration.
-- Replaces the app's interim client-side holdout (#221). Objects are altered or replaced in place.

alter table public.practice_questions
  add column pool text not null default 'practice' check (pool in ('practice', 'assessment'));
comment on column public.practice_questions.pool is
  'CR-23: practice items serve sessions and the recommender; assessment items serve progress checks only.';
grant select (pool) on public.practice_questions to authenticated;
create index practice_questions_assessment_idx on public.practice_questions(exam_version_id, section) where pool = 'assessment';

-- A check is live (unlocks reserved content, takes attempts) while open and within 4 hours of its start.
create function public.benchmark_is_live(p_started timestamptz, p_completed timestamptz) returns boolean
language sql stable set search_path = '' as $$
  select p_completed is null and p_started > now() - interval '4 hours'
$$;
revoke all on function public.benchmark_is_live(timestamptz, timestamptz) from public, anon;
grant execute on function public.benchmark_is_live(timestamptz, timestamptz) to authenticated, service_role;

-- From 20261003120300; a check needs an exam version, and a live, unanswered open check of the same version and kind is resumed.
create or replace function public.start_benchmark(p_student uuid, p_kind text, p_exam_version uuid default null) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_id uuid;
begin
  perform public.require_linked_student(p_student);
  if p_kind is null or p_kind not in ('initial','mini','full') then
    raise exception 'Benchmark kind must be initial, mini or full' using errcode = '22023';
  end if;
  if p_exam_version is null then
    raise exception 'A progress check needs an exam version' using errcode = '22023';
  end if;
  if not exists (select 1 from public.exam_versions e where e.id = p_exam_version) then
    raise exception 'Unknown exam version' using errcode = '22023';
  end if;
  -- Locking the student row serialises concurrent starts.
  perform 1 from public.students s where s.id = p_student for update;
  select b.id into v_id from public.practice_benchmarks b
  where b.student_id = p_student and b.exam_version_id = p_exam_version and b.kind = p_kind
    and public.benchmark_is_live(b.started_at, b.completed_at)
    -- Only a check nothing was answered in yet (a failed or empty start): resuming a half-taken check would re-plan its
    -- full length from the remaining items. A half-taken check stays open until it expires.
    and not exists (select 1 from public.practice_attempts a where a.benchmark_id = b.id)
  order by b.started_at desc limit 1;
  if v_id is not null then return v_id; end if;
  insert into public.practice_benchmarks(student_id, kind, exam_version_id) values (p_student, p_kind, p_exam_version)
  returning id into v_id;
  return v_id;
end $$;

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
  if p_benchmark is not null and not exists (select 1 from public.practice_benchmarks b
      where b.id = p_benchmark and public.benchmark_is_live(b.started_at, b.completed_at)) then
    raise exception 'This progress check has expired; start a new one' using errcode = '22023';
  end if;
  -- CR-23: checks use reserved (assessment) items only; practice never uses them, and never lends items to checks.
  if p_benchmark is not null and not exists (select 1 from public.practice_questions q where q.id = p_question and q.pool = 'assessment') then
    raise exception 'Progress checks use reserved questions only' using errcode = '22023';
  end if;
  if p_benchmark is not null and not exists (select 1 from public.practice_benchmarks b join public.practice_questions q on q.id = p_question
      where b.id = p_benchmark and b.exam_version_id = q.exam_version_id) then
    raise exception 'A progress check uses reserved questions of its own exam version' using errcode = '22023';
  end if;
  if p_benchmark is not null and exists (select 1 from public.practice_attempts a
      where a.benchmark_id = p_benchmark and a.question_id = p_question) then
    raise exception 'A question is used once per progress check' using errcode = '22023';
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
  where b.id = p_benchmark and s.linked_user_id = auth.uid() and s.archived_at is null and b.completed_at is null;
  if not found then raise exception 'No open benchmark of yours with that id' using errcode = '42501'; end if;
  if not public.benchmark_is_live(v.started_at, v.completed_at) then
    raise exception 'This progress check has expired; start a new one' using errcode = '22023';
  end if;
  if v.exam_version_id is null then
    raise exception 'A progress check needs an exam version' using errcode = '22023';
  end if;
  return query
    with seen as (select a.question_id as qid, max(a.presented_at) as last_seen
      from public.practice_attempts a where a.student_id = v.student_id
        and (a.benchmark_id is distinct from p_benchmark) group by a.question_id)
    select q.section::text, q.id, q.difficulty::integer, q.expected_time_seconds::integer, s.qid is not null, s.last_seen
    from public.practice_questions q left join seen s on s.qid = q.id
    where q.pool = 'assessment' and q.status = 'published' and q.review_current
      and q.exam_version_id = v.exam_version_id
      and not exists (select 1 from public.practice_attempts u where u.benchmark_id = p_benchmark and u.question_id = q.id)
    order by q.section, (s.qid is not null), s.last_seen nulls first, abs(coalesce(q.difficulty, 3) - 3), q.id;
end $$;

-- Repeats per section: scored attempts in the benchmark whose question the student had been shown before, outside it.
create function public.benchmark_repeats_internal(p_benchmark uuid) returns jsonb
language sql stable set search_path = '' as $$
  -- "Shown before" is an earlier attempt (lower attempt_number) on the same question outside this benchmark; timestamps
  -- can tie within one transaction, attempt numbers can't.
  with a as (select a.*, q.section from public.practice_attempts a join public.practice_questions q on q.id = a.question_id
        where a.benchmark_id = p_benchmark and a.submitted_at is not null and not a.skipped),
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
  where b.id = p_benchmark and s.linked_user_id = auth.uid() and s.archived_at is null for update of b;
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

-- Reserved items' content: a student with a live check for that exam version, or anyone who may view a student who has
-- attempted the item. Child rows (skills, strategies, passages) follow through their policies' question subqueries.
create function public.can_read_reserved_question(p_question uuid, p_exam_version uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.practice_benchmarks b join public.students s on s.id = b.student_id
      where s.linked_user_id = auth.uid() and s.archived_at is null and b.exam_version_id = p_exam_version
        and public.benchmark_is_live(b.started_at, b.completed_at))
    or exists (select 1 from public.practice_attempts a where a.question_id = p_question and public.can_view_student(a.student_id))
$$;
revoke all on function public.can_read_reserved_question(uuid, uuid) from public, anon;
grant execute on function public.can_read_reserved_question(uuid, uuid) to authenticated, service_role;
alter policy published_question_read on public.practice_questions
  using (status = 'published' and review_current
    and (pool = 'practice' or public.can_read_reserved_question(id, exam_version_id)));

-- Counts only (no content): reserved items per section of an exam version and how many this student hasn't been shown.
create function public.assessment_pool_status(p_student uuid, p_exam_version uuid)
returns table (section text, reserved bigint, unseen bigint)
language plpgsql stable security definer set search_path = '' as $$
begin
  if not public.can_view_student(p_student) then
    raise exception 'Not allowed to view this student' using errcode = '42501';
  end if;
  return query
    select q.section::text, count(*), count(*) filter (where not exists (select 1 from public.practice_attempts a
        where a.student_id = p_student and a.question_id = q.id))
    from public.practice_questions q
    where q.pool = 'assessment' and q.status = 'published' and q.review_current and q.exam_version_id = p_exam_version
    group by q.section order by q.section;
end $$;
revoke all on function public.assessment_pool_status(uuid, uuid) from public, anon;
grant execute on function public.assessment_pool_status(uuid, uuid) to authenticated, service_role;
comment on function public.assessment_pool_status(uuid, uuid) is
  'CR-23: reserved items per section and how many the student has not been shown; counts only, for viewers of the student.';
