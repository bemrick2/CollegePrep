"""Scripted recomputation for ACT Math batch 59. Each check derives the answer from the stem's numbers only."""
import math
import os
import sys
from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def pt(t):
    return tuple(int(s.replace('−', '-')) for s in t.strip('()').split(','))


def c01(ch):
    want = Decimal('3.4672').quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    hits = [k for k, v in ch.items() if v == str(want)]
    assert len(hits) == 1
    return hits[0]


def c02(ch):
    w = F(48, 8)
    return pick(ch, 2 * (8 + w))


def c03(ch):
    return pick(ch, 3 * -4 - 2)


def c04(ch):
    want = (3 - 4, 2 - 5)
    hits = [k for k, v in ch.items() if pt(v) == want]
    assert len(hits) == 1
    return hits[0]


def c05(ch):
    return pick(ch, 1 - (1 - 0.3) * (1 - 0.4))


def c06(ch):
    return pick(ch, F(35, 10) * F(5, 2))


def c07(ch):
    # x is at least (>=) 4 more than twice y
    hits = [k for k, v in ch.items() if v.replace(' ', '') == 'x≥2y+4']
    assert len(hits) == 1
    return hits[0]


def c08(ch):
    h = math.sqrt(13 ** 2 - ((20 - 10) / 2) ** 2)
    return pick(ch, (10 + 20) / 2 * h)


def c09(ch):
    return pick(ch, F(32 - 8, 9))


def c10(ch):
    return pick(ch, F(25, 100) * 60 + F(40, 100) * 40, conv=lambda t: F(t.rstrip('%')))


CHECKS = {f'B059-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
