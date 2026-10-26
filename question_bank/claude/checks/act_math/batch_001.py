"""Scripted recomputation for ACT Math batch 1. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def exp_of(text):  # 'x^(9/2)' -> 9/2, 'x^5' -> 5
    m = re.fullmatch(r'x\^\(?(−?-?\d+(?:/\d+)?)\)?', text.strip())
    return F(m.group(1).replace('−', '-'))


def c01(ch):  # (x^(3/2))^4 · x^(−1)
    return pick(ch, F(3, 2) * 4 + (-1), conv=exp_of)


def c02(ch):  # 35 + 12m <= 150, greatest whole m
    m = max(m for m in range(0, 100) if 35 + 12 * m <= 150)
    return pick(ch, m)


def c03(ch):  # 4x - 6y = 10, 6x + ky = 15 infinitely many: proportional rows
    r = F(6, 4)
    assert F(15, 10) == r, 'constants not proportional: system would have no solution'
    return pick(ch, -6 * r)


def c04(ch):
    f = lambda x: 2 * x**2 - 3 * x + 1
    return pick(ch, f(-2))


def c05(ch):
    f = lambda x: x**2 - 4
    g = lambda x: 3 * x + 1
    return pick(ch, g(f(3)))


def c06(ch):
    opp_a, hyp = 5, 13  # BC, AB
    ac = math.sqrt(hyp**2 - opp_a**2)
    return pick(ch, ac / opp_a)  # tan B = AC / BC


def c07(ch):  # r*theta = 4pi, 0.5 r^2 theta = 24pi; solve numerically over a grid of r
    for r in [x / 100 for x in range(1, 10000)]:
        theta = 4 * math.pi / r
        if 0 < theta < math.pi and abs(0.5 * r * r * theta - 24 * math.pi) < 1e-9:  # minor arc
            return pick(ch, r)
    raise ValueError('no radius found')


def c08(ch):
    return pick(ch, 6 * 15 - 5 * 13)


def c09(ch):
    return pick(ch, round(100 * 1.20 * 0.75, 9))


def c10(ch):
    rise = (1.2 - 0.3) - 0.4
    liters = 2 * 1.5 * rise * 1000
    return pick(ch, round(liters / 36))


CHECKS = {f'B001-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
