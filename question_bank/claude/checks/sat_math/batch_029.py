"""Scripted recomputation for SAT Math batch 29. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    x = next(x for x in range(1, 50) if x * x + x == 12)
    return x * x - x


def c02(ch):
    m = next(m for m in range(-50, 51) if 3 * m + 4 == 2 * (m + 4))
    return pick(ch, m)


def c03(ch):
    return by_text(ch, "Class B's scores are more spread out than class A's.")


def c04(_):
    vals = {F(8) ** x / F(4) ** y for x in range(-5, 10) for y in range(-10, 10) if 3 * x - 2 * y == 7}
    assert vals == {128}
    return 128


def c05(ch):
    f = lambda x: x * x - 3 * x + 2
    n = sum(1 for x in range(-50, 51) if f(x) == f(1))
    return by_text(ch, str(n))


def c06(ch):
    for x, y in ((3, 0), (0, 2), (6, -2)):
        assert F(x, 3) + F(y, 2) == 1 and 2 * x + 3 * y == 6
    return by_text(ch, "2x + 3y = 6")


CHECKS = {f'Q029-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06], 1)}
