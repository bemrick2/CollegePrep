"""Scripted recomputation for ACT Math batch 71. Each check derives the answer from the stem's numbers only."""
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
    a2, b2 = 25, 16  # 25 is under y², so the major axis is vertical
    c = math.isqrt(a2 - b2)
    assert c * c == a2 - b2
    return by_text(ch, f"(0, ±{c})")


def c02(ch):
    th = math.atan(2)
    assert math.isclose(math.cos(th), math.sqrt(5) / 5)
    return by_text(ch, "√5/5")


def c03(ch):
    for start in range(-100, 100):
        xs = list(range(start, start + 15))
        if F(sum(xs), 15) == 40:
            return pick(ch, max(xs))


def c04(ch):
    return pick(ch, F(5 - (-3), (4 - 2) ** 2))


def c05(ch):
    n = 600
    step = 6 / n
    inside = sum(1 for i in range(n) for j in range(n)
                 if abs(-3 + (i + 0.5) * step) + abs(-3 + (j + 0.5) * step) <= 3)
    return pick(ch, round(inside * step * step))


def c06(ch):
    for t in (0.3, 1.1, 2.0):
        assert math.isclose((1 - math.cos(t) ** 2) / math.sin(t), math.sin(t))
    return by_text(ch, "sin θ")


def c07(ch):
    s = 1
    hexa = 6 * math.sqrt(3) / 4 * s ** 2
    tri = math.sqrt(3) / 4 * (6 * s / 3) ** 2
    r = F(hexa / tri).limit_denominator(10)
    return by_text(ch, f"{r.numerator}:{r.denominator}")


def c08(ch):
    coeffs, out = [1, -2, -5, 6], []
    acc = 0
    for a in coeffs:
        acc = acc * 3 + a
        out.append(acc)
    assert out[-1] == 0 and out[:-1] == [1, 1, -2]
    return by_text(ch, "x² + x − 2")


def c09(ch):
    cx, cy = (2 + 6) / 2, (0 + 4) / 2
    return pick(ch, F(int(cy), int(cx)))


def c10(ch):
    return pick(ch, round(60 / math.tan(math.radians(30))))


CHECKS = {f'B071-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
