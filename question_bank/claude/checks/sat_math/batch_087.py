"""Scripted recomputation for SAT Math batch 87. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import statistics
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))

m, t, x, y, a, b, v = sp.symbols('m t x y a b v', real=True)


def by_text(ch, want):
    hits = [kk for kk, s in ch.items() if s.startswith(want)]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(ch):
    cost = lambda d, mi: 25 * d + sp.Rational(15, 100) * mi
    diff = sp.simplify(cost(3, m) - cost(2, m + 100))
    assert diff == 10
    return by_text(ch, 'Trip A costs $10 more')


def c02(_):
    k = sp.Rational(-1, 4)
    assert sp.expand(k * (6 * x - 4 * y)) == sp.expand(y - sp.Rational(3, 2) * x)
    return F(str(k * 18))


def c03(ch):
    S = lambda tt: 30 - sp.Rational(3, 2) * tt
    assert sp.simplify(S(t) - S(t + 3)) == sp.Rational(9, 2)
    return by_text(ch, 'The decrease in snow depth, in centimeters, during any 3-hour period')


def c04(ch):
    from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
    tr = standard_transformations + (implicit_multiplication_application,)
    bad = []
    for kk, s in ch.items():
        lhs, rhs = s.replace('−', '-').split('=')
        e = parse_expr(lhs, local_dict={'x': x, 'y': y}, transformations=tr) - parse_expr(rhs, local_dict={'x': x, 'y': y}, transformations=tr)
        sol = sp.solve(e, y)
        if not sol or sp.simplify(sol[0] - (2 * x - 5)) != 0:
            bad.append(kk)
    assert len(bad) == 1, bad
    return bad[0]


def c05(ch):
    sa = sp.solve_univariate_inequality(3 < 4 * a - 5, a, relational=False)
    sb = sp.solve_univariate_inequality(3 > b - 8, b, relational=False)
    assert sa == sp.Interval.open(2, sp.oo) and sb == sp.Interval.open(-sp.oo, 11)
    return by_text(ch, 'a > 2 and b < 11')


def c06(ch):
    return by_text(ch, 'The predicted population increases by 40% each decade')


def c07(_):
    mid = F(38 + 44, 2)
    return mid / 100 * 1200


def c08(ch):
    return by_text(ch, 'Students chose whether to attend')


def c09(_):
    remaining = F(120, 60) - F(40, 50)
    return F(80) / remaining


def c10(ch):
    assert F(10 - 8, 8) == F(1, 4)
    return by_text(ch, 'It increased by 2 percentage points, which is an increase of 25 percent')


def c11(_):
    data = [2, 3, 4, 5, 20, 26]
    add = F(sum(data), len(data))
    new = sorted(data + [add])
    assert F(sum(new), 7) == add
    return F(statistics.median(new))


def c12(ch):
    p = F(10, 20 + 10)
    return by_text(ch, f'{p.numerator}/{p.denominator}')


def c13(ch):
    assert F(62, 100) * 500 == 310
    return by_text(ch, 'Exactly 310 of the 500')


CHECKS = {f'Q087-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13], 1)}
