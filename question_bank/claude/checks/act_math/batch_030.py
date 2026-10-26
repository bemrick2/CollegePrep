"""Scripted recomputation for ACT Math batch 30. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def money(t):
    return F(t.replace('$', '').replace(',', ''))


def c01(ch):
    return pick(ch, next(n for n in range(1, 200) if n > math.sqrt(150)))


def c02(ch):
    sides = [(l, w) for l in range(1, 34) for w in range(1, 34) if 2 * (l + w) == 34 and l * w == 60 and l >= w]
    return pick(ch, sides[0][0])


def c03(ch):
    return pick(ch, sum(1 for x in range(-100, 101) if 2 * x + 1 > x * x - 2))


def c04(ch):
    sols = [(a, b, c) for a in range(1, 30) for b in range(1, 30) for c in range(1, 30) if a * b == 12 and b * c == 15 and a * c == 20]
    a, b, c = sols[0]
    return pick(ch, a * b * c, conv=lambda t: F(t.replace(',', '')))


def c05(ch):
    return pick(ch, 2 * 50 / 360 * 2 * math.pi * 9)


def c06(ch):
    rest = ['c', 'd', 'e']
    return pick(ch, sum(1 for k in range(4) for _ in itertools.combinations(rest, k)))


def c07(ch):
    have, total = 200, 1000
    tp, fp = F(9, 10) * have, F(1, 10) * (total - have)
    return pick(ch, tp / (tp + fp))


def c08(ch):
    return pick(ch, F(5 - 4, 4) * 100, conv=lambda t: F(t.rstrip('%')))


def c09(ch):
    parts = (2, 3, 7)
    return pick(ch, F(840, sum(parts)) * max(parts), conv=money)


def c10(ch):
    return pick(ch, math.hypot(9, 12))


CHECKS = {f'B030-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
