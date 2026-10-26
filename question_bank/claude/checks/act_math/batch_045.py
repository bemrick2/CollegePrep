"""Scripted recomputation for ACT Math batch 45. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def c01(ch):
    target = lambda n: 4 * (n + 3) - 5
    hits = []
    for k, v in ch.items():
        expr = re.sub(r'(\d)\(', r'\1*(', v.replace(' ', ''))
        expr = re.sub(r'(\d)n', r'\1*n', expr)
        if all(eval(expr, {'n': n}) == target(n) for n in range(-3, 4)):
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c02(ch):
    mg, bg = F(10 - 2, 2 - 0), 2
    mf, bf = 3, -4
    assert mg > mf and bg > bf
    hits = [k for k, v in ch.items() if v.startswith('g has the greater slope and the greater')]
    assert len(hits) == 1
    return hits[0]


def c03(ch):
    return pick(ch, 720 - (120 + 130 + 110 + 125 + 115), conv=lambda t: F(t.rstrip('°')))


def c04(ch):
    return pick(ch, sum(1 for n in range(0, 300) if n * n > 20 and n * n < 200))


def c05(ch):
    return pick(ch, sum(1 for _ in itertools.combinations(range(6), 2)))


def c06(ch):
    return pick(ch, F(420, 30 * 2))


def c07(ch):
    return pick(ch, F(6, 15) * 50)


def c08(ch):
    pairs = [(a, b) for a in range(-20, 21) for b in range(-20, 21) if a + b == 7 and a * b == 12 and a > b]
    assert len(pairs) == 1
    a, b = pairs[0]
    return pick(ch, a - b)


def c09(ch):
    good = sum(1 for n in range(100, 1000) if len(set(str(n))) == 3)
    return pick(ch, F(good, 900))


def c10(ch):
    d = abs(6 - 1) / math.sqrt(2 ** 2 + 1)
    return pick(ch, d, tol=1e-9)


CHECKS = {f'B045-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
