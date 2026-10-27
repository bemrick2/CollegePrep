"""Scripted recomputation for SAT Math batch 31. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    h = lambda x: 2 ** x - (x + 3)
    lo, hi = 2.0, 3.0
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if h(mid) < 0 else (lo, mid)
    return by_text(ch, f"{round(lo, 1)}")


def c02(_):
    sols = [x for x in range(1, 1000) if (x ** 0.5) * 4 == x]
    assert sols == [16]
    return 16


def c03(ch):
    x = next(x for x in range(1, 100) if 100 * 1.1 ** x > 100 + 15 * x)
    return pick(ch, x)


def c04(ch):
    xs, ys = [1, 2, 3, 4], [3.1, 4.9, 7.2, 8.8]
    mx, my = sum(xs) / 4, sum(ys) / 4
    m = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    b = my - m * mx
    assert round(m, 2) == 1.94 and round(b, 2) == 1.15
    return by_text(ch, "y = 1.94x + 1.15")


def c05(ch):
    for b in (4, 5, -2, F(1, 2)):
        x = F(2 * b + 5) / (b - 3)
        assert b * x - 5 == 3 * x + 2 * b
    return by_text(ch, "x = (2b + 5)/(b − 3)")


CHECKS = {f'Q031-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05], 1)}
