import io, sys, tempfile, unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import make_reserve_migration as r
import apply_migrations as a

A = '30000000-0000-0000-0000-000000000001'
B = '30000000-0000-0000-0000-000000000002'


class ReserveGeneratorTests(unittest.TestCase):
    """The generator. The database-side refusals and the single-transaction release are tested by
    scripts/test_reserve_migration.py and scripts/test_reserve_release.py in CI's database job."""

    def test_parse_items(self):
        self.assertEqual(r.parse_items(f'# reserve\n{A} math\n\n{B.upper()}  reading  # second\n'), [(A, 'math'), (B, 'reading')])

    def test_empty_list_is_refused(self):
        for text in ('', '\n# nothing here\n   \n'):
            with self.assertRaisesRegex(r.ReserveError, 'empty'):
                r.parse_items(text)
        with self.assertRaisesRegex(r.ReserveError, 'empty'):
            r.reserve_sql('act_enhanced_2025', [])

    def test_malformed_lines_and_duplicates_are_refused(self):
        for text, msg in ((f'{A}', 'expected'), (f'{A} math extra', 'expected'), ('not-a-uuid math', 'not a question uuid'),
                          (f'{A} Math', 'not a section'), (f"{A} math'", 'not a section'), (f'{A} math\n{A} reading', 'twice')):
            with self.assertRaisesRegex(r.ReserveError, msg):
                r.parse_items(text)

    def test_exam_version_key_is_validated(self):
        for bad in ("act'; drop table x; --", '', 'ACT'):
            with self.assertRaises(r.ReserveError):
                r.reserve_sql(bad, [(A, 'math')])

    def test_sql_marks_exactly_the_listed_ids_and_checks_each_rule(self):
        sql = r.reserve_sql('act_enhanced_2025', [(A, 'math'), (B, 'english')])
        self.assertTrue(sql.startswith(r.MARKER))
        self.assertIn(f'"id":"{A}","section":"math"', sql)
        self.assertIn(f'"id":"{B}","section":"english"', sql)
        self.assertIn("set pool = 'assessment'", sql)
        self.assertNotIn("pool = 'practice'", sql)
        self.assertIn(r"q.review_method ~ '^human:\s*\S'", sql)  # case-sensitive, names a reviewer
        for rule in ("is not published", "fails the rights gate", "has no current approved review", "named human reviewer",
                     "has been attempted by a student", "was planned into a practice session", "was assigned to a progress check",
                     "belongs to exam version", "is in section", "has no progress-check plan", "does not exist",
                     "shares its passage with a practice item", "shares its passage with another reserved or listed item",
                     "using errcode = '23514'"):
            self.assertIn(rule, sql)

    def test_script_records_itself_and_refuses_a_rerun(self):
        sql = r.reserve_sql('sat_digital_2024', [(A, 'math')])
        self.assertIn('insert into public.practice_reserve_releases', sql)
        self.assertIn('this reserve was already applied', sql)
        self.assertIn("current_setting('collegeprep.reserve_file_sha256', true)", sql)

    def test_verify_script_requires_an_exact_regeneration(self):
        raw = r.reserve_sql('sat_digital_2024', [(A, 'math'), (B, 'math')]).encode()
        self.assertEqual(r.verify_script(raw), [])
        self.assertTrue(r.verify_script(raw + b'\n'))                               # any extra byte
        self.assertTrue(r.verify_script(raw.replace(b'math', b'reading', 1)))         # the listing no longer matches
        self.assertTrue(r.verify_script(raw.replace(b'do $reserve$', b'Commit Work;\ndo $reserve$')))
        self.assertTrue(r.verify_script(raw.replace(b'do $reserve$', b'\\i other.sql\ndo $reserve$')))
        self.assertTrue(r.verify_script(b'select 1;'))

    def test_script_passes_the_appliers_reserve_checks(self):
        d = Path(tempfile.mkdtemp()); p = d / 'reserve.sql'
        p.write_text(r.reserve_sql('sat_digital_2024', [(A, 'math')]))
        self.assertEqual(a.check_reserve(p), [])

    def test_cli_writes_a_script_outside_migrations_and_refuses_bad_input(self):
        d = Path(tempfile.mkdtemp()); mig = d / 'migrations'; mig.mkdir()
        items = d / 'items.txt'; items.write_text(f'{A} math\n')
        args = ['--exam-version', 'sat_digital_2024', '--items', str(items), '--migrations-dir', str(mig)]
        out = d / 'reserve' / 'r1.sql'
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()) as err:
            self.assertEqual(r.main(args + ['--out', str(mig / '20991231000000_assessment_reserve.sql')]), 1)
            self.assertIn('never a migration', err.getvalue())
            self.assertEqual(r.main(args + ['--out', str(mig / 'sub' / 'r.sql')]), 1)
            self.assertEqual(r.main(args + ['--out', str(d / 'r.txt')]), 1)
            self.assertEqual(r.main(args + ['--out', str(out)]), 0)
            self.assertTrue(out.read_text().startswith(r.MARKER))
            self.assertEqual(r.main(args + ['--out', str(out)]), 1)  # never overwrites
            items.write_text('# nothing\n')
            self.assertEqual(r.main(args + ['--out', str(d / 'r2.sql')]), 1)
            self.assertIn('empty', err.getvalue())
        self.assertEqual(list(mig.rglob('*.sql')), [])
        self.assertFalse((d / 'r2.sql').exists())


if __name__ == '__main__':
    unittest.main()
