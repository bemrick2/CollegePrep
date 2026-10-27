"""Scripted recomputation for SAT Math batch 88. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))

x, a, b, c, k, d, th = sp.symbols('x a b c k d theta', real=True)


def by_text(ch, want):
    hits = [kk for kk, s in ch.items() if s == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    vals = {sp.nsimplify(sp.expand(r**3 - 5 * r)) for r in sp.solve(x**2 - 2 * x - 1, x)}
    assert vals == {2}
    return F(2)


def c02(_):
    s = sp.solve([a + b + c, 9 * a + 3 * b + c, c - 6], [a, b, c])
    f = s[a] * x**2 + s[b] * x + s[c]
    xv = sp.solve(sp.diff(f, x), x)[0]
    return F(int(f.subs(x, xv)))


def c03(ch):
    f = x**2 - 6 * x + 11
    g = sp.expand(8 - f)
    assert g == -x**2 + 6 * x - 3
    return by_text(ch, 'g(x) = −x² + 6x − 3')


def c04(ch):
    e = sp.simplify((x**2 + 5 * x + 6) / (x + 2) + (x**2 - 9) / (3 - x))
    assert e == 0
    return by_text(ch, '0')


def c05(ch):
    av = sp.nsolve(x**3 - 4 * x + 2 - 9, x, 2.5)
    val = (-av)**3 - 4 * (-av) + 2
    assert abs(val + 5) < 1e-9
    return by_text(ch, '−5')


def c06(ch):
    f = lambda t: 3 * 2**t
    r = F(f(3) - f(1), 2) / F(f(2) - f(0), 2)
    assert r == 2
    return by_text(ch, '2')


def c07(ch):
    for av in [-0.1, -1, -7]:
        kv = 1 - 4 * av
        f = lambda t: av * (t - 2)**2 + kv
        assert f(5) < 1 and abs(f(4) - 1) < 1e-12 and abs(f(5) - f(-1)) < 1e-12
    return by_text(ch, 'f(5) < 1')


def c08(ch):
    s = sp.solve(sp.Eq(th / 2 * 36 - th / 2 * 16, 5 * sp.pi), th)[0]
    assert s == sp.pi / 2
    return by_text(ch, 'π/2')


def c09(ch):
    hyp = 10
    area = sp.Rational(1, 2) * (hyp / 2) * (hyp / 2 * sp.sqrt(3))
    assert sp.simplify(area - 25 * sp.sqrt(3) / 2) == 0
    return by_text(ch, '25√3/2')


def c10(_):
    sols = sp.solve((k - 2)**2 + (3 - k)**2 - 25, k)
    return F(int(max(sols)))


def c11(_):
    return F(1, 2) * 12 * 12 * F(4, 10)


def c12(_):
    bc = 8 * F(3, 4)
    dv = sp.solve((8 - d)**2 - d**2 - bc**2, d)[0]
    return F(str(dv))


def c13(_):
    rem = F(120, 60) - F(30, 45)
    return F(90) / rem


CHECKS = {f'Q088-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13], 1)}
