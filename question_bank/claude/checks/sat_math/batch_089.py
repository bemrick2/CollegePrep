"""Scripted recomputation for SAT Math batch 89. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))

x, h, t, k, a = sp.symbols('x h t k a', real=True)


def by_text(ch, want):
    hits = [kk for kk, s in ch.items() if s == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(ch):
    f = lambda u: 3 * u**2 - 2
    assert sp.expand(f(x + h) - f(x)) == 6 * x * h + 3 * h**2
    return by_text(ch, '6xh + 3h²')


def c02(ch):
    xv = 2 * t - 1
    assert sp.expand(xv**2 + 2 * xv) == 4 * t**2 - 1
    return by_text(ch, '4t² − 1')


def c03(_):
    vals = {sp.nsimplify(sp.expand(r * (r + 1) * (r + 3) * (r + 4))) for r in sp.solve(x**2 + 4 * x - 6, x)}
    assert vals == {54}
    return F(54)


def c04(_):
    sols = [s for s in sp.solve((16 - k**2) - 10 * (4 - k), k) if s != 4]
    assert sols == [6]
    return F(6)


def c05(ch):
    f = (x - 1) * (x - 5)
    neg = sp.solve_univariate_inequality(f < 0, x, relational=False)
    fall = sp.solve_univariate_inequality(sp.diff(f, x) < 0, x, relational=False)
    assert neg.intersect(fall) == sp.Interval.open(1, 3)
    return by_text(ch, '1 < x < 3')


def c06(_):
    sols = [s for s in sp.solve((a + 1) - a * (a - 3), a) if s != 3]
    return F(int(sp.nsimplify(sum(sols))))


def c07(ch):
    ab = sp.sqrt(8**2 + 15**2)
    assert ab == 17
    return by_text(ch, '8.5')


def c08(ch):
    import numpy as np
    p, q = np.array([1, 2]), np.array([7, 6])
    cen = (p + q) / 2
    v = q - cen
    cands = {tuple(cen + np.array([-v[1], v[0]])), tuple(cen - np.array([-v[1], v[0]]))}
    assert (2.0, 7.0) in cands
    return by_text(ch, '(2, 7)')


def c09(ch):
    r = sp.Symbol('r', positive=True)
    assert sp.solve(sp.Eq(r * sp.Symbol('th'), 2 * r), sp.Symbol('th')) == [2]
    return by_text(ch, '2')


def c10(ch):
    total = sp.Rational(1, 2) * 2 * sp.pi * 3 * 10 + 2 * sp.Rational(1, 2) * sp.pi * 9 + 6 * 10
    assert sp.simplify(total - (39 * sp.pi + 60)) == 0
    return by_text(ch, '39π + 60')


def c11(ch):
    ae = sp.sqrt(8**2 + 6**2)
    assert F(8, int(ae)) == F(4, 5)
    return by_text(ch, '0.8')


def c12(ch):
    rem = 6**3 - F(1, 3) * F(1, 2) * 6 * 6 * 6
    assert rem == 180
    return by_text(ch, '180')


CHECKS = {f'Q089-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
