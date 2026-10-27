"""Scripted recomputation for SAT Math batch 79. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402

x, c, k = sp.symbols('x c k', real=True)


def by_text(ch, want):
    hits = [kk for kk, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(ch):
    m = F(4 - (-2), 3 - 0)
    sol = sp.solve_univariate_inequality(c < sp.Rational(m.numerator, m.denominator) * c - 2, c, relational=False)
    assert sol == sp.Interval.open(2, sp.oo)
    return by_text(ch, 'c > 2')


def c02(ch):
    a, b = 1, 3
    slope = F(a - b, b - a)
    kk = b - slope * a
    assert kk == a + b
    return by_text(ch, 'f(0) = a + b')


def c03(ch):
    s = sp.solve(sp.Eq(x * sp.Rational(1, 2) * sp.Rational(2, 3) + 12, x - 8), x)[0]
    return pick(ch, F(int(s)))


def c04(ch):
    mean = sp.simplify(((2 * x + 1) + (3 * x - 4) + (x + 9)) / 3)
    assert sp.solve(sp.Eq(mean, 2 * x + 3), x) == []
    return by_text(ch, 'There are no such values of x.')


def c05(ch):
    return by_text(ch, f'W = {int(18 * 1.5)}n + 240')


def c06(_):
    return F(18, 60) * 600 + F(32, 80) * 400


def c07(_):
    filled, t = 0, 0
    while True:
        for minute in range(10):
            filled += 40
            t += 1
            if filled >= 1800:
                return F(t)
        t += 2


def c08(ch):
    hits = [n for n in range(1, 51) if 3 * n + 4 > 110 and (3 * n + 4) % 2 == 0]
    return pick(ch, F(len(hits), 50), conv=F)


def c09(_):
    flour, butter = F(300) * 5 / 2, F(300) * 3 / 2
    return (flour - 500) + (butter - 300)


def c10(ch):
    lo, hi = round(49 / 1.02, 2), round(49 / 0.98, 2)
    return by_text(ch, f'{lo:.2f} ≤ w ≤ {hi:.2f}')


def c11(ch):
    C = F(100)
    B = C * F(7, 10)
    A = B * F(5, 4)
    pct = (C - A) / A * 100
    return pick(ch, F(str(round(float(pct), 1))), conv=lambda t: F(t.replace('%', '')))


def c12(ch):
    hits = []
    for kk, v in ch.items():
        xs = [int(s) for s in v.split(';')[0].replace('x:', '').split(',')]
        ys = [int(s) for s in v.split(';')[1].replace('y:', '').split(',')]
        if len({F(yv, xv) for xv, yv in zip(xs, ys)}) == 1:
            hits.append(kk)
    assert len(hits) == 1
    return hits[0]


CHECKS = {f'Q079-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
