"""Scripted recomputation for ACT Math batch 23. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def _expr(t):
    """Turn a choice like '2a + 4' or 'a² + 5a + 4' into a function of a."""
    e = t.replace('−', '-').replace('²', '**2')
    e = re.sub(r'(\d)a', r'\1*a', e)
    return lambda a: eval(e, {'__builtins__': {}}, {'a': a})  # noqa: S307 (author-written choice text)


def c01(ch):
    f = lambda x: x * x + 3 * x
    pts = (-3, 0, 1, 2, 7)
    return pick(ch, tuple(f(a + 1) - f(a) for a in pts), conv=lambda t: tuple(_expr(t)(a) for a in pts))


def _ineq(t):
    e = t.replace('−', '-').replace('≤', '<=').replace('≥', '>=')
    e = re.sub(r'\|([^|]*)\|', r'abs(\1)', e)
    e = re.sub(r'(\d+(?:\.\d+)?)', r"F('\1')", e)  # exact decimals so boundary values compare exactly
    return lambda L: eval(e, {'__builtins__': {}, 'abs': abs, 'F': F}, {'L': L})  # noqa: S307


def c02(ch):
    xs = [F(n, 1000) for n in range(4400, 4601, 5)]
    truth = tuple(abs(L - F(45, 10)) <= F(3, 100) for L in xs)
    return pick(ch, truth, conv=lambda t: tuple(_ineq(t)(L) for L in xs))


def c03(ch):
    side, d1 = 13, 24
    d2 = 2 * math.sqrt(side ** 2 - (d1 / 2) ** 2)
    return pick(ch, d1 * d2 / 2)


def c04(ch):
    A, B, t = (F(-2), F(1)), (F(10), F(9)), F(1, 4)
    p = (A[0] + t * (B[0] - A[0]), A[1] + t * (B[1] - A[1]))
    conv = lambda s: tuple(F(v.strip().replace('−', '-')) for v in s.strip('()').split(','))
    return pick(ch, p, conv=conv)


def c05(ch):
    r = -0.9
    want = 'lower' if r < -0.5 else None  # strong negative association, no causal claim
    return pick(ch, want, conv=lambda t: 'lower' if ('tended' in t and 'lower' in t) else t)


def c06(ch):
    return pick(ch, F(5, 6) ** 2 * F(1, 6))


def c07(ch):
    return pick(ch, (F(1, 2) + F(1, 3)) / (F(1, 2) - F(1, 3)))


def c08(ch):
    g = math.gcd(84, 126)
    return pick(ch, 84 // g + 126 // g)


def c09(ch):
    return pick(ch, F(50 - 40, 50) * 100, conv=lambda t: F(t.replace('%', '')))


def c10(ch):
    dep = 22 * 60 + 40
    land = (dep + 7 * 60 + 35 - 3 * 60) % (24 * 60)

    def conv(t):
        m = re.fullmatch(r'(\d+):(\d+) ([ap])\.m\.', t)
        h = int(m.group(1)) % 12 + (12 if m.group(3) == 'p' else 0)
        return h * 60 + int(m.group(2))
    return pick(ch, land, conv=conv)


CHECKS = {f'B023-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
