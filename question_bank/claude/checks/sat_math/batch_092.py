"""Scripted recomputation for SAT Math batch 92. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))

a, b, k, x, n, s = sp.symbols('a b k x n s', real=True)


def by_text(ch, want):
    hits = [kk for kk, t in ch.items() if t.startswith(want)]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    sols = sp.solve([2 / a + 6 / b - 1, a * b / 2 - 25], [a, b], dict=True)
    bs = [d[b] for d in sols if d[a] > 0 and d[b] > 0]
    assert len(bs) == 2
    return F(int(max(bs)))


def c02(_):
    sol = sp.solve([b - (2 * a + 1), a - (3 * b - 13)], [a, b])
    return F(int(sol[b]))


def c03(_):
    sol = sp.solve_univariate_inequality((x + 4) / 3 - (x - 2) / 5 < 4, x, relational=False)
    assert sol == sp.Interval.open(-sp.oo, 17)
    return F(16)


def c04(_):
    sol = sp.solve([(a + b) * (a - b) - 45, a - b - 3], [a, b], dict=True)[0]
    return F(int(sol[a] + sol[b]))


def c05(_):
    sols = [v for v in sp.solve(1 / x + 1 / (x + 2) - sp.Rational(5, 12), x) if v > 0]
    return F(int(sols[0] + 2))


def c06(_):
    c = sp.Symbol('c')
    sol = [d for d in sp.solve([a + c - 5, a * b + c - 11, a * b**2 + c - 29], [a, b, c], dict=True) if d[b] > 0][0]
    return F(int(sol[a] * sol[b]**3 + sol[c]))


def c07(_):
    nv = sp.solve(30 * n + 50 - 32 * (n + 1), n)[0]
    return F(int(30 * nv + 6), int(nv + 1))


def c08(ch):
    sv = sp.solve(sp.Rational(8, 10) * s + sp.Rational(3, 10) * (1 - s) - sp.Rational(65, 100), s)[0]
    assert sv == sp.Rational(7, 10)
    return by_text(ch, '70%')


def c09(_):
    h = sp.Symbol('h')
    hv = sp.solve((1 - h)**2 + (7 - 2 * h)**2 - (5 - h)**2 - (3 - 2 * h)**2, h)[0]
    return F(int((1 - hv)**2 + (7 - 2 * hv)**2))


def c10(_):
    arc = F(216, 360) * 2 * 15
    r = arc / 2
    hgt = sp.sqrt(15**2 - r**2)
    return F(1, 3) * r**2 * int(hgt)


def c11(_):
    xint = F(24, 3)
    return F(24) / (xint / 2)


def c12(ch):
    import random
    random.seed(3)
    for _ in range(300):
        low = sorted(random.randint(40, 75) for _ in range(12))
        high = sorted(random.randint(77, 90) for _ in range(8)) + sorted(random.randint(91, 100) for _ in range(4))
        d = low + [76] + high
        nd = [min(v + 10, 100) for v in d]
        assert sorted(nd)[12] - sorted(d)[12] == 10 and sum(nd) - sum(d) < 250
    return by_text(ch, 'The median increased by exactly 10 points, and the mean increased by less than 10 points.')


def c13(ch):
    return by_text(ch, 'The percent of the students who did not earn an A in algebra who attended the tutoring program')


CHECKS = {f'Q092-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13], 1)}
