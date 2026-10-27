"""Scripted recomputation for SAT Math batch 56. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    return F(next(m for m in range(1, 5000) if F(96, 100) * m + 12 == F(98, 100) * m))


def c02(ch):
    old = lambda x: F(32, 10) * (x - 2010) + 45
    b = old(2015)
    assert all(old(2015 + t) == F(32, 10) * t + b for t in range(0, 10))
    return by_text(ch, f"y = 3.2t + {int(b)}")


def c03(_):
    ta = F(10, 5) + F(900, 600)
    return (ta - F(7, 5)) * 600


def c04(ch):
    return pick(ch, float(F(30 * 2 + 20 * F(12, 10), 48)))


def c05(ch):
    C = lambda x: F(24, 10) * x + F(15, 10) * (12 - x)
    assert C(5) - C(4) == F(9, 10) and C(0) == 18
    return by_text(ch, "The increase, in dollars, in the cost of the blend for each liter of juice B replaced by a liter of juice A")


def c06(ch):
    s = next(s for s in (F(n, 4) for n in range(1, 400)) if F(1) / s + F(30) / (10 * s) == 2)
    return pick(ch, float(F(30) / (10 * s) * 60))


def c07(ch):
    a = F(30 - 10, 50 ** 2)
    return pick(ch, float(a * (20 - 50) ** 2 + 10))


def c08(_):
    v = 55 + math.sqrt((1.25 * 0.03 - 0.03) / 0.00005)
    return F(round(v))


def c09(ch):
    V = lambda x: x ** 3 + 7 * x * x + 14 * x + 8
    assert all(V(x) == (x + 1) * (x + 2) * (x + 4) for x in range(-5, 6))
    return by_text(ch, "4x + 12")


def c10(ch):
    return pick(ch, round(2 + 25 - 25 * math.cos(math.radians(60)), 9))


CHECKS = {f'Q056-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
