"""Scripted recomputation for SAT Math batch 10. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    a = F(6, (0 - 2) * (0 - 3))
    f = lambda x: a * (x - 2) * (x - 3)
    assert f(0) == 6 and f(2) == 0 and f(3) == 0
    return f(1)


def c02(ch):
    f = 5
    for _ in range(4):
        f *= 3
    return pick(ch, f)


def c03(ch):
    x, y = 5, 2
    assert x * x + y * y == 29 and x * y == 10
    return pick(ch, 29 + 2 * 10)


def c04(ch):
    sols = [x for x in range(-50, 51) if x * (x - 6) == -9]
    assert sols == [3] and 36 - 4 * 9 == 0
    return by_text(ch, "Exactly one")


def c05(ch):
    return pick(ch, F(360 - 24 * 10, 15))


def c06(_):
    ks = [k for k in range(-50, 51) if k != 2 and F(3 * k - 4, k - 2) == 5]
    assert len(ks) == 1
    return ks[0]


def c07(_):
    x = 5 * 11 - (5 + 8 + 12 + 15)
    d = sorted([5, 8, x, 12, 15])
    return d[2]


def c08(ch):
    return pick(ch, F(72, 8))


def c09(ch):
    # (1/3) r^2 h = (4/3) r^3  ->  h/r = 4
    return pick(ch, F(4, 3) / F(1, 3))


def c10(ch):
    w = F(96, 12)
    return pick(ch, 2 * (12 + w))


CHECKS = {f'Q010-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
