-- CR-24 (issue #37, #218 B2): rights gate on published questions, and the question-bank import rule.
--
-- Rights. A question can be status = 'published' only when
--   * license is one of: original-owned, public-domain, us-federal-pd, cc-by-4.0, cc-by-sa-4.0, or licensed:<vendor>
--     (<vendor>: lowercase letters, digits and hyphens), and
--   * source_attribution is non-empty when the license requires attribution (cc-by-4.0, cc-by-sa-4.0, licensed:*).
-- This is separate from content review (CR-21): changing license or attribution still does not void an approval, but
-- a published row whose rights fail the gate can't be written at all (the update or insert is refused).
--
-- Origin. practice_questions.origin records how an item was drafted: 'authored' (a person), 'generated' (a model or
-- other automated drafting), 'licensed' (taken from a licensed source). A published question must record it.
-- Generation alone confers nothing: a 'generated' item is review_current only when its approval was recorded with a
-- review_method starting 'human:' (the editorial ledger's stages 3-8, CONTENT_PLAN.md section 5), and
-- approve_practice_question refuses any other approval of it. Imports of generated items therefore arrive as drafts and
-- stay unservable until a human review is recorded.
--
-- Local fixtures. The local disposable stack seeds the demo bank, which is generated and has no human review. Its
-- approvals are recorded with a method starting 'fixture:' and count only in a database whose owner has run
-- `alter database ... set collegeprep.fixture_approvals = 'on'` (scripts/local/live_stack.sh does; hosted never does,
-- and no client, import or service_role session can set a database-level setting).
--
-- What the database can and can't establish. It enforces the rules above for whatever origin and method are recorded.
-- It can't tell who drafted an item or whether a person really reviewed it: the importer must label origin honestly,
-- and a 'human:' method is the approver's attestation (the editorial ledger names the people). A draft may have no
-- origin yet (it then counts as not generated); origin must be set before publishing.
--
-- Nothing is backfilled: if a database already holds published questions without a valid license or origin, this
-- migration stops (the check is validated) rather than silently changing what is served.

alter table public.practice_questions
  add column origin text check (origin in ('authored', 'generated', 'licensed'));
comment on column public.practice_questions.origin is
  'CR-24: how the item was drafted (authored, generated, licensed). Generated items need a human: review to be served.';

create function public.fixture_approvals_enabled() returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from pg_catalog.pg_db_role_setting d
    where d.setdatabase = (select oid from pg_catalog.pg_database where datname = pg_catalog.current_database())
      and d.setrole = 0 and 'collegeprep.fixture_approvals=on' = any(d.setconfig))
$$;
revoke all on function public.fixture_approvals_enabled() from public, anon, authenticated;

create function public.question_review_counts(p_origin text, p_method text) returns boolean
language sql stable security definer set search_path = '' as $$
  select p_origin is distinct from 'generated' or coalesce(p_method ~* '^human:', false)
    or (coalesce(p_method ~* '^fixture:', false) and public.fixture_approvals_enabled())
$$;
revoke all on function public.question_review_counts(text, text) from public, anon, authenticated;

create function public.question_license_allowed(p_license text) returns boolean
language sql immutable set search_path = '' as $$
  select coalesce(p_license in ('original-owned', 'public-domain', 'us-federal-pd', 'cc-by-4.0', 'cc-by-sa-4.0')
    or p_license ~ '^licensed:[a-z0-9][a-z0-9-]{0,62}$', false)
$$;
create function public.question_license_needs_attribution(p_license text) returns boolean
language sql immutable set search_path = '' as $$
  select coalesce(p_license in ('cc-by-4.0', 'cc-by-sa-4.0') or p_license like 'licensed:%', false)
$$;
grant execute on function public.question_license_allowed(text) to anon, authenticated, service_role;
grant execute on function public.question_license_needs_attribution(text) to anon, authenticated, service_role;

alter table public.practice_questions add constraint practice_questions_rights_gate check (
  status <> 'published' or (
    public.question_license_allowed(license)
    and (not public.question_license_needs_attribution(license) or length(btrim(coalesce(source_attribution, ''))) > 0)
    and origin is not null));

-- Defence in depth: even if the trigger below is skipped (a restore with triggers disabled, session_replication_role),
-- a generated row can't be stored as current without a human: (or local fixture:) review method.
alter table public.practice_questions add constraint practice_questions_generated_review check (
  not review_current or origin is distinct from 'generated' or coalesce(review_method ~* '^(human|fixture):', false));

-- A generated item's approval counts only when a human review recorded it.
create or replace function public.practice_question_review_sync() returns trigger
language plpgsql security definer set search_path = '' as $$
begin
  -- Relabelling can't launder a generated item: once generated, always generated.
  if tg_op = 'UPDATE' and old.origin = 'generated' and new.origin is distinct from 'generated' then
    raise exception 'A generated question stays marked generated' using errcode = '22023';
  end if;
  new.review_current := new.review_status is not distinct from 'approved'
    and new.content_hash is not distinct from public.practice_question_content_hash(new)
    and public.question_review_counts(new.origin, new.review_method);
  return new;
end $$;

create or replace function public.approve_practice_question(p_question uuid, p_method text, p_reviewed_at timestamptz default now(),
  p_status text default 'approved') returns text
language plpgsql security definer set search_path = '' as $$
declare v_hash text; v_origin text;
begin
  if p_status is null or p_status not in ('approved','changes_needed','rejected') then
    raise exception 'Review status must be approved, changes_needed or rejected' using errcode = '22023';
  end if;
  select public.practice_question_content_hash(q), q.origin into v_hash, v_origin
  from public.practice_questions q where q.id = p_question for update;
  if v_hash is null then raise exception 'Unknown question' using errcode = '22023'; end if;
  if p_status = 'approved' and not public.question_review_counts(v_origin, p_method) then
    raise exception 'A generated question is approved only by a recorded human review (method ''human: ...''; ''fixture: ...'' only where collegeprep.fixture_approvals is on)'
      using errcode = '22023';
  end if;
  update public.practice_questions set review_status = p_status, reviewed_at = coalesce(p_reviewed_at, now()),
    review_method = p_method, content_hash = v_hash
  where id = p_question;
  return v_hash;
end $$;
revoke all on function public.practice_question_review_sync() from public, anon, authenticated;
revoke all on function public.approve_practice_question(uuid, text, timestamptz, text) from public, anon, authenticated;
grant execute on function public.approve_practice_question(uuid, text, timestamptz, text) to service_role;
