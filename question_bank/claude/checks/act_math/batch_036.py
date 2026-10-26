"""Scripted recomputation for ACT Math batch 36. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402



def c01(ch):
    m = F(3, 4)  # from 3x - 4y = 12
    return pick(ch, -1 / m)


def c02(ch):
    r = F(15, 5)
    return pick(ch, 5 * r ** 4, conv=lambda t: F(t.replace(',', '')))


def c03(ch):
    r = 6
    # centroid at 2/3 of the median: height = 1.5 r; side = height * 2 / sqrt(3)
    return pick(ch, 1.5 * r * 2 / math.sqrt(3), tol=1e-9)


def c04(ch):
    return pick(ch, F(5, 1000) * 240, conv=lambda t: F(t.replace(',', '')))


def c05(ch):
    marbles = 'RRRRRBBB'
    pairs = list(itertools.permutations(range(8), 2))
    return pick(ch, F(sum(1 for a, b in pairs if marbles[b] == 'R'), len(pairs)))


def c06(ch):
    return pick(ch, (12 * 12) // (12 + 8))


def c07(ch):
    f = lambda x: x ** 3 + 2 * x + 1
    xs = [x for x in [F(k, 100) for k in range(-1000, 1001)] if f(x) == 13]
    return pick(ch, xs[0])


def c08(ch):
    a, b, c = 13, 14, 15
    s = F(a + b + c, 2)
    return pick(ch, math.sqrt(s * (s - a) * (s - b) * (s - c)), tol=1e-9)


def c09(ch):
    return pick(ch, F(1, 2) * 3 * 4 * 10)


def c10(ch):
    actual_hours = F(11 * 60, 66)
    h = 12 + actual_hours
    want = f'{int(h) - 12}:{int((h - int(h)) * 60):02d} p.m.'
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1
    return hits[0]


CHECKS = {f'B036-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
