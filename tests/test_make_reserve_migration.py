import io, sys, tempfile, unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import make_reserve_migration as r
import apply_migrations as a

A = '30000000-0000-0000-0000-000000000001'
B = '30000000-0000-0000-0000-000000000002'


class ReserveGeneratorTests(unittest.TestCase):
    """The generator (the database-side refusals are tested by scripts/test_reserve_migration.py in CI's database job)."""

    def test_parse_items(self):
        self.assertEqual(r.parse_items(f'# reserve\n{A} math\n\n{B.upper()}  reading  # second\n'), [(A, 'math'), (B, 'reading')])

    def test_empty_list_is_refused(self):
        for text in ('', '\n# nothing here\n   \n'):
            with self.assertRaisesRegex(r.ReserveError, 'empty'):
                r.parse_items(text)
        with self.assertRaisesRegex(r.ReserveError, 'empty'):
            r.migration_sql('act_enhanced_2025', [])

    def test_malformed_lines_and_duplicates_are_refused(self):
        for text, msg in ((f'{A}', 'expected'), (f'{A} math extra', 'expected'), ('not-a-uuid math', 'not a question uuid'),
                          (f'{A} Math', 'not a section'), (f"{A} math'", 'not a section'), (f'{A} math\n{A} reading', 'twice')):
            with self.assertRaisesRegex(r.ReserveError, msg):
                r.parse_items(text)

    def test_exam_version_key_is_validated(self):
        for bad in ("act'; drop table x; --", '', 'ACT'):
            with self.assertRaises(r.ReserveError):
                r.migration_sql(bad, [(A, 'math')])

    def test_version_must_sort_after_every_migration(self):
        r.check_version('20991231000000', ['20261022050000', '20261023010000'])
        for bad in ('20261023010000', '20261022000000', '2026', 'x'):
            with self.assertRaises(r.ReserveError):
                r.check_version(bad, ['20261022050000', '20261023010000'])

    def test_sql_marks_exactly_the_listed_ids_and_checks_each_rule(self):
        sql = r.migration_sql('act_enhanced_2025', [(A, 'math'), (B, 'english')])
        self.assertIn(f'"id":"{A}","section":"math"', sql)
        self.assertIn(f'"id":"{B}","section":"english"', sql)
        self.assertIn("set pool = 'assessment'", sql)
        self.assertNotIn("pool = 'practice'", sql)
        for rule in ("is not published", "fails the rights gate", "has no current approved review", "'^human:'",
                     "has been attempted by a student", "was planned into a practice session", "was assigned to a progress check",
                     "belongs to exam version", "is in section", "does not exist", "using errcode = '23514'"):
            self.assertIn(rule, sql)

    def test_generated_file_is_applicable_by_the_applier(self):
        d = Path(tempfile.mkdtemp()); p = d / '20991231000000_assessment_reserve.sql'
        p.write_text(r.migration_sql('sat_digital_2024', [(A, 'math')]))
        sql = a.transaction_sql(p, '20991231000000', 'assessment_reserve')  # refuses files with their own transaction control
        self.assertTrue(sql.startswith('begin;'))

    def test_cli_writes_one_file_and_refuses_bad_input(self):
        d = Path(tempfile.mkdtemp()); mig = d / 'migrations'; mig.mkdir()
        (mig / '20261023010000_benchmark_item_assignment.sql').write_text('select 1;\n')
        items = d / 'items.txt'; items.write_text(f'{A} math\n')
        args = ['--exam-version', 'sat_digital_2024', '--items', str(items), '--migrations-dir', str(mig)]
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()) as err:
            self.assertEqual(r.main(args + ['--version', '20261023000000']), 1)  # older than an existing migration
            self.assertIn('must sort after', err.getvalue())
            self.assertEqual(r.main(args + ['--version', '20261024000000']), 0)
            out = mig / '20261024000000_assessment_reserve.sql'
            self.assertTrue(out.exists())
            self.assertEqual(r.main(args + ['--version', '20261024000000', '--out', str(out)]), 1)  # never overwrites
            items.write_text('# nothing\n')
            self.assertEqual(r.main(args + ['--version', '20261025000000']), 1)
            self.assertIn('empty', err.getvalue())
        self.assertFalse((mig / '20261025000000_assessment_reserve.sql').exists())


if __name__ == '__main__':
    unittest.main()
