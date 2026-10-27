"""Scripted recomputation for SAT Math batch 32. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    a, b, c = -4.9, 20, 1.5
    t = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return F(str(round(t, 1)))


def c02(ch):
    x = F(180, 5)
    return by_text(ch, f"{int(3 * x)}°")


def c03(ch):
    xs = [F(n, 10) for n in range(-200, 200)]
    best = max(x for x in xs if 2 * x - 3 <= -x + 9)
    return pick(ch, best)


def c04(ch):
    m = F(10, 3 - 1)
    return pick(ch, m * (8 - 5))


def c05(ch):
    def count(c):
        sols = [F(n, 4) for n in range(-200, 200) if (c - 4) * F(n, 4) == c * c - 16]
        return len(sols)
    inf = [k for k, v in ch.items() if count(int(v.replace('−', '-'))) > 100]
    assert len(inf) == 1
    return inf[0]


def c06(ch):
    return pick(ch, F(8, 10) * 60)


def c07(_):
    return next(y for y in range(0, 21) if 3 * (20 - y) + 5 * y >= 80)


def c08(ch):
    for a in (1, 2, -3, F(1, 2)):
        assert F(0 - 2 * a) / (3 * a - a) == -1
    return pick(ch, -1)


def c09(ch):
    a = math.sqrt(12)
    assert math.isclose(a / 3, 4 / a) and not math.isclose(4 / a, 9 / 6)
    return by_text(ch, "2√3")


def c10(_):
    return next(x for x in range(-50, 51) if F(x + 4, 3) - F(x - 2, 2) == 1)


CHECKS = {f'Q032-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
