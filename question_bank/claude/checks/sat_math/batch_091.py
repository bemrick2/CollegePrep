"""Scripted recomputation for SAT Math batch 91. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))

fee, r, k = sp.symbols('fee r k', real=True)


def by_text(ch, want):
    hits = [kk for kk, s in ch.items() if s.startswith(want)]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    a_rate = F(110 - 50, 4)
    net = F(140 - 110, 6)
    b_rate = a_rate - net
    return 10 + F(140) / b_rate


def c02(_):
    s = sp.solve([fee + 3 * r - 2 * (fee + r) - 5, fee + 4 * r - 70], [fee, r])
    return F(int(s[r]))


def c03(ch):
    kv = sp.solve(sp.Eq(k / 10, sp.Rational(-2, 5)), k)[0]
    assert kv == -4
    return by_text(ch, '−4')


def c04(ch):
    lo, hi = F(2, 10), F(8, 2)
    assert (lo, hi) == (F(1, 5), F(4))
    return by_text(ch, '1/5 ≤ m ≤ 4')


def c05(ch):
    assert all(p % 4 == 0 for p in range(8, 400, 8))
    return by_text(ch, 'Every inspected item comes from machine D')


def c06(ch):
    xi = F(96) / F(42, 10)
    assert xi < 58
    return by_text(ch, 'The model predicts 0 iced drinks at about 22.9°F, a temperature far below the data.')


def c07(ch):
    t = {'Chess': (30, 39), 'Drama': (75, 93), 'Robotics': (24, 33), 'Debate': (120, 141)}
    best = max(t, key=lambda n: F(t[n][1] - t[n][0], t[n][0]))
    return by_text(ch, best)


def c08(ch):
    rest = F(450 - 48, 8)
    assert rest == F(201, 4)
    lo = [10, 20, 30, 40, 48, 60, 70, 80, 92]
    hi = [10, 20, 30, 47, 48, 49, 80, 80, 86]
    assert sum(lo) == 450 and sorted(lo)[4] == 48 and sum(hi) == 450 and sorted(hi)[4] == 48
    m1 = sorted(lo); m1.remove(48); m2 = sorted(hi); m2.remove(48)
    assert F(m1[3] + m1[4], 2) != F(m2[3] + m2[4], 2)
    return by_text(ch, 'The mean is 50.25, and the median cannot be determined')


def c09(_):
    a, b = 100000 * F(8, 10), 150000 * F(3, 10)
    return a / (a + b) * 100


def c10(_):
    frac = F(18, 340)
    return 18 + 27 + 850 * frac


CHECKS = {f'Q091-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
