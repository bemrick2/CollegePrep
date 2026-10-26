"""Scripted recomputation for ACT Math batch 3. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F
from itertools import product

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402

SUP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻', '0123456789-')


def sci(t):  # '3.0 × 10²' -> 300.0
    m = re.fullmatch(r'([\d.]+) × 10(.+)', t.strip())
    return float(m.group(1)) * 10 ** int(m.group(2).translate(SUP))


def c01(ch):
    return pick(ch, (6.0e5 * 4.0e-2) / 8.0e1, conv=sci)


def c02(ch):  # brute force the system
    sols = [a for a in range(0, 341) if 12 * a + 8 * (340 - a) == 3480]
    assert len(sols) == 1
    return pick(ch, sols[0])


def c03(ch):
    f = {3: 7}  # only known point of f
    pts = [(x, f[x + 2] - 5) for x in range(-20, 21) if x + 2 in f]
    def pt(t):
        a, b = t.strip('() ').split(',')
        return (int(a), int(b))
    return pick(ch, pts[0], conv=pt)


def c04(ch):  # solve for a, h, k with vertex max 9 through (0,5) and (4,5), by search on a grid
    sols = set()
    for h2 in range(-40, 41):  # h on a quarter grid
        h = F(h2, 4)
        if (0 - h) ** 2 == 0:
            continue
        a = F(5 - 9, 1) / (0 - h) ** 2
        if a < 0 and a * (4 - h) ** 2 + 9 == 5:
            sols.add(a * (5 - h) ** 2 + 9)
    assert len(sols) == 1, sols
    return pick(ch, sols.pop())


def c05(ch):
    sols = [(p, q) for p in range(181) for q in range(181) if p + q + 40 == 180 and p == q + 20]
    return pick(ch, sols[0][0], conv=lambda t: float(t.strip('°')))


def c06(ch):
    s = 36 / 3
    return pick(ch, math.sqrt(3) / 4 * s * s)


def c07(ch):
    return pick(ch, F(66, 114))


def c08(ch):
    return pick(ch, round((4.80 / 24 - 5.76 / 32) * 100, 6))


def c09(ch):
    return pick(ch, 68 / (1 - 0.15))


def c10(ch):
    for x2 in range(0, 200):  # half-liter grid
        x = x2 / 2
        if abs(0.10 * 6 + 0.40 * x - 0.20 * (6 + x)) < 1e-12:
            return pick(ch, x)
    raise ValueError


CHECKS = {f'B003-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
