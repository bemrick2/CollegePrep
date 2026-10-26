"""Scripted recomputation for ACT Math batch 24. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def _ratfn(t):
    e = t.replace('−', '-')
    e = re.sub(r'(\d)x', r'\1*x', e)
    return lambda x: eval(e, {'__builtins__': {}}, {'x': x})  # noqa: S307 (author-written choice text)


def c01(ch):
    f = lambda x: (2 * x + 1) / (x - 3)
    xs = [F(n) for n in (4, 5, 7, -1, 10)]
    ys = tuple(f(x) for x in xs)  # an inverse must send f(x) back to x
    return pick(ch, tuple(xs), conv=lambda t: tuple(_ratfn(t)(y) for y in ys))


def c02(ch):
    n = next(n for n in range(-100, 101, 2) if n + (n + 2) + (n + 4) == 2 * (n + 4) + 8)
    return pick(ch, n)


def c03(ch):
    return pick(ch, 10 * math.sin(math.radians(45)) / math.sin(math.radians(30)))


def c04(ch):
    v = lambda r, h: math.pi * r * r * h
    return pick(ch, v(1 / 2, 2) / v(1, 1))


def c05(ch):
    phi = lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2)))
    exact = (phi((86 - 70) / 8) - phi((62 - 70) / 8)) * 100  # about 81.9 exactly; empirical rule gives 81.5
    vals = {k: float(v.rstrip('%')) for k, v in ch.items()}
    best = min(vals, key=lambda k: abs(vals[k] - exact))
    assert abs(vals[best] - 81.5) < 1e-9
    return best


def c06(ch):
    lo, hi = 52 - 3, 52 + 3
    want = 'below half plausible' if lo < 50 else None
    return pick(ch, want, conv=lambda t: 'below half plausible' if ('plausible' in t and 'fewer than half' in t) else t)


def c07(ch):
    a, b, c, d = 3, -2, 4, 1
    return pick(ch, a * d - b * c)


def c08(ch):
    return pick(ch, abs(250 - 200) / 200 * 100)


def c09(ch):
    best = max(2 * m + 9 * c for m in range(0, 200) for c in range(0, 20) if 5 * m + 40 * c <= 480 and m >= 30)
    return pick(ch, best)


def c10(ch):
    return pick(ch, 225 * math.pi / 180, conv=lambda t: float(F(t.replace('π', '').split('/')[0] or 1) / F(t.split('/')[1])) * math.pi)


CHECKS = {f'B024-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
