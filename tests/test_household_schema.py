"""Static guards for the household practice migration (no database needed)."""
import re, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MIGRATION = next((ROOT / 'supabase/migrations').glob('*_household_practice_progress.sql'))
HIDDEN_QUESTION_COLUMNS = {'accepted_answers', 'hints', 'teaching_explanation', 'strategy_explanation'}
CLIENT_READ_ONLY = ['practice_attempts', 'practice_attempt_events', 'practice_sessions', 'practice_session_items',
                    'ai_help_requests', 'subscriptions', 'household_members', 'household_invitations']


def sql_text():
    return re.sub(r'--[^\n]*', '', MIGRATION.read_text(encoding='utf-8')).lower()


def expanded(sql):
    """Inline `foreach t in array array['a',...] loop ... end loop` blocks once per element."""
    def unroll(m):
        names = re.findall(r"'([^']+)'", m.group(1))
        body = m.group(2)
        out = []
        for name in names:
            stmt = re.sub(r"execute format\('((?:[^']|'')*)'\s*,\s*t\)",
                          lambda s: s.group(1).replace("''", "'").replace('%i', name), body)
            out.append(stmt)
        return '\n'.join(out)
    return re.sub(r'foreach t in array array\[(.*?)\] loop(.*?)end loop', unroll, sql, flags=re.S)


class HouseholdMigrationTests(unittest.TestCase):
    def setUp(self):
        self.sql = sql_text()
        self.flat = expanded(self.sql)
        self.grants = re.findall(r'\bgrant\b[^;]*;', self.flat)

    def test_every_table_has_rls_and_anon_revoke(self):
        tables = re.findall(r'create table public\.(\w+)', self.sql)
        self.assertGreaterEqual(len(tables), 25)
        for t in tables:
            self.assertRegex(self.flat, rf'alter table public\.{t} enable row level security', t)
            self.assertRegex(self.flat, rf'revoke all on public\.{t} from [^;]*\banon\b', t)
        for v in re.findall(r'create view public\.(\w+)', self.sql):
            self.assertIn('security_invoker = true', self.sql.split(f'create view public.{v}')[1].split(' as')[0], v)
            self.assertRegex(self.flat, rf'revoke all on public\.{v} from [^;]*\banon\b', v)

    def test_nothing_is_granted_to_anon(self):
        for grant in self.grants:
            self.assertNotRegex(grant, r'\bto\b[^;]*\banon\b', grant)

    def test_every_function_pins_search_path(self):
        functions = re.findall(r'create (?:or replace )?function (.*?)\bas \$\$', self.sql, flags=re.S)
        definers = [f for f in functions if 'security definer' in f]
        self.assertGreaterEqual(len(definers), 28)
        for header in functions:
            self.assertIn("set search_path = ''", header, header.split('(')[0])

    def test_functions_are_revoked_from_public(self):
        defined = set(re.findall(r'create function public\.(\w+)\(', self.sql))
        listed = set()
        for block in re.findall(r'proname = any \(array\[(.*?)\]\)', self.sql, flags=re.S):
            listed |= set(re.findall(r"'(\w+)'", block))
        self.assertEqual(defined, listed, 'every function needs an explicit privilege decision')

    def test_answers_are_not_client_selectable(self):
        grant = re.search(r'grant select \(([^)]*)\)\s*on public\.practice_questions to authenticated', self.sql)
        self.assertIsNotNone(grant)
        columns = {c.strip() for c in grant.group(1).split(',')}
        self.assertFalse(columns & HIDDEN_QUESTION_COLUMNS)
        self.assertNotRegex(self.flat, r'grant [^;(]*on public\.practice_questions to authenticated')
        self.assertNotRegex(self.flat, r'grant [^;]*on public\.(practice_question_distractors|app_settings) to authenticated')
        strategies = re.search(r'grant select \(([^)]*)\)\s*on public\.practice_question_strategies', self.sql)
        self.assertNotIn('strategy_explanation', strategies.group(1))

    def test_integrity_tables_are_read_only_for_clients(self):
        for table in CLIENT_READ_ONLY:
            grants = [g for g in self.grants if re.search(rf'on public\.{table} to [^;]*authenticated', g)]
            self.assertTrue(grants, table)
            for g in grants:
                self.assertRegex(g, r'^grant select\b(?! *,)(?:\s*\([^)]*\))?\s+on\b', f'{table}: {g}')

    def test_no_date_of_birth_column(self):
        self.assertNotRegex(self.sql, r'birth|\bdob\b')


if __name__ == '__main__':
    unittest.main()
