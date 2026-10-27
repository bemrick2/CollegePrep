"""Scripted recomputation for SAT Math batch 11. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    return pick(ch, next(x for x in range(-50, 51) if 5 * (x - 2) == 3 * x + 4))


def c02(_):
    return next(n for n in range(-50, 51) if 3 * n + 7 == 5 * n - 5)


def c03(ch):
    lines = {"y = 2x + 3": (2, 3), "y = −2x + 3": (-2, 3), "y = −2x − 3": (-2, -3), "y = 2x − 3": (2, -3)}
    xs = [F(-i, 4) for i in range(1, 400)]
    avoid = [k for k, (m, b) in lines.items() if all(m * x + b >= 0 for x in xs)]
    assert len(avoid) == 1
    return by_text(ch, avoid[0])


def c04(ch):
    for x in (1, 2, -3):
        assert F(6 * x ** 3 - 9 * x ** 2, 3 * x ** 2) == 2 * x - 3
    return by_text(ch, "2x − 3")


def c05(ch):
    # vertex midway between 1 and 9; the minimum occurs at the vertex
    xv = F(1 + 9, 2)
    f = lambda x: 2 * (x - xv) ** 2 - 5
    assert f(1) == f(9) and f(xv) == -5
    return pick(ch, f(5))


def c06(_):
    return (F(12, 10) ** 2 - 1) * 100


def c07(ch):
    return pick(ch, F(3, 8) * 1240)


def c08(ch):
    return pick(ch, F(18) / F(3, 4))


def c09(ch):
    return pick(ch, F(10, 12) * 6 - 2)


def c10(_):
    h = F(2 * 18, 7 - 1)
    return 1 + h


CHECKS = {f'Q011-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
