"""Scripted recomputation for SAT Math batch 48. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    a = lambda p: 12 + F(8, 100) * p
    b = lambda p: 27 + F(5, 100) * p
    c = lambda p: F(11, 100) * p
    ok = [p for p in range(0, 1001) if a(p) < b(p) and a(p) < c(p)]
    assert ok[0] == 401 and ok[-1] == 499
    return by_text(ch, "400 < p < 500")


def c02(ch):
    return pick(ch, 58 - 2.5 * (10500 - 4000) / 1000)


def c03(ch):
    def sols(a, b):
        return [x for x in (F(n, 4) for n in range(-80, 81)) if a * x + 5 >= 3 * x + b]
    target = [x for x in (F(n, 4) for n in range(-80, 81)) if x <= 4]
    pairs = {'A': (2, 1), 'B': (2, 9), 'C': (3, 5), 'D': (4, 9)}
    hits = [k for k, (a, b) in pairs.items() if sols(a, b) == target]
    assert len(hits) == 1 and ch[hits[0]].startswith(f"a = {pairs[hits[0]][0]}")
    return hits[0]


def c04(_):
    d0, d10 = 8, -12
    m = F(d10 - d0, 10)
    return -d0 / m


def c05(ch):
    a = F(-12, 4 * -6)
    f = lambda x: a * (x + 4) * (x - 6)
    return pick(ch, float(f(0 - 3)))


def c06(ch):
    x = 32 ** (2 / 5)
    return pick(ch, round(x ** -1.5, 9))


def c07(_):
    xs, ys = (3 + 4, 3 - 4), (-2 + 3, -2 - 3)
    return F(max(x - y for x in xs for y in ys))


def c08(_):
    data = list(range(1, 11))
    new = [v + 5 for v in data[:9]] + [data[9] + 25]
    med = lambda d: F(sorted(d)[4] + sorted(d)[5], 2)
    return (F(sum(new), 10) - F(sum(data), 10)) - (med(new) - med(data))


def c09(_):
    return F(45, 10) * 7200 / 8 / 1000


def c10(ch):
    s = 3 / (math.sqrt(2) - 1)
    assert math.isclose(s * math.sqrt(2), s + 3)
    assert math.isclose(s + 3, 6 + 3 * math.sqrt(2))
    return by_text(ch, "6 + 3√2")


def c11(ch):
    per = 2 * (16 - 8) + 2 * (10 - 8) + 4 * 4 * math.sqrt(2)
    assert math.isclose(per, 20 + 16 * math.sqrt(2))
    return by_text(ch, "20 + 16√2")


def c12(_):
    t = next(t for t in range(0, 200) if math.isclose(22 + 64 * 0.5 ** (t / 10), 38))
    return F(t)


CHECKS = {f'Q048-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
