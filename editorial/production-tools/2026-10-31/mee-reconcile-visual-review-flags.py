from pathlib import Path
from datetime import datetime,timezone
import json
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');s=json.load(open(r/'editorial/production-state.json'));reg=json.load(open(r/'inventario/plan-editorial-840-status.json'));changed=[]
for row in reg['entries']:
 if row['number']not in s['completed_this_run']or row['status']!='terminada':continue
 d=r/'editorial/articles'/row['id'];a=json.load(open(d/'article.json'));v=json.load(open(d/'verification.json'));assert a['review']['images_visually_checked']and len(v['images'])==3 and not v['issues']
 for n in ['research.json','metadata-draft.json']:
  p=d/n;x=json.load(open(p))
  if x.get('images_visually_checked')is not True:
   x['images_visually_checked']=True;p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');changed.append(str(p.relative_to(r)))
p=r/'inventario/auditoria-2026-10-28/editorial-631-633-visual-records-reconciliation.json';p.write_text(json.dumps(dict(checked_at=datetime.now(timezone.utc).isoformat(),changed=changed,basis='Existing article review confirms visual inspection; public verification confirms three images without issues. Only stale research/metadata flags reconciled; no WordPress or content change.'),ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(files_updated=len(changed),wordpress_changes=0)))
