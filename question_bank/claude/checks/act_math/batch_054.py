"""Scripted recomputation for ACT Math batch 54. Each check derives the answer from the stem's numbers only."""
import itertools
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def sci(t):
    c, e = t.split(' × 10^')
    return F(c) * F(10) ** int(e.replace('−', '-'))


def c01(ch):
    return pick(ch, F(405, 18))


def c02(ch):
    return pick(ch, next(F(x, 2) for x in range(-40, 41) if 5 - 2 * (F(x, 2) - 1) == 1))


def c03(ch):
    s = next(s for s in range(1, 100) if 6 * s * s == 150)
    return pick(ch, s ** 3)


def c04(ch):
    return pick(ch, F(20 * 75 + 30 * 85, 50))


def c05(ch):
    t = F(-64, 2 * -16)
    return pick(ch, -16 * t * t + 64 * t + 5)


def c06(ch):
    for x in range(-20, 21):
        y = 4 * x - 5
        if 2 * x + 3 * y == 13:
            return pick(ch, x - y)


def c07(ch):
    return pick(ch, F(6 * 10 ** 5) * F(4, 100) / 80, conv=sci)


def c08(ch):
    return pick(ch, F(10) * F(6, 6 + 9))


def c09(ch):
    best = 0
    for lows in itertools.combinations(range(1, 10), 3):
        for highs in itertools.combinations(range(11, 80), 3):
            if sum(lows) + 10 + sum(highs) == 70:
                best = max(best, max(highs))
    return pick(ch, best)


def c10(ch):
    out = []
    for k, v in ch.items():
        y = F(v.replace('−', '-'))
        if y == 2:
            out.append(k)  # (3y + 1)/(y - 2) undefined
            continue
        x = (3 * y + 1) / (y - 2)
        assert x != 3 and (2 * x + 1) / (x - 3) == y
    assert len(out) == 1
    return out[0]


CHECKS = {f'B054-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
