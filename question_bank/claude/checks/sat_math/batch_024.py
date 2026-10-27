"""Scripted recomputation for SAT Math batch 24. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    return pick(ch, F(6) / F(25, 100))


def c02(ch):
    return pick(ch, F(-110 + 20, -15))


def c03(_):
    return next(e for e in range(0, 100) if 45 * (e + 2) == 60 * e)


def c04(ch):
    f = lambda x: 4 * 3 ** x
    assert [f(x) for x in range(4)] == [4, 12, 36, 108]
    return by_text(ch, "f(x) = 4 · 3ˣ")


def c05(_):
    a = math.log(7, 3)
    v = 3 ** (a + 2)
    assert math.isclose(v, 63)
    return 63


def c06(ch):
    f = lambda x: x ** 3 - 4 * x
    return pick(ch, f(-2) + f(3))


def c07(ch):
    return pick(ch, 4 ** 2 - 7)


def c08(ch):
    return by_text(ch, "The new routine likely caused higher test scores for people similar to these volunteers.")


def c09(ch):
    return pick(ch, F(5 * 15 - 3 * 12, 2))


def c10(ch):
    h = 10 * math.sin(math.radians(30))
    half = 10 * math.cos(math.radians(30))
    assert math.isclose(h * half, 25 * math.sqrt(3))
    return by_text(ch, "25√3")


CHECKS = {f'Q024-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
