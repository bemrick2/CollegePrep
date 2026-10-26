"""Scripted recomputation for ACT Math batch 48. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def c01(ch):
    target = lambda w: 2 * (w + 2 * w + 3)
    hits = []
    for k, v in ch.items():
        expr = re.sub(r'(\d)w', r'\1*w', v.replace(' ', ''))
        if all(eval(expr, {'w': w}) == target(w) for w in range(1, 6)):
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c02(ch):
    f = {1: 4, 3: 7, 5: 2, 7: 9}
    inv = {v: k for k, v in f.items()}
    return pick(ch, inv[7])


def c03(ch):
    r1, r2 = 3, 5
    hits = [k for k, v in ch.items() if v.replace(' ', '') == f'{r1}:{r2}']
    assert len(hits) == 1
    return hits[0]


def c04(ch):
    hits = [k for k, v in ch.items() if F(v) == F('0.375')]
    assert len(hits) == 1
    return hits[0]


def c05(ch):
    d = sorted([3, 8, 8, 10, 12, 15])
    return pick(ch, F(d[2] + d[3], 2))


def c06(ch):
    return pick(ch, math.ceil(F(400) / F(25, 2)))


def c07(ch):
    ang = 60  # chord = radius gives an equilateral triangle
    assert abs(2 * 10 * math.sin(math.radians(ang / 2)) - 10) < 1e-9
    vals = {'A': 10, 'B': 10 * math.pi / 3, 'C': 5 * math.pi, 'D': 20 * math.pi / 3}
    target = ang / 360 * 2 * math.pi * 10
    hits = [k for k, v in vals.items() if abs(v - target) < 1e-9]
    assert len(hits) == 1 and ch['B'] == '10π/3'
    return hits[0]


def c08(ch):
    disc = F(1, 2) / 3 * 100
    return pick(ch, round(disc), conv=lambda t: F(t.rstrip('%')))


def c09(ch):
    x = F(14 - 6, 2)
    y = 6 - x
    return pick(ch, x * y)


def c10(ch):
    g = lambda x: (x + 2) * (x - 4) + 3
    xs = [k / 1000 for k in range(-10000, 10001)]
    signs = 0
    for a, b in zip(xs, xs[1:]):
        if g(a) == 0 or g(a) * g(b) < 0:
            signs += 1
    return pick(ch, signs)


CHECKS = {f'B048-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
