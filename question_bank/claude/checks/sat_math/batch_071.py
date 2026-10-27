"""Scripted recomputation for SAT Math batch 71. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(_):
    n0, m0, m1 = 600, 4, 2
    n1 = n0 * F(m0, m1) ** 2
    return n1 - n0


def c02(ch):
    moe_sub = 3 * 2  # margin scales with sqrt(1200 / 300) = 2
    assert moe_sub > 3
    return [k for k, v in ch.items() if v.startswith('The margin of error for this estimate is greater than 3')][0]


def c03(ch):
    return pick(ch, F(9) / F('1.25') * 2)


def c04(ch):
    a = (F(49) - F('3.3'), F(49) + F('3.3'))
    b = (F(45) - F('3.3'), F(45) + F('3.3'))
    assert a[0] <= 46 <= a[1] and b[0] <= 47 <= b[1] and a[0] < b[1]
    return [k for k, v in ch.items() if 'plausible that, for example' in v][0]


def c05(ch):
    solids = F(50) * F('0.2')
    return pick(ch, solids / F('0.8'))


def c06(_):
    tagged = 120 * F('0.9')
    return tagged * 150 / 9


def c07(_):
    return (F('0.25') / F('0.10')) / (F('0.75') / F('0.90'))


def c08(_):
    bound = F(6 * 10 + 9 * 20 + 5 * 30, 20)
    return F(int(bound) if bound != int(bound) else int(bound) - 1)


def c09(ch):
    return [k for k, v in ch.items() if v.startswith('The prediction is not appropriate, because age 30 is far outside')][0]


def c10(ch):
    kg = F(22) / F('2.2')
    per_dose_mg = 12 * kg / 3
    return pick(ch, per_dose_mg / 250 * 5)


def c11(ch):
    union = 90 + 70 - 30
    return pick(ch, F(30, union))


CHECKS = {f'Q071-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11], 1)}
