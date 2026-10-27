"""Scripted recomputation for SAT Math batch 78. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import itertools
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402

x, a, b, m = sp.symbols('x a b m', real=True)


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    s = sp.solve([3 * a + 5 * b - 410, 5 * a + 3 * b - 390], [a, b])
    return F(int(10 * (s[a] + s[b])))


def c02(ch):
    bb = sp.Symbol('bb')
    f = lambda t: m * t + bb
    slope = sp.solve(sp.expand(f(x + 2) - (f(x) + 3)), m)[0]
    return pick(ch, F(str(slope)))


def c03(_):
    best = None
    for hi in range(0, 101):
        for lo in range(0, hi + 1):
            if 320 + hi + lo >= 6 * 85:
                best = lo if best is None else min(best, lo)
                break
    return F(best)


def c04(ch):
    sol = sp.solve_univariate_inequality(-7 <= 3 - 2 * x, x, relational=False).intersect(
        sp.solve_univariate_inequality(3 - 2 * x < 7, x, relational=False))
    assert sol == sp.Interval.Lopen(-2, 5)
    return by_text(ch, '−2 < x ≤ 5')


def c05(_):
    n = sp.solve(sp.Eq(5 - sp.Rational(2, 3) * x, sp.Rational(1, 3)), x)[0]
    return F(int(n))


def c06(ch):
    steps = [lambda v: 4 - 2 * v - 6 - 10, lambda v: -2 * v - 2 - 10, lambda v: -2 * v - 12, lambda v: v + 6]
    true_sol = sp.solve(4 - 2 * (x - 3) - 10, x)
    for i, st in enumerate(steps):
        if sp.solve(st(x), x) != true_sol:
            return by_text(ch, f'Step {i + 1}')


def c07(_):
    sols = []
    for bv in sp.solve(sp.Eq(sp.Rational(1, 2) * 3 * sp.Abs(b), 12), b):
        slope = (bv - 0) / (0 - (-3))
        if slope < 0:
            sols.append(slope)
    assert len(sols) == 1
    return F(str(sols[0]))


def c08(_):
    k = sp.solve(sp.Eq(-5 - 12, 3 * (-5) + sp.Symbol('k')), sp.Symbol('k'))[0]
    return F(str(sp.solve(sp.Eq(7 * x - 12, 3 * x + k), x)[0]))


def c09(ch):
    both = F(30, 100) * F(40, 100)
    choir = both / F(25, 100)
    return pick(ch, choir * 100, conv=lambda t: F(t.replace('%', '')))


def c10(ch):
    # Even n: the median is the mean of the middle two values. Class A (40): the 20th value is at most 75,
    # so at least 20 scores are 75 or lower. Class B (20): the 11th value is at least 80, so at most 10
    # scores are below 80, hence at most 10 are 75 or lower.
    a_le75_min = 40 // 2
    b_le75_max = 20 // 2
    assert a_le75_min > b_le75_max
    return by_text(ch, 'More students in class A than in class B scored 75 or lower.')


def c11(ch):
    pct = {1: 25, 2: 35, 3: 20, 4: 15, 5: 5}
    people = sum(k * v for k, v in pct.items())
    big = sum(k * v for k, v in pct.items() if k >= 4)
    return pick(ch, F(big, people), conv=F)


def c12(ch):
    hits = [k for k, v in ch.items() if 'seriously ill' in v]
    assert len(hits) == 1
    return hits[0]


def c13(_):
    return F(30) * F(1, 10) * F(1, 5)


def c14(_):
    s = sp.Symbol('s')
    return F(int(sp.solve(sp.Eq((F(80, 100) - F(74, 100)) * s, 30 - 12), s)[0]))


CHECKS = {f'Q078-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14], 1)}
