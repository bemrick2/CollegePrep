"""Scripted recomputation for SAT Math batch 82. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import statistics
import sys
from fractions import Fraction as F

import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402

x, y, a, b, c = sp.symbols('x y a b c', real=True)


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v.startswith(want)]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(ch):
    base = (15, 10, 900)
    facts = {'A': (2, 3, 170), 'B': (3, 2, 180), 'C': (6, 4, 360), 'D': (18, 12, 1080)}
    unique = [k for k, (p, q, r) in facts.items() if sp.Matrix([[15, 10], [p, q]]).det() != 0]
    assert len(unique) == 1
    s = sp.solve([15 * x + 10 * y - 900, 2 * x + 3 * y - 170], [x, y])
    assert s == {x: 40, y: 30}
    return unique[0]


def c02(_):
    s = sp.solve([(a + b) / 2 - 30, (a + 2 * b) / 3 - 25], [a, b])
    xa = sp.solve(sp.Eq(s[a] / 100 * x + s[b] / 100 * (12 - x), sp.Rational(40, 100) * 12), x)[0]
    return F(int(xa))


def c03(_):
    P = sp.Symbol('P')
    return F(str(sp.solve(sp.Eq(sp.Rational(1, 10) * P, sp.Rational(3360 - 2880, 100)), P)[0]))


def c04(_):
    best = max(l for l in [F(n, 10) for n in range(0, 501)] if l + (l + 8) <= 50)
    return best


def c05(_):
    sols = set()
    for cv in [v for v in range(-10, 11) if v != 3]:
        s = sp.solve(sp.Eq(cv * x + 12, 3 * x + 4 * cv), x)
        assert len(s) == 1
        sols.add(s[0])
    assert len(sols) == 1
    return F(int(sols.pop()))


def c06(_):
    m = F(28 - 10, 9 - 3)
    bb = 10 - 3 * m
    return sum(m * k + bb for k in range(1, 12))


def c07(ch):
    return pick(ch, F(35, 1000) * 1200)


def c08(ch):
    X = np.array([0, 1, 3, 4, 6, 7.0])
    Y = np.array([12.0, 14.6, 19.9, 22.4, 27.8, 30.5])
    m, b0 = np.polyfit(X, Y, 1)
    assert max(abs(Y - (m * X + b0))) < 0.2 and abs(m - 2.6) < 0.1
    return by_text(ch, 'A linear model, because y increases by about 2.6')


def c09(ch):
    counts = [a1 + b1 for a1, b1 in zip([6, 5, 2, 3, 4], [1, 3, 3, 4, 13])]
    data = [s for s, n in zip(range(1, 6), counts) for _ in range(n)]
    return pick(ch, F(str(statistics.median(data))), conv=lambda t: F(t) if 'About' not in t else F(-1))


def c10(_):
    water = 3 + F(12, 100) * 5
    return water / 8 * 100


def c11(ch):
    rows = [(1, 1350, 600), (1, 1200, 650), (1, 1420, 720), (1, 1100, 580), (2, 1800, 950), (2, 2100, 1000), (2, 1950, 1050), (2, 2000, 980)]
    q = [r for r in rows if F(r[1], r[2]) < 2]
    return pick(ch, F(sum(1 for r in q if r[0] == 2), len(q)), conv=F)


def c12(ch):
    pts = [(0, 0), (5, 90), (20, 300), (30, 420), (45, 600)]
    rates = [F(v2 - v1, t2 - t1) for (t1, v1), (t2, v2) in zip(pts, pts[1:])]
    i = rates.index(max(rates))
    assert rates.count(max(rates)) == 1
    return by_text(ch, f'From t = {pts[i][0]} to t = {pts[i + 1][0]}')


CHECKS = {f'Q082-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
