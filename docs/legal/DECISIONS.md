# Legal and privacy decisions for the owner (#161)

These are the decisions the privacy policy and terms drafts depend on. They are not legal advice; have counsel confirm before launch.

Tags: [Certain] = checked in code or the law's text; [Likely]; [Guessing].

## Decisions

| # | Decision | Options | Recommendation and why |
|---|---|---|---|
| 1 | **Minimum student age** | (a) 13 and up only. (b) Under-13s allowed, with verifiable parental consent under COPPA. | **(a) 13+ at launch.** COPPA covers personal information collected online from children under 13 [Certain]. Practice answers and timing are collected from the child as they use the app, so a guardian-managed profile does not avoid COPPA for an under-13 user [Likely]. Allowing under-13s means verifiable parental consent, a COPPA-specific notice, and stricter retention [Certain that these are COPPA requirements]. The FTC amended the COPPA Rule in 2025 [Likely]; counsel should confirm current obligations. High-school test prep rarely needs under-13s [Likely]. |
| 2 | **How age is checked** | (a) Ask for a date of birth. (b) Ask grade and graduation year (current). (c) The parent attests age when adding a student. | **(c) plus (b).** Have the parent attest "this student is 13 or older" when adding a student or sending an invite, and keep not storing a date of birth. Needs a small UI change; not built yet. |
| 3 | **Who the account holder is** | (a) Adults only; students only under a household. (b) Independent student sign-up (students 18+ without a parent). | **(a) at launch.** The schema has `is_independent` [Certain], but contracting with minors is risky [Likely]. Revisit for students who are 18 or older. |
| 4 | **Legal entity and contacts** | LLC or other entity; privacy email; postal address | Required in both documents. |
| 5 | **Data retention** | Per data type; see the privacy draft | Delete practice history within 30 days of deleting the student or household. Keep email-sent records 13 months. Keep billing records per tax law. |
| 6 | **Deletion and export** | (a) Build in-app deletion and export. (b) Manual by email, with a stated response time. | **(b) at launch, (a) soon.** No deletion or export function exists today [Certain, no such RPC in migrations]. Manual handling needs a documented runbook and a service-role procedure, owned by Research. |
| 7 | **AI hints** | Keep off, or enable with a named provider | **Keep off at launch.** It is off by default (`ai_help_enabled`) [Certain]. Enabling it needs a provider, a policy update, and a no-training commitment from that provider. |
| 8 | **Data region** | US or other | Must match the hosted Supabase project's region; this is the owner's fact to confirm. |
| 9 | **Refunds, trial and renewal notices** | Policy choices | State auto-renewal laws (for example California's) require clear disclosure and easy cancellation [Likely]. Stripe's customer portal provides cancellation [Certain, #108]. |
| 10 | **Governing law and disputes** | Courts or arbitration; which state | Counsel. |
| 11 | **Student privacy laws** | Applicability | FERPA binds schools, not direct-to-family services [Likely]. California's SOPIPA and similar state laws apply to services for K-12 school purposes [Likely]: if you sell to schools, that changes everything. Several states now have laws on minors' online data [Likely]; counsel should list which apply. |
| 12 | **Trademark disclaimer** | Wording for ACT® and SAT® | Use counsel-approved non-affiliation wording. |

## What changes in the app once the text is approved (Design)

- Privacy and Terms pages, linked from the footer, sign-up, the invitation acceptance page and every email footer.
- An age attestation when adding a student or sending a student invitation (decision 2).
- "Last updated" dates. A notice when a material change is made.

## Promises in the drafts that the app can't keep yet ([[NOT BUILT]])

- Deletion and export (decision 6).
- Data export on shutdown (terms §7).
