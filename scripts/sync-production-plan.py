#!/usr/bin/env python3
"""Build the numbered editorial manifest from the founder's two source documents."""
import csv, json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = root.parent / 'MEE_Plan_Editorial_840_entradas.md'
plan = source.read_text()
prompt = (root.parent / 'MEE_Prompt_ChatGPT_Produccion_WordPress.md').read_text()
batches = {}
for match in re.finditer(r'^\| (\d+)/56 \| (\d+\.\d+) (.+?) \| `([^`]+)` \| `([^`]+)` \|', prompt, re.M):
    batches['E' + match[2]] = dict(batch=int(match[1]), topic_name=match[3], topic=match[4], area=match[5])
entries = []
for match in re.finditer(r'^#### (E\d+\.\d+\.\d+) · (.+)\n`([^`]+)` · \*\*([^*]+)\*\*', plan, re.M):
    prefix = '.'.join(match[1].split('.')[:2])
    entries.append(dict(id=match[1], title=match[2], slug=match[3], level=match[4], entry=int(match[1].split('.')[-1]), source_line=plan[:match.start()].count('\n')+1, **batches[prefix]))
entries.sort(key=lambda row: (row['batch'], row['entry']))
assert len(entries) == len({row['id'] for row in entries}) == len({row['slug'] for row in entries}) == 840
assert len(batches) == 56
for number, row in enumerate(entries, 1):
    row['number'] = number
destination = root / 'wordpress/plugins/mee-editorial/data/production-plan.json'
destination.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + '\n')
print(f'{len(entries)} entradas numeradas en {destination}')
