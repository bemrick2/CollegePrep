# Program and transfer data contract

The importer supports `academic_programs`, `transfer_policies`, and
`degree_requirements` records. Store files under an institution's matching domain
directory, with a wrapper declaring `institution_key`, `academic_year`, and
`records`. Each record needs an official HTTPS `source_url`,
`verification_status`, and `last_verified_at`. Never fill missing facts with
defaults. An unknown numeric value is omitted or null.

**Catalog periods.** A program's `catalog_year` is the catalog label exactly as printed. Most catalogs cover one
academic year (`"2026-2027"`); some cover a period (`"2026-2028 Catalog"`, Cal Poly). A period label is never
relabelled to one year: records read from it keep `catalog_year: "2026-2028"`, the printed line stays in the record's
evidence, and the wrapper's `academic_year` is the year of the period the record is read for (`"2026-27"` now,
`"2027-28"` when that year is built from the same catalog). `program_catalogs.catalog_year_label` is likewise the
printed period.

Programs require `program_key` and `program_name`. Keep `program_key` stable
when the display name changes. Optional fields are `cip_code`,
`credential_level`, `delivery_mode`, `catalog_year`, `total_credits`,
`program_url`, and `active`. Do not assume a program remains active.

Requirements require `program_key`, `requirement_key`, and `requirement_kind`.
Kinds are `total_credits`, `general_education`, `major`, `minor`, `residency`,
`gpa`, `other`, or `program_plan` (a whole catalog plan held in `rule_details`). Optional `minimum_credits` and `minimum_gpa` hold documented
numbers; `rule_details` is an object for course lists and conditional rules.
The referenced program must exist at the same institution and academic year;
the entire import fails otherwise. Requirements for separate programs may use
the same requirement key.

Transfer records are unique per institution and academic year. Optional fields
are `policy_url`, `min_grade`, `max_transfer_credits`, `max_transfer_percent`,
`residency_requirement_credits`, `articulation_url`, `summary`, and `notes`; the
full reviewed payload is kept in `transfer_policies.policy_details`. The source URL
is used when a separate policy URL is omitted. This schema records general
policy; it does not promise individual course acceptance or degree applicability.

Programs import before requirements, including across batch boundaries. Annual
records remain separate. Accepted same-year changes retain the previous payload
in the private revision ledger. Rollback-only synthetic integration tests check
year separation, missing-parent rejection, unknown values, evidence downgrade
rejection, and repeat-import idempotence. These fixtures do not count as coverage.

Controlled values and required fields for every domain live in
`backend/catalog.py` and must match the latest migration's check constraints;
`scripts/validate_data.py` and the importer both enforce them, and
`tests/test_import_contract.py` fails if they drift.

## Structured requirement groups (`requirement_group/v1`)

Each `degree_requirements` row is one requirement group of one program for one catalog year. A program usually has several rows: general education, major core, choose-N groups, electives, concentrations, totals and rules. The recommended semester sequence is a separate `program_plan` row. Each row's `rule_details` must declare the following:

| key | required | meaning |
| --- | --- | --- |
| `schema` | yes | `"requirement_group/v1"` |
| `catalog_year` | yes | Catalog year exactly as printed, e.g. `"2026-2027"`. A catalog published for a multi-year period keeps its printed period (`"2026-2028"`, Cal Poly); the file's `academic_year` must be a year inside the period. |
| `group_type` | yes | One of the group types below. |
| `category` | yes | One of the categories below. |
| `choose_count` | if `group_type` = `choose_courses` | The number of courses to choose. |
| `choose_credits` | if `group_type` = `choose_credits` | The number of credit hours to choose. |
| `courses` | when the catalog lists courses | A list of course items. |
| `course_rules` | optional | Pool rules exactly as printed, e.g. "Any 3XX/4XX COSC course not otherwise used". |
| `concentration` | if `category` = `concentration` | The concentration name. |
| `parent_requirement_key` | optional | The requirement group this group belongs to. |
| `terms` | if `group_type` = `sequence` | Ordered terms: `{"term_index": 1, "label": "Year 1 Fall", "credit_hours": "15", "items": [course items or text]}`. |
| `source_section` | optional | The catalog heading the group was read from. |

Group types:

- `all_required`: every listed course is required.
- `choose_courses`: choose `choose_count` courses from the list.
- `choose_credits`: choose `choose_credits` hours from the list or rules.
- `elective_pool`: hours from a pool defined by `course_rules`.
- `credit_total`: a program or area hour total, carried in `minimum_credits`.
- `gpa_rule`: a minimum GPA, carried in `minimum_gpa` and stated in `rule_text`.
- `grade_rule`: a minimum grade in named courses, stated in `rule_text`.
- `residency_rule`: hours that must be taken at the institution.
- `sequence`: a recommended term-by-term plan. Use this only with `requirement_kind` = `program_plan`.

Categories:

- `general_education`: the institution's general-education core.
- `major_core`: courses every student in the major takes.
- `major_elective`: restricted electives within the major.
- `concentration`: a named concentration, track or emphasis.
- `supporting_coursework`: required courses outside the major department, such as math or science.
- `free_elective`: unrestricted hours.
- `university_requirement`: rules for every degree.
- `program_total`: the program's total hours.
- `recommended_sequence`: the semester plan.
- `minor`: a minor.
- `other`: anything else.

**Course items.** A course item is `{"code": "COSC 102", "title": "...", "credits": 4}`. `credits` may be a string such as `"1-3"` when the catalog prints a range. Optional `prerequisites_text` and `corequisites_text` copy the catalog wording verbatim. A printed "X or Y" choice is `{"any_of": [item, item]}`.

**Rules.**

- Record only what the catalog prints. Never infer prerequisites, course placement or credit totals.
- Leave a field out when the catalog does not state it.
- Keep a plain-language `rule_text` when a rule does not fit the fields above.
- Map `requirement_kind` as follows:
  - `general_education` → `general_education`
  - `major_core`, `major_elective`, `concentration`, `supporting_coursework` → `major`
  - `program_total` → `total_credits`
  - `gpa_rule` → `gpa`
  - `residency_rule` → `residency`
  - `sequence` → `program_plan`
  - anything else → `other`

`scripts/validate_data.py` enforces this structure for every `degree_requirements` row.

## Institution keys for curated schools

A school already present in the national IPEDS snapshot keeps its existing `ipeds-<unitid>` key. Curated files for it live in a readable folder, such as `data/institutions/utc/`, but every wrapper declares the national key, such as `"institution_key": "ipeds-221740"`. The folder name is only a label; the record keys come from the wrapper.

These schools get no second `institution.json`. A second one would collide with the IPEDS identity on `unitid`, and renaming a live identity key is a separate decision that has not been made. UT Knoxville (`utk`) predates the national snapshot and keeps its curated key.

| Folder | Key | School |
| --- | --- | --- |
| utc | ipeds-221740 | The University of Tennessee at Chattanooga |
| memphis | ipeds-220862 | University of Memphis |
| mtsu | ipeds-220978 | Middle Tennessee State University |
| tntech | ipeds-221847 | Tennessee Technological University |
| etsu | ipeds-220075 | East Tennessee State University |
| belmont | ipeds-219709 | Belmont University |
| vanderbilt | ipeds-221999 | Vanderbilt University |

## CR-14 program-depth fields (migration `20261005150000_program_depth_cr14`)

Optional on `academic_programs`; null means not verified. Each carries its own evidence because admission rules are
usually published on a different page than the catalog program page.

| field | shape | rule |
| --- | --- | --- |
| `cip_code` + `cip_source_url` | `"14.1901"`, https URL | Only from an official source that prints the code for this program (state program inventory, institutional CIP list). Never matched by name. |
| `admission_type` + `admission_details` | `direct` / `pre_major` / `open`; `{quote, source_url, source_sha256, retrieved_at, criteria_text?, gpa_min?, paths?}` | See programs/README.md. A selective first-year path beside a standard path is listed in `paths`; the value is the standard path. |
| `internal_transfer` | `{restricted, quote, source_url, criteria_text?, gpa_min?}` | Published limits on changing into the major after enrolling. |
| `college` | text | As printed. |

`program_catalogs` (one per institution and academic year): `catalog_url`, `catalog_year_label`,
`listed_bachelor_programs`, `programs_complete`, `completeness_basis`, `listed_program_keys` (repository only),
`undeclared_policy {allowed, quote, source_url, declare_by_text?}`. `programs_complete=true` requires every listed key
to have a verified program record for the same year (`backend/program_fields.py`). Read API: `program_catalog_status(keys, year)`.

`awards.program_keys` / `awards.cip_codes`: set only when the institution itself ties the award to the program or
field; `major_requirement` must quote that tie.
