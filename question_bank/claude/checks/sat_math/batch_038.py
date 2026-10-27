"""Scripted recomputation for SAT Math batch 38. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    sols = [(a, s) for a in range(151) for s in [150 - a] if (9 * a + 14 * s) - (14 * a + 9 * s) == 150]
    assert len(sols) == 1
    return pick(ch, sols[0][1])


def c02(_):
    ks = [F(n, 2) for n in range(-40, 41) if not (3 * 5 - 7 < 2 * (5 + F(n, 2)))]
    return max(ks)


def c03(ch):
    def empty(k):  # no (x, y) with 2x + 3 < y < 2x + k
        return k <= 3
    hits = [l for l, v in ch.items() if empty(int(v))]
    assert len(hits) == 1
    return hits[0]


def c04(_):
    f0 = F(-7)  # f(0) = 2 f(0) + 7
    m = 4 - f0
    assert m * 2 + f0 == 2 * (m + f0) + 7
    return 3 * m + f0


def c05(_):
    sols = [(k, c) for k in range(-20, 21) for c in range(-20, 21)
            if all((x * x + k * x - 12) == (x - 2) * (x + c) for x in range(-5, 6))]
    assert len(sols) == 1
    return F(sols[0][1])


def c06(ch):
    t = next(t for t in range(100) if 2000 * 1.15 ** t > 6000 * 1.06 ** t)
    return pick(ch, t)


def c07(ch):
    sols = [b for b in (F(n, 5) for n in range(-50, 51)) if 2 * (b + 1) + 3 * b == 12]
    return pick(ch, float(sols[0]))


def c08(_):
    disc = 25 - 4
    assert disc > 0
    r1, r2 = (5 + math.sqrt(disc)) / 2, (5 - math.sqrt(disc)) / 2
    assert all(math.isclose(k * (k - 5), -1) for k in (r1, r2))
    return F(round(r1 + r2))


def c09(_):
    return F(24, 100) * 600 / F(6, 10)


def c10(_):
    cost = F(100)
    return (cost * F(125, 100) - cost * F(110, 100)) / (cost * F(125, 100)) * 100


def c11(_):
    theta = (16 * math.pi / 3) / 8
    area = 0.5 * 8 * 8 * math.sin(theta)
    return F(round(area / math.sqrt(3), 9)).limit_denominator(1000)


def c12(_):
    s = next(s for s in range(1, 100) if 2 * s * s + 4 * s * (s + 3) == 210)
    return F(s * s * (s + 3))


CHECKS = {f'Q038-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
