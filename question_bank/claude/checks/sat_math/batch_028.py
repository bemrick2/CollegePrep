"""Scripted recomputation for SAT Math batch 28. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    return next(x for x in range(-100, 101) if F(3, 4) * x - 2 == F(1, 2) * x + 3)


def c02(ch):
    return pick(ch, F(352, 32))


def c03(ch):
    assert round(3 / math.sqrt(409), 3) == 0.148
    return pick(ch, F(3, 20))


def c04(ch):
    return pick(ch, max(n for n in range(0, 20) if 11 * n <= 50))


def c05(ch):
    return by_text(ch, "y = −3x")


def c06(ch):
    sols = [x for x in range(-20, 21) if x ** 3 == -64]
    assert sols == [-4]
    return by_text(ch, "−4")


def c07(_):
    sols = [F(n, 2) for n in range(-40, 41) if abs(2 * F(n, 2) - 3) == 7]
    assert sorted(sols) == [-2, 5]
    return sum(sols)


CHECKS = {f'Q028-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07], 1)}
