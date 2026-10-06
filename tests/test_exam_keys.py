import unittest
from backend.exam_keys import catalog, exam_key


class ExamKeys(unittest.TestCase):
    def test_keys(self):
        self.assertEqual(exam_key('AP', 'AP Calculus AB'), 'ap:calculus-ab')
        self.assertEqual(exam_key('AP', 'AP Chinese Language and Culture'), exam_key('AP', 'AP Chinese Language & Culture'))
        self.assertEqual(exam_key('AP', 'AP Physics C - Mechanics'), 'ap:physics-c-mechanics')
        self.assertEqual(exam_key('AP', 'AP Physics C: Mechanics'), 'ap:physics-c-mechanics')
        self.assertEqual(exam_key('AP', 'AP American History'), 'ap:united-states-history')
        self.assertEqual(exam_key('AP', 'AP World History: Modern'), 'ap:world-history-modern')
        self.assertEqual(exam_key('CLEP', 'CLEP Spanish Language Level 2'), 'clep:spanish-language')
        self.assertEqual(exam_key('CLEP', 'CLEP Biology'), 'clep:biology')

    def test_unmatched(self):
        for kind, name in [('AP', 'AP Music Theory - Aural Subscore'), ('AP', 'AP Spanish Language or Literature'),
                           ('IB', 'IB Biology'), ('AP', 'CLEP Biology'), ('CLEP', 'AP Biology'), ('AP', None),
                           ('CLEP', 'CLEP Trigonometry'), ('AP', 'Biology')]:
            self.assertIsNone(exam_key(kind, name), name)

    def test_catalog(self):
        keys = [k for k, _, _ in catalog()]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertTrue(all(k.split(':')[0] == f for k, f, _ in catalog()))
        self.assertRegex(' '.join(keys), r'^[a-z0-9:\- ]+$')


if __name__ == '__main__':
    unittest.main()
