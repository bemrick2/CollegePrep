"""Scripted recomputation for SAT Math batch 62. Multiple-choice checks return a letter; SPR checks receive None and return the value.
Statistics-reasoning items (Q062-12, 15, 16, 18, 21) are checked by locating the keyed reasoning and, where numeric, recomputing the supporting quantity."""
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


def starts(ch, prefix):
    hits = [k for k, v in ch.items() if v.startswith(prefix)]
    assert len(hits) == 1, (prefix, ch)
    return hits[0]


def c01(_):
    b = 5  # no solution needs equal x-coefficients
    a = (F(5 * 6) - (b + 1) * 6 - 15) / 5
    assert -5 * a != 15
    return a


def c02(_):
    return F(20) / F(8, 10)


def c03(ch):
    C = lambda h, p: 150 + h * (40 + 2 * p)
    assert C(1, 11) - C(1, 10) == 2 and C(3, 11) - C(3, 10) == 6
    return starts(ch, "The amount, in dollars, by which the hourly charge increases")


def c04(_):
    return F(next(L for L in range(0, 200) if L >= F(6, 10) * (L + 15)))


def c05(ch):
    t = F(100 - 20, 3 + 2)
    return pick(ch, float(F(8, 10) * t))


def c06(_):
    bill = lambda g: 3 * min(g, 5) + 5 * max(g - 5, 0)   # g in thousands
    target = 2 * bill(8)
    return F(next(g for g in range(0, 100) if bill(g) == target) * 1000)


def c07(ch):
    s = (F(39) - F(2550, 100)) / (4 - 2)
    return pick(ch, s)


def c08(_):
    x = next(x for x in range(-50, 51) if 5 * x - 8 == 2 * x + (27 - 4 * x))
    return F(27 - 4 * x)


def c09(_):
    T = (85 - F(3, 10) * 92) / F(7, 10)
    return F(math.ceil(4 * T - 3 * 78))


def c10(_):
    return F(next(s for s in range(10000, 100000, 100) if 2000 + F(7, 100) * (s - 10000) >= 2400 + F(3, 100) * s))


def c11(ch):
    D = lambda t: (1500 - 12 * t) - (900 - 4 * t)
    assert all(D(t) == 600 - 8 * t for t in range(0, 50))
    return starts(ch, "The number of meters per minute by which the difference between the hikers' elevations decreases")


def c12(ch):
    return starts(ch, "The increase cannot be attributed to the fertilizer, because the fertilizer's effect cannot be separated")


def c13(_):
    resin_ml = F(230) / F(115, 100)
    return resin_ml / 2 * F(95, 100)


def c14(_):
    survive = F(75, 100) * F(80, 100)
    return F(25, 100) / (1 - survive) * 100


def c15(ch):
    return starts(ch, "Without a comparison group")


def c16(ch):
    lo, hi = 48 - 4, 48 + 4
    return starts(ch, f"It is plausible that between about {lo}% and {hi}%")


def c17(ch):
    shared = F(4, 10) * 2160 / 3
    by_area = F(6, 10) * 2160 * F(14, 36)
    return pick(ch, shared + by_area)


def c18(ch):
    sd = math.sqrt(16 + 25)
    assert sd > 4
    return by_text(ch, "It is greater than 4.")


def c19(ch):
    return pick(ch, (F(6, 10) * F(11, 10) + F(4, 10) * F(95, 100) - 1) * 100, conv=lambda s: float(s.replace('−', '-').rstrip('%')))


def c20(_):
    k = math.isqrt(24000000 // 6)
    assert 6 * k * k == 24000000
    return F(3 * k, 300)


def c21(ch):
    mean = F(99 * 400000 + 21 * 350000, 120)
    assert mean < 400000
    return by_text(ch, "The mean decreases, and the median stays the same.")


def c22(ch):
    return pick(ch, 2 - F(16, 10) * 5)


CHECKS = {f'Q062-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15,
                                                    c16, c17, c18, c19, c20, c21, c22], 1)}
