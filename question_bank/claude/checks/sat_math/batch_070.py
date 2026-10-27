"""Scripted recomputation for SAT Math batch 70. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
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
    sums = set()
    for a in (F(2), F(-3), F(7, 2), F(10)):
        b = 9 - a
        assert a != b
        r = (a - b) / (a - b)
        sums.add(r + a * r + b)
    assert sums == {10}
    return F(10)


def c02(_):
    bs = [b for b in range(1, 16) for a in range(1, 16) if 4 * a + 6 * b == 60]
    return F(len(set(bs)))


def c03(ch):
    assert 2 * F('11.40') != F('21.60')
    return [k for k, v in ch.items() if v.startswith('No pair of prices')][0]


def c04(_):
    def ok(m):
        return all((3 - m) * x - 8 > 0 for x in [4 + F(1, 10**k) for k in range(1, 8)] + [5, 10, 1000])
    ms = [F(n, 100) for n in range(-300, 301) if ok(F(n, 100))]
    return max(ms)


def c05(ch):
    x = (F('5.4') - F(3)) / F('0.75')
    return pick(ch, round(float(x), 1))


def c06(ch):
    assert F(48) / F('0.75') == 64
    return [k for k, v in ch.items() if v.startswith('The number of miles of driving')][0]


def c07(_):
    return F(2300) - F('0.8') * (2300 - 500)


def c08(ch):
    true = lambda n: F(5) + F('0.4') * (n - 1)
    forms = {'0.40n + 5.00': lambda n: F('0.4') * n + 5, '5.00n': lambda n: 5 * n,
             '4.60n + 0.40': lambda n: F('4.6') * n + F('0.4'), '0.40n + 4.60': lambda n: F('0.4') * n + F('4.6')}
    ok = [t for t, fn in forms.items() if all(fn(n) == true(n) for n in (1, 2, 7))]
    assert len(ok) == 1
    return by_text(ch, ok[0])


def c09(_):
    pts = [(x, F(12 - 2 * x, 3)) for x in range(1, 7) if (12 - 2 * x) % 3 == 0 and 12 - 2 * x > 0]
    assert pts == [(3, 2)]
    return F(2, 3)


def c10(ch):
    lo, hi = F(1500 - 800, 40), F(1500 - 400, 40)
    return by_text(ch, f"{float(lo):g} ≤ t ≤ {float(hi):g}")


def c11(ch):
    return [k for k, v in ch.items() if v.startswith('The y-intercept increases from 20 to 25')][0] if (F(300, 6), F(300, 12)) == (50, 25) else None


def c12(_):
    n = 1
    while F(45 + F('5.5') * n, n) > 9:
        n += 1
    return F(n)


def c13(_):
    return (F('56.16') - F('54.27')) / F('1.75') * 100 - 100


def c14(ch):
    t_a = F(100) / F('0.8')
    return pick(ch, F(100) / (F('1.25') * t_a))


def c15(ch):
    slope = F(-20) / F('0.5')
    b = 400 - slope * 3
    return by_text(ch, f"n = {int(b)} − {int(-slope)}p")


def c16(ch):
    a = F(12) / F('0.3')
    assert 208 - F('0.7') * (a + 1) > 220 - (a + 1)
    return by_text(ch, f"a > {int(a)}")


CHECKS = {f'Q070-{i:02d}': f for i, f in enumerate(
    [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16], 1)}
