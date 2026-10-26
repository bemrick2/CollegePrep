"""Scripted recomputation for ACT Math batch 56. Each check derives the answer from the stem's numbers only."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def pi_coef(t):
    return F(t.replace('π', '') or 1)


def c01(ch):
    return pick(ch, (F(5, 2) * 4) / (F(1, 2) ** 2))


def c02(ch):
    hits = []
    for k, v in ch.items():
        a, b = v.replace('−', '-').replace(' ', '').split('x')
        f = lambda x: F(a) * x + F(b)  # noqa: E731
        if all(f(x) == 3 * (2 * x - 4) - 2 * (x - 5) for x in (0, 1, 7)):
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c03(ch):
    return pick(ch, 40 - F(85, 100) * 40)


def c04(ch):
    h = math.isqrt(10 ** 2 - 6 ** 2)
    return pick(ch, F(1, 3) * 36 * h, conv=pi_coef)


def c05(ch):
    return pick(ch, min(abs(F(x, 4) - 4) - 2 for x in range(-200, 200)))


def c06(ch):
    return pick(ch, (12 * 2.54) ** 2, tol=1e-4)


def c07(ch):
    m = F(-1, 2)
    return pick(ch, 3 - m * (-2))


def c08(ch):
    return pick(ch, F(20 * 10 + sum(range(1, 11)), 10))


def c09(ch):
    sq = {n * n for n in range(1, 11)}
    cu = {n ** 3 for n in range(1, 5)}
    return pick(ch, F(len(sq | cu), 100))


def c10(ch):
    f = 2
    for _ in range(10):
        f += 3
    return pick(ch, f)


CHECKS = {f'B056-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
