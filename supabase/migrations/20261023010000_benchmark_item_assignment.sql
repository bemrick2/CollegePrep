-- #263 (CR-23 follow-up): a progress check is assigned its items once, at start, and exposes only those.
--
-- Before this migration an open check unlocked every reserved stem of its exam version for 4 hours, the server took as
-- many attempts as the reserve held, and reading without answering left no trace (a later check could be scored
-- "comparable" on items already read). Now:
--
-- * practice_benchmark_plan(exam_family, kind, section, items): the check length per section, owned by the server.
--   Seeded with the app's rule (web/src/lib/engine/benchmark.ts PER_SECTION; checkPlanFromCounts uses the same sizes):
--   a section's check takes min(items, reserved items in that section). There are no 'full' rows: the full-length form
--   isn't ready (the app's FULL_FORM_READY is false; its 99-per-section placeholder would drain the whole reserve), and
--   start_benchmark refuses a kind with no plan rows for the exam family. Readable by any signed-in user (it is not
--   secret); written only by migrations. A section without a row is not measured. No caller can supply a size.
-- * practice_benchmark_kinds(kind, available, needs_prior, needs_no_prior, min_days_after_prior): which kinds may open,
--   per the owner's decision of 2026-10-26. A "prior check" is any earlier check of the student for the exam version
--   that was assigned items (completed, abandoned or expired) or was completed. 'initial' opens only with no prior
--   check; 'mini' only after one, and at least 28 days after the last prior check's start; 'full' is unavailable. So
--   abandoning a check (letting it expire) never resets the rules: a student who abandons their initial check gets a
--   mini 28 days later. The rule values live only in this table; benchmark_rules_internal applies them, for both
--   start_benchmark (every caller, including direct RPC calls) and the read-only benchmark_allowed_kinds.
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
--   assignment. A student has at most one live check per exam version. A start of the same kind resumes it, answered
--   in or not, with the same assignment (benchmark_questions lists only its unused items), so a reload or retry never
--   draws a fresh set; a start of another kind while it is live is refused (22023, "already open ... resume it"). This
--   replaces 20261022050000's "a half-taken check expires instead of being resumed". Expiry is unchanged: 4 hours after
--   its start a check is no longer live, and the next start follows the kind rules. A live check of one exam version
--   neither blocks nor resumes a start for another. A check with only minutes left is still resumed (refusing would
--   strand the student until it expires); benchmark_allowed_kinds returns live_expires_at so the app can warn. There is
--   no unique index for "one live check": liveness depends on the clock (expired checks stay completed_at null), so the
--   per-student lock in start_benchmark enforces it instead.
-- * benchmark_allowed_kinds(student, exam_version), read-only, for anyone who may view the student: the live check
--   (id, kind, expiry), the kinds start_benchmark would accept now, when the next mini opens (a timestamp), and
--   reserve_available (false: the exam version has no servable reserved item in a planned section, nothing is allowed,
--   and a start is refused with 22023 "Not measured: no reserved questions for this exam" instead of opening a check
--   that would assign nothing yet count as the student's check). The 28-day gap is counted in UTC 24-hour days.
-- * can_read_reserved_question admits a reserved item only when it is assigned to a live check of the caller's own
--   (linked) student login, or, as before, to anyone who may view a student who attempted it (review of results).
-- * benchmark_questions lists only the check's assigned items it hasn't used yet.
-- * start_practice_attempt with a benchmark accepts only that check's assigned items, each at most once.
-- * Cross-exam isolation: assignment draws only from the check's own exam version, and composite foreign keys make an
--   item row of another version impossible to store.
-- Checks opened before this migration have no assignment (items_assigned_at is null): they unlock nothing, take no
-- attempts, and are never resumed; they expire as before and can still be completed.
-- Passages: a reserved (assessment) item must be the only question on its passage. The reserve script refuses an item
-- whose passage another question uses, and a trigger on practice_questions refuses any write that would put a
-- reserved item and another question on the same passage (attaching a practice item to a reserved passage, or
-- reserving an item whose passage is shared).
-- practice_reserve_releases records each applied reserve script (digest, exam version, items, file sha256, time); the
-- script refuses to run twice.
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
  ('sat', 'initial', 'reading_writing', 9), ('sat', 'initial', 'math', 9),
  ('sat', 'mini', 'reading_writing', 4), ('sat', 'mini', 'math', 4);
alter table public.practice_benchmark_plan enable row level security;
revoke all on public.practice_benchmark_plan from anon, authenticated;
grant select on public.practice_benchmark_plan to authenticated;
grant select, insert, update, delete on public.practice_benchmark_plan to service_role;
create policy benchmark_plan_read on public.practice_benchmark_plan for select to authenticated using (true);

-- Which kinds of check may open (owner decision 2026-10-26; rule values live only here, for Design to adjust). A prior
-- check is an earlier check of the student for the exam version that was assigned items or completed.
--   initial  only while the student has no prior check for the exam version;
--   mini     (repeat) only after a prior check, and at least min_days_after_prior days after the last one's start;
--   full     not available until a full-length form exists (and it has no plan rows).
create table public.practice_benchmark_kinds (
  kind text primary key check (kind in ('initial','mini','full')),
  available boolean not null,
  needs_prior boolean not null,
  needs_no_prior boolean not null,
  min_days_after_prior integer not null check (min_days_after_prior between 0 and 365),
  check (not (needs_prior and needs_no_prior))
);
comment on table public.practice_benchmark_kinds is
  '#263: which progress-check kinds may open, enforced by start_benchmark for every caller. The app schedules a mini every ~35 days.';
insert into public.practice_benchmark_kinds values
  ('initial', true, false, true, 0),
  ('mini', true, true, false, 28),
  ('full', false, true, false, 28);
alter table public.practice_benchmark_kinds enable row level security;
revoke all on public.practice_benchmark_kinds from anon, authenticated;
grant select on public.practice_benchmark_kinds to authenticated;
grant select, insert, update, delete on public.practice_benchmark_kinds to service_role;
create policy benchmark_kinds_read on public.practice_benchmark_kinds for select to authenticated using (true);

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

-- Whole days after a moment, counted in UTC (24-hour days), whatever the session TimeZone or a DST change.
create function public.benchmark_plus_days_utc(p_at timestamptz, p_days integer) returns timestamptz
language sql immutable set search_path = '' as $$
  select ((p_at at time zone 'UTC') + make_interval(days => p_days)) at time zone 'UTC'
$$;
revoke all on function public.benchmark_plus_days_utc(timestamptz, integer) from public, anon;
grant execute on function public.benchmark_plus_days_utc(timestamptz, integer) to authenticated, service_role;

-- The one place the check rules are applied (start_benchmark and benchmark_allowed_kinds both call it).
-- reserve_available: the exam version has at least one servable reserved item in a planned section; without one no
-- check can be measured, so nothing is allowed and a start is refused (it would burn the student's initial check).
create function public.benchmark_rules_internal(p_student uuid, p_exam_version uuid)
returns table (live_benchmark uuid, live_kind text, live_expires_at timestamptz, last_prior_start timestamptz,
  allowed_kinds text[], next_mini_at timestamptz, reserve_available boolean)
language plpgsql stable set search_path = '' as $$
declare v_family text; v_mini integer;
begin
  select e.exam_family into v_family from public.exam_versions e where e.id = p_exam_version;
  reserve_available := exists (select 1 from public.practice_questions q
    join public.practice_benchmark_plan p on p.exam_family = v_family and p.section = q.section
    join public.practice_benchmark_kinds k on k.kind = p.kind and k.available
    where q.exam_version_id = p_exam_version and q.pool = 'assessment' and q.status = 'published' and q.review_current);
  select b.id, b.kind, b.started_at + interval '4 hours' into live_benchmark, live_kind, live_expires_at
  from public.practice_benchmarks b
  where b.student_id = p_student and b.exam_version_id = p_exam_version
    and public.benchmark_is_live(b.started_at, b.completed_at) and b.items_assigned_at is not null
  order by b.started_at desc limit 1;
  select max(b.started_at) into last_prior_start from public.practice_benchmarks b
  where b.student_id = p_student and b.exam_version_id = p_exam_version
    and (b.items_assigned_at is not null or b.completed_at is not null)
    and b.id is distinct from live_benchmark;
  if live_benchmark is not null then
    allowed_kinds := array[live_kind];  -- the live check is resumed; nothing else opens
  elsif not reserve_available then
    allowed_kinds := '{}';  -- not measured: no reserved questions for this exam
  else
    select coalesce(array_agg(k.kind order by k.kind), '{}') into allowed_kinds
    from public.practice_benchmark_kinds k
    where k.available
      and exists (select 1 from public.practice_benchmark_plan p where p.exam_family = v_family and p.kind = k.kind)
      and not (k.needs_no_prior and last_prior_start is not null)
      and not (k.needs_prior and last_prior_start is null)
      and (last_prior_start is null or public.benchmark_plus_days_utc(last_prior_start, k.min_days_after_prior) <= now());
  end if;
  select k.min_days_after_prior into v_mini from public.practice_benchmark_kinds k where k.kind = 'mini' and k.available;
  -- When the next mini may open: min_days_after_prior days after the last check started, counting a live check too.
  next_mini_at := public.benchmark_plus_days_utc(greatest(last_prior_start, live_expires_at - interval '4 hours'), v_mini);
  return next;
end $$;
revoke all on function public.benchmark_rules_internal(uuid, uuid) from public, anon, authenticated;

-- Read-only: what a start would do now, for anyone who may view the student (the app reads this instead of guessing).
create function public.benchmark_allowed_kinds(p_student uuid, p_exam_version uuid)
returns table (live_benchmark uuid, live_kind text, live_expires_at timestamptz, allowed_kinds text[], next_mini_at timestamptz,
  reserve_available boolean)
language plpgsql stable security definer set search_path = '' as $$
begin
  if not public.can_view_student(p_student) then
    raise exception 'Not allowed to view this student' using errcode = '42501';
  end if;
  if p_exam_version is null or not exists (select 1 from public.exam_versions e where e.id = p_exam_version) then
    raise exception 'Unknown exam version' using errcode = '22023';
  end if;
  return query select r.live_benchmark, r.live_kind, r.live_expires_at, r.allowed_kinds, r.next_mini_at, r.reserve_available
    from public.benchmark_rules_internal(p_student, p_exam_version) r;
end $$;
revoke all on function public.benchmark_allowed_kinds(uuid, uuid) from public, anon;
grant execute on function public.benchmark_allowed_kinds(uuid, uuid) to authenticated, service_role;
comment on function public.benchmark_allowed_kinds(uuid, uuid) is
  '#263: the live check (resumed by start_benchmark), the kinds a start would accept now, when the next mini opens, and whether the exam version has a reserve at all.';

-- From 20261022050000; owner contract (2026-10-26): one live check per student and exam version, resumed answered in
-- or not with its assignment; which kinds may open comes from benchmark_rules_internal; sizes from the plan only.
create or replace function public.start_benchmark(p_student uuid, p_kind text, p_exam_version uuid default null) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_id uuid; r record; v_rule public.practice_benchmark_kinds;
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
  select k.* into v_rule from public.practice_benchmark_kinds k where k.kind = p_kind;
  if not coalesce(v_rule.available, false) or not exists (select 1 from public.exam_versions e
      join public.practice_benchmark_plan p on p.exam_family = e.exam_family where e.id = p_exam_version and p.kind = p_kind) then
    raise exception 'This kind of progress check is not available for this exam yet' using errcode = '22023';
  end if;
  -- Serialise starts per student: the student row lock, and an advisory lock tests can observe in pg_locks.
  perform 1 from public.students s where s.id = p_student for update;
  perform pg_catalog.pg_advisory_xact_lock(pg_catalog.hashtextextended('practice_benchmark_start:' || p_student::text, 0));
  select * into r from public.benchmark_rules_internal(p_student, p_exam_version);
  -- Resume: the live check for this exam version, answered in or not, with its assignment.
  if r.live_benchmark is not null and r.live_kind = p_kind then return r.live_benchmark; end if;
  if r.live_benchmark is not null then
    raise exception 'A % progress check is already open for this exam; resume it', r.live_kind using errcode = '22023';
  end if;
  if not r.reserve_available then
    raise exception 'Not measured: no reserved questions for this exam' using errcode = '22023';
  end if;
  if not p_kind = any(r.allowed_kinds) then
    if v_rule.needs_no_prior and r.last_prior_start is not null then
      raise exception 'An initial progress check is only for a student who has not started one for this exam' using errcode = '22023';
    elsif v_rule.needs_prior and r.last_prior_start is null then
      raise exception 'A repeat progress check comes after a first check for this exam' using errcode = '22023';
    else
      raise exception 'The next progress check opens % days after the last one started (on % in the student''s time zone)',
        v_rule.min_days_after_prior,
        to_char(public.benchmark_plus_days_utc(r.last_prior_start, v_rule.min_days_after_prior) at time zone public.student_time_zone(p_student),
          'YYYY-MM-DD HH24:MI')
        using errcode = '22023';
    end if;
  end if;
  insert into public.practice_benchmarks(student_id, kind, exam_version_id) values (p_student, p_kind, p_exam_version)
  returning id into v_id;
  -- A check with no items would measure nothing yet count as the student's check: refuse, and the start rolls back.
  if public.assign_benchmark_items_internal(v_id) = 0 then
    raise exception 'Not measured: no reserved questions for this exam' using errcode = '22023';
  end if;
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

-- A reserved item is the only question on its passage: refuse any write that would share a passage between a reserved
-- item and another question (attaching a practice item to a reserved passage, or reserving an item on a shared one).
create function public.practice_question_passage_guard() returns trigger
language plpgsql security definer set search_path = '' as $$
begin
  -- Lock the passage so two concurrent writers can't both attach to it.
  perform 1 from public.practice_passages pp where pp.id = new.passage_id for update;
  if new.passage_id is not null and exists (select 1 from public.practice_questions o
      where o.passage_id = new.passage_id and o.id <> new.id and (o.pool = 'assessment' or new.pool = 'assessment')) then
    raise exception 'A reserved progress-check question must be the only question on its passage' using errcode = '23514';
  end if;
  return new;
end $$;
revoke all on function public.practice_question_passage_guard() from public, anon, authenticated;
create trigger practice_question_passage_guard before insert or update of passage_id, pool on public.practice_questions
  for each row execute function public.practice_question_passage_guard();

-- Each applied reserve script (scripts/make_reserve_migration.py): what it marked, when, and from which file. A script
-- refuses to run when its digest is already recorded.
create table public.practice_reserve_releases (
  digest text primary key check (digest ~ '^[0-9a-f]{64}$'),
  exam_version_key text not null,
  items jsonb not null check (jsonb_typeof(items) = 'array' and jsonb_array_length(items) > 0),
  script_sha256 text check (script_sha256 is null or script_sha256 ~ '^[0-9a-f]{64}$'),
  applied_at timestamptz not null default now(),
  applied_by text not null default current_user
);
comment on table public.practice_reserve_releases is
  'CR-23: one row per applied reserve script (content digest, exam version, items, file sha256). Written only by the script.';
alter table public.practice_reserve_releases enable row level security;
revoke all on public.practice_reserve_releases from anon, authenticated;
grant select on public.practice_reserve_releases to service_role;
