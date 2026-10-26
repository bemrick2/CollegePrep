"""Scripted recomputation for ACT Math batch 14. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F
from itertools import permutations

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    ndiv = lambda n: sum(1 for d in range(1, n + 1) if n % d == 0)
    return pick(ch, sum(1 for n in range(1, 201) if ndiv(n) % 2 == 1))


def c02(ch):
    good = 0
    for c in range(-50, 51):
        if (10 + c) % 2 == 0:
            x, y = (10 + c) // 2, (10 - c) // 2
            if x > 0 and y > 0:
                good += 1
    return pick(ch, good)


def c03(ch):
    sols = [c for c in range(-100, 101) if F(9, 5) * c + 32 == c]
    return pick(ch, sols[0], conv=lambda t: float(t.replace('−', '-').rstrip('°')))


def c04(ch):
    for a in range(-20, 21):
        for b in range(-20, 21):
            c = 3
            if a + b + c == 0 and a - b + c == 10:
                return pick(ch, 4 * a + 2 * b + c)
    raise ValueError


def c05(ch):
    grid = [i / 100 for i in range(-400, 401)]
    ok = frozenset(x for x in grid if 5 - x * x - 1 >= -1e-12)
    def region(t):
        s = t.replace('−', '-').replace('√5', str(math.sqrt(5)))
        m = re.fullmatch(r'(-?[\d.]+) ≤ x ≤ (-?[\d.]+)', s)
        if m:
            return frozenset(x for x in grid if float(m.group(1)) - 1e-12 <= x <= float(m.group(2)) + 1e-12)
        m = re.fullmatch(r'x ≥ (-?[\d.]+)', s)
        if m:
            return frozenset(x for x in grid if x >= float(m.group(1)))
        m = re.fullmatch(r'x ≤ (-?[\d.]+)', s)
        return frozenset(x for x in grid if x <= float(m.group(1)))
    return pick(ch, ok, conv=region)


def c06(ch):  # largest circle inside the triangle (0,0),(6,0),(0,8): search center on y = x line (equidistant from legs)
    best = 0
    for i in range(1, 4000):
        r = i / 1000
        # center (r, r); distance to hypotenuse 8x + 6y = 48
        d = abs(8 * r + 6 * r - 48) / 10
        if d >= r - 1e-12 and 8 * r + 6 * r < 48:
            best = r
    return pick(ch, round(best, 3), tol=1e-3)


def c07(ch):
    rs = [r / 1000 for r in range(1, 20000) if abs((2 - r / 1000) ** 2 + (1 - r / 1000) ** 2 - (r / 1000) ** 2) < 1e-9]
    return pick(ch, sum(rs))


def c08(ch):
    people = 'ABCDE'
    n = sum(1 for p in permutations(people) if abs(p.index('A') - p.index('B')) != 1)
    return pick(ch, n)


def c09(ch):
    return pick(ch, 50 - (2.4 * 5 + 31), tol=1e-9)


def c10(ch):
    return pick(ch, (30000 + 16000) / (12 + 8))


def c11(ch):
    sols = [10 * t + u for t in range(1, 10) for u in range(0, 10) if t + u == 9 and (10 * u + t) - (10 * t + u) == 27]
    return pick(ch, sols[0])


CHECKS = {f'B014-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11], 1)}
