"""Scripted recomputation for SAT Math batch 40. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    G = lambda m: 15 - F(m, 28)
    assert G(0) - G(28) == 1 and G(420) == 0  # 28 miles per gallon; empty at 420 miles
    return by_text(ch, "The car travels 28 miles for each gallon of fuel it uses.")


def c02(ch):
    lo, hi = 2 * -1 + 3, 2 * 4 + 3  # -1 <= x <= 4 from 3x + 5 <= 2x + 9
    hits = [k for k, v in ch.items() if lo <= int(v.replace('−', '-')) <= hi]
    assert len(hits) == 1
    return hits[0]


def c03(ch):
    b = 9 - 2 * 2
    return pick(ch, 2 * 7 + b)


def c04(ch):
    sols = [(x, y) for x in range(0, 1000) for y in [x - 40] if y > 20 and x + 20 == 2 * (y - 20)]
    assert len(sols) == 1
    return pick(ch, sum(sols[0]))


def c05(ch):
    t = 10 * math.log(2) / math.log(4)
    return pick(ch, round(t, 9))


def c06(ch):
    a = F(19 - 5, 8 - 1)
    b = 5 - a
    return pick(ch, float(a * 4 + b))


def c07(_):
    profit = lambda x: x * (50 - F(1, 2) * x) - (10 * x + 200)
    return max(profit(F(n, 2)) for n in range(0, 201))


def c08(ch):
    plans = {k: ('at random' in v and 'randomly assign' in v) for k, v in ch.items()}
    hits = [k for k, ok in plans.items() if ok]
    assert len(hits) == 1
    return hits[0]


def c09(_):
    return F(25 // 2, 25)


def c10(ch):
    bc, ac = 25 * F(3, 5), 25 * F(4, 5)
    return pick(ch, float(bc * ac / 25))


def c11(ch):
    r = F(40, 30)  # 40 r_P = 30 r_Q
    return by_text(ch, f"{(r * r).numerator}/{(r * r).denominator}")


def c12(ch):
    ant = 50 * (math.tan(math.radians(41)) - math.tan(math.radians(35)))
    return pick(ch, round(ant))


CHECKS = {f'Q040-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
