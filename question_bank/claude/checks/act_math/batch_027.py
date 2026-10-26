"""Scripted recomputation for ACT Math batch 27. Each check derives the answer from the stem's numbers only."""
import itertools
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    down, up = F(24, 2), F(24, 3)
    return pick(ch, (down - up) / 2)


def c02(ch):
    xs = {F(n, 4) for n in range(-80, 81) if (F(n, 4) - 3) * (F(n, 4) ** 2 - 4) == 0}
    return pick(ch, len(xs))


def c03(ch):
    x = next(F(n, 4) for n in range(-400, 400) if 5 * F(n, 4) - 10 == (2 * F(n, 4) + 5) + (F(n, 4) + 25))
    return pick(ch, 5 * x - 10, conv=lambda t: F(t.rstrip('°')))


def c04(ch):
    s = round(64 ** (1 / 3))
    assert s ** 3 == 64
    return pick(ch, 6 * s * s)


def c05(ch):
    primes = {2, 3, 5, 7, 11}
    rolls = list(itertools.product(range(1, 7), repeat=2))
    return pick(ch, F(sum(1 for r in rolls if sum(r) in primes), len(rolls)))


def c06(ch):
    freq = {1: 4, 2: 6, 3: 8, 4: 2}
    return pick(ch, F(sum(k * v for k, v in freq.items()), sum(freq.values())))


def c07(ch):
    return pick(ch, F(3, 4) * F(2, 5))


def c08(ch):
    before, after = F(400, 20), F(400, 16)
    return pick(ch, (after - before) / before * 100, conv=lambda t: F(t.rstrip('%')))


def c09(ch):
    a, b = F(3), F(4)
    return pick(ch, (a + b) / (a - b))


def c10(ch):
    minute = 50 * 6
    hour = 2 * 30 + 50 * F(1, 2)
    d = abs(minute - hour) % 360
    return pick(ch, min(d, 360 - d), conv=lambda t: F(t.rstrip('°')))


CHECKS = {f'B027-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
