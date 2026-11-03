-- A4 (launch checklist; #218 B8): data export and deletion requests, by service role.
--
-- Owner decisions (docs/legal/DECISIONS.md): #6 manual handling by email at launch, in-app soon; #5 retention: practice
-- history deleted within 30 days of deleting the student or household, email-sent records kept 13 months, billing
-- records kept as tax law requires. The procedure is docs/operations/DATA_REQUESTS.md.
--
--   admin_export_student / admin_export_household   one jsonb document with every row about the student or household
--   admin_delete_student / admin_delete_household   delete (dry run by default), keep what retention requires, log it
--   admin_record_auth_deletion                      records that the listed auth users were deleted (admin API)
--   admin_rescrub_billing_events                    de-identifies payment events that arrived after a deletion
--   admin_purge_expired_retention                   deletes retained email-sent records past their 13 months
--   record_billing_event / deidentify_billing_event the Stripe webhook's writes: events for a deleted (or unknown)
--                                                   household are stored already de-identified
--   data_request_log                                one row per export or deletion; RLS on, no client access
--   data_request_billing_refs                       payment-provider customer and subscription ids of deleted households
--   retained_email_records                          email-sent records kept 13 months after a deletion, unlinked
--
-- Every function here is service-role only (the admin_* entry points and the two webhook writes) or owner only (the
-- data_request_* internals). Privileges are revoked from public, anon, authenticated AND service_role first and then
-- granted, so Supabase's default privileges (which grant new objects to all three roles) cannot widen them.
--
-- A future in-app RPC (Apple 5.1.1(v)) is a SECURITY DEFINER wrapper that checks auth.uid() against the household's
-- permissions and then calls these with channel 'in_app': the definer runs them as the owner, so no client grant is
-- ever needed here.
--
-- Auth accounts are not deleted in SQL: the result lists auth_users_to_delete, which the runbook deletes through the
-- Supabase admin API (that also removes the Auth identities and sessions SQL cannot reach). Their profile rows and
-- rate-limit rows are removed here, so nothing personal waits on that step.
--
-- tests: supabase/tests/data_requests.sql (its allow-list decides every table; a new table without a decision fails CI).

-- Billing events kept for tax are de-identified in place; this records when.
alter table public.billing_events add column deidentified_at timestamptz;

create table public.data_request_log (
  id uuid primary key default gen_random_uuid(),
  action text not null check (action in ('export', 'delete')),
  subject_kind text not null check (subject_kind in ('student', 'household')),
  subject_id uuid not null,
  household_id uuid,                       -- no foreign key: the row outlives the household it describes
  requested_by text not null check (length(btrim(requested_by)) > 0),
  channel text not null check (channel in ('email', 'in_app')),
  reason text,
  requested_at timestamptz not null,
  performed_at timestamptz not null default now(),
  operator text not null check (length(btrim(operator)) > 0),  -- the person who ran it (name or email)
  performed_by text not null,              -- the database role and session it ran as
  exported jsonb,                          -- export: row count per table
  removed jsonb,                           -- delete: row count per table removed
  kept jsonb,                              -- delete: what was kept and why (counts, billing references)
  auth_users_to_delete uuid[] not null default '{}',
  auth_users_deleted_at timestamptz,
  billing_rescrubbed_at timestamptz,
  check (action = 'export' or (reason is not null and length(btrim(reason)) > 0))
);
comment on table public.data_request_log is
  'A4: one row per data export or deletion (docs/operations/DATA_REQUESTS.md). Ids and counts only; no copy of the data.';
alter table public.data_request_log enable row level security;

-- Payment-provider references of a deleted household, so later events about them are de-identified on arrival.
create table public.data_request_billing_refs (
  request_id uuid not null references public.data_request_log(id) on delete cascade,
  provider text not null,
  kind text not null check (kind in ('customer', 'subscription')),
  ref text not null check (length(ref) > 0),
  primary key (request_id, kind, ref)
);
create index data_request_billing_refs_ref_idx on public.data_request_billing_refs(ref);
alter table public.data_request_billing_refs enable row level security;

create table public.retained_email_records (
  id uuid primary key default gen_random_uuid(),
  kind text not null check (kind in ('household_invitation')),
  recipient_email text not null,
  send_count integer not null check (send_count > 0),
  last_sent_at timestamptz not null,
  retain_until timestamptz not null,
  data_request_id uuid references public.data_request_log(id) on delete set null,
  created_at timestamptz not null default now()
);
comment on table public.retained_email_records is
  'A4 / DECISIONS.md #5: email-sent records kept 13 months after the household or student is deleted, linked to no account.';
alter table public.retained_email_records enable row level security;

-- Only the definer functions write these; service_role may read them.
revoke all on public.data_request_log, public.data_request_billing_refs, public.retained_email_records
  from public, anon, authenticated, service_role;
grant select on public.data_request_log, public.data_request_billing_refs, public.retained_email_records to service_role;

-- Subscription states that still bill or still grant access: the provider subscription must be cancelled first.
-- Complimentary ('comp') subscriptions bill nothing and never block; they are deleted with the household.
create function public.data_request_live_subscription(p_provider text, p_status text) returns boolean
language sql immutable set search_path = '' as $$
  select coalesce(p_provider, '') <> 'comp'
    and p_status in ('trialing', 'active', 'past_due', 'unpaid', 'paused', 'incomplete', 'grace', 'billing_retry')
$$;

-- De-identification of a payment event keeps ONLY these keys, at any depth: ids, object types, amounts, currency,
-- tax, status, timestamps and the containers that hold them. Everything else (names, emails, phones, addresses,
-- card details, receipt and invoice URLs and numbers of receipts, metadata, descriptions, custom fields, collected
-- information, URLs) is dropped. A kept key whose value is an object or array is de-identified the same way.
create function public.data_request_billing_kept_keys() returns text[]
language sql immutable set search_path = '' as $$
  select array[
    -- identity and containers
    'id', 'object', 'type', 'api_version', 'created', 'livemode', 'pending_webhooks', 'data', 'previous_attributes',
    'request', 'lines', 'items', 'period', 'price', 'plan', 'recurring', 'product', 'parent', 'subscription_details',
    'invoice_item_details', 'subscription_item_details', 'pricing', 'price_details', 'status_transitions',
    'total_details', 'total_tax_amounts', 'tax_amounts', 'total_taxes', 'taxes', 'tax_rate', 'has_more', 'total_count',
    -- provider references
    'customer', 'subscription', 'subscription_item', 'invoice', 'invoice_item', 'payment_intent', 'charge',
    'latest_invoice', 'lookup_key', 'number',
    -- amounts, currency and tax
    'currency', 'amount', 'amount_due', 'amount_paid', 'amount_remaining', 'amount_total', 'amount_subtotal',
    'amount_tax', 'amount_discount', 'amount_shipping', 'amount_excluding_tax', 'subtotal', 'subtotal_excluding_tax',
    'total', 'total_excluding_tax', 'tax', 'unit_amount', 'unit_amount_decimal', 'quantity', 'percentage', 'inclusive',
    'taxable_amount', 'taxability_reason', 'tax_behavior', 'proration',
    -- status
    'status', 'billing_reason', 'collection_method', 'mode', 'payment_status', 'paid', 'attempted', 'attempt_count',
    'interval', 'interval_count', 'cancel_at_period_end',
    -- timestamps
    'period_start', 'period_end', 'start', 'end', 'start_date', 'current_period_start', 'current_period_end',
    'cancel_at', 'canceled_at', 'ended_at', 'trial_start', 'trial_end', 'due_date', 'effective_at', 'finalized_at',
    'paid_at', 'voided_at', 'marked_uncollectible_at', 'expires_at']::text[]
$$;

create function public.data_request_scrub_billing_payload(p jsonb) returns jsonb
language plpgsql immutable set search_path = '' as $$
declare v jsonb;
begin
  if jsonb_typeof(p) = 'object' then
    select coalesce(jsonb_object_agg(e.key, public.data_request_scrub_billing_payload(e.value)), '{}'::jsonb) into v
    from jsonb_each(p) e where e.key = any (public.data_request_billing_kept_keys());
    return v;
  elsif jsonb_typeof(p) = 'array' then
    select coalesce(jsonb_agg(public.data_request_scrub_billing_payload(e.value) order by e.ord), '[]'::jsonb) into v
    from jsonb_array_elements(p) with ordinality e(value, ord);
    return v;
  end if;
  return p;
end $$;

-- Every string value in a payload, at any depth (customer and subscription ids appear in many shapes).
create function public.data_request_payload_strings(p jsonb) returns text[]
language sql immutable set search_path = '' as $$
  select coalesce(array_agg(v #>> '{}'), '{}') from jsonb_path_query(coalesce(p, 'null'::jsonb), 'strict $.**') v
  where jsonb_typeof(v) = 'string'
$$;

-- Does an event refer to a deleted household's provider customer or subscription?
create function public.data_request_event_is_deleted(p_payload jsonb, p_subscription text) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.data_request_billing_refs r
    where r.ref = p_subscription or r.ref = any (public.data_request_payload_strings(p_payload)))
$$;

create function public.data_request_add_counts(a jsonb, b jsonb) returns jsonb
language sql immutable set search_path = '' as $$
  select coalesce(jsonb_object_agg(k, coalesce((a->>k)::bigint, 0) + coalesce((b->>k)::bigint, 0)), '{}'::jsonb)
  from (select jsonb_object_keys(coalesce(a, '{}'::jsonb)) k union select jsonb_object_keys(coalesce(b, '{}'::jsonb))) x
$$;

create function public.data_request_count_rows(p_tables jsonb) returns jsonb
language sql immutable set search_path = '' as $$
  select coalesce(jsonb_object_agg(e.key, jsonb_array_length(e.value)), '{}'::jsonb) from jsonb_each(p_tables) e
$$;

-- Member accounts of a household that belong to nothing else (no other household, no student profile elsewhere),
-- other than the logins of the household's own students (those go with their student).
create function public.data_request_household_accounts(p_household uuid) returns uuid[]
language sql stable security definer set search_path = '' as $$
  select coalesce(array_agg(m.user_id order by m.user_id), '{}') from public.household_members m
  where m.household_id = p_household
    and not exists (select 1 from public.students x where x.household_id = p_household and x.linked_user_id = m.user_id)
    and not exists (select 1 from public.household_members o where o.user_id = m.user_id and o.household_id <> p_household)
    and not exists (select 1 from public.students o where o.linked_user_id = m.user_id
                    and o.household_id is distinct from p_household)
$$;

-- The billing rows a household request covers, shared by export and delete so both see the same set:
-- subscriptions of the household and the personal (no-household) subscriptions of its departing accounts; their
-- provider customer and subscription ids; and every payment event linked to the household, to one of those
-- subscriptions, or mentioning one of those ids.
create function public.data_request_household_billing(p_household uuid, p_accounts uuid[]) returns jsonb
language plpgsql stable security definer set search_path = '' as $$
declare v_subs text[]; v_customers text[]; v_events bigint[];
begin
  select coalesce(array_agg(distinct x.provider_subscription_id) filter (where x.provider_subscription_id is not null), '{}'),
         coalesce(array_agg(distinct x.provider_customer_id) filter (where x.provider_customer_id is not null), '{}')
    into v_subs, v_customers
  from public.subscriptions x
  where x.household_id = p_household or (x.household_id is null and x.owner_user_id = any (p_accounts));
  select v_customers || coalesce(array_agg(c.provider_customer_id), '{}') into v_customers
  from public.billing_customers c where c.household_id = p_household and c.provider_customer_id <> all (v_customers);
  select coalesce(array_agg(e.id order by e.id), '{}') into v_events from public.billing_events e
  where e.household_id = p_household or e.provider_subscription_id = any (v_subs)
     or public.data_request_payload_strings(e.payload) && (v_subs || v_customers);
  return jsonb_build_object('subscriptions', to_jsonb(v_subs), 'customers', to_jsonb(v_customers),
    'event_ids', to_jsonb(v_events));
end $$;

-- Every per-student row, as jsonb arrays by table. Student view (the student's own request): no other account's ids
-- (set_by, entered_by, requested_by, invitation actors) and no guardian alert settings. Household view: actor ids kept,
-- guardians' alert settings for this student included, and the account and invitation rows left to the household
-- level. Never: invitation code digests, question content or answer keys (attempts carry question ids only).
create function public.data_request_student_tables(p_student uuid, p_household_view boolean) returns jsonb
language plpgsql stable security definer set search_path = '' as $$
declare v_link uuid; v_household uuid; v jsonb; actors text[] := case when p_household_view then '{}'::text[]
  else array['set_by', 'entered_by', 'requested_by', 'created_by', 'revoked_by', 'accepted_by'] end;
begin
  select s.linked_user_id, s.household_id into v_link, v_household from public.students s where s.id = p_student;
  v := jsonb_build_object(
    'students', coalesce((select jsonb_agg(to_jsonb(s)) from public.students s where s.id = p_student), '[]'::jsonb),
    'weekly_practice_goals', coalesce((select jsonb_agg(to_jsonb(g) - actors order by g.week_start, g.id)
      from public.weekly_practice_goals g where g.student_id = p_student), '[]'::jsonb),
    'practice_sessions', coalesce((select jsonb_agg(to_jsonb(x) order by x.started_at, x.id)
      from public.practice_sessions x where x.student_id = p_student), '[]'::jsonb),
    'practice_session_items', coalesce((select jsonb_agg(to_jsonb(i) order by x.started_at, i.session_id, i.position)
      from public.practice_session_items i join public.practice_sessions x on x.id = i.session_id
      where x.student_id = p_student), '[]'::jsonb),
    'practice_attempts', coalesce((select jsonb_agg(to_jsonb(a) order by a.presented_at, a.id)
      from public.practice_attempts a where a.student_id = p_student), '[]'::jsonb),
    'practice_attempt_events', coalesce((select jsonb_agg(to_jsonb(e) order by e.occurred_at, e.id)
      from public.practice_attempt_events e where e.student_id = p_student), '[]'::jsonb),
    'ai_help_requests', coalesce((select jsonb_agg(to_jsonb(r) - actors order by r.requested_at, r.id)
      from public.ai_help_requests r where r.student_id = p_student), '[]'::jsonb),
    'practice_benchmarks', coalesce((select jsonb_agg(to_jsonb(b) order by b.started_at, b.id)
      from public.practice_benchmarks b where b.student_id = p_student), '[]'::jsonb),
    'practice_benchmark_items', coalesce((select jsonb_agg(to_jsonb(b) order by b.benchmark_id, b.section, b.position)
      from public.practice_benchmark_items b where b.student_id = p_student), '[]'::jsonb),
    'student_test_scores', coalesce((select jsonb_agg(to_jsonb(t) - actors order by t.test_date, t.id)
      from public.student_test_scores t where t.student_id = p_student), '[]'::jsonb),
    'student_exam_plan', coalesce((select jsonb_agg(to_jsonb(t) - actors order by t.exam_key)
      from public.student_exam_plan t where t.student_id = p_student), '[]'::jsonb),
    'student_planning_preferences', coalesce((select jsonb_agg(to_jsonb(t) - actors)
      from public.student_planning_preferences t where t.student_id = p_student), '[]'::jsonb),
    'student_academic_interests', coalesce((select jsonb_agg(to_jsonb(t) - actors)
      from public.student_academic_interests t where t.student_id = p_student), '[]'::jsonb));
  if p_household_view then
    v := v || jsonb_build_object(
      'alert_preferences', coalesce((select jsonb_agg(to_jsonb(a) order by a.created_at, a.user_id)
        from public.alert_preferences a where a.student_id = p_student), '[]'::jsonb));
  else
    v := v || jsonb_build_object(
      'household_invitations', coalesce((select jsonb_agg(to_jsonb(i) - 'code_hash' - 'short_code_hash' - actors
        order by i.created_at, i.id) from public.household_invitations i where i.student_id = p_student), '[]'::jsonb),
      'profiles', coalesce((select jsonb_agg(to_jsonb(p)) from public.profiles p where p.id = v_link), '[]'::jsonb),
      'household_members', coalesce((select jsonb_agg(to_jsonb(m)) from public.household_members m
        where m.user_id = v_link and m.household_id = v_household), '[]'::jsonb));
  end if;
  return v;
end $$;

create function public.data_request_household_tables(p_household uuid) returns jsonb
language plpgsql stable security definer set search_path = '' as $$
declare v jsonb; t jsonb; k text; s uuid; v_accounts uuid[] := public.data_request_household_accounts(p_household);
  v_billing jsonb;
begin
  v_billing := public.data_request_household_billing(p_household, v_accounts);
  v := jsonb_build_object(
    'households', coalesce((select jsonb_agg(to_jsonb(h)) from public.households h where h.id = p_household), '[]'::jsonb),
    'household_members', coalesce((select jsonb_agg(to_jsonb(m) order by m.created_at, m.user_id)
      from public.household_members m where m.household_id = p_household), '[]'::jsonb),
    -- Member accounts' profiles: what other members already see in the app (display name).
    'profiles', coalesce((select jsonb_agg(to_jsonb(p) order by p.created_at, p.id) from public.profiles p
      where p.id in (select m.user_id from public.household_members m where m.household_id = p_household)), '[]'::jsonb),
    'household_invitations', coalesce((select jsonb_agg(to_jsonb(i) - 'code_hash' - 'short_code_hash'
      order by i.created_at, i.id) from public.household_invitations i where i.household_id = p_household), '[]'::jsonb),
    'household_saved_schools', coalesce((select jsonb_agg(to_jsonb(x) order by x.added_at, x.institution_key)
      from public.household_saved_schools x where x.household_id = p_household), '[]'::jsonb),
    -- Billing: plan, status and periods. Provider identifiers and raw provider payloads never leave the server;
    -- receipts and invoices come from the payment provider's customer portal.
    'subscriptions', coalesce((select jsonb_agg(to_jsonb(x) - 'provider_customer_id' - 'provider_subscription_id'
      order by x.created_at, x.id) from public.subscriptions x
      where x.household_id = p_household or (x.household_id is null and x.owner_user_id = any (v_accounts))), '[]'::jsonb),
    'billing_customers', coalesce((select jsonb_agg(to_jsonb(x) - 'provider_customer_id' order by x.created_at)
      from public.billing_customers x where x.household_id = p_household), '[]'::jsonb),
    'billing_events', coalesce((select jsonb_agg(jsonb_build_object('id', e.id, 'provider', e.provider,
      'event_type', e.event_type, 'received_at', e.received_at, 'processed_at', e.processed_at) order by e.id)
      from public.billing_events e
      where e.id = any (array(select jsonb_array_elements_text(v_billing->'event_ids')::bigint))), '[]'::jsonb));
  -- Per-student tables, every key present even with no students.
  v := v || (select jsonb_object_agg(e.key, '[]'::jsonb) from jsonb_each(public.data_request_student_tables(null, true)) e);
  for s in select x.id from public.students x where x.household_id = p_household order by x.created_at, x.id loop
    t := public.data_request_student_tables(s, true);
    for k in select jsonb_object_keys(t) loop
      v := jsonb_set(v, array[k], (v->k) || (t->k));
    end loop;
  end loop;
  return v;
end $$;

create function public.data_request_check_requester(p_requested_by text, p_channel text) returns void
language plpgsql immutable set search_path = '' as $$
begin
  if p_requested_by is null or length(btrim(p_requested_by)) = 0 then
    raise exception 'Record who made the request (p_requested_by): the verified account email' using errcode = '22023';
  end if;
  if p_channel is null or p_channel not in ('email', 'in_app') then
    raise exception 'p_channel must be email or in_app' using errcode = '22023';
  end if;
end $$;

create function public.data_request_check_operator(p_operator text) returns text
language plpgsql immutable set search_path = '' as $$
begin
  if p_operator is null or length(btrim(p_operator)) = 0 then
    raise exception 'Record who is running this (p_operator): your name or email' using errcode = '22023';
  end if;
  return btrim(p_operator);
end $$;

-- The database role (from the request's JWT claims, when called through the API) and the session user.
create function public.data_request_jwt_claims_role() returns text
language plpgsql stable set search_path = '' as $$
begin
  return nullif(current_setting('request.jwt.claims', true), '')::jsonb->>'role';
exception when others then return null;  -- not JSON: fall back to the older single claim
end $$;

create function public.data_request_performed_by() returns text
language sql stable set search_path = '' as $$
  select 'jwt_role=' || coalesce(public.data_request_jwt_claims_role(),
    nullif(current_setting('request.jwt.claim.role', true), ''), '(none)') || '; session_user=' || session_user::text
$$;

-- The student must be the requesting household's (or, with p_household null, have no household).
create function public.data_request_student_in_scope(p_student uuid, p_household uuid) returns public.students
language plpgsql security definer set search_path = '' as $$
declare v public.students;
begin
  if p_student is null then raise exception 'p_student is required' using errcode = '22023'; end if;
  select * into v from public.students s where s.id = p_student for update;
  if not found then raise exception 'No student %', p_student using errcode = 'P0002'; end if;
  if v.household_id is distinct from p_household then
    raise exception 'Student % is not in household %: refused', p_student, coalesce(p_household::text, '(none)')
      using errcode = '42501';
  end if;
  return v;
end $$;

create function public.admin_export_student(p_student uuid, p_household uuid, p_requested_by text, p_operator text,
  p_channel text default 'email', p_requested_at timestamptz default null) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare v_s public.students; v_tables jsonb; v_log uuid; v_operator text;
begin
  perform public.data_request_check_requester(p_requested_by, p_channel);
  v_operator := public.data_request_check_operator(p_operator);
  v_s := public.data_request_student_in_scope(p_student, p_household);
  v_tables := public.data_request_student_tables(p_student, false);
  insert into public.data_request_log(action, subject_kind, subject_id, household_id, requested_by, channel, requested_at,
    operator, performed_by, exported)
  values ('export', 'student', p_student, v_s.household_id, btrim(p_requested_by), p_channel, coalesce(p_requested_at, now()),
    v_operator, public.data_request_performed_by(), public.data_request_count_rows(v_tables))
  returning id into v_log;
  return jsonb_build_object('format', 'collegeprep-data-export/v1', 'generated_at', now(), 'request_id', v_log,
    'subject', jsonb_build_object('kind', 'student', 'id', p_student, 'household_id', v_s.household_id),
    'notes', jsonb_build_array(
      'Practice attempts list question ids and your answers; question text and answer keys are licensed content and are not included.',
      'Other household members'' account ids and guardians'' alert settings are not included in a student export.'),
    'tables', v_tables);
end $$;

create function public.admin_export_household(p_household uuid, p_requested_by text, p_operator text,
  p_channel text default 'email', p_requested_at timestamptz default null) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare v_tables jsonb; v_log uuid; v_operator text;
begin
  perform public.data_request_check_requester(p_requested_by, p_channel);
  v_operator := public.data_request_check_operator(p_operator);
  perform 1 from public.households h where h.id = p_household for share;
  if not found then raise exception 'No household %', p_household using errcode = 'P0002'; end if;
  v_tables := public.data_request_household_tables(p_household);
  insert into public.data_request_log(action, subject_kind, subject_id, household_id, requested_by, channel, requested_at,
    operator, performed_by, exported)
  values ('export', 'household', p_household, p_household, btrim(p_requested_by), p_channel, coalesce(p_requested_at, now()),
    v_operator, public.data_request_performed_by(), public.data_request_count_rows(v_tables))
  returning id into v_log;
  return jsonb_build_object('format', 'collegeprep-data-export/v1', 'generated_at', now(), 'request_id', v_log,
    'subject', jsonb_build_object('kind', 'household', 'id', p_household),
    'notes', jsonb_build_array(
      'Practice attempts list question ids and answers given; question text and answer keys are licensed content and are not included.',
      'Payment-provider identifiers and raw payment events are not included; invoices and receipts are in the billing portal.'),
    'tables', v_tables);
end $$;

-- Deletes one student (p_apply) or reports what would go. Returns removed and kept counts and the auth users the
-- runbook deletes through the admin API.
create function public.data_request_delete_student_internal(p_student uuid, p_apply boolean, p_log uuid) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare v_s public.students; v_auth uuid[] := '{}'; v_removed jsonb; v_kept jsonb;
begin
  select * into v_s from public.students s where s.id = p_student for update;
  if not found then raise exception 'No student %', p_student using errcode = 'P0002'; end if;
  -- The student's own login goes too, unless it belongs to another household or holds a subscription.
  if v_s.linked_user_id is not null
     and not exists (select 1 from public.household_members m where m.user_id = v_s.linked_user_id
                     and m.household_id is distinct from v_s.household_id)
     and not exists (select 1 from public.subscriptions x where x.owner_user_id = v_s.linked_user_id) then
    v_auth := array[v_s.linked_user_id];
  end if;
  v_removed := jsonb_build_object(
    'students', 1,
    'weekly_practice_goals', (select count(*) from public.weekly_practice_goals x where x.student_id = p_student),
    'practice_sessions', (select count(*) from public.practice_sessions x where x.student_id = p_student),
    'practice_session_items', (select count(*) from public.practice_session_items i
      join public.practice_sessions x on x.id = i.session_id where x.student_id = p_student),
    'practice_attempts', (select count(*) from public.practice_attempts x where x.student_id = p_student),
    'practice_attempt_events', (select count(*) from public.practice_attempt_events x where x.student_id = p_student),
    'ai_help_requests', (select count(*) from public.ai_help_requests x where x.student_id = p_student),
    'practice_benchmarks', (select count(*) from public.practice_benchmarks x where x.student_id = p_student),
    'practice_benchmark_items', (select count(*) from public.practice_benchmark_items x where x.student_id = p_student),
    'student_test_scores', (select count(*) from public.student_test_scores x where x.student_id = p_student),
    'student_exam_plan', (select count(*) from public.student_exam_plan x where x.student_id = p_student),
    'student_planning_preferences', (select count(*) from public.student_planning_preferences x where x.student_id = p_student),
    'student_academic_interests', (select count(*) from public.student_academic_interests x where x.student_id = p_student),
    'alert_preferences', (select count(*) from public.alert_preferences x where x.student_id = p_student),
    'household_invitations', (select count(*) from public.household_invitations x where x.student_id = p_student),
    'household_members', (select count(*) from public.household_members m
      where m.user_id = v_s.linked_user_id and m.household_id = v_s.household_id),
    'profiles', (select count(*) from public.profiles p where p.id = any (v_auth)),
    'invitation_code_attempts', (select count(*) from public.invitation_code_attempts a where a.user_id = any (v_auth)));
  v_kept := jsonb_build_object('retained_email_records', (select count(*) from public.household_invitations i
    where i.student_id = p_student and i.recipient_email is not null and i.email_send_count > 0
      and i.last_emailed_at > now() - interval '13 months'));
  if p_apply then
    insert into public.retained_email_records(kind, recipient_email, send_count, last_sent_at, retain_until, data_request_id)
    select 'household_invitation', i.recipient_email, i.email_send_count, i.last_emailed_at,
      i.last_emailed_at + interval '13 months', p_log
    from public.household_invitations i
    where i.student_id = p_student and i.recipient_email is not null and i.email_send_count > 0
      and i.last_emailed_at > now() - interval '13 months';
    delete from public.household_members m where m.user_id = v_s.linked_user_id and m.household_id = v_s.household_id;
    delete from public.profiles p where p.id = any (v_auth);
    delete from public.invitation_code_attempts a where a.user_id = any (v_auth);
    -- Every per-student table references students(id) on delete cascade.
    delete from public.students s where s.id = p_student;
    if exists (select 1 from public.practice_attempts where student_id = p_student)
       or exists (select 1 from public.practice_sessions where student_id = p_student)
       or exists (select 1 from public.practice_attempt_events where student_id = p_student)
       or exists (select 1 from public.household_invitations where student_id = p_student) then
      raise exception 'Student % rows remain after delete', p_student;
    end if;
  end if;
  return jsonb_build_object('removed', v_removed, 'kept', v_kept, 'auth_users_to_delete', to_jsonb(v_auth));
end $$;

create function public.data_request_delete_household_internal(p_household uuid, p_apply boolean, p_log uuid) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare v_removed jsonb := '{}'::jsonb; v_kept jsonb := '{}'::jsonb; v_auth uuid[] := '{}'; v_accounts uuid[];
  v_links uuid[]; v_billing jsonb; v_events bigint[]; r jsonb; s uuid;
begin
  perform 1 from public.households h where h.id = p_household for update;
  if not found then raise exception 'No household %', p_household using errcode = 'P0002'; end if;
  if exists (select 1 from public.subscriptions x where x.household_id = p_household
             and public.data_request_live_subscription(x.provider, x.status)) then
    raise exception 'Household % has a live subscription: cancel it with the payment provider first', p_household
      using errcode = '55000';
  end if;
  select coalesce(array_agg(x.linked_user_id), '{}') into v_links from public.students x
    where x.household_id = p_household and x.linked_user_id is not null;
  v_accounts := public.data_request_household_accounts(p_household);
  if exists (select 1 from public.subscriptions x where x.owner_user_id = any (v_accounts)
             and public.data_request_live_subscription(x.provider, x.status)) then
    raise exception 'A member account of household % owns a live subscription: cancel it first', p_household
      using errcode = '55000';
  end if;
  v_billing := public.data_request_household_billing(p_household, v_accounts);
  v_events := array(select jsonb_array_elements_text(v_billing->'event_ids')::bigint);

  for s in select x.id from public.students x where x.household_id = p_household order by x.created_at, x.id loop
    r := public.data_request_delete_student_internal(s, p_apply, p_log);
    v_removed := public.data_request_add_counts(v_removed, r->'removed');
    v_kept := public.data_request_add_counts(v_kept, r->'kept');
    v_auth := v_auth || array(select jsonb_array_elements_text(r->'auth_users_to_delete')::uuid);
  end loop;

  v_removed := public.data_request_add_counts(v_removed, jsonb_build_object(
    'households', 1,
    'household_members', (select count(*) from public.household_members m where m.household_id = p_household
      and m.user_id <> all (v_links)),
    'household_invitations', (select count(*) from public.household_invitations i
      where i.household_id = p_household and i.student_id is null),
    'household_saved_schools', (select count(*) from public.household_saved_schools x where x.household_id = p_household),
    'billing_customers', (select count(*) from public.billing_customers x where x.household_id = p_household),
    'subscriptions', (select count(*) from public.subscriptions x where x.household_id = p_household
      or (x.household_id is null and x.owner_user_id = any (v_accounts))),
    'profiles', (select count(*) from public.profiles p where p.id = any (v_accounts)),
    'invitation_code_attempts', (select count(*) from public.invitation_code_attempts a where a.user_id = any (v_accounts))));
  v_kept := public.data_request_add_counts(v_kept, jsonb_build_object(
    'retained_email_records', (select count(*) from public.household_invitations i
      where i.household_id = p_household and i.student_id is null and i.recipient_email is not null
        and i.email_send_count > 0 and i.last_emailed_at > now() - interval '13 months'),
    'billing_events', cardinality(v_events)));
  -- Provider references, so the invoices the provider holds can still be found for tax, and so later events about
  -- them are de-identified on arrival (record_billing_event, admin_rescrub_billing_events).
  v_kept := v_kept || jsonb_build_object('billing_event_ids', to_jsonb(v_events), 'billing_refs',
    jsonb_build_object('customers', v_billing->'customers', 'subscriptions', v_billing->'subscriptions'));
  v_auth := v_auth || v_accounts;

  if p_apply then
    insert into public.data_request_billing_refs(request_id, provider, kind, ref)
    select p_log, 'stripe', 'customer', c from jsonb_array_elements_text(v_billing->'customers') c
    union select p_log, 'stripe', 'subscription', x from jsonb_array_elements_text(v_billing->'subscriptions') x
    on conflict do nothing;
    insert into public.retained_email_records(kind, recipient_email, send_count, last_sent_at, retain_until, data_request_id)
    select 'household_invitation', i.recipient_email, i.email_send_count, i.last_emailed_at,
      i.last_emailed_at + interval '13 months', p_log
    from public.household_invitations i
    where i.household_id = p_household and i.student_id is null and i.recipient_email is not null
      and i.email_send_count > 0 and i.last_emailed_at > now() - interval '13 months';
    update public.billing_events e set household_id = null, payload = public.data_request_scrub_billing_payload(e.payload),
      deidentified_at = coalesce(e.deidentified_at, now())
    where e.id = any (v_events);
    delete from public.subscriptions x where x.household_id = p_household
      or (x.household_id is null and x.owner_user_id = any (v_accounts));
    delete from public.profiles p where p.id = any (v_accounts);
    delete from public.invitation_code_attempts a where a.user_id = any (v_accounts);
    -- Cascades household_members, household_invitations, household_saved_schools and billing_customers.
    delete from public.households h where h.id = p_household;
  end if;
  return jsonb_build_object('removed', v_removed, 'kept', v_kept, 'auth_users_to_delete', to_jsonb(v_auth));
end $$;

create function public.data_request_check_live(p_dry_run boolean, p_confirm uuid, p_subject uuid, p_operator text)
returns text language plpgsql immutable set search_path = '' as $$
begin
  if p_dry_run is null then raise exception 'p_dry_run must be true or false' using errcode = '22023'; end if;
  if p_dry_run then return null; end if;
  if p_confirm is distinct from p_subject then
    raise exception 'A live deletion needs p_confirm => % (the id being deleted); run with p_dry_run => true first', p_subject
      using errcode = '22023';
  end if;
  return public.data_request_check_operator(p_operator);
end $$;

create function public.admin_delete_student(p_student uuid, p_reason text, p_household uuid, p_requested_by text,
  p_dry_run boolean default true, p_confirm uuid default null, p_operator text default null,
  p_channel text default 'email', p_requested_at timestamptz default null) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare v_s public.students; v_log uuid; r jsonb; v_operator text;
begin
  perform public.data_request_check_requester(p_requested_by, p_channel);
  if p_reason is null or length(btrim(p_reason)) = 0 then raise exception 'p_reason is required' using errcode = '22023'; end if;
  v_operator := public.data_request_check_live(p_dry_run, p_confirm, p_student, p_operator);
  v_s := public.data_request_student_in_scope(p_student, p_household);
  if p_dry_run then
    return public.data_request_delete_student_internal(p_student, false, null)
      || jsonb_build_object('dry_run', true, 'subject', jsonb_build_object('kind', 'student', 'id', p_student));
  end if;
  insert into public.data_request_log(action, subject_kind, subject_id, household_id, requested_by, channel, reason,
    requested_at, operator, performed_by)
  values ('delete', 'student', p_student, v_s.household_id, btrim(p_requested_by), p_channel, btrim(p_reason),
    coalesce(p_requested_at, now()), v_operator, public.data_request_performed_by())
  returning id into v_log;
  r := public.data_request_delete_student_internal(p_student, true, v_log);
  update public.data_request_log l set removed = r->'removed', kept = r->'kept',
    auth_users_to_delete = array(select jsonb_array_elements_text(r->'auth_users_to_delete')::uuid)
  where l.id = v_log;
  return r || jsonb_build_object('dry_run', false, 'request_id', v_log,
    'subject', jsonb_build_object('kind', 'student', 'id', p_student));
end $$;

create function public.admin_delete_household(p_household uuid, p_reason text, p_requested_by text,
  p_dry_run boolean default true, p_confirm uuid default null, p_operator text default null,
  p_channel text default 'email', p_requested_at timestamptz default null) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare v_log uuid; r jsonb; v_operator text;
begin
  perform public.data_request_check_requester(p_requested_by, p_channel);
  if p_reason is null or length(btrim(p_reason)) = 0 then raise exception 'p_reason is required' using errcode = '22023'; end if;
  v_operator := public.data_request_check_live(p_dry_run, p_confirm, p_household, p_operator);
  if p_dry_run then
    return public.data_request_delete_household_internal(p_household, false, null)
      || jsonb_build_object('dry_run', true, 'subject', jsonb_build_object('kind', 'household', 'id', p_household));
  end if;
  insert into public.data_request_log(action, subject_kind, subject_id, household_id, requested_by, channel, reason,
    requested_at, operator, performed_by)
  values ('delete', 'household', p_household, p_household, btrim(p_requested_by), p_channel, btrim(p_reason),
    coalesce(p_requested_at, now()), v_operator, public.data_request_performed_by())
  returning id into v_log;
  r := public.data_request_delete_household_internal(p_household, true, v_log);
  update public.data_request_log l set removed = r->'removed', kept = r->'kept',
    auth_users_to_delete = array(select jsonb_array_elements_text(r->'auth_users_to_delete')::uuid)
  where l.id = v_log;
  return r || jsonb_build_object('dry_run', false, 'request_id', v_log,
    'subject', jsonb_build_object('kind', 'household', 'id', p_household));
end $$;

-- After the admin-API deletion: refuses while any listed auth user still exists.
create function public.admin_record_auth_deletion(p_request uuid) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare v public.data_request_log; v_left uuid[];
begin
  select * into v from public.data_request_log l where l.id = p_request and l.action = 'delete' for update;
  if not found then raise exception 'No deletion request %', p_request using errcode = 'P0002'; end if;
  select coalesce(array_agg(u.id), '{}') into v_left from auth.users u where u.id = any (v.auth_users_to_delete);
  if cardinality(v_left) > 0 then
    raise exception 'Auth users still exist: %; delete them through the admin API first', v_left using errcode = '55000';
  end if;
  update public.data_request_log l set auth_users_deleted_at = coalesce(l.auth_users_deleted_at, now())
  where l.id = p_request returning * into v;
  return jsonb_build_object('request_id', v.id, 'auth_users_deleted_at', v.auth_users_deleted_at,
    'auth_users', to_jsonb(v.auth_users_to_delete));
end $$;

-- After the provider's retry window (Stripe: about 3 days): de-identify any payment event about the deleted
-- household that arrived, or was retried, after the deletion. Returns how many events it changed.
create function public.admin_rescrub_billing_events(p_request uuid) returns integer
language plpgsql security definer set search_path = '' as $$
declare v public.data_request_log; v_refs text[]; n integer;
begin
  select * into v from public.data_request_log l
  where l.id = p_request and l.action = 'delete' and l.subject_kind = 'household' for update;
  if not found then raise exception 'No household deletion request %', p_request using errcode = 'P0002'; end if;
  select coalesce(array_agg(r.ref), '{}') into v_refs from public.data_request_billing_refs r where r.request_id = p_request;
  update public.billing_events e set household_id = null, payload = public.data_request_scrub_billing_payload(e.payload),
    deidentified_at = now()
  where (e.household_id = v.household_id or e.provider_subscription_id = any (v_refs)
         or public.data_request_payload_strings(e.payload) && v_refs)
    and (e.household_id is not null or e.deidentified_at is null
         or e.payload is distinct from public.data_request_scrub_billing_payload(e.payload));
  get diagnostics n = row_count;
  update public.data_request_log l set billing_rescrubbed_at = now() where l.id = p_request;
  return n;
end $$;

create function public.admin_purge_expired_retention() returns integer
language plpgsql security definer set search_path = '' as $$
declare n integer;
begin
  delete from public.retained_email_records r where r.retain_until <= now();
  get diagnostics n = row_count;
  return n;
end $$;

-- The Stripe webhook's insert (supabase/functions/stripe-webhook): exactly once per provider event, and stored
-- already de-identified when it refers to a deleted household's customer or subscription. Returns the new row id,
-- or null when the event was already recorded.
create function public.record_billing_event(p_provider text, p_event_id text, p_event_type text,
  p_subscription_id text, p_payload jsonb) returns bigint
language plpgsql security definer set search_path = '' as $$
declare v_deleted boolean := public.data_request_event_is_deleted(p_payload, p_subscription_id); v_id bigint;
begin
  insert into public.billing_events(provider, event_id, event_type, provider_subscription_id, payload, deidentified_at)
  values (p_provider, p_event_id, p_event_type, p_subscription_id,
    case when v_deleted then public.data_request_scrub_billing_payload(p_payload) else p_payload end,
    case when v_deleted then now() end)
  on conflict (provider, event_id) do nothing
  returning id into v_id;
  return v_id;
end $$;

-- The webhook's call for an event whose household does not exist (deleted, or never ours).
create function public.deidentify_billing_event(p_provider text, p_event_id text) returns boolean
language plpgsql security definer set search_path = '' as $$
begin
  update public.billing_events e set household_id = null, payload = public.data_request_scrub_billing_payload(e.payload),
    deidentified_at = coalesce(e.deidentified_at, now())
  where e.provider = p_provider and e.event_id = p_event_id;
  return found;
end $$;

-- Privileges: nothing for clients; service_role gets only the entry points.
do $$
declare f regprocedure;
begin
  for f in select p.oid::regprocedure from pg_proc p join pg_namespace n on n.oid = p.pronamespace
           where n.nspname = 'public' and (p.proname like 'data\_request\_%' or p.proname like 'admin\_%'
             or p.proname in ('record_billing_event', 'deidentify_billing_event')) loop
    execute format('revoke all on function %s from public, anon, authenticated, service_role', f);
  end loop;
end $$;
grant execute on function public.admin_export_student(uuid, uuid, text, text, text, timestamptz) to service_role;
grant execute on function public.admin_export_household(uuid, text, text, text, timestamptz) to service_role;
grant execute on function public.admin_delete_student(uuid, text, uuid, text, boolean, uuid, text, text, timestamptz) to service_role;
grant execute on function public.admin_delete_household(uuid, text, text, boolean, uuid, text, text, timestamptz) to service_role;
grant execute on function public.admin_record_auth_deletion(uuid) to service_role;
grant execute on function public.admin_rescrub_billing_events(uuid) to service_role;
grant execute on function public.admin_purge_expired_retention() to service_role;
grant execute on function public.record_billing_event(text, text, text, text, jsonb) to service_role;
grant execute on function public.deidentify_billing_event(text, text) to service_role;
