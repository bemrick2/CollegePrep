"""Scripted recomputation for SAT Math batch 17. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    return pick(ch, F(0 - (-1), 6 - 2))


def c02(_):
    pairs = [(a, b) for a in range(-20, 21) for b in range(a, 21) if a * b == 12 and (1 - a) * (1 - b) == 6]
    assert pairs
    return pairs[0][0] + pairs[0][1]


def c03(ch):
    for x in (0, 1, -3, 7):
        assert (x + 5) * (x - 5) + 25 == x * x
    return by_text(ch, "x²")


def c04(ch):
    g = lambda x: (x + 3) ** 2 - 4 * (x + 3) + 7
    xm = min(range(-50, 51), key=g)
    return by_text(ch, f"Minimum {g(xm)} at x = {'−' if xm < 0 else ''}{abs(xm)}")


def c05(ch):
    return by_text(ch, "It would be smaller than 5 percentage points.")


def c06(ch):
    return pick(ch, 14 - F(200, 32))


def c07(_):
    k = 12  # 3k - 2k
    return 2 * k


def c08(ch):
    return by_text(ch, f"{115 - 48}°")


def c09(_):
    sphere = F(4, 3) * 3 ** 3
    cyl = F(3 ** 2 * 4)
    return sphere / cyl


CHECKS = {f'Q017-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09], 1)}
