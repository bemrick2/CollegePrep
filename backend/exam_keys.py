"""Canonical exam keys for credit equivalencies (issue #37 CR-10).

A key is assigned only when a row's published exam name matches the closed catalog below after
normalising punctuation ("&" -> "and", ":" or " - " -> space), or a listed alias that names the same exam.
Anything else (subscores, "Language or Literature", IB and Cambridge, which mix levelled and unlevelled
names) keeps a null key, and matching falls back to the published name.
"""
import re

AP = ['2-D Art and Design', '3-D Art and Design', 'African American Studies', 'Art History', 'Biology',
      'Business with Personal Finance', 'Calculus AB', 'Calculus BC', 'Chemistry', 'Chinese Language and Culture',
      'Comparative Government and Politics', 'Computer Science A', 'Computer Science Principles', 'Cybersecurity',
      'Drawing', 'English Language and Composition', 'English Literature and Composition', 'Environmental Science',
      'European History', 'French Language and Culture', 'German Language and Culture', 'Human Geography',
      'Italian Language and Culture', 'Japanese Language and Culture', 'Latin', 'Macroeconomics', 'Microeconomics',
      'Music Theory', 'Physics 1', 'Physics 2', 'Physics C: Electricity and Magnetism', 'Physics C: Mechanics',
      'Precalculus', 'Psychology', 'Research', 'Seminar', 'Spanish Language and Culture',
      'Spanish Literature and Culture', 'Statistics', 'United States Government and Politics',
      'United States History', 'World History: Modern']
CLEP = ['American Government', 'American Literature', 'Analyzing and Interpreting Literature', 'Biology', 'Calculus',
        'Chemistry', 'College Algebra', 'College Composition', 'College Composition Modular', 'College Mathematics',
        'English Literature', 'Financial Accounting', 'French Language', 'German Language',
        'History of the United States I', 'History of the United States II', 'Human Growth and Development',
        'Humanities', 'Information Systems', 'Introduction to Educational Psychology', 'Introductory Business Law',
        'Introductory Psychology', 'Introductory Sociology', 'Natural Sciences', 'Precalculus',
        'Principles of Macroeconomics', 'Principles of Management', 'Principles of Marketing',
        'Principles of Microeconomics', 'Social Sciences and History', 'Spanish Language', 'Spanish with Writing',
        'Western Civilization I', 'Western Civilization II']
# Other published names for the same exam. Level 1/2 on CLEP language exams are score levels of one exam.
ALIASES = {
    'ap': {'american history': 'United States History', 'us government and politics': 'United States Government and Politics',
           'italian': 'Italian Language and Culture'},
    'clep': {'french language level 1': 'French Language', 'french language level 2': 'French Language',
             'german language level 1': 'German Language', 'german language level 2': 'German Language',
             'spanish language level 1': 'Spanish Language', 'spanish language level 2': 'Spanish Language'},
}
FAMILIES = {'AP': 'ap', 'CLEP': 'clep'}
NAMES = {'ap': AP, 'clep': CLEP}


def _norm(text):
    t = re.sub(r'\s*&\s*', ' and ', text.lower())
    t = re.sub(r'\s*(?::|\s-\s)\s*', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def _slug(name):
    return re.sub(r'[^a-z0-9]+', '-', _norm(name)).strip('-')


def catalog():
    """[(exam_key, family, display_name)] for every catalog exam."""
    return [(f'{fam}:{_slug(n)}', fam, n) for fam in ('ap', 'clep') for n in NAMES[fam]]


LOOKUP = {fam: {_norm(n): n for n in NAMES[fam]} for fam in NAMES}


def exam_key(policy_kind, name):
    fam = FAMILIES.get(policy_kind)
    if not fam or not name:
        return None
    n = _norm(name)
    prefix = fam + ' '
    if not n.startswith(prefix):
        return None
    n = n[len(prefix):]
    hit = LOOKUP[fam].get(n) or ALIASES[fam].get(n)
    return f'{fam}:{_slug(hit)}' if hit else None
