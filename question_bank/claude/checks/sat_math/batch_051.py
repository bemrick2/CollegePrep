"""Scripted recomputation for SAT Math batch 51. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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


def c01(ch):
    m = F(-6, 4)
    on = {'3x + 2y = 12': (3, 2, 12), '2x + 3y = 13': (2, 3, 13), '3x − 2y = 0': (3, -2, 0), '2x − 3y = −5': (2, -3, -5)}
    hits = [t for t, (a, b, c) in on.items() if a * 2 + b * 3 == c and F(-a, b) == m]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c02(_):
    f12 = F(112, 100) * 50
    m = (f12 - 50) / 2
    return 50 - 10 * m


def c03(ch):
    x = F(7 + 2, 3)
    y = x - 2
    assert 2 * x + y == 7
    return by_text(ch, str((13 - 3 * y) / x).replace('', '') if False else f"{((13 - 3 * y) / x).numerator}/{((13 - 3 * y) / x).denominator}")


def c04(ch):
    y = next(y for y in range(0, 631) if 45 * (630 - y) == 2 * 30 * y)
    return pick(ch, y)


def c05(_):
    b = F(6, 2)
    return (3 * (2 + b) - 6) / 2


def c06(_):
    w = next(w for w in range(1, 100) if w * (w + 20) == 525)
    return F((w + 10) ** 2)


def c07(_):
    return F(next(k for k in range(-50, 100) if 36 - 4 * k < 0))


def c08(_):
    counts = {0: 12, 1: 15, 2: 8, 3: 4, 4: 1}
    mean = F(sum(k * v for k, v in counts.items()), sum(counts.values()))
    group = {k: v for k, v in counts.items() if k > mean}
    return F(sum(v for k, v in group.items() if k >= 3), sum(group.values()))


def c09(ch):
    t = F(2200, 10) / F(22, 10)
    return pick(ch, float(t))


def c10(ch):
    h = F(1, 3) * 4 * 12  # (1/3)π(2r)²(12) = πr²h
    return pick(ch, float(h))


def c11(ch):
    opp, adj = 2, 1
    hyp2 = opp ** 2 + adj ** 2
    v = F(opp ** 2, hyp2) - F(adj ** 2, hyp2)
    return by_text(ch, f"{v.numerator}/{v.denominator}")


def c12(ch):
    for na in (5, 20, 60):
        for nb in (5, 30, 90):
            assert F(na * 78 + 80, na + 1) > 78 and F(nb * 83 - 80, nb - 1) > 83
    return by_text(ch, "Class A's mean increases, and class B's mean increases.")


CHECKS = {f'Q051-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
