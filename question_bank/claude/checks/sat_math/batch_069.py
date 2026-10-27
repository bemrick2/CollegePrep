"""Scripted recomputation for SAT Math batch 69. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import itertools
import math
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def rad(text):
    return float(sp.sympify(text.replace('π', '*pi').replace('^', '**').lstrip('*')))


def deg(text):
    return num(text.replace('°', ''))


def c01(ch):
    minute, hour = 30 * 6, 2 * 30 + 30 * 0.5
    a = abs(minute - hour)
    a = min(a, 360 - a)
    return pick(ch, math.radians(a), conv=rad)


def c02(_):
    R, half = 12, math.pi / 6
    r = R / (1 / math.sin(half) + 1)
    d = r / math.sin(half)
    assert abs(d + r - R) < 1e-12
    return F(round(r, 9)).limit_denominator()


def c03(_):
    r = sp.symbols('r', positive=True)
    th = 2 * sp.pi / 3
    return F(int(sp.solve(sp.Eq(r**2 * th / 2, r * th), r)[0]))


def c04(ch):
    s = F(3)
    small = 27 * 6 * (s / 3) ** 2
    return pick(ch, small / (6 * s * s))


def c05(ch):
    ext = [360 * F(k, 12) for k in (3, 4, 5)]
    return pick(ch, min(180 - e for e in ext), conv=deg)


def c06(ch):
    k = sp.Rational(3, 5)
    val = sp.sqrt(1 - k**2) / k
    forms = {t: sp.sympify(t.replace('√', 'sqrt').replace('²', '**2').replace('k', '(3/5)').replace('−', '-')) for t in ch.values()}
    ok = [t for t, e in forms.items() if sp.simplify(e - val) == 0]
    assert len(ok) == 1
    return by_text(ch, ok[0])


def c07(_):
    xs = [v for v in range(1, 30) if (v - 5) ** 2 + 144 == 169]
    ys = [v for v in range(1, 30) if 25 + (v - 12) ** 2 == 169]
    assert xs == [10] and ys == [24]
    return F(xs[0] * ys[0], 2)


def c08(_):
    cpd = F(8)
    ratio = F(12, 6)
    return cpd + cpd * ratio**2 + 2 * cpd * ratio


def c09(ch):
    v1 = F(1, 3) * 4**2 * 3
    v2 = F(1, 3) * 3**2 * 4
    return pick(ch, float((v1 - v2)) * math.pi, conv=rad)


def c10(ch):
    A, B, C, D = map(sp.Matrix, ([0, 3], [-7, 0], [0, -7], [7, 0]))  # diagonals AC = 10 (vertical) and BD = 14 (horizontal), perpendicular
    pts = [(A + B) / 2, (B + C) / 2, (C + D) / 2, (D + A) / 2]
    area = abs(sum(pts[i][0] * pts[(i + 1) % 4][1] - pts[(i + 1) % 4][0] * pts[i][1] for i in range(4))) / 2
    assert (A - C).norm() == 10 and (B - D).norm() == 14
    return pick(ch, F(int(area * 2), 2))


def c11(ch):
    base = math.hypot(3, 4)
    diag = math.hypot(base, 12)
    return pick(ch, base / diag)


CHECKS = {f'Q069-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11], 1)}
