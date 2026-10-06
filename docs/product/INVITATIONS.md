# Student invitations

A guardian creates a student profile (no email needed), then invites the student to their own login by email or by link.

## Flow

1. The parent enters the student's email and selects **Send invitation**. The browser calls the
   `send-household-invitation` edge function with the parent's own session.
2. The function calls `create_student_invitation` as the parent. The database checks `manage_students`, creates a
   single-use code valid for 72 hours (only its SHA-256 digest is stored), records `recipient_email` on the
   invitation, and revokes that student's earlier outstanding invitations.
3. The function calls `prepare_invitation_email` as the parent. This confirms the invite is theirs and still
   usable, enforces at most 5 sends per invitation with 30 seconds between sends, and returns the names and expiry.
   It never returns the hash.
4. The function sends the email through Resend: the **Join Prep & Price** button links to
   `<site>/join?code=<code>`, with the code shown underneath as a fallback.
5. The student opens the link, creates an account or signs in (the code is carried through sign-in), and joins.
   `accept_household_invitation` links the guardian-created profile and sets `accepted_at` and `accepted_by`.

If sending fails, the invitation stays valid. The parent sees "We couldn't send the email" and can copy the link
or code, or retry. A retry resends the same code.

**Revoke:** the parent can revoke an outstanding invitation. Accepting a revoked one fails with "Invitation cancelled".

**Errors the student sees:**

| Message | Meaning |
|---|---|
| Invalid invitation | No invitation matches the code |
| Invitation expired | The 72 hours have passed |
| Invitation already used | The code was already accepted |
| Invitation cancelled | The parent revoked it or sent a newer one |

## Rules kept

- The recipient email lives only on the invitation row. It is never copied to the student or their profile.
- The email does not authenticate anyone. The student still needs their own account.
- The function runs with the caller's JWT, never a service-role key.
- The link base comes from an allowlist (`APP_ORIGINS`), never from the request alone.
- The code is never logged. Function logs record only the kind of failure.
- Resend keeps the message it delivers, so turn click and open tracking off for the sending domain. Tracking would
  rewrite the link.

## One-time owner setup

1. **Resend:** verify a sending domain for Prep & Price. The verified domains today are `inbox.familycues.com`,
   which belongs to FamilyCues, and `getcimiento.com`, which is not verified. Keep click and open tracking off.
2. **Resend:** create an API key with sending access for that domain only.
3. **Supabase → Edge Functions → Secrets** (project `butlklkzafvklwasbynr`):
   - `RESEND_API_KEY`: the key from step 2.
   - `INVITE_FROM_EMAIL`: for example `Prep & Price <invites@your-domain>`.
   - `APP_ORIGINS`: `https://college-optimizer-staging.netlify.app` for staging, plus the production origin later,
     comma-separated.

Until these secrets are set, sending returns `not_configured`. The parent sees "We couldn't send the email" and can
still copy the link.

## Deploying

- The migration `20261006120000_household_invitation_email.sql` is applied by the "Deploy Supabase migrations"
  workflow when it reaches `main`.
- The function is deployed with `supabase functions deploy send-household-invitation`, which keeps JWT
  verification on.
