"""Scripted recomputation for SAT Math batch 22. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    return pick(ch, F(280) / (2000 * F(35, 1000)))


def c02(ch):
    sol = next(x for x in range(-50, 51) if 2 * (x - 4) == 10)
    assert sol - 4 == 5
    return by_text(ch, "x − 4 = 5")


def c03(_):
    return F(15) / (F(3, 4) - F(1, 3))


def c04(ch):
    m = F(3, 6)
    return pick(ch, F(4) / m)


def c05(ch):
    zs = sorted(x for x in range(-50, 51) if (x + 3) * (x - 1) - 5 == 0)
    assert zs == [-4, 2]
    return by_text(ch, "−4 and 2")


def c06(_):
    return 6 - ((-2) ** 2 + 4 * -2)


def c07(ch):
    for x in (1, 4, 9, 2.25):
        assert abs((4 * x ** 0.5) ** 2 - 16 * x) < 1e-9
    return by_text(ch, "16x")


def c08(ch):
    vals = [abs(F(n, 4) - 4) + abs(F(n, 4) + 2) for n in range(-400, 400)]
    return pick(ch, min(vals))


def c09(_):
    zs = [x for x in range(-50, 51) if -x * x + 8 * x - 12 == 0]
    assert all(-F(x) ** 2 + 8 * x - 12 > 0 for x in (3, 4, 5))
    return max(zs) - min(zs)


def c10(ch):
    d2 = 10 ** 2 + 5 ** 2
    assert d2 == 125
    return by_text(ch, "5√5")


CHECKS = {f'Q022-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
