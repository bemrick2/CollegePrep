"""Scripted recomputation for ACT Math batch 16. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402

money = lambda t: float(t.replace('$', '').replace(',', ''))


def c01(ch):
    best = min(packs * 10.0 + singles * 1.5 for packs in range(0, 6) for singles in range(0, 40) if packs * 10 + singles >= 37)
    return pick(ch, best, conv=money)


def c02(ch):
    juice = 2.0
    for _ in range(2):
        juice -= juice * 2 / 10
    return pick(ch, round(10 - juice, 2))


def c03(ch):
    return pick(ch, round(375 / 80, 1), conv=lambda t: float(t.split()[0]))


def c04(ch):
    n = sum(1 for x in range(-100, 101) if abs(x - 3) + abs(x + 2) == 5)
    return pick(ch, n, conv=lambda t: float('inf') if t.startswith('Inf') else float(t))


def c05(ch):
    hits = []
    for k, v in ch.items():
        e = v.replace('a²', 'a**2').replace('b²', 'b**2').replace(' ', '*')
        ok = True
        for a, b in ((1.0, 4.0), (2.0, 1.0), (3.0, 5.0)):
            lhs = (a ** -2 * b ** 3) ** (-0.5) * a * b ** 0.5
            if abs(eval(e, {'a': a, 'b': b}) - lhs) > 1e-9:  # noqa: S307
                ok = False
        if ok:
            hits.append(k)
    assert len(hits) == 1, hits
    return hits[0]


def c06(ch):
    f = lambda x: (x - 4) / 3
    hits = []
    for k, v in ch.items():
        e = v.split('=')[1].replace('−', '-').strip()
        e = re.sub(r'(\d)x', r'\1*x', e)
        g = lambda x, e=e: eval(e, {'x': x})  # noqa: S307
        try:
            if all(abs(f(g(x)) - x) < 1e-9 for x in (0.5, 2.0, 7.0)):
                hits.append(k)
        except ZeroDivisionError:
            pass
    assert len(hits) == 1, hits
    return hits[0]


def c07(ch):
    a = F(8, (3 - 1) * (3 - 5))
    return pick(ch, a * (0 - 1) * (0 - 5))


def pi_expr(t):
    s = t.replace(' ', '')
    m = re.fullmatch(r'(?:(\d+)\+)?(\d*)π', s)
    return (int(m.group(1)) if m.group(1) else 0) + (int(m.group(2)) if m.group(2) else 1) * math.pi


def c08(ch):
    r, ang = 9, 80
    return pick(ch, 2 * r + ang / 360 * 2 * math.pi * r, conv=pi_expr, tol=1e-9)


def c09(ch):  # coordinates: B=(0,0), C=(15,0); find A with AB=8, AC=12; bisector direction; intersect BC
    x = (8 ** 2 - 12 ** 2 + 15 ** 2) / (2 * 15)
    y = math.sqrt(8 ** 2 - x ** 2)
    A = (x, y)
    ub = ((0 - x) / 8, (0 - y) / 8)
    uc = ((15 - x) / 12, (0 - y) / 12)
    dvec = (ub[0] + uc[0], ub[1] + uc[1])
    t = -y / dvec[1]
    D = (x + t * dvec[0], 0)
    return pick(ch, round(D[0], 9), tol=1e-6)


def c10(ch):
    return pick(ch, sum((n if n % 2 == 0 else -2) for n in range(1, 7)) / 6)


CHECKS = {f'B016-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
