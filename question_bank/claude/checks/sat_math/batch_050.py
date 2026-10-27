"""Scripted recomputation for SAT Math batch 50. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    t = next(t for t in range(0, 50) if 320 + 12 * t == 500 - 8 * (t - 5))
    return pick(ch, 2010 + t)


def c02(_):
    return F(68, 10) / (4 * F(2, 3) + 3)


def c03(ch):
    sols = {F(a, b) for a in range(-30, 31) for b in range(1, 31) if 3 * (2 * a - b) == 4 * (a + b)}
    assert sols == {F(7, 2)}
    return by_text(ch, "7/2")


def c04(ch):
    a = lambda b: 20 + (b - (-10)) * F(180 - 20, 90 - (-10))
    return pick(ch, float(a(0)), conv=lambda t: float(t.rstrip('°')))


def c05(ch):
    return pick(ch, round((8 ** 2) ** (1 / 3), 9))


def c06(_):
    b = F(9, 12)
    a = 12 / (1 - b)
    assert a - a * b == 12 and a * b - a * b * b == 9
    return a * b ** 3


def c07(ch):
    cands = {"x + 1/x": lambda x: x + 1 / x, "x + 1 + 1/x": lambda x: x + 1 + 1 / x,
             "x + 2 + 1/x": lambda x: x + 2 + 1 / x, "x² + 2 + 1/x²": lambda x: x * x + 2 + 1 / (x * x)}
    hits = [t for t, f in cands.items() if all(math.isclose(f(x), (math.sqrt(x) + 1 / math.sqrt(x)) ** 2) for x in (0.5, 2, 7))]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c08(ch):
    a_new = F(20 * 78 + 80, 21)
    b_new = F(30 * 83 - 80, 29)
    assert a_new > 78 and b_new > 83
    return by_text(ch, "Class A's mean increases, and class B's mean increases.")


def c09(ch):
    pts = {k: tuple(float(t) for t in v.strip('()').split(',')) for k, v in ch.items()}
    resid = {k: y - (-1.5 * x + 40) for k, (x, y) in pts.items()}
    return min(resid, key=resid.get)


def c10(_):
    h = F(50 * 40 * 15, 50 * 40 - 20 * 20)
    assert h < 20
    return h


def c11(ch):
    base = 55  # alternate interior angle; must be acute as a base angle
    return pick(ch, 180 - 2 * base, conv=lambda t: float(t.rstrip('°')))


CHECKS = dict(zip(['Q050-01', 'Q050-02', 'Q050-03', 'Q050-04', 'Q050-05', 'Q050-06', 'Q050-07', 'Q050-09', 'Q050-10', 'Q050-11'],
                  [c01, c02, c03, c04, c05, c06, c07, c09, c10, c11]))
