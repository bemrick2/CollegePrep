"""Scripted recomputation for ACT Math batch 4. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F
from itertools import permutations

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402


def expr(t):  # '10 − √5', '36π − 72', '144 − 36π', '√61', '17'
    s = t.replace('−', '-').replace(' ', '')
    s = re.sub(r'√(\d+)', r'math.sqrt(\1)', s)
    s = re.sub(r'(\d+)π', r'(\1*math.pi)', s)
    s = s.replace('π', 'math.pi')
    return eval(s, {'math': math})  # noqa: S307 - our own fixed choice strings


def c01(ch):
    u, v = (3, -4), (-1, 2)
    w = (2 * u[0] - v[0], 2 * u[1] - v[1])
    return pick(ch, math.hypot(*w), conv=expr)


def c02(ch):
    sols = [F(n, 2) for n in range(-200, 201) if (F(n, 2) - 4) / 3 == (F(n, 2) + 2) / 5]
    return pick(ch, sols[0])


def c03(ch):
    sols = sorted(x for x in range(-50, 51) if 2 * x + 7 >= 0 and abs(math.sqrt(2 * x + 7) - (x + 2)) < 1e-12)
    target = '{' + ', '.join(str(s).replace('-', '−') for s in sols) + '}'
    return pick(ch, target, conv=lambda t: t.strip())


def c04(ch):
    bad = [k for k, v in ch.items() if num(v) - 3 < 0]
    assert len(bad) == 1
    return bad[0]


def c05(ch):
    y = lambda x: 3 * math.sin(4 * x) + 1
    # smallest p > 0.01 with y(x + p) == y(x) at several sample x, scanned on a 1e-5 grid
    period = next(p for p in (i / 100000 for i in range(1000, 700000))
                  if all(abs(y(x + p) - y(x)) < 1e-3 for x in (0.1, 0.37, 1.3)))
    return pick(ch, period, conv=expr, tol=1e-3)


def c06(ch):
    m = -1 / F(3, 4)
    b = 2 - m * 1
    def pt(t):
        a, c = t.strip('() ').split(',')
        return F(c.strip().replace('−', '-'))
    return pick(ch, b, conv=pt)


def c07(ch):
    r = 6
    side = 2 * r / math.sqrt(2)
    return pick(ch, math.pi * r * r - side * side, conv=expr)


def c08(ch):
    n = sum(1 for p in permutations(range(10), 4) if p[0] % 2 == 1 and p[3] % 2 == 0)
    return pick(ch, n)


def c09(ch):
    return pick(ch, round(4.2 * 20 / 1.5, 1))


def c10(ch):
    sa = 2 * math.pi * 16 + 2 * math.pi * 4 * 9
    return pick(ch, math.ceil(sa / 40))


CHECKS = {f'B004-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
