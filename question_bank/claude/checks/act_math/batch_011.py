"""Scripted recomputation for ACT Math batch 11. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def is_cube(m):
    r = round(m ** (1 / 3))
    return any((r + d) ** 3 == m for d in (-1, 0, 1))


def c01(ch):
    return pick(ch, next(n for n in range(1, 10000) if is_cube(12 * n)))


def c02(ch):
    sols = [(s, 30 - s) for s in range(-100, 101) if 30 - s == 2 * s + 3]
    return pick(ch, sols[0][1])


def c03(ch):
    a = math.log(3, 2)
    b = math.log(16, 3)
    return pick(ch, round(a * b, 9), tol=1e-6)


def c04(ch):
    f = lambda x: -2 * (x + 1) ** 2 + 5
    xs = [i / 100 for i in range(-1000, 1000)]
    xmax = max(xs, key=f)
    target = f'It has a maximum value of {round(f(xmax))} at x = {round(xmax)}.'.replace('-', '−')
    return pick(ch, target, conv=lambda t: t)


def c05(ch):
    f = lambda x: 2 * x + 3
    hits = []
    for k, v in ch.items():
        m = re.fullmatch(r'g\(x\) = (\d+)x − (\d+)', v)
        g = lambda x, a=int(m.group(1)), b=int(m.group(2)): a * x - b
        if all(f(g(x)) == 6 * x - 5 for x in range(-5, 6)):
            hits.append(k)
    assert len(hits) == 1, hits
    return hits[0]


def c06(ch):
    over = (16 - 10) / 2
    h = math.sqrt(5 * 5 - over * over)
    return pick(ch, (10 + 16) / 2 * h)


def c07(ch):  # integrate cross-sections of a cone of height 1, radius 1 numerically
    n = 200000
    dz = 1 / n
    vol = lambda a, b: sum(math.pi * ((i + .5) * dz) ** 2 * dz for i in range(int(a * n), int(b * n)))
    whole = vol(0, 1)
    bottom = vol(0.5, 1)  # radius grows linearly from the vertex at z=0
    return pick(ch, bottom / whole, tol=1e-4)


def c08(ch):
    pa, pb = F(1, 3), F(1, 4)
    return pick(ch, pa * (1 - pb) + (1 - pa) * pb)


def c09(ch):
    known = [3, 5, 7, 7, 8, 10, 12, 15]
    sols = []
    for x in range(-200, 201):
        lst = sorted(known + [x])
        if F(sum(lst), 9) == lst[4]:
            sols.append(x)
    assert len(sols) == 1, sols
    return pick(ch, sols[0])


def c10(ch):
    return pick(ch, 18 * 60 / 12)


CHECKS = {f'B011-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
