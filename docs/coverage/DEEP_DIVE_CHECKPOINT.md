# Deep Dive checkpoint

This file is how a new Deep Dive session picks up degree-requirement, roadmap and specialised-reader work without redoing finished work. It is updated with every Deep Dive PR. Research keeps its own file, `docs/coverage/RESEARCH_CHECKPOINT.md`.

- **Main at the last refresh:** `c8bbce6cac` (merge of Design #302). #297 and #300 are accepted as complete by the owner (2026-11-03); the count reconciliation is resolved. This PR (`programs/utc-truncated-rows`) is on top of main.
- **Deep Dive's initial-release workstream is complete** (owner, 2026-11-03). That isn't overall release approval: hosted holds stay, deployed flags stay off, and question generation stays paused.
- **Ownership (owner, 2026-11-02):**
  - **Deep Dive:** programs, degree requirements and term-by-term plans, and the catalog readers behind them.
  - **Research:** school-level data, scholarships, current tuition, server and release tooling.
  - **Design:** app integration, question-bank intake and launch readiness.
  - Coordinated on #218. Degree-detail completeness is reported apart from school-level readiness.

## Numbers

Counted from `data/institutions/*`. Plans are `program_plan` records; groups are every other `degree_requirements` record.

| | main `b2c83c4` (#261) | main `2e386c2` (#281) | main `43d4c72` (before #297) | main `6b81928` (#297) | main `e3b6beb` (#300) | with this PR |
|---|---|---|---|---|---|---|
| Verified plans | 3,502 at 68 schools | 3,117 at 65 | 3,047 at 64 | 3,100 at 63 | 3,099 at 63 | 3,095 at 63 |
| Partially verified plans | 119 | 510 | 580 | 527 | 528 | 532 |
| Verified requirement groups | 15,307 | 15,545 | 15,545 | 15,545 | 15,545 | 15,545 |
| Partially verified groups | 51 | 89 | 89 | 89 | 89 | 89 |
| Covered schools (STATUS.json) | 73 of 2,119 | 73 | 73 | 73 | 73 | 73 |

**#297 reconciliation** (every plan record at `43d4c72` vs `6b81928`; 3,627 records at both):

| Transition | Plans | Verified count |
|---|---|---|
| UTC: partially verified → verified (reviewed re-read, `replaces_correction`) | 63 | +63 |
| UTC: verified → verified (reviewed re-read adds notice and checklist; no status change) | 13 | 0 |
| EOU: verified → partially verified (audit) | 4 | −4 |
| PDX: verified → partially verified (audit) | 6 | −6 |
| **Net** | | **+53** (3,047 → 3,100) |

The 76 reviewed UTC approvals are 63 status promotions plus 13 content-only replacements. Partially verified: 580 − 63 + 10 = 527.

Verified plans outside UTC that the 2026-10-23 re-read didn't reach: **27** (20 EOU + 6 PDX + 1 UTK). An earlier chat summary said 26; that was wrong. The inventory table always listed 27.

Verified bachelor's program records: 10,665 throughout (Research and Deep Dive).

## Initial release: what Deep Dive owes, and where it stands

The app shows only `verified` records. For a release, Deep Dive owes:
1. that every verified plan and group is accurate and complete for its section;
2. the pilot's plan (UTC Management, `COLLEGE_PLANNING_PILOT.md` §4, Slice 1) verified.

| Item | State |
|---|---|
| Every verified plan whose printed notes were known to be uncaptured has been downgraded or recaptured (2026-10-23 rule) | **Done.** The CourseLeaf plans in #275/#277/#281/#286/#287. The 115 plans the 2026-10-23 re-read did not reach (`PLAN_REREAD_INVENTORY.md`) are now all handled: UTC Clear Path and pilot plans in this PR; EOU and PDX audited and downgraded in this PR; the UTK hand-reviewed plan stores its footnote and rules |
| Pilot Slice 1 plan: UTC Management | **Verified in this PR**, with its ENGL placement footnote. Every UTC business and economics plan in the pilot fixture is verified too |
| Pilot page shows the plan's footnotes | **Design (open).** The pilot renders "Elective (ENGL 1010 or 1011)*" without the note; `rule_details.footnotes` / `plan_notes` need to be shown (#218) |
| Pilot gate's other items | Not Deep Dive: UTC credit tables (#191, Research), owner copy review, hosted hold, privacy policy |
| Verified groups (15,545) | Read by readers reviewed in #258/#260/#271; the 37 UWM incomplete groups stay partially verified |
| Records with known unresolved defects | All partially verified, each with a `verification_correction_reason` and a `supabase/corrections.json` entry |

Nothing else in Deep Dive blocks the initial release. The backlog below improves coverage after it.

## #297 (merged): UTC Clear Path notes, and the plans the re-read missed

**Reader (`programs/clearpath.py`).** `printed_notes` / `add_notes` store everything a Clear Path PDF prints outside the plan grid, verbatim, from the raw text layer:
- `source_notice`: the line above the plan;
- `footnotes`: `[{marker, text, cited?}]`. A combined mark (`**+`) cites both notes. `cited: false` marks a note whose mark no row prints;
- `plan_notes`: `[{text, location, scope}]`;
- `degree_summary`: both columns of the 'Completed:' checklist.

`verify` checks the notice and every checklist row verbatim.

The reader holds a plan for:
- a mark printed with no note (`footnote_missing`);
- a repeated mark (`footnote_marker_duplicate`);
- columns after the last total (`notes_region_unreadable`);
- unread text above the plan;
- a checklist without columns (`summary_unreadable`);
- a checklist that continues over a page break (`summary_spans_pages`).

A note after a footnote is recorded as one that "may continue" it only when that footnote's last line runs to the printed width.

**Review.** Two rounds by an independent reviewer, using its own scripts on the text layer and word positions:
- **Round 1:** found that `Page.lines` strips the spaces that place a lone right-column checklist row (73 plans), and that a page-2 running title was captured (2 plans). Both are fixed and tested.
- **Round 2:** 76 approved, 7 held.

The tests cover every layout; 27 new mutants are killed.

**Promoted: 76** (all course rows unchanged):
- 63 partially verified plans verified again (`replaces_correction`; their correction entries stay);
- 13 verified plans gain their notice and checklist (`replaces_promoted`).

**Held, partially verified:**
- **Geology and Hydrogeology:** the checklist continues onto page 2.
- **Political Science:** prints '*' twice and '**' with no note.
- **Four plans** whose uncited note concerns specific courses:
  - Environmental Compliance;
  - Languages and Linguistics;
  - Spanish;
  - Spanish for the Professions.
- **Psychology:** its checklist prints '**' with no note.

**Downgraded: 10 verified plans** (independent audit, 2026-11-02; each record has the corrections entry and the quoted text):
- EOU Early Childhood Education: program conditions and prerequisites.
- EOU English/Writing on-campus and online: the BA-only language note.
- 6 PDX records whose terms are the whole requirements section: elective definitions, grade/GPA rules and printed totals not stored.
- EOU Multidisciplinary Studies: its term labels are misread (the page's 'THRID YEAR' heading is stored as an item, and terms 7-9 are labelled Second Year).

The other 16 verified EOU plans were audited line by line and stayed verified. One of them, Business Administration, was downgraded afterwards in `programs/release-backlog` (see below).

**Pilot app (web).** The fixture was rebuilt. `CollegePlan.test.tsx` and `roadmap.pilot.test.ts` now describe today's data: Management is verified and shows "Partly on file", because the AP table is still unverified. The unverified-plan wording stays tested by patching the record. Design to review on #218.

## This PR (`programs/utc-truncated-rows`): the two truncated pilot plans

- **The finding (Design, #302):** truncated rows in UTC Economics, International Public Policy and Entrepreneurship.
- **The cause:** UTC's Clear Path PDFs print those rows cut off. The PDFs' own word positions end at "(ENGL 1010 or 101", "Natural Science without La", "Controversies in Public Polic" and "Individual and Global Citizenshi". The records transcribe them exactly.
- **Why the source can't be completed:** the review workspace can't re-fetch the PDFs. utc.edu is outside its network allowlist, and robots.txt disallows the web reader. Neither is worked around.
- **Both plans are excluded from the pilot.** They are now `partially_verified`, with corrections entries (owner, 2026-11-03: exclude a pilot plan whose source can't support a complete record) and `source_rows_truncated: true`.
- **Same defect outside the pilot.** A scan of every UTC plan for rows ending in a cut-off word found two more verified plans: Middle Grades Education: English and Physics: STEM Education. Both are downgraded the same way, under the 2026-10-23 instruction.
- **Unchanged:** the #297 footnotes and checklists, and the correction history.
- **Way back to verified:** a complete official copy, captured by Research's pipeline and independently reviewed, recorded with `replaces_correction`.
- **Engine behaviour on current main (#302 supersedes Deep Dive's earlier note).** `degreeCredit.ts` fills a row only from a structured course code, or from free text that is a single reviewed code or a plain combination. Alternatives that exist only in printed wording are reported and never filled: "A or B", "Elective (ENGL 1010 or 1011)*", alternatives in a title, free-text options, comma lists. `unresolvedOrRows.test.ts` (22 tests) passes on main. This protects matching; it doesn't approve the 54 held 'or' plans.
- **Pilot after this PR:** 10 verified UTC plans and 2 excluded. `PILOT_ACCEPTANCE.md` sections 1, 3 and 5 and checklist row 5 are updated.

## #300 (merged, `e3b6bebbed`)

- **EOU Business Administration downgraded (new evidence, 2026-11-03).** All 12 terms are labelled "TYPICAL FIRST YEAR CURRICULUM", and the page's Second/Third/Fourth Year headings are stored as items. The 2026-11-02 audit compared lines and missed the labels. The Savings view shows covered-term labels, so the wrong years would be displayed. It now has a corrections entry, and verified plans go to 3,099. A nationwide scan of verified plans for year labels that repeat beyond one year found no other case; the scan's hits on "First/Second Semester" labels are expected.
- **EOU page debris: documented cleanup, not a pilot blocker.** Every EOU plan stores code-less, credit-less rows: "Updated <month year>", "|". Some also store notes as rows: Art admission, History "NOTE: …", Theatre minor recommendations, the Multidisciplinary UD list. They affect:
  - **Matching:** no. `degreeCredit.ts` treats a row with no course code as a requirement nothing fills, and a "note" row is never fillable. So no credit is placed into them, and they can only stop a term from counting as covered, which errs safe.
  - **Totals:** no; they have no credits.
  - **Displayed courses:** no. The only view that lists plan rows is the planning pilot, which holds UTC records only, and EOU isn't in it. `programFit.ts` reads terms 1–2, where EOU has no debris.

  Flagged to Design on #218. Fix them by re-reading EOU with an Acalog notes reader (backlog P3).
- **Pilot acceptance package** started: `docs/product/PILOT_ACCEPTANCE.md`. §1 (plans and their printed conditions) and the exclusions are Deep Dive's; the other sections name their owners.

## Owner decision, 2026-11-03: the 54 'or' plans stay held

The 54 plans held only because an 'or' row is kept as the exact printed string stay `partially_verified`:
- Exact transcription may be verified separately.
- Plan-level promotion needs confirmed completeness and a tested guarantee that no unsupported automated matching happens. Design writes that regression test (`PILOT_ACCEPTANCE.md` §4).
- Displaying the wording verbatim is not enough.

Since #302, printed-wording alternatives are never filled automatically (see above). That protection is necessary for promotion, but not enough on its own. Promoting the 54 plans needs reviewed completeness and an explicit distinction, in the record, between the source wording and the structured requirement.

## Backlog after release (prioritized; none of it blocks the initial release)

1. **P1: protect what is shown.**
   - When Design's 'or'-row test lands, re-check the 54 'or' plans for completeness. Promote only with that test passing and an independent review.
   - Sampled completeness audit of the ~2,400 verified plans the re-reads didn't change. A parser finding no change doesn't prove completeness.
2. **P2: recover held plans with known fixes.**
   - CourseLeaf re-reads: 28 note-only with findings (UNO disclaimer joined to the last footnote, Kingsville Course List notes, WIT 'ENGL/HSS Note', NCSU career text and GPA heading, UNH outcomes, DYU). Then 111 structural, 43 of them flat choice blocks.
   - UTC Clear Path checklists over a page break (Geology, Hydrogeology).
   - UTC plans with truncated source rows (Economics: International Public Policy, Entrepreneurship, Middle Grades Education: English, Physics: STEM Education). These need a complete official copy, which only Research's pipeline can fetch.
   - #229 remainder: 49 plans and 51 groups (multi-row 'or', YSU separators, LMU sessions, spanning subtotals).
3. **P3: readers to extend.**
   - Acalog plan notes and term structure (EOU: the four downgraded plans, Business Administration, the debris rows).
   - SmartCatalog sample plans versus requirement sections (PDX, 7 records).
   - Notes printed before a grid or under a 'Notes:' heading (LMU).
   - `courseleaf_plangrid` notes (UW-Madison, SHSU).
4. **P4: groups.** #250: re-extract and review the schools the Course List reader affects; the 225-group audit needs owner approval.
5. **P5: depth.**
   - Pilot expansion: UTK plans and hours, then MTSU (`COLLEGE_PLANNING_PILOT.md` §4).
   - High-enrolment schools: Texas A&M and CU Boulder groups; Penn State, Illinois, UF, UC Davis and UC Irvine plans.

## Blockers (recorded, not evaded)

- **Bot challenges / robots.txt:** see `RESEARCH_CHECKPOINT.md`.
- **Utah, BYU:** tab and Kuali views not stored.
- **UMD:** 28 majors print no award.
- **KU:** no single official list.
- **UCR:** PDF layout.

## How to resume

1. `git fetch origin`. Read this file, #218, #229, #250, and the open Deep Dive PRs.
2. Fetch the run branches: `git fetch origin '+refs/heads/program-run/*:refs/remotes/origin/program-run/*'`. Copy a run with `git archive`.
3. Before a reader change is promoted, extract the stored runs it can touch with main's code and with the branch's code, and explain every change.
4. Review independently, then promote. Then run:
   - retention (`--push`, `--verify-store`, `--check`);
   - `update_coverage`, `programs status`, `research_priority`, `validate_data`, `review_provenance`;
   - the database check, web `vitest` (rebuild `web/src/features/planning/pilotFixture.json` when pilot records change) and unit tests;
   - `scripts/program_mutation_check.py`, never at the same time as tests or extractions in the same tree.
5. Open the PR, merge on green CI, and update this file in the same PR.

Hosted imports, migrations and deployments stay on hold.
