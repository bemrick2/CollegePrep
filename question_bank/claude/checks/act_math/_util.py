"""Shared helpers for the scripted answer checks. A check recomputes the answer from the stem's own numbers and
returns the single choice letter whose text matches; it never reads the answer key."""
from fractions import Fraction
import math
import re


def num(text: str) -> float:
    """Parse a choice like '−9', '12/5', '90%', '$1,250', '2√6', '3.5', '4π' into a float."""
    t = text.strip().replace('−', '-').replace(',', '').replace('$', '').replace('%', '').replace(' ', '')
    m = re.fullmatch(r'(-?[\d.]*)√(\d+)', t)
    if m:
        c = m.group(1)
        coef = -1.0 if c == '-' else (float(c) if c else 1.0)
        return coef * math.sqrt(float(m.group(2)))
    m = re.fullmatch(r'(-?[\d.]*)π', t)
    if m:
        c = m.group(1)
        return (-1.0 if c == '-' else (float(c) if c else 1.0)) * math.pi
    if '/' in t:
        a, b = t.split('/')
        return float(Fraction(a)) / float(Fraction(b))
    return float(t)


def pick(choices: dict, target, conv=num, tol=1e-9) -> str:
    """The one letter whose converted text equals target. Raises if zero or several match."""
    hits = []
    for k, v in choices.items():
        try:
            val = conv(v)
        except Exception:  # noqa: BLE001
            continue
        if isinstance(target, (int, float, Fraction)) and isinstance(val, (int, float, Fraction)):
            if abs(float(val) - float(target)) <= tol * max(1.0, abs(float(target))):
                hits.append(k)
        elif val == target:
            hits.append(k)
    if len(hits) != 1:
        raise ValueError(f'expected exactly one matching choice for {target!r}, got {hits}')
    return hits[0]
