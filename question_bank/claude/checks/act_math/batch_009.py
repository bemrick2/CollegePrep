"""Scripted recomputation for ACT Math batch 9. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F
from itertools import product

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402


def c01(ch):
    return pick(ch, abs(3 - 8) + abs(-4))


def c02(ch):
    sols = [x for x in range(-100, 101) if 3 * (x - 2) == 2 * x + 5]
    return pick(ch, sols[0])


def sset(t):
    return frozenset(F(x.strip().replace('−', '-')) for x in t.strip('{} ').split(','))


def c03(ch):  # scan rationals for exact roots, plus a sign-change scan for irrational roots
    f = lambda x: 4.0 ** x - 3 * 2.0 ** x - 4
    roots = set()
    xs = [i / 1000 for i in range(-10000, 10000)]
    for a, b in zip(xs, xs[1:]):
        if f(a) == 0:
            roots.add(round(a, 6))
        elif f(a) * f(b) < 0:
            lo, hi = a, b
            for _ in range(100):
                mid = (lo + hi) / 2
                lo, hi = (mid, hi) if f(lo) * f(mid) > 0 else (lo, mid)
            roots.add(round(lo, 6))
    return pick(ch, frozenset(F(r).limit_denominator(1000) for r in roots), conv=sset)


def c04(ch):
    area = (3.5 * 4) * (5 * 4)
    return pick(ch, area * 6)


def c05(ch):
    xs = [i / 1000 for i in range(0, 4001)]
    vals = [x * x - 6 * x + 11 for x in xs]
    lo, hi = min(vals), max(vals)
    def rng(t):
        s = t.replace('−', '-')
        m = re.fullmatch(r'(\d+) ≤ f\(x\) ≤ (\d+)', s)
        if m:
            return (float(m.group(1)), float(m.group(2)))
        m = re.fullmatch(r'f\(x\) ≥ (\d+)', s)
        return (float(m.group(1)), math.inf)
    return pick(ch, (round(lo, 6), round(hi, 6)), conv=rng)


def c06(ch):
    sols = [x for x in range(0, 200) if 3 * x + 10 == 5 * x - 30]
    return pick(ch, sols[0])


def c07(ch):  # coordinates: D at origin, A=(-4,0), B=(9,0), C=(0,h); find h with angle C = 90°
    for h1000 in range(1, 20000):
        h = h1000 / 1000
        if abs((-4) * 9 + h * h) < 1e-9:  # CA · CB = 0
            return pick(ch, h, conv=lambda t: math.sqrt(float(t[1:])) if t.startswith('√') else float(t))
    raise ValueError


def c08(ch):
    seqs = list(product('HT', repeat=5))
    return pick(ch, F(sum(s.count('H') == 3 for s in seqs), len(seqs)))


def c09(ch):
    return pick(ch, math.floor(20 / 0.75))


def c10(ch):  # build a population of 100 students that matches the percents and count directly
    students = [('S', 'F')] * 20 + [('S',)] * 40 + [('F',)] * 25 + [()] * 15
    assert sum('S' in s for s in students) == 60 and sum('F' in s for s in students) == 45
    return pick(ch, sum('S' in s and 'F' not in s for s in students))


CHECKS = {f'B009-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
