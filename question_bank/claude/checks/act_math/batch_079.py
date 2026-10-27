"""Scripted recomputation for ACT Math batch 79. Each check derives the answer from the stem's numbers only."""
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
    for x in (2, -3):
        assert x * x + x - 6 == 0
    return by_text(ch, "x² + x − 6")


def c02(ch):
    semi_over_pi = F(1, 2) * 2 ** 2
    return by_text(ch, f"{4 * 6} + {semi_over_pi}π")


def c03(ch):
    d = F(29 - 5, 4)
    return pick(ch, sum(5 + k * d for k in (1, 2, 3)))


def c04(ch):
    return pick(ch, round(3 * 0.301, 3))


def c05(ch):
    return pick(ch, 60 + 80 - round(math.hypot(60, 80)))


def c06(ch):
    n = sum(1 for k in range(100, 1000) if str(k)[0] < str(k)[1] < str(k)[2])
    return pick(ch, F(n, 900))


def c07(ch):
    return pick(ch, sum(range(1, 100, 2)) - sum(range(2, 101, 2)))


def c08(ch):
    return pick(ch, F(24 * 60 * 60, 20) / 1000)


def c09(ch):
    return pick(ch, 6 * 6 + 4 * F(1, 2) * 6 * 5)


def c10(ch):
    return pick(ch, (2 * 1 - 1) ** 5)


CHECKS = {f'B079-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
