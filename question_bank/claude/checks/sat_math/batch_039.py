"""Scripted recomputation for SAT Math batch 39. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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


def c01(_):
    miles = (F('26.00') - F('2.50') - F('0.40') * 15) / F('1.75')
    return miles / F(15, 60)


def c02(ch):
    old = next(x for x in range(1, 200) if 5 * F(6, 5) * x == 4 * x + 30)
    return pick(ch, float(F(6, 5) * old))


def c03(ch):
    side = lambda x, y: 4 * x - 3 * y < 12
    pts = {k: tuple(int(t.strip().replace('−', '-')) for t in v.strip('()').split(',')) for k, v in ch.items()}
    hits = [k for k, p in pts.items() if side(*p) == side(0, 0)]
    assert len(hits) == 1
    return hits[0]


def c04(ch):
    d = F(4) / (F(1, 50) + F(1, 30))
    return pick(ch, float(d))


def c05(_):
    ks = []
    for n in range(-40, 41):
        k = F(n, 4)
        if k == 0:
            continue
        a, b, c = k, -2 * k, -3 * k + 8  # g(x) = k(x^2 - 2x - 3) + 8
        if b * b - 4 * a * c == 0:
            ks.append(k)
    assert ks == [2]
    return F(2)


def c06(ch):
    x = 8 ** (4 / 3)
    assert math.isclose(math.sqrt(x * math.sqrt(x)), 8)
    return pick(ch, round(x, 9))


def c07(ch):
    import random
    rnd = random.Random(2)
    keep = {k: True for k in ch}
    tests = {"b < 0 and b² > 4c": lambda b, c: b < 0 and b * b > 4 * c,
             "b < 0 and c < 0": lambda b, c: b < 0 and c < 0,
             "b > 0 and c < 0": lambda b, c: b > 0 and c < 0,
             "b > 0 and b² > 4c": lambda b, c: b > 0 and b * b > 4 * c}
    for _ in range(20000):
        b, c = rnd.uniform(-20, 20), rnd.uniform(-50, 50)
        if -b / 2 > 0 and c - b * b / 4 < 0:  # vertex in Quadrant IV
            for k, v in ch.items():
                if not tests[v](b, c):
                    keep[k] = False
    hits = [k for k, v in keep.items() if v]
    assert len(hits) == 1
    return hits[0]


def c08(ch):
    f_rate, g_rate = 1 - 0.95, 1 - 0.9 ** 0.5
    assert g_rate > f_rate
    return by_text(ch, "The value g decreases by a greater percent each year than f does.")


def c09(ch):
    return by_text(ch, f"y = {int(2.5 * 100)}x + {int(10 * 100):,}")


def c10(ch):
    old, new = 60 / 8, 60 / 7.5
    pct = round((new - old) / old * 100, 2)
    return by_text(ch, f"{pct}%")


def c11(_):
    v = F(2, 3) * 9 ** 3  # in units of pi
    return v / 6 ** 2


def c12(_):
    ad = F(6 * 6, 9)
    return 9 - ad


CHECKS = {f'Q039-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
