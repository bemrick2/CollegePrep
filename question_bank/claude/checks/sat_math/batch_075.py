"""Scripted recomputation for SAT Math batch 75. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import itertools
import os
import statistics
import sys
from fractions import Fraction as F

import numpy as np
import sympy as sp
from sympy.parsing.sympy_parser import implicit_multiplication_application, parse_expr, standard_transformations

T = standard_transformations + (implicit_multiplication_application,)

sys.path.insert(0, os.path.dirname(__file__))
from _util import num, pick  # noqa: E402

x, y = sp.symbols('x y', real=True)


def by_text(ch, want):
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def line_hits(ch, pred):
    hits = []
    for k, v in ch.items():
        lhs, rhs = v.replace('−', '-').replace(',', '').split('=')
        e = parse_expr(lhs, local_dict={'x': x, 'y': y}, transformations=T) - sp.sympify(rhs)
        if pred(e):
            hits.append(k)
    assert len(hits) == 1, hits
    return hits[0]


def c01(ch):
    P = sp.Matrix([4, 3]) * 10 / 5
    def ok(e):
        on = e.subs({x: P[0], y: P[1]}) == 0
        grad = (sp.diff(e, x), sp.diff(e, y))
        return on and grad[0] * 3 - grad[1] * 4 == 0  # normal parallel to (4, 3)
    return line_hits(ch, ok)


def c02(ch):
    quads = set()
    for px, py in itertools.product(np.linspace(-20, 20, 161), repeat=2):
        if px == 0 or py == 0:
            continue
        if py > 2 * px + 3 and py < -px - 1:
            quads.add({(1, 1): 'I', (-1, 1): 'II', (-1, -1): 'III', (1, -1): 'IV'}[(int(np.sign(px)), int(np.sign(py)))])
    order = ['I', 'II', 'III', 'IV']
    q = [o for o in order if o in quads]
    want = q[0] + ' only' if len(q) == 1 else (' and '.join(q) if len(q) == 2 else ', '.join(q[:-1]) + ', and ' + q[-1])
    return by_text(ch, want)


def c03(ch):
    return pick(ch, F(9) / F('1.8'))


def c04(ch):
    r = F('4.5') * (1 - (F('6.0') - F('4.5')) / F('6.0'))
    return pick(ch, r, conv=lambda t: F(t.replace('%', '')))


def c05(ch):
    return pick(ch, F(500, 125) + F(300, 200))


def c06(ch):
    return pick(ch, F(72, 180) / F(24, 120))


def c07(_):
    return F('0.4') / F('0.25') * 3600


def c08(ch):
    return by_text(ch, "For patients like those in the study, taking drug A likely causes fewer symptom days than taking drug B does.")


def c09(_):
    sols = []
    for jn, sc in itertools.product(range(151), repeat=2):  # juniors-not-in-club, seniors-in-club
        if 24 + jn + sc + 36 != 150:
            continue
        juniors, club = 24 + jn, 24 + sc
        if F(24, club) == F(24, juniors):
            sols.append(sc)
    assert len(sols) == 1
    return F(sols[0])


def c10(_):
    n = 1
    while not (F(45, 100) * n).denominator == 1 or not (F(40, 100) * F(45, 100) * n).denominator == 1:
        n += 1
    return F(n)


def c11(ch):
    p = F(100)
    dec = (F(120, 100) * p - F(114, 100) * p) / (F(120, 100) * p) * 100
    return pick(ch, dec, conv=lambda t: F(t.replace('%', '')))


def c12(_):
    vals = set()
    for cand in [F(n, 2) for n in range(-200, 201)]:
        d = sorted([3, 8, 12, cand, 15, 20])
        if F(sum(d), 6) == (F(d[2]) + F(d[3])) / 2:
            vals.add(cand)
    assert vals == {2, 11, 23}, vals
    return F(sum(vals))


def c13(ch):
    return pick(ch, F(35, 65), conv=F)


def c14(ch):
    X = np.arange(1, 13)
    Y = 3 * X + 5.0
    Y[0] = 30
    m1, b1 = np.polyfit(X, Y, 1)
    m2, b2 = np.polyfit(X[1:], Y[1:], 1)
    want = ('Greater' if m2 > m1 else 'Smaller') + ' slope and ' + ('greater' if b2 > b1 else 'smaller') + ' y-intercept'
    return by_text(ch, want)


def c15(ch):
    A = [2] * 4 + [8] * 4
    B = [0] + [5] * 6 + [10]
    rA, rB = max(A) - min(A), max(B) - min(B)
    sA, sB = statistics.pstdev(A), statistics.pstdev(B)
    assert statistics.stdev(A) > statistics.stdev(B)
    assert rB > rA and sA > sB
    return by_text(ch, "Data set B has the greater range, but data set A has the greater standard deviation.")


CHECKS = {f'Q075-{i:02d}': f for i, f in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15], 1)}
