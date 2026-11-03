-- CR-25 (#218 B3): "Report a problem" on a question, for stage 10 (monitoring) of the editorial workflow.
--
-- * report_question_problem(p_attempt, p_reason, p_note) files a report against the question of one practice attempt.
--   - Callers: the attempt's student (their own login), or a guardian with view_progress in the student's household
--     (can_view_student's guardian rule). Anyone else, including anon and the service role (no user), gets 42501. A
--     missing attempt gets the same error as someone else's, so the RPC never says whether an attempt id exists.
--   - Reasons: wrong_key, two_answers, unclear, typo, other. The note is optional, trimmed of all leading and trailing
--     whitespace (spaces, tabs, newlines; a note of only whitespace is no note), and at most 500 characters. Anything
--     else is 22023.
--   - Reserved (assessment) items: reportable only once the attempt was submitted (answered or skipped), or, by the
--     student, while the attempt's own progress check is still live. Otherwise 42501. Practice items are reportable
--     from any of the caller's visible attempts.
--   - One open report per reporter, student, question and content version (the question's content hash when reported,
--     from practice_question_content_hash). Repeating the call returns that open report ({"created": false}) and
--     replaces its reason and note with the new ones ("updated": true when either changed); the same note rules apply,
--     and a repeat never counts against the rate limit. A guardian reporting the same question for two students files
--     two reports. After an editor resolves it, or the content changes, the same person can report again.
--   - Rate limit per reporter: at most 10 new reports in any hour and 30 in any 24 hours (22023, hint 'rate_limited').
--     Calls for one reporter are serialised with a transaction advisory lock, so concurrent calls can't exceed it.
--   - Returns only {"report_id", "created", "updated", "status"}: never the key, an explanation, another family's report, or
--     whether an item is reserved.
-- * question_reports is readable and writable only by the service role (RLS on, no client grants or policies), so no
--   family ever reads a report, their own included.
-- * Review path (service role only, the editorial ledger's reviewers): read question_reports; resolve_question_report
--   (p_report, p_status resolved|dismissed, p_reviewed_by, p_resolution_note) closes an open report once.
-- Deleting a student deletes their reports; deleting a reporter's account keeps the report without the reporter.

create table public.question_reports (
  id uuid primary key default gen_random_uuid(),
  question_id uuid not null references public.practice_questions(id),
  content_hash text not null check (content_hash ~ '^[0-9a-f]{64}$'),
  question_pool text not null check (question_pool in ('practice', 'assessment')),
  attempt_id uuid references public.practice_attempts(id) on delete set null,
  student_id uuid not null references public.students(id) on delete cascade,
  reporter_user_id uuid references auth.users(id) on delete set null,
  reporter_role text not null check (reporter_role in ('student', 'guardian')),
  reason text not null check (reason in ('wrong_key', 'two_answers', 'unclear', 'typo', 'other')),
  note text check (note is null or (length(note) between 1 and 500 and note !~ '^\s' and note !~ '\s$')),
  status text not null default 'open' check (status in ('open', 'resolved', 'dismissed')),
  created_at timestamptz not null default now(),
  reviewed_at timestamptz,
  reviewed_by text check (reviewed_by is null or length(btrim(reviewed_by)) between 1 and 200),
  resolution_note text check (resolution_note is null or length(resolution_note) <= 2000),
  check ((status = 'open') = (reviewed_at is null)),
  check (status = 'open' or reviewed_by is not null)
);
comment on table public.question_reports is
  'CR-25: problem reports on questions. Service role only; filed through report_question_problem, closed through resolve_question_report.';
comment on column public.question_reports.content_hash is
  'CR-25: practice_question_content_hash of the question when reported: the content version the report is about.';
create unique index question_reports_open_idx on public.question_reports(reporter_user_id, student_id, question_id, content_hash)
  where status = 'open';
create index question_reports_reporter_idx on public.question_reports(reporter_user_id, created_at);
create index question_reports_question_idx on public.question_reports(question_id, status);
create index question_reports_student_idx on public.question_reports(student_id);
create index question_reports_attempt_idx on public.question_reports(attempt_id);
alter table public.question_reports enable row level security;
revoke all on public.question_reports from public, anon, authenticated;
grant select, insert, update, delete on public.question_reports to service_role;

create function public.report_question_problem(p_attempt uuid, p_reason text, p_note text default null) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare
  v_uid uuid := auth.uid(); v_a public.practice_attempts; v_s public.students; v_q public.practice_questions;
  v_role text; v_note text := nullif(regexp_replace(p_note, '^\s+|\s+$', '', 'g'), ''); v_hash text; v_id uuid;
  v_old public.question_reports;
begin
  if v_uid is null then raise exception 'Authentication required' using errcode = '42501'; end if;
  if p_reason is null or p_reason not in ('wrong_key', 'two_answers', 'unclear', 'typo', 'other') then
    raise exception 'Reason must be wrong_key, two_answers, unclear, typo or other' using errcode = '22023';
  end if;
  if v_note is not null and length(v_note) > 500 then
    raise exception 'A note is at most 500 characters' using errcode = '22023';
  end if;
  select a.* into v_a from public.practice_attempts a where a.id = p_attempt;
  select s.* into v_s from public.students s where s.id = v_a.student_id;
  if v_s.id is not null and v_s.linked_user_id = v_uid then
    v_role := 'student';
  elsif v_s.id is not null and public.has_household_permission(v_s.household_id, 'view_progress') then
    v_role := 'guardian';
  else
    raise exception 'Not allowed to report on this attempt' using errcode = '42501';
  end if;
  select q.* into v_q from public.practice_questions q where q.id = v_a.question_id;
  -- A reserved item: once attempted, or by the student during the attempt's own live check. The message is the same
  -- for every refusal here, and names no pool.
  if v_q.pool = 'assessment' and v_a.submitted_at is null
     and not (v_role = 'student' and exists (select 1 from public.practice_benchmarks b
       where b.id = v_a.benchmark_id and public.benchmark_is_live(b.started_at, b.completed_at))) then
    raise exception 'This question can be reported once it has been answered' using errcode = '42501';
  end if;
  v_hash := public.practice_question_content_hash(v_q);
  -- One reporter at a time: the open-report check and the rate limit can't be raced.
  perform pg_advisory_xact_lock(hashtextextended('question_reports:' || v_uid::text, 0));
  select r.* into v_old from public.question_reports r
  where r.reporter_user_id = v_uid and r.student_id = v_s.id and r.question_id = v_q.id and r.content_hash = v_hash
    and r.status = 'open'
  for update;
  if v_old.id is not null then
    -- A repeat on your own open report replaces its reason and note; it is not a new report.
    update public.question_reports r set reason = p_reason, note = v_note where r.id = v_old.id;
    return jsonb_build_object('report_id', v_old.id, 'created', false,
      'updated', v_old.reason is distinct from p_reason or v_old.note is distinct from v_note, 'status', 'open');
  end if;
  if (select count(*) from public.question_reports r where r.reporter_user_id = v_uid and r.created_at > now() - interval '1 hour') >= 10
     or (select count(*) from public.question_reports r where r.reporter_user_id = v_uid and r.created_at > now() - interval '24 hours') >= 30 then
    raise exception 'Too many reports; try again later' using errcode = '22023', hint = 'rate_limited';
  end if;
  insert into public.question_reports(question_id, content_hash, question_pool, attempt_id, student_id, reporter_user_id,
    reporter_role, reason, note)
  values (v_q.id, v_hash, v_q.pool, v_a.id, v_s.id, v_uid, v_role, p_reason, v_note)
  returning id into v_id;
  return jsonb_build_object('report_id', v_id, 'created', true, 'updated', false, 'status', 'open');
end $$;
revoke all on function public.report_question_problem(uuid, text, text) from public, anon;
grant execute on function public.report_question_problem(uuid, text, text) to authenticated, service_role;
comment on function public.report_question_problem(uuid, text, text) is
  'CR-25: report a problem with an attempt''s question (student, or guardian with view_progress). One open report per reporter, student, question and content version (a repeat updates it); rate-limited; returns only the report id.';

-- Service role only: an editor closes an open report.
create function public.resolve_question_report(p_report uuid, p_status text, p_reviewed_by text,
  p_resolution_note text default null) returns void
language plpgsql security definer set search_path = '' as $$
begin
  if p_status is null or p_status not in ('resolved', 'dismissed') then
    raise exception 'Status must be resolved or dismissed' using errcode = '22023';
  end if;
  if p_reviewed_by is null or length(btrim(p_reviewed_by)) not between 1 and 200 then
    raise exception 'Name the reviewer' using errcode = '22023';
  end if;
  update public.question_reports r set status = p_status, reviewed_at = now(), reviewed_by = btrim(p_reviewed_by),
    resolution_note = nullif(btrim(p_resolution_note), '')
  where r.id = p_report and r.status = 'open';
  if not found then
    raise exception 'No open report with that id' using errcode = '22023';
  end if;
end $$;
revoke all on function public.resolve_question_report(uuid, text, text, text) from public, anon, authenticated;
grant execute on function public.resolve_question_report(uuid, text, text, text) to service_role;
comment on function public.resolve_question_report(uuid, text, text, text) is
  'CR-25: service role only. Close an open question report as resolved or dismissed.';
