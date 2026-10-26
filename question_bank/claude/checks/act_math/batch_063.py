"""Scripted recomputation for ACT Math batch 63. Each check derives the answer from the stem's numbers only."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    return pick(ch, 360 // (180 - 150))


def c02(ch):
    return pick(ch, math.comb(8, 2))


def c03(ch):
    return pick(ch, round(10 / 0.574, 1), tol=1e-6)


def c04(ch):
    return pick(ch, sum(1 for x in range(-50, 51) if -3 < 2 * x + 1 <= 7))


def c05(ch):
    return pick(ch, F(4 * 4 + 3 * 3 + 2 * 3, 10))


def c06(ch):
    pts = [(0, 0), (6, 0), (6, 4), (2, 4)]
    area = abs(sum(pts[i][0] * pts[(i + 1) % 4][1] - pts[(i + 1) % 4][0] * pts[i][1] for i in range(4))) / 2
    return pick(ch, area)


def c07(ch):
    V, r = 7.0, 2.0
    h = 3 * V / (math.pi * r * r)
    assert math.isclose(math.pi * r * r * h / 3, V)
    forms = {'V/(3πr²)': V / (3 * math.pi * r * r), '3Vπr²': 3 * V * math.pi * r * r,
             '3V − πr²': 3 * V - math.pi * r * r, '3V/(πr²)': 3 * V / (math.pi * r * r)}
    hits = [k for k, v in ch.items() if math.isclose(forms[v], h)]
    assert len(hits) == 1
    return hits[0]


def c08(ch):
    ratio = (2 ** 2) * F(1, 2)
    words = {F(2): 'It is doubled.', F(1): 'It is unchanged.', F(1, 2): 'It is halved.', F(4): 'It is quadrupled.'}
    hits = [k for k, v in ch.items() if v == words[ratio]]
    assert len(hits) == 1
    return hits[0]


def c09(ch):
    roots = {0.0, 2.0, 1 + math.sqrt(3), 1 - math.sqrt(3)}
    f = lambda x: x * x - 2 * x  # noqa: E731
    assert all(abs(f(f(x))) < 1e-9 for x in roots)
    return pick(ch, len(roots))


def c10(ch):
    fav = math.comb(4, 2) * math.comb(4, 1) + math.comb(4, 3)
    return pick(ch, F(fav, math.comb(8, 3)))


CHECKS = {f'B063-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
