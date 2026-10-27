"""Scripted recomputation for SAT Math batch 5. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    ok = [x for x in range(-20, 21) if 7 - 2 * x < 1]
    assert min(ok) == 4 and 3 not in ok
    return by_text(ch, "x > 3")


def c02(_):
    return F(10) * F(3, 2) - 6


def c03(ch):
    return pick(ch, F(20, 2) - F(20, 5))


def c04(_):
    sols = [x for x in range(-50, 51) if x * (x + 2) == 2 * x + 9]
    assert len(sols) == 2
    return sols[0] * sols[1]


def c05(ch):
    ks = [k for k in range(-10, 11) if 4 + 4 * k == 0]
    assert ks == [-1]
    # k = 0 gives two intersections
    assert len([x for x in range(-10, 11) if x * x == 2 * x]) == 2
    return pick(ch, ks[0])


def c06(ch):
    for c in range(-50, 51):
        d = 64 - 4 * c
        if d > 0 and math.isqrt(d) ** 2 == d and math.isqrt(d) == 6:
            return pick(ch, c)


def c07(ch):
    return pick(ch, F(125 * 840 + 21000, 840))


def c08(_):
    return F(60, 100) * 140 + 30


def c09(ch):
    rt = math.isqrt(20 ** 2 - 12 ** 2)
    assert rt * rt == 256
    return pick(ch, F(rt, 20))


def c10(ch):
    x = math.isqrt(150 // 6)
    assert 6 * x * x == 150
    return pick(ch, math.isqrt((3 * x) ** 2 + (4 * x) ** 2))


CHECKS = {f'Q005-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
