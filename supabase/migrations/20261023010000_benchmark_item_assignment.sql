-- #263 (CR-23 follow-up): a progress check is assigned its items once, at start, and exposes only those.
--
-- Before this migration an open check unlocked every reserved stem of its exam version for 4 hours, the server took as
-- many attempts as the reserve held, and reading without answering left no trace (a later check could be scored
-- "comparable" on items already read). Now:
--
-- * practice_benchmark_plan(exam_family, kind, section, items): the check length per section, owned by the server.
--   Seeded with the app's rule (web/src/lib/engine/benchmark.ts PER_SECTION; checkPlanFromCounts uses the same sizes):
--   a section's check takes min(items, reserved items in that section). 'full' is 99 per section, i.e. the whole
--   section's reserve, as the app plans it. Readable by any signed-in user (it is not secret); written only by
--   migrations. A section without a row is not measured.
-- * practice_benchmark_items(benchmark_id, question_id, ...): the items start_benchmark assigned to a check, per
--   section in the order the check uses them: unseen first (mid difficulty first), then repeats (least recently seen
--   first). Each row records seen_before / last_seen as they were at assignment. Viewers of the student can read the
--   rows; no client can write them.
-- * Assignment is exposure. An item counts as seen by the student once it was assigned to any check of theirs, attempted
--   or not, and also when that check was abandoned, expired or completed. benchmark_questions' seen_before, the next
--   check's assignment order, assessment_pool_status' unseen count and complete_benchmark's repeats/comparable all
--   use this (repeats: a scored attempt on an item that was seen when it was assigned, or, as before, that has an
--   earlier attempt outside the check).
-- * start_benchmark assigns once, in the transaction that opens the check (practice_benchmarks.items_assigned_at is set
--   once, compare-and-set). It serialises per student (the student row lock it already took, plus a transaction
--   advisory lock on the student, which tests can observe), so two simultaneous starts give one check and one
--   assignment. Resuming a live, untouched check returns the same check and never re-assigns.
-- * can_read_reserved_question admits a reserved item only when it is assigned to a live check of the caller's own
--   (linked) student login, or, as before, to anyone who may view a student who attempted it (review of results).
-- * benchmark_questions lists only the check's assigned items it hasn't used yet.
-- * start_practice_attempt with a benchmark accepts only that check's assigned items, each at most once.
-- * Cross-exam isolation: assignment draws only from the check's own exam version, and composite foreign keys make an
--   item row of another version impossible to store.
-- Checks opened before this migration have no assignment (items_assigned_at is null): they unlock nothing, take no
-- attempts, and are never resumed; they expire as before and can still be completed.
-- Objects are altered or replaced in place. Nothing here marks any question as reserved.

-- The server-owned check length per exam family, kind and section.
create table public.practice_benchmark_plan (
  exam_family text not null,
  kind text not null check (kind in ('initial','mini','full')),
  section text not null check (length(btrim(section)) > 0),
  items integer not null check (items between 1 and 200),
  primary key (exam_family, kind, section)
);
comment on table public.practice_benchmark_plan is
  '#263: items a progress check assigns per section (min of this and the reserved items in the section). Mirrors the app''s PER_SECTION.';
insert into public.practice_benchmark_plan(exam_family, kind, section, items) values
  ('act', 'initial', 'english', 7), ('act', 'initial', 'math', 8), ('act', 'initial', 'reading', 6), ('act', 'initial', 'science', 6),
  ('act', 'mini', 'english', 3), ('act', 'mini', 'math', 4), ('act', 'mini', 'reading', 3), ('act', 'mini', 'science', 3),
  ('act', 'full', 'english', 99), ('act', 'full', 'math', 99), ('act', 'full', 'reading', 99), ('act', 'full', 'science', 99),
  ('sat', 'initial', 'reading_writing', 9), ('sat', 'initial', 'math', 9),
  ('sat', 'mini', 'reading_writing', 4), ('sat', 'mini', 'math', 4),
  ('sat', 'full', 'reading_writing', 99), ('sat', 'full', 'math', 99);
alter table public.practice_benchmark_plan enable row level security;
revoke all on public.practice_benchmark_plan from anon, authenticated;
grant select on public.practice_benchmark_plan to authenticated;
grant select, insert, update, delete on public.practice_benchmark_plan to service_role;
create policy benchmark_plan_read on public.practice_benchmark_plan for select to authenticated using (true);

-- Targets for the composite keys below (id is already unique; these add the pair).
alter table public.practice_benchmarks add constraint practice_benchmarks_id_student_version_key unique (id, student_id, exam_version_id);
alter table public.practice_questions add constraint practice_questions_id_version_key unique (id, exam_version_id);
alter table public.practice_benchmarks add column items_assigned_at timestamptz;
comment on column public.practice_benchmarks.items_assigned_at is
  '#263: when start_benchmark assigned the check''s items (set once). Null for checks opened before assignment existed.';

create table public.practice_benchmark_items (
  benchmark_id uuid not null,
  student_id uuid not null,
  exam_version_id uuid not null,
  question_id uuid not null,
  section text not null,
  position integer not null check (position >= 1),
  seen_before boolean not null,
  last_seen timestamptz,
  assigned_at timestamptz not null default now(),
  primary key (benchmark_id, question_id),
  unique (benchmark_id, section, position),
  foreign key (benchmark_id, student_id, exam_version_id)
    references public.practice_benchmarks(id, student_id, exam_version_id) on delete cascade,
  foreign key (question_id, exam_version_id) references public.practice_questions(id, exam_version_id)
);
comment on table public.practice_benchmark_items is
  '#263: items assigned to a progress check at its start. Assignment counts as exposure, attempted or not.';
create index practice_benchmark_items_student_idx on public.practice_benchmark_items(student_id, question_id);
alter table public.practice_benchmark_items enable row level security;
revoke all on public.practice_benchmark_items from anon, authenticated;
grant select on public.practice_benchmark_items to authenticated;
grant select, insert, update, delete on public.practice_benchmark_items to service_role;
create policy student_data_read on public.practice_benchmark_items for select to authenticated using (public.can_view_student(student_id));

-- What a student has been shown: any attempt, or any assignment to a check (attempted or not).
create function public.student_exposure_internal(p_student uuid)
returns table (question_id uuid, last_seen timestamptz)
language sql stable set search_path = '' as $$
  select e.qid, max(e.at) from (
    select a.question_id as qid, a.presented_at as at from public.practice_attempts a where a.student_id = p_student
    union all
    select i.question_id, i.assigned_at from public.practice_benchmark_items i where i.student_id = p_student
  ) e group by e.qid
$$;
revoke all on function public.student_exposure_internal(uuid) from public, anon, authenticated;

-- Assigns a just-opened check's items, once. Callers hold the student's lock (start_benchmark).
create function public.assign_benchmark_items_internal(p_benchmark uuid) returns integer
language plpgsql set search_path = '' as $$
declare v public.practice_benchmarks; v_family text; v_n integer;
begin
  update public.practice_benchmarks b set items_assigned_at = now()
  where b.id = p_benchmark and b.items_assigned_at is null
  returning b.* into v;
  if not found then raise exception 'This progress check already has its items' using errcode = '22023'; end if;
  select e.exam_family into v_family from public.exam_versions e where e.id = v.exam_version_id;
  insert into public.practice_benchmark_items(benchmark_id, student_id, exam_version_id, question_id, section, position,
    seen_before, last_seen)
  select v.id, v.student_id, v.exam_version_id, r.id, r.section, r.pos, r.seen, r.last_seen
  from (
    select q.id, q.section, x.question_id is not null as seen, x.last_seen, p.items,
      row_number() over (partition by q.section
        order by (x.question_id is not null), x.last_seen nulls first, abs(coalesce(q.difficulty, 3) - 3), q.id)::integer as pos
    from public.practice_questions q
    join public.practice_benchmark_plan p on p.exam_family = v_family and p.kind = v.kind and p.section = q.section
    left join public.student_exposure_internal(v.student_id) x on x.question_id = q.id
    where q.pool = 'assessment' and q.status = 'published' and q.review_current and q.exam_version_id = v.exam_version_id
  ) r
  where r.pos <= r.items;
  get diagnostics v_n = row_count;
  return v_n;
end $$;
revoke all on function public.assign_benchmark_items_internal(uuid) from public, anon, authenticated;

-- From 20261022050000; the check's items are assigned once when it opens, and resuming never re-assigns.
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
  -- Serialise starts per student: the student row lock, and an advisory lock tests can observe in pg_locks.
  perform 1 from public.students s where s.id = p_student for update;
  perform pg_catalog.pg_advisory_xact_lock(pg_catalog.hashtextextended('practice_benchmark_start:' || p_student::text, 0));
  select b.id into v_id from public.practice_benchmarks b
  where b.student_id = p_student and b.exam_version_id = p_exam_version and b.kind = p_kind
    and public.benchmark_is_live(b.started_at, b.completed_at)
    and b.items_assigned_at is not null
    -- Only a check nothing was answered in yet: a half-taken check stays open until it expires.
    and not exists (select 1 from public.practice_attempts a where a.benchmark_id = b.id)
  order by b.started_at desc limit 1;
  if v_id is not null then return v_id; end if;
  insert into public.practice_benchmarks(student_id, kind, exam_version_id) values (p_student, p_kind, p_exam_version)
  returning id into v_id;
  perform public.assign_benchmark_items_internal(v_id);
  return v_id;
end $$;

-- From 20261022050000; a check attempt must be on an item assigned to that check.
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
  -- #263: only the items assigned to this check when it opened.
  if p_benchmark is not null and not exists (select 1 from public.practice_benchmark_items i
      where i.benchmark_id = p_benchmark and i.question_id = p_question) then
    raise exception 'This question is not part of this progress check' using errcode = '22023';
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

-- From 20261022050000; the check's assigned items it hasn't used yet, in assignment order, with seen_before as assigned.
create or replace function public.benchmark_questions(p_benchmark uuid)
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
    select i.section, q.id, q.difficulty::integer, q.expected_time_seconds::integer, i.seen_before, i.last_seen
    from public.practice_benchmark_items i join public.practice_questions q on q.id = i.question_id
    where i.benchmark_id = p_benchmark
      and q.pool = 'assessment' and q.status = 'published' and q.review_current and q.exam_version_id = v.exam_version_id
      and not exists (select 1 from public.practice_attempts u where u.benchmark_id = p_benchmark and u.question_id = q.id)
    order by i.section, i.position;
end $$;
comment on function public.benchmark_questions(uuid) is
  '#263: the items assigned to an open check of the caller that it has not used yet: unseen first (mid difficulty first), then repeats, with seen_before as assigned.';

-- From 20261022050000; an item that was seen when assigned (assignment is exposure) is a repeat too.
create or replace function public.benchmark_repeats_internal(p_benchmark uuid) returns jsonb
language sql stable set search_path = '' as $$
  -- "Shown before": the item was already seen (attempted or assigned elsewhere) when this check was assigned it, or it
  -- has an earlier attempt (lower attempt_number) outside this benchmark; timestamps can tie, attempt numbers can't.
  with a as (select a.*, q.section from public.practice_attempts a join public.practice_questions q on q.id = a.question_id
        where a.benchmark_id = p_benchmark and a.submitted_at is not null and not a.skipped),
  r as (select a.section, count(*) filter (where exists (select 1 from public.practice_benchmark_items i
            where i.benchmark_id = p_benchmark and i.question_id = a.question_id and i.seen_before)
          or exists (select 1 from public.practice_attempts p
            where p.student_id = a.student_id and p.question_id = a.question_id and p.attempt_number < a.attempt_number
              and p.benchmark_id is distinct from p_benchmark)) as n
        from a group by a.section)
  select coalesce(jsonb_object_agg(section, n), '{}'::jsonb) from r
$$;
revoke all on function public.benchmark_repeats_internal(uuid) from public, anon, authenticated;

-- From 20261022050000; only items assigned to a live check of the caller's own student login (or attempted by a student
-- the caller may view). p_exam_version is kept for the policy and checked as well.
create or replace function public.can_read_reserved_question(p_question uuid, p_exam_version uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.practice_benchmark_items i
      join public.practice_benchmarks b on b.id = i.benchmark_id
      join public.students s on s.id = b.student_id
      where i.question_id = p_question and i.exam_version_id = p_exam_version
        and s.linked_user_id = auth.uid() and s.archived_at is null
        and public.benchmark_is_live(b.started_at, b.completed_at))
    or exists (select 1 from public.practice_attempts a where a.question_id = p_question and public.can_view_student(a.student_id))
$$;

-- From 20261022050000; unseen also excludes items assigned to any earlier check (assignment is exposure).
create or replace function public.assessment_pool_status(p_student uuid, p_exam_version uuid)
returns table (section text, reserved bigint, unseen bigint)
language plpgsql stable security definer set search_path = '' as $$
begin
  if not public.can_view_student(p_student) then
    raise exception 'Not allowed to view this student' using errcode = '42501';
  end if;
  return query
    select q.section::text, count(*), count(*) filter (where x.question_id is null)
    from public.practice_questions q left join public.student_exposure_internal(p_student) x on x.question_id = q.id
    where q.pool = 'assessment' and q.status = 'published' and q.review_current and q.exam_version_id = p_exam_version
    group by q.section order by q.section;
end $$;
