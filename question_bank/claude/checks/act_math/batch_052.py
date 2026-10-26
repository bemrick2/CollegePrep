"""Scripted recomputation for ACT Math batch 52. Each check derives the answer from the stem's numbers only."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def mixed(t):
    t = t.strip()
    if ' ' in t:
        w, fr = t.split(' ')
        return F(w) + F(fr)
    return F(t)


def c01(ch):
    return pick(ch, F(9, 4) * 6, conv=mixed)


def c02(ch):
    w = F(48, 8)
    return pick(ch, w * 3 * w)


def c03(ch):
    x = -2
    return pick(ch, x * x - 3 * x, conv=lambda t: F(t.replace('−', '-')))


def c04(ch):
    return pick(ch, F(6 * 80 - 50, 5), conv=mixed)


def c05(ch):
    return pick(ch, math.hypot(16 / 2, 6))


def c06(ch):
    lo, hi = F(-7 + 5, 2), F(7 + 5, 2)
    assert all(abs(2 * x - 5) < 7 for x in (lo + F(1, 100), hi - F(1, 100)))
    hits = [k for k, v in ch.items() if v == f"−{-lo} < x < {hi}"]
    assert len(hits) == 1
    return hits[0]


def c07(ch):
    k = next(k for k in range(1, 100) if F(3 * k + 6, 5 * k) == F(3, 4))
    return pick(ch, 5 * k)


def c08(ch):
    return pick(ch, F(300, 12) - F(440, 20))


def c09(ch):
    return pick(ch, sum(1 for k in range(-100, 101) if k * k - 36 < 0))


def c10(ch):
    # z - x = (y + z) - (x + y) for any y
    return pick(ch, 2 * 30 - 2 * 20)


CHECKS = {f'B052-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
