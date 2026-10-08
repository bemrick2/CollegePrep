# Roadmap

Owner decisions and the order of work. Details live in the linked documents.

## Product scope (owner, 2026-10-07)

- **Web app:** families sign up, pay and practise on the website. This ships first.
- **Native iPhone and Android apps are part of the intended product.**
  - They reuse the web app and the shared backend; Capacitor is recommended in `NATIVE_APPS.md`.
  - Practice reminders follow the same rules on every platform, and a student gets one notification per reminder across all their devices.

## Milestones

| | Milestone | What "done" means | Plan / blockers |
|---|---|---|---|
| M1 | **Web launch** | Launch checklist sections A, B and D closed; real-device acceptance passed for web push | `LAUNCH_CHECKLIST.md` |
| M2 | **Native apps** (N0–N6) | Apps in the App Store and Google Play; real-device acceptance passed for native push, sign-in links, account deletion and iOS subscriptions | `NATIVE_APPS.md` |
| M3 | College cost completeness | CR-10, CR-11, CR-15, CR-17 to CR-20 served; savings beyond "potential" only where the data supports it | `docs/frontend/CONTRACT_REQUESTS.md` |
| M4 | Personalized college planning (Tennessee business pilot) | Slice 1 (UTC Management, B.S.B.A.) shown from verified records only, behind `VITE_PLANNING_PILOT`; then UTK, MTSU, dual enrollment | `COLLEGE_PLANNING_PILOT.md`, #198 |

M2 can start in parallel with M1 (N0, N1). Its push, deletion and subscription steps need hosted restored and Research's CR-16, CR-22 and CR-27 migrations, the same as M1.

M4 is isolated from M1: separate code and flag. Its engine and demo work need no database; account storage (CR-28) waits for hosted.
