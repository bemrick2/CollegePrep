import json, sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import retain_evidence as R


class CitedShaTests(unittest.TestCase):
    def test_list_pages_cited_by_sha_are_collected(self):  # Liberty catalog count, UVU listed programs
        ev = {'catalog:k:2026-27': {'decision': {'source_evidence': {'sha256': 'a' * 64, 'url': 'https://x/programs/'}}, 'sentences': []},
              'c1': {'decision': {'reason': 'r'}, 'source': {'page_file': 'p.json.gz', 'url': 'https://x/p/'},
                     'evidence': [{'field': 'program_name', 'sha256': 'b' * 64, 'value': 'X, BS'}, {'field': 'catalog_year', 'value': '2026-2027'}]}}
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'evidence.json'; p.write_text(json.dumps(ev))
            self.assertEqual(R.cited_shas(p), {'a' * 64, 'b' * 64})
            self.assertEqual(R.cited(p)[0], {'p.json.gz'})


if __name__ == '__main__':
    unittest.main()
