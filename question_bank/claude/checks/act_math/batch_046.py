"""Scripted recomputation for ACT Math batch 46. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


money = lambda t: F(t.replace('$', '').replace(',', ''))


def c01(ch):
    return pick(ch, 18000 - 4 * 1500, conv=money)


def c02(ch):
    hits = []
    for k, v in ch.items():
        pairs = re.findall(r'\((-?\d+), (-?\d+)\)', v)
        xs = {}
        ok = True
        for a, b in pairs:
            if a in xs and xs[a] != b:
                ok = False
            xs[a] = b
        if not ok:
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c03(ch):
    return pick(ch, math.pi * 4 * 10, tol=1e-9)


def c04(ch):
    return pick(ch, abs(-3 - abs(-5)))


def c05(ch):
    return pick(ch, F(18, 60) * 900)


def c06(ch):
    return pick(ch, F(350, 100) * 8 * F(3, 2), conv=money)


def c07(ch):
    return pick(ch, round(3 ** 2.7 / 3 ** 0.7, 9), tol=1e-6)


def c08(ch):
    s = 2
    inner = (math.hypot(s / 2, s / 2)) ** 2
    ratio = inner / (s * s)
    vals = {'A': 0.25, 'B': 0.5, 'C': 1 / math.sqrt(2), 'D': 0.75}
    hits = [k for k, v in vals.items() if abs(v - ratio) < 1e-9]
    assert len(hits) == 1 and ch['B'] == '1 : 2'
    return hits[0]


def c09(ch):
    bag = 'RRRRBBB'
    groups = list(itertools.combinations(range(7), 3))
    return pick(ch, F(sum(1 for g in groups if sum(bag[i] == 'R' for i in g) == 2), len(groups)))


def c10(ch):
    terms, t = [], 3
    while t <= 384:
        terms.append(t)
        t *= 2
    return pick(ch, sum(terms), conv=lambda x: F(x.replace(',', '')))


CHECKS = {f'B046-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
