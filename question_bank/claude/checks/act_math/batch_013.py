"""Scripted recomputation for ACT Math batch 13. Each check derives the answer from the stem's numbers only."""
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def cfrac(t):
    s = t.replace('−', '-').replace(' ', '')
    m = re.fullmatch(r'\(([-\d]+)\+([-\d]+)i\)/\(?([-\d]+)\)?', s)
    if m:
        return complex(int(m.group(1)), int(m.group(2))) / int(m.group(3))
    m = re.fullmatch(r'([-\d]+)/([-\d]+)-i/([-\d]+)', s)
    return complex(int(m.group(1)) / int(m.group(2)), -1 / int(m.group(3)))


def c01(ch):
    target = (5 + 1j) / (2 - 3j)
    hits = [k for k, v in ch.items() if abs(cfrac(v) - target) < 1e-9]
    assert len(hits) == 1, hits
    return hits[0]


def c02(ch):
    sols = [x for x in range(-5, 200) if x + 6 > 0 and abs(math.log2(x + 6) - 5) < 1e-12]
    return pick(ch, sols[0])


def c03(ch):
    sols = [10 * t + u for t in range(1, 10) for u in range(0, 10) if t + u == 9 and (10 * u + t) - (10 * t + u) == 27]
    assert len(sols) == 1
    return pick(ch, sols[0])


def c04(ch):
    return pick(ch, round(min(4 * math.cos(i / 1000) - 1 for i in range(0, 7000)), 6), tol=1e-6)


def c05(ch):
    f = {2: 5}
    pts = [(F(x, 2), -f[x] + 1) for x in f]  # 2*(x/2) = x
    def pt(t):
        a, b = t.strip('() ').split(',')
        return (F(a.strip().replace('−', '-')), F(b.strip().replace('−', '-')))
    return pick(ch, (pts[0][0], F(pts[0][1])), conv=pt)


def c06(ch):
    cx, cy = 1, 1
    x, y = 3, -2
    th = math.pi / 2
    rx = cx + (x - cx) * math.cos(th) - (y - cy) * math.sin(th)
    ry = cy + (x - cx) * math.sin(th) + (y - cy) * math.cos(th)
    def pt(t):
        a, b = t.strip('() ').split(',')
        return (float(a.strip().replace('−', '-')), float(b.strip().replace('−', '-')))
    hits = [k for k, v in ch.items() if abs(pt(v)[0] - rx) < 1e-9 and abs(pt(v)[1] - ry) < 1e-9]
    assert len(hits) == 1
    return hits[0]


def c07(ch):
    return pick(ch, 4 / 3 * math.pi * 27, conv=lambda t: float(t.rstrip('π')) * math.pi, tol=1e-9)


def c08(ch):
    d = sorted([12, 15, 17, 20, 22, 25, 30, 31])
    med = lambda a: (a[len(a) // 2 - 1] + a[len(a) // 2]) / 2 if len(a) % 2 == 0 else a[len(a) // 2]
    return pick(ch, med(d[4:]) - med(d[:4]))


def c09(ch):
    sols = [w / 100 for w in range(1, 1250) if abs((40 - 2 * w / 100) * (25 - 2 * w / 100) - 544) < 1e-9]
    return pick(ch, sols[0])


def c10(ch):
    new = 100 * 0.8
    pct = (100 - new) / new * 100
    def p(t):
        m = re.fullmatch(r'(\d+) (\d+)/(\d+)%', t)
        return int(m.group(1)) + int(m.group(2)) / int(m.group(3)) if m else float(t.rstrip('%'))
    return pick(ch, pct, conv=p)


CHECKS = {f'B013-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
