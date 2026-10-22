# #229 corrections: before and after

Owner approval 2026-10-21: repair the older verified plans and the course-choice groups whose stored interpretation is unsupported or confuses credit hours with course counts; downgrade or hold what cannot be corrected confidently; preserve evidence and correction history.

## How

- **Plans.** Every verified plan read by `courseleaf_plan/v1` (2,485) was re-read by `courseleaf_plan/v3` (#241) from the same stored page and grid (same sha256, same `requirement_key`).
  - An independent review compared each re-extraction with the stored grid using its own reader, and hand-checked 68 plans across all 58 schools.
  - Approved plans replace their v1 record in place (`replaces_promoted` in `programs/decisions/*-plans-i229.json`). The v1 evidence stays in each run's evidence archive.
  - The others are downgraded to `partially_verified` with a `verification_correction_reason` and a `supabase/corrections.json` entry.
- **Groups.** 144 verified groups whose printed rule names hours, credits or units but store a course count were each reviewed against the stored Course List layout:
  - REPLACE: the re-extraction is exact (`*-groups-i229.json`);
  - DOWNGRADE: no exact replacement;
  - KEEP: the stored count is printed, e.g. 'Select four of the following'.

## Totals (verified only; main `8bc6414` → this PR)

| | before | after |
|---|---|---|
| Verified term-by-term plans | 3,475 at 67 schools | 3,356 at 65 schools |
| Plans downgraded to partially verified | 0 | 119 |
| Verified requirement groups | 15,062 | 15,011 |
| Verified bachelor's program records | 10,648 | 10,648 |
| Covered schools (STATUS.json) | 70 | 70 |

## What changed in the 2,366 replaced plans (independent review)

- **Rows removed from items** (none of them courses):
  - 13,580 term subtotal rows, which are now each term's `credit_hours`;
  - 1,627 plan total rows, now `rule_text`;
  - 5,755 year or term label rows, now terms;
  - 687 term header rows.
- **Rows restored:** 497 items in 103 plans that v1 had lost, mostly first terms (UNI 'Fall | Hour', UMT, SPU, West Chester and others).
- **Credits restored:** 77 decimal credits that v1 had dropped ('0.5', '1.5').
- **Kept:** no v1 course row is missing from its replacement.
- **Fields:** code, title and credits are now separate fields where the cells say so (#230). Rows that don't say so stay as printed strings.

## Downgraded plans (119)

| School | Why the plan could not be corrected exactly | Plans |
|---|---|---|
| lmu | per-plan total 'Minimum Semester Hours' not read | 54 |
| ysu | first term header 'Fall · S.H.' not read | 46 |
| slu | subtotal printed for a whole term or year | 6 |
| dunwoody | a label row the reader does not know ('Transfer Credits', 'Preadmission Courses') | 2 |
| eku | alternatives ANT 306 / ANT 371 printed differently | 1 |
| eku | printed credits not read | 1 |
| lorainccc | a label row the reader does not know ('Transfer Credits', 'Preadmission Courses') | 1 |
| marshall | subtotal printed for a whole term or year | 1 |
| oregonstate | alternatives BI 223Z / BI 103 / BI 206 printed differently | 1 |
| sc-218663 | printed for one concentration | 1 |
| uakron | a label row the reader does not know ('Transfer Credits', 'Preadmission Courses') | 1 |
| uic | printed credits not read | 1 |
| umt | printed credits not read | 1 |
| unc | subtotal printed for a whole term or year | 1 |
| uvu | subtotal printed for a whole term or year | 1 |

## Groups (144)

- 76 replaced: 60 hour or unit rules now stored as `choose_credits`, and 16 elective pools re-read.
- 51 downgraded:
  - all 12 Oklahoma State residency rules ('N of these M hours must be in residence at OSU');
  - 21 Stetson unit rules;
  - Creighton, UVM, CSUSB and PVAMU credit rules that the reader still reads as counts;
  - Columbus State, Biola and TAMUCC hour rules;
  - YSU and Case groups with wrong option sets;
  - 3 held re-extractions.
- 17 kept: the printed count is right. Five of them also print a credit minimum that is kept only in `rule_text`.
- Downgrades by school: stetson 21, okstate 12, columbusstate 3, sc-218663 2, case 2, csusb 2, uvm 2, apu 1, utep 1, biola 1, creighton 1, pvamu 1, tamucc 1, ysu 1.

## Per school

| School | plans replaced | plans downgraded | groups replaced | groups downgraded | groups kept |
|---|---|---|---|---|---|
| odu | 140 |  |  |  |  |
| ncsu | 129 |  |  |  | 1 |
| okstate | 89 |  | 28 | 12 |  |
| temple | 127 |  |  |  |  |
| oregonstate | 121 | 1 |  |  |  |
| uvu | 112 | 1 | 1 |  | 2 |
| uoregon | 113 |  |  |  |  |
| utexas | 90 |  |  |  |  |
| unh-183044 | 85 |  |  |  |  |
| coloradomesa | 83 |  |  |  | 1 |
| uic | 80 | 1 |  |  |  |
| sc-218663 | 70 | 1 | 7 | 2 |  |
| marshall | 75 | 1 |  |  |  |
| uakron | 63 | 1 |  |  |  |
| tamuk | 63 |  |  |  |  |
| slu | 56 | 6 |  |  |  |
| unomaha | 61 |  |  |  |  |
| uidaho | 56 |  |  |  |  |
| lmu |  | 54 |  |  |  |
| pace | 52 |  |  |  |  |
| ysu |  | 46 | 1 | 1 |  |
| sru | 45 |  |  |  | 1 |
| uaa | 44 |  |  |  |  |
| louisville | 40 |  |  |  |  |
| tamucc | 33 |  | 6 | 1 |  |
| umt | 39 | 1 |  |  |  |
| uni | 39 |  |  |  |  |
| njit | 38 |  |  |  |  |
| eku | 35 | 2 |  |  |  |
| tulane | 37 |  |  |  |  |
| calpoly | 35 |  |  |  |  |
| csupueblo | 32 |  |  |  |  |
| spu | 32 |  |  |  |  |
| lasalle | 31 |  |  |  |  |
| vsu | 29 |  |  |  |  |
| uwm | 28 |  |  |  |  |
| georgian | 23 |  |  |  | 3 |
| qu | 25 |  |  |  |  |
| stetson |  |  | 3 | 21 |  |
| unc | 22 | 1 |  |  |  |
| jsu | 20 |  |  |  |  |
| wcupa | 17 |  |  |  | 1 |
| clayton | 16 |  |  |  |  |
| wit | 12 |  |  |  |  |
| miamioh-204024 |  |  | 10 |  |  |
| wayne | 8 |  |  |  | 1 |
| utep |  |  | 8 | 1 |  |
| jhu | 5 |  |  |  |  |
| wku |  |  | 3 |  | 2 |
| csusb |  |  | 2 | 2 |  |
| csus | 1 |  | 2 |  |  |
| dunwoody | 1 | 2 |  |  |  |
| georgetown | 3 |  |  |  |  |
| columbusstate |  |  |  | 3 |  |
| apu | 1 |  |  | 1 |  |
| lorainccc | 1 | 1 |  |  |  |
| tmcc | 1 |  | 1 |  |  |
| western | 2 |  |  |  |  |
| pvamu |  |  | 1 | 1 |  |
| ucdavis |  |  | 2 |  |  |
| case |  |  |  | 2 |  |
| uvm |  |  |  | 2 |  |
| northeastern |  |  |  |  | 2 |
| dyu | 1 |  |  |  |  |
| nmc | 1 |  |  |  |  |
| rider | 1 |  |  |  |  |
| tamu | 1 |  |  |  |  |
| ucdenver | 1 |  |  |  |  |
| uncg | 1 |  |  |  |  |
| unk |  |  | 1 |  |  |
| biola |  |  |  | 1 |  |
| creighton |  |  |  | 1 |  |
| purdueglobal |  |  |  |  | 1 |
| stkate |  |  |  |  | 1 |
| wisc |  |  |  |  | 1 |

## Follow-ups

- Reader work to recover the downgraded plans:
  - LMU's per-plan 'Minimum Semester Hours' total;
  - YSU's 'S.H.' header;
  - subtotals printed for a whole term or year (SLU sub-sessions, Marshall, UVU, UNC);
  - '.5', '3 or 4' and '1 (0)' credits.
- #250: Course List subjects of 6–7 letters or two words.
