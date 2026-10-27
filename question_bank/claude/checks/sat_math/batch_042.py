"""Scripted recomputation for SAT Math batch 42. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    pages = lambda t: F(18, 60) * (t - 30)
    cands = {'p = 0.3t − 9': lambda t: F(3, 10) * t - 9, 'p = 0.3t − 30': lambda t: F(3, 10) * t - 30,
             'p = 0.3t + 9': lambda t: F(3, 10) * t + 9, 'p = 18t − 540': lambda t: 18 * t - 540}
    hits = [k for k, f in cands.items() if all(f(t) == pages(t) for t in range(30, 300, 7))]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c02(_):
    return F(sum(1 for x in range(-100, 101) if abs(x - 5) < 4 and abs(x - 10) <= 4))


def c03(_):
    return F(next(p for p in range(1, 1000) if 300 * p == 270 * (p + 2)))


def c04(ch):
    sols = [(a, b) for a in range(0, 30) for b in range(0, 30) if 3 * a + 2 * b == 24 and 2 * a + 3 * b == 26]
    assert len(sols) == 1
    return pick(ch, sols[0][1])


def c05(_):
    k = F(-(27 - 48 + 48), 9)
    p = lambda x: x ** 3 + k * x * x - 16 * x + 48
    zeros = [x for x in range(-50, 51) if p(x) == 0]
    assert len(zeros) == 3
    return F(max(zeros))


def c06(ch):
    a = F(4 - 8, abs(1 - 3))
    zeros = [3 + 8 / -a * s for s in (1, -1)]
    return pick(ch, float(max(zeros)))


def c07(ch):
    a_vals = [a for a in (F(n, 2) for n in range(-40, 41)) if all((a * x + 5) ** 2 - (a * x - 5) ** 2 == 60 * x for x in range(-3, 4))]
    assert len(a_vals) == 1
    return pick(ch, float(a_vals[0]))


def c08(_):
    f = lambda x: (x - 3) ** 2 - 4
    assert all(f(x) == f(6 - x) for x in range(-5, 10))
    return F(f(-1))


def c09(_):
    km_per_l = F(100, 8)
    return F(round(float(km_per_l) * 3.785 / 1.609))


def c10(ch):
    m = next(m for m in (F(n, 2) for n in range(0, 400)) if (3 * (m + 10) + m) / 4 == 85)
    return pick(ch, float(m))


def c11(_):
    x = F(180 - 12 - 24, 8)
    a, b = 5 * x + 12, 3 * x + 24
    assert a != b
    return max(a, b)


def c12(_):
    s = F(1, 2)  # sin A = 3 sin A - 1 since cos B = sin A
    assert s == 3 * s - 1
    return s


CHECKS = {f'Q042-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
