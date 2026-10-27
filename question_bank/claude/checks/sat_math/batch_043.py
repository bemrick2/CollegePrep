"""Scripted recomputation for SAT Math batch 43. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    sol = lambda k: F(k + 2, 2)
    ks = [k for k in range(-50, 51) if sol(k + 6) == 2 * sol(k)]
    assert ks == [4]
    return F(4)


def c02(ch):
    m = F(0 - (-6), 4 - 0)
    return pick(ch, float(m * 10 - 6))


def c03(ch):
    on_or_above = lambda x, y: y >= 3 - F(x, 2)
    cands = {'x + 2y ≥ 6': lambda x, y: x + 2 * y >= 6, 'x + 2y ≤ 6': lambda x, y: x + 2 * y <= 6,
             '2x + y ≥ 6': lambda x, y: 2 * x + y >= 6, '2x + y ≤ 6': lambda x, y: 2 * x + y <= 6}
    pts = [(x, y) for x in range(-6, 7) for y in range(-6, 7)]
    hits = [t for t, f in cands.items() if all(f(x, y) == on_or_above(x, y) for x, y in pts)]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c04(ch):
    s, d = F(300, 2), F(300, 10)
    return pick(ch, float((s + d) / 2))


def c05(_):
    sols = [(a, b) for a in range(1, 40) for b in range(1, 40) if 2 * (a + b) == 40 and 2 * (a + 4 + F(b, 2)) == 34]
    assert len(sols) == 1
    a, b = sols[0]
    return F(a * b)


def c06(ch):
    r = math.sqrt(3)
    roots = [r + 2 * r, r - 2 * r]
    assert all(math.isclose(x * x - 2 * r * x - 9, 0, abs_tol=1e-9) for x in roots)
    return pick(ch, max(roots))


def c07(ch):
    p = lambda x: (x + 2) * (x - 4) ** 2
    return pick(ch, p(0))


def c08(ch):
    b = 3  # b^2 = 9, b > 0
    a = F(6, b)
    return pick(ch, float(a * F(1, b)))


def c09(ch):
    diffs = set()
    for k in range(-20, 21):
        f = lambda x: 2 * x * x - 16 * x + k
        diffs.add(f(0) - min(f(F(n, 4)) for n in range(-40, 80)))
    assert diffs == {32}
    return pick(ch, 32)


def c10(ch):
    dist = {0: F(25, 100), 1: F(40, 100), 2: F(25, 100), 3: F(10, 100)}
    mean = sum(k * p for k, p in dist.items())
    cum, med = 0, None
    for k in sorted(dist):
        cum += dist[k]
        if cum > F(1, 2):
            med = k
            break
    return pick(ch, float(mean - med))


def c11(ch):
    n = next(n for n in range(7, 500) if (F(2, 5) * n).denominator == 1 and F(F(2, 5) * n - 6, n - 6) == F(1, 4))
    return pick(ch, n)


def c12(ch):
    r = F(60, 2 * 6)
    return by_text(ch, f"{int(r * r * 6)}π")


def c13(_):
    cases = [180 - 2 * (180 - 100), 180 - 100]
    return F(min(cases))


CHECKS = {f'Q043-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13], 1)}
