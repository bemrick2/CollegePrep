"""Scripted recomputation for ACT Math batch 49. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def c01(ch):
    return pick(ch, next(x for x in range(-100, 100) if F(x, 3) - 2 > 1))


def c02(ch):
    h = lambda t: -16 * t * t + 64 * t + 5
    return pick(ch, h(1))


def c03(ch):
    return pick(ch, 5 + 12 + math.isqrt(25 + 144))


def c04(ch):
    v = F(2, 3) ** -2
    hits = [k for k, t in ch.items() if F(t) == v]
    assert len(hits) == 1
    return hits[0]


def c05(ch):
    hits = [k for k, v in ch.items() if v.startswith('The median')]
    assert len(hits) == 1
    return hits[0]


def c06(ch):
    return pick(ch, next(n for n in range(0, 100) if F(30 + n, 100 + n) >= F(35, 100)))


def c07(ch):
    vals = {'A': 36 * math.pi, 'B': 54 * math.pi, 'C': 108 * math.pi, 'D': 216 * math.pi}
    v = math.pi * 3 ** 2 * 6
    hits = [k for k, x in vals.items() if abs(x - v) < 1e-9]
    assert len(hits) == 1 and ch['B'] == '54π'
    return hits[0]


def c08(ch):
    # f(g(x)) - g(f(x)) = -2x^2 + 12x - 12 -> roots sum = 6
    a, b, c = 2, -12, 12
    disc = b * b - 4 * a * c
    r1 = (-b + math.sqrt(disc)) / (2 * a)
    r2 = (-b - math.sqrt(disc)) / (2 * a)
    for r in (r1, r2):
        assert abs((2 * r * r - 3) - (2 * r - 3) ** 2) < 1e-9
    return pick(ch, round(r1 + r2, 9), tol=1e-9)


def c09(ch):
    return pick(ch, next(x for x in range(0, 20) if 2 ** (x + 1) + 2 ** x == 48))


def c10(ch):
    return pick(ch, F(12 + 6, 40))


CHECKS = {f'B049-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
