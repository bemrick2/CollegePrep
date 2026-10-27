"""Scripted recomputation for ACT Math batch 75. Each check derives the answer from the stem's numbers only."""
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
    d = 4
    return by_text(ch, f"{d // 2}π + {d}")


def c02(ch):
    r = 1
    return pick(ch, F(4, 3) * r ** 3 / (r * r * 2 * r))


def c03(ch):
    area = 10 * 6 * math.sin(math.radians(60))
    assert math.isclose(area, 30 * math.sqrt(3))
    return by_text(ch, "30√3")


def c04(ch):
    return pick(ch, round(math.log10(1000) + math.log10(0.01)))


def c05(ch):
    x = F(90 - 10 + 5, 5)
    return by_text(ch, f"{max(2 * x + 10, 3 * x - 5)}°")


def c06(ch):
    sols = [x for x in range(0, 181) if math.isclose(2 * math.cos(math.radians(x)), 1)]
    assert sols == [60]
    return by_text(ch, "60°")


def c07(ch):
    return pick(ch, 5 * 3 ** 0 - 2)


def c08(ch):
    n = next(n for n in range(2, 1000) if all(n % d == 1 for d in (2, 3, 4, 5, 6)))
    return pick(ch, n)


def c09(ch):
    for x in (0.5, 1, 2.3):
        assert math.isclose(2 ** (x + 3), 8 * 2 ** x)
    return by_text(ch, "8 · 2^x")


def c10(ch):
    x, y = -4, 7
    return by_text(ch, f"({-x}, {y})")


CHECKS = {f'B075-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
