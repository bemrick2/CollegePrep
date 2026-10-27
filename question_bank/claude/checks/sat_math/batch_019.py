"""Scripted recomputation for SAT Math batch 19. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    f = lambda x: 2 * x + 3
    g = lambda x: -2 * x + 15
    assert [f(x) for x in (0, 2, 4)] == [3, 7, 11] and [g(x) for x in (0, 2, 4)] == [15, 11, 7]
    return pick(ch, F(15 - 3, 4))


def c02(ch):
    x = F(12, 5)  # 3x + 2x = 12 on y = x
    return pick(ch, x / x)


def c03(_):
    return F(85 - 40, 12 + 18)


def c04(ch):
    return pick(ch, next(x for x in range(0, 20) if 2 ** x - 8 == 0))


def c05(ch):
    sols = [x for x in range(-50, 51) if x * x - 5 * x - 14 == 0]
    hit = [k for k, v in ch.items() if int(v.replace('−', '-')) in sols]
    assert len(hit) == 1
    return hit[0]


def c06(ch):
    a = F(110, 100) * F(90, 100)
    b = F(90, 100) * F(110, 100)
    assert a == b
    return by_text(ch, "The final prices are equal.")


def c07(_):
    n = next(n for n in range(3, 100) if F(3, n) * F(2, n - 1) == F(1, 12))
    return n - 3


def c08(_):
    return math.isqrt(32 // 2)


def c09(ch):
    x2 = F(100, 5)
    return pick(ch, x2)


def c10(ch):
    x, y = 3, 4
    return by_text(ch, f"({'−' if -y < 0 else ''}{abs(-y)}, {x})")


CHECKS = {f'Q019-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
