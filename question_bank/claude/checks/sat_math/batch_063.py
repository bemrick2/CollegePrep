"""Scripted recomputation for SAT Math batch 63. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    ks = [k for k in range(1, 200) if (F(k, 3)) ** 2 - 7 * F(k, 3) + k == 0]
    assert ks == [12]
    return F(ks[0])


def c02(_):
    diffs = set()
    for a in [-5, 0, 3, 11]:
        p, q = F(a + 6, 3), F(a - 6, 3)
        assert 9 * p * p - 6 * a * p + a * a == 36
        diffs.add(p - q)
    assert len(diffs) == 1
    return diffs.pop()


def c03(ch):
    r = F(120, 24)
    assert 3 * (-2) * 4 * (-r) == 120
    return pick(ch, r)


def c04(ch):
    f = lambda x: (x - 2) * (x - 5)
    g = lambda x: f(3 - x)
    zs = sorted(x for x in range(-20, 21) if g(x) == 0)
    return by_text(ch, f"{zs[0]} and {zs[1]}".replace('-', '−'))


def c05(ch):
    T = lambda t: 70 + 110 * 0.5 ** (t / 20)
    assert abs((T(20) - 70) / (T(0) - 70) - 0.5) < 1e-12 and abs(T(20) / T(0) - 0.5) > 0.1
    return [k for k, v in ch.items() if v.startswith("Every 20 minutes, the amount by which")][0]


def c06(_):
    p3 = 4
    return F(2 * p3 + 5)


def c07(ch):
    sols = []
    for x in range(-20, 21):
        if x in (2, -1):
            continue
        if F(x, x - 2) + F(3, x + 1) == F(6, x * x - x - 2):
            sols.append(x)
    return by_text(ch, "{" + ", ".join(str(s).replace('-', '−') for s in sols) + "}")


def c08(ch):
    s, p = 5, 2
    return pick(ch, p + 3 * s + 9)


def c09(ch):
    tot = lambda x: x * F(2 * x + 600, x)
    assert tot(11) - tot(10) == 2
    return [k for k, v in ch.items() if v.startswith("Each additional item")][0]


def c10(ch):
    best = max((3 + 2 * math.cos(t / 1000)) ** 2 + (4 + 2 * math.sin(t / 1000)) ** 2 for t in range(0, 6284))
    return pick(ch, round(best, 6), tol=1e-5)


def c11(ch):
    sin = F(5, 13); cos = F(12, 13)
    m = sin / cos
    return pick(ch, m * 2)


def c12(ch):
    h_ab = F(9) * 16 / 12
    return pick(ch, h_ab - 9)


def c13(ch):
    slant = math.hypot(12, 5)
    return pick(ch, 4 * 0.5 * 10 * slant + 5 * 100)


def c14(_):
    k = F(81 - 36, 18)
    r = 9 - k
    assert r * r == 36 + k * k
    return r


def c15(_):
    x = math.sqrt(100 - 25)
    ang = 180 - 2 * math.degrees(math.atan2(5, x))
    assert abs(ang - 120) < 1e-9
    return F(120, 360) * 2 * 10


def c16(_):
    ks = [k for k in range(-50, 51) if k != 6 and F(11 - 2, k - 6) * F(2, 6) == -1]
    assert ks == [3]
    return F(ks[0])


def c17(_):
    return F(12, 45) * 180


CHECKS = {f'Q063-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17], 1)}
