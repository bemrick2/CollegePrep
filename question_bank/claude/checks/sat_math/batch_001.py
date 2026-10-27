"""Scripted recomputation for SAT Math batch 1. Each check derives the answer from the stem's numbers only.
Multiple-choice checks return a choice letter; student-produced-response checks receive None and return the value."""
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
    return pick(ch, F(60 - 4 * 6, 3))


def c02(_):
    for x in range(-50, 51):
        for y in range(-50, 51):
            if 3 * x + 2 * y == 19 and x - y == 3:
                return x + y


def c03(ch):
    ok = [n for n in range(0, 100) if 35 * n + 80 <= 1200]
    assert max(ok) == 32 and 33 not in ok
    return by_text(ch, "35n + 80 ≤ 1,200")


def c04(ch):
    for x in range(-5, 6):
        assert (2 * x - 3) ** 2 - (x + 1) ** 2 == 3 * x * x - 14 * x + 8
    return by_text(ch, "3x² − 14x + 8")


def c05(_):
    return F(15) * F(4, 5)


def c06(ch):
    # p(2) = 0 * q(2) + 5 for any polynomial q
    for q in (lambda x: x ** 2 + 1, lambda x: 7 - x):
        assert (2 - 2) * q(2) + 5 == 5
    return by_text(ch, "p(2) = 5")


def c07(_):
    m, n = math.isqrt(4), math.isqrt(9)
    return 2 * m * n


def c08(ch):
    return pick(ch, F(240) * F(35, 100) * F(25, 100))


def c09(ch):
    return pick(ch, F(425) / (F(150) / 6))


def c10(ch):
    x = F(180 - 15 - 45, 6)
    return by_text(ch, f"{min(2 * x + 15, 4 * x + 45)}°")


CHECKS = {f'Q001-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
