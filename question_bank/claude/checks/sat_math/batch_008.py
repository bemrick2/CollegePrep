"""Scripted recomputation for SAT Math batch 8. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    for k in range(-50, 51):
        if all(5 * (2 * x - k) + 3 * x == 13 * x - 35 for x in (0, 1, 2)):
            return pick(ch, k)


def c02(ch):
    ok = lambda m, r: m + r <= 10 and m >= 2 * r
    assert ok(6, 3) and not ok(3, 6) and not ok(8, 3)
    return by_text(ch, "m + r ≤ 10\nm ≥ 2r")


def c03(_):
    return F(3, 2) * -6


def c04(ch):
    f = lambda x: x * x - 2 * x - 15
    zs = [x for x in range(-20, 21) if f(x - 3) == 0]
    assert zs == [0, 8]
    return by_text(ch, "0 and 8")


def c05(ch):
    ks = [k for k in range(-100, 100) if 144 - 8 * k > 0]
    assert max(ks) == 17 and 18 not in ks
    return by_text(ch, "k < 18")


def c06(ch):
    for x in range(-10, 20):
        if 3 * 2 ** (x + 1) == 96:
            return pick(ch, x)


def c07(ch):
    n = next(n for n in range(0, 1000) if 12 < F(15, 100) * n)
    assert F(15, 100) * 80 == 12
    return pick(ch, n)


def c08(_):
    return 4 * 87 - 3 * 84


def c09(ch):
    assert 7 ** 2 + 24 ** 2 == 25 ** 2
    return pick(ch, F(7 * 24, 2))


def c10(_):
    x = F(360 - 110 + 20, 6)
    return max(x, 2 * x, 3 * x - 20, 110)


CHECKS = {f'Q008-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
