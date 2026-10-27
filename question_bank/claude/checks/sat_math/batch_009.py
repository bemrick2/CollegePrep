"""Scripted recomputation for SAT Math batch 9. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    ks = [k for k in range(-100, 100) if 144 - 8 * k > 0]
    assert max(ks) == 17 and all(144 - 8 * k <= 0 for k in range(18, 36))
    return by_text(ch, "k < 18")


def c02(ch):
    x = F(9 * 4)
    return pick(ch, x / 12)


def c03(ch):
    return pick(ch, next(w for w in range(0, 100) if 1250 - 45 * w < 500))


def c04(_):
    s = F(12, 8)
    a, b = s * 4, F(3) / s
    # the two equations are proportional
    assert (a, 3, 12) == (s * 4, s * b, s * 8)
    return a + b


def c05(ch):
    a = F(-1 - 8, 2 - 1)
    assert (a - 1) / (a + 4) == 2
    return pick(ch, a)


def c06(_):
    for x in (1, 2, 3, 6):
        assert math.isclose(4 ** (x / 2) * 8 ** (x / 3), 2 ** (2 * x))
    return 2


def c07(ch):
    return by_text(ch, f"{int(F(28, 80) * 100)}%")


def c08(_):
    return F(10 * 20 - 38 + 18, 10)


def c09(ch):
    return pick(ch, F(168, 4 * 6))


def c10(ch):
    ks = [k for k in range(1, 100) if 4 * k * k - 8 * (k * k - 50) == 0]
    assert ks == [10]
    return by_text(ch, "10")


CHECKS = {f'Q009-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
