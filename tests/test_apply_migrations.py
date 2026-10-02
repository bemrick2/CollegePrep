import sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import apply_migrations as a


class ApplyMigrationTests(unittest.TestCase):
    def write(self, text):
        d = Path(tempfile.mkdtemp()); p = d / '20990101000000_x.sql'; p.write_text(text); return p

    def test_one_transaction_records_whole_file(self):
        sql = a.transaction_sql(self.write('create table t(id int);\r\n'), '20990101000000', 'x')
        self.assertTrue(sql.startswith('begin;\n\\i '))
        self.assertTrue(sql.rstrip().endswith('commit;'))
        self.assertIn("values ('20990101000000', 'x', array[$m", sql)
        self.assertIn('create table t(id int);\n', sql)
        self.assertNotIn('\r', sql)

    def test_dollar_tag_never_collides_with_content(self):
        sql = a.transaction_sql(self.write("select $m$ text $m$;"), '20990101000000', 'x')
        tag = sql.split('array[')[1].split('$')[1]
        self.assertNotIn(f'${tag}$', "select $m$ text $m$;")

    def test_files_with_own_transaction_control_are_refused(self):
        for text in ('begin;\nselect 1;\ncommit;', 'select 1;\n  COMMIT ;'):
            with self.assertRaises(ValueError):
                a.transaction_sql(self.write(text), '20990101000000', 'x')

    def test_repository_migrations_are_applicable(self):
        for p in sorted(a.h.MIGRATIONS.glob('*.sql')):
            a.transaction_sql(p, p.name[:14], p.stem[15:])


if __name__ == '__main__':
    unittest.main()
