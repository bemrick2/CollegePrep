"""Scripted recomputation for SAT Math batch 4. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    return pick(ch, 1 - F(-3, 4) * 8)


def c02(ch):
    # (a − 2)x = b − 3: no solution iff a = 2 and b ≠ 3
    def nsol(a, b):
        return 'none' if a == 2 and b != 3 else ('all' if a == 2 else 'one')
    assert nsol(2, 5) == 'none' and nsol(2, 3) == 'all' and nsol(4, 3) == 'one'
    return by_text(ch, "a = 2 and b ≠ 3")


def c03(ch):
    on = [p for p in [(9, 6), (4, -6), (-6, -4), (-9, 6)] if F(p[1], p[0]) == F(-4, 6)]
    assert on == [(-9, 6)]
    return by_text(ch, "(−9, 6)")


def c04(_):
    for x in range(-50, 51):
        y = x
        if 4 * (x + 2 * y) == 48:
            return x


def c05(ch):
    disc = {k: 36 - 4 * c for k, c in (("x² + 6x + 8 = 0", 8), ("x² + 6x + 9 = 0", 9), ("x² + 6x + 10 = 0", 10))}
    disc["x² − 6x − 10 = 0"] = 36 + 40
    neg = [k for k, v in disc.items() if v < 0]
    assert len(neg) == 1
    return by_text(ch, neg[0])


def c06(_):
    a, b, c = 3, -5, -12
    r = math.isqrt(b * b - 4 * a * c)
    return max(F(-b + r, 2 * a), F(-b - r, 2 * a))


def c07(ch):
    xv = F(3 + (-5), 2)
    return pick(ch, F(32) / ((xv - 3) * (xv + 5)))


def c08(ch):
    for x, y in ((2, 3), (1.5, 0.7)):
        assert math.isclose((x ** 3 * y ** -2) ** 2 / (x * y ** -3), x ** 5 / y)
    return by_text(ch, "x⁵/y")


def c09(ch):
    return pick(ch, F(18) / (1 - F(40, 100) - F(35, 100)))


def c10(_):
    return F(45, 100) * 1600 - F(40, 100) * 1200


CHECKS = {f'Q004-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
