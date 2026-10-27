"""Scripted recomputation for SAT Math batch 12. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    s = lambda w: 120 + 35 * w
    assert s(0) == 120 and s(1) == 155
    return by_text(ch, "s = 120 + 35w")


def c02(ch):
    sols = [(x, y) for x in range(-20, 21) for y in range(-20, 21) if 2 * x + y == 1 and x - y == 8]
    assert sols == [(3, -5)]
    return by_text(ch, "(3, −5)")


def c03(_):
    m = F(-1 - 5, 6 - (-3))
    b = -1 - m * 6
    m2 = -1 / m
    return b / (m2 - m)


def c04(ch):
    roots = lambda a, b, c, d: {F(-b, a), F(-d, c)}
    opts = {"(x − 3)(2x + 5) = 0": roots(1, -3, 2, 5), "(x + 3)(5x − 2) = 0": roots(1, 3, 5, -2),
            "(x − 3)(5x − 2) = 0": roots(1, -3, 5, -2), "(x + 3)(2x − 5) = 0": roots(1, 3, 2, -5)}
    hit = [k for k, v in opts.items() if v == {F(-3), F(5, 2)}]
    assert len(hit) == 1
    return by_text(ch, hit[0])


def c05(_):
    for a in range(-20, 21):
        if all(F(a * x + 3, x - 2) == 5 + F(13, x - 2) for x in (0, 1, 3, 7)):
            return a


def c06(ch):
    pct = round((1.02 ** 12 - 1) * 100, 1)
    return by_text(ch, f"{pct}%")


def c07(_):
    return F(150, 100) * (1 - F(40, 100)) * 100


def c08(ch):
    return pick(ch, F(14 + 10, 40 + 10) * 100)


def c09(ch):
    for k in range(-100, 101):
        if 25 + 4 - k == 36:
            return pick(ch, k)


def c10(ch):
    return by_text(ch, f"{180 - 48 - 67}°")


CHECKS = {f'Q012-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
