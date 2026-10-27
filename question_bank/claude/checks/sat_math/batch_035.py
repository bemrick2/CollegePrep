"""Scripted recomputation for SAT Math batch 35. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    d = F('2.40')
    h = F(5 - 2, 3 - 1) * d  # 3h + 2d = h + 5d
    return pick(ch, float(h))


def c02(_):
    sols = [m for m in (F(n, 4) for n in range(-80, 81)) if m * (8 - 6) + 4 == 0]
    assert sols == [-2]
    return F(-2)


def c03(_):
    w = next(w for w in range(0, 100) if 200 + 15 * w > 2 * (350 - 10 * w))
    assert 350 - 10 * w > 0
    return F(w)


def c04(_):
    n = next(n for n in range(1, 1000) if 12 * n + 40 == 14 * n - 26)
    return F(12 * n + 40)


def c05(ch):
    pts = []
    for k in (0, 1, 4, -3):
        b, c = -2 * k, k * k + 2 * k - 8
        vx = F(-b, 2)
        pts.append((vx, vx * vx + b * vx + c))
    lines = {'y = 2x − 8': (2, -8), 'y = −2x + 8': (-2, 8), 'y = x − 8': (1, -8), 'y = 2x': (2, 0)}
    hits = [t for t, (m, q) in lines.items() if all(y == m * x + q for x, y in pts)]
    assert len(hits) == 1
    return [k for k, v in ch.items() if v == hits[0]][0]


def c06(_):
    return F(str(round((math.sqrt(2) - 1) * 100, 1)))


def c07(ch):
    r = 3 + math.sqrt(5)
    return pick(ch, round(-(r * r - 6 * r), 9))


def c08(_):
    x = next(x for x in range(0, 295) if F(x, x + 66) == F(45, 100))
    assert x + 66 + 48 + 126 == 294
    return F(x, x + 48)


def c09(ch):
    lo, hi = max(54 - 4, 46 - 5), min(54 + 4, 46 + 5)
    hits = [k for k, v in ch.items() if lo <= float(v.rstrip('%')) <= hi]
    assert len(hits) == 1
    return hits[0]


def c10(ch):
    d = math.sqrt(10 ** 2 - 6 ** 2)
    return pick(ch, math.hypot(6, 10 - d))


CHECKS = {f'Q035-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
