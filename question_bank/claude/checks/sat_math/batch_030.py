"""Scripted recomputation for SAT Math batch 30. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    y = lambda x: 3 * x * x
    return pick(ch, F(y(3 * 2), y(2)))


def c02(ch):
    r2 = 50
    return by_text(ch, str(r2))


def c03(ch):
    return by_text(ch, f"{180 - 90}°")


def c04(ch):
    sols = [x for x in range(-20, 21) if 2 ** (x * x) == 16]
    assert sorted(sols) == [-2, 2]
    return pick(ch, sols[0] * sols[1])


CHECKS = {f'Q030-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04], 1)}
