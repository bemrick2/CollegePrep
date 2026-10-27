"""Scripted recomputation for SAT Math batch 20. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    return pick(ch, (6 - 2) * 5)


def c02(ch):
    xs = [F(n, 4) for n in range(-400, 400)]
    pts = [x for x in xs if -x + 7 == abs(x - 1)]
    assert pts == [4]
    # left branch parallel: 1 - x = -x + 7 never holds
    return by_text(ch, "1")


def c03(ch):
    for x in range(-5, 8):
        assert 3 * (x - 2) ** 2 - 12 == 3 * x * (x - 4)
    return by_text(ch, "y = 3x(x − 4)")


def c04(_):
    sols = [x for x in range(-50, 51) if x != 0 and F(3, x) + F(4, x * x) == 1]
    assert sorted(sols) == [-1, 4]
    return sum(sols)


def c05(ch):
    f = lambda x: 3 * x * x
    return pick(ch, f(2) - f(1))


def c06(ch):
    s = [70, 75, 80, 85, 90, 100]
    mean = F(sum(s), 6)
    med = F(s[2] + s[3], 2)
    assert mean > med
    return by_text(ch, "The mean is greater than the median.")


def c07(ch):
    return pick(ch, F(240, 4))


def c08(_):
    return next(r for r in range(1, 50) if 4 * r * r - r * r == 27)


def c09(ch):
    x = next(x for x in range(1, 100) if x * x + 36 == (x + 2) ** 2)
    return pick(ch, x + 2)


CHECKS = {f'Q020-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09], 1)}
