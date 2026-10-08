# Research checkpoint

This file is how a new Research session resumes the national program-research workstream without redoing finished work. It is updated with every batch PR.

- **Main at the last refresh:** `517dc1f6dbff5f066c17abf0267d903c6913332c` (merge of #209).
- **Branch carrying this checkpoint:** `research/batch-01`.
- **Ranking:** `docs/coverage/research_priority.json`, written by `python3 scripts/research_priority.py`. CI (validate-data) checks that it is current.

## Numbers

| | main `517dc1f` | research/batch-01 |
|---|---|---|
| Registered four-year institutions | 2,119 | 2,119 |
| Covered (docs/PROGRAM_DEPTH_COMPLETION.md) | 58 | 60 |
| Researched | 641 | 661 |
| Verified bachelor's program records | 9,256 | 9,738 |

All figures are counted from `docs/coverage/programs/STATUS.json` and from the `academic_programs` files with `verification_status == "verified"` and `credential_level == "bachelor"`.

## Completed in batch 1 (research/batch-01)

| Institution | Run | Result |
|---|---|---|
| Oklahoma State | OK/2026-10-08-b01 | 127/184, partial. The 2026-2027 catalog had been misread as 2025-26 because of the print link 'Full 2025-2026 Catalog'. Options printed as 'Major: Option, AWARD' beside their major are held and not counted. The run hit the 450-page cap before reaching most BSBA/BSET/engineering pages; a re-run with a 900-page cap is in flight. |
| Missouri | MO/2026-10-08-b02 | 86/99, partial. Award-only entries ('BA', 'BS*', 'BSAcc') are identified by their own page. The entries whose awards the list reader missed were never crawled; a re-run with an 800-page cap is in flight. |
| UTEP | TX/2026-10-08-b04 | 83/87, covered. List cards run the name or award on to category labels. |
| Georgia Tech | GA/2026-10-08-b03 | 41/42, covered. Thread and concentration pages are variants of the degree's page. Electrical Engineering is held because of a misspelled thread URL (queued). |
| VCU | VA/2026-10-08-b02 | 120 verified records (#209's 57 kept as on main, b02 adds 63); 120/151 listed. Concentration lines with no degree line are read as the degree. |
| UTSA | TX/2026-10-08-b03 | 82 degree sections. The '2026-28 Undergraduate Catalog' period label is kept. There is no program list page, so no completeness count (queued). |

Reader and checker changes in this batch each come with tests and mutants: `programs/extract.py`, `programs/catalog_counts.py`, `programs/autoreview.py`, `pipeline/extractors/catalog.py` and `pipeline/extractors/common.py`.

## Unresolved (queued in programs/queue; the reason is in each entry)

- **bot_challenge (never evaded):** LSU, UKY, plus the earlier set (Purdue, Kennesaw, Dallas College, HCC, Michigan, Texas Tech, UNT and others).
- **fetch_failed (robots.txt unreachable):** UConn, Montclair, UH, CSU Fullerton (also Virginia Tech, earlier).
- **no_year_label (a year is never inferred):**
  - Coursedog catalogs whose API answered 401: Arizona, UCSB, Illinois State, USU, FIU. CSUN: its pages print no year label.
  - Alabama: the only label printed is the print-menu link 'Download 2026-27 Undergraduate PDF'. This is a shared reader request.
  - UT Dallas: pages print the edition name '2026 Undergraduate Catalog', and the edition's home page prints '2026-2027 Undergraduate Catalog'. Reader work for the Research session: read the year from the edition home page and cite that page.
- **layout_not_readable:** UCR (its catalog PDF gives no program records).
- **Stale configured catalogs (find the 2026-27 catalog by web search before running):**
  - Lone Star (2019-20 PDF)
  - Cincinnati (2025-26 PDF)
  - CSULB (2015-16 PDF)
  - UNM (2009-10 PDF)
  - Modesto JC (2020-21 PDF)
  - St. Petersburg College (2025-26 PDF)
- **Pending owner decision:** the UTK downgrade of 7 records (#191).

## In flight (run branches pushed, not yet reviewed)

- `program-run/ok-r2-2026-10-08` and `program-run/mo-r2-2026-10-08`: Oklahoma State and Missouri re-runs with higher page caps. Undotted awards are now classified, so their business and engineering entries are counted.

- `program-run/ut-b03-2026-10-08`: BYU and Utah, reconfigured as Coursedog with a paged list.
- `program-run/il-b04-2026-10-08`: UIC; the walk starts at /ucat/colleges-depts/.
- Batch 2, `program-run/<st>-c01-2026-10-08`:
  - SHSU (TX)
  - Colorado State (CO)
  - UNL (NE)
  - Pitt (PA)
  - Weber and Ensign (UT)
  - The State College of Florida (FL)
  - K-State (KS)
  - UW-Milwaukee (WI)

## Next prioritized batch

From `research_priority.json`, excluding blocked institutions:

1. **Near tier** (catalog share 75-90%): Iowa State, VCU, SF State, ODU, CU Denver, JHU, ESU, YSU. Find which listed programs are unrecorded and why: held variants, unread pages, or a reader rule.
2. **Configured tier, largest first:**
   - Stale catalogs first: Lone Star, Cincinnati.
   - UT Austin 42% and Texas State 45%: Deep Dive has worked these; coordinate before re-running.
   - Penn State, Illinois, UCI, UC Davis, Arkansas: records exist but there is no list count. Configure each official list and compute the count.
3. **Unconfigured tier, largest first** (958 institutions): SNHU, ASU, Indiana, Michigan State, Ohio State, UCF, Rutgers, Washington, UCSD and others. Each needs its official catalog found by web search, using only search-surfaced URLs or links seen on stored official pages.

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
