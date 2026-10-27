"""Scripted recomputation for SAT Math batch 76. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
import os
import re
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402

x, u, m, k = sp.symbols('x u m k', real=True)


def expr(text):
    s = text.replace('−', '-').replace('π', '*pi').replace('√', 'sqrt').replace('²', '**2').replace('³', '**3')
    s = re.sub(r'sqrt(\d+)', r'sqrt(\1)', s)
    s = re.sub(r'(\d)(sqrt|x|\()', r'\1*\2', s)
    s = re.sub(r'\)\s*\(', ')*(', s)
    s = re.sub(r'x\(', 'x*(', s)
    s = re.sub(r'(^|[(/+\-])\*pi', r'\1pi', s)
    return sp.sympify(s, locals={'x': x})


def same(ch, value):
    hits = [kk for kk, v in ch.items() if sp.simplify(expr(v) - value) == 0]
    assert len(hits) == 1, (value, ch)
    return hits[0]


def c01(_):
    f = lambda t: (t - 2)**2 + 3  # a quadratic with f(t) = f(4 - t)
    g = lambda t: f(2 * t - 6)
    ks = [kk for kk in range(-20, 21) if sp.expand(g(x) - g(kk - x)) == 0]
    assert len(ks) == 1
    return F(ks[0])


def c02(_):
    sols = [s for s in sp.solve(sp.Eq(x**2 - 4 * x, 2 * sp.sqrt(x**2 - 4 * x + 8)), x)]
    sols = [s for s in sols if abs(complex(sp.N((s**2 - 4 * s) - 2 * sp.sqrt(s**2 - 4 * s + 8)))) < 1e-9 and s.is_real]
    return F(str(sp.nsimplify(sp.simplify(sum(sols)))))


def c03(ch):
    return same(ch, sp.simplify((x**3 - 8) / (x**2 - 4) - (x**2 + 4) / (x + 2)))


def c04(ch):
    xs = [s for s in sp.solve(x - 1 / x - 3, x) if s > 0]
    return same(ch, sp.nsimplify(sp.simplify(xs[0]**2 - 1 / xs[0]**2)))


def c05(_):
    R = (12 + x) * (360 - 15 * x)
    xv = sp.solve(sp.diff(R, x), x)[0]
    return F(int(12 + xv))


def c06(ch):
    return same(ch, sp.simplify((1 - 1 / x) * (1 - 1 / (x + 1)) * (1 - 1 / (x + 2))))


def c07(ch):
    f = lambda t: (t + 1) / (t - 1)
    target = sp.simplify(f(1 / x))
    opts = {'f(x)': f(x), '1/f(x)': 1 / f(x), '−1/f(x)': -1 / f(x), '−f(x)': -f(x)}
    hits = [kk for kk, v in ch.items() if sp.simplify(opts[v] - target) == 0]
    assert len(hits) == 1
    return hits[0]


def c08(_):
    ms = set()
    for yv in sp.solve(16 + sp.Symbol('y')**2 - 25):
        ms.add(F(int(yv) - 5, 4))
    return sum(ms)


def c09(ch):
    comp = sp.factor((x + 2)**2 - 4 * (x + 2))
    sol = sp.solve_univariate_inequality(comp < 0, x, relational=False)
    want = f"{str(sol.start).replace('-', '−')} < x < {sol.end}"
    hits = [kk for kk, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c10(_):
    out = set()
    for a_ang in (64, 116):
        b_ang = 180 - a_ang
        out.add(180 - F(a_ang, 2) - F(b_ang, 2))
    assert len(out) == 1
    return out.pop()


def c11(ch):
    bae = 180 - 50 - 75
    return pick(ch, F(bae), conv=lambda t: F(t.replace('°', '')))


def c12(ch):
    return same(ch, sp.Rational(45, 60) * 2 * sp.pi)


def c13(_):
    h = F(360, 72)
    return 2 * (8 * 9 + 8 * h + 9 * h)


def c14(_):
    cd = F(6) * F(6, 12)
    return 12 - cd


def c15(ch):
    m_, d = sp.symbols('m d')
    sol = sp.solve(sp.Eq(m_, F(2, 5) * d + 12), d)[0]
    slope = sp.diff(sol, m_)
    want = f"{float(slope):g}; the crystal takes {float(slope):g} days to gain each gram."
    hits = [kk for kk, v in ch.items() if v == want]
    assert len(hits) == 1
    return hits[0]


def c16(_):
    q, r = sp.div(2 * x**2 + 7 * x + 9, x + 2, x)
    return F(int(r))


def c17(ch):
    hits = [kk for kk, v in ch.items() if v.startswith('For patients like those in the study, taking drug A likely causes fewer symptom days than taking drug B')]
    assert len(hits) == 1
    return hits[0]


CHECKS = {f'Q076-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17], 1)}
