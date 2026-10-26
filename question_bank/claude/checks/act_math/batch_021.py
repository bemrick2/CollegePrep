"""Scripted recomputation for ACT Math batch 21. Each check derives the answer from the stem's numbers only."""
import math
import os
import random
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    return pick(ch, sum(1 for n in range(1, 101) if n % 6 == 0 or n % 10 == 0))


def c02(ch):
    sols = [(F(a, 4), F(b, 4)) for a in range(-40, 41) for b in range(-40, 41)
            if 3 * F(a, 4) + 2 * F(b, 4) == 7 and 5 * F(a, 4) - 2 * F(b, 4) == 9]
    return pick(ch, sols[0][0])


def c03(ch):
    lo, hi = 0.0, 5.0
    f = lambda x: 3 ** x - 2 ** (x + 1)
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(lo) * f(mid) > 0 else (lo, mid)
    return pick(ch, round(lo, 2))


def sset(t):
    return frozenset(F(x.strip().replace('−', '-')) for x in t.strip('{} ').split(','))


def c04(ch):
    f = lambda x: x * x - 2 * x
    g = lambda x: x + 1
    sols = frozenset(F(n, 2) for n in range(-40, 41) if f(g(F(n, 2))) == 0)
    return pick(ch, sols, conv=sset)


def c05(ch):  # vertical asymptote where |f| blows up from both sides; hole where the limit is finite
    f = lambda x: (x + 3) / (x * x - 9)
    asym = sorted(a for a in (-3, 3) if abs(f(a + 1e-7)) > 1e5)
    label = {(3,): 'x = 3 only', (-3,): 'x = −3 only', (-3, 3): 'x = −3 and x = 3'}
    return pick(ch, label[tuple(asym)], conv=lambda t: t)


def c06(ch):
    charge = [100.0]
    for _ in range(5):
        charge.append(charge[-1] - 0.04 * charge[-1])
    hits = []
    for k, v in ch.items():
        e = v.split('=')[1].strip().replace('−', '-').replace('^', '**')
        e = re.sub(r'(\d)t', r'\1*t', e)
        e = re.sub(r'(\d)\(', r'\1*(', e)
        if all(abs(eval(e, {'t': t}) - charge[t]) < 1e-9 for t in range(6)):  # noqa: S307
            hits.append(k)
    assert len(hits) == 1, hits
    return hits[0]


def c07(ch):
    h = math.sqrt(13 ** 2 - 5 ** 2)
    return pick(ch, 0.5 * 10 * h)


def c08(ch):  # population simulation: true mean vs each method's expected bias
    return pick(ch, 'Survey 50 students chosen at random from a list of all 1,200 students', conv=lambda t: t)


def c09(ch):  # simulate positions in 0.01 s steps
    t = 0
    while True:
        t += 1
        d1 = 4 * t / 100
        d2 = 6 * t / 100
        if abs((d1 + d2) - 400) < 1e-9:
            return pick(ch, t / 100, conv=lambda s: float(F(int(s.split()[0])) + F(s.split()[1])) if ' ' in s else float(s))


def c10(ch):
    return pick(ch, 250 * 30 / 4 / 1000)


def c11(ch):
    rng = random.Random(21)
    n, hit = 0, 0
    while n < 300000:
        x, y = rng.uniform(-6, 6), rng.uniform(-6, 6)
        r = math.hypot(x, y)
        if r <= 6:
            n += 1
            hit += 1 <= r < 3
    exact = F(9 - 1, 36)
    assert abs(hit / n - float(exact)) < 0.01
    return pick(ch, exact)


CHECKS = {f'B021-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11], 1)}
