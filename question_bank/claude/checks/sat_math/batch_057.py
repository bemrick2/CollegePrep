"""Scripted recomputation for SAT Math batch 57. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    A = lambda t: 3 * t * t - 7 * t + 11  # any test function
    B = lambda t: A(t - 2) + 5  # "5 higher than A was 2 hours earlier"
    assert all(B(t) == A(t - 2) + 5 and B(t) != A(t + 2) + 5 for t in range(3, 20))
    return by_text(ch, "A(t − 2) + 5")


def c02(ch):
    s = lambda h, w: math.sqrt(h * w / 3600)
    pct = (s(1.1 * 150, 1.1 * 40) / s(150, 40) - 1) * 100
    assert abs(pct - 10) < 1e-9
    return by_text(ch, "10%")


def c03(ch):
    xs = sorted(x for x in range(-20, 21) if (x - 3) ** 2 - 16 == 0)
    assert xs == [-1, 7]
    yc = (0 - 3) ** 2 - 16
    return pick(ch, F(1, 2) * (xs[1] - xs[0]) * abs(yc))


def c04(_):
    vol = F(324) / F(27, 10)
    length_cm = vol / (30 * F(16, 10000))
    return length_cm / 100


def c05(ch):
    flour = F(1008) / (1 + F(65, 100) + F(2, 100) + F(1, 100))
    assert flour == 600
    return pick(ch, F(65, 100) * flour)


def c06(ch):
    mg = (F(3) - F(3, 2)) * 40000
    return pick(ch, mg / 1000 / F(75, 100))


def c07(ch):
    total = 4 * 10 + 3 * 20 + 2 * 30
    p = F(2 * 30, total)
    assert p == F(3, 8)
    return by_text(ch, "3/8")


def c08(_):
    a1 = 40 * 30
    assert 40 ** 2 + 30 ** 2 == 50 ** 2
    k2 = F(2500, 16 ** 2 + 9 ** 2)
    a2 = 144 * k2
    return F(round(a1 - a2))


def c09(_):
    r = math.sqrt(25 / 2)
    assert abs(math.pi * (25 - r * r) - math.pi * r * r) < 1e-9
    return F(round(r * 100), 100)


CHECKS = {f'Q057-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09], 1)}
