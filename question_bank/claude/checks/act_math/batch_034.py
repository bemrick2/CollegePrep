"""Scripted recomputation for ACT Math batch 34. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def frac(t):
    return F(t.replace(' ', ''))


def point_x(t):
    return F(t.strip('()').split(',')[0].strip())


def c01(ch):
    m = -F(3, 4)  # negative reciprocal of the radius slope 4/3
    return pick(ch, 3 - F(4) / m, conv=point_x)


def c02(ch):
    return pick(ch, min((x - 2) * (x - 8) for x in [F(k, 10) for k in range(0, 101)]), conv=frac)


def c03(ch):
    return pick(ch, next(n for n in range(1, 50) if 3 ** n > 1000))


def c04(ch):
    s = str(math.factorial(25))
    return pick(ch, len(s) - len(s.rstrip('0')))


def c05(ch):
    return pick(ch, next(x for x in range(0, 100) if F(10 + x, 2) == 16))


def c06(ch):
    f = lambda x: -2 * x ** 3 + 5 * x ** 2 + 1
    big, small = f(10 ** 6) > 0, f(-10 ** 6) > 0
    text = {(False, True): 'B', (True, True): 'A', (True, False): 'C', (False, False): 'D'}[(big, small)]
    return text


def c07(ch):
    return pick(ch, sum(1 for _ in itertools.permutations(range(8), 3)))


def c08(ch):
    cost = lambda mpg: F(12000, mpg) * F(7, 2)
    return pick(ch, cost(25) - cost(40), conv=lambda t: F(t.replace('$', '').replace(',', '')))


def c09(ch):
    total, h = F(10), F(10)
    for _ in range(200):
        h *= F(3, 5)
        total += 2 * h
    return pick(ch, float(total), tol=1e-6)


def c10(ch):
    months = list(itertools.product(range(12), repeat=3))
    return pick(ch, F(sum(1 for m in months if len(set(m)) < 3), len(months)), conv=frac)


def c11(ch):
    s = 2
    r_in, r_out = F(s, 2), math.sqrt(2) * s / 2
    ratio = float(r_in) ** 2 / r_out ** 2
    vals = {'A': 1 / 4, 'B': 1 / 2, 'C': 1 / math.sqrt(2), 'D': math.pi / 4}
    keys = [k for k, v in vals.items() if abs(v - ratio) < 1e-9]
    assert ch['B'] == '1 : 2'
    return keys[0]


CHECKS = {f'B034-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 12)}
