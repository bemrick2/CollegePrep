"""Scripted recomputation for SAT Math batch 74. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import itertools
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402

x, y, a, b, k, t = sp.symbols('x y a b k t', real=True)


def by_text(ch, want):
    hits = [kk for kk, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    sols = [s for s in sp.solve(sp.Eq((-8 / a) * (2 / a), -1), a) if s > 0]
    assert len(sols) == 1
    return F(int(sols[0]))


def c02(_):
    n = 0
    for A in range(1, 200):
        for B in range(1, 200):
            if F(3, A) + F(4, B) == 1:
                n += 1
    return F(n)


def c03(ch):
    d = sp.solve(sp.Eq(sp.Symbol('m'), 0.4 * x + 12), x)[0]
    slope = sp.nsimplify(sp.diff(d, sp.Symbol('m')))
    return by_text(ch, f"{float(slope):g}; the crystal takes {float(slope):g} days to gain each gram.")


def c04(ch):
    good = []
    for kv in sp.solve(sp.Eq(k * (k + 1), 6), k):
        s = sp.solve([kv * x + 2 * y - 6, 3 * x + (kv + 1) * y - 9], [x, y], dict=True)
        if s == []:
            good.append(int(kv))
    want = ' and '.join(str(v).replace('-', '−') for v in sorted(good)) + (' only' if len(good) == 1 else '')
    return by_text(ch, want)


def c05(ch):
    tt = sp.solve(sp.Eq(F(3) + F(2, 5) * t, F(12, 5) + F(3, 10) * t), t)[0]
    h = F(3) + F(2, 5) * tt
    assert tt == -6 and h == F(3, 5)
    # both trees existed then: planted 7.5 and 8 years before
    assert F(3) / F(2, 5) >= 6 and F(12, 5) / F(3, 10) >= 6
    return by_text(ch, "The trees had the same height 6 years before the measurements, when each was 0.6 meter tall.")


def c06(ch):
    hits = []
    for kk, v in ch.items():
        px, py = (num(s) for s in v.strip('()').split(','))
        if py > 0 and py < px and py < -2 * px + 12:
            hits.append(kk)
    assert len(hits) == 1
    return hits[0]


def c07(_):
    p = sp.solve(sp.Eq(12 * x, 8 * x + F(6, 5)), x)[0]
    return F(str(8 * p))


def c08(_):
    return F(sum(1 for s, l in itertools.product(range(1, 7), range(1, 5)) if 2 * s + 3 * l <= 12))


def c09(_):
    A, B, C = sp.symbols('A B C')
    s = sp.solve([A + B - 41, B + C - 47, A + C - 50], [A, B, C])
    return F(int(max(s.values())))


def c10(_):
    v1, v3 = F(80), F(5, 8) * 80
    slope = (v3 - v1) / 2
    return v1 - slope


def c11(ch):
    m = sp.solve(sp.Eq(x, 3 * y - 6), y)[0]
    xs = sp.solve(sp.Eq(3 * x - 6, m), x)
    return pick(ch, F(int(xs[0])))


def c12(ch):
    hits = []
    for kk, v in ch.items():
        bv = sp.nsimplify(num(v))
        s = sp.solve([y - 2 * x - 1, y + x / 2 - bv], [x, y])
        if s[x] < 0 and s[y] > 0:
            hits.append(kk)
    assert len(hits) == 1
    return hits[0]


def c13(_):
    f = lambda z: 2 * z + 3
    g = lambda z: a * z + 1
    e = sp.expand(f(g(x)) - g(f(x)))
    sol = sp.solve(sp.Poly(e, x).coeffs(), a)
    return F(str(sol[a] if isinstance(sol, dict) else sol[0]))


def c14(ch):
    rem = int((F('128') - F('22.5')) * 1000)
    return by_text(ch, f"4x + 120y ≤ {rem:,}")


def c15(_):
    q, r = sp.div(2 * x**2 + 7 * x + 9, x + 2, x)
    assert q == 2 * x + 3
    return F(int(r))


CHECKS = {f'Q074-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15], 1)}
