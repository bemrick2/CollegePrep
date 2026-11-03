# Deep Dive checkpoint

This file is how a new Deep Dive session picks up degree-requirement, roadmap and specialised-reader work without redoing finished work. It is updated with every Deep Dive PR. Research keeps its own file, `docs/coverage/RESEARCH_CHECKPOINT.md`.

- **Main at the last refresh:** `43d4c7269c` (merge of #279). This PR (`programs/utc-clearpath-notes`) is on top of it.
- **Ownership (owner, 2026-11-02):**
  - **Deep Dive:** programs, degree requirements and term-by-term plans, and the catalog readers behind them.
  - **Research:** school-level data, scholarships, current tuition, server and release tooling.
  - **Design:** app integration, question-bank intake and launch readiness.
  - Coordinated on #218. Degree-detail completeness is reported apart from school-level readiness.

## Numbers

Counted from `data/institutions/*`. Plans are `program_plan` records; groups are every other `degree_requirements` record.

| | main `b2c83c4` (#261) | main `2e386c2` (#281) | main `af0a2d2` (#287) = `43d4c72` | with this PR |
|---|---|---|---|---|
| Verified plans | 3,502 at 68 schools | 3,117 at 65 | 3,047 at 64 | 3,100 at 63 |
| Partially verified plans | 119 | 510 | 580 | 527 |
| Verified requirement groups | 15,307 | 15,545 | 15,545 | 15,545 |
| Partially verified groups | 51 | 89 | 89 | 89 |
| Covered schools (STATUS.json) | 73 of 2,119 | 73 | 73 | 73 |

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

## This PR: UTC Clear Path notes, and the plans the re-read missed

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

The other 16 verified EOU plans were audited line by line and stay verified.

**Pilot app (web).** The fixture was rebuilt. `CollegePlan.test.tsx` and `roadmap.pilot.test.ts` now describe today's data: Management is verified and shows "Partly on file", because the AP table is still unverified. The unverified-plan wording stays tested by patching the record. Design to review on #218.

## Still held (backlog, not release-blocking)

- **CourseLeaf re-reads:**
  - 111 structural, of which 54 wait only on the 'or'-string policy below;
  - 28 note-only with findings (UNO disclaimer joined to the last footnote, Kingsville Course List notes, WIT 'ENGL/HSS Note', NCSU career text and GPA heading, UNH outcomes, DYU);
  - reader-held re-reads (`PLAN_REREAD_INVENTORY.md`).
- **Readers to extend:**
  - notes printed before a grid or under a 'Notes:' heading (LMU);
  - `courseleaf_plangrid` notes (UW-Madison, SHSU);
  - Acalog plan notes (EOU);
  - SmartCatalog sample plans versus requirement sections (PDX);
  - Clear Path checklists over a page break (UTC geology).
- **#229 remainder:** 49 plans and 51 groups (multi-row 'or', YSU separators, LMU sessions, spanning subtotals).
- **#250:** re-extract and review the schools the Course List reader affects; the 225-group audit needs owner approval.
- **EOU tidy-up:** page debris ('Updated June 2024', '|') and plan notes stored as course rows in some verified EOU records. The text is present; only its placement is off.
- **Unchanged plans:** a sampled completeness audit of the ~2,400 plans the re-reads did not change.
- **Depth at high-enrolment schools:** Texas A&M, CU Boulder groups; Penn State, Illinois, UF, UC Davis, UC Irvine plans.

## Decision recommended to the owner (not blocking)

**'Or' rows kept as the exact printed string (54 plans).** Recommendation: accept them as verified when the string is stored verbatim and the app shows it as printed, not as parsed alternatives. The 2026-10-22 data rule asks for printed options to be preserved, and these are. Before approving them, check that the credit engine places no credit into such a row (not yet tested). Until decided, they stay held.

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
