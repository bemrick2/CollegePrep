# Program and transfer data contract

The importer supports `academic_programs`, `transfer_policies`, and
`degree_requirements` records. Store files under an institution's matching domain
directory, with a wrapper declaring `institution_key`, `academic_year`, and
`records`. Each record needs an official HTTPS `source_url`,
`verification_status`, and `last_verified_at`. Never fill missing facts with
defaults. An unknown numeric value is omitted or null.

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
