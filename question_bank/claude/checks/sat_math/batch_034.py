"""Scripted recomputation for SAT Math batch 34. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    f = lambda x: x * x - 4 * x
    sols = [a for a in range(-20, 21) if f(a) == f(a + 2)]
    assert sols == [1]
    return pick(ch, 1)


def c02(_):
    # a + 3(x - 1) = 2x + 1 gives x = 4 - a; no solution exactly when that x is the excluded value 1
    bad = [a for a in range(-20, 21) if 4 - a == 1]
    assert bad == [3]
    return F(3)


def c03(_):
    f = lambda x: 5 * F(3) ** x
    sols = [t for t in range(-10, 11) if f(t + 2) - f(t) == 360]
    assert sols == [2]
    return F(2)


def c04(ch):
    pounds = F(3, 4) * 43560 * F(5, 2) / 1000
    return pick(ch, math.ceil(pounds / 20))


def c05(ch):
    def median(x):
        data = sorted(v for v, n in zip(range(1, 6), (4, 7, x, 6, 3)) for _ in range(n))
        n = len(data)
        return F(data[n // 2]) if n % 2 else F(data[n // 2 - 1] + data[n // 2], 2)
    return pick(ch, min(x for x in range(0, 50) if median(x) == 3))


def c06(ch):
    a, b = (50, 58), (41, 51)
    assert max(a[0], b[0]) <= min(a[1], b[1])  # intervals overlap
    return by_text(ch, "It is plausible that the true percents of supporters in the two cities are equal.")


def c07(_):
    return (F(6, 5) * F(1, 2) / F(2, 5) - 1) * 100


def c08(_):
    s = F(6 * 8, 6 + 8)
    assert s / 6 + s / 8 == 1  # (s, s) lies on x/6 + y/8 = 1
    return s


def c09(ch):
    adj, opp = 2, 6  # tan θ = 3, the shorter leg is adjacent
    return pick(ch, math.sqrt(adj ** 2 + opp ** 2))


def c10(ch):
    return pick(ch, 180 - (180 - 50) / 2, conv=lambda t: float(t.rstrip('°')))


CHECKS = {f'Q034-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
