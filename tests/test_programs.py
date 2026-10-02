import unittest
from pathlib import Path
from backend.store import natural_key
from scripts.validate_data import ROOT,validate_record
from scripts.test_program_import import fixture_rows

class ProgramTests(unittest.TestCase):
    def test_identity_survives_rename_and_separates_years(self):
        r=fixture_rows()[1]['payload']
        renamed={**r,'program_name':'New name','record_key':'different-label'}
        self.assertEqual(natural_key('academic_programs',r),natural_key('academic_programs',renamed))
        self.assertNotEqual(natural_key('academic_programs',r),natural_key('academic_programs',{**r,'academic_year':'2026-27'}))

    def test_requirement_identity_includes_parent(self):
        r=fixture_rows()[-1]['payload']
        self.assertNotEqual(natural_key('degree_requirements',r),natural_key('degree_requirements',{**r,'program_key':'chemistry-bs'}))

    def test_invalid_credit_rules_rejected_but_unknowns_allowed(self):
        r=fixture_rows()[-1]['payload']
        self.assertEqual(validate_record(ROOT/'data',r,0,'degree_requirements'),[])
        for change in [{'minimum_credits':-1},{'rule_details':'guess'},{'program_key':None},{'requirement_kind':'imaginary'}]:
            self.assertTrue(validate_record(ROOT/'data',{**r,**change},0,'degree_requirements'))

if __name__=='__main__': unittest.main()
