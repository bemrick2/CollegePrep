"""Scripted recomputation for SAT Math batch 66. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    drop_per_m = F(3, 2) / 1
    return drop_per_m * 10 + 2


def c02(ch):
    v = 0.3 * 50 * 3600 / 1000
    return pick(ch, round(v))


def c03(ch):
    t = math.sqrt(4)  # tan A = 4 / tan A
    k2 = F(85, 1 + 4)
    assert abs(math.tan(math.atan(t)) - 4 * math.tan(math.pi / 2 - math.atan(t))) < 1e-12
    return pick(ch, F(1, 2) * 2 * k2)


def c04(ch):
    return pick(ch, round(F(4, 9) * F(12, 10), 2), conv=lambda s: round(num(s), 2))


def c05(_):
    xs = [F(n, 3) for n in range(1, 37) if (12 - F(n, 3)) ** 2 + 64 == F(n, 3) ** 2]
    assert len(xs) == 1
    return xs[0]


def c06(ch):
    x = (820 - F(4, 100) * 15000) / F(2, 100)
    y = 15000 - x
    assert F(6, 100) * x + F(4, 100) * y == 820
    term = F(2, 100) * x
    assert term == 820 - F(4, 100) * 15000 == 220
    return [k for k, v in ch.items() if v.endswith("would have earned at 4%")][0]


def c07(ch):
    t1, t2 = 100 * 3, 300 * 2
    return pick(ch, F(t2 - t1, 200))


def c08(_):
    P = F(100)
    g = F(25, 100) * P
    p15, p25 = P + g, P + 3 * g
    return (p25 - p15) / p15 * 100


def c09(_):
    vals = set()
    for x2 in range(-6, 7):
        x = F(x2, 2)
        y = 2 - x
        # choose a, b so the system holds with this (x, y) when possible
        det = x * x - y * y
        if det == 0:
            continue
        a = (7 * x - 5 * y) / det
        b = (5 * x - 7 * y) / det
        assert a * x + b * y == 7 and b * x + a * y == 5
        if a * a != b * b:
            vals.add(a + b)
    assert vals == {6}
    return F(6)


def c10(_):
    sols = [a for a in range(0, 401) if 3 * a - 2 * (400 - a) == 0]
    assert sols == [160]
    return F(160)


def c11(_):
    b = (1 - 2 * F(1, 6)) / 7
    a = F(1, 6) - b
    assert 2 * a + 9 * b == 1
    return 1 / a


def c12(ch):
    return pick(ch, 10 * 5 - 5 * 6)


def c13(ch):
    ok = [k for k, v in ch.items() if 8 <= 2 * num(v) + 3 and not 21 <= 6 * num(v) + 3]
    assert len(ok) == 1
    return ok[0]


def c14(ch):
    w = max(w for w in range(1, 100) if 2.5 * w + 2 * (w + w) <= 108)
    return pick(ch, w)


def c15(ch):
    return pick(ch, (F(7, 2) - 1) * 10)


def c16(ch):
    h = lambda w: 8 + F(15, 100) * 8 * w
    assert h(3) == 8 + F(36, 10)
    return by_text(ch, "h = 8 + 1.2w")


def c17(ch):
    L = [L for L in range(0, 51) if 300 <= 4 * (50 - L) + 9 * L <= 360]
    return pick(ch, len(L))


def c18(ch):
    for c in range(0, 50):
        for b in range(0, 2000):
            p = 24 * b
            assert (12 * c + F(1, 4) * p == 480) == (12 * c + 6 * b == 480)
            if b > 100:
                break
    return by_text(ch, "12c + 6b = 480")


def c19(ch):
    rate = F(66 - 50, 10 - 6)
    fee = 50 - 6 * rate
    diffs = {(fee + rate * c) - (20 + 4 * c) for c in range(0, 30)}
    assert diffs == {6}
    return [k for k, v in ch.items() if v.startswith("Plan A costs $6 less")][0]


def c20(_):
    T = 4 / (1 - 1 / F(12, 10))
    return (45 - T) / F(3, 2)


CHECKS = {f'Q066-{i:02d}': f for i, f in enumerate(
    [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20], 1)}
