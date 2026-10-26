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
    return pick(ch, F(25 - 4, 3))


def c04(ch):
    return pick(ch, next(x for x in range(1, 100) if 2 * x * x - 5 == 27))


def c05(ch):
    return pick(ch, 3 * 10 - 4 - 9)


def c06(ch):
    r = math.isqrt(100 // 4)
    return pick(ch, F(4, 3) * r ** 3, conv=lambda t: F(t.replace('π', '') or 1) if '/' not in t else F(t.replace('π', '')))


def c07(ch):
    x = (10 + 4) // 2
    return pick(ch, x * (10 - x))


def c08(ch):
    return pick(ch, sum(n for n in range(1, 100) if n % 3 == 0))


def c09(ch):
    return pick(ch, next(s for s in range(1, 200) if 12 * 72 + 81 * s == 78 * (12 + s)))


def c10(ch):
    return pick(ch, F(math.comb(5, 4) + math.comb(5, 5), 2 ** 5))


CHECKS = {f'B062-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
