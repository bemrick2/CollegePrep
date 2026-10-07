# Question bank: size, distribution, sources and editorial review (#19)

Status: **proposal for owner decision**. Nothing here changes the app's weekly goal. The default stays 40 questions a week. When fresh content runs out, the app says so plainly (#163) rather than hiding the shortage with a smaller goal.

Tags: [Certain] = verified against a source or the code; [Likely] = strong but unverified; [Guessing] = estimate.

## 1. Where we are

- **Bank** [Certain]: 58 items. ACT 38 (English 10, Math 12, Reading 8, Science 8); SAT 20.
- **Reviewed by AI only** [Certain]: all 58 were reviewed by Claude in separate contexts, with two blind solves and an audit (`questionReviews.json`, `human_reviewed: false`). No human has reviewed them, so they are not launch-ready content.
- **Weekly goal** [Certain]: onboarding offers 20, 40 (default) or 60 a week.
- **Check cadence** [Certain]: a baseline, then a mini check every 35 days, and a "full" check at 70 days. The full check is currently capped at 99 per section, which in practice means the whole bank. It needs a real size before launch; see §2.
- **What happens now** [Certain]: an ACT student at 40 a week runs out of new ACT questions in week one.

## 2. Sustainable size

"Fresh" is per student: every student draws from the same pool, so the bank has to cover one student's whole horizon. That horizon is:

- new practice questions (goal × weeks),
- plus the progress-check items held out of practice (baseline plus later checks),
- plus headroom, because the plan targets weak skills and difficulty bands, so a student doesn't use the bank evenly.

| Per exam | ACT | SAT |
|---|---|---|
| Fresh practice, 8 weeks at 40 | 320 | 320 |
| Fresh practice, 12 weeks at 40 | 480 | 480 |
| Check items, baseline plus 2 minis [Certain, from `PER_SECTION`] | 27 + 13 + 13 = 53 | 18 + 8 + 8 = 34 |
| Headroom for skill and difficulty targeting [Guessing] | about 15% | about 15% |
| **Launch minimum (8 weeks)** | **≈ 430** | **≈ 410** |
| **Target (12 weeks, one semester)** | **≈ 600** | **≈ 600** |

What this means in practice:
- **A student on 60 a week** exhausts a 600-item bank in roughly 9 weeks. The app tells them so at that point, which is acceptable.
- **The full check** should be one fixed full-length practice form per exam, authored separately and held out of practice entirely:
  - ACT: 50 + 45 + 36 (+ 40 science) items.
  - SAT: 54 + 44 items.
  - Until that form exists, the full check should fall back to a mini. That needs a code change, and I recommend it before launch.

**Recommendation:** ship at no less than the launch minimum per exam. Better still, launch with one exam only (ACT or SAT) at the 12-week target rather than both exams thin.

## 3. Skill distribution

The bank is weighted by the official blueprints, so practice mirrors the test. The planner then over-samples a student's weak skills from within that pool.

### ACT (enhanced ACT, 600 items)

Sources: ACT reporting-category tables and the ACT enhancements FAQ.
- **Test length** [Certain]: English 50 Q, Math 45, Reading 36, Science 40 (Science optional since Sept 2025).
- **Category ranges** [Likely]: the item ranges come from the ACT PDF, read through a summarising fetch tool. The editor should re-check them against the PDF before briefs go out.

Section split, by test length: English 176, Math 158, Reading 126, Science 140.

**English (176 items, ≈ 18 passages of about 10 items each)**

| Reporting category | Enhanced range | Items |
|---|---|---|
| Production of Writing | 15–17 | 71 |
| Knowledge of Language | 7–9 | 35 |
| Conventions of Standard English | 15–17 | 70 |

**Math (158 items, mostly discrete)**

Preparing for Higher Math (33 on the test, about 80%) gives 126 items:

| Subcategory | On the test | Items |
|---|---|---|
| Number & Quantity | 4–5 | 17 |
| Statistics & Probability | 5–6 | 21 |
| Algebra | 7–8 | 30 |
| Functions | 7–8 | 29 |
| Geometry | 7–8 | 29 |

Integrating Essential Skills (8 on the test, about 20%) gives 32 items.

Modeling is a cross-tag on at least 20% of the test, so at least 32 of these items should also carry it.

**Reading (126 items, ≈ 14 passages of about 9 items each, including paired passages)**

| Reporting category | Enhanced range | Items |
|---|---|---|
| Key Ideas & Details | 12–14 | 61 |
| Craft & Structure | 7–9 | 37 |
| Integration of Knowledge & Ideas | 5–7 | 28 |

**Science (140 items, ≈ 20 data or experiment sets of about 7 items each)**

| Reporting category | Enhanced range | Items |
|---|---|---|
| Interpretation of Data | 13–17 | 62 |
| Scientific Investigation | 6–11 | 35 |
| Evaluation of Models, Inferences & Experimental Results | 8–13 | 43 |

### SAT (digital SAT, 600 items)

Source: College Board domain table, as reproduced in Rhode Island Department of Education materials. The structure is [Certain]; counts are as stated in that document.
- **Test length:** Reading and Writing 54 Q, Math 44, each in two adaptive modules.
- **Section split:** Reading and Writing 331, Math 269.

**Reading and Writing (331 items)**

Each Reading and Writing item has its own short passage, so this is about 331 short passages to write or source. It is the single largest authoring cost.

| Domain | On the test | Items |
|---|---|---|
| Craft and Structure | ≈ 28% (13–15) | 93 |
| Information and Ideas | ≈ 26% (11–14) | 86 |
| Standard English Conventions | ≈ 26% (11–15) | 86 |
| Expression of Ideas | ≈ 20% (8–12) | 66 |

**Math (269 items)**

| Domain | On the test | Items |
|---|---|---|
| Algebra | ≈ 35% (13–15) | 94 |
| Advanced Math | ≈ 35% (13–15) | 94 |
| Problem-Solving and Data Analysis | ≈ 15% (5–7) | 40 |
| Geometry and Trigonometry | ≈ 15% (5–7) | 41 |

About 25% of math items should be student-produced response (numeric entry) [Likely].

### Difficulty, both exams

- Target roughly a third each of easy, medium and hard per skill [Guessing; calibrate after launch from first-answer accuracy].
- The SAT's adaptive second module means hard items must not be thin.

### Sections already done

The 58 existing items count toward these targets once a human reviews them. The gap is about 562 for ACT and 580 for SAT at the 12-week target.

## 4. Content sources

| Source | Rights position | Use for | Owner decision |
|---|---|---|---|
| **Original items, written by people we contract** | We own them if contracts assign copyright (work-for-hire or assignment) [Likely; a lawyer should confirm the contract wording]. | Everything. This is the default. | Budget and authors. Whether AI-drafted items edited by humans are acceptable; if so, say so in the terms and keep human review mandatory. |
| **US federal government works** (NASA, NOAA, USGS, NIH, Census text and data) | Not copyrighted under 17 U.S.C. §105 [Certain]. Third-party images inside them may still be copyrighted [Certain]. | ACT Science data sets; SAT and ACT informational passages; math data contexts. | None; the editor records the source URL per passage. |
| **Public-domain literature** (e.g. Project Gutenberg texts published before 1931) | US public domain [Certain for pre-1931 US publication]. Gutenberg's license and trademark apply to its packaging, not to the underlying public-domain text [Likely]. | ACT and SAT literary passages, excerpted and lightly adapted. | None. Avoid modern translations and editions, which carry their own copyright. |
| **OpenStax textbooks** | Most are CC BY 4.0 [Certain]; some titles carry a non-commercial license [Likely, check per book]. CC BY requires attribution [Certain]. | Science and social-science passage material, math contexts. | Accept showing attribution on the item (the `source_attribution` column exists [Certain]). |
| **Licensed commercial item banks** (test-prep publishers and item vendors) | Terms unknown until negotiated [Guessing]. The license must cover display in an app, editing, per-student analytics, and use after the contract ends. | Fastest path to volume. | Whether to spend money here; which vendors to approach. I have not contacted anyone. |
| **Official College Board and ACT material** (SAT Suite Question Bank, Bluebook tests, ACT free practice tests) | Copyrighted [Certain]. I could not verify the reuse terms [unverified]. I would not copy these items into our bank without written permission [Likely the right call]. | Link out to them as free official practice, especially full-length tests; don't ingest them. | Whether to seek a license. Linking out needs no decision [Likely]. |

**Recommendation:**
- Original items as the backbone.
- Federal and public-domain passages to cut passage-writing cost.
- Link out to official full-length tests rather than recreating them.

## 5. Editorial review workflow (human)

The database gate already exists, from #142 / CR-21 [Certain]:
- An item is served only when `status = 'published'` and `review_current`.
- Any change to its content voids approval through the content hash.
- `approve_practice_question` records who, when and how.

The workflow below supplies the "how". Every item passes each stage in order. Any content edit sends it back to stage 4.

### Stages

| # | Stage | Who | Pass criteria |
|---|---|---|---|
| 1 | **Brief** | Content lead | Exam, section, blueprint category, skill, target difficulty, item type, passage plan. |
| 2 | **Draft** | Author | Stem, choices, key, one explanation per choice, hint, skill tags, expected time, source and license for any passage. |
| 3 | **Rights check** | Rights reviewer (can be the content lead) | Source is original, federal, public domain or licensed, with proof recorded (URL, contract, license). CC BY attribution text is filled in. Anything else is rejected. |
| 4 | **Blind solve ×2** | Two subject reviewers, neither the author | Each solves the item without the key, explanations or hint, and records answer and time. Both must match the key. |
| 5 | **Content audit** | One of the solvers, or an editor | Exactly one defensible answer. Each distractor reflects a plausible error. The explanation is correct for every choice. The hint doesn't give the answer away. Numeric answer forms are complete. Within blueprint scope and the right difficulty band. |
| 6 | **Fairness and sensitivity** | A reviewer outside the author's group | No cultural, regional or socioeconomic knowledge required beyond the passage. No stereotypes. Distressing topics are avoided. Names and contexts are varied across the bank. |
| 7 | **Copy edit and accessibility** | Editor | House style. Readable by a screen reader. Alt text for every figure and table, which must not leak the answer. Math renders correctly. |
| 8 | **Approve** | Content lead | Calls `approve_practice_question` with a method such as `'human: 2 blind solves + audit + fairness'`. The approver is a named human, never the author. |
| 9 | **Publish** | Content lead | `status = 'published'`. Content loads through the normal migration and import path (held while hosted is paused). |
| 10 | **Monitor** | Content lead, monthly | First-answer accuracy, time spent, and choice distribution per item. Flags: accuracy above 95% or below 15%, a distractor no one picks, or a wrong answer picked more often than the key. Flagged items go back to stage 4; retired items move to `status = 'retired'`. |

### Throughput

The rate is a [Guessing] estimate:
- **Per item:** about 30 to 45 minutes of author time and about 20 minutes total across reviewers, including passage time spread over its items.
- **Per exam at 600 items:** roughly 500 to 650 person-hours.
- At two authors and two reviewers part-time, think in months, not weeks.

### Tracking

- Use one row per item in a shared sheet or the repo fixtures, with each stage's sign-off and date. The approval record in the database is the final source of truth.
- The existing 58 AI-reviewed items enter at stage 3. They are not grandfathered.

### Gaps this workflow exposes

These are contract requests for Research on #37 (CR-24 and CR-25), not things the app does today:
- **Rights gate:** a `published` item should require a non-empty `license`, from an allowed list, plus `source_attribution` when the license requires it. Today a license change does not void approval [Certain, migration comment].
- **"Report a problem" on a question:** students and parents have no way to flag a bad item [Certain: no such feature in code]. Stage 10 needs this signal.

## 6. Decisions needed from the owner

1. Launch with one exam at the 12-week target, or both exams at the 8-week minimum?
2. Content budget: original authoring only, or also a licensed bank?
3. Are AI-drafted items acceptable if every item passes human stages 3 to 8?
4. Who is the content lead and approver? A named human is required by stage 8.
5. Should the "full" check fall back to a mini until a held-out full-length form exists? Recommended: yes.
