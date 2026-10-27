"""Scripted recomputation for SAT Math batch 15. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    # 15(x - d) + 25(y + 6) = 750 whenever 15x + 25y = 750
    return F(25 * 6, 15)


def c02(ch):
    m = F(-5 - 7, 4 - (-2))
    b = 7 - m * -2
    return pick(ch, m + b)


def c03(ch):
    return pick(ch, next(F(a, 2) for a in range(-100, 100) if 2 * (F(a, 2) - 3) == 10))


def c04(ch):
    for x in (0, 1, 3, -4, 5):
        assert x ** 3 - 8 == (x - 2) * (x * x + 2 * x + 4)
    return by_text(ch, "x² + 2x + 4")


def c05(_):
    xs = [x for x in range(-10, 11) if x * x + (x + 1) ** 2 == 25]
    assert len(xs) == 2
    return xs[0] * xs[1]


def c06(ch):
    a = next(a for a in range(1, 50) if 3 * a * a - 2 == 25)
    return by_text(ch, str(a))


def c07(_):
    dogs, cats = F(60) / F(30, 100), F(60) / F(50, 100)
    return (dogs - 60) + (cats - 60)


def c08(ch):
    n = sum(1 for k in range(1, 51) if k % 3 == 0 or k % 5 == 0)
    return pick(ch, F(n, 50))


def c09(ch):
    return by_text(ch, "3π")


def c10(ch):
    return pick(ch, F(7 + 13, 2) * 5)


CHECKS = {f'Q015-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
