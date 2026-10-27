"""Scripted recomputation for SAT Math batch 18. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    mem, non = 40 * 60, 60 * 40
    return F(mem * 100, mem + non)


def c02(_):
    a = F(-4, 2 * -1)
    c = 3 - (a * 1 + 4 * -1)
    return a + c


def c03(ch):
    xs = [x for x in range(-20, 21) if x * x + 6 * x == 7]
    vals = {(x + 3) ** 2 for x in xs}
    assert len(vals) == 1
    return pick(ch, vals.pop())


def c04(ch):
    y = 3 * 2 - 4
    return pick(ch, F(y - 2, 2))


def c05(ch):
    r = math.isqrt(49)
    side = F(2 * r, 4)  # times pi
    return by_text(ch, f"{float(side)}π")


def c06(ch):
    k = F(12, 3)
    return pick(ch, -3 * 2 * k + 12)


def c07(ch):
    return pick(ch, 2 * 3 * 7)


def c08(ch):
    for x in (1, 2, -3):
        assert 2 * x * (3 * x - 4) == 6 * x * x - 8 * x
    return by_text(ch, "6x² − 8x")


def c09(ch):
    m = F(5 - 0, 6 - 4)
    return pick(ch, m * (0 - 4))


def c10(_):
    hyp = math.isqrt(9 ** 2 + 12 ** 2)
    return F(81, hyp)


CHECKS = {f'Q018-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
