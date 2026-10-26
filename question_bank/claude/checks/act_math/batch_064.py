"""Scripted recomputation for ACT Math batch 64. Each check derives the answer from the stem's numbers only."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    return pick(ch, max(3 * math.sin(t / 1000) + 2 for t in range(0, 6284)), tol=1e-5)


def c02(ch):
    want = 26 ** 3 * 10 * 9 * 8
    vals = {'26³ · 10³': 26 ** 3 * 10 ** 3, '26 · 25 · 24 · 10 · 9 · 8': 26 * 25 * 24 * 720,
            '26³ + 10 · 9 · 8': 26 ** 3 + 720, '26³ · 10 · 9 · 8': want}
    hits = [k for k, v in ch.items() if vals[v] == want]
    assert len(hits) == 1
    return hits[0]


def c03(ch):
    return pick(ch, F(3 * 20, 12))


def c04(ch):
    return pick(ch, (20 - 6) * (12 - 6) * 3)


def c05(ch):
    return pick(ch, math.gcd(2 ** 4 * 3 ** 2 * 5, 2 ** 2 * 3 ** 3 * 7))


def c06(ch):
    return pick(ch, F(1, 2) ** 3)


def c07(ch):
    word = 'MATHEMATICS'
    return pick(ch, F(sum(1 for c in word if c in 'AEIOU'), len(word)))


def c08(ch):
    # tan 30 = h/(x+40), tan 60 = h/x
    x = 40 * math.tan(math.radians(30)) / (math.tan(math.radians(60)) - math.tan(math.radians(30)))
    h = x * math.tan(math.radians(60))
    return pick(ch, h, tol=1e-9)


def c09(ch):
    a, b = (1 + 7) / 2, 2
    assert abs(1 - a) + b == 5
    return pick(ch, a + b)


def c10(ch):
    a = F(12, 4)
    return pick(ch, a * 9)


CHECKS = {f'B064-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
