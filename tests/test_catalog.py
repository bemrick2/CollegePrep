import unittest
from datetime import date
from backend.catalog import eligible_appeal
class GateTests(unittest.TestCase):
    def setUp(self):
        self.r={'academic_year':'2026-27','verification_status':'verified','last_verified_at':'2026-10-01','offered':True,'appeal_kind':'financial_aid_appeal','source_url':'https://example.edu/appeals'}
    def test_generic_denied(self): self.assertFalse(eligible_appeal(self.r,'2026-27',date(2026,10,2)))
    def test_documented_year_and_freshness(self):
        self.r.update(qualifies_for_paid_addon=True,qualifying_path_evidence='Documented award review process')
        self.assertTrue(eligible_appeal(self.r,'2026-27',date(2026,10,2)))
        self.assertFalse(eligible_appeal(self.r,'2027-28',date(2026,10,2)))
        self.assertFalse(eligible_appeal(self.r,'2026-27',date(2027,10,2)))
        self.r['appeal_kind']='professional_judgment'
        self.assertFalse(eligible_appeal(self.r,'2026-27',date(2026,10,2)))
if __name__=='__main__': unittest.main()
