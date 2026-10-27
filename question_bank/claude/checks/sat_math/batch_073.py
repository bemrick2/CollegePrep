"""Scripted recomputation for SAT Math batch 73. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import re
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402

x, y, k, t = sp.symbols('x y k t', real=True)


def expr(text):
    s = text.replace('−', '-').replace('π', '*pi').replace('²', '**2')
    s = re.sub(r'√(\d+)', r'*sqrt(\1)', s).replace('(*', '(').lstrip('*')
    s = re.sub(r'(^|[+\-(\s])\*', r'\1', s)
    return sp.sympify(s)


def same(ch, value):
    hits = [kk for kk, v in ch.items() if sp.simplify(expr(v) - value) == 0]
    assert len(hits) == 1, (value, ch)
    return hits[0]


def c01(ch):
    # two distinct positive roots of x^2-6x+c: test sample c values against each choice's set
    def ok(c):
        r = sp.solve(x**2 - 6 * x + c, x)
        return len(r) == 2 and all(v.is_real and v > 0 for v in r)
    samples = [F(-1), F(0), F(1, 2), F(5), F(9), F(10)]
    truth = [ok(c) for c in samples]
    tests = {'A': lambda c: c < 9, 'B': lambda c: 0 < c < 9, 'C': lambda c: 0 < c <= 9, 'D': lambda c: c > 0}
    hits = [kk for kk, f in tests.items() if [f(c) for c in samples] == truth and ch[kk] in ('c < 9', '0 < c < 9', '0 < c ≤ 9', 'c > 0')]
    assert len(hits) == 1, hits
    return hits[0]


def c02(_):
    ks = sp.solve(sp.Eq((k - 2)**2 - 4 * (k - 3), 0), k)
    sols = {sp.solve(x**2 + (kk - 2) * x + kk - 3, x)[0] for kk in ks}
    assert len(sols) == 1
    return F(int(sols.pop()))


def c03(_):
    A, B, C = sp.Matrix([0, 6]), sp.Matrix([8, 0]), sp.Matrix([0, 0])  # C at origin, A on y-axis, B on x-axis
    u = (B - A) / (B - A).norm()
    D = A + 4 * u
    n = sp.Matrix([-u[1], u[0]])
    s = sp.symbols('s')
    E = D + s * n
    sol = sp.solve(E[1], s)[0]  # E on BC (y = 0)
    Ept = E.subs(s, sol)
    assert 0 <= Ept[0] <= 8
    return F(str(sp.nsimplify((Ept - D).norm())))


def c04(_):
    b, h = 15, 10
    s = sp.solve(sp.Eq(s_ := sp.Symbol('s'), b * (h - s_) / h), s_)[0]
    return F(int(s))


def c05(ch):
    A = 180 - 45 - 30
    BC = 6 * sp.sqrt(2) * sp.sin(sp.rad(A)) / sp.sin(sp.rad(30))
    area = sp.Rational(1, 2) * 6 * sp.sqrt(2) * BC * sp.sin(sp.rad(45))
    return same(ch, sp.nsimplify(sp.simplify(area)))


def c06(_):
    a = sp.Symbol('a')
    small = sp.solve(sp.Eq(a + a * sp.Rational(9, 4), 52), a)[0]
    return F(int(small))


def c07(ch):
    sols = [s for s in sp.solve(sp.cos(t) + sp.Rational(1, 2), t) + [2 * sp.pi - s for s in sp.solve(sp.cos(t) + sp.Rational(1, 2), t)]
            if 0 <= s < 2 * sp.pi and sp.sin(s) < 0]
    sols = set(sols)
    assert len(sols) == 1
    return same(ch, sols.pop())


def c08(ch):
    px, py = sp.Rational(-3, 5), sp.Rational(4, 5)
    th = sp.atan2(py, px)
    q = (sp.nsimplify(sp.cos(th + sp.pi / 2)), sp.nsimplify(sp.sin(th + sp.pi / 2)))
    want = '(' + ', '.join(('−' if v < 0 else '') + str(float(abs(v))).rstrip('0') for v in q) + ')'
    hits = [kk for kk, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c09(ch):
    # sin A = cos B with A, B acute => A + B = 90, so C is right; AB = 10 hypotenuse, BC = 6 leg
    leg = sp.sqrt(10**2 - 6**2)
    return pick(ch, F(int(sp.Rational(1, 2) * 6 * leg)))


def c10(_):
    c = sp.Rational(28, 100)
    s = sp.sqrt(1 - c**2)
    return F(str(sp.nsimplify(c + s)))  # sin(90-x)=cos x, cos(90-x)=sin x


def c11(ch):
    g = x**2 + y**2 + 6 * x - 4 * y - 3
    cx = sp.solve(sp.diff(g, x), x)[0]
    cy = sp.solve(sp.diff(g, y), y)[0]
    r2 = cx**2 + cy**2
    hits = []
    for kk, v in ch.items():
        lhs, rhs = v.replace('−', '-').replace('²', '**2').split('=')
        e = sp.expand(sp.sympify(lhs, locals={'x': x, 'y': y}) - sp.sympify(rhs, locals={'x': x, 'y': y}))
        if sp.simplify(e - sp.expand((x - cx)**2 + (y - cy)**2 - r2)) == 0:
            hits.append(kk)
    assert len(hits) == 1, hits
    return hits[0]


def c12(ch):
    r, L = 3, 20
    v = sp.pi * r**2 * (L - 2 * r) + sp.Rational(4, 3) * sp.pi * r**3
    return same(ch, v)


def c13(_):
    import itertools
    n, m = 5, 2
    # voxelize at 0.5 cm: notch spans x in [1.5, 3.5] along the edge y = 0, z = 0
    sc = 2
    N = n * sc
    solid = set(itertools.product(range(N), repeat=3))
    for i in range(3 * sc // 2 * 1, 3 * sc // 2 * 1 + m * sc):
        for j in range(m * sc):
            for kk in range(m * sc):
                solid.discard((i, j, kk))
    faces = 0
    for (i, j, kk) in solid:
        for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            if (i + d[0], j + d[1], kk + d[2]) not in solid:
                faces += 1
    return F(faces, sc * sc)


CHECKS = {f'Q073-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13], 1)}
