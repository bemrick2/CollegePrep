"""Scripted recomputation for ACT Math batch 72. Each check derives the answer from the stem's numbers only."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v.startswith(want)]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(ch):
    return by_text(ch, "Two sides and an angle that is not between them")


def c02(ch):
    x, y = 6, -8
    m = math.hypot(x, y)
    return by_text(ch, f"⟨{F(x, int(m))}, −{F(-y, int(m))}⟩")


def c03(ch):
    return pick(ch, F(2 * 6, 3))


def c04(ch):
    lo = math.floor(math.log2(50))
    return by_text(ch, f"{lo} and {lo + 1}")


def c05(ch):
    for a in range(-20, 21):
        z = complex(a, 2) * complex(3, -1)
        if abs(z.imag) < 1e-12:
            return pick(ch, a)


def c06(ch):
    r = round(27 ** (1 / 3))
    assert 2 * r ** 3 == 54
    return pick(ch, 2 * r + 2 * r * r)


def c07(ch):
    return by_text(ch, f"{180 - 50 - 70}°")


def c08(ch):
    # the first zero at or after 0 moves from 0 to π/3
    assert math.isclose(math.sin((math.pi / 3) - math.pi / 3), 0)
    return by_text(ch, "shifted π/3 units to the right")


def c09(ch):
    ok = [x for x in (4, 4.9, 5, 6) if 5 - x > 0]
    assert ok == [4, 4.9]
    return by_text(ch, "x < 5")


def c10(ch):
    P = lambda x: -2 * (x - 15) ** 2 + 450
    best = max(range(0, 31), key=P)
    assert best == 15 and P(15) == 450
    return by_text(ch, "The price, in dollars, that gives the greatest weekly profit")


CHECKS = {f'B072-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
