"""Scripted recomputation for ACT Math batch 61. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def nums(t):
    t = t.replace('−', '-').replace(' only', '')
    return sorted(int(s) for s in t.split(' and '))


def by_set(ch, want):
    hits = [k for k, v in ch.items() if nums(v) == sorted(want)]
    assert len(hits) == 1
    return hits[0]


def c01(ch):
    return by_set(ch, [x for x in range(-50, 51) if abs(x - 3) == 5])


def c02(ch):
    return pick(ch, 80 - F(3, 8) * 80)


def c03(ch):
    return pick(ch, 180 / 2, conv=lambda t: float(t.rstrip('°')))


def c04(ch):
    hits = []
    for k, v in ch.items():
        lhs, rhs = v.replace('−', '-').replace(' ', '').split('=')
        a = int(lhs.split('x')[0] or 1)
        b = int(lhs.split('x')[1].rstrip('y') or 1)
        c = int(rhs)
        if a * 0 + b * 4 == c and a * 6 + b * 0 == c:
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c05(ch):
    return pick(ch, 24000 * 0.85 ** 2)


def c06(ch):
    return pick(ch, 48 * F(6, 4) ** 3)


def c07(ch):
    return pick(ch, sum(1 for d in range(1, 73) if 72 % d == 0))


def c08(ch):
    ac = math.dist((0, 0), (6, 8))
    return pick(ch, 2 * (0.5 * 6 * 8) / ac)


def c09(ch):
    w = next(w for w in range(1, 100) if (w + 2) * (w + 6) - w * (w + 4) == 40)
    return pick(ch, w)


def c10(ch):
    outs = [o for o in itertools.product(range(1, 7), repeat=2) if 6 in o]
    return pick(ch, F(sum(1 for o in outs if o == (6, 6)), len(outs)))


CHECKS = {f'B061-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
