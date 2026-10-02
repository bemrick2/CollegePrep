"""Guards that keep validated repository data loadable by the normalized Supabase importer."""
import json, re, tempfile, unittest
from pathlib import Path
from unittest import mock

import scripts.import_supabase as importer
from backend.catalog import ROOT, records, IMPORT_DOMAINS, CONTROLLED_VALUES, import_contract_errors
from scripts.validate_data import validate_record

MIGRATIONS = sorted((ROOT / 'supabase/migrations').glob('*.sql'))


def latest_check_values(constraint, inline_pattern):
    """Allowed values from the most recent migration defining a check constraint (or its inline original)."""
    text = '\n'.join(m.read_text() for m in MIGRATIONS)
    found = re.findall(r'add constraint %s check \(\s*\w+ in \(([^)]*)\)\)' % constraint, text)
    if not found:
        found = re.findall(inline_pattern, text)
    assert found, 'constraint not found: ' + constraint
    return frozenset(re.findall(r"'([^']+)'", found[-1]))


class ImportContractTests(unittest.TestCase):
    def test_repository_data_generates_import_sql(self):
        # Every persisted record must pass the importer's own checks, not only validate_data.py.
        batches = list(importer.batches())
        self.assertGreater(len(batches), 0)
        domains = {d for _, d, _ in records()}
        self.assertTrue(domains <= IMPORT_DOMAINS, domains - IMPORT_DOMAINS)

    def test_every_import_domain_has_a_normalized_mapping(self):
        sql = importer.bulk_batch([])
        for domain in IMPORT_DOMAINS:
            self.assertIn("r.domain=%s" % importer.literal(domain), sql, 'no insert mapping for ' + domain)
        self.assertEqual(set(importer.TABLES), set(IMPORT_DOMAINS))

    def test_controlled_values_match_database_constraints(self):
        expected = {
            ('credit_policies', 'policy_kind'): latest_check_values('credit_policies_policy_kind_check',
                r"policy_kind text not null check \(policy_kind in \(([^)]*)\)\)"),
            ('appeals', 'appeal_kind'): latest_check_values('appeal_policies_appeal_kind_check',
                r"appeal_kind text not null check \(appeal_kind in \(([^)]*)\)\)"),
            ('degree_requirements', 'requirement_kind'): latest_check_values('degree_requirements_requirement_kind_check',
                r"requirement_kind text not null check \(requirement_kind in \(([^)]*)\)\)"),
            ('costs', 'residency'): latest_check_values('institution_costs_residency_check',
                r"residency text not null check \(residency in \(([^)]*)\)\)"),
        }
        for (domain, field), values in expected.items():
            self.assertEqual(CONTROLLED_VALUES[domain][field], values, f'{domain}.{field} drifted from the migration')

    def test_new_unmapped_domain_fails_validation_and_import(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / 'data/institutions/test/scholarship_essays/2026-27.json'
            target.parent.mkdir(parents=True)
            target.write_text(json.dumps({'institution_key': 'test', 'academic_year': '2026-27', 'records': [
                {'record_key': 'essay', 'source_url': 'https://example.edu', 'verification_status': 'verified',
                 'last_verified_at': '2026-10-01'}]}))
            rows = list(records(root))
            self.assertEqual(rows[0][1], 'scholarship_essays')
            self.assertEqual(validate_record(target, rows[0][2], 1), [])  # provenance alone would pass...
            self.assertTrue(import_contract_errors('scholarship_essays', rows[0][2]))  # ...the contract does not
            with mock.patch.object(importer, 'records', lambda: iter(rows)):
                with self.assertRaisesRegex(ValueError, 'explicit normalized mapping'):
                    list(importer.batches())

    def test_disallowed_controlled_value_and_missing_key_are_rejected(self):
        self.assertTrue(import_contract_errors('credit_policies', {'institution_key': 'x', 'policy_kind': 'TRANSFER',
            'policy_url': 'https://example.edu', 'source_url': 'https://example.edu'}))
        self.assertTrue(import_contract_errors('appeals', {'institution_key': 'x', 'appeal_kind': 'budget', 'offered': True}))
        self.assertTrue(import_contract_errors('degree_requirements', {'institution_key': 'x', 'academic_year': '2026-27',
            'program_name': 'P', 'requirement_key': 'k', 'requirement_kind': 'program_plan', 'source_url': 'https://example.edu'}))

    def test_reconciliation_covers_all_repository_domains(self):
        sql = importer.reconcile_sql()
        for domain in {d for _, d, _ in records()}:
            self.assertIn("domain=%s" % importer.literal(domain), sql)
        self.assertIn('credit_equivalencies', sql)
        self.assertIn('reference_revisions', sql)

    def test_synthetic_program_integration_sql_still_generates(self):
        # The rollback-only PostgreSQL fixtures must satisfy the same import contract.
        from scripts.test_program_import import integration_sql
        self.assertIn('rollback;', integration_sql())

    def test_degree_mapping_keeps_full_payload(self):
        r = next(r for _, d, r in records() if d == 'degree_requirements')
        sql = importer.bulk_batch([{'domain': 'degree_requirements', 'natural_key': 'k', 'source_file': 'f', 'payload': r}])
        self.assertIn('rule_details', sql)
        r = next(r for _, d, r in records() if d == 'degree_requirements' and r['institution_key'] == 'utk' and r['requirement_kind'] == 'program_plan')
        sql = importer.bulk_batch([{'domain': 'degree_requirements', 'natural_key': 'k', 'source_file': 'f', 'payload': r}])
        self.assertEqual(len(r['rule_details']['terms']), 8)
        self.assertIn('requirement_group/v1', sql)  # structured plan travels intact into the batch


if __name__ == '__main__':
    unittest.main()


class LiveImportWorkflowTests(unittest.TestCase):
    def test_existing_database_reconciliation_allows_revision_history(self):
        self.assertIn('reference_revisions', importer.reconcile_sql(fresh=True))
        self.assertNotIn('reference_revisions', importer.reconcile_sql(fresh=False))

    def test_live_import_script_runs_preflight_reconciles_and_checks_idempotence(self):
        script = (ROOT / 'scripts/live_import.sh').read_text()
        self.assertIn('set -euo pipefail', script)
        self.assertIn('live_preflight.sql', script)
        self.assertLess(script.index('check_migration_history.py --live'), script.index('live_preflight.sql'))
        self.assertIn('--existing-database', script)
        self.assertEqual(script.count('for f in "$work"/batches/*.sql'), 2)  # two passes
        self.assertNotIn('echo "$DATABASE_URL', script)

    def test_preflight_checks_every_migration_the_importer_needs(self):
        sql = (ROOT / 'supabase/checks/live_preflight.sql').read_text()
        for marker in ('20261002131440', '20261002134049', '20261002132345', 'program_plan', 'policy_details'):
            self.assertIn(marker, sql)

    def test_workflow_skips_cleanly_without_secret_and_never_runs_concurrently(self):
        wf = (ROOT / '.github/workflows/live-import.yml').read_text()
        self.assertIn('secrets.SUPABASE_DB_URL', wf)
        self.assertIn("steps.secret.outputs.configured == 'true'", wf)
        self.assertIn('cancel-in-progress: false', wf)
        self.assertIn('branches: [main]', wf)
        self.assertNotIn('pull_request', wf)  # PR code never receives the database secret
