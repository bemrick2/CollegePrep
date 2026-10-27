"""Scripted recomputation for SAT Math batch 13. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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


def c01(_):
    # intercepts of y - 5 = m(x - 2): x = 2 - 5/m, y = 5 - 2m
    ms = [F(n, d) for n in range(-40, 41) for d in range(1, 11) if n != 0]
    eq = sorted({m for m in ms if 2 - 5 / m == 5 - 2 * m})
    assert eq == [F(-1), F(5, 2)]
    return min(eq)


def c02(ch):
    opts = {k: F(v) for k, v in ch.items()}
    bad = [k for k, x in opts.items() if not 2 * x - 5 > 7]
    assert len(bad) == 1
    return bad[0]


def c03(ch):
    m = F(-2 - 10, 5 + 1)
    b = 10 - m * -1
    return pick(ch, (4 - b) / m)


def c04(ch):
    for x in (0, 1, 3, 7, -5):
        assert F(x * x - 16, x - 4) - F(x * x - 4, x - 2) == 2
    return pick(ch, 2)


def c05(ch):
    k = next(k for k in range(-10, 11) if 3 * F(2) ** k == 12)
    return pick(ch, k)


def c06(_):
    club, non = F(60, 100), F(40, 100)
    a, b = club * F(40, 100), non * F(25, 100)
    return a / (a + b)


def c07(ch):
    return pick(ch, F(240) * F(115, 100))


def c08(ch):
    h = math.isqrt(10 ** 2 - 6 ** 2)
    return by_text(ch, f"{F(h, 10).numerator}/{F(h, 10).denominator}")


def c09(_):
    x = next(x for x in range(1, 50) if x * x + (x + 7) ** 2 == 169)
    return F(x * (x + 7), 2)


def c10(ch):
    return by_text(ch, f"(0, {2 * (0 - 3) ** 2 + 1})")


CHECKS = {f'Q013-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
