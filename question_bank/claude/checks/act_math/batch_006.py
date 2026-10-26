"""Scripted recomputation for ACT Math batch 6. Each check derives the answer from the stem's numbers only."""
import math
import os
import random
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    x = (5 + math.sqrt(21)) / 2  # a root of x + 1/x = 5
    assert abs(x + 1 / x - 5) < 1e-12
    return pick(ch, x * x + 1 / (x * x), tol=1e-9)


def c02(ch):
    packs = [t + f for t in range(0, 12) for f in range(0, 8) if 3 * t + 5 * f == 31]
    return pick(ch, max(packs))


def as_func(t):  # '(x − 3)/(x − 2)' or '3/2' -> python callable
    s = t.replace('−', '-')
    return lambda x: eval(s, {'x': x})  # noqa: S307 - fixed choice strings


def c03(ch):
    xs = [F(n, 7) for n in (-20, -1, 0, 5, 11, 30)]
    orig = lambda x: (x * x - 9) / (x * x + x - 6)
    hits = [k for k, v in ch.items() if all(as_func(v)(x) == orig(x) for x in xs)]
    assert len(hits) == 1, hits
    return hits[0]


def c04(ch):
    f = 3
    for _ in range(4):
        f = 2 * f - 1
    return pick(ch, f)


def c05(ch):  # measure of {t : h(t) > 16.75} on a fine grid
    h = lambda t: -5 * t * t + 20 * t + 1.75
    step = 1e-4
    dur = sum(step for i in range(0, 60000) if h(i * step) > 16.75)
    return pick(ch, round(dur, 2), tol=1e-6)


def c06(ch):  # coordinates: O at origin, P at (13, 0); tangency points satisfy OT ⟂ PT
    r, d = 5.0, 13.0
    xt = r * r / d
    yt = math.sqrt(r * r - xt * xt)
    assert abs((xt * (xt - d)) + yt * yt) < 1e-9  # OT · PT = 0
    return pick(ch, 2 * yt)


def trig(t):
    m = re.fullmatch(r'1\.2 ?(/)? ?(sin|cos|tan) 6°', t.replace(' / ', '/').replace('/ ', '/'))
    s = t.replace('°', '')
    v = {'sin': math.sin, 'cos': math.cos, 'tan': math.tan}[re.search(r'(sin|cos|tan)', s).group(1)](math.radians(6))
    return 1.2 / v if '/' in s else 1.2 * v


def c07(ch):  # hypotenuse L with L*sin(6°) = 1.2, found by bisection on the geometry
    lo, hi = 1.2, 100.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if mid * math.sin(math.radians(6)) < 1.2:
            lo = mid
        else:
            hi = mid
    return pick(ch, lo, conv=trig, tol=1e-9)


def c08(ch):  # exact count on a fine lattice of cell centers, then Monte Carlo cross-check
    n = 1000
    h = 10 / n
    inside = sum(1 for i in range(n) for j in range(n)
                 if min((i + .5) * h, 10 - (i + .5) * h, (j + .5) * h, 10 - (j + .5) * h) <= 2)
    p = inside / n / n
    rng = random.Random(6)
    mc = sum(min(x, 10 - x, y, 10 - y) <= 2 for x, y in ((rng.uniform(0, 10), rng.uniform(0, 10)) for _ in range(200000))) / 200000
    assert abs(mc - p) < 0.01
    return pick(ch, p, tol=1e-3)


def c09(ch):  # simulate in small time steps
    level, t, dt = F(1, 3), F(0), F(1, 100)
    while level < 1:
        level += (F(1, 6) - F(1, 9)) * dt
        t += dt
    return pick(ch, t)


def c10(ch):
    for k in range(1, 100):
        if 3 * k + 6 == 5 * k:
            return pick(ch, 8 * k)
    raise ValueError


CHECKS = {f'B006-{i:02d}': fn for i, fn in enumerate([c01, c02, c03, c04, c05, c06, c07, c08, c09, c10], 1)}
