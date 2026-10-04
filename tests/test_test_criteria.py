import unittest
from backend.test_criteria import parse


def k(text):
    p = parse(text)
    return p['kind'], p['act_min'], p['act_max'], p['sat_min'], p['sat_max']


class TestCriteria(unittest.TestCase):
    def test_single_minimum(self):
        self.assertEqual(k('Minimum 31 ACT / 1390 SAT.'), ('single_minimum', 31, None, 1390, None))
        self.assertEqual(k('ACT 30+ / SAT 1360+'), ('single_minimum', 30, None, 1360, None))
        self.assertEqual(k('ACT: 27+ / SAT: 1220+'), ('single_minimum', 27, None, 1220, None))
        self.assertEqual(k('ACT 28 and above'), ('single_minimum', 28, None, None, None))
        self.assertEqual(k('ACT 28 & higher / SAT 1310 & higher'), ('single_minimum', 28, None, 1310, None))
        self.assertEqual(k('ACT/SAT Score: 28+/1300+'), ('single_minimum', 28, None, 1300, None))

    def test_range(self):
        self.assertEqual(k('ACT 30–36 / SAT 1360–1600'), ('range', 30, 36, 1360, 1600))
        self.assertEqual(k('22-23 ACT or 1100-1150 SAT'), ('range', 22, 23, 1100, 1150))
        self.assertEqual(k('32 - 36 ACT Score'), ('range', 32, 36, None, None))
        self.assertEqual(k('ACT/SAT Score: 34–36 / 1490–1600'), ('range', 34, 36, 1490, 1600))
        self.assertEqual(k('Trustees Scholarship(GPA 3.75+/ACT 33-36/SAT 1490-1600)'), ('range', 33, 36, 1490, 1600))

    def test_test_optional(self):
        self.assertEqual(k('Test-optional'), ('test_optional', None, None, None, None))
        self.assertEqual(k('No test score required; minimum 24 ACT preferred'), (None,) * 5)

    def test_unclassified(self):
        none = (None,) * 5
        for text in [None, '', 'ACT 27', '30 ACT Score', 'ACT 28 / SAT 1310', 'ACT 27 / SAT 1260–1290',
                     "Dean's 24-27 ACT or National Merit Semifinalist", 'ACT 1160 / 24 / SAT 1160 / 24',
                     '3.6+ GPA*,26-27 ACT**,1230-1290 SAT**', '3.98-4.00 GPA or 3.0+ GPA & 30+ ACT (1370+ SAT)',
                     'Valedictorian or Salutatorian', 'Old GED Score: 500-559', 'ACT 30+ / SAT 1365+',
                     'ACT 36-30', 'ACT 37+', 'ACT 24 ACT 26', 'Minimum ACT 24-27', 'ACT 30-36+',
                     'Tiers by GPA and ACT 21–23, 24–26', 'ACT 28+ / SAT 1300']:
            self.assertEqual(k(text), none, text)


if __name__ == '__main__':
    unittest.main()
