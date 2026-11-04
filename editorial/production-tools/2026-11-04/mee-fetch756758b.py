from pathlib import Path
from urllib.request import Request,urlopen
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,fitz
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
jobs=[
('E2.2.07','gaceta2026-o74-mirror.pdf','https://www.cibercuba.com/s/gacetaoficial/pdf/goc-2026-o74.pdf'),
('E2.2.08','reaf2026-probe.pdf','https://economistas.es/Contenido/REAF/Informes/Panorama%202026.pdf'),
('E2.2.08','ley29-1987-boe.pdf','https://www.boe.es/buscar/pdf/1987/BOE-A-1987-28141-consolidado.pdf'),
('E2.2.08','ley22-2009-boe.pdf','https://www.boe.es/buscar/pdf/2009/BOE-A-2009-20375-consolidado.pdf')]

def fetch(job):
 ident,name,u=job;p=r/ident/'sources'/name;rec=p.with_name(name+'.retrieval.json')
 if p.exists():return dict(file=name,existing=True)
 x=dict(url=u,checked_on='2026-11-04',sources_verified=False,reading_complete=False)
 try:
  with urlopen(Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=25)as f:b=f.read();x.update(status=f.status,final_url=f.url,content_type=f.headers.get('Content-Type'))
  assert b.startswith(b'%PDF'),'Not PDF';p.write_bytes(b);d=fitz.open(p);x.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),pages=len(d));p.with_name(name+'.text.txt').write_text('\n\n'.join('PDFPAGE '+str(i+1)+'\n'+pg.get_text()for i,pg in enumerate(d)))
 except Exception as e:x['error']=type(e).__name__+': '+str(e)
 rec.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');return x
with ThreadPoolExecutor(max_workers=4)as pool:
 for x in pool.map(fetch,jobs):print(json.dumps(x),flush=True)
