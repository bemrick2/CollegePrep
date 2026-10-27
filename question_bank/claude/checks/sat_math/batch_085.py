"""Scripted recomputation for SAT Math batch 85. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))

x, y, k, n, w = sp.symbols('x y k n w', real=True)


def by_text(ch, want):
    hits = [kk for kk, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    good = [kv for kv in range(-20, 21) if len(set(sp.solve((x - 3) * (x + 2) - kv * (x - 3), x))) == 1]
    assert good == [5]
    return F(5)


def c02(_):
    sols = [v for v in sp.solve(n * (n - 1) / 2 - 78, n) if v > 0]
    return F(int(sols[0]))


def c03(_):
    area = w * (8 - sp.Rational(8, 10) * w)
    wv = sp.solve(sp.diff(area, w), w)[0]
    return F(str(area.subs(w, wv)))


def c04(ch):
    xv = sp.nsolve(2**(x + 1) * 3**(x - 1) - 16, x, 1)
    val = sp.Rational(16) * sp.Rational(3, 2)
    assert abs(6**xv - val) < 1e-9
    return by_text(ch, '24')


def c05(ch):
    sols = sp.solve((sp.Symbol('t'))**2 - 5 * sp.Symbol('t') + 6, sp.Symbol('t'))
    sols = [s for s in sols if s != 2]
    assert sols == [3]
    return by_text(ch, '3')


def c06(_):
    hv = sp.solve(sp.Eq((sp.Rational(1, 2))**(10 / y), sp.Rational(1, 32)), y)
    return F(int([v for v in hv if v > 0][0]))


def c07(ch):
    area = sp.pi * (6**2 - 2**2 - 4**2) / 2
    assert sp.simplify(area - 8 * sp.pi) == 0
    return by_text(ch, '8π')


def c08(ch):
    assert (6 // 2)**3 == 27
    return by_text(ch, '27')


def c09(_):
    ang = 360 - 60 - F(180 * 8, 10)
    return 360 / (180 - ang)


def c10(ch):
    pq = sp.sqrt(24**2 + 7**2)
    assert pq == 25
    return by_text(ch, '7/25')


def c11(ch):
    eb = sp.sqrt(10**2 - 6**2)
    return by_text(ch, str(6 + eb))


def c12(_):
    a, b = sp.symbols('a b')
    pts = [(1, 2), (13, 2), (1, 7)]
    r2 = sp.Symbol('r2')
    s_ = sp.solve([(px - a)**2 + (py - b)**2 - r2 for px, py in pts], [a, b, r2], dict=True)[0]
    return F(str(sp.sqrt(s_[r2])))


def c13(_):
    AB, CD = 15, 10
    ratio = F(AB, AB + CD)
    return ratio * CD * 2


def c14(_):
    h1 = 17 * F(8, 17)
    base2 = 17 * F(8, 17)
    h2 = sp.sqrt(17**2 - base2**2)
    return F(int(h2)) - h1


CHECKS = {f'Q085-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14], 1)}
