"""Scripted recomputation for SAT Math batch 27. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    assert F(135, 15) == 9
    return by_text(ch, "Dana earns $135 by working 9 hours at job A and no hours at job B.")


def c02(ch):
    sols = [(n, 40 - n) for n in range(41) if 3 * n + F(3, 2) * (40 - n) == 87]
    assert sols == [(18, 22)]
    return by_text(ch, "n + p = 40\n3n + 1.5p = 87")


def c03(_):
    prods = set()
    for k in (-5, 0, 2, 7):
        d = k * k + 96
        r1, r2 = (-k + math.sqrt(d)) / 4, (-k - math.sqrt(d)) / 4
        prods.add(round(r1 * r2, 9))
    assert prods == {-6.0}
    return -6


def c04(ch):
    zs = sorted(x for x in range(-50, 51) if -(x + 1) ** 2 + 9 == 0)
    assert zs == [-4, 2]
    return by_text(ch, "x = −4 and x = 2")


def c05(ch):
    g = lambda x: (x - 2) ** 2 + 3
    xm = min(range(-20, 21), key=g)
    return by_text(ch, f"({xm}, {g(xm)})")


def c06(_):
    a = 12 - 3
    return F(18, a)


def c07(ch):
    y = math.isqrt(100 - 36)
    return pick(ch, F(y, 6))


CHECKS = {f'Q027-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07], 1)}
