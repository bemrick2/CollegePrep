# Migration history

The repository files in `supabase/migrations` use the **same version numbers** that the live CollegePrep project (`butlklkzafvklwasbynr`) recorded in `supabase_migrations.schema_migrations`. `supabase/migration_history.json` lists every applied migration with its live version and a normalized content hash. The hash ignores line endings and trailing whitespace.

## 2026-10-02 reconciliation

Earlier migrations were applied through the Supabase connector. The connector stamps each migration with the time it was applied, so the live versions differed from the repository filenames. A `supabase db push` would therefore have treated all seven as new and tried to apply them again.

The live statements were compared with the repository files after normalizing line endings and trailing whitespace. All seven matched exactly, so the files were renamed to the live versions with no content changes. Nothing in the live database was changed, dropped or re-run.

| Previous repository file | Live version (current filename) |
|---|---|
| 20261001180000_initial_collegeprep_schema | 20261002105521 |
| 20261002085527_protect_reference_data_and_appeal_gate | 20261002105559 |
| 20261002105640_normalized_reference_import | 20261002110216 |
| 20261002113143_preserve_unknown_award_flags | 20261002113323 |
| 20261002130818_program_catalog_imports | 20261002131440 |
| 20261002131409_school_comparison_api | 20261002132345 |
| 20261002150000_degree_transfer_import_domains | 20261002134049 |
| (not in repository) reviewed_policy_domains | 20261002165225 |

A live-only migration, `20261002165225_reviewed_policy_domains`, was found during the same check. It was applied directly to the live project at 16:52 UTC on 2026-10-02 and was not in any repository branch. It adds `credit_equivalencies.is_current`, a null-safe unique key, an `is_current` filter on public equivalency reads, and the matching `compare_institutions` change. It was captured into the repository exactly as applied; only CRLF line endings were converted. Its normalized digest matches live.

Applied migration files are left exactly as they were applied, and their contents must not change. For example, `20261002134049_degree_transfer_import_domains.sql` still mentions its predecessor's old filename in a comment.

## Guards

- `python scripts/check_migration_history.py` runs in CI. It fails when:
  - a filename does not follow the `<14-digit version>_<name>.sql` pattern
  - two files share a version
  - an applied migration is renamed or edited
  - a migration name appears under two versions
- `python scripts/check_migration_history.py --live` runs at the start of every live import, using `DATABASE_URL`. It fails when:
  - a live migration has no local file
  - a name is recorded live under a different version than the local file
  - live and local content differ
  - a pending local migration is older than the newest live one

  Newer local migrations that have not been applied yet are reported as pending.

## Adding a migration

1. Create `supabase/migrations/<UTC timestamp>_<name>.sql`, newer than every existing file. Do not put `begin`/`commit` in it: the deploy wraps each file in one transaction.
2. Merge it to `main` after CI passes. `.github/workflows/deploy-migrations.yml` then runs `scripts/apply_migrations.py`, which:
   - re-runs the offline and live history checks and refuses on any drift
   - applies each pending file in one transaction together with its `supabase_migrations.schema_migrations` row (its own version, the whole file stored as one statement, as the connector did)
   - re-checks that live history now matches the repository
   A failed file is rolled back completely, including its history row, and nothing after it runs. The live import runs again after a successful deploy.
3. Record the now-live migration in `supabase/migration_history.json` (version, name and normalized MD5: the file text with `\r` removed and trailing newlines and spaces stripped). From then on CI treats the file as frozen.

Applying through the Supabase connector or SQL editor is still possible, but then the local file must be renamed to the version the connector recorded before merging. `supabase db push` is not used: it stores statements split, so its content hash would not match this repository's check.

To run the deploy by hand: `DATABASE_URL=... python scripts/apply_migrations.py --dry-run`, then without `--dry-run`.

## Two recording formats
`20261002223000_state_policies_dual_enrollment` was applied live by Supabase's own migration tooling
(most likely the Supabase GitHub integration on merge to `main`) a few minutes before the deploy
workflow, which was waiting on the shared `live-supabase` lock. That tooling stores one array element
per statement; `scripts/apply_migrations.py` stores the whole file as one element. The live check
therefore accepts either the whole-file md5 or the canonical md5 (comments, semicolons and whitespace
ignored), and the schema change itself is identical. If both deployers stay enabled, whichever runs
first records the migration and the other finds nothing pending.
