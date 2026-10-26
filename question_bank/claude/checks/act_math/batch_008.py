"""Scripted recomputation for ACT Math batch 8. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F
from itertools import product
from statistics import mean, pstdev

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402


def cplx(t):
    s = t.replace('−', '-').replace(' ', '')
    if s == 'i':
        return 1j
    return complex(s.replace('i', 'j')) if 'i' in s else complex(float(s))


def c01(ch):
    return pick(ch, sum(1j ** k for k in range(1, 51)), conv=cplx, tol=1e-9)


def c02(ch):
    ks = [k for k in range(-50, 51) if 2**3 + k * 4 - 4 * 2 + 6 == 18]
    k = ks[0]
    p = lambda x: x**3 + k * x * x - 4 * x + 6
    # remainder by synthetic long division, not by the theorem
    coeffs, r = [1, k, -4, 6], 0
    for c in coeffs:
        r = r * (-1) + c
    assert r == p(-1)
    return pick(ch, r)


def c03(ch):  # find theta numerically in (pi, 3pi/2) with sin = -3/5
    lo, hi = math.pi, 1.5 * math.pi
    for _ in range(200):
        mid = (lo + hi) / 2
        if math.sin(mid) > -0.6:
            lo = mid
        else:
            hi = mid
    return pick(ch, math.sin(2 * lo), tol=1e-9)


def c04(ch):
    f = {1: 3, 2: 4, 3: 1, 4: 2}
    g = {1: 2, 2: 1, 3: 4, 4: 3}
    return pick(ch, sum(f[g[x]] == g[f[x]] for x in f))


def dist_point_line(q, a, b):
    (x0, y0), (x1, y1), (x2, y2) = q, a, b
    return abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1) / math.hypot(x2 - x1, y2 - y1)


def expr(t):
    s = t.replace('−', '-')
    s = re.sub(r'(\d+)√(\d+)', r'\1*math.sqrt(\2)', s)
    s = re.sub(r'√(\d+)', r'math.sqrt(\1)', s)
    return eval(s, {'math': math})  # noqa: S307


def c05(ch):
    return pick(ch, dist_point_line((8, 0), (0, 0), (2, 6)), conv=expr, tol=1e-9)


def c06(ch):
    for s2 in range(1, 1000):  # edge on a half-unit grid
        s = s2 / 2
        if abs(math.sqrt(3 * s * s) - 6 * math.sqrt(3)) < 1e-9:
            return pick(ch, s**3, conv=expr, tol=1e-9)
    raise ValueError


def c07(ch):
    rolls = [r for r in product(range(1, 7), repeat=2) if sum(r) == 8]
    return pick(ch, F(sum(6 in r for r in rolls), len(rolls)))


def c08(ch):
    data = [8, 16]
    assert mean(data) == 12 and pstdev(data) == 4
    new = [3 * x + 5 for x in data]
    target = (mean(new), pstdev(new))
    def parse(t):
        m = re.fullmatch(r'Mean (\d+), standard deviation (\d+)', t)
        return (float(m.group(1)), float(m.group(2)))
    return pick(ch, target, conv=parse)


def c09(ch):
    salt = 0.15 * 40
    for w2 in range(0, 80):
        w = w2 / 2
        if abs(salt / (40 - w) - 0.25) < 1e-12:
            return pick(ch, w)
    raise ValueError


def c10(ch):  # simulate minute by minute
    for m in range(0, 300):
        t = m / 60
        ana = 4 * t
        ben = 10 * max(0, t - 0.5)
        if t > 0.5 and abs(ben - ana) < 1e-9:
            h, mm = divmod(9 * 60 + m, 60)
            return pick(ch, f'{h}:{mm:02d} a.m.', conv=lambda s: s.strip())
    raise ValueError


CHECKS = {f'B008-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
