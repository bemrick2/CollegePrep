-- CR-5 and CR-8 (issue #37): content fields needed before the question bank is loaded.
--   practice_passages + practice_questions.passage_id: shared passages and stimuli.
--   practice_questions.remember_text: a takeaway (at most 16 words), hidden until submission.
--   practice_questions.hint_count: a client-visible count; the hints themselves stay hidden.
--   choices: either plain strings or [{key,text}] objects with unique keys; a choice answer must be a key.
--   skills.concept_summary and question_strategies.sections: answer-free help, readable like the rest of each table.

create table public.practice_passages (
  id uuid primary key default gen_random_uuid(),
  exam_version_id uuid not null references public.exam_versions(id),
  title text check (title is null or length(btrim(title)) between 1 and 200),
  -- English items mark the underlined portion as [bracketed text] and sentence numbers as [1].
  body text not null check (length(btrim(body)) > 0),
  source_attribution text,
  license text,
  created_at timestamptz not null default now(),
  unique (id, exam_version_id)
);

alter table public.practice_questions
  add column passage_id uuid,
  add column remember_text text check (remember_text is null or (length(btrim(remember_text)) > 0
    and array_length(regexp_split_to_array(btrim(remember_text), '\s+'), 1) <= 16)),
  add column hint_count integer generated always as (jsonb_array_length(hints)) stored,
  -- A question and its passage belong to the same exam version.
  add foreign key (passage_id, exam_version_id) references public.practice_passages(id, exam_version_id);
create index practice_questions_passage_idx on public.practice_questions(passage_id) where passage_id is not null;

create function public.choices_valid(p_format text, p_choices jsonb, p_accepted jsonb) returns boolean
language sql immutable set search_path = '' as $$
  select case
    when jsonb_array_length(p_choices) = 0 then p_format <> 'choice'
    when (select bool_and(jsonb_typeof(c) = 'string') from jsonb_array_elements(p_choices) c) then true
    when (select bool_and(jsonb_typeof(c) = 'object' and jsonb_typeof(c->'key') = 'string' and jsonb_typeof(c->'text') = 'string'
            and length(btrim(c->>'key')) > 0) from jsonb_array_elements(p_choices) c)
      then (select count(distinct c->>'key') = count(*) from jsonb_array_elements(p_choices) c)
        and (p_format <> 'choice' or (select bool_and(a #>> '{}' in (select c->>'key' from jsonb_array_elements(p_choices) c))
                                      from jsonb_array_elements(p_accepted) a))
    else false end
$$;
alter table public.practice_questions add constraint practice_questions_choices_shape
  check (public.choices_valid(answer_format, choices, accepted_answers));

alter table public.skills add column concept_summary text
  check (concept_summary is null or length(btrim(concept_summary)) between 1 and 600);
comment on column public.skills.concept_summary is
  'CR-8: a 1-3 sentence lesson on the skill that never refers to a specific question (pre-answer "Teach me").';
alter table public.question_strategies add column sections text[] not null default '{}'
  check (sections <@ array['english','math','reading','science','reading_writing']);
comment on column public.question_strategies.sections is
  'CR-8: sections where the strategy applies (pre-answer "Test strategy"); empty means not yet assigned.';

-- Passages are readable when a published question uses them.
alter table public.practice_passages enable row level security;
revoke all on public.practice_passages from anon, authenticated;
grant select, insert, update, delete on public.practice_passages to service_role;
grant select on public.practice_passages to authenticated;
create policy published_passage_read on public.practice_passages for select to authenticated
  using (exists (select 1 from public.practice_questions q where q.passage_id = practice_passages.id and q.status = 'published'));
grant select (passage_id, hint_count) on public.practice_questions to authenticated;

-- submit_practice_attempt now also reveals remember_text (return type changes, so it is recreated).
drop function public.submit_practice_attempt(uuid, text, integer, integer, integer, text, boolean);
create function public.submit_practice_attempt(p_attempt uuid, p_selected_answer text,
  p_active_ms integer default null, p_first_interaction_ms integer default null,
  p_confidence integer default null, p_strategy_key text default null, p_skipped boolean default false)
returns table (is_correct boolean, skipped boolean, elapsed_ms integer, accepted_answers jsonb,
  teaching_explanation text, strategy_explanation text, distractors jsonb, strategies jsonb, remember_text text)
language plpgsql security definer set search_path = '' as $$
#variable_conflict use_column
declare v public.practice_attempts; v_q public.practice_questions; v_strategy uuid; v_elapsed numeric;
  v_correct boolean; v_last text; v_answer text := nullif(btrim(p_selected_answer), '');
begin
  v := public.open_attempt_for_caller(p_attempt);
  if p_skipped is null then raise exception 'p_skipped must not be null' using errcode = '22023'; end if;
  if p_skipped and v_answer is not null then raise exception 'A skipped attempt has no answer' using errcode = '22023'; end if;
  if not p_skipped and v_answer is null then raise exception 'An answer is required' using errcode = '22023'; end if;
  if p_active_ms < 0 or p_first_interaction_ms < 0 then
    raise exception 'Client timing values must be non-negative' using errcode = '22023';
  end if;
  if p_confidence not between 1 and 3 then raise exception 'Confidence must be 1, 2 or 3' using errcode = '22023'; end if;
  v_elapsed := floor(extract(epoch from now() - v.presented_at) * 1000);
  if v_elapsed > 2147483647 then raise exception 'Attempt is too old to submit; start a new attempt' using errcode = '22023'; end if;
  if p_active_ms > v_elapsed or p_first_interaction_ms > v_elapsed then
    raise exception 'Client-reported time exceeds server elapsed time' using errcode = '22023';
  end if;
  if p_strategy_key is not null then
    select st.id into v_strategy from public.question_strategies st where st.strategy_key = p_strategy_key;
    if not found then raise exception 'Unknown strategy %', p_strategy_key using errcode = '22023'; end if;
  end if;
  select q.* into v_q from public.practice_questions q where q.id = v.question_id;
  if not p_skipped then
    v_correct := public.grade_answer(v_q.answer_format, v_q.accepted_answers, v_answer);
    select e.answer into v_last from public.practice_attempt_events e
    where e.attempt_id = p_attempt and e.kind in ('answered','changed_answer') order by e.id desc limit 1;
    if v_last is not null and v_last <> v_answer then
      insert into public.practice_attempt_events(attempt_id, student_id, kind, answer) values (p_attempt, v.student_id, 'changed_answer', v_answer);
    end if;
  end if;
  update public.practice_attempts a set
    submitted_at = now(), elapsed_ms = v_elapsed, active_ms = p_active_ms, first_interaction_ms = p_first_interaction_ms,
    selected_answer = v_answer, is_correct = v_correct, skipped = p_skipped, confidence = p_confidence,
    strategy_used_id = v_strategy
  where a.id = p_attempt;
  insert into public.practice_attempt_events(attempt_id, student_id, kind, answer)
  values (p_attempt, v.student_id, case when p_skipped then 'skipped' else 'submitted' end, v_answer);
  return query select v_correct, p_skipped, v_elapsed::integer, v_q.accepted_answers, v_q.teaching_explanation,
    v_q.strategy_explanation,
    coalesce((select jsonb_agg(jsonb_build_object('choice', d.choice_key, 'rationale', d.rationale, 'trap', t.trap_key)
      order by d.choice_key) from public.practice_question_distractors d left join public.trap_types t on t.id = d.trap_type_id
      where d.question_id = v_q.id), '[]'::jsonb),
    coalesce((select jsonb_agg(jsonb_build_object('strategy_key', st.strategy_key, 'role', ps.role,
      'is_fastest', ps.is_fastest, 'explanation', ps.strategy_explanation) order by ps.is_fastest desc, st.strategy_key)
      from public.practice_question_strategies ps join public.question_strategies st on st.id = ps.strategy_id
      where ps.question_id = v_q.id), '[]'::jsonb),
    v_q.remember_text;
end $$;
revoke all on function public.submit_practice_attempt(uuid, text, integer, integer, integer, text, boolean) from public, anon;
grant execute on function public.submit_practice_attempt(uuid, text, integer, integer, integer, text, boolean) to authenticated, service_role;
revoke all on function public.choices_valid(text, jsonb, jsonb) from public, anon;
grant execute on function public.choices_valid(text, jsonb, jsonb) to authenticated, service_role;
