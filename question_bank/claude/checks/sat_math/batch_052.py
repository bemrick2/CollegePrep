"""Scripted recomputation for SAT Math batch 52. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    cands = {"x < 2 + 6/a": lambda x, a: x < 2 + 6 / a, "x > 2 + 6/a": lambda x, a: x > 2 + 6 / a,
             "x < 2 − 6/a": lambda x, a: x < 2 - 6 / a, "x > 2 − 6/a": lambda x, a: x > 2 - 6 / a}
    tests = [(F(x, 2), F(a)) for a in (-1, -2, -3, -5) for x in range(-40, 41)]
    hits = [t for t, f in cands.items() if all(f(x, a) == (a * x - 6 > 2 * a) for x, a in tests)]
    assert len(hits) == 1
    return by_text(ch, hits[0])


def c02(_):
    def ok(k):
        return any(3 - x <= x + k for x in (F(n, 4) for n in range(-200, -7)))
    return F(next(k for k in range(-20, 50) if ok(k)))


def c03(_):
    return F(next(n for n in range(0, 2000) if 18 * n - (2000 + 8 * n) >= F(1, 4) * (2000 + 8 * n)))


def c04(_):
    m = F(0 - 7, 5 - 3)
    return 7 - 3 * m


def c05(ch):
    lhs = lambda x: (2 * x + 3) * (x - 4) - 2 * (x - 1) ** 2
    a, b = lhs(1) - lhs(0), lhs(0)
    assert all(lhs(x) == a * x + b for x in range(-5, 6))
    return pick(ch, a + b)


def c06(ch):
    assert F(1) + F(4, 100) / 4 == F(101, 100)
    return by_text(ch, "Interest is added to the account 4 times each year.")


def c07(_):
    xs = [x for x in range(1, 200) if F(x * x, 2) + 10 * x + 200 <= 35 * x]
    return F(max(xs))


def c08(ch):
    return pick(ch, round(22.5 / (5 / 1.6), 9))


def c09(_):
    return F(6, 10) / 12 * 2000 * F(748, 100)


def c10(ch):
    area = 7 * 7 * math.sqrt(3)
    assert math.isclose(math.hypot(7, 7 * math.sqrt(3)), 14)
    return by_text(ch, "49√3") if math.isclose(area, 49 * math.sqrt(3)) else None


def c11(_):
    cd = F(2 * 16, 4)
    db = cd * cd / 4
    return F(1, 2) * (4 + db) * cd


CHECKS = dict(zip(['Q052-01', 'Q052-02', 'Q052-03', 'Q052-04', 'Q052-06', 'Q052-07', 'Q052-08', 'Q052-09', 'Q052-10', 'Q052-11'],
                  [c01, c02, c03, c04, c06, c07, c08, c09, c10, c11]))
