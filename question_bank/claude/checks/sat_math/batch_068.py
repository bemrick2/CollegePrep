"""Scripted recomputation for SAT Math batch 68. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
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
    k = sp.symbols('k', positive=True)
    lhs = sp.expand((x**2 - k * x + 9) * (x**2 + k * x + 9))
    sol = sp.solve(sp.Eq(lhs.coeff(x, 2), 2), k)
    assert sol == [4]
    return F(4)


def c02(ch):
    expr = 1 / (sp.sqrt(x) - 1) - 1 / (sp.sqrt(x) + 1)
    cands = {'2/(x − 1)': 2 / (x - 1), '2/(x + 1)': 2 / (x + 1), '−2/(x − 1)': -2 / (x - 1), '2√x/(x − 1)': 2 * sp.sqrt(x) / (x - 1)}
    ok = [t for t, e in cands.items() if all(abs(float((expr - e).subs(x, v))) < 1e-12 for v in (2, 5, 9.5))]
    assert len(ok) == 1
    return by_text(ch, ok[0])


def c03(_):
    sols = [8 + 1, -8 + 1]
    for s in sols:
        r = math.copysign(abs(s - 1) ** (1 / 3), s - 1)
        assert abs(r * r - 4) < 1e-9
    return F(min(sols))


def c04(_):
    y = sp.symbols('y')
    xy = sp.solve(sp.Eq(8 / y, sp.Rational(4, 3)), y)[0]
    return F(int(64 - 2 * xy))


def c05(_):
    sols = sp.solve(sp.Eq((x - 3)**2, (2 * x + 1)**2), x)
    return F(sp.Rational(sum(sols)))


def c06(ch):
    f = x**2 + 4 * x
    sols = sp.solve(sp.Eq(f.subs(x, f), 0), x)
    return pick(ch, len(set(sols)))


def c07(ch):
    g = 4 * sp.Rational(1, 2)**x
    for a in (-1, 0.5, 2, 3.7):
        assert abs(float(g.subs(x, 2 - a) - 2**a)) < 1e-9
    return by_text(ch, 'g(x) = 4(0.5)^x')


def c08(_):
    f = x**2 - 2
    g = 2 * x + 1
    sols = sp.solve(sp.Eq(f.subs(x, g), g.subs(x, f)), x)
    assert sols == [-1]
    return F(-1)


def c09(ch):
    for v in (0.5, 2, 7):
        assert abs(math.sqrt(9 * v) - 3 * math.sqrt(v)) < 1e-12
    return by_text(ch, 'A vertical stretch by a factor of 3')


def c10(_):
    k = sp.symbols('k')
    bad = [kv for kv in range(-20, 21) if not sp.solve(sp.Eq((3 * x + 2) / (x - 4), kv), x)]
    assert bad == [3]
    return F(3)


def c11(ch):
    P = lambda t: -t * t + 6 * t - 5
    return pick(ch, max(P(F(t, 100)) for t in range(400, 701)))


def c12(_):
    good = []
    for k in range(2, 20):
        xs = sp.solve(sp.Eq(k * x, (x**2 - 9) / (x - 3)), x)
        if not xs:
            good.append(k)
    assert good == [2]
    return F(2)


def c13(_):
    bs = {p + 12 // p for p in range(-12, 13) if p != 0 and 12 % p == 0}
    return F(len(bs))


def c14(_):
    p = sp.symbols('p', positive=True)
    return F(int(sp.solve(sp.Eq((1 + p / 100) * (1 - p / 100), sp.Rational(91, 100)), p)[0]))


def c15(_):
    d = x**2 - (6 * x - 13)
    v = sp.solve(sp.diff(d, x), x)[0]
    assert not sp.solve(sp.Eq(x**2, 6 * x - 13), x)
    return F(int(d.subs(x, v)))


def c16(ch):
    f = (x - 1) * (x - 5)
    assert f.subs(x, 0) == 5
    g = f.subs(x, x / 2)
    v = sp.solve(sp.diff(g, x), x)[0]
    return pick(ch, F(int(g.subs(x, v))))


def c17(ch):
    p = (x + 1) * (x - 2) * (x - 3)
    return pick(ch, len(set(sp.solve(p * p.subs(x, x - 1), x))))


def c18(ch):
    def pop(t):
        return 2000 * 1.1**min(t, 5) * 0.9**max(t - 5, 0)
    forms = {'2,000(1.1)^5(0.9)^t': lambda t: 2000 * 1.1**5 * 0.9**t, '2,000(1.1)^5(0.9)^(t − 5)': lambda t: 2000 * 1.1**5 * 0.9**(t - 5),
             '2,000(0.99)^t': lambda t: 2000 * 0.99**t, '2,000(1.1)^t(0.9)^(t − 5)': lambda t: 2000 * 1.1**t * 0.9**(t - 5)}
    ok = [k for k, fn in forms.items() if all(abs(fn(t) - pop(t)) < 1e-6 for t in (5, 6, 9, 14))]
    assert len(ok) == 1
    return by_text(ch, ok[0])


CHECKS = {f'Q068-{i:02d}': f for i, f in enumerate(
    [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17, c18], 1)}
