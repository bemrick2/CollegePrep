"""Static guards for the household practice migration (no database needed)."""
import re, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MIGRATION = next((ROOT / 'supabase/migrations').glob('*_household_practice_progress.sql'))


def sql_text():
    return re.sub(r'--[^\n]*', '', MIGRATION.read_text(encoding='utf-8')).lower()


def expanded(sql):
    """Inline `foreach t in array array['a',...] loop ... end loop` blocks once per element."""
    def unroll(m):
        names = re.findall(r"'([^']+)'", m.group(1))
        body = m.group(2)
        out = []
        for name in names:
            stmt = re.sub(r"execute format\('([^']*(?:''[^']*)*)'\s*,\s*t\)", lambda s: s.group(1).replace('%i', name), body)
            out.append(stmt.replace('public.%i', 'public.' + name))
        return '\n'.join(out)
    return re.sub(r'foreach t in array array\[(.*?)\] loop(.*?)end loop', unroll, sql, flags=re.S)


class HouseholdMigrationTests(unittest.TestCase):
    def setUp(self):
        self.sql = sql_text()
        self.flat = expanded(self.sql)

    def test_every_table_has_rls_and_anon_revoke(self):
        tables = re.findall(r'create table public\.(\w+)', self.sql)
        self.assertGreaterEqual(len(tables), 11)
        for t in tables:
            self.assertRegex(self.flat, rf'alter table public\.{t} enable row level security', t)
            self.assertRegex(self.flat, rf'revoke all on public\.{t} from [^;]*\banon\b', t)

    def test_nothing_is_granted_to_anon(self):
        for grant in re.findall(r'\bgrant\b[^;]*;', self.flat):
            self.assertNotRegex(grant, r'\bto\b[^;]*\banon\b', grant)

    def test_security_definer_functions_pin_search_path(self):
        functions = re.findall(r'create (?:or replace )?function (.*?)\bas \$\$', self.sql, flags=re.S)
        definers = [f for f in functions if 'security definer' in f]
        self.assertGreaterEqual(len(definers), 13)
        for header in definers:
            self.assertIn("set search_path = ''", header, header.split('(')[0])

    def test_answers_are_not_client_selectable(self):
        grant = re.search(r'grant select \(([^)]*)\)\s*on public\.practice_questions to authenticated', self.sql)
        self.assertIsNotNone(grant)
        columns = {c.strip() for c in grant.group(1).split(',')}
        self.assertFalse(columns & {'correct_answer', 'explanation', 'distractor_rationales'})
        self.assertNotRegex(self.sql, r'grant [^;(]*on public\.practice_questions to authenticated')

    def test_clients_cannot_write_attempts(self):
        grants = re.findall(r'grant ([^;]*?) on public\.practice_attempts to authenticated', self.sql)
        self.assertEqual(grants, ['select'])

    def test_no_date_of_birth_column(self):
        self.assertNotRegex(self.sql, r'birth|\bdob\b')


if __name__ == '__main__':
    unittest.main()
