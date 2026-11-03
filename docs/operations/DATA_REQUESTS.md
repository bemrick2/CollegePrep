# Data export and deletion requests (runbook)

Launch checklist A4; #218 B8. Owner decisions: `docs/legal/DECISIONS.md` #6 (manual by email at launch, in-app soon) and #5 (retention). This runbook is not legal advice. Items marked **[[OWNER/COUNSEL]]** need confirmation before launch.

The database side is in `supabase/migrations/20261102070000_data_requests.sql` and is tested by `supabase/tests/data_requests.sql`. The test runs in the CI `database` job twice: on plain PostgreSQL, and under Supabase's default privileges.

**Status:** the procedure is in the repository but **not applied on hosted**. The Supabase hold is in place (`docs/SUPABASE_PAUSE.md`). When the hold lifts:
1. Apply the migration before deploying `supabase/functions/stripe-webhook`. The webhook now records events through `record_billing_event`, and fails (Stripe retries) until that function exists.
2. Then deploy the functions.

## At a glance

| Step | What | Where |
|---|---|---|
| 1 | Receive the request at the privacy address and acknowledge it | Privacy mailbox |
| 2 | Verify the requester against the account email on file | `psql` (read only) |
| 3 | Export (always offered before a deletion) | `admin_export_student` / `admin_export_household`, saved with `psql \copy` |
| 4 | For a household with a paid subscription, cancel it immediately with the payment provider | Stripe dashboard |
| 5 | Dry run the deletion, then run it live | `admin_delete_student` / `admin_delete_household` |
| 6 | Straight away: re-check the account list, then delete those auth accounts through the admin API | Supabase dashboard or Auth admin API |
| 7 | Record the auth deletion; reply to the requester | `admin_record_auth_deletion`; privacy mailbox |
| 8 | About 3 days later (Stripe's retry window), re-scrub late payment events | `admin_rescrub_billing_events` |

## Response time

**We complete a request within 30 days of receiving it.** This is the default because it matches the 30-day practice-history rule in decision #5. **[[OWNER/COUNSEL: confirm 30 days, and whether state law needs a shorter or a different window. CCPA, for example, allows 45 days with acknowledgement within 10 business days.]]**

Acknowledge the request within 5 business days. **[[OWNER/COUNSEL: confirm.]]** Use the date the request arrived as `p_requested_at`, so the log shows how long it took.

## 1. Who may ask for what (verification)

Act only on a request that comes from, or is confirmed from, **the email address on the Supabase Auth account**. Never act on an address that is not on file. If the request came from another address, reply to the account email and ask the person to confirm from there.

Find the account and its household (read only):

```sql
select u.id as user_id, m.household_id, m.role, h.created_by = u.id as is_account_holder,
       m.can_manage_students, m.can_manage_members, m.can_manage_billing
from auth.users u
left join public.household_members m on m.user_id = u.id
left join public.households h on h.id = m.household_id
where lower(u.email) = lower('person@example.com');

select id, display_name, linked_user_id, graduation_year, created_at
from public.students where household_id = '<household id>';
```

| Requester | Export | Delete |
|---|---|---|
| Household account holder (`households.created_by`) | The household | The household, or one of its students |
| Guardian with manage-students | One of the household's students | One of the household's students |
| Other guardian (view-only and similar) | Their own account data only; ask the account holder for the household | Leaving the household is done in the app; deleting their account goes through the account holder **[[OWNER: confirm]]** |
| Student 13–17 with their own login | Their own student data (`admin_export_student`) | Confirm with a guardian of the household before deleting **[[COUNSEL: confirm]]** |
| Student 18+, or an independent student (no household) | Their own student data | Their own student profile and login |

- Students must be 13 or older (decision #1). If you learn a student is under 13, tell the owner. Deleting that student's data at the guardian's request follows the same steps.
- Parents of students under 18 can review or delete their child's information (privacy draft).
- A student is always deleted **within the requester's household**. The functions refuse a student from a different household, and refuse a household student when the call passes no household.

## 2. Running the functions

**Use `psql`** on the production project's direct connection, as the database owner (`postgres`). Do not use the dashboard SQL editor for exports: it truncates large results and keeps query history in the browser. Check the project ref in the connection string first, so you never run this against the wrong project.

Every `admin_*` function is service-role only. Clients (anon and signed-in users) cannot call them or read the request tables. Each call is one transaction: it completes fully or changes nothing.

Every export and every live deletion needs **`p_operator`**: your own name or email. It is stored in the log next to `performed_by`, which records the database role and session the call ran as.

### Export

Save the document straight to a file with psql's `\o`, never by copying from a results grid:

```sh
psql "$PROD_DB_URL" -v ON_ERROR_STOP=1 <<'SQL'
\pset tuples_only on
\pset format unaligned
\o export-household.json
select public.admin_export_household(
  p_household    => '<household id>',
  p_requested_by => 'parent@example.com',            -- the verified account email
  p_operator     => 'you@example.com',               -- who is running this
  p_requested_at => '2026-11-02 14:05+00');          -- when the request arrived
\o
SQL
```

For one student (to a guardian of that household, or to the student), the call is `public.admin_export_student(p_student => '<student id>', p_household => '<household id>', p_requested_by => …, p_operator => …, p_requested_at => …)`. Pass `p_household => null` only for an independent student.

Prefer `\o` to `\copy (select …) to 'file'`: COPY's text format doubles every backslash, which corrupts JSON. Check the file with `jq . export-household.json` before sending it.

What the export contains:

- One JSON document (`format: collegeprep-data-export/v1`). Under `tables` it holds every row about the student or household.
- A household export holds:
  - the household, its members, and the members' profiles;
  - its invitations and saved schools;
  - subscription status and periods, including the personal subscriptions of member accounts that go with it;
  - a summary of every payment event the deletion would keep;
  - every student's practice history, goals, plans, scores and alert settings.
- A student export leaves out guardians' alert settings and other accounts' ids.
- No export includes:
  - invitation code digests;
  - question text or answer keys (attempts list question ids and the answers given);
  - payment-provider ids or raw payment events. Invoices are in the Stripe customer portal.

How to deliver it:

1. Rename the file to `export-<request id>.json`. The request id is in the document.
2. Send it only to the verified account email, as an encrypted attachment or a link that expires. **[[OWNER: choose the delivery method.]]**
3. Delete your local copy once it is delivered.

Each export writes a `data_request_log` row with the row counts per table.

### Delete

Always offer the export first.

**Cancel paid subscriptions first.** These statuses refuse the deletion: `trialing`, `active`, `past_due`, `unpaid`, `paused`, `incomplete`, `grace` and `billing_retry`. That covers the household's subscriptions and the personal subscriptions of any member account that would be deleted.
- **Stripe:** in the dashboard, choose **Cancel immediately**, not "at period end". Refund per the terms. Wait until the webhook shows `status = 'canceled'` in `public.subscriptions`.
- **Apple** (later): the user cancels through Apple. The `grace` and `billing_retry` statuses keep blocking until Apple reports the subscription expired.
- **Complimentary (`provider = 'comp'`):** these bill nothing and never block. They are deleted with the household, and there are no payment events to keep.

1. **Dry run.** This is the default. It changes nothing (the test checks every personal, billing and request table byte for byte) and writes no log row. Read the counts, `kept` and `auth_users_to_delete`.

   ```sql
   select public.admin_delete_household(
     p_household    => '<household id>',
     p_reason       => 'Account holder asked by email to delete the household',
     p_requested_by => 'parent@example.com');

   select public.admin_delete_student(
     p_student      => '<student id>',
     p_reason       => 'Guardian asked by email to delete one student profile',
     p_household    => '<household id>',             -- null only for an independent student
     p_requested_by => 'parent@example.com');
   ```

   Do not put names in `p_reason`. The log keeps ids and counts, not personal details.

2. **Live run.** The same call with `p_dry_run => false`, `p_confirm =>` the same id, and `p_operator`. Without all three, the call refuses.

   ```sql
   select public.admin_delete_household(
     p_household    => '<household id>',
     p_reason       => 'Account holder asked by email to delete the household',
     p_requested_by => 'parent@example.com',
     p_requested_at => '2026-11-02 14:05+00',
     p_dry_run      => false,
     p_confirm      => '<household id>',
     p_operator     => 'you@example.com');
   ```

   Keep the returned `request_id` and `auth_users_to_delete`.

3. **Straight away, delete the auth accounts** listed in `auth_users_to_delete`. Do it in the same sitting: until then, a listed person could still sign in to an empty account.

   First re-check the list. Every listed account must still belong to nothing (no household membership, no linked student, no subscription); this query should return no rows:

   ```sql
   select u.id from unnest('{<id1>,<id2>}'::uuid[]) u(id)
   where exists (select 1 from public.household_members m where m.user_id = u.id)
      or exists (select 1 from public.students s where s.linked_user_id = u.id)
      or exists (select 1 from public.subscriptions x where x.owner_user_id = u.id);
   ```

   If it returns a row, that person joined something since the deletion: do not delete that account, and note it in the request thread.

   Then delete each account through the Supabase Auth admin API, not SQL. The admin API also removes the account's identities, sessions and refresh tokens. Use either:
   - Dashboard: Authentication → Users → the user → Delete user.
   - API, from a trusted machine:

     ```sh
     curl -X DELETE "https://<project-ref>.supabase.co/auth/v1/admin/users/<user id>" \
       -H "apikey: $SUPABASE_SERVICE_ROLE_KEY" -H "Authorization: Bearer $SUPABASE_SERVICE_ROLE_KEY"
     ```

     The equivalent call is `supabase.auth.admin.deleteUser('<user id>')` with a service-role client.

   The list only names accounts that belong to nothing else. A guardian who is also in another household keeps their account, and only this household's membership is removed. A student login that holds a subscription is kept too. The deletion has already removed the listed accounts' profiles and rate-limit rows.

4. **Record the auth deletion.** This refuses while any listed account still exists.

   ```sql
   select public.admin_record_auth_deletion('<request id>');
   ```

5. **About 3 days later, re-scrub** (households with payment history only). Stripe retries failed webhook deliveries for up to 3 days.
   - The webhook already stores any event that names the deleted household's customer or subscription ids in de-identified form.
   - It also de-identifies events for a household that no longer exists.
   - The re-scrub catches anything else that arrived about the deleted household, and is safe to repeat. It returns the number of events it changed (normally 0).

   ```sql
   select public.admin_rescrub_billing_events('<request id>');
   ```

## 3. What is removed and what is kept

| Data | On deletion | Why |
|---|---|---|
| Student profile, practice sessions, items, attempts, attempt events, AI-help requests, progress checks and their items, weekly goals, test scores, exam plan, planning preferences, academic interests, guardians' alert settings for the student | **Deleted at once** (within the 30 days of decision #5) | Practice history rule |
| Household, memberships, invitations, saved schools, subscription state (Stripe, comp, and departing accounts' personal subscriptions), payment-customer map | **Deleted** | Personal data |
| Account profiles and invitation-code rate-limit rows of the accounts listed for deletion | **Deleted**; the auth account itself through the admin API | Personal data |
| Payment events (`billing_events`) linked to the household, to its or a departing account's subscriptions, or naming their customer or subscription ids | **Kept, de-identified** (see below) | Billing records are kept as tax law requires (decision #5) **[[COUNSEL: confirm the period, often 7 years]]** |
| Payment-provider customer and subscription ids | **Kept** in `data_request_billing_refs` and in the request's `data_request_log.kept.billing_refs` | Lets the invoices Stripe holds be found for tax, and later events about them be de-identified on arrival |
| Invitation emails sent in the last 13 months | **Kept** in `retained_email_records`: recipient address, send count, last sent time. No link to any account. Removed by `admin_purge_expired_retention()` after 13 months | Email-sent records are kept 13 months (decision #5) |
| `data_request_log` | **Kept**: ids, counts, requester email, operator, reason, dates | Record that the request was handled **[[COUNSEL: retention period for request records, e.g. 24 months under CCPA regulations]]** |

**De-identifying a payment event.** The household link is cleared and `deidentified_at` is set. The payload keeps **only** an allow-list of keys, at any depth (`data_request_billing_kept_keys()` in the migration):

| Kind | Keys |
|---|---|
| Event envelope and object types | `id`, `object`, `type`, `api_version`, `created`, `livemode`, `pending_webhooks`, `request.id` |
| Containers | `data`, `previous_attributes`, `lines`, `items`, `period`, `price`, `plan`, `recurring`, `product`, `parent`, `subscription_details`, `pricing`, `price_details`, `status_transitions`, `total_details`, tax-amount lists, `tax_rate`, `has_more`, `total_count` |
| Provider ids | `customer`, `subscription`, `subscription_item`, `invoice`, `invoice_item`, `payment_intent`, `charge`, `latest_invoice`, `lookup_key`; the invoice `number` |
| Amounts and tax | every `amount*` field, `subtotal*`, `total*`, `tax`, `currency`, `unit_amount*`, `quantity`, `percentage`, `inclusive`, `taxable_amount`, `taxability_reason`, `tax_behavior`, `proration` |
| Status | `status`, `billing_reason`, `collection_method`, `mode`, `payment_status`, `paid`, `attempted`, `attempt_count`, `interval`, `interval_count`, `cancel_at_period_end` |
| Timestamps | period, trial, cancel, due, finalized, paid, voided and expiry times |

Everything else is dropped, including:
- names, emails and phones, addresses, and customer and collected information;
- shipping and billing details;
- card details (`last4`, `exp_*`, `fingerprint`, `brand`);
- receipt email, number and URL; hosted invoice URLs and PDFs;
- metadata, descriptions, footers and custom fields;
- tax ids, success URLs and idempotency keys.

Outside the database:

- **Stripe.** Do not delete the Stripe customer: Stripe holds the invoices that the tax rule needs. **[[OWNER/COUNSEL: whether to redact the customer's name and email in Stripe after cancellation.]]**
- **Resend (email).** Resend keeps its own delivery logs under its retention settings. If the address is in a Resend audience or contact list, remove it. Keep any suppression entry (an unsubscribe or bounce): it stops future mail. **[[OWNER: confirm Resend log retention.]]**
- **Backups.** Deleted rows remain in Supabase backups and point-in-time recovery until those roll off, as set by the project's plan. **[[OWNER: confirm the backup window, and that it is within the stated response time or disclosed.]]**
- **The privacy mailbox.** Keep the request thread with the request id. It is the record of verification.

## 4. Recording the request

- Every export and live deletion writes one `data_request_log` row. Dry runs and refused calls write none. The row holds:
  - `action`, `subject_kind` and `subject_id`;
  - `household_id`;
  - `requested_by` (the verified account email) and `channel` (`email` now, `in_app` later);
  - `reason`;
  - `requested_at` (received) and `performed_at`;
  - `operator` (you) and `performed_by` (the JWT role, from `request.jwt.claims`, and the session user);
  - `exported`, `removed` and `kept` (counts, the kept payment-event ids, the billing references);
  - `auth_users_to_delete`, `auth_users_deleted_at` and `billing_rescrubbed_at`.
- Only these functions write the request tables. service_role can read them but not change them.
- Reply to the requester with what was exported or deleted, and what was kept and why (the tables above). Use the request id as the reference.
- A request is complete when:
  - its log row exists;
  - `auth_users_deleted_at` is set, for deletions that listed accounts;
  - `billing_rescrubbed_at` is set, for households with payment history;
  - the reply is sent.

Open deletions:

```sql
select id, subject_kind, subject_id, requested_at, performed_at, auth_users_to_delete,
       auth_users_deleted_at, billing_rescrubbed_at
from public.data_request_log
where action = 'delete'
  and ((cardinality(auth_users_to_delete) > 0 and auth_users_deleted_at is null)
       or (subject_kind = 'household' and (kept->>'billing_events')::int > 0 and billing_rescrubbed_at is null));
```

Monthly, remove email-sent records past their 13 months:

```sql
select public.admin_purge_expired_retention();
```

## 5. Keeping this complete

`supabase/tests/data_requests.sql` lists a decision for every table in the database:

- personal;
- retained;
- security (deleted, not exported);
- request record;
- reference (not personal).

It fails CI when a new table has no decision. When a migration adds a table that holds personal data, do all of the following in the same change:

- add it to `data_request_student_tables` or `data_request_household_tables`, and to the matching delete function;
- add it to the test's decision list;
- add it to section 3 above.

Proposals that will need this when adopted as migrations:

- CR-22, `parent_email_deliveries`. These are email-sent records, so they are kept 13 months. The proposed `on delete cascade` from `auth.users` would drop them early.
- CR-27: `notification_devices` (push tokens, deleted, never exported) and `practice_reminder_*`.

## 6. In-app deletion and export later (Apple 5.1.1(v))

The in-app path reuses these functions. It needs a client RPC that is `security definer`, which works like this:

1. It checks `auth.uid()` against the same rules as section 1 (the account holder for a household, manage-students for a student, the linked login for its own student).
2. It calls `admin_delete_*` or `admin_export_*` with:
   - `p_channel => 'in_app'`;
   - `p_requested_by` and `p_operator` set to the account email;
   - `p_confirm` set to the id.

The definer runs as the owner, so no client grant on the `admin_*` functions is needed. The auth-account step then runs in an Edge Function with the service role, using `auth.admin.deleteUser`. Design owns the UI: a confirmation screen, an export download, and the 'what we keep' text from section 3.
