"""Scripted recomputation for ACT Math batch 47. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def c01(ch):
    target = lambda x: 3 * x ** 2 + 2 * x - x ** 2 + 5 * x
    hits = []
    for k, v in ch.items():
        expr = v.replace(' ', '').replace('²', '**2')
        expr = re.sub(r'(\d)x', r'\1*x', expr)
        if all(eval(expr, {'x': x}) == target(x) for x in range(-3, 4)):
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c02(ch):
    return pick(ch, F(500, 25))


def c03(ch):
    x = next(F(k, 2) for k in range(0, 181) if 180 - F(k, 2) == 3 * (90 - F(k, 2)))
    return pick(ch, x, conv=lambda t: F(t.rstrip('°')))


def c04(ch):
    hits = [k for k, v in ch.items() if F(1, 3) < F(v) < F(1, 2)]
    assert len(hits) == 1
    return hits[0]


def c05(ch):
    d = [12, 7, 19, 3, 15]
    return pick(ch, max(d) - min(d))


def c06(ch):
    return pick(ch, (F(2, 6) - F(3, 12)) * 60)


def c07(ch):
    for k in range(1, 200):
        b = k / 10
        disc = (2 * b) ** 2 - 4 * 2 * (b * b - 8)
        if abs(disc) < 1e-9:
            return pick(ch, b, tol=1e-9)


def c08(ch):
    sols = [(l, 23 - l) for l in range(1, 23) if l * l + (23 - l) ** 2 == 289]
    l, w = sols[0]
    return pick(ch, l * w)


def c09(ch):
    return pick(ch, F(1, 2) * F(3, 5) + F(1, 2) * F(1, 5))


def c10(ch):
    for x in range(1, 100):
        if (1 + F(x, 100)) * (1 - F(x, 100)) == F(96, 100):
            return pick(ch, x)


CHECKS = {f'B047-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
