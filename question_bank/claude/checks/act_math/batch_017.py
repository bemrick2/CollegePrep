"""Scripted recomputation for ACT Math batch 17. Each check derives the answer from the stem's numbers only."""
import math
import os
import sys
from fractions import Fraction as F
from itertools import permutations

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    A = [[1, 2], [3, 4]]
    B = [[2, 0], [1, 5]]
    AB = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    return pick(ch, AB[1][0])


def c02(ch):  # long division of the repeating decimal: x = 0.(36)
    x = sum(F(36, 100 ** k) for k in range(1, 40))
    return pick(ch, F(x).limit_denominator(1000))


def c03(ch):  # a continuous linear f has a root iff it changes sign on a huge interval or is identically zero
    from _util import num
    def has_solution(k):
        f = lambda x: k * x + 3 - (4 * x - 7)
        lo, hi = f(-1e9), f(1e9)
        return lo * hi <= 0
    hits = [key for key, v in ch.items() if not has_solution(num(v))]
    assert len(hits) == 1, hits
    return hits[0]


def sset(t):
    return frozenset(F(x.strip().replace('−', '-').replace(',', '')) for x in t.strip('{} ').split(', ') if x)


def c04(ch):
    cbrt = lambda x: math.copysign(abs(x) ** (1 / 3), x)
    sols = frozenset(F(x) for x in range(-5000, 5001) if abs(cbrt(x) ** 2 - 16) < 1e-9)
    hits = [k for k, v in ch.items() if frozenset(F(y.strip().replace('−', '-').replace(',', '')) for y in v.strip('{}').split(', ')) == sols]
    assert len(hits) == 1, (sols, hits)
    return hits[0]


def c05(ch):
    sols = [(a, b) for a in range(0, 32) for b in range(0, 32) if a + b == 31 and a + 5 == 2 * (b - 3)]
    return pick(ch, sols[0][0])


def c06(ch):
    dist, h, hits = 0.0, 16.0, 0
    dist += h
    hits = 1
    while hits < 4:
        h /= 2
        dist += 2 * h
        hits += 1
    return pick(ch, dist)


def c07(ch):  # coordinates: P at origin, Q at 7 along x-axis, R at 8 units at 60 degrees
    Q = (7.0, 0.0)
    R = (8 * math.cos(math.radians(60)), 8 * math.sin(math.radians(60)))
    qr = math.dist(Q, R)
    return pick(ch, qr, conv=lambda t: math.sqrt(float(t[1:])) if t.startswith('√') else float(t), tol=1e-9)


def c08(ch):  # centers (0,0) r=5 and (10,0) r=3; find external tangent numerically by angle search
    best = None
    for i in range(1, 200000):
        th = math.pi * i / 200000  # normal direction of the line
        n = (math.cos(th), math.sin(th))
        # line: n·p = c with distance from centers equal to radii on same side
        c = 5.0  # n·(0,0) - c = -5  -> c = 5
        d2 = n[0] * 10 - c
        if abs(d2 - (-3)) < 1e-6 or abs(abs(d2) - 3) < 1e-4 and d2 < 0:
            t1 = (5 * n[0], 5 * n[1])
            t2 = (10 + 3 * n[0], 3 * n[1])
            best = math.dist(t1, t2)
            break
    def conv(t):
        return 4 * math.sqrt(6) if t == '4√6' else float(t)
    return pick(ch, best, conv=conv, tol=1e-3)


def c09(ch):
    return pick(ch, len(set(permutations('LEVEL'))))


def c10(ch):
    import statistics as st
    old = [4, 7, 9, 12, 15]
    new = sorted(old + [1, 20])
    same = {'median': st.median(old) == st.median(new), 'mean': st.mean(old) == st.mean(new),
            'range': max(old) - min(old) == max(new) - min(new)}
    label = {frozenset(['median']): 'The median only', frozenset(['mean']): 'The mean only',
             frozenset(['median', 'range']): 'The median and the range', frozenset(['mean', 'median']): 'The mean and the median'}
    return pick(ch, label[frozenset(k for k, v in same.items() if v)], conv=lambda t: t)


CHECKS = {f'B017-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
