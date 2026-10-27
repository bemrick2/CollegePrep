"""Scripted recomputation for SAT Math batch 21. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(_):
    return next(p for p in range(-100, 101) if F(4, 3) * p - p == 5)


def c02(ch):
    ok = [k for k, v in ch.items() if (2 - int(v.replace('−', '-'))) != 0 and F(12, 2 - int(v.replace('−', '-'))) < 0]
    assert len(ok) == 1
    return ok[0]


def c03(ch):
    b = 1 - F(2, 3) * 9
    return pick(ch, F(2, 3) * -3 + b)


def c04(_):
    return next(L for L in range(1, 200) if 3 * 3 * L + 5 * L == 364)


def c05(ch):
    return pick(ch, (F(470, 100) - F(25, 100) * 12) / F(10, 100))


def c06(ch):
    h = lambda t: -2 * (t - 3) ** 2 + 50
    ts = [t for t in range(1, 20) if h(t) == h(0)]
    return pick(ch, ts[0])


def c07(ch):
    xs = [F(n, d) for n in range(1, 40) for d in range(1, 10)]
    sols = {x for x in xs if x > 1 and x + 1 / x == F(10, 3)}
    assert sols == {3}
    return pick(ch, 3)


def c08(_):
    r = F(1452, 1200)
    root = F(math.isqrt(r.numerator), math.isqrt(r.denominator))
    assert root * root == r
    return (root - 1) * 100


def c09(ch):
    x = next(x for x in range(-10, 10) if 2 ** (3 * x) == 64)
    return pick(ch, 2 ** x)


def c10(ch):
    return pick(ch, F(2, 5) * (300 - 40))


CHECKS = {f'Q021-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
