"""Scripted recomputation for SAT Math batch 54. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    costs = [F(n, 100) for n in range(180, 251)]
    prices = [F(n, 100) for n in range(300, 361)]
    return 50 * min(p - c for p in prices for c in costs)


def c02(ch):
    return pick(ch, (1280 - 6 * 180 - 2 * 40) / (6 - 1))


def c03(_):
    return F(18, 100) + F(20, 50)


def c04(ch):
    f = next(f for f in (F(n, 4) for n in range(0, 400)) if 12 + F(1, 2) * f + 15 + F(3, 10) * f == 47)
    return pick(ch, float(f))


def c05(_):
    k = 360 * 4 ** 2
    return F(k, 3 ** 2)


def c06(_):
    k = -(-16 * 4 + 16 * 2)
    t = F(-16, 2 * -16)
    return -16 * t * t + 16 * t + k


def c07(ch):
    cands = {'S = 2πr² + 1000π/r': lambda r: 2 * math.pi * r * r + 1000 * math.pi / r,
             'S = πr² + 1000π/r': lambda r: math.pi * r * r + 1000 * math.pi / r,
             'S = 2πr² + 1000π': lambda r: 2 * math.pi * r * r + 1000 * math.pi,
             'S = 2πr² + 1000π²r': lambda r: 2 * math.pi * r * r + 1000 * math.pi ** 2 * r}
    true = lambda r: 2 * math.pi * r * r + 2 * math.pi * r * (500 / (r * r))
    hits = [t for t, f in cands.items() if all(math.isclose(f(r), true(r)) for r in (1, 3.5, 8))]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c08(_):
    return F(next(v for v in range(1, 200) if v + F(v * v, 20) == 120))


def c09(ch):
    ra = (F(95, 100), F(120, 300), F(215, 400))
    rb = (F(270, 300), F(35, 100), F(305, 400))
    assert ra[0] > rb[0] and ra[1] > rb[1] and ra[2] < rb[2]
    return by_text(ch, "Clinic A's rate is higher for mild cases, higher for severe cases, and lower for all patients combined.")


def c10(ch):
    return pick(ch, float(F(38, 50) * F(12, 10) * 10000))


def c11(_):
    return F(str(round(4 * math.sqrt(2) - 4, 2)))


def c12(ch):
    return pick(ch, float(F(8 * 600, 1500)))


CHECKS = {f'Q054-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
