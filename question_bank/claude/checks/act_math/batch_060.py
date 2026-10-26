"""Scripted recomputation for ACT Math batch 60. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import statistics
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402

SUP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789')


def c01(ch):
    primes = [k for k, v in ch.items() if all(int(v) % d for d in range(2, math.isqrt(int(v)) + 1))]
    assert len(primes) == 1
    return primes[0]


def c02(ch):
    return pick(ch, 3 + 4 - 2, conv=lambda t: int(t.lstrip('x').translate(SUP)))


def c03(ch):
    return pick(ch, 10 / math.sqrt(2))


def c04(ch):
    xs = [x for x in range(0, 101) if statistics.median([78, 85, 92, x]) == 86]
    assert len(xs) == 1
    return pick(ch, xs[0])


def c05(ch):
    rs = [r for r in range(1, 50) if (2 - r) ** 2 + (1 - r) ** 2 == r * r]
    return pick(ch, sum(rs))


def c06(ch):
    for c in range(-50, 51):
        disc = 36 - 4 * c
        if disc >= 0 and math.isclose(math.sqrt(disc), 4):
            return pick(ch, c)


def c07(ch):
    hours = 12 * 60 / 3
    return pick(ch, hours / 24)


def c08(ch):
    hits = [k for k, v in ch.items() if v.replace(' ', '') == 'y≤5']
    assert len(hits) == 1
    return hits[0]


def c09(ch):
    return pick(ch, math.ceil(12 * 40 * 2 / 350))


def c10(ch):
    best = 0
    for lst in itertools.combinations_with_replacement(range(1, 31), 5):
        if sum(lst) == 30 and statistics.median(lst) == 7:
            m = statistics.multimode(lst)
            if m == [8]:
                best = max(best, min(lst))
    return pick(ch, best)


CHECKS = {f'B060-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
