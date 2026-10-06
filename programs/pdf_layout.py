"""Word positions from a PDF via poppler (`pdftotext -bbox-layout`): [{'width', 'height', 'lines': [{'y', 'words':
[[x0, x1, text], ...]}]}] per page, lines in poppler's reading order with their own y (top). Nothing is interpreted."""
from __future__ import annotations
import re, shutil, subprocess, tempfile
from html import unescape


def words(raw):
    exe = shutil.which('pdftotext')
    if not exe: return None
    with tempfile.NamedTemporaryFile(suffix='.pdf') as f:
        f.write(raw); f.flush()
        try:
            r = subprocess.run([exe, '-bbox-layout', '-enc', 'UTF-8', f.name, '-'], capture_output=True, timeout=120)
        except subprocess.TimeoutExpired:
            return None
    if r.returncode: return None
    return parse_bbox(r.stdout.decode('utf-8', 'replace'))


def parse_bbox(xhtml):
    pages = []
    for pm in re.finditer(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', xhtml, re.S):
        page = {'width': float(pm.group(1)), 'height': float(pm.group(2)), 'lines': []}
        for lm in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>', pm.group(3), re.S):
            ws = [[round(float(w.group(1)), 1), round(float(w.group(3)), 1), unescape(w.group(5))]
                  for w in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', lm.group(5), re.S)]
            if ws: page['lines'].append({'y': round(float(lm.group(2)), 1), 'y1': round(float(lm.group(4)), 1), 'words': ws})
        pages.append(page)
    return pages
