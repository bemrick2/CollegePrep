"""Scripted recomputation for ACT Math batch 42. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def c01(ch):
    A = [[1, 4], [-2, 3]]
    B = [[0, 2], [5, -1]]
    return pick(ch, sum(2 * A[i][j] + B[i][j] for i in range(2) for j in range(2)))


def c02(ch):
    v = math.sin(math.radians(150))
    vals = {'A': -math.sqrt(3) / 2, 'B': -0.5, 'C': 0.5, 'D': math.sqrt(3) / 2}
    hits = [k for k, x in vals.items() if abs(x - v) < 1e-9]
    assert len(hits) == 1 and ch['C'] == '1/2'
    return hits[0]


def c03(ch):
    a, c = 4, 9  # coefficients of x^2 and y^2, both positive, unequal
    kind = 'An ellipse' if a > 0 and c > 0 and a != c else 'A circle' if a == c else 'A hyperbola'
    hits = [k for k, v in ch.items() if v == kind]
    assert len(hits) == 1
    return hits[0]


def c04(ch):
    hits = []
    for k, v in ch.items():
        x, y = (int(t) for t in v.strip('()').split(','))
        if y > 2 * x - 1 and x + y < 5:
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c05(ch):
    return pick(ch, F(1, 2 ** 3) + 1)


def c06(ch):
    target = lambda x: F(1, x) + F(1, x + 1)
    forms = {'A': lambda x: F(2, 2 * x + 1), 'B': lambda x: F(2, x * (x + 1)),
             'C': lambda x: F(2 * x + 1, x * (x + 1)), 'D': lambda x: F(x + 2, x * (x + 1))}
    hits = [k for k, f in forms.items() if all(f(x) == target(x) for x in range(1, 8))]
    assert len(hits) == 1 and ch['C'] == '(2x + 1)/(x(x + 1))'
    return hits[0]


def c07(ch):
    return pick(ch, F(1, 2) * 8 * 4)


def c08(ch):
    d1, d2 = 12, 16
    side = math.hypot(d1 / 2, d2 / 2)
    return pick(ch, (d1 * d2 / 2) / (2 * side), tol=1e-9)


def c09(ch):
    vals = {'A': lambda x: 5 * x * math.sqrt(2 * x), 'B': lambda x: 5 * x * x * math.sqrt(2 * x),
            'C': lambda x: 25 * x * math.sqrt(2 * x), 'D': lambda x: 10 * x * math.sqrt(x)}
    hits = [k for k, f in vals.items() if all(abs(f(x) - math.sqrt(50 * x ** 3)) < 1e-9 for x in [0.5, 1, 2, 3])]
    assert len(hits) == 1 and ch['A'] == '5x√(2x)'
    return hits[0]


def c10(ch):
    return pick(ch, 1 / (F(1, 20) - F(1, 60)))


CHECKS = {f'B042-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
