"""Scripted recomputation for ACT Math batch 25. Each check derives the answer from the stem's numbers only."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


def c01(ch):
    return pick(ch, -(3 ** 2) + (-2) ** 3)


def c02(ch):
    return pick(ch, sum(1 for n in range(1, 100) if 50 < n * n < 500))


def c03(ch):
    L = 25
    return pick(ch, math.sqrt(L * L - 7 * 7) - math.sqrt(L * L - 15 * 15))


def c04(ch):
    g = lambda t: 350 - 12.5 * t
    rate = g(1) - g(0)
    want = 'loses' if rate < 0 else 'gains'
    return pick(ch, (want, abs(rate)), conv=lambda t: (('loses' if 'loses' in t else 'gains' if 'gains' in t else t),
                                                       12.5 if 'each minute' in t else None))


def c05(ch):
    return pick(ch, 0.5 * 8 * 10 * math.sin(math.radians(60)))


def c06(ch):
    import itertools
    seen = set()
    for lows in itertools.combinations_with_replacement(range(0, 60, 3), 3):  # values below the median
        for highs in itertools.combinations_with_replacement(range(40, 60, 4), 2):  # values between median and max
            before = sorted(list(lows) + [40] + list(highs) + [95])
            after = sorted(list(lows) + [40] + list(highs) + [59])
            if before[3] != 40 or after[-1] != 59:
                continue
            mean_dir = 'dec' if sum(after) < sum(before) else 'same'
            med_dir = 'same' if after[3] == before[3] else 'dec'
            seen.add((mean_dir, med_dir))
    assert seen == {('dec', 'same')}, seen

    def conv(t):
        m = 'dec' if ('mean decreases' in t or 'Both the mean and the median decrease' in t) else 'same'
        d = 'dec' if ('median decreases' in t or 'Both the mean and the median decrease' in t) else 'same'
        return (m, d)
    return pick(ch, ('dec', 'same'), conv=conv)


def c07(ch):
    n = 10
    return pick(ch, sum(1 for i in range(n) for j in range(i + 1, n) if (j - i) % n not in (1, n - 1)))


def c08(ch):
    return pick(ch, (80 - 10) * 0.75 - (80 * 0.75 - 10), conv=lambda t: float(t.replace('$', '')))


def c09(ch):
    sols = [(F(x, 7), F(y, 7)) for x in range(-200, 201) for y in range(-200, 201)
            if 2 * F(x, 7) - 3 * F(y, 7) == 7 and 4 * F(x, 7) + F(y, 7) == 21]
    x, y = sols[0]
    return pick(ch, 6 * x - 2 * y)


def c10(ch):
    roots = set()
    for k in (3, -3):
        v = 4 + k
        if v > 0:
            roots |= {round(math.sqrt(v), 9), round(-math.sqrt(v), 9)}
        elif v == 0:
            roots.add(0.0)
    return pick(ch, len(roots))


CHECKS = {f'B025-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
