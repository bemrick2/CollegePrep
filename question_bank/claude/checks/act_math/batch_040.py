"""Scripted recomputation for ACT Math batch 40. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def poly_pick(ch, f, var='x'):
    hits = []
    for k, v in ch.items():
        expr = v.split('=')[-1].replace(' ', '').replace('²', '**2').replace('³', '**3')
        expr = re.sub(r'(\d)([a-z(])', r'\1*\2', expr)
        expr = re.sub(r'\)\(', ')*(', expr)
        if all(abs(eval(expr, {var: t}) - f(t)) < 1e-9 for t in range(-4, 5)):
            hits.append(k)
    assert len(hits) == 1, hits
    return hits[0]


def c01(ch):
    return poly_pick(ch, lambda x: 5 - 2 * (3 - 4 * x) + x)


def c02(ch):
    f = [2, 6, 12, 20]
    d = [b - a for a, b in zip(f, f[1:])]
    nxt = f[-1] + d[-1] + (d[-1] - d[-2])
    return pick(ch, nxt)


def c03(ch):
    l, w, h = 3, 4, 5
    return pick(ch, 2 * (l * w + l * h + w * h))


def c04(ch):
    g = math.gcd(12, 18)
    want = f'{g}x²y'
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1
    return hits[0]


def c05(ch):
    return pick(ch, next(x for x in range(0, 181) if x + 3 * x - 20 == 180))


def c06(ch):
    return pick(ch, F(3, 8) * 2 * 4)


def c07(ch):
    p = [0.5, 0.6, 0.7]
    tot = 0
    for bits in itertools.product([0, 1], repeat=3):
        if sum(bits) >= 2:
            pr = 1
            for b, q in zip(bits, p):
                pr *= q if b else 1 - q
            tot += pr
    return pick(ch, round(tot, 10), tol=1e-9)


def c08(ch):
    k = F(20, 5)
    return pick(ch, 3 * k * 4 * k)


def c09(ch):
    return pick(ch, next(n for n in range(1, 10000) if F(2000 + 3 * n, n) == 5), conv=lambda t: F(t.replace(',', '')))


def c10(ch):
    t = next(F(k, 7 * 8 * 15) for k in range(1, 10000) if 1 - F(k, 840) / 5 == 2 * (1 - F(k, 840) / 3))
    return pick(ch, t)


CHECKS = {f'B040-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
