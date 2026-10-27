"""Scripted recomputation for SAT Math batch 64. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    gaps = set()
    for f in (lambda x: x * x, lambda x: 7 - 3 * x, lambda x: 2 ** x):
        for x in (-2, 0, 1.5, 4):
            g = 3 * (f(x) + 4)
            h = 3 * f(x) + 4
            gaps.add(round(g - h, 9))
    assert len(gaps) == 1
    return F(gaps.pop()).limit_denominator()


def c02(_):
    # Fit h(t) = a t^2 + b t + c through the three points.
    pts = [(2, 51), (3, 61), (4, 61)]
    a = F(pts[2][1] - 2 * pts[1][1] + pts[0][1], 2)
    b = F(pts[1][1] - pts[0][1]) - a * (3 + 2)
    c = pts[0][1] - a * 4 - b * 2
    assert all(a * t * t + b * t + c == h for t, h in pts)
    v = -b / (2 * a)
    return a * v * v + b * v + c


def c03(ch):
    f2 = F(32805, 40500)
    assert f2 == F(81, 100)
    return pick(ch, F(40500) / f2)


def c04(ch):
    N = lambda t: 500 * 2 ** (t / 4) * 0.5 ** (t / 12)
    d = [k for k in (4, 6, 8, 16) if all(abs(N(t + k) / N(t) - 2) < 1e-12 for t in (0, 3, 10))]
    assert d == [6]
    return by_text(ch, f"N doubles every {d[0]} hours.")


def c05(ch):
    x = F(3 + 1, 2)
    assert 2 * x - 1 == 3
    return by_text(ch, f"x − {x}")


def c06(ch):
    true = []
    rng = [(1, -8, 5), (0.5, -4, -3), (3, -24, 1)]  # a > 0, axis x = 4
    for a, b, c in rng:
        f = lambda x: a * x * x + b * x + c
        assert abs(f(2) - f(6)) < 1e-9
    tests = {"f(0) > f(3)": (0, 3), "f(1) > f(7)": (1, 7), "f(4) > f(5)": (4, 5), "f(3) > f(8)": (3, 8)}
    for txt, (p, q) in tests.items():
        if all((a * p * p + b * p + c) > (a * q * q + b * q + c) for a, b, c in rng):
            true.append(txt)
    assert len(true) == 1
    return by_text(ch, true[0])


def c07(_):
    a = 60 - 20
    b = F(60 - 40, a) ** F(1, 3)
    W = lambda t: 60 - a * (F(1, 2) ** F(t, 3))
    assert W(0) == 20 and W(3) == 40
    return W(6)


def c08(ch):
    counts = set()
    for a in (0.1, 0.5, 1, 2, 7):
        # |x-2| = a (x-2)^2  -> roots at x = 2 and x = 2 +/- 1/a
        sols = {2.0, 2 + 1 / a, 2 - 1 / a}
        for x in sols:
            assert abs(abs(x - 2) - a * (x - 2) ** 2) < 1e-9
        counts.add(len(sols))
    assert counts == {3}
    return pick(ch, 3)


def c09(_):
    # vertex (3, -4): f = (x-3)^2 - 4 = x^2 - 6x + 5
    a, b = 1, 5
    f = lambda x: (x - a) * (x - b)
    assert f(3) == -4 and (a + b) / 2 == 3
    return F(a * b)


def c10(ch):
    good = []
    for k in (-0.3, -0.2, 0.2, 2):
        disc = 1 + 4 * k
        n = 0
        if disc >= 0:
            for x in {(1 + math.sqrt(disc)) / 2, (1 - math.sqrt(disc)) / 2}:
                if x >= 0 and x + k >= 0 and abs(math.sqrt(x + k) - x) < 1e-9:
                    n += 1
        if n == 2:
            good.append(k)
    assert good == [-0.2]
    return pick(ch, -0.2)


def c11(_):
    # 2b + c = -4, b + c = -7
    b = F(-4 - (-7))
    c = -7 - b
    p = lambda x: x ** 3 + b * x * x + c * x
    assert p(2) == 0 and p(1) == -6
    return F(p(-1))


def c12(ch):
    # Grid search over x in steps of 0.01; values of k with irrational roots always give two or zero hits, never one.
    ks = []
    for k in range(-10, 11):
        sols = set()
        for x2 in range(-4000, 4001):
            x = F(x2, 100)
            if x != 2 and x * x - 2 * x - k == 0:
                sols.add(x)
        if len(sols) == 1:
            ks.append(k)
    assert ks == [-1, 0], ks
    return by_text(ch, "{−1, 0}")


CHECKS = {f'Q064-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12], 1)}
