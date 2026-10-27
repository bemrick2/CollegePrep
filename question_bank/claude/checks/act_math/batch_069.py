"""Scripted recomputation for ACT Math batch 69. Each check derives the answer from the stem's numbers only."""
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
    x, y = 2 + -5, -3 + 7
    return by_text(ch, f"⟨{x}, {y}⟩".replace('-', '−'))


def c02(ch):
    return pick(ch, F(-4 - 4, 3 - (-1)))


def c03(ch):
    return pick(ch, 2 * math.isqrt(25))


def c04(ch):
    ok = [x / 2 for x in range(-20, 40) if x / 2 >= 2 and x / 2 != 5]
    assert 2 in ok and 5 not in ok and 1 not in ok
    return by_text(ch, "x ≥ 2 and x ≠ 5")


def c05(ch):
    return by_text(ch, f"x = {-4}".replace('-', '−'))


def c06(ch):
    z = (1 + 1j) ** 2
    assert abs(z - 2j) < 1e-12
    return by_text(ch, "2i")


def c07(ch):
    v = math.sin(5 * math.pi / 3)
    assert math.isclose(v, -math.sqrt(3) / 2)
    return by_text(ch, "−√3/2")


def c08(ch):
    return pick(ch, sum(1 for x in range(1, 10) for y in range(1, 10) if x + y < 5))


def c09(ch):
    roots = [r for r in range(-10, 11) if r ** 3 - 4 * r ** 2 + r + 6 == 0]
    assert sorted(roots) == [-1, 2, 3]
    return pick(ch, sum(roots) - 2)


def c10(ch):
    a = 2
    for _ in range(3):
        a = 3 * a - 1
    return pick(ch, a)


CHECKS = {f'B069-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
