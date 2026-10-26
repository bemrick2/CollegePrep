"""Scripted recomputation for ACT Math batch 28. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def money(t):
    return F(t.replace('$', ''))


def c01(ch):
    return pick(ch, F(12, 8) * 10)


def c02(ch):
    start = next(F(n) for n in range(1, 1000) if F(n) * F(2, 3) * F(3, 4) == 30)
    return pick(ch, start, conv=money)


def _quad(t):
    m = re.fullmatch(r'x² ([+−]) (\d+)x ([+−]) (\d+) = 0', t)
    b = int(m.group(2)) * (-1 if m.group(1) == '−' else 1)
    c = int(m.group(4)) * (-1 if m.group(3) == '−' else 1)
    return (-b, c)  # (sum of roots, product of roots)


def c03(ch):
    return pick(ch, (7, 10), conv=_quad)


def c04(ch):
    x = next(F(n, 2) for n in range(-200, 200) if 3 * F(n, 2) + 10 == 5 * F(n, 2) - 30)
    return pick(ch, 3 * x + 10, conv=lambda t: F(t.rstrip('°')))


def c05(ch):
    xi, yi = F(24, 3), F(24, 4)
    return pick(ch, xi * yi / 2)


def c06(ch):
    return pick(ch, 'at or below', conv=lambda t: 'at or below' if 'at or below' in t else t)


def c07(ch):
    n = next(n for n in range(1, 500) if 80 * n + 70 * 20 == 76 * (n + 20))
    return pick(ch, n)


def c08(ch):
    n = next(n for n in range(1, 2000) if math.gcd(36, n) == 6 and 36 * n // math.gcd(36, n) == 180)
    return pick(ch, n)


def c09(ch):
    w, h = 12, 15
    return pick(ch, sum(1 for x in range(w) for y in range(h) if 0 < x < w - 1 and 0 < y < h - 1))


def c10(ch):
    xs = [F(n, 2) for n in range(-40, 41) if abs(F(n, 2) - 2) - 3 == 0]
    return pick(ch, max(xs) - min(xs))


CHECKS = {f'B028-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
