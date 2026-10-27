"""Scripted recomputation for SAT Math batch 45. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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


def c01(ch):
    p = next(p for p in range(1, 1000) if F(85, 100) * p - 6 == F(80, 100) * p)
    return pick(ch, p)


def c02(ch):
    f6, f2 = F(30 + 10, 2), F(30 - 10, 2)
    m = (f6 - f2) / 4
    return pick(ch, float(f2 - 2 * m))


def c03(ch):
    xi = F(7 - 1, 3)
    assert 2 * xi + 1 == -xi + 7
    ks = [k for k in (F(n, 2) for n in range(5, 100)) if F(1, 2) * ((2 * k + 1) - (-k + 7)) * (k - xi) == 24]
    assert len(ks) == 1
    return pick(ch, float(ks[0]))


def c04(ch):
    y = lambda x: 50 + 4 * (x - 10)
    assert y(10) == 50 and y(0) == 10
    return by_text(ch, "The number of members 10 weeks after the club was formed")


def c05(_):
    rs = [r for r in range(1, 100) if math.isclose(math.pi * r * r * 2 * r, 2 * math.pi * r * r + 2 * math.pi * r * 2 * r)]
    assert rs == [3]
    return F(3)


def c06(_):
    ts = [t for t in range(0, 7) if -5 * t * t + 30 * t == 5 * t + 20]
    peak = F(30, 10)
    falling = [t for t in ts if t > peak]
    assert len(falling) == 1
    return F(5 * falling[0] + 20)


def c07(ch):
    a1, b1 = 500, F(4, 100) * 12500
    a2, b2 = 500, F(4, 100) * (12500 + b1)
    assert a1 == b1 and b2 > a2
    return by_text(ch, "During the first year, the increases are equal; during the second year, town B's increase is greater.")


def c08(ch):
    cands = {"x³ + 2x² + 4x + 8": lambda x: x ** 3 + 2 * x * x + 4 * x + 8, "x³ + 2x² − 4x − 8": lambda x: x ** 3 + 2 * x * x - 4 * x - 8,
             "x³ − 2x² + 4x − 8": lambda x: x ** 3 - 2 * x * x + 4 * x - 8, "x³ + 8": lambda x: x ** 3 + 8}
    hits = [t for t, f in cands.items() if all(f(F(x)) == F(x ** 4 - 16, x - 2) for x in (-3, -1, 0, 1, 3, 5))]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c09(ch):
    r = (F(1, 2) ** (12 // 4)) / (F(1, 2) ** (12 // 6))
    return by_text(ch, f"{r.numerator}/{r.denominator}")


def c10(ch):
    y = lambda x: 1.5 * x + 30
    pct = round((y(20) - y(10)) / y(10) * 100)
    return by_text(ch, f"{pct}%")


def c11(ch):
    both = 30 + 45 - (80 - 10)
    r = F(30 - both, 80 - 45)
    return by_text(ch, f"{r.numerator}/{r.denominator}")


def c12(_):
    b = c = 40
    bad = b  # AD = BD gives angle BAD = angle B
    return F(180 - b - c - bad)


def c13(_):
    ratio = math.sqrt(9 / (9 + 16))
    return F(round(25 - 25 * ratio, 9)).limit_denominator(10)


CHECKS = {f'Q045-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
