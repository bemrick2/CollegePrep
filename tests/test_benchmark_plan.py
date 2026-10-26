"""The server's check plan (practice_benchmark_plan, #263) matches the app's PER_SECTION (web/src/lib/engine/benchmark.ts)."""
import re, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TS = ROOT / 'web/src/lib/engine/benchmark.ts'


def client_plan():
    text = TS.read_text(encoding='utf-8')
    block = text[text.index('export const PER_SECTION'):]
    block = block[:block.index('\n}\n')]
    plan, family = {}, None
    for line in block.splitlines():
        m = re.match(r'\s*(act|sat): \{\s*$', line)
        if m:
            family = m.group(1); continue
        m = re.match(r'\s*(initial|mini|full): \{(.*)\},?\s*$', line)
        if m and family:
            for sec, n in re.findall(r'(\w+): (\d+)', m.group(2)):
                plan[(family, m.group(1), sec)] = int(n)
    return plan


def server_plan():
    plan = {}
    for f in sorted((ROOT / 'supabase/migrations').glob('*.sql')):
        text = f.read_text(encoding='utf-8')
        for stmt in re.findall(r'insert into public\.practice_benchmark_plan\b.*?;', text, re.S | re.I):
            for fam, kind, sec, n in re.findall(r"\('(\w+)',\s*'(\w+)',\s*'(\w+)',\s*(\d+)\)", stmt):
                plan[(fam, kind, sec)] = int(n)
    return plan


class BenchmarkPlanTests(unittest.TestCase):
    def test_parsers_found_the_plans(self):
        self.assertGreaterEqual(len(client_plan()), 18)
        self.assertGreaterEqual(len(server_plan()), 12)

    def test_server_plan_matches_the_client_for_initial_and_mini(self):
        client = {k: v for k, v in client_plan().items() if k[1] != 'full'}
        self.assertEqual(server_plan(), client)

    def test_full_is_not_served_until_the_full_form_is_ready(self):
        # The client's full plan is a 99-per-section placeholder behind FULL_FORM_READY = false; the server has no rows.
        self.assertIn('export const FULL_FORM_READY = false', TS.read_text(encoding='utf-8'))
        self.assertFalse([k for k in server_plan() if k[1] == 'full'])

    def test_repeat_gap_is_not_longer_than_the_client_schedule(self):
        # The server refuses a mini sooner than min_days_after_completed; the app schedules one every MINI_EVERY_DAYS.
        days = int(re.search(r'export const MINI_EVERY_DAYS = (\d+)', TS.read_text(encoding='utf-8')).group(1))
        mig = (ROOT / 'supabase/migrations/20261023010000_benchmark_item_assignment.sql').read_text(encoding='utf-8')
        gap = int(re.search(r"\('mini', true, true, false, (\d+)\)", mig).group(1))
        self.assertLessEqual(gap, days)


if __name__ == '__main__':
    unittest.main()
