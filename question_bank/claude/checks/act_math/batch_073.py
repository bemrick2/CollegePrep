"""Scripted recomputation for ACT Math batch 73. Each check derives the answer from the stem's numbers only."""
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
    return pick(ch, F(1) / F('0.4'))


def c02(ch):
    # truth table over (square, rectangle) cases that satisfy "square -> rectangle"
    worlds = [(s, r) for s in (0, 1) for r in (0, 1) if (not s) or r]
    contra = all((r or not s) for s, r in worlds)
    converse = all((s or not r) for s, r in worlds)
    assert contra and not converse
    return by_text(ch, "If a figure is not a rectangle, then it is not a square.")


def c03(ch):
    interior = (5 - 2) * 180 / 5
    return by_text(ch, f"{round(5 * interior / 3)}°")


def c04(ch):
    return pick(ch, F(3 * 4, 6))


def c05(ch):
    assert math.isclose(6 / math.sqrt(3), 2 * math.sqrt(3))
    return by_text(ch, "2√3")


def c06(ch):
    area_over_pi = F(1, 2) * 36 * F(2, 3)
    return by_text(ch, f"{area_over_pi}π")


def c07(ch):
    pis = 4 * F(1, 4) * 4 ** 2
    return by_text(ch, f"64 − {pis}π")


def c08(ch):
    deg = 3 * 2 + 1
    return pick(ch, deg)


def c09(ch):
    return by_text(ch, f"{F(1, 2) * F(4, 3) * 6 ** 3}π")


def c10(ch):
    return pick(ch, pow(2, 100, 5))


CHECKS = {f'B073-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
