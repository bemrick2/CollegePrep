"""Scripted recomputation for ACT Math batch 55. Each check derives the answer from the stem's numbers only."""
import itertools
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def deg(t):
    return F(t.replace('°', ''))


def pi_coef(t):
    return F(t.replace('π', '') or 1)


def c01(ch):
    return pick(ch, F(450, 3) * 8 / 100)


def c02(ch):
    x = F(180, 5)
    return pick(ch, 4 * x, conv=deg)


def c03(ch):
    return pick(ch, F(-3, -4))


def c04(ch):
    pairs = list(itertools.permutations(range(1, 6), 2))
    return pick(ch, F(sum(1 for a, b in pairs if a % 2 == 0 and b % 2 == 0), len(pairs)))


def c05(ch):
    return pick(ch, sum(x for x in range(-50, 51) if (x + 3) ** 2 == 49))


def c06(ch):
    hits = []
    for k, v in ch.items():
        x, y = (int(s.replace('−', '-')) for s in v.strip('()').split(','))
        if (x - 2) ** 2 + (y + 1) ** 2 == 25:
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c07(ch):
    return pick(ch, 50 ** 0.5 + 18 ** 0.5)


def c08(ch):
    hits = []
    for k, v in ch.items():
        kk = F(v)
        det = kk * 6 - 2 * 3
        if det == 0 and F(5, 2) != F(7, 6):  # parallel and distinct (compare y-intercepts)
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c09(ch):
    water = F(9 * 8)
    ball = F(4, 3) * 27
    cap = F(9 * 10)
    return pick(ch, max(F(0), water + ball - cap), conv=lambda t: F(0) if t == '0' else pi_coef(t))


def c10(ch):
    d = 120
    return pick(ch, F(2 * d) / (F(d, 60) + F(d, 40)))


CHECKS = {f'B055-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
