"""Scripted recomputation for ACT Math batch 22. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    return pick(ch, sum(1 for x in range(1, 100) if x + 7 > 12 and x + 12 > 7 and 7 + 12 > x))


def c02(ch):
    s = 4
    return pick(ch, 6 * math.sqrt(3) / 4 * s * s)


def _set_from_text(t):
    """Turn a choice describing a set of reals into a predicate."""
    t = t.replace('−', '-')
    parts = [p.strip() for p in re.split(r'\bor\b', t)]
    preds = []
    for p in parts:
        excl = [float(m) for m in re.findall(r'x ≠ (-?\d+)', p)]
        p2 = re.sub(r'and x ≠ -?\d+', '', p).strip()
        m = re.fullmatch(r'(-?\d+) < x < (-?\d+)', p2)
        if m:
            a, b = float(m.group(1)), float(m.group(2))
            preds.append(lambda x, a=a, b=b, e=excl: a < x < b and x not in e)
            continue
        m = re.fullmatch(r'x < (-?\d+)', p2)
        if m:
            b = float(m.group(1))
            preds.append(lambda x, b=b, e=excl: x < b and x not in e)
            continue
        m = re.fullmatch(r'x > (-?\d+)', p2)
        b = float(m.group(1))
        preds.append(lambda x, b=b, e=excl: x > b and x not in e)
    return lambda x: any(f(x) for f in preds)


def c03(ch):
    xs = [n / 4 for n in range(-60, 61)]
    truth = tuple((x + 2) ** 2 * (x - 3) < 0 for x in xs)
    return pick(ch, truth, conv=lambda t: tuple(_set_from_text(t)(x) for x in xs))


def c04(ch):
    def paths(a, b):  # right/up lattice paths between points
        dx, dy = b[0] - a[0], b[1] - a[1]
        return math.comb(dx + dy, dy)
    return pick(ch, paths((0, 0), (2, 1)) * paths((2, 1), (4, 3)))


def c05(ch):
    return pick(ch, math.sqrt(72) + math.sqrt(50), tol=1e-9)


def c06(ch):
    d = 24
    return pick(ch, 2 * d / (d / 12 + d / 8))


def c07(ch):
    k = 9 * 2 ** 2
    return pick(ch, k / 3 ** 2)


def c08(ch):
    sols = [(x, y, z) for x in range(-50, 51) for y in range(-50, 51) for z in [14 - y] if x + y == 10 and x + z == 12]
    return pick(ch, sols[0][0])


def c09(ch):
    f = lambda x: (6 * x * x - 1) / (2 * x * x + 5 * x)
    return pick(ch, round(f(1e9), 6), conv=lambda t: float(F(t.replace('y = ', '').replace('−', '-'))))


def c10(ch):
    return pick(ch, 0.35 * 240)


CHECKS = {f'B022-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
