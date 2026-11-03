# Data export and deletion requests (runbook)

Launch checklist A4; #218 B8. Owner decisions: `docs/legal/DECISIONS.md` #6 (manual by email at launch, in-app soon) and #5 (retention). This runbook is not legal advice. Items marked **[[OWNER/COUNSEL]]** need confirmation before launch.

The database side is in `supabase/migrations/20261102070000_data_requests.sql` and is tested by `supabase/tests/data_requests.sql`. The test runs in the CI `database` job.

## At a glance

| Step | What | Where |
|---|---|---|
| 1 | Receive the request at the privacy address and acknowledge it | Privacy mailbox |
| 2 | Verify the requester against the account email on file | Supabase dashboard, SQL editor (read only) |
| 3 | Export (always offered before a deletion) | `admin_export_student` / `admin_export_household` |
| 4 | For a household with a live subscription, cancel it with the payment provider | Stripe dashboard |
| 5 | Dry run the deletion, then run it live | `admin_delete_student` / `admin_delete_household` |
| 6 | Delete the listed auth accounts through the admin API | Supabase dashboard or Auth admin API |
| 7 | Record the auth deletion; reply to the requester | `admin_record_auth_deletion`; privacy mailbox |

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

Run them in the Supabase SQL editor of the production project, or with `psql` on the project's service connection. Every `admin_*` function is service-role only. Clients (anon and signed-in users) cannot call them or read the request tables.

Each call is one transaction: it completes fully or changes nothing.

Never run against staging data by mistake: check the project ref in the dashboard first.

### Export

```sql
-- Household (to the account holder):
select public.admin_export_household(
  p_household    => '<household id>',
  p_requested_by => 'parent@example.com',            -- the verified account email
  p_requested_at => '2026-11-02 14:05+00');          -- when the request arrived

-- One student (to a guardian of that household, or to the student):
select public.admin_export_student(
  p_student      => '<student id>',
  p_household    => '<household id>',                -- null only for an independent student
  p_requested_by => 'parent@example.com',
  p_requested_at => '2026-11-02 14:05+00');
```

What the export contains:

- The result is one JSON document (`format: collegeprep-data-export/v1`). Under `tables` it holds every row about the student or household.
- A household export holds the household and its members' profiles, invitations, saved schools, subscription status and periods, and every student's practice history, goals, plans, scores and alert settings.
- A student export leaves out guardians' alert settings and other accounts' ids.
- No export includes:
  - invitation code digests;
  - question text or answer keys (attempts list question ids and the answers given);
  - payment-provider ids or raw payment events. Invoices are in the Stripe customer portal.

How to deliver it:

1. Save the result as `export-<request id>.json`.
2. Send it only to the verified account email, as an encrypted attachment or a link that expires. **[[OWNER: choose the delivery method.]]**
3. Delete your local copy once it is delivered.

Each export writes a `data_request_log` row with the row counts per table.

### Delete

Always offer the export first.

For a household, first check for a live subscription. A trialing, active, past-due, unpaid, paused or incomplete subscription makes the deletion refuse. Cancel it in the Stripe dashboard (refunds per the terms). Wait until the webhook shows `status = 'canceled'` in `public.subscriptions`. App Store subscriptions (later) are cancelled by the user through Apple.

1. **Dry run.** This is the default. It changes nothing and writes no log row. Read the counts, `kept` and `auth_users_to_delete`.

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

2. **Live run.** The same call with `p_dry_run => false` and `p_confirm =>` the same id. Without both, the call refuses.

   ```sql
   select public.admin_delete_household(
     p_household    => '<household id>',
     p_reason       => 'Account holder asked by email to delete the household',
     p_requested_by => 'parent@example.com',
     p_requested_at => '2026-11-02 14:05+00',
     p_dry_run      => false,
     p_confirm      => '<household id>');
   ```

   Keep the returned `request_id` and `auth_users_to_delete`.

3. **Delete the auth accounts** listed in `auth_users_to_delete`. Use the Supabase Auth admin API, not SQL: the admin API also removes the account's identities, sessions and refresh tokens. Do either of the following:
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

## 3. What is removed and what is kept

| Data | On deletion | Why |
|---|---|---|
| Student profile, practice sessions, items, attempts, attempt events, AI-help requests, progress checks and their items, weekly goals, test scores, exam plan, planning preferences, academic interests, guardians' alert settings for the student | **Deleted at once** (within the 30 days of decision #5) | Practice history rule |
| Household, memberships, invitations, saved schools, subscription state, payment-customer map | **Deleted** | Personal data |
| Account profiles and invitation-code rate-limit rows of the accounts listed for deletion | **Deleted**; the auth account itself through the admin API | Personal data |
| Payment events (`billing_events`) | **Kept, de-identified.** The household link is cleared. Names, emails, phones, addresses, metadata and descriptions are stripped from the payload. Ids, amounts, tax, currency, status and dates stay. | Billing records are kept as tax law requires (decision #5) **[[COUNSEL: confirm the period, often 7 years]]** |
| Payment-provider customer reference | **Kept** in the request's `data_request_log.kept.billing_customer_refs` | Lets the invoices that Stripe holds be found for tax purposes |
| Invitation emails sent in the last 13 months | **Kept** in `retained_email_records`: recipient address, send count, last sent time. No link to any account. Removed by `admin_purge_expired_retention()` after 13 months | Email-sent records are kept 13 months (decision #5) |
| `data_request_log` | **Kept**: ids, counts, requester email, reason, dates | Record that the request was handled **[[COUNSEL: retention period for request records, e.g. 24 months under CCPA regulations]]** |

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
  - `requested_at` (received), `performed_at` and `performed_by`;
  - `exported`, `removed` and `kept` (counts and references);
  - `auth_users_to_delete` and `auth_users_deleted_at`.
- Reply to the requester with what was exported or deleted, and what was kept and why (the table above). Use the request id as the reference.
- A request is complete when its log row exists, `auth_users_deleted_at` is set (for deletions with accounts listed), and the reply is sent.

Open deletions with accounts still to delete:

```sql
select id, subject_kind, subject_id, requested_at, performed_at, auth_users_to_delete
from public.data_request_log
where action = 'delete' and cardinality(auth_users_to_delete) > 0 and auth_users_deleted_at is null;
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
2. It calls `admin_delete_*` or `admin_export_*` with `p_channel => 'in_app'`, `p_requested_by` set to the account email, and `p_confirm` set to the id.

The definer runs as the owner, so no client grant on the `admin_*` functions is needed. The auth-account step then runs in an Edge Function with the service role, using `auth.admin.deleteUser`. Design owns the UI: a confirmation screen, an export download, and the 'what we keep' text from section 3.
