"""Scripted recomputation for SAT Math batch 46. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    inc = 8 * F(3, 2)
    return pick(ch, float(inc / F(3, 10)))


def c02(_):
    monthly = F(10 * 35 - 230, 10 - 4)
    return 230 - 4 * monthly


def c03(ch):
    q = next(q for q in range(1, 500) if F(1, 3 * q) + F(1, q) == F(1, 12))
    return pick(ch, q)


def c04(ch):
    cands = {'A = C²/(4π)': lambda c: c * c / (4 * math.pi), 'A = C²/(4π²)': lambda c: c * c / (4 * math.pi ** 2),
             'A = C²/(2π)': lambda c: c * c / (2 * math.pi), 'A = C²/π': lambda c: c * c / math.pi}
    hits = [t for t, f in cands.items() if all(math.isclose(f(2 * math.pi * r), math.pi * r * r) for r in (1, 2.5, 7))]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c05(ch):
    peaks = [12 * F(3, 4) ** n for n in range(1, 6)]
    cands = {'h(n) = 12 − 3n': lambda n: 12 - 3 * n, 'h(n) = 12(0.25)ⁿ': lambda n: 12 * F(1, 4) ** n,
             'h(n) = 12(0.75)ⁿ⁻¹': lambda n: 12 * F(3, 4) ** (n - 1), 'h(n) = 12(0.75)ⁿ': lambda n: 12 * F(3, 4) ** n}
    hits = [t for t, f in cands.items() if all(f(n) == peaks[n - 1] for n in range(1, 6))]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c06(_):
    p = lambda x: (x - 1) * (x - 2) * (x - 3) + 5
    assert p(1) == p(2) == p(3) == 5
    return F(p(4))


def c07(ch):
    c = next(c for c in range(0, 361) if F(9, 100) * c + F(6, 100) * (360 - c) == F(252, 10))
    return pick(ch, c)


def c08(ch):
    both = F(45, 100) * 40
    return pick(ch, float(both / 150 * 6000))


def c09(ch):
    return pick(ch, 360 - 90 - 90 - 50, conv=lambda t: float(t.rstrip('°')))


def c10(ch):
    r = F(1, 2) * F(2, 5)
    return by_text(ch, f"{r.numerator}/{r.denominator}")


CHECKS = {f'Q046-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
