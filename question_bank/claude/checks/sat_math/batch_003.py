"""Scripted recomputation for SAT Math batch 3. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    cs = [7 * a + 3 * b for a in range(1, 16) for b in range(1, 16) if a * b == 15 and a + b == 8]
    return max(cs)


def c02(_):
    # (x + 4)² + (y − 3)² = k + 16 + 9
    return 6 ** 2 - 16 - 9


def c03(ch):
    k = F(26, 13)
    return pick(ch, 5 * k)


def c04(ch):
    sols = [v for v in (-6, -4, 0, 4) if 3 - 2 * v > 11]
    assert sols == [-6]
    return pick(ch, sols[0])


def c05(ch):
    x = F(21, 3)
    return pick(ch, 6 * x - 10)


def c06(ch):
    ok = [(r, b) for r, b in [(10, 20), (12, 15), (15, 12), (20, 15)] if 110 * r + 40 * b >= 2000 and r + b <= 30]
    assert ok == [(15, 12)]
    return by_text(ch, "(15, 12)")


def c07(ch):
    for x in range(-5, 6):
        assert 2 * x * x - 12 * x + 7 == 2 * (x - 3) ** 2 - 11
    return by_text(ch, "2(x − 3)² − 11")


def c08(ch):
    P = lambda t: 8000 * 1.05 ** (t / 2)
    assert math.isclose(P(4) / P(2), 1.05)
    return by_text(ch, "It increases by 5% every 2 years.")


def c09(ch):
    return pick(ch, F(18, 10) * 15 + 12)


def c10(_):
    x = F(20 - 4, 4 - 2)
    assert x not in (2, 5) and F(4) / (x - 2) == F(2) / (x - 5)
    return x


CHECKS = {f'Q003-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
