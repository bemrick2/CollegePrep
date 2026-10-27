"""Scripted recomputation for SAT Math batch 77. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402

x, t, a, b = sp.symbols('x t a b', real=True)


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(ch):
    tv = sp.solve(sp.Eq(1000 * 2**(t / 5), 1000 * (1 + 7)), t)[0]
    return pick(ch, F(int(tv)))


def c02(ch):
    cands = {'P(t) = 400(1.21)ᵗ': lambda s: 400 * 1.21**s, 'P(t) = 400(1.1)ᵗ': lambda s: 400 * 1.1**s,
             'P(t) = 400(1.1)^(t/2)': lambda s: 400 * 1.1**(s / 2), 'P(t) = 400 + 42t': lambda s: 400 + 42 * s}
    rows = [(0, 400), (2, 484), (5, 644.204)]
    hits = [k for k, v in ch.items() if all(abs(cands[v](s) - p) < 1e-6 for s, p in rows)]
    assert len(hits) == 1
    return hits[0]


def c03(ch):
    h, kk = sp.Rational(-3), sp.Rational(-5)
    assert sp.expand((x - h)**2 + kk - (x**2 + 6 * x + 4)) == 0
    return by_text(ch, '3 units left and 5 units down')


def c04(_):
    m = (16 - (-1)) / F(4)
    xs = sp.solve(sp.Eq(x**2, sp.Rational(m.numerator, m.denominator) * x - 1), x)
    other = [s for s in xs if s != 4]
    return F(str(other[0]))


def c05(_):
    sol = sp.solve([1 + a + b, 16 + 4 * a + b], [a, b])
    p = x**4 + sol[a] * x**2 + sol[b]
    assert sp.rem(p, x**2 - 3 * x + 2, x) == 0
    return F(int(sol[b]))


def c06(ch):
    ok = [v for v in range(-10, 11) if math.sqrt((v**2 - 4) + 4) == v]
    assert min(ok) == 0 and max(ok) == 10
    return by_text(ch, 'x ≥ 0')


def c07(ch):
    r, pa = 6, 8
    po = math.hypot(r, pa)
    return pick(ch, F(str(round(2 * r * pa / po, 6))))


def c08(_):
    h, xx = sp.symbols('h xx', positive=True)
    s = sp.solve([sp.Eq(h / xx, sp.Rational(9, 15)), sp.Eq(h / (15 - xx), sp.Rational(6, 15))], [h, xx], dict=True)[0]
    return F(str(s[h]))


def c09(_):
    cob = 2 * 25
    return F(180 - 90 - cob)


def c10(ch):
    r = math.sqrt(5**2 - 4**2)
    return pick(ch, F(int(round(r * r * 8))) , conv=lambda s: num(s.replace('π', '')))


def c11(ch):
    sinx = 0.6
    return pick(ch, F(int(round(50 * sinx))))


def c12(ch):
    ac = 6 / (math.sqrt(3) / 2)
    ad = ac * math.sqrt(2)
    hits = [k for k, v in ch.items() if abs(num(v) - ad) < 1e-9]
    assert len(hits) == 1
    return hits[0]


def c13(_):
    import cmath
    A, B = complex(0, 0), complex(1, 0)
    C, Dp = complex(1, 1), complex(0, 1)
    P = A + (B - A) * cmath.exp(1j * math.pi / 3)
    v1, v2 = P - Dp, C - Dp
    ang = math.degrees(abs(cmath.phase(v1 / v2)))
    return F(str(round(ang, 6)))


def c14(_):
    a_ang = 64
    b_ang = 180 - a_ang
    return 180 - F(a_ang, 2) - F(b_ang, 2)


CHECKS = {f'Q077-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14], 1)}
