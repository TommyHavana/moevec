from pathlib import Path
from urllib.request import Request,urlopen
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,fitz
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
jobs=[
('E2.2.12','cronqvist-siegel-nber2010.pdf','https://conference.nber.org/confer/2010/BEf10/CronqvistSiegel.pdf'),
('E2.2.14','carnegie-gospel1889.pdf','https://media.carnegie.org/filer_public/ab/c9/abc9fb4b-dc86-4ce8-ae31-a983b9a326ed/ccny_essay_1889_thegospelofwealth.pdf')]

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
