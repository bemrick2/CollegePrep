"""Scripted recomputation for SAT Math batch 16. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    return next(k for k in range(1, 1000) if F(k, 3) + F(-k, 5) == 8)


def c02(ch):
    best = max(p for n in range(4, 10) for p in range(0, 40) if F(350, 100) * n + F(125, 100) * p <= 20)
    return pick(ch, best)


def c03(ch):
    return pick(ch, next(F(n, 7) for n in range(-200, 200) if 2 * F(n, 7) + 5 * (F(n, 7) + 3) == 29))


def c04(_):
    return next(x for x in range(0, 1000) if math.isclose(math.sqrt(x + 9) - math.sqrt(x), 1))


def c05(ch):
    return pick(ch, next(t for t in range(0, 100) if 80 - 5 * t * t == 0))


def c06(ch):
    vals = {"f(x) = 100x": 1000, "g(x) = x³": 10 ** 3, "h(x) = 50x + 500": 1000, "k(x) = 2ˣ": 2 ** 10}
    return by_text(ch, max(vals, key=vals.get))


def c07(ch):
    change = F(12, 10) * F(9, 10) - 1
    assert change == F(8, 100)
    return by_text(ch, "An increase of 8%")


def c08(ch):
    hyp = math.isqrt(8 ** 2 + 6 ** 2)
    return pick(ch, F(8, hyp))


def c09(_):
    return F(15) / F(25, 10)


def c10(ch):
    return pick(ch, 3 * 5 * 8)


CHECKS = {f'Q016-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
