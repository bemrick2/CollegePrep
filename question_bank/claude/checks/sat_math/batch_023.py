"""Scripted recomputation for SAT Math batch 23. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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


def d01(_):
    x = F(20 - 2, 4)
    return max(x, 2 * x, x + 2)


def d02(ch):
    r = next(F(n, 10) for n in range(0, 36) if 6 * F(n, 10) + 3 * (F(35, 10) - F(n, 10)) == 15)
    return pick(ch, r)


def d03(ch):
    return pick(ch, next(k for k in range(-20, 21) if (4 - 2) * (4 + k) == 12))


def d04(ch):
    x = next(x for x in range(-10, 0) if x * x - 9 == 0)
    return pick(ch, 5 - x)


def d05(ch):
    v = 4 ** 1.5
    assert math.isclose(v, 8)
    return pick(ch, 8)


def d06(ch):
    for x in (1, 2, 5):
        assert x * x + 7 * x + 12 == (x + 4) * (x + 3)
    return by_text(ch, "x + 3")


def d07(_):
    side = F(3 * 8, 4)
    return side ** 2


def d08(ch):
    d = math.isqrt(5 ** 2 - 4 ** 2)
    return pick(ch, F(8 * d, 2))


CHECKS = {f'Q023-{i:02d}': f for i, f in enumerate([d01, d02, d03, d04, d05, d06, d07, d08], 1)}
