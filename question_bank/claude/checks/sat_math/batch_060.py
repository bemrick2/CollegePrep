"""Scripted recomputation for SAT Math batch 60. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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


def solve2(a, b, c, d, e, f):
    det = a * e - b * d
    return F(c * e - b * f, det), F(a * f - c * d, det)


def c01(ch):
    # pick a concrete system with solution (2, 5), then solve the transformed one
    a, b, d, e = 3, 1, 1, -2
    c, f = a * 2 + b * 5, d * 2 + e * 5
    x, y = solve2(a, 2 * b, c + 3 * a, d, 2 * e, f + 3 * d)
    assert (x, y) == (5, F(5, 2))
    return by_text(ch, "(5, 5/2)")


def c02(ch):
    y = lambda x: (600 - 12 * F(x)) / 15
    assert y(0) - y(1) == F(4, 5)
    return [k for k, v in ch.items() if v.startswith("The number of pounds of Ethiopian beans the café must buy less of")][0]


def c03(_):
    ys = set()
    for a in [1, 2, 5, 7]:
        x, y = solve2(F(1, a), F(1, 6), 1, F(1, 2 * a), F(1, 4), 1)
        ys.add(y)
    assert len(ys) == 1
    return ys.pop()


def c04(_):
    a, b = F(1), F(-6)
    assert -b / a == 6
    return -2 * b / (3 * a)


def c05(_):
    return F(next(n for n in range(501, 100000) if F(12, 100) * 500 + F(8, 100) * (n - 500) == F(9, 100) * n))


def c06(ch):
    g = lambda x: 2 * x - 4
    f = lambda x: 7 * x + 1 - g(x)
    assert all(f(x) - 2 * g(x) == x + 13 for x in range(-5, 6))
    return by_text(ch, "f(x) = 5x + 5")


def c07(ch):
    p, q = solve2(4, 3, F(115, 100), 2, 5, F(95, 100))
    return pick(ch, (p - q) * 1000)


def c08(_):
    return F(next(p for p in range(1, 2000) if F(65, 100) * p - 40 >= 250))


def c09(ch):
    n = lambda p: 1500 - 15 * p
    return pick(ch, n(40) - n(F(48)))


def c10(ch):
    u = (F(10) - 2) / (F(3, 5) - F(1, 5))
    return pick(ch, u)


def c11(ch):
    for E in [2400, 1800, 900]:
        t = F(2400 - E, 300)
        assert 8 + F(18, 10) * t == F(224, 10) - F(6, 1000) * E
    return by_text(ch, "T = 22.4 − 0.006E")


def c12(ch):
    lo, hi = round((36 - 32) / 1.8, 1), round((46 - 32) / 1.8, 1)
    return by_text(ch, f"{lo} ≤ C ≤ {hi}")


def c13(_):
    for a in range(-5, 6):
        d = F(3, 2); b = a + d
        assert F((a + 6) - b, b - a) == 3
    return F(3, 2)


def c14(_):
    return F(80) * F(48, 16) * F(21, 10) * 60 / 1000


def c15(_):
    best = 0
    lows = [10, 20, 30, 40]
    for h6 in range(48, 80):
        for extra in range(0, 3):
            data = lows + [48] + [h6] * 4
            new = sorted(data + [50])
            med = F(new[4] + new[5], 2)
            assert sorted(data)[4] == 48
            best = max(best, med)
    return best


def c16(_):
    total = 50 * F(24, 10)
    return F(next(z for z in range(0, 50) if total / (50 - z) == 3))


def c17(ch):
    p0 = 100 - 75
    p1 = 110 - F(75) * F(108, 100)
    return pick(ch, (p1 - p0) / p0 * 100)


def c18(ch):
    return pick(ch, math.ceil(F(45, 10) / 6 / F(35, 1000)))


def c19(_):
    return F(next(x for x in range(0, 1000) if F(72 + x, 240 + x) == F(72, 120)))


def c20(ch):
    return [k for k, v in ch.items() if 'may differ from those that did not' in v][0]


def c21(_):
    return F(1500) * F(15, 100) * F(624, 10)


def c22(ch):
    per = F(6 * 3600, 45)
    return pick(ch, 18 * per / 60)


def c23(ch):
    return pick(ch, next(M for M in range(1, 100000) if F(25, 100) * F(12, 10) * M - F(2, 10) * M == 300))


def r01(ch):
    return pick(ch, round(1200 / 1.15 ** 4))


CHECKS = {f'Q060-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, r01], 1)}
