"""Canonical AP, CLEP and IB exam names, matched from the wording institutions print.

A row is only treated as an exam equivalency when its exam cell matches one of these patterns,
which keeps navigation tables and footnotes out of the results. Order matters: more specific
patterns come first (Calculus BC before AB, Physics C before Physics 1, Literature before Language).
Codes follow the long form already used in data/institutions/utc.
"""
from __future__ import annotations
import re


def _slug(name):
    return re.sub(r'[^A-Z0-9]+', '-', name.upper().replace('&', ' ')).strip('-')


AP = [
    ('Art History', r'art\s*history'),
    ('African American Studies', r'african\s*american'),
    ('Biology', r'\bbiology\b'),
    ('Business with Personal Finance', r'business.*personal\s*finance|personal\s*finance'),
    ('Calculus BC', r'calc(ulus)?\.?\s*bc\b'),
    ('Calculus AB', r'calc(ulus)?\.?\s*ab\b'),
    ('Chemistry', r'\bchemistry\b'),
    ('Chinese Language & Culture', r'\bchinese\b'),
    ('Comparative Government & Politics', r'comparative\s*gov'),
    ('Computer Science Principles', r'computer\s*science\s*principles|\bcsp\b'),
    ('Computer Science A', r'computer\s*science\s*a\b|\bcs\s*a\b'),
    ('Cybersecurity', r'cyber\s*security|cybersecurity'),
    ('English Literature & Composition', r'english\s*lit(erature)?'),
    ('English Language & Composition', r'english\s*lang(uage)?'),
    ('Environmental Science', r'environmental\s*sci'),
    ('European History', r'european\s*history'),
    ('French Language & Culture', r'\bfrench\b'),
    ('German Language & Culture', r'\bgerman\b'),
    ('Human Geography', r'human\s*geography'),
    ('Italian Language & Culture', r'\bitalian\b'),
    ('Japanese Language & Culture', r'\bjapanese\b'),
    ('Latin', r'\blatin\b'),
    ('Macroeconomics', r'macro\s*-?\s*economics|\bmacro\b'),
    ('Microeconomics', r'micro\s*-?\s*economics|\bmicro\b'),
    ('Music Theory', r'music\s*theory'),
    ('Physics C: Electricity & Magnetism', r'physics\s*c\b.*(electric|e\s*&\s*m|e&m)|physics\s*c\s*[-:]?\s*e\s*(&|and)\s*m'),
    ('Physics C: Mechanics', r'physics\s*c\b.*mech'),
    ('Physics 1', r'physics\s*(1|i)\b'),
    ('Physics 2', r'physics\s*(2|ii)\b'),
    ('Precalculus', r'pre-?\s*calculus'),
    ('Psychology', r'\bpsychology\b'),
    ('Research', r'^(ap\s*)?research\b'),
    ('Seminar', r'^(ap\s*)?seminar\b'),
    ('Spanish Literature & Culture', r'spanish\s*lit'),
    ('Spanish Language & Culture', r'\bspanish\b'),
    ('Statistics', r'\bstatistics\b'),
    ('2-D Art & Design', r'2\s*-?\s*d\b'),
    ('3-D Art & Design', r'3\s*-?\s*d\b'),
    ('Drawing', r'\bdrawing\b'),
    ('United States Government & Politics', r'(u\.?\s*s\.?|united\s*states|american)\s*gov'),
    ('United States History', r'(u\.?\s*s\.?|united\s*states|american)\s*history'),
    ('World History: Modern', r'world\s*history'),
]

CLEP = [
    ('American Government', r'american\s*gov'),
    ('American Literature', r'american\s*lit'),
    ('Analyzing & Interpreting Literature', r'analyzing'),
    ('Biology', r'\bbiology\b'),
    ('Calculus', r'^(clep\s*)?calculus\b'),
    ('Chemistry', r'\bchemistry\b'),
    ('College Algebra', r'college\s*algebra'),
    ('College Composition Modular', r'composition\s*modular'),
    ('College Composition', r'college\s*composition'),
    ('College Mathematics', r'college\s*math'),
    ('English Literature', r'english\s*lit'),
    ('Financial Accounting', r'financial\s*accounting'),
    ('French Language', r'\bfrench\b'),
    ('German Language', r'\bgerman\b'),
    ('Spanish with Writing', r'spanish\s*with\s*writing'),
    ('Spanish Language', r'\bspanish\b'),
    ('History of the United States II', r'(history\s*of\s*the\s*united\s*states|u\.?s\.?\s*history)\s*(ii|2)\b'),
    ('History of the United States I', r'(history\s*of\s*the\s*united\s*states|u\.?s\.?\s*history)\s*(i|1)\b'),
    ('Human Growth & Development', r'human\s*growth'),
    ('Humanities', r'\bhumanities\b'),
    ('Information Systems', r'information\s*systems'),
    ('Introduction to Educational Psychology', r'educational\s*psych'),
    ('Introductory Business Law', r'business\s*law'),
    ('Introductory Psychology', r'(intro(ductory|duction\s*to)?\s*)?psychology'),
    ('Introductory Sociology', r'sociology'),
    ('Natural Sciences', r'natural\s*sciences'),
    ('Precalculus', r'pre-?\s*calculus'),
    ('Principles of Macroeconomics', r'macroeconomics'),
    ('Principles of Microeconomics', r'microeconomics'),
    ('Principles of Management', r'principles\s*of\s*management|\bmanagement\b'),
    ('Principles of Marketing', r'marketing'),
    ('Social Sciences & History', r'social\s*sciences'),
    ('Western Civilization II', r'western\s*civ(ilization)?\s*(ii|2)\b'),
    ('Western Civilization I', r'western\s*civ(ilization)?\s*(i|1)\b'),
]

IB = [
    ('Biology', r'\bbiology\b'), ('Business Management', r'business'), ('Chemistry', r'\bchemistry\b'),
    ('Computer Science', r'computer\s*science'), ('Economics', r'economics'),
    ('English A: Language & Literature', r'english\s*a\b.*lang'), ('English A: Literature', r'english\s*a\b.*lit'),
    ('Environmental Systems & Societies', r'environmental\s*systems'), ('Film', r'\bfilm\b'),
    ('French', r'\bfrench\b'), ('Geography', r'geography'), ('German', r'\bgerman\b'),
    ('Global Politics', r'global\s*politics'), ('History', r'\bhistory\b'), ('Latin', r'\blatin\b'),
    ('Mathematics: Analysis & Approaches', r'analysis\s*(and|&)\s*approaches'),
    ('Mathematics: Applications & Interpretation', r'applications\s*(and|&)\s*interpretation'),
    ('Music', r'\bmusic\b'), ('Philosophy', r'philosophy'), ('Physics', r'\bphysics\b'),
    ('Psychology', r'psychology'), ('Social & Cultural Anthropology', r'anthropology'),
    ('Spanish', r'\bspanish\b'), ('Theatre', r'theat(re|er)'), ('Visual Arts', r'visual\s*arts'),
]

CATALOGS = {'AP': AP, 'CLEP': CLEP, 'IB': IB}
_COMPILED = {k: [(n, re.compile(p, re.I)) for n, p in v] for k, v in CATALOGS.items()}


def match(kind: str, cell: str):
    """(code, canonical name) for an exam cell, or None. IB keeps the printed level (HL/SL)."""
    s = re.sub(r'\s+', ' ', (cell or '').replace('*', ' ')).strip()
    if not s or len(s) > 120: return None
    for name, rx in _COMPILED[kind]:
        if rx.search(s):
            level = ''
            if kind == 'IB':
                m = re.search(r'\b(HL|SL)\b', s)
                level = m.group(1) if m else ''
            code = f'{kind}-{_slug(name)}' + (f'-{level}' if level else '')
            return code, f'{kind} {name}' + (f' ({level})' if level else '')
    return None


def detect_kind(*texts) -> str | None:
    hay = ' '.join(t or '' for t in texts).lower()
    if 'clep' in hay: return 'CLEP'
    if 'international baccalaureate' in hay or re.search(r'\bib\b', hay): return 'IB'
    if 'advanced placement' in hay or re.search(r'\bap\b', hay): return 'AP'
    return None
