"""Scripted recomputation for ACT Math batch 77. Each check derives the answer from the stem's numbers only."""
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


def money(ch, x):
    return by_text(ch, f"${x:,.0f}")


def c01(ch):
    return money(ch, 500 + F(6, 100) * (12000 - 5000))


def c02(ch):
    return money(ch, F(12, 100) * 500 + F(18, 100) * 300)


def c03(ch):
    return pick(ch, F(40, 100) * 60 - F(60, 100) * 40)


def c04(ch):
    return pick(ch, sum((3 - k + 1) ** 2 for k in range(1, 4)))


def c05(ch):
    return by_text(ch, f"{F(15, 60) * 2 * 10}π")


def c06(ch):
    return pick(ch, F(4 * 6, 3))


def c07(ch):
    return pick(ch, sum(1 for n in range(100, 1000) if all(int(d) % 2 for d in str(n))))


def c08(ch):
    h = math.isqrt(8 ** 2 + 15 ** 2)
    return by_text(ch, f"8/{h}")


def c09(ch):
    return pick(ch, F(120, 30) * 75)


def c10(ch):
    f = lambda x: abs(x - 3) - abs(x + 1)
    return pick(ch, max(f(x / 10) for x in range(-200, 201)))


CHECKS = {f'B077-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
