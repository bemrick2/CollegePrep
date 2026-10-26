"""Scripted recomputation for ACT Math batch 12. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F
from itertools import permutations

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    for a1 in range(-100, 101):
        for d in range(-20, 21):
            if a1 + 4 * d == 17 and a1 + 11 * d == 45:
                return pick(ch, a1 + 19 * d)
    raise ValueError


def c02(ch):
    sols = [F(n, 10) for n in range(1, 1000) if F(1) / F(n, 10) + F(1) / (F(n, 10) + 3) == F(1, 2)]
    assert len(sols) == 1
    return pick(ch, sols[0])


def c03(ch):
    from _util import num
    hits = [k for k, v in ch.items() if 2 * num(v) - 5 > 3 * num(v) + 1]
    assert len(hits) == 1
    return hits[0]


def c04(ch):
    f = lambda x: x * x if x < 2 else 3 * x - 2
    sols = set()
    for n in range(-4000, 4001):
        x = F(n, 1000)
        if f(x) == 4:
            sols.add(x)
    return pick(ch, len(sols))


def c05(ch):
    return pick(ch, round(24000 * 0.85 ** 3), conv=lambda t: float(t.replace('$', '').replace(',', '')))


def c06(ch):
    d1 = math.sqrt(100 - 64)
    d2 = math.sqrt(100 - 36)
    return pick(ch, d1 + d2)  # opposite sides of the center


def c07(ch):
    A, M = (F(-2), F(4)), (F(3), F(-1))
    B = (2 * M[0] - A[0], 2 * M[1] - A[1])
    def pt(t):
        a, b = t.strip('() ').split(',')
        return (F(a.strip().replace('−', '-')), F(b.strip().replace('−', '-')))
    return pick(ch, B, conv=pt)


def c08(ch):
    pairs = list(permutations(range(1, 11), 2))
    return pick(ch, F(sum((a * b) % 2 == 0 for a, b in pairs), len(pairs)))


def c09(ch):
    need = next(k for k in range(0, 21) if (15 + k) / 40 >= 0.85)
    return pick(ch, need)


def c10(ch):
    return pick(ch, round(4416 / 160 / 0.92, 2), conv=lambda t: float(t.replace('$', '').replace(',', '')))


CHECKS = {f'B012-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
