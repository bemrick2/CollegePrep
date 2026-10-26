"""Scripted recomputation for ACT Math batch 50. Each check derives the answer from the stem's numbers only."""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(__file__))
from _util import pick  # noqa: E402


money = lambda t: F(t.replace('$', '').replace(',', ''))


def c01(ch):
    return pick(ch, 2000 * (1 + F(5, 100) * 3), conv=money)


def c02(ch):
    g = lambda x: abs(x + 3)
    return pick(ch, g(-5) + g(1))


def c03(ch):
    n = 6
    return pick(ch, 3 * n)


def c04(ch):
    total = 3 * 10 ** 4 + 5 * 10 ** 3
    sup = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789')
    hits = []
    for k, v in ch.items():
        m = re.fullmatch(r'([\d.]+) × 10([⁰¹²³⁴⁵⁶⁷⁸⁹]+)', v)
        if F(m.group(1)) * 10 ** int(m.group(2).translate(sup)) == total:
            hits.append(k)
    assert len(hits) == 1
    return hits[0]


def c05(ch):
    return pick(ch, sum(1 for _ in itertools.product('HT', repeat=4)))


def c06(ch):
    m = 20 * F(9, 2) + 15
    want = f'{int(m) // 60} hour {int(m) % 60} minutes'
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1
    return hits[0]


def c07(ch):
    r2 = (4 - 1) ** 2 + (6 - 2) ** 2
    vals = {'A': 5, 'B': 10, 'C': 25, 'D': 49}
    hits = [k for k, v in vals.items() if v == r2]
    assert len(hits) == 1 and ch['C'] == '25π'
    return hits[0]


def c08(ch):
    ks = [k for k in range(1, 100) if (k / 2) ** 2 == 9]
    return pick(ch, ks[0])


def c09(ch):
    return pick(ch, sum(1 for n in range(1, 100) if 50 < 3 * n + 2 < 100))


def c10(ch):
    t = F(120) / (6 - F(1, 2))
    whole, frac = divmod(t, 1)
    want = f'{int(whole)} {frac.numerator}/{frac.denominator}'
    hits = [k for k, v in ch.items() if v == want]
    assert len(hits) == 1
    return hits[0]


CHECKS = {f'B050-{i:02d}': globals()[f'c{i:02d}'] for i in range(1, 11)}
