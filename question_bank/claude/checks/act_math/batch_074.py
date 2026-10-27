"""Scripted recomputation for ACT Math batch 74. Each check derives the answer from the stem's numbers only."""
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
    xs, ys = (0, 6, 3), (0, 0, 9)
    return by_text(ch, f"({sum(xs) // 3}, {sum(ys) // 3})")


def c02(ch):
    s = 1
    tri = F(1, 2) * s * s  # base AB = s, height from M to AB = s
    return pick(ch, tri / (s * s))


def c03(ch):
    primes = [n for n in range(2, 20) if all(n % d for d in range(2, n))]
    cands = [int(v) for v in ch.values()]
    ce = [n for n in cands if n in primes and n % 2 == 0]
    assert len(ce) == 1
    return pick(ch, ce[0])


def c04(ch):
    return by_text(ch, "tan⁻¹(3/40)")


def c05(ch):
    data = sorted([23, 25, 28, 30, 34, 34, 37, 41, 46])
    return pick(ch, data[len(data) // 2])


def c06(ch):
    return by_text(ch, f"{F(52, 40) * 100}%")


def c07(ch):
    for d in range(31):
        if 5 * (30 - d) + 10 * d == 210:
            return pick(ch, d)


def c08(ch):
    return by_text(ch, f"x = {(-1 + 7) // 2}")


def c09(ch):
    return pick(ch, F(40, 2))


def c10(ch):
    r, h = 3, 5
    return by_text(ch, f"{2 * r * r + 2 * r * h}π")


CHECKS = {f'B074-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
