import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import check_migration_history as c

LIVE_2026_10_02 = [  # supabase_migrations.schema_migrations, verified 2026-10-02
    ('20261002105521', 'initial_collegeprep_schema', '16dfa863d7d95ae0246d948e2209523c'),
    ('20261002105559', 'protect_reference_data_and_appeal_gate', 'e462d1a39de9d803eb6e621e5641f505'),
    ('20261002110216', 'normalized_reference_import', 'cc75824f6923487494371ec6632821b2'),
    ('20261002113323', 'preserve_unknown_award_flags', '13d607dfd42810e2545f9c346e4714a2'),
    ('20261002131440', 'program_catalog_imports', '2a1f69ba3d36a25dd3f5d8ca85e5af6b'),
    ('20261002132345', 'school_comparison_api', 'ef8209eeb29cc0d8183d90f1b6568d0a'),
    ('20261002134049', 'degree_transfer_import_domains', 'ba57c2f07bbbfd3892c92b6a391e13a2'),
    ('20261002165225', 'reviewed_policy_domains', 'f941b44f4cca76ca37f0d79c5555f745'),
    ('20261002183112', 'household_practice_progress', 'e111a09c6ff53c7a33f574a0b86aca00'),  # deployed by workflow
    ('20261002202613', 'practice_foreign_key_indexes', '38ca7c416ba894a72276f9e700231d42'),  # deployed by workflow
    ('20261002213423', 'state_policies', 'ebd208310420777cd0c8f270c261dbd7'),  # deployed by workflow
    # Applied by Supabase's own migration tooling before the workflow (one element per statement), so the
    # whole-file md5 differs; the canonical md5 (comments/semicolons/whitespace ignored) was checked live.
    ('20261002223000', 'state_policies_dual_enrollment', '129783e0dfa2800e0ade059d24c11d34', '1122fa88a77be081b76fbcfadd28bae0'),
]


class MigrationHistoryTests(unittest.TestCase):
    def setUp(self):
        self.local, errors = c.local_migrations()
        self.assertEqual(errors, [])
        # Local migrations not yet applied live are expected to be reported as pending.
        live = {r[0] for r in LIVE_2026_10_02}
        self.unapplied = [v['file'] for k, v in sorted(self.local.items()) if k not in live]

    def test_repository_matches_recorded_live_history(self):
        self.assertEqual(c.offline_errors(self.local), [])
        self.assertEqual(c.live_errors(self.local, LIVE_2026_10_02), ([], self.unapplied))

    def test_name_recorded_under_other_version_is_caught(self):
        drifted = dict(self.local)
        entry = drifted.pop('20261002134049')
        drifted['20261002150000'] = {**entry, 'file': '20261002150000_degree_transfer_import_domains.sql'}
        errors, _ = c.live_errors(drifted, LIVE_2026_10_02)
        self.assertTrue(any('rename the file to the live version' in e for e in errors))

    def test_edited_applied_migration_is_caught(self):
        edited = {k: dict(v) for k, v in self.local.items()}
        edited['20261002110216']['md5'] = '0' * 32
        self.assertTrue(c.offline_errors(edited))
        self.assertTrue(c.live_errors(edited, LIVE_2026_10_02)[0])

    def test_new_migration_is_pending_but_backdated_one_fails(self):
        newer = dict(self.local)
        newer['20991231000000'] = {'name': 'future_change', 'file': '20991231000000_future_change.sql', 'md5': 'x'}
        self.assertEqual(c.live_errors(newer, LIVE_2026_10_02), ([], self.unapplied + ['20991231000000_future_change.sql']))
        older = dict(self.local)
        older['20261002000000'] = {'name': 'backdated', 'file': '20261002000000_backdated.sql', 'md5': 'x'}
        self.assertTrue(c.live_errors(older, LIVE_2026_10_02)[0])

    def test_statement_split_recording_matches_but_edits_do_not(self):
        text = "-- why\nalter table t drop constraint c;\nalter table t add constraint c check (x in ('a','b'));\n"
        split = "-- why\nalter table t drop constraint c\nalter table t add constraint c check (x in ('a','b'))"
        self.assertEqual(c.canonical_md5(text), c.canonical_md5(split))
        self.assertNotEqual(c.canonical_md5(text), c.canonical_md5(split.replace("'b'", "'z'")))
        local = {'20261002223000': {**self.local['20261002223000'], 'canonical_md5': '0' * 32}}
        errors, _ = c.live_errors(local, [LIVE_2026_10_02[-1]])
        self.assertTrue(any('content differs' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
