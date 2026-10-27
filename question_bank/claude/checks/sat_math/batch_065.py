"""Scripted recomputation for SAT Math batch 65. Multiple-choice checks return a letter; SPR checks receive None and return the value.
Items Q065-10 to Q065-17 are batch-64 revisions and reuse that batch's checks."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402
import batch_064 as b64  # noqa: E402


def deg(text):
    return num(text.replace('°', ''))


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    xs = sorted(x for x in range(-10, 11) if x * x == x + 2)
    (x1, y1), (x2, y2) = [(x, x * x) for x in xs]
    return F(abs(x1 * y2 - x2 * y1), 2)


def c02(ch):
    sols = [F(x, 2) for x in range(-100, 101) if abs(F(x, 2) - 3) + abs(F(x, 2) + 5) == 10]
    assert len(sols) == 2
    return pick(ch, sum(sols))


def c03(ch):
    xs = [F(x, 10) for x in range(1, 1000) if -F(5, 100) * F(x, 10) ** 2 + 2 * F(x, 10) == F(1, 2) * F(x, 10)]
    assert len(xs) == 1
    return pick(ch, xs[0])


def c04(ch):
    A = 50
    # exterior angle at C = A + B; half of it equals A (corresponding) and B (alternate)
    for B in range(1, 130):
        if (A + B) / 2 == A and (A + B) / 2 == B:
            return pick(ch, 180 - A - B, conv=deg)
    raise AssertionError


def c05(ch):
    arc_abc = 2 * 70
    ab = bc = cd = arc_abc / 2
    da = 360 - ab - bc - cd
    return pick(ch, da / 2, conv=deg)


def c06(_):
    x, y = 5 + 3 * math.cos(math.radians(60)), 3 * math.sin(math.radians(60))
    d1 = math.hypot(x, y)
    x2 = 5 - 3 * math.cos(math.radians(60))
    d2 = math.hypot(x2, y)
    assert d1 > d2 and abs(d1 - 7) < 1e-12
    return F(7)


def c07(ch):
    areas = set()
    for h1 in (F(18 * 2, 10),):
        h2 = 10 - h1
        areas.add(F(1, 2) * 10 * h2)
    return pick(ch, areas.pop())


def c08(_):
    r, k = 5, 6
    hs = [h for h in range(-20, 21) if (2 - h) ** 2 + (9 - k) ** 2 == r * r]
    h = [h for h in hs if h > 0]
    assert len(h) == 1 and k - r == 1 and k + r == 11
    return F(h[0] ** 2 + k * k - r * r)


def c09(ch):
    tri = {tuple(sorted((a, b, 30 - a - b))) for a in range(1, 30) for b in range(1, 30)
           if 30 - a - b > 0}
    ok = [t for t in tri if t[0] + t[1] > t[2] and len(set(t)) < 3]
    return pick(ch, len(ok))


CHECKS = {f'Q065-{i:02d}': f for i, f in enumerate(
    [c01, c02, c03, c04, c05, c06, c07, c08, c09, b64.c01, b64.c02, b64.c04, b64.c05, b64.c06, b64.c07, b64.c10, b64.c12], 1)}
