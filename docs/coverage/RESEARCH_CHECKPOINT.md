# Research checkpoint

This file is how a new Research session resumes the national program-research workstream without redoing finished work. It is updated with every batch PR.

- **Main at the last refresh:** `4f2e63b0c6` (merge of #245, after Deep Dive's #239 `2c24af0`, #241 and #247, and Research's #243 and #246). The previous header named `86cbac0`, which was stale: Deep Dive's merges after batch 6 had moved main to `2c24af0` (70 covered, 10,648 verified bachelor's records, 3,475 plans at 67 schools), and those figures are confirmed below.
- **Branch carrying this checkpoint:** `research/batch-07`.
- **Ranking:** `docs/coverage/research_priority.json`, written by `python3 scripts/research_priority.py`. CI (validate-data) checks that it is current.

## Numbers

Three separate measures, never mixed: **program coverage** (bachelor's programs listed in the official catalog, docs/PROGRAM_DEPTH_COMPLETION.md), **degree-requirement depth** (requirement groups and plans of verified bachelor's programs) and **reference-data breadth** (costs, aid, admissions and the other domains in docs/coverage/coverage.json).

| | main `2c24af0` (Deep Dive) | main `4f2e63b` | research/batch-07 |
|---|---|---|---|
| Registered four-year institutions | 2,119 | 2,119 | 2,119 |
| Covered (program coverage) | 70 | 70 | 73 |
| Researched | 683 | 683 | 683 |
| Verified bachelor's program records | 10,648 | 10,648 | 10,665 |
| Verified plans (degree-requirement depth) | 3,475 at 67 schools | 3,475 at 67 schools | 3,475 at 67 schools |

Counted from `docs/coverage/programs/STATUS.json` and the `academic_programs` / `degree_requirements` files (`verified`; bachelor's records; `program_plan` rows), by reading those files at the named commit. Reference-data breadth is unchanged by this batch except that cost components now reach the database (#246).

## Completed in batch 7 (research/batch-07)

| Institution | Run | Result |
|---|---|---|
| JHU | MD/2026-10-07-cat2 | **75/75, covered** (was 67/77). The eight 'Bachelor of Music in Performance - <field>' entries are programs as printed (reading (a), agreed with Deep Dive on #153: each is its own list entry with its own Program Requirements; the award is printed on each page). The general BM in Performance (own 122-credit curriculum) is recorded too; the hub page and the Peabody-Homewood double degree are not. **Owner-approved correction:** 'Five-Year BM/MM Program' (combined bachelor's/master's) → unverified, `supabase/corrections.json`. |
| UT Dallas | TX/2026-10-21-u01 | **63/69, covered** (was 51/69). Multiple-degree reader: a page titled 'Biology (BA, BS)' gives one record per award only when it prints each degree's own heading; 12 records from 6 pages. The six combined records are corrected to unverified (owner instruction 2026-10-21 19:58 CT) so no degree counts twice. Not recorded: Education BA/BS, Visual and Performing Arts BA, Mechanical Engineering BS, two unlabelled double majors. |
| YSU | OH/2026-10-07-cat | **60/60, covered** (was 55/71). Tracks of a listed degree (same award) are options; "Bachelor's to Master's" and '... to Master of ...' entries are combined. Dietetics (held as a duplicate of its 4+1 sibling), International Business (ICP) and the online Geographic Information Science degree (its own entry, page and curriculum; counted and recorded as its own program after independent review) promoted. |

Reader and rule changes (tests and mutants for each):
- `pipeline/extractors/catalog.py program_name`: a dashed name is kept when the page's first heading prints it (bachelor's degree before the dash, plain field after); only JHU's 8 pages change across 71 stored runs.
- `programs/extract.py edition_degrees`; `programs/promote.py` keymap never maps a split degree onto its page's combined record.
- `programs/catalog_counts.py`: combined spelled-out and "Bachelor's to Master's" entries; 'Requirements for a Bachelor's Degree' and 'Double Degree Program'; 'Bachelor of X in Y (AWARD)'; `track_of_listed`; track pages under a listed degree's page only with the same award (review: TAMU's 'Chemistry - BS, ... Track' pages sit under 'Chemistry - BA'); a delivery or population qualifier doesn't block a page's own record; on-file recount credits each keyed record on a two-degree page. Replay of 24 schools' counts (main vs branch): only CSU Pueblo, SLU and UT Arlington change, each by excluding combined bachelor's-to-master's entries.
- **Pending owner decision:** JHU's verified 'Bachelor of Music Degree (BM)' record is the common-requirements page for every BM major, not a program of its own (the hub logic used for the BM in Performance); correcting it would leave JHU at 74/74.

**Stale recorded counts (not changed).** Recounts under the current rules disagree sharply with the recorded hand counts for Columbus State (21/68 vs 35/39), Montana (54/134 vs 67/78), Saint Mary's (0/80 vs 55/79) and CSU Pueblo (33/101 vs 34/49): those schools list concentrations or tracks without a plain degree line, which is the emphasis-grouping rule still to agree with Deep Dive (#153). Status uses the smaller of records and listed, so none is inflated; none is covered.

## Database contracts (Research as schema owner, #218)

Hosted stays held (`.operations/supabase-live-hold.json` `hold: true`); every migration below is merged or reviewed code only, unapplied on hosted.
- **Merged:** #243 role rules (C1 exam plan/interests need the linked student or a set-goals guardian; C6 saved-school removal; C7 recipient emails by RPC), `20261022010000`. #246 C3 cost `components` / `living_arrangements` through import and `compare_institutions`, `20261022040000`. #245 CR-24 rights gate and the generated-question rule (a `generated` item needs a `human:` review to be served), `20261022030000`.
- **Draft:** #248 CR-23 part 1 (reserved assessment pool, `benchmark_questions`, repeats/comparable), `20261022050000`. Reviewed; waiting for Design's client commits (LiveSource and seed) so `local-backend` passes.
- **Next:** CR-23 part 2 (`seen_before` on practice items, first-answer estimates); A1–A3 (CR-26, CR-27, CR-22) from Design's reference SQL; B3 CR-25; deletion/export procedure.

## Tennessee pilot

- **#191/#218 C4:** the undated credit tables are listed with recommended statuses on #191 (2026-10-21): UTK's six admissions-page tables (187 rows, verified) rest on a page without a year label and should be partially_verified; UTC and MTSU stay partially_verified. Downgrading UTK needs the owner's approval; nothing changed.
- **#193:** MTSU's catalog home loads, but its program list, academic maps and program pages are still behind a bot challenge (not evaded); no 2026-27 B.B.A. plan.

## Completed in batch 6 (research/batch-06)

| Institution | Run | Result |
|---|---|---|
| UT Dallas | TX/2026-10-21-u01 | 51/69, partial: first count. The 2026 edition's program list (catalog.utdallas.edu/2026/undergraduate/programs) is configured. Most degrees are printed twice ('Bachelor of Science in X (120 semester credit hours)' and 'X (BS)'): one program. '(Double Major)' entries are not counted. 'BA in X - Y' / 'BS in X - Y' (concentrations, Education certification focuses) are options of the listed degree. Where one page is linked as both the BA and the BS of a field (Biology, Chemistry, Economics, Education, International Political Economy, Interdisciplinary Studies, Mathematics, Physics) each award is a listed program; UT Dallas records such as 'Biology (BA, BS)' name two degrees in one record and credit neither entry (the name matches no whole-degree form, and a page with two entries is not credited through its single record); reproducing the count needs the lists re-read with the current reader. Corrected after independent review on #227 (the first count, 59/64, missed the BS links). Splitting those records needs a reader for pages printing two awards. |
| Pitt Greensburg | PA/2026-10-07-cat (re-extracted) | 32/32, **covered**. Four Acalog program pages whose requirement groups are not read now give the program record (static_program/v1). |
| Pitt Johnstown | PA/2026-10-07-cat (re-extracted) | 43/48, partial (+2). 'Pre-K - 12 Education, BS' is cut at its ' - ' by the shared title reader (left as is: changing it would rename existing Acalog records). |
| CU Denver | CO/2026-10-06-cat | 75/86, partial (+3: Law Studies BA, General Business BS, Economics/Mathematics dual degree). The 2026-10-06 entry's 75 predated the removal of rural-partnership variant records (72 were left); corrected. |
| Colorado State | CO/2026-10-08-c02 | 68/83, partial: first count, from the Programs A-Z table (`catalog_counts.table_entries`). Not recorded: majors whose pages are concentration pages only (Computer Science, Data Science, Theatre and others) and four dual degrees. |
| SNHU, Lone Star | NH, TX /2026-10-21-k02 | Queued `robots_disallowed`: rendered Kuali catalogs; their catalog feeds are kept, but the program list API is disallowed by robots.txt. SNHU's catalog is a term catalog ('University Catalog - Fall 2026'). |
| Michigan State | discovery | Queued `no_year_label`: the Academic Programs pages print no catalog year. |
| ASU | discovery | Queued `layout_not_readable`: degree pages print no year; their 2026 curriculum checksheets do, but are reached only through degree pages. |
| Indiana | IN/2026-10-21-c02 | Queued `no_year_label`: the College bulletin's program pages print no year (other school bulletins not configured). |
| UW, UGA, FSU, UCF | discovery | Queued: UW no year label; UGA and FSU JavaScript program lists; UCF's landing page still prints only 2025-26. |

Reader changes (each with tests and mutants; full program mutation check 309/309 killed before the main merge):
- `programs/catalog_counts.py`: `table_entries` (a Programs A-Z table count); `whole_degree` (one degree in four whole-name forms is one program); credit hours are not part of a name; '(Double Major)' not counted.
- `programs/extract.py` list reader: one page linked under two awards of the same field is two listed entries (before, the second link was dropped); credit hours are stripped from list lines (`list_line`), so autoreview and counts read 'Bachelor of Arts in X (120 semester credit hours)' the same way.
- `programs/extract.py`: `AWARD_IN_DASH_OPTION_ENTRY` ('BA in X - Y', an option only where the plain degree is listed; across all local lists only UT Dallas has such entries); 'BA in X' is a degree line; Acalog pages without read requirement groups give the program record (176 pages across 149 local runs: Union 158, Greensburg 12, Johnstown 6; only the six Pitt records are promoted).

**Count side effect (review on #227).** `whole_degree` merges 'Bachelor of Arts in Psychology' with 'Psychology, BA' and the same for Criminal Justice Studies in SF State's list, so a recount would read 117 listed rather than the recorded 118; the recorded entry is not recounted here (the error is conservative and SF State stays covered).

**Integrity note.** JHU's 'Five-Year BM/MM Program' is a verified bachelor's record although it is a combined bachelor's/master's program (the Roosevelt pattern); correcting it needs the owner's approval. Four catalog entries record more verified listed programs than the school has verified records (Columbus State 35 vs 26, Montana 67 vs 55, Saint Mary's 55 vs 54, CSU Pueblo 34 vs 33), because records were consolidated after the counts. Status already uses the smaller figure, so no coverage number is inflated; the entries should be recounted.

## Completed in batch 5 (research/batch-05, merged as #224)

**Integrity corrections (owner-approved 2026-10-21).** Each record keeps its evidence and requirement rows, is `unverified` with a `verification_correction_reason`, has the correction appended to its notes, and is listed in `supabase/corrections.json` with the owner's instruction quoted.
- Roosevelt: 'Digital Marketing, Advertising and Public Relations, BA to Marketing Communications, MSIMC' and 'Health Science Administration, BA/MPA Public Administration' are accelerated bachelor's-to-master's pathways (stored pages filed under 'Accelerated'); both bachelor's degrees are recorded separately. 74/79, still covered.
- SF State: 'Ethnic Studies, BA' and 'Criminal Justice Studies, BA' took their names from list lines that link the extended-learning BA pages; the pages cited are department overviews. 108/118, still covered.
- `programs/status.py`: `requirement_groups` now counts only groups of verified bachelor's programs (47 of 14,128 verified major groups belonged to associate degrees or the removed pathways; no school's dimension changed).

| Institution | Run | Result |
|---|---|---|
| ODU | VA/2026-10-06-cl (re-extracted) | 180/186, **covered**. 25 majors from pages titled 'X with a Major in Y (BSBA)' (also BSET, BSHS, BSPH, BSCS, BSDH, BSMLS) are now read. Seven programs reviewed 2026-10-08 keep their records. Not recorded: Chemistry Pre-Med (page not fetched), Cybersecurity AI (title prints no award), Music Sound Recording Technology emphasis, two Nursing BSN tracks (department-section records collide), HSA (Professional) BSPH (held as a name variant of the HSA BSPH program, '(Professional)' qualifier; listed separately, so counted and unrecorded). The re-extraction also added verified requirement rows for about 12 programs already on file (ODU: 96 to 148 requirement groups). The count is reproducible with `python3 -m programs.catalog_counts --run programs/runs/VA/2026-10-06-cl --on-file odu ...`. |
| UTC (TN pilot, #191) | pipeline TN/2026-10-21 | IB table re-read: level and printed scores in `minimum_score` ('HL 5,6, OR 7'), still partially verified (no year printed). CR-17 billing basis answered on #191 from the FY 2026-2027 bursar fee schedule (by credit hour to 11 hours, one '12+' row; per-credit differential fees). AP/CLEP/IB pages and renewable awards re-read: still no printed year. |

Reader changes (each with tests and mutants): `pipeline/extractors/catalog.py` (a parenthesized undotted award ends a bachelor's name), `programs/catalog_counts.py` (list rows that run the award on to filter labels; 'BS-MBA' combined; NROTC), `pipeline/extractors/credit.py` (an IB 'Levels Offered' column is not the score column).

**Near-tier recounts not adopted.** Recounting CU Denver, JHU, ESU, YSU, Ashland, Johnstown, La Salle and Greensburg under `catalog_counts` gave lower, less accurate counts than their reviewed entries: those lists print tracks as 'Base - X Track, BS', rural-partnership variants, spelled-out 'Bachelor of Arts/Master of Arts' combined entries and Peabody's instrument curricula. The reviewed entries stand. ESU's missing entries are Kuali pages that print no year; JHU's are the BM in Performance instrument curricula (all titled 'Bachelor of Music in Performance').

**Catalog discovery (diagnose runs `program-run/*-diag-2026-10-21`, search-surfaced URLs only):**
- SNHU: www.snhu.edu/admission/academic-catalogs embeds a Kuali catalog (snhu.kuali.co, catalogId 69e917a2592741290eff3c61). Configured as a rendered Kuali catalog; run `program-run/nh-k01-2026-10-21` keeps the page's own feed.
- Lone Star: www.lonestar.edu/catalog/ is a JavaScript catalog (hash routes); the 2019-20 PDF configuration is superseded. Run `program-run/tx-k01-2026-10-21`.
- ASU: degrees.asu.edu/curriculum lists every bachelor's plan (/bachelors/major/ASU00/<code>) with its latest major map year ('2026 - 2027'). Round 2 (`program-run/az-diag2-2026-10-21`) fetches a major page and its map.
- Michigan State: reg.msu.edu Academic Programs links 'Undergraduate Degrees' (Programs.aspx?PType=UGRD); fee sections print '2026-27'. Round 2 fetches the degree list.
- Indiana: separate 2026-2027 school bulletins on three hosts; queued `layout_not_readable` with every bulletin URL.
- Ohio State: no current catalog surfaced; cse.osu.edu answered 403. Cincinnati: only a 2025-2026 program catalog PDF (queued `not_published`).

## Completed in batch 4 (research/batch-04, merged as #215)

| Institution | Run | Result |
|---|---|---|
| Roosevelt | IL/2026-10-08-e01 | 74/79, covered again. The re-run read the undotted-award programs. The two combined BA/MPA and BA-to-MSIMC records from pipeline run IL/2026-10-05 were corrected in batch 5. |
| UT Dallas | TX/2026-10-08-b02 (re-extracted) | 64 verified records; no list count. New `edition_year_from_home` / `edition_program/v1`: pages print only the edition name '2026 Undergraduate Catalog', so the year is quoted from the edition home page. All 87 candidates were checked; double majors are held. Not yet recorded: Mechanical Engineering BS (heading too deep) and Visual and Performing Arts BA (concentration pages only); the seven Education certification focuses are two degrees. |

## Completed in batch 3 (research/batch-03, merged as #214)

| Institution | Run | Result |
|---|---|---|
| Colorado State | CO/2026-10-08-c02 | 68 verified records; no completeness count yet. New reader `award_link_major/v1` reads 'Major in X' pages that the Programs A-Z degree column links as 'B.A.' / 'B.S.'; all 60 first-extraction records were checked against the table rows. The table links concentrations and dual degrees by award only, so the count waits for a reader of its program column (queued). |
| SF State | recount of CA/2026-10-07-cat | 108/118, covered. Options of a listed degree are not counted. Nursing (Accelerated-Prelicensure) is no longer credited through another program's record. No record changed. |
| Roosevelt | recount of IL/2026-10-07-cat | 56/79, **no longer covered**. 18 undotted-award entries (BSBA, BAE, BMA, BSHTM, BAOL) had been left out of the 10-07 count. A re-run is in flight. |
| UTRGV | TX/2026-10-08-d03 | Queued `no_year_label`: the SmartCatalog pages print no catalog year. |

**Recount check.** Every covered school whose entry follows the `catalog_counts` format was recounted from stored runs with the current readers. All stay at or above 90% except Roosevelt. Recount decisions (`*-recount.json`) approve nothing. They map approvals that the current reader re-identifies on the same page, for counting only.

## Completed in batch 2 (research/batch-02, merged as #213)

| Institution | Run | Result |
|---|---|---|
| Oklahoma State | OK/2026-10-08-r2 | 170/184, covered. Re-run with a 900-page cap, superseding b01. Undotted awards (BSBA, BSCH, BSET, BPS, ...) are read in list entries and page names. |
| Missouri | MO/2026-10-08-r2 | 97/100, covered. Re-run with an 800-page cap, superseding b02. Pages named 'BSAcc in Accountancy' and 'BHS in ...' are read. |
| UIC | IL/2026-10-08-b04 | 95/128, partial. The walk starts at /ucat/colleges-depts/. |
| BYU | UT/2026-10-08-b03 | 118/169, partial (secondary majors listed but not counted). New reader `kuali_page/v1` for pages titled '<code> Program'; the year comes from the site header 'Undergraduate Catalog' / 'BYU' / '2026-2027'. |

Blockers queued in batch 2:
- **bot challenge:** Pitt; State College of Florida.
- **robots.txt unreachable:** Weber; Ole Miss.
- **Coursedog 401, no year label:** Ensign; K-State.
- **layout not readable:**
  - UWM; SHSU.
  - Colorado State and UNL: major pages print no award in the heading.
  - Utah: titles print only the field.

## Completed in batch 1 (research/batch-01, merged as #211)

| Institution | Run | Result |
|---|---|---|
| Oklahoma State | OK/2026-10-08-b01 | 127/184, partial. The 2026-2027 catalog had been misread as 2025-26 because of the print link 'Full 2025-2026 Catalog'. Options printed as 'Major: Option, AWARD' beside their major are held and not counted. The run hit the 450-page cap before reaching most BSBA/BSET/engineering pages; a re-run with a 900-page cap is in flight. |
| Missouri | MO/2026-10-08-b02 | 86/99, partial. Award-only entries ('BA', 'BS*', 'BSAcc') are identified by their own page. The entries whose awards the list reader missed were never crawled; a re-run with an 800-page cap is in flight. |
| UTEP | TX/2026-10-08-b04 | 83/87, covered. List cards run the name or award on to category labels. |
| Georgia Tech | GA/2026-10-08-b03 | 41/42, covered. Thread and concentration pages are variants of the degree's page. Electrical Engineering is held because of a misspelled thread URL (queued). |
| VCU | VA/2026-10-08-b02 | 120 verified records (#209's 57 kept as on main, b02 adds 63); 120/151 listed (A-Z list /azprograms/, fetched under robots; #210's robots_disallowed entry for /azindex/ is superseded). Concentration lines with no degree line are read as the degree. |
| UTSA | TX/2026-10-08-b03 | 82 degree sections. The '2026-28 Undergraduate Catalog' period label is kept. There is no program list page, so no completeness count (queued). |

Reader and checker changes in this batch each come with tests and mutants: `programs/extract.py`, `programs/catalog_counts.py`, `programs/autoreview.py`, `pipeline/extractors/catalog.py` and `pipeline/extractors/common.py`.

## Unresolved (queued in programs/queue; the reason is in each entry)

- **bot_challenge (never evaded):** LSU, UKY, plus the earlier set (Purdue, Kennesaw, Dallas College, HCC, Michigan, Texas Tech, UNT and others).
- **fetch_failed (robots.txt unreachable):** UConn, Montclair, UH, CSU Fullerton (also Virginia Tech, earlier).
- **no_year_label (a year is never inferred):**
  - Coursedog catalogs whose API answered 401: Arizona, UCSB, Illinois State, USU, FIU. CSUN: its pages print no year label.
  - Alabama: the only label printed is the print-menu link 'Download 2026-27 Undergraduate PDF'. This is a shared reader request.
- **layout_not_readable:** Utah and UCR (Deep Dive's readers on #153); Indiana (separate school bulletins). Deep Dive's #226 covered UWM (133/133) and UNL (116/124) and added the SHSU header-year rule.
- **not_published:** Cincinnati (only a 2025-2026 program catalog PDF).
- **Stale configured catalogs (find the 2026-27 catalog by web search before running):**
  - CSULB (2015-16 PDF)
  - UNM (2009-10 PDF)
  - Modesto JC (2020-21 PDF)
  - St. Petersburg College (2025-26 PDF)
- **Pending owner decision:** downgrading UTK's six undated credit tables (187 rows) to partially_verified; UTK dual_enrollment depends on its catalog page's year label (#191 2026-10-21, #218 C4).
- **TN pilot (#191):** UTC AP/CLEP/IB tables and renewable awards print no year (partially verified); CR-19 applicability not published; Entrepreneurship and Economics: International Public Policy plan rows are truncated in the source PDF text itself.

## Known reader limits

- `UNDOTTED_LIST_AWARD` reads UMD's 'SDSB - Social Data Science, BSOS' (a college code) as a bachelor's entry; review such entries by hand.

## In flight

None in this session (no program runs pending). Weekly TN reference-data pipeline runs remain unreviewed (reference-data breadth).

## Next prioritized batch

1. **Shared rule with Deep Dive (#153):** degrees listed only through emphases or tracks (BYU; Columbus State, Montana, Saint Mary's, CSU Pueblo recounts above; OSU, SF State, UVU, UNH).
2. **Readers kept by Research:** Colorado State majors whose catalog pages are concentration pages only (11 not recorded; the A-Z table row is the only listing); ASU 2026 checksheets; Alabama print-link label; UTSA (no degree list).
3. **Near tier:** ESU (Kuali pages without a year), Pitt Johnstown (Pre-K - 12 Education title), CU Denver (75/86).
4. **Configured tier:** UT Austin and Texas State (coordinate with Deep Dive), Penn State, Illinois, UCI, UC Davis, Arkansas.
5. **Unconfigured tier:** Rutgers, UCSD, Minnesota (Coursedog), NAU, UMass, Oklahoma, Iowa, JMU, Grand Valley.
6. **Consistency question:** CU Denver's 'Economics BA/Mathematics BS - Dual Degree' is a verified program, while UT Dallas double majors, JHU's double degree and Colorado State's 'Dual Degree B.S.' entries are not counted; agree one rule.

## How to resume

1. `git fetch origin`. Read this file, then run `python3 scripts/research_priority.py --batch 25`.
2. Process the in-flight runs:
   - Fetch: `git fetch origin '+refs/heads/program-run/*:refs/remotes/origin/program-run/*'`.
   - Extract with `python -m programs extract`, then `python -m programs.verify`, then `python -m programs autoreview`.
   - Review the auto decision against the official program list.
   - Write the reviewed decision, deduplicated, with its catalog entries from `python3 -m programs.catalog_counts`.
   - Promote, then run `python3 scripts/retain_evidence.py --push`.
   - Regenerate `python -m programs status`, `scripts/update_coverage.py` and `scripts/research_priority.py`.
3. Queue every blocker in `programs/queue/<ST>.json` with its reason, detail and next action, then move to the next institution.
4. Open the batch PR, get an independent review, merge main, re-run checks, and merge on green CI. Update this file in the same PR.

Hosted imports and deployments stay on hold while Supabase is paused.
