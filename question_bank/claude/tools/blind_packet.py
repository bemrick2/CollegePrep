#!/usr/bin/env python3
"""Write the answer-free packet a blind solver sees: candidate id, passage (if any), stem and choices only.

For ACT English the passage is rendered the way the app shows it: only this item's underlined portion is in [brackets].
"""
import json
import re
import sys
from pathlib import Path

UNDERLINE = re.compile(r'\{\{(\d+)\|([^}]*)\}\}')


def render(t, n):
    return UNDERLINE.sub(lambda m: f'[{m.group(2)}]' if n is not None and int(m.group(1)) == n else m.group(2), t)


draft, out = Path(sys.argv[1]), Path(sys.argv[2])
d = json.loads(draft.read_text(encoding='utf-8'))
passages = {p['passage_id']: p for p in d.get('passages', [])}
packet = []
for c in d['candidates']:
    item = {'cand': c['cand']}
    if c.get('passage_id'):
        item['passage_id'] = c['passage_id']
        item['passage'] = render(passages[c['passage_id']]['text'], c.get('underline'))
    item['stem'] = c['stem']
    if c.get('format') == 'spr':
        item['answer_format'] = 'student-produced response: enter a number (no choices)'
    else:
        item['choices'] = c['choices']
    packet.append(item)
out.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(packet)} items -> {out}')
