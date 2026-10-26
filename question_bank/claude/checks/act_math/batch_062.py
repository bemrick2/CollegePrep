"""Scripted recomputation for ACT Math batch 62. Each check derives the answer from the stem's numbers only."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    return pick(ch, (F('42.50') - 30) / F('0.10'))


def c02(ch):
    return pick(ch, F(1, 2) * 8 * 15)


def c03(ch):
    return pick(ch, 2 * 3 + 4)


def c04(ch):
    return pick(ch, next(x for x in range(1, 100) if 2 * x * x - 5 == 27))


def c05(ch):
    return pick(ch, 3 * 10 - 4 - 9)


def c06(ch):
    s = 36 / 6
    return pick(ch, 6 * math.sqrt(3) / 4 * s * s)


def c07(ch):
    x = (10 + 4) // 2
    return pick(ch, x * (10 - x))


def c08(ch):
    return pick(ch, next(n for n in range(1, 1000) if math.isqrt(180 * n) ** 2 == 180 * n))


def c09(ch):
    return pick(ch, math.sqrt(10 ** 2 - (5 - 3) ** 2))


def c10(ch):
    return pick(ch, F(3, 5) * F(2, 4) * F(2, 3))


CHECKS = {f'B062-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
