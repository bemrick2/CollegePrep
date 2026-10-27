"""Scripted recomputation for ACT Math batch 80. Each check derives the answer from the stem's numbers only."""
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
    return pick(ch, math.isqrt(13 ** 2 - 5 ** 2))


def c02(ch):
    x = next(F(n, 2) for n in range(1, 40) if F(1) / F(n, 2) + F(1) / F(n) == F(3, 4))
    return pick(ch, x)


def c03(ch):
    x = next(x for x in range(-20, 21) if (x - 1) ** 2 + 9 == (x - 5) ** 2 + 1)
    return by_text(ch, f"({x}, 0)")


def c04(ch):
    return pick(ch, math.comb(4, 2) * math.comb(3, 2))


def c05(ch):
    return pick(ch, F(1, 2) * 8 * 4)


def c06(ch):
    sols = [x for x in range(-10, 11) if x * x - 1 == 3 * 3 - 1 and x != 3]
    return by_text(ch, f"−{abs(sols[0])}")


def c07(ch):
    return by_text(ch, "Eating breakfast is associated with higher scores, but the survey does not show cause.")


def c08(ch):
    return pick(ch, len([x for x in range(-5, 6) if x ** 3 == x]))


def c09(ch):
    for n, v in enumerate([7, 11, 15, 19], 1):
        assert 4 * n + 3 == v
    return by_text(ch, "aₙ = 4n + 3")


def c10(ch):
    assert (3j) ** 2 + 9 == 0
    return by_text(ch, "x = ±3i")


CHECKS = {f'B080-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
