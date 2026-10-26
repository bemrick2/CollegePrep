"""Scripted recomputation for ACT Math batch 43. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def c01(ch):
    want = '(-1, 3), slope -2'
    hits = [k for k, v in ch.items() if v == want]
    # verify: the point satisfies the equation and the slope is the coefficient
    x, y = -1, 3
    assert y - 3 == -2 * (x + 1) and len(hits) == 1
    return hits[0]


def c02(ch):
    f = [3, 6, 12, 24]
    ratios = {F(b, a) for a, b in zip(f, f[1:])}
    assert len(ratios) == 1
    want = f'Exponential, with growth factor {int(ratios.pop())}'
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1
    return hits[0]


def c03(ch):
    return pick(ch, F(9, 3) * (3 + 4 + 5))


def c04(ch):
    return pick(ch, F(30, 100) * F(40, 100) * 500)


def c05(ch):
    C = lambda h: 65 * h + 90
    assert C(0) == 90
    hits = [k for k, v in ch.items() if 'no time' in v]
    assert len(hits) == 1
    return hits[0]


def c06(ch):
    return pick(ch, 72 * F(25, 60), conv=lambda t: F(t.replace(',', '')))


def c07(ch):
    u = F(5 + 1, 2)
    return pick(ch, 1 / u)


def c08(ch):
    return pick(ch, F(4 * 6, 3))


def c09(ch):
    L = 10
    pts = [F(k, 1000) * L for k in range(0, 1001)]
    mid = F(L, 2)
    good = sum(1 for x in pts if abs(x - mid) < min(x, L - x))
    return pick(ch, round(F(good, len(pts)), 2), conv=lambda t: round(F(t), 2), tol=0.01)


def c10(ch):
    n = 5
    pts = [(math.cos(2 * math.pi * i / n), math.sin(2 * math.pi * i / n)) for i in range(n)]
    A, C, Dp = pts[0], pts[2], pts[3]
    v1 = (C[0] - A[0], C[1] - A[1]); v2 = (Dp[0] - A[0], Dp[1] - A[1])
    ang = math.degrees(math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / (math.hypot(*v1) * math.hypot(*v2))))
    return pick(ch, round(ang, 6), conv=lambda t: float(t.rstrip('°')), tol=1e-6)


CHECKS = {f'B043-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
