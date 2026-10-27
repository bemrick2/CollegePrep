"""Scripted recomputation for SAT Math batch 67. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(_):
    return F(6 * 540 + 6 * 780 - 10 * 620, 2)


def c02(ch):
    shares = F(900, 15) + F(900, 30)
    return pick(ch, F(1800) / shares)


def c03(_):
    ys = [y for y in range(0, 200) if F(24, 42 + y) == F(24, 24 + 25)]
    assert ys == [7]
    return F(ys[0])


def c04(ch):
    need = F(30 * 150, 1000)
    return pick(ch, round(float(need / (F(8, 10) * F(75, 100))), 2))


def c05(_):
    C = F(100)
    return (F(16, 10) * C - C) / (F(16, 10) * C) * 100


def c06(ch):
    z = F(82 - 70, 8)
    return pick(ch, 76 + z * 6)


def c07(ch):
    return pick(ch, F(150) / F(25, 100))


def c08(ch):
    a, b = 9000 * 12, 12000 * 6
    return pick(ch, F(a, a + b) * 21000)


def c09(_):
    total_change = 7 * (126 - 120)
    return F(150 - total_change)


def c10(ch):
    return pick(ch, F(400 * 10 + 1000 * 15 + 250 * 5, 30))


def c11(_):
    keep = F(7, 10) * F(75, 100) * F(8, 10)
    return F(1512) / keep


def c12(ch):
    a = F(84, 240000) * 100000
    b = F(45, 120000) * 100000
    return pick(ch, b - a)


CHECKS = {f'Q067-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
