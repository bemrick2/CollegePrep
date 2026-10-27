"""Scripted recomputation for ACT Math batch 70. Each check derives the answer from the stem's numbers only."""
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
    a, b = math.isqrt(16), math.isqrt(9)
    return by_text(ch, f"y = ±({F(b, a)})x")


def c02(ch):
    r = F(40, 60) * 2
    assert r == F(4, 3)
    return by_text(ch, "4π/3")


def c03(ch):
    g = lambda x: 2 * x + 5 if x <= -1 else -x
    return pick(ch, g(-1) + g(4))


def c04(ch):
    c = math.degrees(math.acos((3 ** 2 + 5 ** 2 - 7 ** 2) / (2 * 3 * 5)))
    return by_text(ch, f"{round(c)}°")


def c05(ch):
    f = lambda x: (x - 1) ** 2 * (x + 3)
    crossings = sum(1 for z in (1, -3) if f(z - 0.01) * f(z + 0.01) < 0)
    return pick(ch, crossings)


def c06(ch):
    sols = [x for x in range(-20, 21) if x > 0 and x - 2 > 0 and math.isclose(math.log2(x) + math.log2(x - 2), 3)]
    assert sols == [4]
    return by_text(ch, "{4}")


def c07(ch):
    pts = [(x, x + 7) for x in range(-10, 11) if x ** 2 + (x + 7) ** 2 == 25]
    assert len(pts) == 2
    d = math.dist(*pts)
    assert math.isclose(d, math.sqrt(2))
    return by_text(ch, "√2")


def c08(ch):
    return pick(ch, min(5 - 2 * math.cos(3 * x / 1000) for x in range(0, 10000)).__round__())


def c09(ch):
    a, b, c = 3, -12, 7
    r = math.sqrt(b * b - 4 * a * c)
    return pick(ch, round((-b + r) / (2 * a) + (-b - r) / (2 * a), 9))


def c10(ch):
    xs = list(range(10))
    ys = [20 - 2 * x + (0.3 if x % 2 else -0.3) for x in xs]
    mx, my = sum(xs) / 10, sum(ys) / 10
    r = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / math.sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))
    return min(ch, key=lambda k: abs(float(ch[k].replace('−', '-')) - r))


CHECKS = {f'B070-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
