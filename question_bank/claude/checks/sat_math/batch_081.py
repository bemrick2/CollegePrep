"""Scripted recomputation for SAT Math batch 81. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402

x, r, t = sp.symbols('x r t', real=True)


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    sols = [s for s in sp.solve(sp.Eq(120 / r + 120 / (r + 20), 5), r) if s > 0]
    assert len(sols) == 1
    return F(int(sols[0]))


def c02(ch):
    e = sp.expand((x + 2)**3 - x**3)
    assert e == 6 * x**2 + 12 * x + 8
    return by_text(ch, '6x² + 12x + 8')


def c03(_):
    sols = [s for s in sp.solve(sp.Eq(1 / (x - 1) - 1 / (x + 1), sp.Rational(1, 12)), x) if s > 0]
    return F(int(sols[0]))


def c04(_):
    k = sp.solve(sp.Eq(9 * sp.Symbol('k') - sp.Symbol('k'), 32), sp.Symbol('k'))[0]
    return F(int(k * 25))


def c05(ch):
    s = sp.solve(sp.Eq(2 * 2**x, 2**5), x)[0]
    return pick(ch, F(int(s)), conv=lambda v: F(v))


def c06(ch):
    # vertex (2, -5) -> (5, 0); upward parabola touching the x-axis once
    f = lambda z: (z - 2)**2 - 5
    g = sp.expand(f(x - 3) + 5)
    roots = sp.solve(g, x)
    return by_text(ch, str(len(set(roots))))


def c07(ch):
    ok = []
    for a in (-2, 2):
        for b in (F(1, 2), F(3)):
            if a * b > 0 and a * b**2 < a * b:
                ok.append((a > 0, b < 1))
    assert ok == [(True, True)]
    return by_text(ch, 'a > 0 and 0 < b < 1')


def c08(_):
    return F(10 * 20 * 6, 20 * 30)


def c09(ch):
    sols = [s for s in sp.solveset(sp.sin(t) + sp.cos(t), t, sp.Interval.Ropen(0, 2 * sp.pi))]
    total = sp.nsimplify(sum(sols))
    assert total == sp.Rational(5, 2) * sp.pi
    return by_text(ch, '5π/2')


def c10(ch):
    rest = 1 - F(2, 5)**2 - F(3, 5)**2
    return pick(ch, rest, conv=F)


def c11(_):
    h = math.sqrt(5**2 - 4**2)
    area = 0.5 * 8 * h
    alt = 2 * area / 5
    s = alt / 5
    cosC = (25 + 25 - 64) / 50
    assert abs(s - math.sqrt(1 - cosC**2)) < 1e-12
    return F(str(round(s, 6)))


def c12(ch):
    return pick(ch, F(int(math.hypot(6, 8))), conv=lambda v: F(v) if '√' not in v else F(-1))


def c13(ch):
    hits = [k for k, v in ch.items() if 'percentage points' in v and v.startswith('Each year')]
    assert len(hits) == 1
    return hits[0]


CHECKS = {f'Q081-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13], 1)}
