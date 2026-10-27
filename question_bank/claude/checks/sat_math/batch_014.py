"""Scripted recomputation for SAT Math batch 14. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    l, w = 5, 3
    P = 2 * l + 2 * w
    assert F(P - 2 * l, 2) == w and P - 2 * l != w
    return by_text(ch, "w = (P − 2l)/2")


def c02(ch):
    return pick(ch, next(c for c in range(41) if 3 * c - (40 - c) == 76))


def c03(ch):
    y = 3 * 1 - 4
    return pick(ch, 5 - 2 * y)


def c04(_):
    k = next(k for k in range(-20, 21) if F(k + -3, 2) == 0)
    f = lambda x: (x - k) * (x + 3)
    assert f(1) == f(-1)
    return k


def c05(ch):
    b = next(b for b in range(1, 20) if b * b == 54 // 6)
    a = F(6, b)
    assert a * b ** 3 == 54
    return pick(ch, a)


def c06(ch):
    sols = sorted(x for x in range(-50, 51) if x * x == 6 * x)
    assert sols == [0, 6]
    return by_text(ch, "{0, 6}")


def c07(_):
    on, store = F(40), F(60)
    on2, store2 = on * F(12, 10), store * F(8, 10)
    return on2 / (on2 + store2) * 100


def c08(ch):
    return pick(ch, F(25 * 18, 100))


def c09(_):
    # 6/s = 15/(10 + s)
    return F(60, 15 - 6)


def c10(ch):
    return by_text(ch, f"{int(48 * F(3, 2) ** 2)}π")


CHECKS = {f'Q014-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
