"""Scripted recomputation for ACT Math batch 35. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def c01(ch):
    ad, db, de = 4, 6, 5
    return pick(ch, F(de) * (ad + db) / ad)


def c02(ch):
    p, q = [-3, 2], [-1, 4, 1]  # coefficients, lowest degree first
    prod = [0] * 4
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            prod[i + j] += a * b
    return pick(ch, prod[1])


def c03(ch):
    f = lambda x: x * x - 3 * x
    sup = str.maketrans('²', '2')
    hits = []
    for k, v in ch.items():
        expr = v.replace('a²', 'a**2').replace(' ', '')
        if all(eval(expr, {'a': a}) == f(a + 2) for a in range(-5, 6)):
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c04(ch):
    sup = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789')
    order = sorted([(2, 30), (3, 20), (5, 10)], key=lambda t: t[0] ** t[1])
    want = ', '.join(f'{b}{str(e).translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))}' for b, e in order)
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1
    return hits[0]


def c05(ch):
    return pick(ch, F(5, 8) ** 2)


def c06(ch):
    x = F(180 - 20, 8)
    return pick(ch, max(3 * x + 20, 5 * x), conv=lambda t: F(t.rstrip('°')))


def c07(ch):
    t = F(330, 50 + 60)
    return pick(ch, 60 * t)


def c08(ch):
    hits = set()
    for a in range(1, 10):
        for b in range(-20, 21):
            if a * a == 4 and a * b + b == 9:
                hits.add(a + b)
    assert len(hits) == 1
    return pick(ch, hits.pop())


def c09(ch):
    n = 5
    return pick(ch, sum(1 for x, y, z in itertools.product(range(n), repeat=3)
                        if sum(c in (0, n - 1) for c in (x, y, z)) == 2))


def c10(ch):
    return pick(ch, math.hypot(16, 12))


CHECKS = {f'B035-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
