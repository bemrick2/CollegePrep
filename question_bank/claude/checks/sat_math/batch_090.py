"""Scripted recomputation for SAT Math batch 90. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import statistics
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))

x, y, k = sp.symbols('x y k', real=True)


def by_text(ch, want):
    hits = [kk for kk, s in ch.items() if s == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(ch):
    yl = sp.solve(4 * x - 3 * y - 24, y)[0]
    new = yl.subs(x, x - 2) + 3
    assert new.subs(x, 0) == sp.Rational(-23, 3)
    return by_text(ch, '−23/3')


def c02(_):
    xs = set()
    for sgn in (1, -1):
        xs |= set(sp.solve(2 * x - 6 - sgn * x, x))
    return F(int(sum(xs)))


def c03(_):
    s = sp.solve([3 * x - 2 * y - k, x + 4 * y - 2 * k, x + y - 13], [x, y, k])
    return F(int(s[k]))


def c04(_):
    return F(min(F(100 - 5 * 12, 2), F(75 - 2 * 12, 3)).__floor__())


def c05(_):
    slope = F(11 - 5, 2 * 3 - 2)
    return 5 - 2 * slope


def c06(_):
    f = lambda t: 10 + 2 * (t - 2)
    g = lambda t: 4 + 4 * (t - 2)
    p = sp.solve(f(x) - g(x), x)[0]
    assert f(p) == g(p)
    return F(int(f(p)))


def c07(ch):
    rows = {'10': [14, 22, 12], '11': [26, 18, 16], '12': [20, 30, 42]}
    cols = ['band', 'choir', 'orchestra']
    ct = [sum(r[i] for r in rows.values()) for i in range(3)]
    hits = [(g, cols[i]) for g, r in rows.items() for i in range(3) if F(r[i], sum(r)) == F(r[i], ct[i])]
    assert hits == [('11', 'band')]
    return by_text(ch, 'Grade 11 and band')


def c08(ch):
    return by_text(ch, 'The percent of the students who did not earn an A in algebra who attended the tutoring program')


def c09(ch):
    base = [0] * 12 + [1] * 15 + [2] * 11 + [3] * 7
    meds, modes, means = set(), set(), set()
    for top in ([4] * 5, [9] * 5, [4, 5, 6, 7, 8]):
        d = base + top
        meds.add(statistics.median(d)); modes.add(statistics.mode(d)); means.add(F(sum(d), 50))
    assert len(meds) == 1 and len(modes) == 1 and len(means) > 1
    return by_text(ch, 'I and III only')


def c10(ch):
    g, b = 18 + 8, 12 + 16
    r = F(g, b)
    return by_text(ch, f'{r.numerator} to {r.denominator}')


def c11(_):
    dv = F(12) / F(15, 100)
    return dv - F(25, 10) * 12


def c12(_):
    return (16 * 4 + 1) - (15 * 4 + 3)


CHECKS = {f'Q090-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
