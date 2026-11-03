# UTC credit mappings for the planning pilot (#191)

**Owner:** Research. **Reader:** Design (`PILOT_ACCEPTANCE.md` §2, checklist item 4). **As of:** 2026-11-03, main `58252e6`.
**Scope:** UTC's AP table (57 rows) and CLEP table (36 rows) in `data/institutions/utc/credit_policies/2026-27.json`, for
the UTC Management B.S.B.A. pilot.

## Outcome

**No year-labelled official source could be read, so neither table is verified and every AP and CLEP mapping is
excluded.** No data file changes. Both records stay `partially_verified`, so the app's existing rule (verified tables
only) already excludes them. Design needs no new mechanism: the exclusion shape is the whole table at
`partially_verified` (see "Exclusion shape" below).

- **Other UTC credit records:** IB (25 rows) and dual enrollment are also `partially_verified`, so they're hidden too
  (`PILOT_ACCEPTANCE.md` §1).
- **Values:** every one of the 93 rows was compared cell by cell (exam, minimum score, course(s), hours) with the raw
  pages fetched today. Every score, course and hour value is printed as stored. The only differences are spacing in
  3 CLEP course cells and 2 non-numeric hours cells stored as empty (details below).
- **Year:** the AP page prints only "Updated 10.23.2023" and the CLEP page only "*Updated 04/06/2026". Neither prints an
  academic year. The standing rule applies (#191, 2026-10-08; applied to UTK under the owner-approved #218 C4 decision):
  an unlabelled table is not evidence for a specific academic year, so it stays `partially_verified`.
- **The year-labelled source exists but can't be read.** UTC's 2026-2027 Undergraduate Catalog has catoid=53; its home
  page prints "2026-2027 Undergraduate Catalog" and "Published May 1, 2026". The registrar's Course Catalogs page lists
  "2026-27" and links to it. The home page was fetched. Every content page answered with a bot challenge (HTTP 202), and
  the crawler stopped after four, as designed. Its search pages are
  disallowed by robots.txt. The challenge was recorded, not evaded. This matches 60 challenged requests in October
  (`programs/queue/TN.json`).
- **One mapping is out of date in any case.** UTC's math placement page says: "Note: Beginning Fall 2026, 3 math courses
  have course number changes: MATH 1530 was previously 2100 …". The AP page (updated 2023) still awards **MATH 2100** for
  AP Statistics. Even with a year label, that row would need UTC to print the current number before it could be shown.

## Sources (raw, retained)

Run `pipeline/runs/TN/2026-11-03`, branch `pipeline-run/tn-utc-credit-2026-11-03` (workflow run 41731291211). The run
request is `pipeline/run-request.json` on that branch. The branch is never merged; it holds the raw pages, as
`pipeline-run/tn-utc-fees-2026-10-21` does for CR-17.

| Page | Fetched (UTC) | Page file | sha256 | Year label printed |
|---|---|---|---|---|
| [AP Credit by Exam](https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/ap-exam) | 2026-11-03 22:32 | `e5fdf13b85da1f5b2389.json.gz` | `e5fdf13b85da1f5b…` | none ("Updated 10.23.2023") |
| [CLEP credit](https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/clep) | 2026-11-03 22:32 | `044755e2f3a124269f40.json.gz` | `044755e2f3a12426…` | none ("*Updated 04/06/2026") |
| [Math Placement Criteria](https://www.utc.edu/arts-and-sciences/mathematics/student-resources/placement-test/placement) | 2026-11-03 22:32 | `d9af1ab0944bed2daf85.json.gz` | `d9af1ab0944bed2d…` | "Beginning Fall 2026" (renumbering note) |
| [Registrar: Course Catalogs](https://www.utc.edu/academic-affairs/registrar/course-catalogs) | 2026-11-03 22:32 | `d894945ade4e20d0ca30.json.gz` | `d894945ade4e20d0…` | lists "2026-27"; links catoid=53 |
| [2026-2027 Undergraduate Catalog home](https://catalog.utc.edu/index.php?catoid=53) | 2026-11-03 22:32 | `2aa05d341ff4b556668d.json.gz` | `2aa05d341ff4b556…` | "2026-2027 Undergraduate Catalog" (home page only) |
| Catalog content pages (`content.php?catoid=53&navoid=2300`, `2283`, `2292`, `2293`, then others) | 2026-11-03 | — | — | `blocked_bot_challenge`: 4 consecutive challenges (5 in all; navoid 2300 retried once), then 10 stop records (`host_challenge_stop`) |
| Catalog search (`search_advanced.php`: "Advanced Placement", "MATH 1950", "DATA 2130") | 2026-11-03 | — | — | `disallowed_by_robots` |

The comparison was repeated against the 2026-11-02 weekly run (AP `325ccc1a80bcc4cb…`, CLEP `f9a07c5ebe7c392f…`) with
identical results. The pipeline's own review of today's run agrees: AP `same`; CLEP `changed` only for the 3 spacing
cells, plus the no-credit row it doesn't extract; both `year_basis: source_unlabeled`.

## (a) Verified mappings Design may show

**None.** No UTC AP or CLEP row is `verified`, so no UTC exam credit may be placed, counted or shown as fact. The page's
current behaviour is correct as it stands:
- no credit placed;
- "Academic year unconfirmed" for AP;
- "on file but not yet verified" for CLEP. The CLEP record has no `academic_year_basis` field, so the pill can't say
  "Academic year unconfirmed" for it. See "Follow-ups".

## (b) Mappings to exclude: all 93, each with its reason

**Reason codes**
- **Y (every row): the year is unconfirmed.** The source prints no academic year (AP "Updated 10.23.2023"; CLEP
  "*Updated 04/06/2026"), and the 2026-2027 catalog, which would carry it, is behind a bot challenge.
- **R: the course number is retired.** UTC's math page: "Beginning Fall 2026 … MATH 1530 was previously 2100". The table
  still prints MATH 2100. This row can't be shown even after a year label is found, unless UTC prints the 2026-27 number.
- **N: not a credit mapping.** No hours are awarded: Music Theory "Subscores" ("Contact Music Department", hours "Per
  Department"), and CLEP Social Sciences & History ("No Credit", hours "-"). Never show either as credit.
- **S: spacing differs, values agree.** The page prints the course codes without a space ("BIOL1120/1120L",
  "CHEM1110/1110L", "ENGL2230"). The record stores them spaced. Same courses, same hours.
- **P: placeholder course.** `1XXX`/`2XXX`, "Elective" or "Elec 1XXX" names no specific course, so it can never fill a
  named plan row even when verified. It could only count as elective hours.

The "Raw page" column compares exam, minimum score, course(s) and hours.
- **Exam names:** seven AP rows store current College Board exam names where the page prints older ones. They are
  matched by subject and score:
  - Physics 1 / Physics 2 ("Physics 1: Algebra-Based" / "Physics 2: Algebra-Based");
  - 2-D Art & Design ("Studio Art: 2 D Design"), 3-D Art & Design ("Studio Art: 3D Design"), Drawing ("Studio Art:
    Drawing");
  - World History: Modern ("World History");
  - United States Government & Politics ("US Government & Politics").
- **Gen-ed text** is in each record's `notes`. It isn't part of this comparison (#218 C5).

#### AP (57 rows)

| # | Exam | Min. score | Course(s) awarded | Hours | Raw page, 2026-11-03 | Reasons |
|---|---|---|---|---|---|---|
| 1 | AP Art History | 4 | ART 2140 & ART 2150 | 6 | match | Y |
| 2 | AP Art History | 3 | ART 2140 | 3 | match | Y |
| 3 | AP Biology | 3 | BIOL 1110 & BIOL 1120 | 8 | match | Y |
| 4 | AP Calculus AB | 3 | MATH 1950 | 4 | match | Y |
| 5 | AP Calculus BC | 3 | MATH 1950 & MATH 1960 | 8 | match | Y |
| 6 | AP Chemistry | 5 | CHEM 1110/1110L & CHEM 1120/1120L | 8 | match | Y |
| 7 | AP Chemistry | 4 | CHEM 1110/1110L | 4 | match | Y |
| 8 | AP Chinese Language & Culture | 5 | FLNG 1010, FLNG 1020, FLNG 2110 & FLNG 2120 | 12 | match | Y |
| 9 | AP Chinese Language & Culture | 4 | FLNG 1010, FLNG 1020 & FLNG 2110 | 9 | match | Y |
| 10 | AP Chinese Language & Culture | 3 | FLNG 1010 & FLNG 1020 | 6 | match | Y |
| 11 | AP Comparative Government & Politics | 3 | PSPS Elective | 3 | match | Y, P |
| 12 | AP Computer Science A | 4 | CPSC 1100 | 4 | match | Y |
| 13 | AP Computer Science Principles | 4 | CPSC 1XXX | 3 | match | Y, P |
| 14 | AP English Language & Composition | 4 | ENGL 1010 & ENGL 1020 | 6 | match | Y |
| 15 | AP English Language & Composition | 3 | ENGL 1010 | 3 | match | Y |
| 16 | AP English Literature & Composition | 3 | ENGL 1330 | 3 | match | Y |
| 17 | AP Environmental Science | 3 | ESC 1500 & ESC 1510 | 8 | match | Y |
| 18 | AP European History | 4 | HIST 2220 | 3 | match | Y |
| 19 | AP French Language & Culture | 5 | FREN 1010, FREN 1020, FREN 2110 & FREN 2120 | 14 | match | Y |
| 20 | AP French Language & Culture | 4 | FREN 1010, FREN 1020 & FREN 2110 | 11 | match | Y |
| 21 | AP French Language & Culture | 3 | FREN 1010 & FREN 1020 | 8 | match | Y |
| 22 | AP German Language & Culture | 5 | GER 1010, GER 1020, GER 2110 & GER 2120 | 14 | match | Y |
| 23 | AP German Language & Culture | 4 | GER 1010, GER 1020 & GER 2110 | 11 | match | Y |
| 24 | AP German Language & Culture | 3 | GER 1010 & GER 1020 | 8 | match | Y |
| 25 | AP Human Geography | 3 | GEOG 1040 | 3 | match | Y |
| 26 | AP Italian Language & Culture | 5 | ITAL 1010, ITAL 1020, ITAL 2110 & ITAL 2120 | 14 | match | Y |
| 27 | AP Italian Language & Culture | 4 | ITAL 1010, ITAL 1020 & ITAL 2110 | 11 | match | Y |
| 28 | AP Italian Language & Culture | 3 | ITAL 1010 & ITAL 1020 | 8 | match | Y |
| 29 | AP Japanese Language & Culture | 5 | FLNG 1010, FLNG 1020, FLNG 2110 & FLNG 2120 | 12 | match | Y |
| 30 | AP Japanese Language & Culture | 4 | FLNG 1010, FLNG 1020 & FLNG 2110 | 9 | match | Y |
| 31 | AP Japanese Language & Culture | 3 | FLNG 1010 & FLNG 1020 | 6 | match | Y |
| 32 | AP Latin | 4 | LAT 1010, LAT 1020, LAT 2010 & LAT 2020 | 12 | match | Y |
| 33 | AP Macroeconomics | 3 | ECON 1010 | 3 | match | Y |
| 34 | AP Microeconomics | 3 | ECON 1020 | 3 | match | Y |
| 35 | AP Music Theory | 5 | MUS 1710 & MUS 1720 | 4 | match | Y |
| 36 | AP Music Theory | 4 | MUS 1710 | 2 | match | Y |
| 37 | AP Music Theory | 3 | MUS 1060 | 3 | match | Y |
| 38 | AP Music Theory | Subscores | Contact Music Department (423-425-4601) |  | hours printed "Per Department" (stored empty) | Y, N |
| 39 | AP Physics C: Electricity & Magnetism | 4 | PHYS 2310/2310L | 4 | match | Y |
| 40 | AP Physics C: Mechanics | 4 | PHYS 2300/2300L | 4 | match | Y |
| 41 | AP Physics 1 | 3 | PHYS 1030/1030L | 4 | match | Y |
| 42 | AP Physics 2 | 3 | PHYS 1040/1040L | 4 | match | Y |
| 43 | AP Precalculus | 3 | MATH 1730 | 4 | match | Y |
| 44 | AP Psychology | 3 | PSY 1010 | 3 | match | Y |
| 45 | AP Research | 3 | Elec 1XXX | 3 | match | Y, P |
| 46 | AP Seminar | 3 | Elec 1XXX | 3 | match | Y, P |
| 47 | AP Spanish Language & Culture | 5 | SPAN 1010, SPAN 1020, SPAN 2110 & SPAN 2120 | 14 | match | Y |
| 48 | AP Spanish Language & Culture | 4 | SPAN 1010, SPAN 1020 & SPAN 2110 | 11 | match | Y |
| 49 | AP Spanish Language & Culture | 3 | SPAN 1010 & SPAN 1020 | 8 | match | Y |
| 50 | AP Spanish Literature & Culture | 5 | SPAN 3310 | 3 | match | Y |
| 51 | AP Statistics | 3 | MATH 2100 | 3 | match | Y, R |
| 52 | AP 2-D Art & Design | 3 | ART 1XXX (Lower Division) | 3 | match | Y, P |
| 53 | AP 3-D Art & Design | 3 | ART 1XXX (Lower Division) | 3 | match | Y, P |
| 54 | AP Drawing | 3 | ART 1XXX (Lower Division) | 3 | match | Y, P |
| 55 | AP United States History | 4 | HIST 2010 | 3 | match | Y |
| 56 | AP United States Government & Politics | 3 | PSPS 1010 | 3 | match | Y |
| 57 | AP World History: Modern | 4 | HIST 1120 | 3 | match | Y |

Printed on the AP page but not on file: Physics B 4 → PHYS 1030/1030L & PHYS 1040/1040L (8 hours); Physics B 3 → PHYS 1030/1030L (4 hours).

#### CLEP (36 rows)

| # | Exam | Min. score | Course(s) awarded | Hours | Raw page, 2026-11-03 | Reasons |
|---|---|---|---|---|---|---|
| 1 | CLEP American Government | 50 | PSPS 1010 | 3 | match | Y |
| 2 | CLEP American Literature | 50 | ENGL 2130 | 3 | match | Y |
| 3 | CLEP Analyzing & Interpreting Literature | 50 | ENGL 1330 | 3 | match | Y |
| 4 | CLEP Biology | 50 | BIOL 1110/1110L & BIOL 1120/1120L | 8 | spacing only: printed "BIOL 1110/1110L & BIOL1120/1120L" | Y, S |
| 5 | CLEP Calculus | 50 | MATH 1950 | 4 | match | Y |
| 6 | CLEP Chemistry | 50 | CHEM 1110/1110L & CHEM 1120/1120L | 8 | spacing only: printed "CHEM1110/1110L & CHEM1120/1120L" | Y, S |
| 7 | CLEP College Algebra | 50 | MATH 1130 | 3 | match | Y |
| 8 | CLEP College Composition | 50 | ENGL 1010 & ENGL 1020 | 6 | match | Y |
| 9 | CLEP College Composition Modular | 50 | ENGL 1020 | 3 | match | Y |
| 10 | CLEP College Mathematics | 50 | MATH 1010 | 3 | match | Y |
| 11 | CLEP English Literature | 50 | ENGL 2230 | 3 | spacing only: printed "ENGL2230" | Y, S |
| 12 | CLEP Financial Accounting | 50 | ACC 1XXX | 3 | match | Y, P |
| 13 | CLEP French Language Level 1 | 50 | FREN 1010 & FREN 1020 | 8 | match | Y |
| 14 | CLEP French Language Level 2 | 59 | FREN 2110 & FREN 2120 | 6 | match | Y |
| 15 | CLEP German Language Level 1 | 50 | GER 1010 & GER 1020 | 8 | match | Y |
| 16 | CLEP German Language Level 2 | 60 | GER 2110 & GER 2120 | 6 | match | Y |
| 17 | CLEP History of the United States I | 50 | HIST 2010 | 3 | match | Y |
| 18 | CLEP History of the United States II | 50 | HIST 2020 | 3 | match | Y |
| 19 | CLEP Human Growth & Development | 50 | PSY 2220 | 3 | match | Y |
| 20 | CLEP Humanities | 50 | ENGL 1150 | 3 | match | Y |
| 21 | CLEP Information Systems & Computer Applications | 50 | MGT 1XXX | 3 | match | Y, P |
| 22 | CLEP Introduction to Educational Psychology | 50 | EDUC 2XXX | 3 | match | Y, P |
| 23 | CLEP Introductory Business Law | 50 | BUS 1XXX | 3 | match | Y, P |
| 24 | CLEP Introductory Psychology | 50 | PSY 1010 | 3 | match | Y |
| 25 | CLEP Introductory Sociology | 50 | SOC 1510 | 3 | match | Y |
| 26 | CLEP Natural Sciences | 50 | GNSC 1110/1110L | 4 | match | Y |
| 27 | CLEP Precalculus | 50 | MATH 1730 | 4 | match | Y |
| 28 | CLEP Principles of Macroeconomics | 50 | ECON 1010 | 3 | match | Y |
| 29 | CLEP Principles of Microeconomics | 50 | ECON 1020 | 3 | match | Y |
| 30 | CLEP Principles of Management | 50 | MGT 1XXX | 3 | match | Y, P |
| 31 | CLEP Principles of Marketing | 50 | MKT 1XXX | 3 | match | Y, P |
| 32 | CLEP Social Sciences & History | 50 | No Credit |  | hours printed "-" (stored empty) | Y, N |
| 33 | CLEP Spanish Language Level 1 | 50 | SPAN 1010 & SPAN 1020 | 8 | match | Y |
| 34 | CLEP Spanish Language Level 2 | 63 | SPAN 2110 & SPAN 2120 | 6 | match | Y |
| 35 | CLEP Western Civilization I | 50 | HIST 1110 | 3 | match | Y |
| 36 | CLEP Western Civilization II | 50 | HIST 1120 | 3 | match | Y |

## (c) Unsupported plan-row matches (UTC Management B.S.B.A.)

All of the matches below are hypothetical, because every row above is excluded (Y). They say what a future verified
table could and couldn't do in Management's plan (`data/institutions/utc/degree_requirements/2026-27.json`,
`management-b-s-b-a`, verified). Nothing here is an equivalency claim.

**Applicability questions (CR-19): not published.**

| Credit | Plan row as printed | Answer | UTC sources checked |
|---|---|---|---|
| AP Calculus AB 3 → MATH 1950 (also CLEP Calculus 50 → MATH 1950) | Year 1 Fall, `MATH 1130` "College Algebra or MATH 1830: Calculus for Mgt., Life, and Social Sciences (Quantitative Reasoning)" | **Not published.** No UTC source says MATH 1950 satisfies MATH 1130 or MATH 1830. | AP page: its only applicability note is "The Chemistry Department recommends that Chemistry majors NOT use AP Chemistry Credit". PLA pages: credit "can count toward general education, major or minor requirements", with no course-level substitution. Math placement page: MATH 1950's prerequisite is 1730 (1720) or ACT 28 (660), which is a placement rule, not a substitution. Management plan PDF: prints the row only. Catalog course descriptions (MATH 1830, MATH 1950) and College of Business catalog pages: bot challenge or robots-disallowed. |
| AP Statistics 3 → MATH 2100 | Year 2 Fall, `DATA 2130` "Statistics for Business (Quantitative Reasoning)" | **Not published.** No UTC source says MATH 2100 (now MATH 1530) satisfies DATA 2130. The AP row is also excluded for R. | Same as above. The math placement page gives the renumbering only. Catalog descriptions for MATH 1530 and DATA 2130: bot challenge or robots-disallowed. |

**What a verified table would and wouldn't fill in this plan.** This follows Design's rule: only the row's own code, an
option's own code, `any_of`, or exact free text fills a row.

| Credit (exam, score → course) | Plan row | Would fill? |
|---|---|---|
| AP Macroeconomics 3 → ECON 1010; CLEP Principles of Macroeconomics 50 → ECON 1010 | Year 2 Spring `ECON 1010` | Yes: own code |
| AP Microeconomics 3 → ECON 1020; CLEP Principles of Microeconomics 50 → ECON 1020 | Year 2 Fall `ECON 1020` | Yes: own code |
| AP English Language 4 → ENGL 1010 & ENGL 1020; CLEP College Composition 50 → ENGL 1010 & ENGL 1020 | Year 1 Spring `ENGL 1020` | Yes, ENGL 1020 only |
| CLEP College Composition Modular 50 → ENGL 1020 | Year 1 Spring `ENGL 1020` | Yes: own code |
| ENGL 1010 from the above, or AP English Language 3 → ENGL 1010 | Year 1 Fall "Elective (ENGL 1010 or 1011)*" | **No.** It's free text with alternatives and a placement footnote. |
| CLEP College Algebra 50 → MATH 1130 | Year 1 Fall `MATH 1130` | Yes: own code (CLEP table only) |
| AP Calculus AB / BC, CLEP Calculus → MATH 1950 (& 1960) | Year 1 Fall `MATH 1130` row | **No.** MATH 1950 isn't named. Not published (above). |
| AP Precalculus 3, CLEP Precalculus 50 → MATH 1730; CLEP College Mathematics 50 → MATH 1010 | none | **No.** Not in the plan. |
| AP Statistics 3 → MATH 2100 | Year 2 Fall `DATA 2130` | **No.** Not published; course renumbered (R). |
| CLEP Principles of Management, Information Systems & Computer Applications → MGT 1XXX | `MGT 3150`, `DATA 3600` | **No.** Placeholder (P); different level. |
| CLEP Principles of Marketing → MKT 1XXX | `MKT 3130` | **No.** Placeholder (P). |
| CLEP Introductory Business Law → BUS 1XXX | `BUS 3350` | **No.** Placeholder (P). |
| CLEP Financial Accounting → ACC 1XXX | `ACC 2010` | **No.** Placeholder (P). |
| Gen-ed designations (e.g. "23GE Humanities & Fine Arts", "23GE Natural Science Lecture/Lab") | "Humanities and Fine Arts", "Natural Science with Lab", "Individual and Global Citizenship" | **No.** The designations are note text only; a structured field is #218 C5. |
| "Elective" rows | Year 2 Spring "Elective" (0-2) | **No.** Free text; no rule places credit there. |

So even after verification, the most this plan could take from UTC's AP/CLEP tables is ECON 1010, ECON 1020 and
ENGL 1020, plus MATH 1130 from CLEP College Algebra. That's 12 hours, one row in each of four different terms. No term
would be covered. This matches Design's tested scenario (`roadmap.pilot.test.ts`), with the CLEP College Algebra row added.

## Exclusion shape

- **Status is per policy record.** `credit_equivalencies` rows have no `verification_status` of their own (see the
  initial schema migration and later `alter table`s). So "exclude" is the whole AP record and the whole CLEP record
  at `partially_verified`. This is how they're stored today.
- **Nothing to split now.** No row is verifiable, so there's nothing to separate. If the catalog later prints a table
  that matches some rows and not others, the matching rows would become their own verified record from the catalog
  source. The rest would stay in the registrar-page record. Retired-number rows (R) would always stay out.
- **For Design's test:** pin "UTC AP and CLEP records are `partially_verified` → no UTC exam credit placed". No per-row
  flag exists, and none is needed.

## Path to verified

1. **Read the 2026-2027 catalog's credit-by-examination section** (catoid=53). It's the source with a year label. It
   needs either access UTC grants, or an official export or PDF of that section. The challenge isn't evaded, so this is
   an owner or UTC contact action (the same next action as `programs/queue/TN.json`).
2. Compare that table cell by cell, as above. Upgrade only the rows it prints as stored.
3. **AP Statistics:** use UTC's printed 2026-27 number (MATH 1530, if the catalog prints it), never a substitution.

## Follow-ups (not done here)

- **CLEP record wording.** Its `notes` still say the values were "not yet confirmed against the raw page". They now are
  (above). It also lacks `academic_year_basis` (AP and IB have `aid_year_in_force_at_review_source_unlabeled`).
  - Changing either means a re-read promotion. Approving today's CLEP candidate would also store the three unspaced
    codes as printed and drop the "No Credit" row, so it hasn't been done.
  - Today the app labels CLEP "on file but not yet verified" rather than "Academic year unconfirmed".
- **AP notes vs page.** The AP record's 2026-10-03 note says the page "has dropped the discontinued Physics B exam". The
  raw pages of 2026-11-02 and 2026-11-03 still print two Physics B rows. They aren't on file. That's display-irrelevant,
  but the note is inaccurate.
