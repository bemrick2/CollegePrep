"""Scripted recomputation for SAT Math batch 80. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402

x, k, u = sp.symbols('x k u', real=True)


def by_text(ch, want):
    hits = [kk for kk, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(ch):
    f = sp.expand((4 * x**2 - 6 * x + 1).subs(x, u / 2)).subs(u, x)
    assert sp.expand(f.subs(x, 2 * x) - (4 * x**2 - 6 * x + 1)) == 0
    return by_text(ch, 'f(x) = x² − 3x + 1')


def c02(_):
    f = lambda t: t**2 - 4 * t
    sols = [s for s in sp.solve(sp.Eq((f(k) - f(1)) / (k - 1), 5), k) if s != 1]
    assert len(sols) == 1
    return F(int(sols[0]))


def c03(ch):
    sol = sp.solve_univariate_inequality(12 / (x - 2) + 3 > 5, x, relational=False).intersect(sp.Interval.open(2, sp.oo))
    assert sol == sp.Interval.open(2, 8)
    return by_text(ch, '2 < x < 8')


def c04(_):
    s = sp.solve(sp.Eq(x**2 + 3, (x + 3)**2), x)
    assert len(s) == 1
    return F(int(s[0]))


def c05(_):
    e = sp.expand((x + k) * (x - 3) - (x - k) * (x + 3) - 10 * x)
    return F(int(sp.solve(sp.Poly(e, x).coeffs(), k)[k]))


def c06(_):
    c = sp.Symbol('c')
    vx = sp.Rational(8, 2)
    vy = vx**2 - 8 * vx + c
    return F(int(sp.solve(sp.Eq(vy, vx), c)[0]))


def c07(_):
    a, b = sp.solve(x**2 - 7 * x + 5, x)
    return F(int(sp.simplify(a**2 + b**2)))


def c08(_):
    cosA = sp.Rational(5, 13)
    sinA = sp.sqrt(1 - cosA**2)
    ac = 60 / sinA
    return F(int(sp.nsimplify(ac / cosA)))


def c09(_):
    a = sp.Symbol('a')
    return F(int(sp.solve(sp.Eq(a + 2 * a + 2 * a, 180), a)[0]))


def _val(t):
    import re
    t = t.strip().replace('−', '-')
    t = re.sub(r'√(\d+)', r'sqrt(\1)', t)
    t = re.sub(r'(\d)sqrt', r'\1*sqrt', t)
    return float(sp.sympify(t))


def c10(ch):
    want = (round(4 * math.cos(5 * math.pi / 6), 9), round(4 * math.sin(5 * math.pi / 6), 9))
    hits = []
    for kk, v in ch.items():
        px, py = (_val(t) for t in v.strip('()').split(','))
        if abs(px - want[0]) < 1e-6 and abs(py - want[1]) < 1e-6:
            hits.append(kk)
    assert len(hits) == 1
    return hits[0]


def c11(ch):
    # Place A at the top of a circle of radius 5 centered at the origin; find B on the circle with AB = 8.
    A = (0, 5)
    y = sp.Symbol('y')
    yb = [s for s in sp.solve(sp.Eq((sp.sqrt(25 - y**2))**2 + (y - 5)**2, 64), y)][0]
    xb = math.sqrt(25 - float(yb)**2)
    return pick(ch, F(str(round(2 * xb, 6))))


def c12(_):
    h = sp.Symbol('h')
    return F(str(sp.solve(sp.Eq(h / 30, sp.Rational(16, 10) / 2), h)[0]))


def c13(ch):
    ht = math.sqrt(2.5**2 - 2**2)
    return pick(ch, F(str(round(0.5 * 4 * ht * 3, 6))))


CHECKS = {f'Q080-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13], 1)}
