"""Scripted recomputation for SAT Math batch 83. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402

x, c, n, a = sp.symbols('x c n a', real=True)


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v.startswith(want)]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    return F(min(k for k in range(1, 12) if 12 * 11 < 15 * k))


def c02(_):
    s = sp.solve([sp.Eq(c * n, (c - 30) * (n + 2)), sp.Eq(c * n, (c + 30) * (n - 1))], [c, n], dict=True)
    s = [d for d in s if d[n] > 0][0]
    return F(int(s[c] * s[n]))


def c03(ch):
    err = (2 * x + 30) - (sp.Rational(18, 10) * x + 32)
    sol = sp.solve_univariate_inequality(sp.Abs(err) <= 2, x, relational=False)
    assert sol == sp.Interval(0, 20)
    return by_text(ch, '0 ≤ C ≤ 20')


def c04(ch):
    m = (3 * a - 2 * a) / (2 * a - a)
    b = 2 * a - m * a
    return by_text(ch, str(sp.simplify(m * 5 * a + b)).replace('*', ''))


def c05(ch):
    return by_text(ch, 'The means vary by chance')


def c06(_):
    need = F(52, 100) * 7000 - F(46, 100) * 5000
    return need / 2000 * 100


def c07(_):
    mid_sum = 10 * 18 - 4 * 10 - 4 * 27
    return F(mid_sum, 2)


def c08(ch):
    return by_text(ch, 'The 55 finishers chose')


def c09(ch):
    return pick(ch, F(1200 * 60, 2500), conv=lambda t: F(t.replace(',', '')))


def c10(_):
    v1 = F(12) / F(12, 10)
    t_meet = F(18) / v1
    v2 = F(12) / t_meet
    return F(18) / v2


def c11(ch):
    return pick(ch, F(85, 100) * 4000 * F(40, 100) / 400, conv=F)


CHECKS = {f'Q083-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11], 1)}
