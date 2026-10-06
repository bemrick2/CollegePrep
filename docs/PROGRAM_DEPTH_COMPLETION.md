# Program & Degree Deep Dive: when a state is "deep-dive complete"

This is the production standard for the program-depth workstream (`programs/`). It measures each state from
committed files only, so anyone can reproduce it:

    python -m programs status            # writes docs/coverage/programs/STATUS.json and STATUS.md for every state the deep dive has worked
                                         # (a queue file or a promoted program_catalogs record)
    python -m programs status --check    # CI: fails when the queue is malformed or STATUS.json is stale

The numbers below live in `programs/status.py` (`COVERAGE_SHARE`, `CATALOG_SHARE`, `PLAN_SHARE`, `HIGH_VALUE`).
Changing one is a product decision, not a tuning knob. Make the change in the same PR as this document.

## Inputs

| Input | Owner | Used for |
|---|---|---|
| `pipeline/registry/<STATE>.json` | national pipeline | the state's in-scope institutions; `level == "four_year"` is the deep-dive scope |
| `data/national/ipeds/2023-24/<STATE>/admissions.csv` (`enrolled`) | national pipeline | weight of each school: first-time students who enrolled |
| `data/institutions/<folder>/{academic_programs,program_catalogs,degree_requirements}/<year>.json` | this workstream | promoted program-depth records (latest catalog year per school) |
| `programs/queue/<STATE>.json` | this workstream | every gap the pipeline could not close, with a reason and a next action |

The deep dive never creates institutions, costs, admissions statistics or credit policies. Those come from the
national dataset. A national-data defect found here is filed against the national pipeline (issue plus a
shared-pipeline fix), never patched in a parallel model.

## Per institution

Each in-scope four-year institution is measured on four dimensions.

| Dimension | Met when | Otherwise |
|---|---|---|
| **catalog** | a `program_catalogs` record exists and either `programs_complete` is true (every listed bachelor's program has a verified record, which the validator enforces) or verified bachelor's records are at least **90%** of the official `listed_bachelor_programs` | `queued` if the queue has a `catalog`, `catalog_count` or `institution` entry, else `open` |
| **degree_maps** | verified `program_plan` records cover at least **50%** of the verified bachelor's programs | `queued` with a `degree_maps` entry (e.g. `not_published`, `layout_not_readable`), else `open` |
| **requirement_groups** | at least one verified `major` requirement record (required vs choose groups) | `queued` / `open` |
| **admission_rules** | every high-value family the school offers (engineering, computer science, nursing, business) has at least one verified program with an official `admission_type` (direct / pre_major / open, with a verbatim quote) | `queued` with an `admission_rules` entry (e.g. `no_official_statement` after the pages were read), else `open` |

Institution status:

* `covered`: catalog met, and every other dimension is met or queued.
* `covered_open_items`: catalog met, but some dimension is `open` (unaccounted).
* `partial`: some program records exist (verified or partially verified), the catalog is not met, and every gap is queued.
* `partial_unqueued`: as above with an `open` dimension (unaccounted).
* `exception`: no records, but the queue says why (e.g. `bot_challenge`, `robots_disallowed`).
* `not_started`: no records and no queue entry (unaccounted).

## Per state

A state is **complete** only when all of these hold:

1. **Coverage:** `covered` institutions enrolled at least **80%** of the state's entering first-year students at in-scope
   four-year institutions (IPEDS 2023-24).
2. **Nothing silently omitted:** no institution is `not_started`, `partial_unqueued` or `covered_open_items`.
   Every gap is a queue entry.
3. **Queue is well-formed:** every entry names a registry institution, one of the known gaps and reasons, a `next_action`,
   and evidence (`evidence_url` or `detail`) unless the reason is `not_yet_researched`.
4. **Promoted records pass validation:** `scripts/validate_data.py` (CR-14 field rules, provenance, verbatim quotes,
   `programs_complete` integrity), `python -m programs audit --check` and the database import tests all pass.
   CI enforces this for every promoted record, so a state cannot be complete on failing data.

Otherwise the state is `in_progress`, or `not_started` when nothing has been done.

A queued `not_yet_researched` entry keeps a school accounted for but does **not** count toward the 80%. So a state
cannot be completed by queuing its large schools.

## What the rule deliberately does not do

* It never treats a missing program as "not offered". That claim needs `programs_complete` on a verified catalog.
* It never counts partially verified records (for example the Tennessee THEC inventory, which prints no academic year)
  toward catalog coverage.
* It never turns an unreadable or blocked source into a completed one. Blocked sources stay queued (`bot_challenge`),
  and a bot challenge is recorded, never evaded.

## Queue file format

```json
{"state": "OR", "entries": [
  {"institution_key": "ipeds-209807", "gap": "degree_maps", "reason": "not_published",
   "detail": "Program pages list requirements but no term-by-term plan", "evidence_url": "https://…",
   "next_action": "re-check at the 2027-28 catalog release"}
]}
```

`gap` is one of `catalog`, `catalog_count`, `degree_maps`, `requirement_groups`, `admission_rules`, `institution`.
`reason` is one of `bot_challenge`, `robots_disallowed`, `no_year_label`, `year_inconsistent`, `layout_not_readable`,
`not_published`, `no_official_statement`, `state_inventory_only`, `not_yet_researched`, `out_of_scope`.
