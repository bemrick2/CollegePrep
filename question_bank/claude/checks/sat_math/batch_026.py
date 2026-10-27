"""Scripted recomputation for SAT Math batch 26. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    R = lambda p: p * (600 - 20 * p)
    return pick(ch, max(range(0, 31), key=R))


def c02(ch):
    return pick(ch, round(1200 / (30 - 12)))


def c03(_):
    return next(n for n in range(-50, 51) if 2 * (n + 5) == 26)


def c04(ch):
    sols = [x for x in range(-50, 51) if (x + 2) * (x - 3) == 14]
    assert sorted(sols) == [-4, 5]
    return pick(ch, max(sols))


def c05(ch):
    assert 3000 * 1.05 ** 0 == 3000
    return by_text(ch, "The value at the time of purchase is $3,000.")


def c06(_):
    sols = [a for a in range(1, 10000) if math.isclose(a ** 0.5, 2 * a ** 0.25)]
    assert sols == [16]
    return 16


def c07(ch):
    return pick(ch, F(4 * 9, 6))


def c08(ch):
    ok = [k for k, v in ch.items() if 9 - 5 < int(v) < 9 + 5]
    assert len(ok) == 1
    return ok[0]


def c09(_):
    ys = [y for y in range(-20, 21) if (0 - 4) ** 2 + (y - 5) ** 2 == 25]
    assert sorted(ys) == [2, 8]
    return sum(ys)


def c10(ch):
    r = 6
    assert F(1, 3) * r * r * 12 == 144
    return by_text(ch, "144π")


CHECKS = {f'Q026-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
