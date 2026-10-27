"""Scripted recomputation for SAT Math batch 33. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    per_min = F(1540 - 1240, 15)
    start = 1240 - 10 * per_min
    assert 1840 == start + 40 * per_min
    return by_text(ch, f"E = {int(start):,} + {int(per_min * 60):,}h")


def c02(_):
    m = F(4 - 8, 3 - 1)
    b = 8 - m
    return -b / m


def c03(ch):
    sols = sorted(x for x in range(-50, 51) if (x - 3) * (x + 5) == (x - 3) * (2 * x - 1))
    assert sols == [3, 6]
    return pick(ch, sum(sols))


def c04(ch):
    sols = [x for x in range(0, 200) if math.isclose(x - math.sqrt(x), 6)]
    assert sols == [9]
    return by_text(ch, "9")


def c05(ch):
    pts = {(x, y) for x in range(-10, 11) for y in range(-10, 11) if x * x + y * y == 25 and y == x * x - 5}
    assert pts == {(3, 4), (-3, 4), (0, -5)}
    return pick(ch, len(pts))


def c06(_):
    g = lambda x: x ** 3 - 6 * x ** 2 + 9 * x
    c = -g(1)
    zeros = sorted({x for x in range(-10, 11) if g(x) + c == 0})
    assert c == -4 and zeros == [1, 4]
    return c


def c07(ch):
    for x in range(-5, 6):
        assert 6 * x * x + 7 * x - 20 == (2 * x + 5) * (3 * x - 4)
    return pick(ch, 2 + 5 + 3 - 4)


def c08(ch):
    x = math.log(5, 9)
    assert math.isclose(27 ** x * 3 ** (-x), 5)
    return pick(ch, 5)


def c09(ch):
    for r in ((5 + math.sqrt(21)) / 2, (5 - math.sqrt(21)) / 2):
        assert math.isclose(r + 1 / r, 5)
    return pick(ch, 5)


def c10(_):
    total = 200 * 0.8 ** 5 + 200 * 0.8 ** 2
    return F(str(round(total, 1)))


CHECKS = {f'Q033-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
