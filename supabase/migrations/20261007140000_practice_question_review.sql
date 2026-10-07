-- CR-21 (issue #37): a question is served only after review, and only while the reviewed content is unchanged.
--
--   practice_questions.review_status  'approved' | 'changes_needed' | 'rejected' (null: never reviewed)
--   practice_questions.reviewed_at    when the review decision was recorded
--   practice_questions.review_method  how it was reviewed (free text, e.g. 'human: two reviewers', 'loader v2 checks')
--   practice_questions.content_hash   public.practice_question_content_hash() of the content that was reviewed
--   practice_questions.review_current maintained by triggers: approved and content_hash equals the current hash
--
-- The hash covers what a student sees and what grading reveals: exam version, question type, section, stem, choices,
-- answer format, accepted answers, hints, explanations, remember_text, the passage (title and body), skill tags,
-- distractor rationales and traps, and strategy links. Calibration and logistics (difficulty, difficulty_calibrated,
-- difficulty_label, expected_time_seconds, blueprint, attribution, license, status) do not void an approval.
--
-- Any content edit, to the question, its passage or its skill/distractor/strategy rows, sets review_current to false
-- until public.approve_practice_question() records a new approval. Edits are never blocked. Serving requires
-- status = 'published' and review_current in: the question, link and passage read policies, start_practice_attempt and
-- the recommender behind recommend_practice_set and start_practice_session. Objects are altered or replaced in place.

alter table public.practice_questions
  add column review_status text check (review_status in ('approved','changes_needed','rejected')),
  add column reviewed_at timestamptz,
  add column review_method text check (review_method is null or length(btrim(review_method)) between 1 and 200),
  add column content_hash text check (content_hash is null or content_hash ~ '^[0-9a-f]{64}$'),
  add column review_current boolean not null default false,
  add constraint practice_questions_review_recorded
    check (review_status is null or (reviewed_at is not null and review_method is not null and content_hash is not null));
comment on column public.practice_questions.content_hash is
  'CR-21: sha256 (hex) of the reviewed content, from public.practice_question_content_hash().';
comment on column public.practice_questions.review_current is
  'CR-21: trigger-maintained; true only when review_status = approved and content_hash matches the current content.';

-- Canonical content: jsonb text output is deterministic (keys ordered), and child rows are aggregated in key order.
create function public.practice_question_content_hash(q public.practice_questions) returns text
language sql stable security definer set search_path = '' as $$
  select encode(sha256(convert_to(jsonb_build_object(
    'exam_version_id', q.exam_version_id, 'question_type_id', q.question_type_id, 'section', q.section,
    'stem', q.stem, 'choices', q.choices, 'answer_format', q.answer_format, 'accepted_answers', q.accepted_answers,
    'hints', q.hints, 'teaching_explanation', q.teaching_explanation, 'strategy_explanation', q.strategy_explanation,
    'remember_text', q.remember_text,
    'passage', (select jsonb_build_object('title', p.title, 'body', p.body) from public.practice_passages p where p.id = q.passage_id),
    'skills', (select coalesce(jsonb_agg(jsonb_build_object('skill_id', s.skill_id, 'is_primary', s.is_primary) order by s.skill_id), '[]')
               from public.practice_question_skills s where s.question_id = q.id),
    'distractors', (select coalesce(jsonb_agg(jsonb_build_object('choice_key', d.choice_key, 'rationale', d.rationale,
                      'trap_type_id', d.trap_type_id) order by d.choice_key), '[]')
                    from public.practice_question_distractors d where d.question_id = q.id),
    'strategies', (select coalesce(jsonb_agg(jsonb_build_object('strategy_id', t.strategy_id, 'role', t.role, 'is_fastest', t.is_fastest,
                     'strategy_explanation', t.strategy_explanation) order by t.strategy_id), '[]')
                   from public.practice_question_strategies t where t.question_id = q.id)
  )::text, 'UTF8')), 'hex')
$$;

create function public.practice_question_review_sync() returns trigger
language plpgsql security definer set search_path = '' as $$
begin
  new.review_current := new.review_status is not distinct from 'approved'
    and new.content_hash is not distinct from public.practice_question_content_hash(new);
  return new;
end $$;
create trigger practice_question_review_sync before insert or update on public.practice_questions
  for each row execute function public.practice_question_review_sync();

-- Child and passage edits recompute the parent's review_current (a no-op update fires the trigger above).
create function public.practice_question_child_touch() returns trigger
language plpgsql security definer set search_path = '' as $$
begin
  if tg_table_name = 'practice_passages' then
    update public.practice_questions q set review_current = q.review_current where q.passage_id = coalesce(new.id, old.id);
  else
    update public.practice_questions q set review_current = q.review_current
    where q.id in (select x from unnest(array[case when tg_op <> 'DELETE' then new.question_id end,
                                              case when tg_op <> 'INSERT' then old.question_id end]) x where x is not null);
  end if;
  return null;
end $$;
create trigger practice_question_review_touch after insert or update or delete on public.practice_question_skills
  for each row execute function public.practice_question_child_touch();
create trigger practice_question_review_touch after insert or update or delete on public.practice_question_distractors
  for each row execute function public.practice_question_child_touch();
create trigger practice_question_review_touch after insert or update or delete on public.practice_question_strategies
  for each row execute function public.practice_question_child_touch();
create trigger practice_question_review_touch after update on public.practice_passages
  for each row execute function public.practice_question_child_touch();

-- Records a review of the question's current content (the loader calls this after its checks pass).
create function public.approve_practice_question(p_question uuid, p_method text, p_reviewed_at timestamptz default now(),
  p_status text default 'approved') returns text
language plpgsql security definer set search_path = '' as $$
declare v_hash text;
begin
  if p_status is null or p_status not in ('approved','changes_needed','rejected') then
    raise exception 'Review status must be approved, changes_needed or rejected' using errcode = '22023';
  end if;
  select public.practice_question_content_hash(q) into v_hash from public.practice_questions q where q.id = p_question for update;
  if v_hash is null then raise exception 'Unknown question' using errcode = '22023'; end if;
  update public.practice_questions set review_status = p_status, reviewed_at = coalesce(p_reviewed_at, now()),
    review_method = p_method, content_hash = v_hash
  where id = p_question;
  return v_hash;
end $$;

revoke all on function public.practice_question_content_hash(public.practice_questions) from public, anon, authenticated;
revoke all on function public.practice_question_review_sync() from public, anon, authenticated;
revoke all on function public.practice_question_child_touch() from public, anon, authenticated;
revoke all on function public.approve_practice_question(uuid, text, timestamptz, text) from public, anon, authenticated;
grant execute on function public.practice_question_content_hash(public.practice_questions) to service_role;
grant execute on function public.approve_practice_question(uuid, text, timestamptz, text) to service_role;

-- Clients see whether a visible question is current (always true for what they can read); review details stay private.
grant select (review_current) on public.practice_questions to authenticated;

alter policy published_question_read on public.practice_questions using (status = 'published' and review_current);
alter policy published_question_skill_read on public.practice_question_skills
  using (exists (select 1 from public.practice_questions q where q.id = question_id and q.status = 'published' and q.review_current));
alter policy published_question_strategy_read on public.practice_question_strategies
  using (exists (select 1 from public.practice_questions q where q.id = question_id and q.status = 'published' and q.review_current));
alter policy published_passage_read on public.practice_passages
  using (exists (select 1 from public.practice_questions q where q.passage_id = practice_passages.id
                 and q.status = 'published' and q.review_current));

-- From 20261003120300; the only change is the review_current requirement.
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
  insert into public.practice_attempts(session_id, benchmark_id, student_id, question_id, presented_at, attempt_number)
  select p_session, p_benchmark, p_student, p_question, now(), count(*) + 1
  from public.practice_attempts a where a.student_id = p_student and a.question_id = p_question
  returning id into v_id;
  insert into public.practice_attempt_events(attempt_id, student_id, kind) values (v_id, p_student, 'presented');
  return v_id;
end $$;

-- From 20261003120300; the only change is the review_current requirement on candidates.
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
      where q.status = 'published' and q.review_current and q.expected_time_seconds is not null
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
