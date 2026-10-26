"""Scripted recomputation for ACT Math batch 10. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):  # rational iff value equals a fraction with small denominator (checked exactly where possible)
    vals = {'A': math.sqrt(9 / 4), 'B': F(12, 99), 'C': math.sqrt(8) * math.sqrt(2), 'D': math.sqrt(2) + math.sqrt(8)}
    assert set(vals) == set(ch)
    irr = [k for k, v in vals.items() if abs(float(v) - float(F(float(v)).limit_denominator(1000))) > 1e-9]
    assert len(irr) == 1, irr
    return irr[0]


def c02(ch):
    b = F(20)
    a, c = F(3, 4) * b, b / F(2, 5)
    return pick(ch, (a + c) / c)


def c03(ch):
    sols = [(x, y) for x in range(-50, 51) for y in range(-50, 51) if x + y == 7 and x * x - y * y == 21]
    assert len(sols) == 1
    return pick(ch, sols[0][0])


def c04(ch):
    best = max(x / 100 * (120 - 2 * x / 100) for x in range(1, 6000))
    return pick(ch, round(best, 6))


def c05(ch):
    sols = [F(n, 3) for n in range(-300, 300) if 5 - 3 * F(n, 3) == 20]
    return pick(ch, sols[0])


def expr(t):
    s = t.replace('−', '-')
    s = re.sub(r'(\d+)√(\d+)', r'\1*math.sqrt(\2)', s)
    s = re.sub(r'√(\d+)', r'math.sqrt(\1)', s)
    return eval(s, {'math': math})  # noqa: S307


def c06(ch):  # brute-force P along the x-axis
    A, B = (1, 3), (7, 5)
    best = min(math.hypot(x / 1000 - A[0], A[1]) + math.hypot(x / 1000 - B[0], B[1]) for x in range(-5000, 15000))
    return pick(ch, best, conv=expr, tol=1e-6)


def c07(ch):
    r = 10 * math.pi / (2 * math.pi)
    return pick(ch, math.pi * r * r, conv=lambda t: float(t.rstrip('π') or 1) * math.pi, tol=1e-9)


def c08(ch):
    return pick(ch, (20 * 80 + 30 * 70) / 50)


def c09(ch):  # simulate hour by hour (fractional steps)
    done, t, step = F(0), F(0), F(1, 100)
    while done < 60:
        workers = 6 if t < 4 else 9
        done += workers * step
        t += step
    def mixed(s):
        m = re.fullmatch(r'(\d+) (\d+)/(\d+)', s)
        return F(int(m.group(1))) + F(int(m.group(2)), int(m.group(3))) if m else F(s)
    return pick(ch, t, conv=mixed)


def c10(ch):
    def val(t):
        if t.endswith('%'):
            return F(t[:-1]) / 100
        return F(t)
    vals = {k: val(v) for k, v in ch.items()}
    best = max(vals.values())
    hits = [k for k, v in vals.items() if v == best]
    assert len(hits) == 1
    return hits[0]


CHECKS = {f'B010-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
