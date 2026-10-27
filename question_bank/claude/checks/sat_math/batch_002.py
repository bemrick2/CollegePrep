"""Scripted recomputation for SAT Math batch 2. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    a = F(15, 5)
    return pick(ch, -a + 5)


def c02(_):
    return F(9 + 15 - 2, 5 - 3)


def c03(ch):
    k = -3
    for x in range(-5, 6):
        assert 3 * (2 * x - 1) == 6 * x + k
    return pick(ch, k)


def c04(ch):
    for m in range(0, 2000, 25):
        for c in range(0, 2000, 25):
            if 3 * m + 2 * c == 1450 and 2 * m + 3 * c == 1550:
                return by_text(ch, f"${c / 100:.2f}")


def c05(ch):
    for x in (1, 2, 3.5):
        assert math.isclose(9 ** (x / 2), 3 ** x)
    return by_text(ch, "3^x")


def c06(_):
    return max(x for x in range(-20, 21) if x * x - 3 * x == x + 5)


def c07(ch):
    for x in (2, 3, 7):
        assert F(x + 5, x - 1) - F(6, x - 1) == 1
    return by_text(ch, "1")


def c08(ch):
    return by_text(ch, "Walking 30 minutes a day likely causes lower blood pressure for adults in the city.")


def c09(_):
    return F(1500, 6) * 60 / 1000


def c10(ch):
    return pick(ch, 5 * math.isqrt(13 ** 2 - 5 ** 2))


CHECKS = {f'Q002-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
