# Native iPhone and Android apps: route, work and milestone

Status: **recommendation for owner decision, 2026-10-07.** Native apps are part of the intended product (owner, 2026-10-07; recorded in `ROADMAP.md`). Nothing native exists yet. Payment and store-policy flags live in `APP_DISTRIBUTION_AND_PAYMENTS.md` and still apply.

Tags: [Certain] = checked in the code or an official page today. [Likely] = strong but unverified. [Guessing] = estimate.

## What already transfers

**Product code (all TypeScript):**
- The React app (`web/`): every screen, the `DataSource` layer (Supabase client), the engines and the copy.
- The reminder rules: `supabase/functions/_shared/reminders.ts`, imported by the app and by the sender.

**Backend, the same for every client:**
- Supabase auth and row security.
- The household entitlement (CR-16).
- The reminder pipeline: settings, devices, deliveries, snooze tokens and guardian notices.

**Push sending already supports native apps** [Certain, in code; tested locally against fakes only]:
- `send-practice-reminders` sends web push to browsers and FCM HTTP v1 to app installs (`_shared/fcm.ts`).
- Every reminder is claimed in the database before sending, which gives one notification per reminder however many devices or overlapping runs there are.
- It goes to the device opened most recently. On a same-day tie the native app wins.
- Other devices are tried only if the push service rejects the first.

## Options compared

| | **A. Capacitor shell around the existing app** | **B. React Native (Expo), new UI** | **C. Swift (iOS) + Kotlin (Android)** |
|---|---|---|---|
| Reuses | All screens, data layer, engines, copy; one codebase with the web | Engines, data layer, reminder rules; **every screen rebuilt** | Backend only; everything client-side written twice |
| Time to first TestFlight / closed test, one developer [Guessing] | 4–7 weeks | 3–5 months | 6–9+ months |
| Ongoing cost | One UI for three platforms | Two UIs (web + RN) | Three UIs |
| Feel | Web UI in a native shell; good on recent phones, weaker on low-end Android [Likely] | Native components | Best possible |
| Push, deep links, IAP | Plugins (below) | Mature libraries | First-party APIs |
| App Review risk | Highest: 4.2 says an app should be "beyond a repackaged website" [Certain, quoted]; needs real app value (below) | Low | Lowest |

### Recommendation: A, Capacitor

**Why:**
- It reuses almost everything, including the parts most expensive to get right: honest copy, permissions handling and practice flows.
- It keeps one product instead of two.
- The backend pieces native needs already exist, or are in Research's queue.

**Weakest point:** Apple guideline 4.2.

**What makes the app more than a wrapped website:**
- native push with action buttons;
- a 5-minute session opened straight from a notification;
- deep links for invitations and email links;
- secure native sign-in storage;
- (later) a home-screen widget showing this week's progress.

If App Review still rejects the app, the fallback is to move the practice and home screens to native components inside the same Capacitor app, not a rewrite.

**Revisit B** if web-view performance on low-end Android fails real-device testing.

## Additional work, by area

### Push notifications

**Setup:**
- **Firebase project:** one for iOS and Android. Upload the APNs auth key (.p8) to it, so both platforms get FCM tokens and the server keeps one native channel.
  - The stock `@capacitor/push-notifications` returns the APNs token on iOS [Certain, Capacitor v8 docs]. Getting an FCM token on iOS needs a Firebase messaging plugin [Likely: `@capacitor-firebase/messaging`].
- **Action buttons:** register a `PRACTICE_REMINDER` category with "Start" and "Remind me later" (iOS), plus an Android channel `practice_reminders`. Category registration may need a few lines of native code if the plugin doesn't expose it [Likely].

**Behaviour:**
- **Tap:** opens `/student/practice?quick=1&r=<delivery>` inside the app, through the plugin's action event.
- **"Remind me later":** posts the signed token to `practice-reminder-action`, the same endpoint as the web service worker. A background action without opening the app depends on plugin support [Guessing]. If unsupported, the app opens briefly and shows "Okay, we'll remind you later".

**On each app open:**
- Read the permission. Android 13+ needs the runtime `POST_NOTIFICATIONS` permission [Likely].
- Report it with the token: `report_notification_device(channel 'fcm', token)`.
- As on the web, blocked notifications are shown as "blocked in device settings, as of the last open", never as detected immediately.

**Server:**
- Set the `FCM_SERVICE_ACCOUNT` secret. The FCM sender is built: the JWT bearer grant, a collapsing message, a 1-hour TTL, and `UNREGISTERED` retiring the device.
- Needs CR-27 as a real migration.

### Sign-in

- **Email and password:** sign-in uses Supabase email and password, as on the web.
- **Links that must open the app:**
  - Email confirmation, password reset and invitation links (`/join#t=…`) must open the app. That needs Universal Links (an `apple-app-site-association` file) and Android App Links (`assetlinks.json`), served by the website, plus a link handler in the app.
  - Until then, links open the website, which works but is a worse experience.
- **Session storage:** keep the Supabase session in Keychain/Keystore (a secure-storage plugin), not web-view storage, which the OS may clear [Likely].
- **Sign in with Apple:** required only if we add Google or other social sign-in (4.8) [Certain].
- **In-app account deletion:**
  - Apple 5.1.1(v) requires it when the app supports account creation [Certain, per our distribution record].
  - Google requires an in-app path plus a web link [Likely].
  - This depends on the deletion procedure that's still missing (launch checklist A4).

### Subscriptions

**iOS** (decision 2026-10-05):
- Apple In-App Purchase for the same household plan, alongside web checkout, with no external link.
- **Client:** StoreKit 2 through a Capacitor purchases plugin (for example RevenueCat [Likely]). `appAccountToken` is the household id.
- **Server:** App Store Server Notifications v2, received by a new edge function, write `household_subscriptions` with source `apple`. This is CR-16 plus an Apple source, for Research.
- **App behaviour:**
  - Restore purchases.
  - No purchase offer when the household is already entitled from any source.
  - Students never see prices.
  - Sandbox purchases never grant production access.

**Android:** decide G1–G3. The options are a consumption-only app (sign in to a web-bought plan) or Play Billing. The entitlement model already takes any source.

### Store submission

**Apple:**
- Developer Program enrollment as an organization (needs a D-U-N-S number) [Likely].
- App record and bundle id.
- Privacy nutrition labels from the privacy draft (#165).
- Age rating (follows the minimum-age decision; not the Kids category).
- Review notes with a demo household.
- Screenshots, then TestFlight.

**Google:**
- Play Console, as an **organization** account if possible. Personal accounts created after 2023-11-13 must run a closed test with 12 testers opted in for 14 consecutive days before production [Certain, Play Console Help].
- Data safety form.
- Content rating.
- Account-deletion URL.
- Target API level.
- Closed testing.

## Milestone N: native apps

| Step | Work | Owner | Depends on |
|---|---|---|---|
| N0 | Approve Capacitor; Apple and Google organization accounts; Firebase project; Android billing decision (G1–G3) | Owner | — |
| N1 | Capacitor project from `web/` builds; safe areas; secure session storage; Universal and App Links (site files and handler) | Design | N0 |
| N2 | Push: Firebase messaging plugin, categories and actions, device reporting on open, tap and snooze handling | Design | N0, N1, CR-27 migration |
| N3 | In-app account deletion; privacy labels and data safety from the approved policy; age rating | Design + Research + Owner | Deletion procedure (A4), legal text (A3) |
| N4 | iOS IAP: purchases plugin, Apple server notifications, entitlement source `apple`; Android per G1–G3 | Design + Research + Owner | CR-16 Apple source, counsel check |
| N5 | TestFlight and Play closed testing | Owner + Design | N1–N4 |
| N6 | **Real-device acceptance** (below) | Owner + Design | Hosted restored (A5), CR-22/CR-27 migrations, email domain (A7) |

## Acceptance: real devices, not fakes

Local tests use a fake push service, fake FCM and fake mail. They prove the code paths, **not delivery**, so they aren't launch acceptance.

Once hosted is available, each of these must pass on a real **iPhone** and a real **Android phone**, for each channel we ship (web push from the Home Screen web app, and the native app):
1. **Delivery:** a reminder arrives at the chosen time. None arrives in quiet hours, school hours, after today's planned practice, or past the limits.
2. **One notification across devices:** with the same student signed in on a phone and a laptop, only one device gets each reminder, and two overlapping sender runs still produce one.
3. **Tap:** tapping the notification opens a 5-minute practice session, and the delivery is marked opened.
4. **Remind me later:** works from the notification where buttons exist, and from the home-screen card where they don't. It pauses for an hour, sends one reminder at the end, and emails nobody.
5. **Turn off in the app:** a linked student sees the parent notice first. The guardian receives exactly one real email in their inbox, and the dashboard says "Emailed to you …" only after it was sent.
6. **Turn off in device settings:** the next app open shows "blocked in device settings (as of …)" for the family. Nothing claims to have known sooner.
7. **Reinstall or a new phone:** the old token is retired after the push service rejects it, and the new device receives the next reminder.

## Sources

- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/): 4.2, 4.8, 5.1.1(v).
- [Capacitor Push Notifications API (v8)](https://capacitorjs.com/docs/apis/push-notifications)
- [Google Play Console Help: app testing requirements for new personal developer accounts](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en)
