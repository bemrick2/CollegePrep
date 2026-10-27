"""Scripted recomputation for SAT Math batch 59. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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


def n01(_):
    drop = F(48000 - 6000, 12)
    return F(next(t for t in range(1, 13) if 48000 - drop * t < 24000))


def n02(_):
    adults = math.ceil(F(180, 8))
    return F(math.ceil(F(180 + adults, 50)))


def n03(ch):
    s = (F(85) + 41) / 2
    return pick(ch, s)


def n04(ch):
    x = F(70) / F(108, 100)
    assert 1 * x + 5 + F(8, 100) * x == 75
    return pick(ch, round(float(x), 2))


def n05(ch):
    return pick(ch, round((1.02 / 1.06) ** 10 * 100, 1))


def n06(_):
    return F(max(24 * F(t, 100) - F(3, 2) * F(t, 100) ** 2 for t in range(0, 1601)))


def n07(ch):
    r = F(27, 81)
    assert round(81 ** 0.75) == 27
    return pick(ch, r)


def n08(ch):
    f = lambda x: 2 ** x - 2 ** -x
    a = math.log2((3 + math.sqrt(13)) / 2)
    assert abs(f(a) - 3) < 1e-12
    return pick(ch, round(f(-a), 9))


def n09(_):
    return F(10) ** ((100 - 120) // 10) / F(10) ** ((70 - 120) // 10)


def n10(ch):
    for x in [F(4), F(5), F(7), F(19, 2)]:
        v = (x * x - 9) / (x * x + 6 * x + 9) / ((x - 3) / (2 * x + 6))
        assert v == 2
    return by_text(ch, "2")


def n11(ch):
    t = next(t for t in range(1, 50) if F(t, 2) + F(t, 6) == 4)
    return pick(ch, t)


def n12(ch):
    return pick(ch, round(1200 / 1.15 ** 4))


def n13(ch):
    f = lambda x: x * x + 3 * x
    xs = [x for x in range(-50, 51) if f(2 * x) == 4 * f(x) - 18]
    assert xs == [3]
    return pick(ch, xs[0])


def n14(ch):
    for t in [1, 2, 3]:
        assert abs(4 / 3 * math.pi * (2 * t) ** 3 - 32 / 3 * math.pi * t ** 3) < 1e-9
    return by_text(ch, "V = (32/3)πt³")


def n15(_):
    sols = set()
    for x2 in range(-400, 401):
        x = F(x2, 2)
        if abs(x - 10) == 2 * abs(x - 1):
            sols.add(x)
    assert sols == {F(4), F(-8)}
    return sum(sols)


def n16(ch):
    return pick(ch, round(100 * 26 / 25, 1))


def n17(_):
    extra = (F(1, 24) - F(1, 30)) * F(36, 10)
    saved = F(1, 60) - F(1, 75)
    return extra / saved


def n18(ch):
    r = 3 / math.tan(math.radians(30))
    v = math.pi * r * r * 3 / 3
    return pick(ch, v, conv=lambda s: float(s.replace('π', '') or 1) * math.pi)


def n19(ch):
    area = 0.5 * 8 * 10 * math.sin(math.radians(150))
    assert abs(area - 20) < 1e-9
    return by_text(ch, "20")


def n20(ch):
    h = F(10) / (1 - F(6, 10))
    return pick(ch, F(1, 2) * F(6, 10) * h * F(8, 10) * h)


def n21(_):
    bs = [b for b in range(1, 10) if F(b * b, 4) < 25 and F(b * b) * (100 - b * b) == 2304]
    assert sorted(bs) == [6, 8]
    return F(8)


def r01(_):
    ns = [n for n in range(1, 200) if 6 <= F(108, n) <= F(15, 2)]
    assert ns == [15, 16, 17, 18]
    return F(len(ns))


def r02(ch):
    for s in range(5, 15):
        lm, lw = F(s + 22, 3), F(2 * s + 41, 6)
        assert lm - lw == F(1, 2)
    return by_text(ch, "The man's foot is 0.5 inch longer.")


def r03(ch):
    t = (F(42) - 2 - 8 * F(3, 4)) / 8
    return pick(ch, t * 60)


def r04(_):
    f3 = F(int(math.isqrt(144)))
    b2 = F(48) / f3
    b = F(int(math.isqrt(int(b2))))
    assert b * b == b2
    A = f3 / b ** 3
    f = lambda x: A * b ** x
    assert f(2) * f(4) == 144 and f(5) == 48
    return f(1)


def r05(ch):
    arc = 30 * F(2, 3)  # in units of pi
    ang = arc / 12
    assert ang == F(5, 3)
    return by_text(ch, "5π/3")


def r06(_):
    xs = [x for x in range(-50, 51) if (x - 3) ** 2 + (x + 4) ** 2 == 289]
    assert sorted(xs) == [-12, 11]
    x = next(x for x in xs if x - 3 > 0 and x + 4 > 0)
    return F(x - 3, x + 4)


CHECKS = {f'Q059-{i:02d}': f for i, f in enumerate([n01, n02, n03, n04, n05, n06, n07, n08, n09, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, r01, r02, r03, r04, r05, r06], 1)}
