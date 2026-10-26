"""Scripted recomputation for ACT Math batch 29. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def _lin(t):
    m = re.fullmatch(r'(\d+)x ([+−]) (\d+)', t)
    return (int(m.group(1)), int(m.group(3)) * (-1 if m.group(2) == '−' else 1))


def c01(ch):
    pts = (-2, 0, 1, 5)
    target = tuple(x * (x - 3) + 4 * (x - 3) for x in pts)

    def conv(t):
        e = t.replace('−', '-').replace('²', '**2').replace(')(', ')*(')
        e = re.sub(r'(\d)(x|\()', r'\1*\2', e)
        return tuple(eval(e, {'__builtins__': {}}, {'x': x}) for x in pts)  # noqa: S307 (author-written choice text)
    return pick(ch, target, conv=conv)


def c02(ch):
    return pick(ch, sum(1 for x in range(-100, 101) if x * x - x - 12 < 0))


def c03(ch):
    f = lambda x: math.sqrt(x - 3) + 2
    lo = min(f(3 + k / 10) for k in range(0, 1000))
    return pick(ch, lo, conv=lambda t: float(re.search(r'y ≥ (\d+)', t).group(1)) if '≥' in t else None)


def c04(ch):
    s = math.sqrt(2 * 18)
    return pick(ch, s * math.sqrt(2))


def c05(ch):
    (x1, y1), (x2, y2) = (1, 2), (7, 6)
    mx, my = F(x1 + x2, 2), F(y1 + y2, 2)
    m = -1 / F(y2 - y1, x2 - x1)
    return pick(ch, my - m * mx)


def c06(ch):
    deck = [(r, s) for r in range(1, 14) for s in 'HDCS']
    hits = [c for c in deck if c[1] == 'H' or c[0] in (11, 12, 13)]
    return pick(ch, F(len(hits), 52))


def c07(ch):
    return pick(ch, F(50) / F(5, 40))


def c08(ch):
    return pick(ch, F(2 ** 7 * 4 ** 3, 8 ** 3))


def c09(ch):
    return pick(ch, F(6) * F(10, 4))


def c10(ch):
    n = 200000
    xs = [2 * math.pi * k / n for k in range(n)]
    g = [math.sin(2 * x) - 0.5 for x in xs]
    crossings = sum(1 for i in range(n - 1) if g[i] == 0 or (g[i] < 0) != (g[i + 1] < 0))
    return pick(ch, crossings)


CHECKS = {f'B029-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
