#!/usr/bin/env python3
"""Write the answer-free packet a blind solver sees: candidate id, stem and choices only."""
import json
import sys
from pathlib import Path

draft, out = Path(sys.argv[1]), Path(sys.argv[2])
d = json.loads(draft.read_text(encoding='utf-8'))
packet = [{'cand': c['cand'], 'stem': c['stem'], 'choices': c['choices']} for c in d['candidates']]
out.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(packet)} items -> {out}')
