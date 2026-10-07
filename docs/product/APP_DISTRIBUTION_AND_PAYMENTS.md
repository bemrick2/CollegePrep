# App distribution and payments: intended flows and policy flags

Status: **design and decision record, not legal advice.** Nothing here implements native payments. Store rules change often. Before building or submitting any native purchase behaviour, verify each flag against the current App Store Review Guidelines, Google Play Payments policy and program terms, and with counsel.

Tags: **[Certain]** = quoted from the store's own current text (checked 2026-10-05). **[Likely]** = from secondary sources or older knowledge; verify. **[Decision]** = a business choice we have to make.

## Decision (2026-10-05)

**Update, 2026-10-07:** native iPhone and Android apps are part of the intended product. The route (Capacitor, recommended), the extra work and milestone M2 are in `NATIVE_APPS.md` and `ROADMAP.md`. The payment decisions below are unchanged.

- **Web stays primary.** Marketing, onboarding and selling happen on the website.
- **iOS offers the same household subscription through Apple In-App Purchase**, alongside the web purchase. This follows 3.1.3(b), so we don't rely on the 3.1.3(f) companion-app exception (flags A1/A2).
- **No external checkout link inside iOS for now**, in any storefront, the US included.
- **Our backend is the system of record for access.** A household's entitlement works the same whether payment came from the web, Apple or (later) Google. Apple and Google are payment sources that feed it, never the authority on access.
- **Android keeps the same entitlement architecture.** No Google Play Billing purely for symmetry; add it only if Play policy requires it for the distribution approach we actually choose (flags G1–G3).
- **Nothing is submitted to Apple yet.**

## Principles

1. The **website** is where families learn about Prep & Price, create the household, choose a plan and pay (where permitted).
2. The **iOS and Android apps** are for signing in and using the service. By default they contain no purchase flow, no prices and no calls to action to buy.
3. **Ownership is not installation.** A subscription belongs to the household (the parent is usually the payer) and is recorded by our backend with its payment source. Installing an app never creates a second purchase. A student signs in to their own account and inherits the household's entitlement.
4. We do not add Apple In-App Purchase or Google Play Billing just because apps exist. We do not add in-app links to web checkout until the rules below are verified for each storefront.

## Intended flows

| Step | Web | iOS app | Android app |
|---|---|---|---|
| Learn and compare | Landing page, sample family | — | — |
| Create household and accounts | Yes (primary CTA "Create your family plan") | Sign in only (see flag A5) | Sign in only (see flag G4) |
| Choose plan and pay | Web checkout (processor TBD; no billing exists yet) | Apple IAP for the same household plan; no external link | None unless Play policy requires it for our approach (G1–G3) |
| Use the service | Yes | Yes, with the same account | Yes, with the same account |
| Entitlement check | Backend | Backend (read-only) | Backend (read-only) |
| Manage or cancel the subscription | Web account page (to build) | No in-app management by default | No in-app management by default |

### Entitlement model (backend, CR-16)

One household entitlement, fed by any payment source. Access is computed only from it.

**`household_subscriptions`**: one row per paid subscription, whatever its source.

| Field | Type | Notes |
|---|---|---|
| `id` | uuid | |
| `household_id` | uuid | The subscription belongs to the household |
| `owner_user_id` | uuid | The payer, usually a guardian; manages or cancels it |
| `plan_key` | text | Same plan keys across web, Apple and Google |
| `source` | `web \| apple \| google \| comp` | |
| `source_customer_id` | text null | e.g. the web processor's customer id |
| `source_subscription_id` | text | Web subscription id, Apple `originalTransactionId`, Google `purchaseToken` |
| `status` | `trialing \| active \| grace \| billing_retry \| expired \| canceled \| refunded \| revoked` | Normalised across sources |
| `auto_renew` | boolean | |
| `current_period_start` / `current_period_end` | timestamptz | |
| `environment` | `production \| sandbox` | Apple and Google sandbox purchases never grant production access |
| `last_event_at` | timestamptz | |

**`household_subscription_events`** is the append-only log of every source event, raw payload included. It is used for audit, replays and disputes.

**`household_entitlement(p_household)`** is the read RPC: `{ active: boolean, plan_key, status, period_end, source, owner_user_id, manage_url_hint }`. It is computed from the subscriptions as the best active row (precedence: `active` > `grace`/`billing_retry` > others). Every household member can read it: guardians with `view_progress` and linked students. Only `owner_user_id` and guardians with `can_manage_billing` see source details.

**Events that write it** (server-side only, never from the client):

- **Web processor:** subscription created, renewed, payment failed, updated (plan change), canceled, refunded. The processor is TBD (CR-16 open).
- **Apple:** App Store Server Notifications v2 (`SUBSCRIBED`, `DID_RENEW`, `DID_CHANGE_RENEWAL_STATUS`, `DID_FAIL_TO_RENEW` with grace period, `EXPIRED`, `REFUND`, `REVOKE`, `GRACE_PERIOD_EXPIRED`), plus on-demand verification of the signed transaction the app sends after purchase. The app's `appAccountToken` is set to the household's id, so a purchase links to the right household.
- **Google** (only if adopted): Real-time Developer Notifications plus the Play Developer API purchase check.

**Rules the frontend relies on:**

1. **No double charge.** A household with an active entitlement from any source is never offered a purchase in any app. The iOS paywall appears only when `active` is false.
2. **Managing a subscription.** Changing or cancelling happens where it was bought: web on the web account page; Apple through Apple's subscription settings. `manage_url_hint` tells the UI which to show.
3. **Overlapping subscriptions.** If two active subscriptions exist (for example web and Apple), access stays on and the UI tells the owner where each one is managed. The backend never cancels a store subscription on its own.
4. **Students** never see purchase UI or prices. A linked student's access comes from household membership.

Until CR-16 lands, the frontend shows no plan, price or paywall anywhere and invents no entitlement state.

## Apple flags

- **A1. Unlocking web-bought subscriptions in the iOS app.** [Certain]
  - Guideline 3.1.3(b), Multiplatform Services, allows apps to let users "access content, subscriptions, or features they have acquired … on other platforms or your web site … provided those items are also available as in-app purchases within the app."
  - Read literally, a login-only iOS app that unlocks a web subscription must also offer the subscription as IAP.
  - **[Decision]** Choose one of:
    - (a) Also offer IAP in iOS. Apple's commission applies only to purchases made through IAP; web purchases are unaffected.
    - (b) Rely on 3.1.3(f) (below).
    - (c) Rely on the US-storefront link-out rule (A3) where it applies.
- **A2. 3.1.3(f) Free stand-alone apps.** [Certain text; fit is Likely risky]
  - "Free apps acting as a stand-alone companion to a paid web based tool (i.e. VoIP, Cloud Storage, Email Services, Web Hosting) do not need to use in-app purchase, provided there is no purchasing inside the app, or calls to action for purchase outside of the app."
  - Education/test-prep is not among the examples, so App Review may not accept this.
  - If we rely on it, the app must contain no purchasing and no "subscribe on our website" prompts.
- **A3. United States storefront: buttons and links to web purchase.** [Certain text]
  - 3.1.1(a) says entitlements "are not required for developers to include buttons, external links, or other calls to action in their United States storefront apps."
  - Commission on linked-out purchases: [Likely] currently 0% after the April 2025 Epic v. Apple order.
  - On 2025-12-11 the Ninth Circuit allowed Apple to seek a commission limited to costs "genuinely and reasonably necessary" for link-outs, with the rate to be set by the district court. That could change the economics; re-check before relying on it.
- **A4. All other storefronts.** [Certain]
  - Apps "may not include buttons, external links, or other calls to action that direct customers to purchasing mechanisms other than in-app purchase," except through the regional link entitlements.
  - [Likely] Those entitlements carry fees, reporting and disclosure requirements: EU about 12–20% in total, Japan 15–21%, South Korea 26%.
  - Default: no price, plan or "buy on web" language in non-US builds.
- **A5. Account creation and deletion.** [Certain]
  - 5.1.1(v): "If your app supports account creation, you must also offer account deletion within the app."
  - If the app allows sign-up (for example a student creating an account from an invite code), it needs in-app deletion.
- **A6. Social sign-in.** [Certain]
  - 4.8: if we add Google (or another third-party) sign-in, we must also offer a privacy-focused equivalent, such as Sign in with Apple.
- **A7. Children.** [Likely]
  - Students may be 11–17.
  - Listing in the Kids category brings extra rules (no third-party analytics or ads, parental gates for links and purchases).
  - COPPA applies to under-13 users regardless of store.
  - **[Decision]** Category and age rating.

## Google Play flags

- **G1. Payments policy outside the US.** [Likely] In-app purchases of digital goods use Play Billing, unless we're enrolled in an alternative or user-choice billing program where offered (with service fees).
- **G2. Consumption-only apps.** [Likely; verify current Payments policy text] Apps that only let users access content bought elsewhere, with no in-app purchase and no steering, have historically not required Play Billing.
- **G3. United States.** [Likely, from Google's Play Console Help]
  - Since 2025-10-29, Google does not prohibit communicating about or linking to purchases outside Play, or offering other in-app payment methods.
  - Developers in the alternative billing or external content links programs report transactions and pay service fees starting 2026-10-01; the external-links download reporting deadline is 2026-12-01.
  - Secondary sources report fee levels (for example around 10% on auto-renewing subscriptions) and ongoing court review; verify before relying on any figure.
- **G4. Account creation and deletion.** [Likely] Play's data-safety and account-deletion requirements apply if the app supports account creation (deletion must be available in-app and through a web link).
- **G5. Families policy.** [Likely] If the target audience includes children under 13, the Designed for Families requirements apply.

## Website store badges (implemented)

- **Badge files:**
  - `web/src/components/StoreBadges.tsx` renders only the official badge files, `web/public/badges/app-store-badge.svg` and `web/public/badges/google-play-badge.png`.
  - Download them from Apple's marketing resources and Google Play's badge page. Don't redraw, recolour or crop them.
  - Follow each brand's clear-space and minimum-size rules: the component keeps clear space of a quarter of the badge height around a 40px-tall badge.
  - Check the Google PNG's built-in padding once the asset is added.
- **Listing URLs:** set at build time with `VITE_APP_STORE_URL` and `VITE_PLAY_STORE_URL`. Only official hosts are accepted (`apps.apple.com`, `play.google.com/store/apps/details?id=…`).
- **Until listings exist:** no badge and no link. The site says "Apps for iPhone and Android are coming soon."
- **Order:** Android visitors see Google Play first; everyone else sees the App Store first. Both are always offered.
- **Placements:** hero (under the primary CTA), the "Practice on the go" section, the site footer, and the parent post-signup screen.
- **Primary CTA:** the website's primary conversion is "Create your family plan", not "Download the app".

## Go-live checklist (apps)

1. ~~Decide A1~~ Decided 2026-10-05: Apple IAP alongside web; no iOS external link. Confirm the plan's IAP product setup with counsel before submission.
2. Build CR-16 entitlements and a web account page for plan management and cancellation.
3. Add the official badge files; set both URLs; verify badges render at 40px with clear space, in light and dark.
4. Review store metadata and in-app copy per storefront for purchase language (A3/A4, G1/G3).
5. Account deletion in-app if sign-up is in-app (A5/G4); Sign in with Apple if social login (A6).
6. Age rating, Kids/Families decisions, privacy labels and data-safety forms (A7/G5).

## Sources

- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) (3.1.1, 3.1.1(a), 3.1.3(b), 3.1.3(f), 4.8, 5.1.1(v); read 2026-10-05)
- [Google Play Console Help: policies for developers serving users in the US](https://support.google.com/googleplay/android-developer/answer/15582165?hl=en)
- [Neon: Apple alternative payment fees 2026](https://www.neonpay.com/blog/apple-app-store-alternative-payment-fees-what-developers-pay-in-2026) (secondary)
- [Coda: Epic v. Google policy update 2026](https://www.coda.co/blog/epic-v-google-policy-update-2026/) (secondary)
- [iClarified: Apple allows external purchase links in US](https://www.iclarified.com/97192/apple-updates-app-store-rules-to-allow-external-purchase-links-in-us) (secondary)
