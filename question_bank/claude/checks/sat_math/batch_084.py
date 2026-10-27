"""Scripted recomputation for SAT Math batch 84. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))

x, y, k, b, c, r, a, L, T, g, d, s = sp.symbols('x y k b c r a L T g d s', real=True)


def by_text(ch, want):
    hits = [kk for kk, v in ch.items() if v.startswith(want)]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(ch):
    sol = sp.solve(sp.Eq(T, 2 * sp.pi * sp.sqrt(L / g)), L)
    assert len(sol) == 1 and sp.simplify(sol[0] - g * T**2 / (4 * sp.pi**2)) == 0
    return by_text(ch, 'L = gT²/(4π²)')


def c02(_):
    sols = [v for v in sp.solve((30 - x) * (20 - x) - 336, x) if 0 < v < 20]
    assert len(sols) == 1
    return F(int(sols[0]))


def c03(ch):
    f = lambda t: 1 / (1 - t)
    expr = sp.simplify(f(f(x)))
    assert sp.simplify(expr - (x - 1) / x) == 0
    return by_text(ch, '(x − 1)/x')


def c04(_):
    vx = -b / 2
    vy = vx**2 + b * vx + c
    slope = sp.simplify((c - vy) / (0 - vx))
    assert sp.simplify(slope - b / 2) == 0
    return F(int(sp.solve(sp.Eq(slope, -3), b)[0]))


def c05(_):
    av = sp.solve(sp.Eq(a * (0 + 1) * (0 - 5), -5), a)[0]
    f = av * (x + 1) * (x - 5)
    sol = sp.solve_univariate_inequality(f < -5, x, relational=False)
    assert sol == sp.Interval.open(0, 4)
    return F(int(sol.sup))


def c06(_):
    sols = sp.solve([sp.Eq(b + c, -b), sp.Eq(b * c, c)], [b, c], dict=True)
    good = [s_ for s_ in sols if s_[b] != 0 and s_[c] != 0 and s_[b] != s_[c]]
    assert len(good) == 1
    bb, cc = good[0][b], good[0][c]
    assert set(sp.solve(x**2 + bb * x + cc, x)) == {bb, cc}
    return F(int(cc))


def c07(ch):
    disc = sp.expand(k**2 - 4 * (k + 3))
    sol = sp.solve_univariate_inequality(disc < 0, k, relational=False)
    assert sol == sp.Interval.open(-2, 6)
    return by_text(ch, '−2 < k < 6')


def c08(_):
    sols = [v for v in sp.solve(3**2 + (1 + r)**2 - (2 + r)**2, r) if v > 2]
    assert len(sols) == 1
    return F(int(sols[0]))


def c09(_):
    A2, B2, C2 = sp.symbols('A2 B2 C2', positive=True)
    s_ = sp.solve([A2 + B2 - 13, A2 + C2 - 40, B2 + C2 - 45], [A2, B2, C2])
    assert (s_[A2], s_[B2], s_[C2]) == (4, 9, 36)
    return F(int(sp.sqrt(s_[A2] + s_[B2] + s_[C2])))


def c10(_):
    dd = sp.symbols('dd', positive=True)
    dv = [v for v in sp.solve(sp.Eq(sp.Rational(1, 2) * 3 * dd * 4 * dd, 54), dd) if v > 0][0]
    sides = [3 * dv, 4 * dv, 5 * dv]
    assert sides[0]**2 + sides[1]**2 == sides[2]**2 and sides[1] - sides[0] == sides[2] - sides[1]
    return F(int(sum(sides)))


def c11(ch):
    rv = [v for v in sp.solve(sp.Rational(1, 2) * r * r * sp.sqrt(3) - 18 * sp.sqrt(3), r) if v > 0][0]
    assert rv == 6
    return by_text(ch, '6')


def c12(_):
    rv = sp.solve(sp.Eq(r, 6 - (2 * r) / 2), r)[0]
    vol = sp.pi * rv**2 * (2 * rv)
    return F(int(vol / sp.pi))


def c13(ch):
    return by_text(ch, 'The means vary by chance')


CHECKS = {f'Q084-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13], 1)}
