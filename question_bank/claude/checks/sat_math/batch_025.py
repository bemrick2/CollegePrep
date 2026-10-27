"""Scripted recomputation for SAT Math batch 25. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    g = lambda x: 3 * (2 * x + 1) - 2 * (x - 4)
    a = g(1) - g(0)
    b = g(0)
    assert all(g(x) == a * x + b for x in range(-5, 6))
    return a + b


def c02(ch):
    k = F(11 - 3, 2)
    return pick(ch, k * -1 + 3)


def c03(ch):
    p = 15
    return pick(ch, p * (600 - 20 * p))


def c04(ch):
    R = lambda p: p * (600 - 20 * p)
    return pick(ch, max(range(0, 31), key=R))


def c06(_):
    sols = [x for x in range(-50, 51) if x * x - 2 * x - 8 == -9]
    assert sols == [1]
    return 1


def c07(ch):
    fs = {"f(x) = 3(1.2)ˣ": lambda x: 3 * 1.2 ** x, "f(x) = 0.8x": lambda x: 0.8 * x,
          "f(x) = −3(0.8)ˣ": lambda x: -3 * 0.8 ** x, "f(x) = 3(0.8)ˣ": lambda x: 3 * 0.8 ** x}
    dec = [k for k, f in fs.items() if all(f(x + 1) < f(x) for x in range(-10, 10))]
    assert len(dec) == 1
    return by_text(ch, dec[0])


def c08(ch):
    return by_text(ch, "5/12")


def c09(ch):
    opp = F(3, 5) * 20
    adj = math.isqrt(20 ** 2 - int(opp) ** 2)
    return pick(ch, opp + adj + 20)


def c10(ch):
    return pick(ch, 13 + 24)


CHECKS = {f'Q025-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c06, c07, c08, c09, c10], 1)}
