"""Scripted recomputation for ACT Math batch 20. Each check derives the answer from the stem's numbers only."""
import math
import os
import random
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    return pick(ch, (4e-3) ** 2 / 2e-5, tol=1e-9)


def c02(ch):
    bs = []
    for r in range(1, 25):
        for s in range(r, 25):
            if r * s == 24:
                bs.append(-(r + s))
    return pick(ch, max(bs))


def c03(ch):
    expr = lambda x, y: (2 * x ** 3 * y) ** 2 * 3 * x * y ** -4
    hits = []
    for k, v in ch.items():
        m = re.fullmatch(r'(\d+)x(\S)(?:/y(\S)|y⁻(\S))', v)
        sup = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789')
        coef, xe = int(m.group(1)), int(m.group(2).translate(sup))
        ye = -int((m.group(3) or m.group(4)).translate(sup))
        if all(abs(coef * x ** xe * y ** ye - expr(x, y)) < 1e-6 * abs(expr(x, y)) for x, y in ((1.5, 2.0), (2.0, 0.5), (3.0, 1.7))):
            hits.append(k)
    assert len(hits) == 1, hits
    return hits[0]


def c04(ch):
    zeros = sorted(x for x in range(-20, 21) if 2 * x * x - 8 == 0)
    label = {(2,): '2 only', (4,): '4 only', (-2, 2): '−2 and 2', (-4, 4): '−4 and 4'}
    return pick(ch, label[tuple(zeros)], conv=lambda t: t)


def c05(ch):  # coordinates: D=(0,0), C=(15,0), A=(a,h), B=(a+6,h); choose a,h so AC = 14, intersect diagonals
    h = 5.0
    # solve a from |AC| = 14: (15 - a)^2 + h^2 = 196
    a = 15 - math.sqrt(196 - h * h)
    A, B, C, D = (a, h), (a + 6, h), (15.0, 0.0), (0.0, 0.0)
    # intersection of AC and BD
    def inter(p1, p2, p3, p4):
        x1, y1 = p1; x2, y2 = p2; x3, y3 = p3; x4, y4 = p4
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
        return px, py
    E = inter(A, C, B, D)
    return pick(ch, math.dist(A, E), tol=1e-9)


def c06(ch):
    h = math.sqrt(5 ** 2 - 3 ** 2)
    return pick(ch, math.pi * 9 * h / 3, conv=lambda t: float(t.rstrip('π')) * math.pi, tol=1e-9)


def c07(ch):
    rng = random.Random(20)
    n, hit = 400000, 0
    tot = 0
    while tot < n:
        x, y = rng.uniform(-6, 6), rng.uniform(-6, 6)
        r = math.hypot(x, y)
        if r <= 6:
            tot += 1
            hit += 2 <= r < 4
    exact = (16 - 4) / 36
    assert abs(hit / n - exact) < 0.01
    return pick(ch, F(12, 36))


def c08(ch):
    from statistics import pstdev
    from _util import num
    base = [10, 12, 14, 16, 18]
    s0 = pstdev(base)
    hits = [k for k, v in ch.items() if pstdev(base + [num(v)]) < s0]
    assert len(hits) == 1, hits
    return hits[0]


def c09(ch):
    m = next(m for m in range(0, 1000) if 40 + 0.25 * m < 25 + 0.40 * m - 1e-12)
    return pick(ch, m)


def c10(ch):
    n = 27 / 0.15
    return pick(ch, round(0.40 * n, 6))


CHECKS = {f'B020-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
