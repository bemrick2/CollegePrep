"""Scripted recomputation for SAT Math batch 86. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))

a, b, n, s, v = sp.symbols('a b n s v', real=True)


def by_text(ch, want):
    hits = [kk for kk, t in ch.items() if t.startswith(want)]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    sol = sp.solve([2 * a + 3 * b - 12, 6 * a + 1 * b - 12], [a, b])
    return F(str(sol[a] + sol[b]))


def c02(_):
    r0, d = sp.symbols('r0 d')
    sol = sp.solve([3 * r0 + 3 * d - 45, 3 * (r0 + 3 * d) + 3 * d - 63], [r0, d])
    return F(int(sol[r0] + 6 * sol[d]))


def c03(_):
    sol = sp.solve([a + b - 150, a - b - 30], [a, b])
    t = F(1500, 150)
    return F(int(sol[b])) * t


def c04(_):
    return F(int(sp.solve(480 * (300 - n) + 360 * n - 117600, n)[0]))


def c05(ch):
    s18 = 100
    inc = F(25, 100) * s18
    pct = (s18 + 2 * inc) / (s18 + inc) - 1
    assert pct == F(1, 5)
    return by_text(ch, '20%')


def c06(_):
    pred = lambda x: 3.2 * 1.3**x
    ratio = pred(7) * 1.1 / (pred(6) * 0.9)
    return F(round((ratio - 1) * 100))


def c07(ch):
    assert F(62, 100) * 500 == 310
    return by_text(ch, 'Exactly 310')


def c08(ch):
    return by_text(ch, 'Volunteering likely causes higher satisfaction for adults like those in study 2')


def c09(ch):
    blue = 1 * F(1, 4) + 2 * F(2, 5)
    frac = blue / 3
    assert frac == F(7, 20)
    return by_text(ch, '7/20')


def c10(_):
    pages = F(12) / F(8, 10) * 50
    return F(3000) / pages


def c11(ch):
    import random
    random.seed(1)
    for _ in range(200):
        lows = sorted(random.sample(range(-50, 20), 5))
        highs = sorted(random.sample(range(21, 90), 5))
        data = lows + [20] + highs
        new = [x - 5 for x in lows] + [20] + [x + 5 for x in highs]
        assert sum(new) == sum(data) and (max(new) - min(new)) - (max(data) - min(data)) == 10
    return by_text(ch, 'The mean is the same, and the range is 10 greater')


def c12(_):
    slope = (F(92, 10) - F(42, 10)) / 10
    return slope * 16 + F(42, 10)


CHECKS = {f'Q086-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
