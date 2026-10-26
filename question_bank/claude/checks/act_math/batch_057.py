"""Scripted recomputation for ACT Math batch 57. Each check derives the answer from the stem's numbers only."""
import math
import os
import statistics
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def deg(t):
    return F(t.replace('°', ''))


def pt(t):
    return tuple(int(s.replace('−', '-')) for s in t.strip('()').split(','))


def by_point(ch, want):
    hits = [k for k, v in ch.items() if pt(v) == want]
    assert len(hits) == 1
    return hits[0]


def c01(ch):
    best = max(ch, key=lambda k: F(ch[k]))
    return best


def c02(ch):
    return pick(ch, F(180, 9) * 4, conv=deg)


def c03(ch):
    hits = [k for k, v in ch.items() if pt(v)[1] == -2 * pt(v)[0] + 7]
    assert len(hits) == 1
    return hits[0]


def c04(ch):
    return pick(ch, F(30, 45 + 30))


def c05(ch):
    return pick(ch, next(x for x in range(1, 1000) if F(x, 3) + F(x, 4) == 14))


def c06(ch):
    return pick(ch, 2 * math.sqrt(10 ** 2 - 6 ** 2))


def c07(ch):
    return pick(ch, F(27, 99))


def c08(ch):
    x, y = 6, 8
    x, y = y, -x
    return by_point(ch, (x, -y))


def c09(ch):
    return pick(ch, sum(1 for x in range(1, 100) if statistics.median([3, 8, 12, 15, x]) == 8))


def c10(ch):
    a = math.log2(3)
    return pick(ch, 8 ** a, tol=1e-9)


CHECKS = {f'B057-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
