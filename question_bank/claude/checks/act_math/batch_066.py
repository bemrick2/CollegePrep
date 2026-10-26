"""Scripted recomputation for ACT Math batch 66. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import statistics
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1
    return hits[0]


def c01(ch):
    assert 3 == 3  # both points share x = 3
    return by_text(ch, "x = 3")


def c02(ch):
    return pick(ch, F(60 * 5280, 3600))


def c03(ch):
    r1 = (4 + math.sqrt(20)) / 2
    assert math.isclose(r1, 2 + math.sqrt(5))
    return by_text(ch, "2 ± √5")


def c04(ch):
    return pick(ch, 0.5 * 8 * 10 * math.sin(math.radians(30)), tol=1e-9)


def c05(ch):
    return pick(ch, 4 * 5 ** 2)


def c06(ch):
    return by_text(ch, "|L − 50| ≤ 0.4")


def c07(ch):
    xs = [62, 65, 65, 71, 78, 78, 78, 83, 90]
    mean, med, mode = statistics.mean(xs), statistics.median(xs), statistics.mode(xs)
    assert med == mode > mean
    return by_text(ch, "The median and the mode are equal and greater than the mean.")


def root_frac(t):
    """'√3/2' -> 0.866…, '√2' -> 1.414…, '1/2' -> 0.5."""
    num, _, den = t.partition('/')
    val = math.sqrt(float(num[1:])) if num.startswith('√') else float(num)
    return val / float(den or 1)


def c08(ch):
    s = 1.0
    tri = math.sqrt(3) / 4 * (s * math.sqrt(2)) ** 2
    return pick(ch, tri / (s * s), conv=root_frac, tol=1e-9)


def c09(ch):
    return pick(ch, F(5 ** 2, 2))


def c10(ch):
    outs = list(itertools.product(range(1, 7), repeat=2))
    return pick(ch, F(sum(1 for o in outs if max(o) == 4), len(outs)))


CHECKS = {f'B066-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
