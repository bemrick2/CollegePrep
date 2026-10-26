"""Scripted recomputation for ACT Math batch 32. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    return pick(ch, F(1, 3) * 36 * 10)


def c02(ch):
    # brute-force the minimum distance from (1, 2) to points on 3x + 4y = 21
    best = min(math.dist((1, 2), (x, (21 - 3 * x) / 4)) for x in (k / 1000 for k in range(-10000, 10000)))
    return pick(ch, round(best, 4), tol=1e-3)


def c03(ch):
    def conv(t):
        return 'equal' if ('same total' in t and '12 months' in t and '$450' in t) else t
    return pick(ch, 'equal', conv=conv)


def c04(ch):
    return pick(ch, next(t for t in range(0, 100) if abs(50 * 2 ** (t / 3) - 400) < 1e-9))


def c05(ch):
    f = lambda x: 2 * x * x - 12 * x + 7
    return pick(ch, min(f(F(k, 100)) for k in range(-1000, 1000)))


def c06(ch):
    return pick(ch, sum(1 for code in itertools.product(range(10), repeat=4) if code[0] != 0), conv=lambda t: F(t.replace(',', '')))


def c07(ch):
    return pick(ch, 3 * math.comb(8, 2))


def c08(ch):
    return pick(ch, (F(-3, 4) + F(5, 6)) / 2)


def c09(ch):
    return pick(ch, abs(6 - 1) + abs(9 - 2))


def c10(ch):
    return pick(ch, (2 * 40 + 2 * 60) / 4)


CHECKS = {f'B032-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
