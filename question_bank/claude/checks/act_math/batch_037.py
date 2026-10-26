"""Scripted recomputation for ACT Math batch 37. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def pt(t):
    a, b = t.strip('()').split(',')
    return (F(a.strip()), F(b.strip()))


def c01(ch):
    return pick(ch, F(14, 10) / F(2, 10) + 5)


def c02(ch):
    xs = [F(k, 2) for k in range(-40, 41)]
    x = min(xs, key=lambda v: abs(v - 3) + 2)
    hits = [k for k, v in ch.items() if pt(v) == (x, abs(x - 3) + 2)]
    assert len(hits) == 1
    return hits[0]


def c03(ch):
    hits = []
    for k, v in ch.items():
        rhs = v.split('=')[1].replace(' ', '')
        f = lambda x: eval(re.sub(r'(\d)x', r'\1*x', rhs.replace('-(1/2)x', '-(1/2)*x')), {'x': F(x)})
        slope = f(1) - f(0)
        if slope == 2 and f(3) == 4:
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c04(ch):
    return pick(ch, sum(range(1, 50, 2)))


def c05(ch):
    return pick(ch, F(3, 3 + 5))


def c06(ch):
    A, B, C = (1, 1), (5, 2), (6, 5)
    Dv = (A[0] + C[0] - B[0], A[1] + C[1] - B[1])
    hits = [k for k, v in ch.items() if pt(v) == Dv]
    assert len(hits) == 1
    return hits[0]


def c07(ch):
    return pick(ch, sum(1 for n in range(100, 501) if n % 6 == 0))


def c08(ch):
    return pick(ch, round(63360 / (28 * math.pi)), conv=lambda t: F(t.replace(',', '')))


def c09(ch):
    ks = set()
    for k in range(-50, 51):
        disc = 25 - 4 * k
        if disc < 0:
            continue
        r = (5 + math.sqrt(disc)) / 2
        s = (5 - math.sqrt(disc)) / 2
        if abs(r * r + s * s - 13) < 1e-9:
            ks.add(k)
    assert len(ks) == 1
    return pick(ch, ks.pop())


def c10(ch):
    best = min(math.hypot(8 - 5 * math.cos(t / 10000 * 2 * math.pi), 6 - 5 * math.sin(t / 10000 * 2 * math.pi)) for t in range(10000))
    return pick(ch, round(best, 6), tol=1e-3)


CHECKS = {f'B037-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
