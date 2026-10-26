"""Scripted recomputation for ACT Math batch 33. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def deg(t):
    return F(t.rstrip('°'))


def c01(ch):
    x = next(F(n, 2) for n in range(0, 400) if (3 * F(n, 2) + 10) + (2 * F(n, 2) + 20) == 180)
    return pick(ch, 3 * x + 10, conv=deg)


def c02(ch):
    return pick(ch, 2 * math.pi * 3 * 10)


def c03(ch):
    return pick(ch, next(F(n, 4) for n in range(-200, 200) if (2 * F(n, 4) + 3 * F(n, 4) + 4 + F(n, 4) - 1) / 3 == 9))


def c04(ch):
    a, c = F(6), F(2)
    b = 1 / (1 / c - 1 / a)
    conv = lambda t: eval(t.replace('−', '-').replace('ac', '(a*c)').replace(')(', ')*('), {'__builtins__': {}}, {'a': a, 'c': c})  # noqa: S307
    return pick(ch, b, conv=conv)


def c05(ch):
    n = next(n for n in range(1, 500) if 4 + 3 * (n - 1) == 100)
    return pick(ch, n, conv=lambda t: int(t.split()[-1]))


def c06(ch):
    people = 'ABCDEF'
    seen = set()
    for p in itertools.permutations(people):
        # canonical rotation: start at A
        k = p.index('A')
        seen.add(p[k:] + p[:k])
    adj = sum(1 for s in seen if abs(s.index('A') - s.index('B')) in (1, 5))
    return pick(ch, adj)


def c07(ch):
    flips = list(itertools.product('HT', repeat=3))
    return pick(ch, F(sum(1 for f in flips if f.count('H') >= 2), 8))


def c08(ch):
    return pick(ch, sum(1 for n in range(51, 70) if all(n % d for d in range(2, int(n ** 0.5) + 1))))


def c09(ch):
    return pick(ch, 15 * (44 / 2.2), tol=1e-6)


def c10(ch):
    tax = F(10, 100) * 10000 + F(20, 100) * (25000 - 10000)
    return pick(ch, tax / 25000 * 100, conv=lambda t: F(t.rstrip('%')))


def c11(ch):
    return pick(ch, (2 * 40 + 2 * 60) / 4)


CHECKS = {f'B033-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 12)}
