"""Scripted recomputation for ACT Math batch 5. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F
from statistics import pstdev

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    lo, hi = F(3, 8), F(5, 12)
    hits = [k for k, v in ch.items() if lo < F(v) < hi]
    assert len(hits) == 1, hits
    return hits[0]


def c02(ch):
    t = next(m for m in range(1, 1000) if m % 12 == 0 and m % 18 == 0)
    h, mm = divmod(7 * 60 + t, 60)
    return pick(ch, f'{h}:{mm:02d} a.m.', conv=lambda s: s.strip())


def c03(ch):
    sols = [x for x in range(-50, 51) if 4 ** (x + 1) == F(8) ** (x - 1)]
    return pick(ch, sols[0])


def c04(ch):
    f = lambda x: x * x - 3 * x
    return pick(ch, F(f(5) - f(1), 5 - 1))


def c05(ch):  # evaluate each expression for two bases and compare with log_b(18/b)
    hits = []
    for k, v in ch.items():
        ok = True
        for b in (2.0, 7.0):
            p, q = math.log(2, b), math.log(3, b)
            e = v.replace('−', '-').replace('2pq', '2*p*q').replace('2q', '2*q').replace('q²', 'q**2')
            if abs(eval(e, {'p': p, 'q': q, 'b': b}) - math.log(18 / b, b)) > 1e-9:  # noqa: S307
                ok = False
        if ok:
            hits.append(k)
    assert len(hits) == 1, hits
    return hits[0]


def pi_expr(t):  # '1150π/3', '425π', '300π'
    m = re.fullmatch(r'(\d+)π(?:/(\d+))?', t.strip())
    return int(m.group(1)) * math.pi / int(m.group(2) or 1)


def c06(ch):
    r, h = 5, 12
    return pick(ch, math.pi * r * r * h + (4 / 3) * math.pi * r**3 / 2, conv=pi_expr)


def c07(ch):
    k = F(6, 6 + 4)
    abc = 54 / k**2
    return pick(ch, abc - 54)


def c08(ch):
    e = 10 * 0.1 + 4 * 0.2 + 0 * 0.7 - 2
    return pick(ch, round(e, 9))


def c09(ch):
    sds = {k: pstdev([int(x) for x in v.split(',')]) for k, v in ch.items()}
    best = max(sds.values())
    hits = [k for k, s in sds.items() if s == best]
    assert len(hits) == 1
    return hits[0]


def c10(ch):
    gal = 300 / 30 + (420 - 300) / 20
    return pick(ch, round(gal * 3.60, 2))


CHECKS = {f'B005-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
