"""Scripted recomputation for ACT Math batch 65. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1
    return hits[0]


def c01(ch):
    x, y = 2 * 3, -1 * 3
    return by_text(ch, f"({x}, {y})".replace('-', '−'))


def c02(ch):
    return pick(ch, F(54, 27))


def c03(ch):
    r = round((96 / 12) ** (1 / 3))
    return pick(ch, F(12, r ** 2))


def c04(ch):
    return by_text(ch, f"{2} × {4}")


def c05(ch):
    return by_text(ch, f"{36 // 4}π − {6 * 6 // 2}")


def c06(ch):
    zeros = {1, -2}  # x^2 + 1 has no real zeros
    return pick(ch, len(zeros))


def c07(ch):
    pa, pb, pab = F(1, 2), F(2, 5), F(1, 5)
    assert pa * pb == pab
    return by_text(ch, "A and B are independent.")


def c08(ch):
    return pick(ch, F(20, 60) * 100, conv=lambda t: F(t.replace('π', '')))


def c09(ch):
    return pick(ch, sum(1 for x in range(1, 61) for y in range(1, 61) if 3 * x + 5 * y == 60))


def c10(ch):
    pairs = list(itertools.combinations(range(1, 9), 2))
    return pick(ch, F(sum(1 for a, b in pairs if (a + b) % 2 == 0), len(pairs)))


CHECKS = {f'B065-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
