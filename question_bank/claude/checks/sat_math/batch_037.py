"""Scripted recomputation for SAT Math batch 37. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(ch):
    H = lambda A: F(54 + 8 * A, 3)
    return pick(ch, float(H(1) - H(0)))


def c02(ch):
    t = F(270 + 60 * F(1, 2), 40 + 60)
    minutes = int(t * 60)
    return by_text(ch, f"{1 + minutes // 60}:{minutes % 60:02d} p.m.")


def c03(ch):
    cost = lambda n: 35 * min(n, 3) + 28 * max(n - 3, 0)
    exprs = {'28n + 105': lambda n: 28 * n + 105, '28n + 21': lambda n: 28 * n + 21,
             '35n − 21': lambda n: 35 * n - 21, '63n − 84': lambda n: 63 * n - 84}
    hits = [t for t, e in exprs.items() if all(e(n) == cost(n) for n in range(3, 40))]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c04(_):
    best = max((F(60) * t / (t * t + 9), t) for t in (F(n, 100) for n in range(0, 2001)))
    assert best[1] == 3
    return best[0]


def c05(ch):
    import random
    rnd = random.Random(1)
    counts = set()
    for _ in range(2000):
        a, b, c = -rnd.uniform(0.01, 10), rnd.uniform(-50, 50), rnd.uniform(0.01, 10)
        counts.add(2 if b * b - 4 * a * c > 0 else (1 if b * b == 4 * a * c else 0))
    assert counts == {2}
    return by_text(ch, '2')


def c06(_):
    return F(round(2000 / 1.05 ** 3))


def c07(_):
    return F('0.4') * 100 * 100 / 1000


def c08(_):
    d = math.hypot(9, 12)
    return F(int(d - 5))


def c09(ch):
    ok = [x / 100 for x in range(1, 2000)
          if all(s > 0 for s in (x / 100, x / 100 + 3, 2 * x / 100 - 1))
          and x / 100 + x / 100 + 3 > 2 * x / 100 - 1 and x / 100 + 2 * x / 100 - 1 > x / 100 + 3
          and x / 100 + 3 + 2 * x / 100 - 1 > x / 100]
    assert math.isclose(min(ok), 2.01)
    return by_text(ch, 'x > 2')


def c10(_):
    f = {1: 5, 2: 3, 3: 8, 4: 2, 5: 6}
    sols = [x for x in range(0, 5) if x + 1 in f and f[x + 1] - 2 == 6]
    assert sols == [2]
    return F(2)


CHECKS = {f'Q037-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
