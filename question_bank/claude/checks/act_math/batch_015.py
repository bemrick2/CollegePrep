"""Scripted recomputation for ACT Math batch 15. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402

SUP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻', '0123456789-')


def c01(ch):
    rate = F(3, 3 * 3)
    return pick(ch, rate * 6 * 6)


def c02(ch):
    b = 40 * 36 / 24
    c = b
    d = c * 30 / 15
    return pick(ch, d)


def c03(ch):
    return pick(ch, round(60 + 0.08 * 60 + 0.20 * 60, 2), conv=lambda t: float(t.strip('$')))


def c04(ch):
    students, others = 400, 600
    users_s, users_o = 0.25 * students, 0.10 * others
    return pick(ch, round(100 * users_s / (users_s + users_o), 1), conv=lambda t: float(t.rstrip('%')))


def sci(t):
    m = re.fullmatch(r'([\d.]+) × 10(.+)', t.strip())
    return float(m.group(1)) * 10 ** int(m.group(2).translate(SUP))


def c05(ch):
    return pick(ch, 3.0e5 * 3600, conv=sci, tol=1e-9)


def c06(ch):
    grid = [k / 4 for k in range(-40, 41)]
    def two_distinct(k):
        if k == 0:
            return False
        return 16 - 4 * k > 0
    good = frozenset(k for k in grid if two_distinct(k))
    def region(t):
        if t == 'k < 4 and k ≠ 0':
            return frozenset(k for k in grid if k < 4 and k != 0)
        m = re.fullmatch(r'k (<|>|≤) (\d+)', t)
        op, v = m.group(1), float(m.group(2))
        return frozenset(k for k in grid if (k < v if op == '<' else k > v if op == '>' else k <= v))
    return pick(ch, good, conv=region)


def c07(ch):
    return pick(ch, sum(1 for x in range(1, 11) if 2 ** x >= 4 * x))


def c08(ch):
    funcs = {}
    for k, v in ch.items():
        e = v.split('=')[1].replace('−', '-').replace('x³', 'x**3').replace('x²', 'x**2').replace('|x|', 'abs(x)')
        funcs[k] = lambda x, e=e: eval(e, {'x': x, 'abs': abs})  # noqa: S307
    hits = [k for k, f in funcs.items() if all(abs(f(-x) + f(x)) < 1e-12 for x in (0.5, 1, 2, 3.7))]
    assert len(hits) == 1, hits
    return hits[0]


def c09(ch):
    return pick(ch, math.sqrt(3 * 3 + 4 * 4 + 12 * 12))


def frac_expr(t):
    s = t.replace('√30', str(math.sqrt(30)))
    a, b = s.split('/')
    return float(a) / float(b)


def c10(ch):  # Monte Carlo cross-checked with exact length
    n = 1000000
    exact = sum(1 for i in range(n) if ((i + .5) * 10 / n) ** 2 < 30) / n
    return pick(ch, exact, conv=frac_expr, tol=1e-4)


CHECKS = {f'B015-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
