"""Scripted recomputation for ACT Math batch 78. Each check derives the answer from the stem's numbers only."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(ch):
    bins = [("60–69", 4), ("70–79", 9), ("80–89", 12), ("90–99", 5)]
    n = sum(c for _, c in bins)
    cum = 0
    for name, c in bins:
        if cum < n // 2 and cum + c >= n // 2 + 1:
            return by_text(ch, name)
        cum += c


def c02(ch):
    d = [12, 14, 15, 15, 16, 18, 95]
    drop = sum(d) / 7 - sum(d[:-1]) / 6
    return pick(ch, round(drop, 1))


def c03(ch):
    for x in range(-5, 6):
        assert 2 * x ** 3 - 8 * x == 2 * x * (x - 2) * (x + 2)
    return by_text(ch, "2x(x − 2)(x + 2)")


def c04(ch):
    for x in (-3, -0.5, -10):
        assert abs(x) + x == 0
    return by_text(ch, "|x| + x")


def c05(ch):
    return pick(ch, round((3 + math.sqrt(2)) * (3 - math.sqrt(2))))


def c06(ch):
    return pick(ch, sum(1 for x in range(-5, 6) for y in range(-5, 6) if x * x + y * y == 25))


def c07(ch):
    assert math.isclose(math.tan(math.radians(135)), -1)
    return by_text(ch, "−1")


def c08(ch):
    r = 10
    chord = 2 * r * math.sin(math.radians(30))
    return pick(ch, round(chord))


def c09(ch):
    return pick(ch, math.factorial(10) // math.factorial(8))


def c10(ch):
    d = math.dist((0, 0), (2, 4))
    assert math.isclose(d, 2 * math.sqrt(5))
    return by_text(ch, "2√5")


CHECKS = {f'B078-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
