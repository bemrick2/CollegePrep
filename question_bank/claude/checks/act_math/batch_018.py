"""Scripted recomputation for ACT Math batch 18. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    hits = []
    for k, v in ch.items():
        e = v.split('=')[1].strip().replace('−', '-')
        e = re.sub(r'(\d)S', r'\1*S', e)
        ok = True
        for n, a, l in ((2, 1, 3), (5, 2, 10), (7, -3, 4)):
            S = F(n, 2) * (a + l)
            try:
                if F(eval(e, {'S': S, 'n': F(n), 'a': F(a)})) != l:  # noqa: S307
                    ok = False
            except ZeroDivisionError:
                ok = False
        if ok:
            hits.append(k)
    assert len(hits) == 1, hits
    return hits[0]


def c02(ch):
    orig = lambda x: (x * x - 4) / (x * x - 4 * x + 4) * (x - 2) / (x + 2)
    hits = []
    for k, v in ch.items():
        e = v.replace('−', '-')
        if all(abs(eval(e, {'x': x}) - orig(x)) < 1e-9 for x in (3.0, 4.5, -7.0, 10.0)):  # noqa: S307
            hits.append(k)
    assert len(hits) == 1, hits
    return hits[0]


def c03(ch):
    return pick(ch, sum(20 + 2 * i for i in range(15)))


def c04(ch):
    f = lambda x: 3.0 ** x
    hits = []
    for k, v in ch.items():
        e = v.replace('·', '*').replace('^', '**').replace('−', '-')
        if all(abs(eval(e, {'x': x}) - (f(x + 1) - f(x))) < 1e-9 for x in (0.0, 1.0, 2.5)):  # noqa: S307
            hits.append(k)
    assert len(hits) == 1, hits
    return hits[0]


def c05(ch):
    return pick(ch, (4 / 3 * math.pi * 27) / (math.pi * 36), tol=1e-9)


def expr(t):
    s = t.replace('−', '-')
    s = re.sub(r'(\d+)√(\d+)', r'\1*math.sqrt(\2)', s)
    s = re.sub(r'√(\d+)', r'math.sqrt(\1)', s)
    return eval(s, {'math': math})  # noqa: S307


def c06(ch):
    return pick(ch, 10 * math.sin(math.radians(60)), conv=expr, tol=1e-9)


def c07(ch):
    r = 2.0
    inc = (math.pi * (1.5 * r) ** 2 - math.pi * r ** 2) / (math.pi * r ** 2) * 100
    return pick(ch, round(inc, 6), conv=lambda t: float(t.rstrip('%')))


def c08(ch):
    for d in range(0, 211):
        for n in range(0, 211):
            p = 210 - d - n
            if p >= 0 and 3 * p == 2 * n and 5 * n == 4 * d:
                return pick(ch, d)
    raise ValueError


def c09(ch):
    comp = 2000 * 1.05 ** 3 - 2000
    simple = 2000 * 0.05 * 3
    return pick(ch, round(comp - simple, 2), conv=lambda t: float(t.replace('$', '').replace(',', '')))


def c10(ch):
    return pick(ch, F(18 + 6, 40))


CHECKS = {f'B018-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
