"""Scripted recomputation for ACT Math batch 68. Each check derives the answer from the stem's numbers only."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402

SUP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻', '0123456789-')


def sci(t):
    c, e = t.split(' × 10')
    return float(c) * 10 ** int(e.translate(SUP))


def c01(ch):
    return pick(ch, 120 / 2400 * 100, conv=lambda t: float(t.rstrip('%')))


def c02(ch):
    return pick(ch, (6 // 2) * (8 // 2) * (10 // 2))


def c03(ch):
    x = next(x for x in range(-50, 51) if 3 * x + 2 == 5 * x - 6)
    return pick(ch, 3 * x + 2)


def c04(ch):
    block = '142857'
    return pick(ch, int(block[(100 - 1) % 6]))


def c05(ch):
    return pick(ch, F(math.comb(4, 2) + math.comb(6, 2), math.comb(10, 2)))


def c06(ch):
    return pick(ch, round(1 - (5 / 6) ** 4, 3))


def c07(ch):
    return pick(ch, F(9, 5) * 180 + 32)


def c08(ch):
    # Verify the relation numerically on a concrete rectangle, then solve.
    import random
    random.seed(1)
    for _ in range(5):
        w, h, x, y = 10.0, 7.0, random.uniform(0, 10), random.uniform(0, 7)
        pa, pb, pc, pd = (x ** 2 + y ** 2), ((w - x) ** 2 + y ** 2), ((w - x) ** 2 + (h - y) ** 2), (x ** 2 + (h - y) ** 2)
        assert math.isclose(pa + pc, pb + pd)
    return pick(ch, math.sqrt(9 + 25 - 16), conv=num)


def c09(ch):
    return pick(ch, 6 ** 3 - 3 * 4 * 6)


def c10(ch):
    return pick(ch, 0.000045, conv=sci, tol=1e-12)


CHECKS = {f'B068-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
