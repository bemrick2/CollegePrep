import json
import tempfile
import unittest
from pathlib import Path
from backend.api import query
from backend.store import connect,load

class ComparisonTests(unittest.TestCase):
    def test_exact_year_missing_schools_and_unverified_records(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder); (root/'data').mkdir()
            identity={'domain':'institutions','institution_key':'test','display_name':'Test',
                'verification_status':'verified','source_url':'https://example.edu','last_verified_at':'2026-10-02'}
            cost={**identity,'domain':'costs','academic_year':'2025-26','residency':'in_state','tuition':1000}
            unknown_cost={**cost,'academic_year':'2026-27','verification_status':'unverified'}
            orphan_requirement={**identity,'domain':'degree_requirements','academic_year':'2026-27','program_key':'biology','requirement_key':'major','requirement_kind':'major','rule_details':{'schema':'requirement_group/v1','catalog_year':'2026-2027','group_type':'credit_total','category':'major_core'}}
            (root/'data/fixtures.json').write_text(json.dumps([identity,cost,unknown_cost,orphan_requirement]))
            db=connect(':memory:')
            try:
                load(db,root)
                status,result=query(db,'/v1/compare',{'institution_key':['test','missing'],'academic_year':['2026-27']})
                self.assertEqual(status,200)
                known,missing=result['institutions']
                self.assertTrue(known['found']); self.assertFalse(missing['found'])
                self.assertEqual(known['domains']['costs'],[])
                self.assertEqual(known['domains']['degree_requirements'],[])
                self.assertIn('degree_requirements',known['missing_domains'])
                self.assertIn('costs',known['missing_domains'])
                self.assertFalse(known['can_offer_paid_addon'])
                old=query(db,'/v1/compare',{'institution_key':['test'],'academic_year':['2025-26']})[1]
                self.assertEqual(old['institutions'][0]['domains']['costs'][0]['tuition'],1000)
                for params in [{},{'institution_key':['test']},{'academic_year':['2026-27'],'institution_key':['test','test']},{'academic_year':['2026-27'],'institution_key':[str(i) for i in range(21)]}]:
                    with self.assertRaises(ValueError): query(db,'/v1/compare',params)
            finally: db.close()
