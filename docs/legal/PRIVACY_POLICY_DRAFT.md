# Prep & Price Privacy Policy — DRAFT FOR REVIEW

> **Not legal advice, and not ready to publish.** This draft was written by an AI from what the code actually collects, as of 2026-10-07. A qualified lawyer must review it before it goes live, especially on children's and students' privacy (COPPA and state student and minor privacy laws).
>
> Items marked **[[OWNER: …]]** are decisions for the owner; see `docs/legal/DECISIONS.md`. Anything the app does not yet do is marked **[[NOT BUILT]]**. Those promises must either be built before launch or removed from this text.

_Last updated: [[DATE]]_

Prep & Price ("we", "us") helps families prepare for the ACT and SAT and compare what colleges may cost. This policy explains what we collect, why, who can see it, and the choices you have.

## Who uses Prep & Price

- **Parents and guardians** create a household, add students, set weekly goals and see progress.
- **Students** practise. A student can either:
  - use the app on a guardian's sign-in without an account of their own ("guardian-managed"), or
  - accept an invitation and sign in themselves ("student login").
- **Minimum age.** Students must be at least **[[OWNER: minimum age, recommended 13]]** to have their own login. We do not knowingly collect personal information from children under 13 **[[OWNER: or describe the parental-consent process if under-13s are allowed]]**.

## What we collect

| Information | From whom | Why |
|---|---|---|
| Email address and password (the password is stored hashed by our authentication provider) | Each person with a login | To sign you in and send account emails |
| Display name | Parents; students with a login | Shown inside your household |
| Household name and time zone | Parent | To group a family and count "this week" correctly |
| Student first name or nickname, graduation year, grade | Parent | To set up practice and plans. We do not ask for a date of birth. |
| Exam plan, target score, weekly goal, daily minutes | Parent or student | To build the weekly plan |
| Practice activity: which questions were shown, answers chosen, whether correct, time spent, hints used, progress-check results | Student, while practising | To give feedback, choose the next questions and show progress |
| Test scores a family enters, and whether they are official or self-reported | Parent or student | To compare with colleges' published ranges |
| Academic interests | Parent or student | To filter programs |
| Saved colleges | Parent or student | To compare costs |
| Notification settings (weekly summary, inactivity alerts) | Parent | To decide which emails to send |
| Invitation records: who invited whom, when, and the recipient's email address | Parent | To deliver and expire invitations. The invitation code itself is stored only as a one-way hash. |
| Billing: a customer reference from our payment processor, subscription status and period | Parent who subscribes | To provide the paid plan. **We never see or store card numbers**; the payment processor handles them. |
| Records of which emails we sent and when | System | So the same email isn't sent twice, and so the app can show "emailed" truthfully |
| Technical logs (IP address, browser, request times) | Everyone, through our hosting and database providers | Security, abuse prevention, debugging |

**Kept only in your browser, not sent to us** (on the current version): grants, loans and other cost figures you type into the savings calculator; some saved-college and interest selections. **[[Verify before publishing; this may change as features move to the database.]]**

**What we don't do:**
- We do not use advertising trackers or third-party analytics.
- We do not sell personal information.
- We do not share it for cross-context behavioural advertising.
- We do not use students' data to train AI models. **[[OWNER: confirm]]**

## AI help

The app has an optional AI hint feature. It is **off**, and no AI provider receives student data today.

If it is turned on, the student's question, their answer and the hint request would be sent to **[[OWNER: provider]]** to generate a hint. **[[Update this section before enabling.]]**

## Who can see a student's information

- **The student**, when they have their own login.
- **Guardians in the same household**, according to the permissions the household gives them (view progress, set goals, manage students, manage billing). A guardian without "view progress" permission does not see practice results.
- **Our service providers**, only to run the service (below).
- **Nobody else.** We do not give student data to colleges, testing companies or marketers.

Email summaries to guardians include the student's name, how many practice questions they did, and whether they met the weekly goal. They are sent only if a guardian turns them on.

## Service providers (processors)

| Provider | What for |
|---|---|
| Supabase | Database, sign-in, server functions |
| Netlify | Website hosting |
| Resend | Sending email |
| Stripe | Payments |
| **[[OWNER: AI provider, if AI help is enabled]]** | AI hints |

Data is stored in **[[OWNER: region, e.g. United States]]**.

## How long we keep it

**[[OWNER: decide retention.]]** Suggested starting point:
- **Practice history:** while the account is active, and deleted **[[30]]** days after the household or student is deleted.
- **Email-sent records:** **[[13 months]]**.
- **Technical logs:** per provider defaults, **[[typically 7–90 days]]**.
- **Billing records:** as long as tax law requires.

## Your choices and rights

- **Change information.** You can change goals, notification settings and student details in the app.
- **Delete data, or get a copy.** Email **[[OWNER: privacy contact]]** to delete a student, a household or your account, or to receive a copy of your data. **[[NOT BUILT: there is no in-app deletion or export yet. Either build it or keep this as a manual email process with a stated response time.]]**
- **Parents of students under 18** can review or delete their child's information and stop further collection.
- **US state residents** may have additional rights (access, correction, deletion, opt-out). We honour these requests for everyone, regardless of state. **[[Counsel to confirm which state laws apply.]]**

## Security

- **Access** to data is enforced in the database: each person can read only their own household's data.
- **Invitation codes** are stored only as hashes.
- **Payments** are handled by Stripe.

No system is perfectly secure. We will notify affected users of a breach as the law requires.

## Changes

If we make a material change, we will tell account holders by email or in the app before it takes effect.

## Contact

**[[OWNER: legal entity name, postal address, privacy email]]**
