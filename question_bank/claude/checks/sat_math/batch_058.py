"""Scripted recomputation for SAT Math batch 58. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    ns = [n for n in range(1, 200) if 6 <= F(108, n) <= F(15, 2)]
    assert ns == [15, 16, 17, 18]
    return F(len(ns))


def c02(ch):
    xs, ys = [1, 4, 6, 9, 13], [5, 14, 21, 29, 41]
    fixes = []
    for i in range(5):
        pts = [(x, y) for j, (x, y) in enumerate(zip(xs, ys)) if j != i]
        (x0, y0), (x1, y1) = pts[0], pts[1]
        m = F(y1 - y0, x1 - x0)
        if all(y == y0 + m * (x - x0) for x, y in pts):
            fixes.append(y0 + m * (xs[i] - x0))
    assert len(fixes) == 1
    return pick(ch, fixes[0])


def c03(ch):
    for s in range(5, 15):
        lm, lw = F(s + 22, 3), F(2 * s + 41, 6)
        assert lm - lw == F(1, 2)
    return by_text(ch, "The man's foot is 0.5 inch longer.")


def c04(_):
    d = F(20) / (F(1) / F(7, 2) - F(1, 6))
    assert d / F(7, 2) == 48 and d / 6 == 28
    return d


def c05(ch):
    extra = (F(210) - 4 * 35) / F(1, 4)
    return pick(ch, 400 + extra)


def c06(ch):
    t = (F(42) - 2 - 8 * F(3, 4)) / 8
    return pick(ch, t * 60)


def c07(ch):
    return pick(ch, F(60, 2) + F(20) / F(1, 2))


def c08(ch):
    C = lambda w: F(9, 2) + F(4, 5) * w
    W = lambda b: F(3, 2) + F(3, 5) * b
    assert C(W(0)) == F(57, 10) and C(W(1)) - C(W(0)) == F(48, 100)
    return by_text(ch, "5.70 + 0.48b")


def c09(ch):
    k = (27 + 273) * F(22, 20)
    return pick(ch, k - 273)


def c10(ch):
    return pick(ch, F(36, 100) * F(78000, 12) - 500)


def c11(ch):
    # solve for b, c from P(6) = P(14) = 2250 with leading coefficient -40
    b = F(-40) * -1 * (6 + 14)
    c = 2250 + 40 * 36 - 6 * b
    P = lambda p: -40 * p * p + b * p + c
    assert P(14) == 2250
    return pick(ch, max(P(F(p, 100)) for p in range(0, 3001)))


def c12(_):
    best = max(F(4 * t, 1000) + 2 * (16 - F(t, 1000) ** 2) for t in range(0, 4001))
    return best


def c13(ch):
    ages = [a for a in range(1, 40) if F(a, a + 12) in (F(1, 4), F(3, 7))]
    assert ages == [4, 9]
    return pick(ch, ages[1] - ages[0])


def c14(ch):
    C = lambda p: F(120 * p, 100 - p)
    return pick(ch, C(80) / C(40))


def c15(_):
    xs = [x for x in range(1, 30) if x * (60 - 2 * x) == 400]
    assert xs == [10, 20]
    return F(max(60 - 2 * x for x in xs))


def c16(ch):
    # f(x) = (x - r)(x - s); g(x) = f(x + 5) has zeros r - 5, s - 5 = {-r, -s}
    hits = set()
    for r10 in range(-100, 101):
        for s10 in range(-100, 101):
            r, s = F(r10, 2), F(s10, 2)
            if r != s and {r - 5, s - 5} == {-r, -s}:
                hits.add((r + s) / 2)
    assert hits == {F(5, 2)}
    return by_text(ch, "5/2")


def c17(_):
    f3 = F(int(math.isqrt(144)))
    b2 = F(48) / f3
    b = F(int(math.isqrt(int(b2))))
    assert b * b == b2
    A = f3 / b ** 3
    f = lambda x: A * b ** x
    assert f(2) * f(4) == 144 and f(5) == 48
    return f(1)


def c18(_):
    sols = []
    for a in range(-50, 6):
        u, v = math.sqrt(5 - a), math.sqrt(13 - a)
        if abs(v - u - 2) < 1e-12:
            sols.append(a)
    assert sols == [4]
    a = 4
    b = 3 - math.sqrt(5 - a)
    return F(int(round(math.sqrt(29 - a) + b)))


def c19(ch):
    for a, b in [(2, -5), (3, 10), (1, 3), (-2, 7)]:
        disc = b * b - 4 * a * a
        if disc < 0:
            continue
        for sgn in (1, -1):
            r = (-b + sgn * math.sqrt(disc)) / (2 * a)
            q = 1 / r
            assert abs(a * q * q + b * q + a) < 1e-9
    return by_text(ch, "1/r")


def c20(_):
    known = [F(60, 10), F(75, 10), F(80, 10), F(95, 10)]
    hits = []
    for x10 in range(0, 101):
        x = F(x10, 10)
        s = sorted(known + [x])
        if sum(s[1:4]) / 3 == 8:
            hits.append(x)
    assert hits == [F(17, 2)]
    return hits[0]


def c21(ch):
    d = 10 - F(60) / F(13, 2)
    return pick(ch, round(float(d), 2))


def c22(ch):
    A = 120 * 80
    return pick(ch, A * (F(4, 10) * F(5, 2) + F(6, 10)))


def c23(ch):
    return pick(ch, 3000 - 600 * F(12, 5))


def c24(_):
    s = next(s for s in range(1, 100) if F(s ** 3, 5000) > 9)
    return F(s)


def c25(ch):
    arc = 30 * F(2, 3)  # in units of pi
    ang = arc / 12
    assert ang == F(5, 3)
    return by_text(ch, "5π/3")


def c26(_):
    rs = []
    for x in (8, -8):
        assert x * x + 15 * 15 == 17 * 17
        r = math.hypot(28 - x, 15)
        assert abs(17 - r) < 28 < 17 + r
        rs.append(r)
    return F(int(round(max(rs))))


def c27(_):
    return F(102, 10) ** 2 - F(98, 10) ** 2


def c28(ch):
    # tangent from origin to circle centre (5,0) radius 3: discriminant of (1+m^2)x^2 - 10x + 16 = 0
    m = F(3, 4)
    assert 100 - 4 * (1 + m * m) * 16 == 0
    return by_text(ch, "3/4")


def c29(_):
    xs = [x for x in range(-50, 51) if (x - 3) ** 2 + (x + 4) ** 2 == 289]
    assert sorted(xs) == [-12, 11]
    x = next(x for x in xs if x - 3 > 0 and x + 4 > 0)
    return F(x - 3, x + 4)


CHECKS = {f'Q058-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15,
                                                    c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29], 1)}
