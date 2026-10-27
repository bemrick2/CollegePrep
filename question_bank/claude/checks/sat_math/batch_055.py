"""Scripted recomputation for SAT Math batch 55. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    cands = {"T = 7c/30 + 40": lambda c: F(7 * c, 30) + 40, "T = 30c/7 + 40": lambda c: F(30 * c, 7) + 40,
             "T = c/14 + 40": lambda c: F(c, 14) + 40, "T = 7(c + 40)/30": lambda c: F(7 * (c + 40), 30)}
    true = lambda c: F(14, 60) * c + 40
    hits = [t for t, f in cands.items() if all(f(c) == true(c) for c in (30, 60, 120))]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c02(_):
    ts = sorted(t for t in (F(n, 60) for n in range(0, 600)) if abs(9 - 6 * t) == 2)
    assert len(ts) == 2
    return ts[1] * 60


def c03(ch):
    return pick(ch, float(F(315, F(5, 2)) - F(315, F(7, 2))))


def c04(ch):
    k = next(k for k in range(0, 50) if F(49, 10) * ((k + 1) ** 2 - k * k) == F(343, 10))
    return pick(ch, k)


def c05(ch):
    t = lambda d, s, c: d / (s - c) + d / (s + c)
    cands = {"2ds/(s² − c²)": lambda d, s, c: 2 * d * s / (s * s - c * c), "2d/s": lambda d, s, c: 2 * d / s,
             "2ds/(s² + c²)": lambda d, s, c: 2 * d * s / (s * s + c * c), "2dc/(s² − c²)": lambda d, s, c: 2 * d * c / (s * s - c * c)}
    pts = [(F(10), F(8), F(3)), (F(4), F(15), F(5))]
    hits = [k for k, f in cands.items() if all(f(*p) == t(*p) for p in pts)]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c06(_):
    a = F(7 - 3, (0 - 2) ** 2)
    return a * (5 - 2) ** 2 + 3


def c07(_):
    return max(x * (12 - x) + 4 * x for x in (F(n, 4) for n in range(-80, 160)))


def c08(ch):
    return pick(ch, ((260 - 100) / 40) ** 2)


def c09(_):
    t1 = F(40, 36) * 60
    t2 = t1 - F(8, 3)
    return 40 / (t2 / 60)


def c10(ch):
    f = F(112, 140)
    return by_text(ch, f"a {int((1 - f) * 100)}% decrease")


def c11(ch):
    cm = 0.45 / (math.pi * 2 ** 2) * 100
    return pick(ch, round(cm, 1))


def c12(_):
    depth = math.sqrt(25 ** 2 - ((70 - 40) / 2) ** 2)
    return F(round((40 + 70) / 2 * depth * 300 / 1000, 6)).limit_denominator(10)


CHECKS = {f'Q055-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
