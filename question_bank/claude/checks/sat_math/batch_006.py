"""Scripted recomputation for SAT Math batch 6. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    m = F(20 - 11, 5 - 2)
    b = 11 - m * 2
    assert m * 9 + b == 32
    return pick(ch, m * -4 + b)


def c02(ch):
    f = lambda c: F(18, 10) * c + 32
    return pick(ch, f(15) - f(0))


def c03(_):
    for cents in range(1, 3400):
        p = F(cents, 100)
        if 8 * (p + 2) + 4 * p == 34:
            return p


def c04(ch):
    for x in (1, 2, -3, F(1, 2)):
        assert (3 * x - 2) ** 2 - (x + 1) * (9 * x - 5) == -16 * x + 9
    return by_text(ch, "−16x + 9")


def c05(ch):
    k = F(18 + 10 - 4, 3)
    return pick(ch, 2 * 1 - k * -1 + 10)


def c06(ch):
    zs = sorted(x for x in range(-20, 21) if x ** 3 - 4 * x ** 2 - 12 * x == 0)
    assert zs == [-2, 0, 6]
    return by_text(ch, "{−2, 0, 6}")


def c07(ch):
    return pick(ch, F(210, 35) * 150)


def c08(ch):
    return by_text(ch, "All 3,500 members of the gym")


def c09(ch):
    for x in range(0, 100):
        if 5 * x - 4 == 2 * (2 * x + 8):
            return pick(ch, 5 * x - 4)


def c10(_):
    ks = [k for k in range(-100, 101) if (4 * k - 7) + (k + 22) == 90]
    assert len(ks) == 1
    k = ks[0]
    assert 0 < 4 * k - 7 < 90 and 0 < k + 22 < 90
    assert math.isclose(math.sin(math.radians(4 * k - 7)), math.cos(math.radians(k + 22)))
    return k


CHECKS = {f'Q006-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
