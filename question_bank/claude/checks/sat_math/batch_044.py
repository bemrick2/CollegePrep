"""Scripted recomputation for SAT Math batch 44. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(_):
    ks = [k for k in range(-50, 51) if k != 3 and 10 + F(k - 10, 3) * k == 3]  # f(x) = 10 + m x with m = (k - 10)/3
    assert ks == [7]
    return F(7)


def c02(_):
    xs = set()
    for k in (F(n, 3) for n in range(-60, 61)):
        if k == 10 or 3 * k - 5 * 6 == 0:
            continue
        det = 3 * k - 5 * 6
        xs.add((11 * k - 5 * 22) / det)
    assert xs == {F(11, 3)}
    return F(11, 3)


def c03(_):
    return F(next(k for k in range(-50, 51) if F(10 + k, 2) > 2 * F(10 - k, 2)))


def c04(_):
    rate = F(1, 4) / 10
    return (F(3, 4) - F(2, 5)) / rate


def c05(ch):
    b = -2 * F(-1, 2) * 4  # vertex at x = -b/(2a) = 4
    h = lambda x: F(-1, 2) * x * x + b * x + 2
    return pick(ch, float(h(4)))


def c06(_):
    b = math.sqrt(98 / 50)
    return F(round((50 + 98) / 2 - 50 * b, 9)).limit_denominator(100)


def c07(ch):
    h = lambda d: F(d * d) / F(3, 2)
    return pick(ch, float(h(9) - h(6)))


def c08(_):
    actual = F(18, 10) * 15 + 12 + 4
    return (actual + 5 - 12) / F(18, 10)


def c09(_):
    theta = F(12, 36 - 30)
    return 30 * theta


def c10(ch):
    return pick(ch, (360 - 110) / 2, conv=lambda t: float(t.rstrip('°')))


def c11(_):
    n = next(n for n in range(7, 500) if (F(2, 5) * n).denominator == 1 and F(F(2, 5) * n - 6, n - 6) == F(1, 4))
    return F(n)


def c12(ch):
    r = math.sqrt(3)
    roots = [r + 2 * r, r - 2 * r]
    assert all(math.isclose(x * x - 2 * r * x - 9, 0, abs_tol=1e-9) for x in roots)
    return pick(ch, max(roots))


CHECKS = {f'Q044-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
