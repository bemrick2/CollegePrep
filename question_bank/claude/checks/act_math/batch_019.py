"""Scripted recomputation for ACT Math batch 19. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def expr(t):
    s = t.replace('−', '-')
    s = re.sub(r'(\d+)√(\d+)', r'\1*math.sqrt(\2)', s)
    s = re.sub(r'√(\d+)', r'math.sqrt(\1)', s)
    return eval(s, {'math': math})  # noqa: S307


def c01(ch):
    return pick(ch, abs(3 - 4j) * abs(1 + 1j), conv=expr, tol=1e-9)


def c02(ch):
    return pick(ch, pow(7, 100, 10))


def sset(t):
    if t == 'The empty set':
        return frozenset()
    return frozenset(F(x.strip().replace('−', '-')) for x in t.strip('{} ').split(','))


def c03(ch):
    sols = frozenset(F(n, 4) for n in range(-400, 401) if abs(F(n, 4) - 4) == 2 * F(n, 4) + 1)
    return pick(ch, sols, conv=sset)


def c04(ch):
    m = 3  # slope of 3x - y = 4 read by solving for y at two points
    y = lambda x: 3 * x - 4
    m = (y(1) - y(0)) / 1
    b = -1 - m * 2
    return pick(ch, F(-b) / F(m))


def c05(ch):
    n = 120000
    hours = sum(1 for i in range(n) if 3 * math.sin(math.pi * (i + .5) * 12 / n / 6) + 5 > 6.5) * 12 / n
    return pick(ch, round(hours, 2), tol=1e-3)


def c06(ch):
    b = next(b / 100 for b in range(1, 1000) if abs(200 * (b / 100) ** 3 - 1600) < 1e-6)
    return pick(ch, b)


def c07(ch):
    (x1, y1), (x2, y2), (x3, y3) = (1, 1), (5, 4), (-2, 6)
    # area by Monte-Carlo-free exact lattice: Pick's-free approach via integration over a fine grid of cell centers
    n = 1400
    xs = [-2 + (i + .5) * 7 / n for i in range(n)]
    ys = [1 + (j + .5) * 5 / n for j in range(n)]
    def inside(px, py):
        d1 = (px - x2) * (y1 - y2) - (x1 - x2) * (py - y2)
        d2 = (px - x3) * (y2 - y3) - (x2 - x3) * (py - y3)
        d3 = (px - x1) * (y3 - y1) - (x3 - x1) * (py - y1)
        neg = d1 < 0 or d2 < 0 or d3 < 0
        pos = d1 > 0 or d2 > 0 or d3 > 0
        return not (neg and pos)
    cnt = sum(1 for x in xs for y in ys if inside(x, y))
    area = cnt * (7 / n) * (5 / n)
    return pick(ch, round(area, 1), tol=1e-2)


def c08(ch):
    return pick(ch, (8 - 2) * 180 / 8, conv=lambda t: float(t.rstrip('°')))


def c09(ch):
    p = next(p / 100 for p in range(0, 101) if abs(0.4 + p / 100 - 0.4 * p / 100 - 0.7) < 1e-12)
    return pick(ch, p)


def c10(ch):
    return pick(ch, 2.5 * 100 * 100)


CHECKS = {f'B019-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
