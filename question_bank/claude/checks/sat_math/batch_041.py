"""Scripted recomputation for SAT Math batch 41. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    sols = [(a, b) for a in range(1, 50) for b in range(1, 50) if F(a - b, 2) == -1 and F(a + b, 2) == 5]
    assert len(sols) == 1
    return F(sols[0][0])


def c02(ch):
    m = F(-1 - 5, 4 - 1)
    b = 5 - m
    return pick(ch, float(b / (1 - m)))


def c03(_):
    q = next(q for q in range(0, 200) if F(25, 100) * q - F(10, 100) * (q + 5) == F(130, 100))
    return F(q + 5)


def c04(ch):
    k = next(k for k in range(-50, 51) if F(k - 4, 2) == F(2 * k - k, 4))
    return pick(ch, k)


def c05(_):
    p = next(p for p in range(6, 200) if F(120, p - 5) == F(120, p) + 2)
    return F(p)


def c06(ch):
    expr = {'xy/(x + y)': lambda x, y: x * y / (x + y), 'x + y': lambda x, y: x + y,
            'xy': lambda x, y: x * y, '(x + y)/(xy)': lambda x, y: (x + y) / (x * y)}
    pts = [(F(2), F(3)), (F(1), F(5)), (F(7, 2), F(4))]
    hits = [t for t, f in expr.items() if all(f(x, y) == 1 / (1 / x + 1 / y) for x, y in pts)]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c07(ch):
    x = math.log(8, 2) / 2
    assert math.isclose(2 ** x, 8 * 2 ** -x)
    return pick(ch, 2 ** x)


def c08(ch):
    f = lambda x: (x + 1) ** 2 + 2 * (x + 1)  # f(u) with x = u + 1
    cands = {'f(x) = x² − 1': lambda x: x * x - 1, 'f(x) = x² + 2x + 1': lambda x: x * x + 2 * x + 1,
             'f(x) = x² + 4x + 1': lambda x: x * x + 4 * x + 1, 'f(x) = x² + 4x + 3': lambda x: x * x + 4 * x + 3}
    hits = [t for t, g in cands.items() if all(g(x) == f(x) for x in range(-5, 6))]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c09(ch):
    def stats(freq):
        data = [v for v, n in zip(range(1, 6), freq) for _ in range(n)]
        mu = sum(data) / len(data)
        return mu, math.sqrt(sum((d - mu) ** 2 for d in data) / len(data))
    (ma, sa), (mb, sb) = stats((1, 2, 4, 2, 1)), stats((4, 1, 0, 1, 4))
    assert ma == mb and sb > sa
    return by_text(ch, "The means are equal, and the standard deviation of set B is greater.")


def c10(_):
    return F(str(round((1000 / 2.7) ** (1 / 3), 1)))


def c11(ch):
    cx, cy = F(8, 2), F(-2, 2)
    assert 1 + 9 - 8 * 1 + 2 * 3 - 8 == 0
    pt = (int(2 * cx - 1), int(2 * cy - 3))
    return by_text(ch, f"({pt[0]}, {pt[1]})".replace('-', '−'))


def c12(_):
    r = F(36, 4)
    return F(1, 2) * r * r * 2


CHECKS = {f'Q041-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
