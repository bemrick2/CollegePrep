-- CR-23 part 2 (#218 B1, issue #37): seen_before on served practice items, and first-answer skill metrics.
--
-- * practice_session_items.seen_before / last_seen: whether the student had been shown the question before the session
--   served it, and when last. "Shown" is the server's exposure rule from #263 (student_exposure_internal): any earlier
--   attempt (answered, skipped or abandoned), or an assignment to a progress check. Set by a trigger when the item is
--   inserted, whoever inserts it (start_practice_session, or a later replacement of it), and frozen there like
--   practice_benchmark_items.seen_before. Readable with the item (viewers of the student); no client can write it.
--   Rows that existed before this migration are backfilled with exposure before their session started.
-- * student_skill_estimates adds first_answers and first_answer_accuracy per skill: over the skill's 30 most recent
--   first answers. A first answer is a submitted, non-skipped attempt with no earlier attempt at that question by the
--   student and no earlier assignment of it to another progress check. Repeats never count, so a question answered
--   correctly the second time is not improvement. The existing columns, thresholds (knowledge_weak, pacing_weak) and
--   the recommender are unchanged; the new columns come last. first_answer_accuracy is null with no first answers.
-- Scope: recommend_practice_set and start_practice_session keep their signatures (CR-26 replaces both to widen the
-- session length); the served session carries seen_before on its items. The client may stop deriving it from attempts.

alter table public.practice_session_items
  add column seen_before boolean not null default false,
  add column last_seen timestamptz;
comment on column public.practice_session_items.seen_before is
  'CR-23: the student had been shown this question (attempted, or assigned to a check) before the session served it.';
comment on column public.practice_session_items.last_seen is
  'CR-23: when the student was last shown this question before the session served it; null when never.';

update public.practice_session_items i set last_seen = x.at, seen_before = true
from (
  select i2.session_id, i2.question_id, max(e.at) as at
  from public.practice_session_items i2
  join public.practice_sessions ps on ps.id = i2.session_id
  join lateral (
    select a.presented_at as at from public.practice_attempts a
      where a.student_id = ps.student_id and a.question_id = i2.question_id and a.presented_at < ps.started_at
    union all
    select b.assigned_at from public.practice_benchmark_items b
      where b.student_id = ps.student_id and b.question_id = i2.question_id and b.assigned_at < ps.started_at
  ) e on true
  group by i2.session_id, i2.question_id
) x
where i.session_id = x.session_id and i.question_id = x.question_id;

create function public.practice_session_item_seen() returns trigger
language plpgsql security definer set search_path = '' as $$
declare v_student uuid;
begin
  select ps.student_id into v_student from public.practice_sessions ps where ps.id = new.session_id;
  select max(e.at) into new.last_seen from (
    select a.presented_at as at from public.practice_attempts a
      where a.student_id = v_student and a.question_id = new.question_id
    union all
    select b.assigned_at from public.practice_benchmark_items b
      where b.student_id = v_student and b.question_id = new.question_id
  ) e;
  new.seen_before := new.last_seen is not null;
  return new;
end $$;
revoke all on function public.practice_session_item_seen() from public, anon, authenticated;
create trigger practice_session_item_seen before insert on public.practice_session_items
  for each row execute function public.practice_session_item_seen();

-- Per primary skill: the 30 most recent first answers (see the header) and how many were correct.
create function public.first_answer_estimates_internal(p_student uuid)
returns table (skill_id uuid, first_answers bigint, first_correct bigint)
language sql stable set search_path = '' as $$
  with f as (
    select qs.skill_id, a.is_correct,
      row_number() over (partition by qs.skill_id order by a.submitted_at desc, a.id) as rn
    from public.practice_attempts a
    join public.practice_question_skills qs on qs.question_id = a.question_id and qs.is_primary
    where a.student_id = p_student and a.submitted_at is not null and not a.skipped
      and not exists (select 1 from public.practice_attempts p
        where p.student_id = a.student_id and p.question_id = a.question_id and p.attempt_number < a.attempt_number)
      and not exists (select 1 from public.practice_benchmark_items i
        where i.student_id = a.student_id and i.question_id = a.question_id
          and i.benchmark_id is distinct from a.benchmark_id and i.assigned_at <= a.presented_at)
  )
  select f.skill_id, count(*), count(*) filter (where f.is_correct) from f where f.rn <= 30 group by f.skill_id
$$;
revoke all on function public.first_answer_estimates_internal(uuid) from public, anon, authenticated;

-- From 20261002183112; adds first_answers and first_answer_accuracy after the existing columns.
drop function public.student_skill_estimates(uuid);
create function public.student_skill_estimates(p_student uuid)
returns table (skill_id uuid, skill_key text, section text, attempts bigint, correct bigint, accuracy numeric,
  median_elapsed_ms bigint, pacing_ratio numeric, knowledge_weak boolean, pacing_weak boolean,
  first_answers bigint, first_answer_accuracy numeric)
language plpgsql stable security definer set search_path = '' as $$
begin
  if not public.can_view_student(p_student) then raise exception 'Not allowed to view this student' using errcode = '42501'; end if;
  return query
    select e.skill_id, e.skill_key, e.section, e.attempts, e.correct, e.accuracy, e.median_elapsed_ms, e.pacing_ratio,
      e.knowledge_weak, e.pacing_weak, coalesce(f.first_answers, 0)::bigint,
      case when f.first_answers > 0 then round(f.first_correct::numeric / f.first_answers, 4) end
    from public.skill_estimates_internal(p_student) e
    left join public.first_answer_estimates_internal(p_student) f on f.skill_id = e.skill_id
    order by e.section, e.skill_key;
end $$;
revoke all on function public.student_skill_estimates(uuid) from public, anon;
grant execute on function public.student_skill_estimates(uuid) to authenticated, service_role;
comment on function public.student_skill_estimates(uuid) is
  'Per-skill estimates over the 30 most recent answers; CR-23: first_answers / first_answer_accuracy over the 30 most recent first answers (repeats excluded).';
