"""Scripted recomputation for ACT Math batch 67. Each check derives the answer from the stem's numbers only."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    return pick(ch, 1440 // 180 + 2)


def c02(ch):
    return pick(ch, 80 * F(1, 2) ** (15 // 5))


def c03(ch):
    r = math.hypot(-5, 12)
    return pick(ch, F(-5, int(r)))


def c04(ch):
    return pick(ch, 4 * 1.5)


def c05(ch):
    return pick(ch, next(x for x in range(-50, 51) if abs(x - 3) == abs(x - 7)))


def c06(ch):
    best = max(2 * x + 3 * y for x in [F(i, 4) for i in range(0, 41)] for y in [F(j, 4) for j in range(0, 41)]
               if x + y <= 6 and x + 2 * y <= 8)
    return pick(ch, best)


def c07(ch):
    n, f, p = 1023, [], 2
    while n > 1:
        while n % p == 0:
            f.append(p)
            n //= p
        p += 1
    return pick(ch, max(f))


def c08(ch):
    return pick(ch, F(1, 2) ** 3)


def c09(ch):
    # discriminant of x^2 - 2x + (3 - c) = 0 is 4 - 4(3 - c)
    return pick(ch, next(c for c in range(-20, 21) if 4 - 4 * (3 - c) == 0))


def c10(ch):
    return pick(ch, 18 - 3 * (2 + 4) ** 2 / 6)


CHECKS = {f'B067-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
