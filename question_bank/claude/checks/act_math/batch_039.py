"""Scripted recomputation for ACT Math batch 39. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def pt(t):
    a, b = t.strip('()').split(',')
    return (F(a.strip()), F(b.strip()))


def c01(ch):
    x = -2
    return pick(ch, 3 * x ** 2 - x)


def c02(ch):
    f = {1: 4, 2: 7, 3: 10}
    g = {1: 9, 2: 5, 3: 1}
    return pick(ch, f[2] + g[2])


def c03(ch):
    return pick(ch, F(180 - 40, 2), conv=lambda t: F(t.rstrip('°')))


def c04(ch):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    want = days[(days.index('Tuesday') + 100) % 7]
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1
    return hits[0]


def c05(ch):
    return pick(ch, 120 - (45 + 50 - 20))


def c06(ch):
    extra = math.ceil(F(53, 10) - 1)
    return pick(ch, F(4) + extra * F(3, 2), conv=lambda t: F(t.replace('$', '')))


def c07(ch):
    s2 = next(F(k, 100) for k in range(1, 10000) if F(k, 100) / 4 + F(k, 100) == 25)
    return pick(ch, s2)


def c08(ch):
    b = F(100)
    a = b * F(125, 100)
    return pick(ch, (a - b) / a * 100, conv=lambda t: F(t.rstrip('%')))


def c09(ch):
    P = (F(4), F(1))
    # reflect across x - y + 1 = 0
    a, b, c = 1, -1, 1
    d = (a * P[0] + b * P[1] + c) / (a * a + b * b)
    img = (P[0] - 2 * a * d, P[1] - 2 * b * d)
    hits = [k for k, v in ch.items() if pt(v) == img]
    assert len(hits) == 1
    return hits[0]


def c10(ch):
    people = [(c, s) for c in range(4) for s in range(2)]
    pairs = list(itertools.combinations(people, 2))
    return pick(ch, F(sum(1 for p, q in pairs if p[0] == q[0]), len(pairs)))


CHECKS = {f'B039-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
