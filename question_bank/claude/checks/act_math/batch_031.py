"""Scripted recomputation for ACT Math batch 31. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    return pick(ch, F(1, 6) + F(1, 10) + F(1, 15))


def c02(ch):
    xs = [F(n, 2) for n in range(-40, 41) if F(n, 2) ** 2 == 2 * F(n, 2) + 3]
    return pick(ch, sum(xs))


def c03(ch):
    cost = lambda h: 8 * h + 5 - 3

    def conv(t):
        m = re.fullmatch(r'(\d+)h ([+−]) (\d+)', t)
        k = int(m.group(3)) * (-1 if m.group(2) == '−' else 1)
        return tuple(int(m.group(1)) * h + k for h in (0, 1, 3))
    return pick(ch, tuple(cost(h) for h in (0, 1, 3)), conv=conv)


def c04(ch):
    v = lambda t: 500 * 0.9 ** t
    change = round((v(1) - v(0)) / v(0) * 100)  # -10 percent per year
    want = ('decreases', abs(change))

    def conv(t):
        m = re.search(r'(decreases|increases) by (\d+)%', t)
        return (m.group(1), int(m.group(2))) if m else t
    return pick(ch, want, conv=conv)


def c05(ch):
    return pick(ch, F(6, 2))


def c06(ch):
    return pick(ch, math.hypot(10, 24) / 2)


def c07(ch):
    return pick(ch, 11 - 3 * (5 - 2))


def c08(ch):
    people = range(8)
    combos = list(itertools.combinations(people, 3))
    return pick(ch, F(sum(1 for c in combos if 0 in c), len(combos)))


def c09(ch):
    return pick(ch, 100 - 75, conv=lambda t: F(t.rstrip('%')))


def c10(ch):
    return pick(ch, min(10 // 3, 8 // 2))


CHECKS = {f'B031-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
