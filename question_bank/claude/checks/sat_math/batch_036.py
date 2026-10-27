"""Scripted recomputation for SAT Math batch 36. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    rate = F(1700 - 1150, 65 - 40)
    fee = 1150 - 40 * rate
    return fee + 50 * rate * F(11, 10)


def c02(ch):
    missed = set()
    for m, b in ((-2, 3), (-0.5, 7), (-5, 0.25)):
        slope, icpt = b, m  # y = bx + m
        xs = [x / 1000 for x in range(-100000, 100001) if x]
        quads = {('I' if y > 0 else 'IV') if x > 0 else ('II' if y > 0 else 'III')
                 for x in xs for y in [slope * x + icpt] if y}
        missed.add(frozenset({'I', 'II', 'III', 'IV'} - quads))
    assert missed == {frozenset({'II'})}
    return by_text(ch, 'Quadrant II')


def c03(ch):
    (x1, y1), (x2, y2) = (2, 3), (5, -1)
    on = lambda p: (y2 - y1) * (F(p[0]) - x1) == (x2 - x1) * (F(p[1]) - y1)
    pts = {k: tuple(int(t.strip().replace('−', '-')) for t in v.strip('()').split(',')) for k, v in ch.items()}
    hits = [k for k, p in pts.items() if on(p)]
    assert len(hits) == 1
    a, b = y2 - y1, x1 - x2  # line: a x + b y = c with c nonzero
    assert a * x1 + b * y1 != 0
    return hits[0]


def c04(_):
    f = {1: 5, 2: 3, 3: 8, 4: 2, 5: 6}
    sols = [x for x in range(0, 5) if x + 1 in f and f[x + 1] - 2 == 6]
    assert sols == [2]
    return F(2)


def c05(_):
    ks = [k for k in (F(n, 4) for n in range(-80, 81)) if (3 - 1) * (3 + 2) * (3 - k) == 20]
    assert ks == [1]
    return F(len({1, -2, ks[0]}))


def c06(_):
    us = [u for u in range(-50, 51) if u * u - 3 * u - 10 == 0]
    return sum(F(u + 1, 2) for u in us)


def c07(ch):
    lo, hi = F(29, 100) * 4000, F(41, 100) * 4000
    hits = [k for k, v in ch.items() if lo <= int(v.replace(',', '')) <= hi]
    assert len(hits) == 1
    return hits[0]


def c08(ch):
    # combined median of A = nine 40s and B = (0,0,0,0,50,50,50,50,50) is 40, so "45" and "greater than 45" fail
    data = sorted([40] * 9 + [0] * 4 + [50] * 5)
    assert (data[8] + data[9]) / 2 == 40
    return by_text(ch, 'It is between 40 and 50, inclusive.')


def c09(ch):
    d2 = (1 + 2) ** 2 + (2 - 5) ** 2
    hits = [k for k, v in ch.items() if int(v.replace('−', '-')) + 29 > d2]
    assert len(hits) == 1
    return hits[0]


def c10(ch):
    s = math.sqrt(100 + 2 * 40)
    a, b = (s + math.sqrt(s * s - 160)) / 2, (s - math.sqrt(s * s - 160)) / 2
    assert math.isclose(a * a + b * b, 100) and math.isclose(a * b / 2, 20)
    return by_text(ch, '10 + 6√5') if math.isclose(10 + a + b, 10 + 6 * math.sqrt(5)) else None


def c11(_):
    x = next(x for x in range(0, 1000) if F(x, x + 66) == F(45, 100))
    return F(x, x + 48)


def c12(ch):
    lo, hi = max(54 - 4, 47 - 5), min(54 + 4, 47 + 5)
    hits = [k for k, v in ch.items() if lo <= int(v.rstrip('%')) <= hi]
    assert len(hits) == 1
    return hits[0]


CHECKS = {f'Q036-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
