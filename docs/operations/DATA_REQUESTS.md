# Data export and deletion requests (runbook)

Launch checklist A4; #218 B8. Owner decisions: `docs/legal/DECISIONS.md` #6 (manual by email at launch, in-app soon) and #5 (retention). This runbook is not legal advice.

**Nothing marked OPEN is settled policy.** Each such value is a placeholder chosen so the procedure can run end to end. All of them are listed in section 0 and need an owner or counsel decision before launch.

The database side is in `supabase/migrations/20261102070000_data_requests.sql` and is tested by `supabase/tests/data_requests.sql`. The test runs in the CI `database` job twice: on plain PostgreSQL, and under Supabase's default privileges.

**Status:** the procedure is in the repository but **not applied on hosted**. The Supabase hold is in place (`docs/SUPABASE_PAUSE.md`). When the hold lifts:
1. Apply the migration before deploying `supabase/functions/stripe-webhook`. The webhook now records events through `record_billing_event`, and fails (Stripe retries) until that function exists.
2. Then deploy the functions.

## At a glance

| Step | What | Where |
|---|---|---|
| 1 | Receive the request at the privacy address and acknowledge it | Privacy mailbox |
| 2 | Verify the requester against the account email on file | `psql` (read only) |
| 3 | Export (always offered before a deletion) | `admin_export_student` / `admin_export_household`, saved with psql `\o` |
| 4 | For a household with a paid subscription, cancel it immediately with the payment provider | Stripe dashboard |
| 5 | Dry run the deletion, then run it live | `admin_delete_student` / `admin_delete_household` |
| 6 | Straight away: re-check the account list, then delete those auth accounts through the admin API | Supabase dashboard or Auth admin API |
| 7 | Record the auth deletion; reply to the requester | `admin_record_auth_deletion`; privacy mailbox |
| 8 | About 3 days later (Stripe's retry window), re-scrub late payment events | `admin_rescrub_billing_events` (a manual step: section 7) |

## 0. OPEN for owner and counsel

None of these is decided. Until each one is, the value used in this runbook is a **placeholder**: it must not be quoted to families or put in the privacy policy as settled.

| # | Choice | Placeholder used here | Who decides |
|---|---|---|---|
| O1 | **Response deadline** to complete a request | 30 days from receipt. Chosen only because it matches the 30-day practice-history rule in decision #5. State laws differ; CCPA, for example, allows 45 days. | Owner + counsel |
| O2 | **Acknowledgement deadline** | 5 business days. CCPA, for example, uses 10. | Owner + counsel |
| O3 | **Requester authority: a guardian who is not the account holder** | They can export their own account data only. Their account is deleted through the account holder. | Owner + counsel |
| O4 | **Requester authority: a student aged 13–17 with their own login** | Their own export only. For a deletion, confirm with a guardian of the household first. | Counsel |
| O5 | **Export delivery** | An encrypted attachment or an expiring link, sent only to the verified account email. No method has been chosen. | Owner |
| O6 | **Billing record retention period** | Kept de-identified "as tax law requires". No period is set (7 years is common). Nothing purges billing events yet. | Counsel |
| O7 | **Request-log retention period** (`data_request_log`, `data_request_billing_refs`) | Kept indefinitely; no purge exists. CCPA regulations, for example, require 24 months of request records. | Counsel |
| O8 | **Stripe redaction**: whether to redact the customer's name and email in Stripe after a deletion | Not redacted. The Stripe customer is kept because it holds the invoices. | Owner + counsel |
| O9 | **Resend log retention** | Whatever Resend's account settings are; not checked. | Owner |
| O10 | **Backup and point-in-time-recovery window** | Unknown. Deleted rows stay in Supabase backups until they roll off. | Owner (confirm the plan's window, and whether it fits O1 or must be disclosed) |

Use the date the request arrived as `p_requested_at`, so the log shows how long each request took against whatever O1 becomes.

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
| Other guardian (view-only and similar) | Their own account data only; ask the account holder for the household (**OPEN O3**) | Leaving the household is done in the app; deleting their account goes through the account holder (**OPEN O3**) |
| Student 13–17 with their own login | Their own student data (`admin_export_student`) (**OPEN O4**) | Confirm with a guardian of the household before deleting (**OPEN O4**) |
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
  - the household (including its home state), its members, and the members' profiles;
  - its invitations and saved schools;
  - subscription status and periods, including the personal subscriptions of member accounts that go with it;
  - a summary of every payment event the deletion would keep;
  - every student's profile (including home state), practice history (including whether each served item had been seen before, and when), goals, plans (including exam intent, planned test date and study days), scores, setup progress, reminder settings, reminder changes and reminder deliveries (without the device), and alert settings (including the weekly-digest choice);
  - the question reports about each student. A reporter's id and note are shown only when the reporter is a member of the household; the editor's name, resolution note and whether the item is reserved never are;
  - the parent emails sent to the household's guardians: alerts about its students, reminders-off notices, and the weekly digests of accounts that belong to no other household.
- Both exports carry a `derived.skill_estimates` section: the per-skill estimates the app computes from the attempts, including CR-23's first-answer count and accuracy. They are not stored, so there is nothing to delete beyond the attempts.
- A student who moved from another household brings rows that name that household and its people. In a household export, `household_id` and the actor ids (`set_by`, `entered_by`, `requested_by`, `changed_by`, `updated_by`, `user_id`) are cleared unless they are this household or its members (`data_request_mask_foreign`).
- A student export leaves out guardians' alert settings and other accounts' ids. It shows the student's own question reports in full, and guardians' reports about the student without the reporter or the note.
- No export includes:
  - invitation code digests;
  - question text or answer keys (attempts list question ids and the answers given);
  - payment-provider ids or raw payment events. Invoices are in the Stripe customer portal;
  - push devices (endpoints, keys, tokens, handles): security records, never exported.

The test (`dr_columns` in `supabase/tests/data_requests.sql`) lists every column of every personal, retained and security table as exported or omitted. It fails when a new column has no decision.

How to deliver it (**OPEN O5**):

1. Rename the file to `export-<request id>.json`. The request id is in the document.
2. Send it only to the verified account email. The placeholder is an encrypted attachment or a link that expires; the method is **OPEN O5**.
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
| Student profile, practice sessions, items, attempts, attempt events, AI-help requests, progress checks and their items, weekly goals, test scores, exam plan, planning preferences, academic interests, setup progress, reminder settings, reminder changes, reminder deliveries, question reports about the student, guardians' alert settings for the student | **Deleted at once** (within the 30 days of decision #5) | Practice history rule |
| Question reports filed by a departing account about a student who stays (for example a student who has moved to another household) | **Kept** for the editors **without the reporter or the note**. Reason, status, review and revision are unchanged | The report is about the question, not the reporter. A closed report's guard (CR-25) refuses note changes even from the service role; the data-request functions use its one exemption (below) |
| Household, memberships, invitations, saved schools, subscription state (Stripe, comp, and departing accounts' personal subscriptions), payment-customer map | **Deleted** | Personal data |
| Account profiles, invitation-code rate-limit rows and push devices (`notification_devices`: endpoint, keys, token, handle) of the accounts listed for deletion | **Deleted**; never exported; the auth account itself through the admin API | Personal and security data |
| Payment events (`billing_events`) linked to the household, to its or a departing account's subscriptions, or naming their customer or subscription ids | **Kept, de-identified** (see below) | Billing records are kept as tax law requires (decision #5); the period is **OPEN O6** |
| Payment-provider customer and subscription ids | **Kept** in `data_request_billing_refs` and in the request's `data_request_log.kept.billing_refs` | Lets the invoices Stripe holds be found for tax, and later events about them be de-identified on arrival |
| Invitation emails sent in the last 13 months | **Kept** in `retained_email_records`: recipient address, send count, last sent time. No link to any account. Removed by `admin_purge_expired_retention()` after 13 months | Email-sent records are kept 13 months (decision #5) |
| Parent emails (`parent_email_deliveries`: weekly digests, inactivity alerts, reminders-off notices) | **Kept, de-identified.** A departing account's records lose `user_id`. Any inactivity key that names a deleted student (`<student id>:<last practice>`) becomes `deleted-<the record's own id>:<last practice>`, which links to no one and stays unique. A guardian who stays keeps their records, without the student's id. Every record is removed by `admin_purge_expired_retention()` 13 months after it was sent | Email-sent records are kept 13 months (decision #5) |
| `data_request_log` | **Kept**: ids, counts, requester email, operator, reason, dates | Record that the request was handled; the period is **OPEN O7** |

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

- **Stripe.** Do not delete the Stripe customer: Stripe holds the invoices that the tax rule needs. Whether to redact the customer's name and email in Stripe is **OPEN O8**.
- **Resend (email).** Resend keeps its own delivery logs under its retention settings (**OPEN O9**). If the address is in a Resend audience or contact list, remove it. Keep any suppression entry (an unsubscribe or bounce): it stops future mail.
- **Push services.** A deleted device's endpoint or token is simply never used again; the browser or FCM expires it.
- **Backups.** Deleted rows remain in Supabase backups and point-in-time recovery until those roll off, as set by the project's plan (**OPEN O10**).
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

The monthly purge and the 3-day re-scrub are operational jobs: see section 7.

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

CR-25 (#295) `question_reports` is personal. Its closed-report guard (`question_reports_closed_guard`) has one exemption, which this migration adds. While `data_request_deidentify_reports` runs, it sets the transaction-local setting `collegeprep.data_request_deidentify`, and the guard then lets a closed report's **note be cleared**. Nothing else may change: reason, revision and updated_at stay fixed, and with the setting on, any other change is still refused. The function clears the setting before it returns. The test checks all of this.

CR-15 and CR-23 (#295): `households.home_state`, `students.home_state` and `practice_session_items.seen_before`/`last_seen` are exported. The first-answer metrics are exported as derived data.

CR-22, CR-26 and CR-27 (#298) are covered: setup progress and the reminder tables are personal; `parent_email_deliveries` is retained (13 months, de-identified); `notification_devices` is security (deleted, never exported).

## 6. In-app deletion and export later (Apple 5.1.1(v))

The in-app path reuses these functions. It needs a client RPC that is `security definer`, which works like this:

1. It checks `auth.uid()` against the same rules as section 1 (the account holder for a household, manage-students for a student, the linked login for its own student).
2. It calls `admin_delete_*` or `admin_export_*` with:
   - `p_channel => 'in_app'`;
   - `p_requested_by` and `p_operator` set to the account email;
   - `p_confirm` set to the id.

The definer runs as the owner, so no client grant on the `admin_*` functions is needed. The auth-account step then runs in an Edge Function with the service role, using `auth.admin.deleteUser`. Design owns the UI: a confirmation screen, an export download, and the 'what we keep' text from section 3.

## 7. Operational jobs: implemented, NOT activated

The code for these jobs exists and is tested. **No schedule exists for any of them.** Nothing runs them automatically: there is no pg_cron job, no scheduled edge function and no GitHub Actions schedule. Activating them needs the Supabase hold lifted (`docs/SUPABASE_PAUSE.md`) and the owner's go-ahead. Until then each is a manual step, and none of them runs anywhere today because the procedure is not on hosted.

| Job | Implemented (code, tested in CI) | What it does | Would be scheduled by | Status |
|---|---|---|---|---|
| Billing re-scrub | `admin_rescrub_billing_events(request_id)` (`20261102070000_data_requests.sql`; `supabase/tests/data_requests.sql` section 8) | De-identifies any payment event about a deleted household that arrived after the deletion and was not already stored de-identified. Idempotent; returns how many it changed. | A manual runbook step about 3 days after each household deletion (section 2, step 5). Could later be a daily scheduled edge function or pg_cron job over open deletions (`billing_rescrubbed_at is null`). | **NOT ACTIVATED.** No schedule; manual only once hosted. |
| Retention purge | `admin_purge_expired_retention()` (same migration and test, section 10) | Deletes retained invitation email records past `retain_until` and every `parent_email_deliveries` record sent more than 13 months ago. Returns the counts per table. | A manual monthly runbook step, or a monthly pg_cron job (`select public.admin_purge_expired_retention()`), or a scheduled edge function. | **NOT ACTIVATED.** No schedule. Until it runs, email-sent records are kept longer than 13 months. |
| Reminder claim expiry | `expire_practice_reminder_claims(p_now)` (#298, `20261102030000_practice_reminders.sql`; `supabase/tests/practice_reminders.sql`) | Marks reminder claims the sender never finished as `failed` (`claim_expired`) after `practice_reminder_claim_timeout()`. Not a privacy job, but it is the third background job these tables need. | The reminder sender edge function (`send-practice-reminders`) on its own schedule, or pg_cron. | **NOT ACTIVATED.** No schedule; the reminder sender is not scheduled either. |

Accepted consequence of the 13-month purge (owner, 2026-11-03): an inactivity alert's record is also the "already sent for this stretch" marker. A guardian whose student stays inactive for more than 13 months in a row can therefore get that alert once more after the purge.

To run them by hand (psql, as the owner):

```sql
select public.admin_rescrub_billing_events('<request id>');   -- ~3 days after a household deletion
select public.admin_purge_expired_retention();                -- monthly
select public.expire_practice_reminder_claims();              -- only if the reminder sender is running
```

## 8. Concurrency and webhook safeguards

**The window.** A household deletion de-identifies the household's payment events and records its Stripe customer and subscription ids in `data_request_billing_refs`. The webhook stores an event about those ids already de-identified. Without coordination, the two could interleave:
- **An event recorded while the deletion is in progress.** The deletion would not see the event, because it was not yet committed when the deletion collected events. The webhook would not see the references, because they were not yet committed either. The event would stay raw, with the payer's name and email, and the 3-day re-scrub only catches events that name the references after they exist.
- **An event recorded just before the deletion.** It was uncommitted while the deletion collected events.

**The fix.** One transaction-scoped advisory lock (`data_request_billing_lock_key()`):
- A live household deletion takes it exclusively before it collects events.
- `record_billing_event` takes it shared before it checks the references.
- An event that arrives during a deletion therefore waits for the deletion to commit, sees its references, and is stored de-identified. A deletion that starts while an event is being recorded waits for that event, then collects and de-identifies it.
- Webhook calls never block each other (shared mode). Deletions are rare and short.
- `scripts/test_data_request_concurrency.py` races both orders on two real connections in CI. Without the lock, the event recorded during the deletion stays raw and the test fails.

What remains after the lock is a webhook that read a live household just before the deletion committed. Its later steps then fail: the subscription upsert hits the deleted household's foreign key, the webhook returns 500, and Stripe retries. The retry finds the household gone and de-identifies the event. The 3-day re-scrub (section 2, step 5) catches anything else, including an event whose processing set the deleted household's id back.

**Webhook rules** (`supabase/functions/stripe-webhook`, `docs/product/STRIPE_BILLING.md`):
- The Stripe endpoint stays subscribed to **the handled events only**. `tests/test_stripe_webhook_events.py` checks that `scripts/stripe/setup_billing.mjs` asks for exactly `HANDLED_EVENTS`.
- Disputes, reviews and Radar warnings can name the cardholder without naming the customer or the subscription, so no deletion could find them. Any event of an unhandled type that arrives anyway is stored **already de-identified** (`p_store_raw => false`). Storing it this way, rather than dropping it, keeps exactly-once delivery and a record that Stripe sent something, with nothing personal in it.
- A failed household lookup returns 500 (Stripe retries). A database error is never taken to mean a missing household, so it cannot de-identify a live household's event.

**Deleting accounts that set a student's plans.** The audit triggers on weekly goals, planning preferences, the exam plan and academic interests used to put `set_by` back when the foreign key cleared it. So deleting an account that had set one of these for a student who still exists failed, through the admin API too. One example is the old guardian of a student who has since moved. This migration keeps that null. The test deletes such an account and then finds nothing of the deleted household anywhere.
