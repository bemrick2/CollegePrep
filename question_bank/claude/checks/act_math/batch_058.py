"""Scripted recomputation for ACT Math batch 58. Each check derives the answer from the stem's numbers only."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402


def pi_expr(t):
    """'36π − 72' or '144 − 36π' -> float."""
    a, b = t.replace('−', '-').split(' - ')
    return num(a) - num(b)


def c01(ch):
    return pick(ch, F(23915 - 23480, 15))


def c02(ch):
    return pick(ch, 36 / 4 * math.sqrt(2))


def c03(ch):
    return pick(ch, next(x for x in range(-100, 101) if 2 * x - 7 == 3 * x + 4))


def c04(ch):
    g = -1 + 3
    return pick(ch, F(2) ** g)


def c05(ch):
    return pick(ch, F(6 * 5 * 4, 6 ** 3))


def c06(ch):
    return pick(ch, math.dist((1, 2), (7, 10)) / 2)


def c07(ch):
    v = (2 + 1j) * (2 - 1j) + 1j * 1j
    return pick(ch, v.real)


def c08(ch):
    return pick(ch, 20 ** 2 - 2 * 91)


def c09(ch):
    side = 12 / math.sqrt(2)
    return pick(ch, math.pi * 36 - side ** 2, conv=pi_expr)


def c10(ch):
    return pick(ch, F(86 - 70, 8))


CHECKS = {f'B058-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
