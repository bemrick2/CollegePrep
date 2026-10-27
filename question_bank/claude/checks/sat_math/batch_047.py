"""Scripted recomputation for SAT Math batch 47. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    return F(sum(1 for x in range(0, 41) if x <= 25 and F(33, 2) * x + 12 * (40 - x) >= 552))


def c02(ch):
    p = (F('49.00') - F('3.25')) / F('12.5') + F('0.12')
    return pick(ch, float(p))


def c03(_):
    diffs = {(-2 + c) - (6 + b) for b in range(-5, 6) for c in [8 + b]}
    assert diffs == {0}
    return F(8)


def c04(ch):
    f = lambda x: 3 * x - 9
    target = F(f(2) + f(10), 2)
    return pick(ch, float((target + 9) / 3))


def c05(ch):
    P = lambda x: -2 * x * x + 25 * x - 63
    zeros = [x for x in (F(n, 2) for n in range(0, 41)) if P(x) == 0]
    return pick(ch, float(min(zeros)))


def c06(ch):
    f = {1: 7, 3: 9, 5: 4, 7: 5, 9: 1}
    sols = [a for a in range(-10, 11) if (3 * a - 3) in f and f[3 * a - 3] == 9]
    assert sols == [2]
    return pick(ch, 2)


def c07(_):
    t = next(t for t in range(0, 200) if math.isclose(22 + 64 * 0.5 ** (t / 10), 38))
    return F(t)


def c08(ch):
    kg = F(3, 2) * F(30, 12) / F(22, 10)
    return pick(ch, float(kg * F(88, 10)))


def c09(ch):
    iqr_a, iqr_b, rng_a, rng_b = 31 - 20, 35 - 18, 48 - 12, 40 - 15
    assert iqr_b > iqr_a and rng_b < rng_a
    return by_text(ch, "Store B's interquartile range is greater, and store B's range is smaller.")


def c10(ch):
    area = 2 * math.sqrt(3) / 4 * 10 ** 2
    return pick(ch, area)


CHECKS = dict(zip(['Q047-01', 'Q047-02', 'Q047-03', 'Q047-04', 'Q047-05', 'Q047-06', 'Q047-08', 'Q047-09', 'Q047-10'],
                  [c01, c02, c03, c04, c05, c06, c08, c09, c10]))
