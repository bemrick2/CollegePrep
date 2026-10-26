"""Scripted recomputation for ACT Math batch 53. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def deg(t):
    return float(t.replace('°', '').replace(',', ''))


def c01(ch):
    return pick(ch, 360 / 8, conv=deg)


def c02(ch):
    xs = sorted([3, 9, 4, 15, 8])
    return pick(ch, xs[2])


def c03(ch):
    return pick(ch, 3 ** (5 + 3) / 3 ** 5)


def c04(ch):
    return pick(ch, 6 * math.sqrt(50 / 18))


def c05(ch):
    roots = [x for x in range(-50, 51) if x * x - 11 * x + 18 == 0]
    good = [x for x in roots if x - 5 >= 0 and abs(math.sqrt(x + 7) - (x - 5)) < 1e-12]
    want = ' and '.join(map(str, good)) if len(good) > 1 else f'{good[0]} only'
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1
    return hits[0]


def c06(ch):
    n = sum(1 for a, b in itertools.product(range(1, 5), repeat=2) if a + b == 5)
    return pick(ch, F(n, 16))


def c07(ch):
    return pick(ch, 2 * 4 * math.sqrt(3) / 2)


def c08(ch):
    return pick(ch, pow(7, 2026, 10))


def c09(ch):
    return pick(ch, F(30) / (F(3, 4) - F(1, 3)))


def c10(ch):
    return pick(ch, sum(1 for n in range(100, 1000) if sum(map(int, str(n))) == 5))


CHECKS = {f'B053-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
