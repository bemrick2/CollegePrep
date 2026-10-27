"""Scripted recomputation for SAT Math batch 49. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    return F(next(a for a in range(-50, 100) if F(12 + a, 3) > 7))


def c02(_):
    m = F(14 - 5, 5 - 2)
    return 5 - 2 * m


def c03(ch):
    for w in (3, 10, 20):
        length = 50 - w
        assert length + w == 50 and 2 * (length + w) == 100
    return by_text(ch, "The sum of the rectangle's length and width, in meters")


def c04(_):
    return F(next(t for t in range(0, 100) if F(50 * t, t + 4) == 30))


def c05(_):
    return F(30, 30 + 18 + 12) / F(20, 20 + 35 + 45)


def c06(ch):
    half_diag = math.hypot(8, 6) / 2
    h = math.sqrt(13 ** 2 - half_diag ** 2)
    return pick(ch, round(8 * 6 * h / 3, 9))


def c07(_):
    d = math.sqrt(13 ** 2 - ((20 - (-4)) / 2) ** 2)
    return F(round(2 + d))


def c08(_):
    return F(60, 360) * (12 ** 2 - 9 ** 2)


CHECKS = {f'Q049-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08], 1)}
