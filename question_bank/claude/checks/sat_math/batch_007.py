"""Scripted recomputation for SAT Math batch 7. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    m, x0, y0 = F(-5, 2), 4, -3
    return pick(ch, x0 + (12 - y0) / m)


def c02(ch):
    x = (F(4, 10) * 15 - F(36, 10)) / (F(2, 10) + F(4, 10))
    assert F(4, 10) * (15 - x) == F(2, 10) * x + F(36, 10)
    return pick(ch, x)


def c03(_):
    for c in range(-50, 51):
        if 3 * (15 - c) == 2 * 15 + 9:
            return c


def c04(ch):
    assert round(2500 * 1.06 ** 1) == 2650
    return by_text(ch, "2,500(1.06)ᵐ")


def c05(ch):
    bs = [b for b in range(1, 100) if b * b - 4 * 36 == 0]
    assert bs == [12]
    return pick(ch, bs[0])


def c06(ch):
    assert math.isclose(64 ** 0.5 * 64 ** (1 / 3), 64 ** (5 / 6))
    return pick(ch, F(1, 2) + F(1, 3))


def c07(ch):
    for g in range(0, 100):
        if F(g, 15 + g) == F(1, 4):
            return pick(ch, g)


def c08(_):
    return F(96) / F(75, 100) / F(160, 100)


def c09(ch):
    rs = [r for r in range(1, 50) if 2 * r ** 3 == 250]
    assert rs == [5]
    return pick(ch, rs[0])


def c10(_):
    h = 5 * math.sqrt(3)
    side = 2 * h / math.sqrt(3)
    assert math.isclose(side, 10)
    return 3 * round(side)


CHECKS = {f'Q007-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
