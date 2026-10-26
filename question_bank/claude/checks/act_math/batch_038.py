"""Scripted recomputation for ACT Math batch 38. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def c01(ch):
    return pick(ch, next(F(k, 3) for k in range(-300, 300) if F(F(k, 3) + 2, 5) == F(F(k, 3) - 1, 2)))


def c02(ch):
    f = lambda x: -(x - 2) ** 2 + 7
    inc = [x for x in range(-20, 21) if f(x + F(1, 2)) > f(x)]
    assert max(inc) == 1 and min(inc) == -20  # increasing exactly to the left of x = 2
    return 'A' if ch['A'] == 'x < 2' else None


def c03(ch):
    return pick(ch, F(1, 2) * 10 * 14)


def c04(ch):
    minutes = round(F(24, 10) * 60)
    want = f'{minutes // 60} hours {minutes % 60} minutes'
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1
    return hits[0]


def c05(ch):
    outs = list(itertools.product(range(1, 5), repeat=2))
    return pick(ch, F(sum(1 for a, b in outs if a * b % 2 == 0), len(outs)))


def c06(ch):
    pay = lambda h: 16 * min(h, 40) + 24 * max(h - 40, 0)
    return pick(ch, next(F(h, 2) for h in range(0, 200) if pay(F(h, 2)) == 760))


def c07(ch):
    half = 5
    return pick(ch, half ** 2 * math.pi, tol=1e-9)


def c08(ch):
    return pick(ch, sum(1 for t in itertools.product(range(6), repeat=3) if sum(t) == 5))


def c09(ch):
    s = 12
    area = math.sqrt(3) / 4 * s * s
    return pick(ch, area / (3 * s / 2), tol=1e-9)


def c10(ch):
    t = F(300, 30 + 45)
    return pick(ch, 45 * t)


CHECKS = {f'B038-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
