#!/usr/bin/env python3
"""Build discovery data from the reviewed local articles and the WordPress register."""
import json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
plan = json.loads((root/'wordpress/plugins/mee-editorial/data/production-plan.json').read_text())
status = json.loads((root/'inventario/plan-editorial-840-status.json').read_text())
published = {x['id']: x for x in status['entries'] if x['status'] == 'terminada'}
catalog = {}
for entry in plan:
    if entry['id'] not in published:
        continue
    folder = root/'editorial/articles'/entry['id']
    article = json.loads((folder/'article.json').read_text())
    body = (folder/'article.html').read_text()
    words = len(re.findall(r'\S+', re.sub('<[^>]+>', ' ', body)))
    catalog[entry['id']] = {
        'id': entry['id'], 'title': article['title'], 'url': published[entry['id']]['url'],
        'slug': entry['slug'], 'area': entry['area'], 'topic': entry['topic'],
        'level': entry['level'], 'minutes': max(1, round(words/200)),
        'description': article['description'], 'keyword': article['keyword'],
    }
paths = json.loads((root/'editorial/reading-paths.json').read_text())
for path in paths:
    assert len(path['steps']) == 6
    path['steps'] = [{**catalog[step['id']], 'purpose': step['purpose']} for step in path['steps']]
    path['minutes'] = sum(step['minutes'] for step in path['steps'])
out = root/'wordpress/plugins/mee-editorial/data'
(out/'article-discovery.json').write_text(json.dumps(catalog, ensure_ascii=False, indent=2)+'\n')
(out/'reading-paths.json').write_text(json.dumps(paths, ensure_ascii=False, indent=2)+'\n')
print(f'{len(catalog)} artículos publicados; {len(paths)} rutas de seis lecturas.')
