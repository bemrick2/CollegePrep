"""Scripted recomputation for SAT Math batch 53. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    sols = [(d, z) for d in range(1, 24) for z in range(-12, 13) if d + z == 3 and (d + 1) - z == 8]
    assert len(sols) == 1
    return F(sols[0][0] + 1)


def c02(ch):
    lo, hi = (F(794, 10) - 2) / 4, (F(806, 10) - 2) / 4
    c, r = (lo + hi) / 2, (hi - lo) / 2
    return by_text(ch, f"|p − {float(c):g}| ≤ {float(r):g}")


def c03(ch):
    C = lambda n: F(108, 100) * (250 + 18 * n)
    assert C(1) - C(0) == F(108, 100) * 18
    return by_text(ch, "The amount, in dollars, by which the total cost increases for each additional guest, including tax")


def c04(ch):
    rate = F(76 - 58, 90)
    mins = (58 - 20) / rate
    t = 11 * 60 + 10 + int(mins)
    h, m = divmod(t, 60)
    return by_text(ch, f"{h - 12 if h > 12 else h}:{m:02d} {'p.m.' if h >= 12 else 'a.m.'}")


def c05(ch):
    v = F(1745, 5)
    return pick(ch, float((v - 331) / F(6, 10)))


def c06(_):
    s = next(s for s in range(1, 100) if (s + 4) ** 2 - s * s == F(5, 4) * s * s)
    return F(s)


def c07(_):
    return F(sum(1 for x in range(0, 41) if x * (80 - 2 * x) - (10 * x + 300) > 0))


def c08(ch):
    ok = [x / 10 for x in range(1, 400) if x / 10 > 0 and 30 - 2 * x / 10 > 0]
    assert math.isclose(max(ok), 14.9)
    return by_text(ch, "0 < x < 15")


def c09(_):
    mm3 = F(54, 100) * 1000 * 1000
    return mm3 / 12 / 3600


def c10(ch):
    diff = 2 * 5 ** 2 - 7 ** 2
    return by_text(ch, "π" if diff == 1 else f"{diff}π")


def c11(_):
    vol = lambda c, h: F(c * c) * h  # times 1/(4π)
    return vol(F(11), F(17, 2)) / vol(F(17, 2), F(11))


def c12(_):
    return F(225, 10) / (F(5) / F(16, 10))


CHECKS = {f'Q053-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
