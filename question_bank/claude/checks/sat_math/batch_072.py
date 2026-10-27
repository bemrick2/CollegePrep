"""Scripted recomputation for SAT Math batch 72. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402

x = sp.symbols('x', real=True)


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    sols = sp.solve(sp.Eq(x**2, 2 * x + 3), x)
    for s in sols:
        assert sp.simplify(2**(s**2) - 8 * 4**s) == 0
    return F(int(sum(sols)))


def c02(ch):
    good = sorted(v for v in range(1, 50) if sp.sqrt(3 * v + 1) - sp.sqrt(v - 1) == 2)
    want = '{' + ', '.join(str(v) for v in good) + '}'
    return by_text(ch, want)


def c03(_):
    t = sp.symbols('t')
    vert = F(1, 2) * (F(1, 2) + F(5, 2))
    other = 2 * vert - 4
    h = -16 * (t - 4) * (t - other)
    assert h.subs(t, sp.Rational(1, 2)) == h.subs(t, sp.Rational(5, 2)) and h.subs(t, 4) == 0
    return F(int(h.subs(t, 0)))


def c04(ch):
    a, b = -1, 2
    r = lambda v: -(v * v) - 1  # a quadratic entirely below the x-axis
    p = lambda v: (v - a) * (v - b) * r(v)
    assert all(p(F(v, 10)) > 0 for v in range(-9, 20))
    assert p(5) < 0
    return [k for k, v in ch.items() if v.startswith('p(x) > 0 for all x such that a < x < b')][0]


def c05(ch):
    f = lambda v: 5 - (v - 2) ** 2  # any f with max 5 at x = 2
    g = lambda v: -2 * f(v - 3) + 1
    vals = {v: g(F(v, 10)) for v in range(-50, 150)}
    vmin = min(vals.values())
    at = [k for k, val in vals.items() if val == vmin]
    assert vmin == -9 and at == [50]
    return by_text(ch, 'g has a minimum value of −9 at x = 5.')


def c06(_):
    ks = []
    for r in (3, -3):
        assert 4 * r * r == 36
        ks.append(-(r + 4 * r))
    return F(max(ks))


def c07(ch):
    e = (x + 1) / x - x / (x + 1)
    forms = {'−1': -1, '1/(x² + x)': 1 / (x**2 + x), '(2x + 1)/(x² + x)': (2 * x + 1) / (x**2 + x), '(−2x − 1)/(x² + x)': (-2 * x - 1) / (x**2 + x)}
    ok = [t for t, f in forms.items() if sp.simplify(e - f) == 0]
    assert len(ok) == 1
    return by_text(ch, ok[0])


def c08(_):
    s = sp.solve(sp.Eq(4**(x + 1) - 4**x, 96), x)
    return F(sp.Rational(s[0]))


def c09(_):
    H = sp.symbols('H')
    return F(int(sp.solve(sp.Eq(H * (1 - sp.Rational(225, 400)), 7), H)[0]))


def c10(ch):
    s = sp.solve(sp.Eq((x - 1) / (x + 1), (x + 1) / (x - 1)), x)
    assert s == [0]
    return by_text(ch, 'x = 0 only')


def c11(ch):
    bad = []
    for k in range(-10, 11):
        if not sp.solve(sp.Eq(3 / (x - 1), k / (x + 2)), x):
            bad.append(k)
    assert bad == [0, 3]
    return by_text(ch, '0 and 3')


def c12(ch):
    e = 2 * x / (x - 3) + 6 / (3 - x)
    assert sp.simplify(e) == 2
    return pick(ch, 2)


def c13(_):
    k = sp.simplify((2 * x**2 + 7 * x + 9) - (2 * x + 3) * (x + 2))
    return F(int(k))


CHECKS = {f'Q072-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13], 1)}
