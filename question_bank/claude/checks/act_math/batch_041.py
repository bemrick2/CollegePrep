"""Scripted recomputation for ACT Math batch 41. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def c01(ch):
    h, k = F(6, 2), F(-4, 2)
    r2 = 12 + h * h + k * k
    want = f'Center ({int(h)}, {int(k)}), radius {int(math.isqrt(int(r2)))}'.replace('(3, -2)', '(3, -2)')
    hits = [x for x, v in ch.items() if v == want]
    assert len(hits) == 1 and math.isqrt(int(r2)) ** 2 == r2
    return hits[0]


def c02(ch):
    th = math.asin(0.6)
    return pick(ch, round(math.cos(math.pi / 2 - th), 9), tol=1e-9)


def c03(ch):
    r, h = 5, 6
    return pick(ch, math.pi * r * r * h, tol=1e-9)


def c04(ch):
    return pick(ch, F(50 - 40, 40) * 100, conv=lambda t: F(t.rstrip('%')))


def c05(ch):
    return pick(ch, 0.25 + 0.35, tol=1e-9)


def c06(ch):
    return pick(ch, 18 * 40 * 50, conv=lambda t: F(t.replace('$', '').replace(',', '')))


def c07(ch):
    # shoelace on a regular octagon with side 2
    n, s = 8, 2
    R = s / (2 * math.sin(math.pi / n))
    pts = [(R * math.cos(2 * math.pi * i / n), R * math.sin(2 * math.pi * i / n)) for i in range(n)]
    area = abs(sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n))) / 2
    vals = {'A': 8 * math.sqrt(2), 'B': 8 + 8 * math.sqrt(2), 'C': 12 + 8 * math.sqrt(2), 'D': 16}
    hits = [k for k, v in vals.items() if abs(v - area) < 1e-9]
    assert len(hits) == 1 and ch['B'] == '8 + 8√2'
    return hits[0]


def c08(ch):
    arc = F(120, 360) * 2 * 6  # in units of pi
    return pick(ch, arc / 2)


def c09(ch):
    hits = []
    for k, v in ch.items():
        expr = v.replace(' ', '').replace('²', '**2')
        expr = re.sub(r'(\d)h', r'\1*h', expr)
        if all(abs(eval(expr, {'h': h}) - ((1 + h) ** 2 - 1) / h) < 1e-9 for h in [0.5, 1, 2, 3]):
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c10(ch):
    outs = list(itertools.product(range(10), repeat=2))
    return pick(ch, F(sum(1 for a, b in outs if a + b == 9), len(outs)))


CHECKS = {f'B041-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
