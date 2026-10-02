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

1. Create `supabase/migrations/<UTC timestamp>_<name>.sql`, newer than every existing file.
2. Apply it to live:
   - **Preferred:** `supabase db push`. The CLI records the file's own version.
   - **Connector or SQL editor:** read the version it recorded, then rename the local file to that version before merging.
3. Once it is live, record it in `supabase/migration_history.json`: the version, the name, and the normalized MD5 (the file text with `\r` removed and trailing newlines and spaces stripped). From then on CI treats the file as frozen.
4. Merge. The live import workflow re-checks the history before importing data.
