"""Scripted recomputation for ACT Math batch 26. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    r = 5
    y = math.sqrt(r * r - 3 * 3)
    return pick(ch, 0.5 * 10 * y)


def c02(ch):
    return pick(ch, max(n for n in range(-100, 101) if 16 <= 3 * n - 5 <= 31))


def c03(ch):
    people = ['T'] * 5 + ['S'] * 4
    return pick(ch, sum(1 for c in itertools.combinations(range(9), 3) if {people[i] for i in c} == {'T', 'S'}))


def c04(ch):
    f = {1: 3, 2: -1, 3: 0, 4: 2, 5: 4}
    x = 51
    while x > 5:
        x -= 5
    return pick(ch, f[x])


def c05(ch):
    p, q = (3, 4), (4, 3)
    return pick(ch, math.dist(p, q))


def c06(ch):
    return pick(ch, math.sqrt(8) * math.sqrt(18) / math.sqrt(4))


def c07(ch):
    # Build a concrete assignment matching every count and count students with no language.
    regions = {'FSL': 1, 'FS': 5 - 1, 'FL': 3 - 1, 'SL': 2 - 1}
    regions['F'] = 15 - regions['FSL'] - regions['FS'] - regions['FL']
    regions['S'] = 12 - regions['FSL'] - regions['FS'] - regions['SL']
    regions['L'] = 8 - regions['FSL'] - regions['FL'] - regions['SL']
    assert min(regions.values()) >= 0
    return pick(ch, 30 - sum(regions.values()))


def c08(ch):
    return pick(ch, 1560 / (4 * 5 * 10))


def c09(ch):
    return pick(ch, F(6, 4) * 30)


def c10(ch):
    bag = ['r'] * 3 + ['b'] * 2
    seqs = list(itertools.permutations(range(5), 3))
    return pick(ch, F(sum(1 for s in seqs if [bag[i] for i in s] == ['r', 'b', 'r']), len(seqs)))


CHECKS = {f'B026-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
