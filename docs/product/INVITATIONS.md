# Student invitations

A guardian creates a student profile (no email needed), then invites the student to their own login by email or by link.

## Flow

1. The parent enters the student's email and selects **Send invitation**. The browser calls the
   `send-household-invitation` edge function with the parent's own session.
2. The function calls `create_student_invitation` as the parent. The database checks `manage_students` and
   creates one single-use invitation valid for 72 hours. It carries two credentials, and only digests of each are
   stored:
   - **Link token:** 64 hex characters (244 random bits). It rides in the email button's URL fragment
     (`/join#t=…`), which browsers never send to a server, and is never shown to people.
   - **Invite code:** 10 characters, shown as `K7M4P-9Q2TX`. It uses a 29-character alphabet with no 0/O, 1/I/L
     or U/V, is case-insensitive, and is about 48 bits. Its digest is keyed with a server-only pepper. Wrong
     manual codes count against the account: 10 per 15 minutes and 30 per day, after which codes are refused
     ("Too many tries"). Link tokens aren't limited, because they can't be guessed.

   The database also records `recipient_email` on the invitation and cancels that student's earlier outstanding
   invitations.
3. The function calls `prepare_invitation_email` as the parent. This confirms the invite is theirs and still
   usable, enforces at most 5 sends per invitation with 30 seconds between sends, and returns the names and expiry.
   It never returns the hash.
4. The function sends the email through Resend. It contains the **Join Prep & Price** button (the link token)
   and `Invite code: K7M4P-9Q2TX` as a fallback.
5. The student opens the link, then creates and confirms an account or signs in. While signed out, the token is
   kept in that browser's storage for up to 72 hours, so it survives the confirmation email. If the confirmation
   link opens in a different browser, the student types the invite code.
6. The student joins. `redeem_household_invitation` returns one of joined, invalid, expired, used, revoked or
   rate_limited. On success it links the guardian-created profile and sets `accepted_at` and `accepted_by`.

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
| Too many tries | Too many wrong codes on this account; wait 15 minutes or use the email link |

## Rules kept

- The recipient email lives only on the invitation row. It is never copied to the student or their profile.
- The email does not authenticate anyone. The student still needs their own account.
- The function runs with the caller's JWT, never a service-role key.
- The link base comes from an allowlist (`APP_ORIGINS`), never from the request alone.
- Neither credential is logged. Function logs record only the kind of failure, and the token never appears in a
  URL that reaches a server.
- Resend keeps the message it delivers, so turn click and open tracking off for the sending domain. Tracking would
  rewrite the link.

## One-time owner setup

1. **Resend:** the temporary sending domain is `mail.getcimiento.com`, added with click and open tracking off. The
   sender is `Prep & Price <invites@mail.getcimiento.com>`, and the function uses it unless `INVITE_FROM_EMAIL` is
   set.
2. **Resend:** create an API key with sending access for that domain only.
3. **Supabase → Edge Functions → Secrets** (project `butlklkzafvklwasbynr`):
   - `RESEND_API_KEY`: the key from step 2.
   - `INVITE_FROM_EMAIL` (optional): overrides the default sender.
   - `APP_ORIGINS` (optional until production): comma-separated allowed site origins. It defaults to
     `https://college-optimizer-staging.netlify.app`.

Until these secrets are set, sending returns `not_configured`. The parent sees "We couldn't send the email" and can
still copy the link.

## Deploying

- The migration `20261006120000_household_invitation_email.sql` is live, and the live migration history records
  it under that version. Future schema changes go through the "Deploy Supabase migrations" workflow on `main`.
- The function `send-household-invitation` is deployed with JWT verification on. Redeploy it with
  `supabase functions deploy send-household-invitation`.
