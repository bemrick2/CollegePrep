"""Scripted recomputation for SAT Math batch 61. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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


def n01(_):
    a = F(5 * 1 + 1, 1 + 2)   # x = 1: 3a = 6
    b = F(5 * -2 + 1, -2 - 1)  # x = -2: -3b = -9
    for x in [F(3), F(5), F(-7, 2)]:
        assert a / (x - 1) + b / (x + 2) == (5 * x + 1) / (x * x + x - 2)
    return b


def n02(ch):
    for x in [7, 16, 40]:
        assert abs(x / (math.sqrt(x + 9) - 3) - (math.sqrt(x + 9) + 3)) < 1e-9
    return by_text(ch, "√(x + 9) + 3")


def n03(_):
    import itertools
    ks = set()
    for num in range(1, 200):
        for den in range(1, 10):
            k = F(num, den)
            zeros = {F(3), F(-3)}
            disc = k * k - 16
            if disc < 0:
                continue
            r = math.isqrt(int(disc * den * den)) if (disc * den * den).denominator == 1 else None
            # roots of x^2 + kx + 4
            if disc == 0:
                zeros.add(-k / 2)
            else:
                s = disc
                # rational roots only matter for shared-root case; check shared root directly
                if 9 + 3 * k + 4 == 0 or 9 - 3 * k + 4 == 0:
                    zeros.add(F(4) / (F(-3) if 9 - 3 * k + 4 == 0 else F(3)))
                else:
                    zeros |= {'r1', 'r2'}
            if len(zeros) == 3:
                ks.add(k)
    assert ks == {F(4), F(13, 3)}
    return sum(ks)


def n04(_):
    for k in range(-50, 26):
        if 25 - k > 0 and abs((25 - k) - math.sqrt(3) * math.sqrt(25 - k)) < 1e-12:
            return F(k)


def n05(_):
    sols = {4 + 4 * math.sqrt(2), 4 - 4 * math.sqrt(2), 4.0}
    for x in sols:
        assert abs(abs(x * x - 8 * x) - 16) < 1e-9
    return F(round(sum(sols)))


def n06(ch):
    xs = [x for x in range(-10, 11) if x * x + 2 * x - 5 == -x * x + 6 * x + 11]
    (x1, x2) = xs
    y = lambda x: x * x + 2 * x - 5
    return pick(ch, F(y(x2) - y(x1), x2 - x1))


def n07(ch):
    for x in range(-5, 6):
        assert (x + 2) ** 2 - 9 == (x - 1) * (x + 5)
    return by_text(ch, "f(x) = (x − 1)(x + 5)")


def n08(ch):
    for x in [F(2), F(5), F(-3)]:
        assert (1 - 1 / x) / (1 - 1 / (x * x)) == x / (x + 1)
    return by_text(ch, "x/(x + 1)")


def n09(ch):
    c = 6
    a = 20 - c
    return pick(ch, a * F(1, 4) + c)


def n10(ch):
    k = (F(-6) * F(9, 4) + 6) / F(3, 2)
    return pick(ch, k)


def n11(ch):
    b2 = F(3, 4)
    return pick(ch, (1 - b2 * b2) * 100, conv=lambda s: float(s.rstrip('%')))


def n12(_):
    s, q = 10, 58
    ab = F(s * s - q, 2)
    d2 = q - 2 * ab
    return F(math.isqrt(int(d2)))


def n13(ch):
    f = 2
    for x in range(3):
        f += 4 * x + 6
    return pick(ch, f)


def n14(_):
    # (x-5)^2 + (y+3)^2 = 34 - c ; radius = 3
    return F(34 - 9)


def n15(ch):
    area = F(1, 2) * 25 * F(16, 10)
    r = math.sqrt(float(area * 2 / F(4, 10)))
    return pick(ch, r * 0.4)


def n16(_):
    dag = 360 - 90 - 108
    return F(180 - dag, 2)


def n17(_):
    P = (F(10, 3), F(4))
    pts = [(F(10), F(0)), (F(10), F(6)), (F(5), F(6)), P]
    s = sum(pts[i][0] * pts[(i + 1) % 4][1] - pts[(i + 1) % 4][0] * pts[i][1] for i in range(4))
    return abs(s) / 2


def n18(ch):
    ang = F(360 - 70 - 50, 2)
    return pick(ch, ang, conv=lambda t: float(t.rstrip('°')))


def n19(ch):
    pi_coef = -2 * 4 + 2 * 2 * 6  # remove two circles (pi r^2), add wall (2 pi r h)
    assert pi_coef == 16
    return by_text(ch, f"{6 * 36} + {pi_coef}π")


def n20(ch):
    # AB = CD + h/tan45 + h/tan60 ; area = h/2 (AB + CD); write as p + q*sqrt(3)
    h, cd = 6, 10
    p = F(h, 2) * (cd + cd + h)          # rational part
    q = F(h, 2) * F(h, 3)                # h/tan60 = 6/sqrt3 = 2*sqrt3 -> (h/2)*2 = 6
    assert abs(float(p) + float(q) * math.sqrt(3) - h / 2 * (2 * cd + h + h / math.tan(math.radians(60)))) < 1e-9
    return by_text(ch, f"{p} + {q}√3")


def n21(_):
    r = F(6) * F(6, 9)
    vol = F(1, 3) * r * r * 6  # in units of pi
    return vol / 36


def n22(ch):
    h = F(2 * 35, 10)
    return pick(ch, F(1, 2) * 14 * h)


def r01(_):
    return F(next(p for p in range(1, 2000) if F(65, 100) * p - 40 >= 250))


def r02(_):
    return F(80) * F(48, 16) * F(21, 10) * 60 / 1000


def r03(ch):
    return pick(ch, math.ceil(F(45, 10) / 6 / F(35, 1000)))


def r04(ch):
    return [k for k, v in ch.items() if 'may differ from those that did not' in v][0]


CHECKS = {f'Q061-{i:02d}': f for i, f in enumerate([n01, n02, n03, n04, n05, n06, n07, n08, n09, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, r01, r02, r03, r04], 1)}
