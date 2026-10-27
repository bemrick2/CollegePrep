"""Scripted recomputation for ACT Math batch 76. Each check derives the answer from the stem's numbers only."""
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
    h, k = -2, 5
    return by_text(ch, f"(x + {-h})² + (y − {k})² = {abs(k) ** 2}")


def c02(ch):
    d = [2, 4, 6, 8, 10]
    m = F(sum(d), len(d))
    return pick(ch, sum(abs(x - m) for x in d) / len(d))


def c03(ch):
    x = 3 - 1
    return pick(ch, 2 * x + 5)


def c04(ch):
    unit = F(40, 3 + 5)
    return pick(ch, 5 * unit - 3 * unit)


def c05(ch):
    return pick(ch, round(math.dist((1, 2), (7, 10))))


def c06(ch):
    return pick(ch, sum(d for d in range(1, 29) if 28 % d == 0))


def c07(ch):
    return pick(ch, sum(F(1, n * (n + 1)) for n in range(1, 10)))


def c08(ch):
    return pick(ch, F(3 ** 3 - 1, 2))


def c09(ch):
    return by_text(ch, f"{round(180 / math.pi)}°")


def c10(ch):
    for x in range(-5, 6):
        assert x * x + 6 * x + 5 == (x + 3) ** 2 - 4
    return by_text(ch, "(x + 3)² − 4")


CHECKS = {f'B076-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
