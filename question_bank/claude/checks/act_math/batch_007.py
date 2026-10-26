"""Scripted recomputation for ACT Math batch 7. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F
from itertools import combinations_with_replacement

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def ndiv(m):
    return sum(1 for d in range(1, m + 1) if m % d == 0)


def c01(ch):
    return pick(ch, sum(n for n in range(1, 10) if ndiv(n * n) == 3))


def c02(ch):
    return pick(ch, 27 ** (-2 / 3), tol=1e-9)


def c03(ch):  # scan c on a fine grid; record which c satisfy the condition; match against interval choices
    def ok(c):
        disc = 36 - 4 * c
        if disc <= 0:
            return False
        r1, r2 = (6 - math.sqrt(disc)) / 2, (6 + math.sqrt(disc)) / 2
        return r1 > 1 and r2 > 1
    grid = [i / 20 for i in range(-200, 400)]
    good = frozenset(c for c in grid if ok(c))
    def region(t):
        s = t.replace('−', '-')
        m = re.fullmatch(r'(-?[\d.]+) < c < (-?[\d.]+)', s)
        if m:
            return frozenset(c for c in grid if float(m.group(1)) < c < float(m.group(2)))
        m = re.fullmatch(r'c < (-?[\d.]+)', s)
        if m:
            return frozenset(c for c in grid if c < float(m.group(1)))
        m = re.fullmatch(r'c > (-?[\d.]+)', s)
        return frozenset(c for c in grid if c > float(m.group(1)))
    return pick(ch, good, conv=region)


def c04(ch):
    rate = (17 - 9.5) / (5 - 2)
    h0 = 17 + 2 * rate
    return pick(ch, round(h0 / rate, 6))


def c05(ch):  # find the real value that f never outputs: scan outputs densely, then test candidates
    f = lambda x: (3 * x + 1) / (x - 2)
    from _util import num
    hits = []
    for k, v in ch.items():
        y = num(v)
        # f(x) = y has a solution iff x = (2y+1)/(y-3) is defined and != 2
        solvable = abs(y - 3) > 1e-12 and abs((2 * y + 1) / (y - 3) - 2) > 1e-12
        if solvable:
            x = (2 * y + 1) / (y - 3)
            assert abs(f(x) - y) < 1e-9
        else:
            hits.append(k)
    assert len(hits) == 1, hits
    return hits[0]


def c06(ch):
    g = lambda x: 2.0 ** x
    def as_expr(t):
        return lambda x: eval(t.replace('g(x)', 'g(x)').replace('3g', '3*g').replace('8g', '8*g'), {'g': g, 'x': x})  # noqa: S307
    hits = [k for k, v in ch.items() if all(abs(as_expr(v)(x) - g(x + 3)) < 1e-9 for x in (-1.5, 0, 0.7, 2))]
    assert len(hits) == 1, hits
    return hits[0]


def c07(ch):  # coordinates: diameter AB on unit circle, C placed so angle BAC = 28°
    A, B = (-1.0, 0.0), (1.0, 0.0)
    # C on circle with angle at A of 28°: C = (cos t, sin t); find t by scanning
    best = None
    for i in range(1, 18000):
        t = math.radians(i / 100)
        C = (math.cos(t), math.sin(t))
        v1 = (B[0] - A[0], B[1] - A[1]); v2 = (C[0] - A[0], C[1] - A[1])
        ang = math.degrees(math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / (math.hypot(*v1) * math.hypot(*v2))))
        if best is None or abs(ang - 28) < abs(best[0] - 28):
            best = (ang, t)
    arc_bc = math.degrees(best[1])  # central angle from B (angle 0) to C
    return pick(ch, round(arc_bc), conv=lambda s: float(s.strip('°')))


def c08(ch):
    count = 0
    for lst in combinations_with_replacement(range(1, 40), 5):
        if lst[2] != 8 or sum(lst) != 35:
            continue
        freq = {v: lst.count(v) for v in lst}
        top = max(freq.values())
        if freq.get(10, 0) == top and sum(1 for v in freq if freq[v] == top) == 1:
            count += 1
    return pick(ch, count)


def c09(ch):
    import math as m
    return pick(ch, m.ceil(30 * 45 / 9 / 10))


def c10(ch):
    return pick(ch, 24 / (12 / 8 + 12 / 24))


CHECKS = {f'B007-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
