"""Scripted recomputation for ACT Math batch 44. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def lin(t):
    t = t.replace(' ', '')
    m = re.fullmatch(r'(\d*)x([+-]\d+)', t)
    a = int(m.group(1) or 1)
    b = int(m.group(2))
    return a, b


def c01(ch):
    hits = []
    for k, v in ch.items():
        a, b = lin(v)
        root = F(-b, a)
        if 2 * root ** 2 + 7 * root + 3 == 0:
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c02(ch):
    return pick(ch, round(5 * 0.8 ** 400 + 2, 9), tol=1e-6)


def c03(ch):
    return pick(ch, F(30, 50))


def c04(ch):
    tests = [(m, n) for m in (1, 3, 5, -7) for n in (0, 2, 4, -6)]
    exprs = {'A': lambda m, n: m * n, 'B': lambda m, n: m + n, 'C': lambda m, n: 2 * m, 'D': lambda m, n: n * n}
    hits = [k for k, f in exprs.items() if all(f(m, n) % 2 == 1 for m, n in tests)]
    assert len(hits) == 1
    return hits[0]


def c05(ch):
    return pick(ch, F(35, 100) * 360, conv=lambda t: F(t.rstrip('°')))


def c06(ch):
    return pick(ch, math.sqrt(50) * math.sqrt(2), tol=1e-9)


def c07(ch):
    return pick(ch, math.pi * 8 ** 2 * 6 / 3, tol=1e-9)


def c08(ch):
    roots = set()
    for k in range(-1000, 1001):
        x = F(k, 100)
        if x ** 4 - 5 * x ** 2 + 4 == 0:
            roots.add(x)
    return pick(ch, sum(r for r in roots if r > 0))


def c09(ch):
    f = lambda x: 2 * x + 1
    return pick(ch, f(f(f(1))))


def c10(ch):
    v = F(300, 25 - 10)
    return pick(ch, 10 * v)


CHECKS = {f'B044-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
