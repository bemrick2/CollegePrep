# Stripe billing for Prep & Price (web)

Status: implemented behind a switch (`VITE_BILLING_ENABLED`). Not live until the owner steps below are done. No Stripe secret ever appears in the repository, the browser bundle, Netlify, or chat.

## Shape

- **Separate Stripe account.** Prep & Price gets its own Stripe account under the owner's existing Stripe login, with its own products, customers, payouts, branding and webhooks. Nothing is shared with the other business.
- **The household is the customer.** One Stripe Customer per household (`billing_customers`), created at the first checkout and tagged `metadata.household_id`.
- **One plan, two periods.** Product **Prep & Price Family Plan**, with prices identified by lookup key:
  - `pp_family_monthly`
  - `pp_family_annual`

  Code never stores price ids, so amounts can change in Stripe without a deploy. Existing subscribers keep their price until moved.
- **Buying happens on Stripe Checkout** (hosted; we never collect card details). **Managing happens in the Stripe Customer Portal**: payment method, invoices, switching monthly/annual, cancelling at period end.
- **Access comes from one record.** `public.subscriptions` (CR-16) is the system of record, and every client reads `household_entitlement(p_household)`. Stripe and, later, Apple IAP are both just sources that write it.

```
Website (guardian with manage_billing)
  └─ billing-checkout ──> Stripe Checkout ──(pays)──> Stripe
                                                       │ webhook (signed)
  billing-portal ──> Stripe Customer Portal            ▼
                                                 stripe-webhook ──> public.subscriptions ──> household_entitlement()
iOS app (later) ── Apple IAP ── App Store Server Notifications ──> (same table, provider 'apple')
```

## Pieces in this repository

| Piece | Path | What it does |
|---|---|---|
| Migration (CR-16) | `supabase/migrations/20261006090000_household_billing_stripe.sql` | Extends the existing `subscriptions` table additively: normalised statuses, period fields, `cancel_at_period_end`, `environment`. Adds the `billing_customers` and `billing_events` tables (server-only) and the `household_entitlement()` RPC. |
| SQL tests | `supabase/tests/billing.sql` | Members read access; only billing members see where it's managed; students can't buy; sandbox purchases never grant access; grace while retrying; Apple is equivalent; an event is stored once. |
| Edge functions | `supabase/functions/billing-plans`, `billing-checkout`, `billing-portal`, `stripe-webhook` | See below. |
| Shared logic | `supabase/functions/_shared/billing.ts` | Lookup-key → plan mapping, status normalisation, event → subscription id, row derivation. Unit-tested in `web/src/lib/billing/stripeLogic.test.ts`. |
| Owner setup script | `scripts/stripe/setup_billing.mjs` | Idempotently creates the product, both prices, the Customer Portal configuration and the webhook endpoint. |
| Deploy workflow | `.github/workflows/deploy-functions.yml` | Deploys the functions on merge to main. Skips until the token and project ref are configured. |
| Web UI | `web/src/features/parent/PlanCard.tsx` (Household page) | Plan status, the period picker → Checkout, and Manage billing → Portal. Hidden unless billing is enabled. Students never see it. |

### Edge functions

- **`billing-plans`** (GET) returns the active prices for the two lookup keys. These are public amounts.
- **`billing-checkout`** (POST `{household_id, lookup_key}`):
  - The caller must be signed in and be a guardian with `manage_billing`.
  - Refuses with 409 if the household already has access from **any** source, so there is never a double charge.
  - Reuses or creates the household's Stripe Customer, with an idempotency key.
  - Creates a subscription Checkout Session carrying `metadata.household_id` and `owner_user_id` on the subscription.
  - The success URL returns to `/parent/household?billing=success`, and the page waits for the webhook instead of assuming payment.
- **`billing-portal`** (POST `{household_id}`) opens a Portal session for the household's customer. Billing guardians only.
- **`stripe-webhook`** is deployed with JWT verification off; Stripe's signature authenticates it instead.
  1. Verifies the `Stripe-Signature` header with `STRIPE_WEBHOOK_SECRET`.
  2. Records the event once in `billing_events`, keyed on `(provider, event_id)`. A duplicate of an already-processed event is acknowledged and skipped.
  3. For handled events, retrieves the subscription **fresh from Stripe** and upserts the household's row from its *current* state. Duplicate, delayed and out-of-order deliveries therefore all converge on the same result.
  4. A subscription with no household metadata, no owner or no Prep & Price lookup key (for example, one made by hand in the dashboard) is recorded with an error and acknowledged, not retried forever.
  5. Transient failures return 500, so Stripe retries.

  Handled events:
  - `checkout.session.completed`
  - `customer.subscription.created`, `.updated`, `.deleted`, `.paused`, `.resumed`
  - `invoice.paid`, `invoice.payment_failed`, `invoice.payment_action_required`

### Status → access

| Stripe status | Our status | Access |
|---|---|---|
| `trialing`, `active` | same | Yes |
| `past_due` | same | Yes, as grace: Stripe is retrying; the UI asks for a new payment method |
| `incomplete`, `incomplete_expired`, `unpaid`, `paused`, `canceled` | same | No |

`cancel_at_period_end` keeps access until `current_period_end`; the UI says "Ends <date>". Test-mode subscriptions are stored with `environment = 'sandbox'` and never grant production access.

### Apple IAP compatibility

The iOS app (later) sets `appAccountToken` to the household id when purchasing. The App Store Server Notifications v2 handler writes the same `subscriptions` table with `provider = 'apple'` and `provider_subscription_id = originalTransactionId`, using the status vocabulary already allowed (`grace`, `billing_retry`, `expired`, `refunded`, `revoked`).

The rules shared with web purchases:
- `billing-checkout` refuses households with Apple access, and the iOS paywall must refuse households with web access, so neither side double-charges.
- Each subscription is managed where it was bought. The Plan card says "Billed through Apple…" for Apple purchases.

## Owner actions (one time, in this order)

1. **Create the Stripe account.**
   - In the Stripe Dashboard, open the account switcher (top left), choose **New account**, and name it **Prep & Price**. All remaining Stripe steps happen inside that account.
   - Fill in **Settings → Business → Public details**: name, support email, website, and optionally terms and privacy URLs. Checkout and the Portal display these.
2. **Approved prices (October 6, 2026).** Family Plan: USD $19.99/month (1999 cents, `pp_family_monthly`) or $149/year paid upfront (14900 cents, `pp_family_annual`). One household subscription covers all children. No traditional free trial. Core college planning remains free; the subscription unlocks adaptive ACT/SAT prep, benchmarks, AI explanations, practice plans and student/parent progress. Stripe Tax remains off until separately configured.
3. **Test mode first.** With the Dashboard in **Test mode**, run the setup script in your own terminal. Use a test secret key in your shell only:

   ```
   export STRIPE_SECRET_KEY=sk_test_...      # Prep & Price account, test mode
   node scripts/stripe/setup_billing.mjs --monthly-cents 1999 --annual-cents 14900 --currency usd \
     --site-url https://college-optimizer-staging.netlify.app \
     --webhook-url https://butlklkzafvklwasbynr.supabase.co/functions/v1/stripe-webhook
   unset STRIPE_SECRET_KEY
   ```

   It prints the webhook signing secret once and the portal configuration id. Put both straight into Supabase (step 5). Alternatively, create the same things by hand in the Dashboard: the product, both prices with those lookup keys, the Customer Portal settings, and a webhook endpoint subscribed to the events listed above.
4. **Create a restricted API key for the server.** Go to **Developers → API keys → Create restricted key**, name it `prep-price-edge-functions`, and give it:
   - Write: Customers, Checkout Sessions, Customer portal
   - Read: Subscriptions, Prices, Products
   - Nothing else
5. **Add the Supabase secrets.** In the Supabase project `butlklkzafvklwasbynr`, go to **Edge Functions → Secrets** and add:

   | Name | Value |
   |---|---|
   | `STRIPE_SECRET_KEY` | the restricted key from step 4 (`rk_test_…`, later `rk_live_…`) |
   | `STRIPE_WEBHOOK_SECRET` | the endpoint's signing secret (`whsec_…`) |
   | `SITE_URL` | `https://college-optimizer-staging.netlify.app` (later the production domain) |
   | `STRIPE_PORTAL_CONFIGURATION_ID` | optional; printed by the script (`bpc_…`) |
   | `STRIPE_AUTOMATIC_TAX` | optional; `true` only if Stripe Tax is set up |
   | `STRIPE_ALLOW_PROMOTION_CODES` | optional; `true` to allow coupon codes at Checkout |

   `SUPABASE_URL`, `SUPABASE_ANON_KEY` and `SUPABASE_SERVICE_ROLE_KEY` are provided to edge functions automatically; don't add them.
6. **Deploy the functions** (pick one):
   - **Automatic:** in GitHub, add the secret `SUPABASE_ACCESS_TOKEN` (a Supabase personal access token) to the `supabase-live` environment, and the repository variable `SUPABASE_PROJECT_REF = butlklkzafvklwasbynr`. The workflow deploys on the next push to `supabase/functions/**`, or run it manually from the Actions tab.
   - **Manual:** with the Supabase CLI logged in on your machine, run `supabase functions deploy billing-plans billing-checkout billing-portal --project-ref butlklkzafvklwasbynr`, then the same for `stripe-webhook` with `--no-verify-jwt`.
7. **Configure Netlify** (site `college-optimizer-staging`, **Site configuration → Environment variables**). None of these are Stripe secrets:
   - `VITE_SUPABASE_URL = https://butlklkzafvklwasbynr.supabase.co`
   - `VITE_SUPABASE_PUBLISHABLE_KEY` = the project's publishable (anon) key
   - `VITE_BILLING_ENVIRONMENT = sandbox` on the named staging site only; omit for production.
   - `VITE_BILLING_ENABLED = true`, only after steps 1–6 work in test mode
8. **Test in test mode.** Check out with the card `4242 4242 4242 4242`, then confirm the Household page shows "Active". Open Manage billing and cancel; it should show "Ends <date>". Optionally run `stripe trigger invoice.payment_failed` against a test subscription and confirm "Payment retrying".
9. **Go live.** Switch the Dashboard to live mode and repeat steps 3–5 with live keys. Live has its own webhook endpoint and signing secret. Then update `SITE_URL` for the production domain.

## What the frontend does not do

- No prices, plans or checkout in the demo, or until `VITE_BILLING_ENABLED=true`.
- No card fields; Stripe hosts them.
- No entitlement is inferred on the client. Production access uses `household_entitlement`; the staging billing card uses membership-checked `household_sandbox_billing_status` for display only.
- Students never see purchase UI.

## Scholarship Negotiator — deferred

$99 one-time per school appeal/reconsideration package; separate from the Family Plan. Do not create a Stripe product or checkout until a server-enforced eligibility gate has verified a documented institutional process applicable to the student. Otherwise show: “We have not verified a formal aid reconsideration process for this school.” Never promise an award increase.

## Sandbox setup check — October 6, 2026

Sandbox account: `acct_1UNUxXBVFG4WtYp0`. Product: `prod_VOI20vz3FjE17k`. Existing `setup_billing.mjs` completed with 1999/14900 USD pricing. Portal: `bpc_1UNVZXBVFG4WtYp0cOJoHPFv`; webhook: `we_1UNVZXBVFG4WtYp0bmPwOn7L`, configured with the exact endpoint and nine documented events.

Restricted key `prep-price-edge-functions` created with the six documented permissions and saved privately as `STRIPE_SECRET_KEY`. Webhook signing secret, SITE_URL and Portal configuration ID are saved in Supabase. No credentials are committed here.

The existing billing migration and two sandbox isolation fixes are applied. All four billing Edge Functions are deployed through the supported Supabase deployment API; only the Stripe webhook has JWT verification disabled. Backend plans return the approved amounts, unsigned webhook requests return 400, TypeScript validation and billing tests pass.

Sandbox customers are separated by environment, derived only from the server key. The staging billing card selects its display-only sandbox status RPC only with `VITE_BILLING_ENVIRONMENT=sandbox` on `college-optimizer-staging.netlify.app`. Both production entitlement RPCs and authenticated direct subscription reads exclude sandbox rows. The sandbox status RPC is not a production authorization source.

Netlify staging public environment variables are configured. A build with billing disabled is deployed (`6ac4d094127348ef99b160f7`). Billing remains disabled until authenticated Checkout/Portal checks work. The project currently has no billing-enabled guardian household, and the browser is at staging sign-in. Owner sign-in/account creation is required to proceed with the documented Checkout → webhook → Active → Portal → cancellation → Ends test. End-to-end verification is pending; it has not been claimed as passed.

Implementation and fixes remain on PR #101 / `claude/stripe-billing`; main has not been merged. No live Stripe billing was changed.
