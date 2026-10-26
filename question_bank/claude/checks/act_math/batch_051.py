"""Scripted recomputation for ACT Math batch 51. Each check derives the answer from the stem's numbers only."""
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
    return pick(ch, F(17 - 5, -2))


def c02(ch):
    return pick(ch, F(90, 3))


def c03(ch):
    want = (F(0), F(5 - 2))
    hits = [k for k, v in ch.items() if pt(v) == want]
    assert len(hits) == 1
    return hits[0]


def c04(ch):
    return pick(ch, F(6, 15))


def c05(ch):
    a = 12 / 2
    b = a * math.sqrt(3)
    area = a * b / 2
    vals = {'A': 18, 'B': 18 * math.sqrt(3), 'C': 36 * math.sqrt(3), 'D': 72}
    hits = [k for k, v in vals.items() if abs(v - area) < 1e-9]
    assert len(hits) == 1 and ch['B'] == '18√3'
    return hits[0]


def c06(ch):
    n = next(n for n in range(2, 100, 2) if n * n + (n + 2) ** 2 == 340)
    return pick(ch, n + 2)


def c07(ch):
    arr = set(itertools.permutations('AABB'))
    return pick(ch, F(sum(1 for a in arr if a[0] == a[1]), len(arr)))


CHECKS = {f'B051-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 8)}
