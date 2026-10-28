"""Scripted recomputation for SAT Math batch 93. Multiple-choice checks return a letter; SPR checks receive None and return the value."""
import math
from fractions import Fraction as F


def by_text(ch, want):
    hits = [kk for kk, t in ch.items() if t == want]
    assert len(hits) == 1, (want, ch)
    return hits[0]


def c01(_):
    h = math.isqrt(13 ** 2 - 5 ** 2)
    assert h * h == 13 ** 2 - 5 ** 2
    return F(1, 3) * 25 * h


def c02(ch):
    pq = F(20) / F(4, 5)          # cos P = 0.8 from sin P = 0.6
    qr = F(3, 5) * pq
    assert qr ** 2 + 20 ** 2 == pq ** 2
    return by_text(ch, str(int(qr)))


CHECKS = {'Q093-01': c02}
