"""Scripted recomputation for ACT Math batch 2. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def cplx(text):  # '−5 + 10i' -> complex
    t = text.replace('−', '-').replace(' ', '').replace('i', 'j')
    return complex(t)


def c01(ch):
    return pick(ch, (3 - 2j) * (1 + 4j), conv=cplx)


def c02(ch):  # 2x^2 - 7x - 15 = 0
    a, b, c = 2, -7, -15
    d = math.sqrt(b * b - 4 * a * c)
    return pick(ch, (-b + d) / (2 * a) + (-b - d) / (2 * a))


def c03(ch):  # x/(x-2) + 1 = 2/(x-2): search rational candidates exactly
    sols = set()
    for num in range(-400, 401):
        for den in (1, 2, 3, 4):
            x = F(num, den)
            if x != 2 and x / (x - 2) + 1 == F(2) / (x - 2):
                sols.add(x)
    # cleared equation is linear (2x = 4); its only root is excluded, so no solution
    target = 'The empty set' if not sols else '{' + ', '.join(str(s) for s in sorted(sols)) + '}'
    return pick(ch, target, conv=lambda t: t.strip())


def c04(ch):
    xs, ys = [1, 2, 3, 4], [7, 10, 13, 16]
    hits = []
    for k, v in ch.items():
        m = re.fullmatch(r'f\(x\) = (\d*)x \+ (\d+)', v)
        a = int(m.group(1) or 1); b = int(m.group(2))
        if all(a * x + b == y for x, y in zip(xs, ys)):
            hits.append(k)
    assert len(hits) == 1, hits
    return hits[0]


def c05(ch):
    t = 5 * math.log(60000 / 1200, 2)
    return pick(ch, round(t, 1), tol=1e-6)


def c06(ch):
    (x1, y1), (x2, y2) = (-3, 4), (5, -2)
    h, k = (x1 + x2) / 2, (y1 + y2) / 2
    r2 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) / 4
    def parse(t):
        m = re.fullmatch(r'\(x ([+−]) (\d+)\)² \+ \(y ([+−]) (\d+)\)² = (\d+)', t)
        hh = int(m.group(2)) * (1 if m.group(1) == '−' else -1)
        kk = int(m.group(4)) * (1 if m.group(3) == '−' else -1)
        return (hh, kk, int(m.group(5)))
    return pick(ch, (h, k, r2), conv=parse)


def c07(ch):
    k = math.sqrt(9 / 4)
    return pick(ch, 160 * k**3)


def c08(ch):
    from itertools import combinations
    people = ['J'] * 5 + ['S'] * 7
    teams = list(combinations(range(12), 3))
    good = sum(any(people[i] == 'J' for i in t) for t in teams)
    return pick(ch, F(good, len(teams)))


def c09(ch):
    vals = sorted([0] * 2 + [1] * 4 + [2] * 5 + [3] * 3 + [4] * 1)
    assert len(vals) == 15
    return pick(ch, vals[7])


def c10(ch):
    rate = 18 / 45 + 3 / 10
    return pick(ch, round(300 / rate / 60))


CHECKS = {f'B002-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
