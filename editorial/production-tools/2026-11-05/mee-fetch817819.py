from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import urllib.request,json,hashlib,fitz
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
jobs=[('E2.6.07','rousseau1989.html','https://link.springer.com/article/10.1007/BF01384942'),('E2.6.07','rousseau1995-sage.html','https://www.sagepub.com/shop/buy-a-book/psychological-contracts-in-organizations-1-5077'),('E2.6.07','rousseau2000-pci.pdf','https://www.andrew.cmu.edu/user/rousseau/0_reports/PCI.pdf'),('E2.6.07','gallup2026.pdf','https://www.gallup.com/file/workplace/707798/state-of-the-global-workplace-2026-download.pdf'),('E2.6.08','stokes2013-excerpt.pdf','https://assets.cambridge.org/97811070/42209/excerpt/9781107042209_excerpt.pdf'),('E2.6.08','stokes2021.pdf','https://www.wider.unu.edu/sites/default/files/Publications/Working-paper/PDF/wp2021-91-clientelism-and-development-poverty-trap.pdf'),('E2.6.09','mintz-wolf1950-translated1995.pdf','https://dspace.ups.edu.ec/bitstream/123456789/21049/1/Cosmos%20hombre%20y%20sacralidad.pdf')]
def fetch(j):
 ident,name,url=j;p=base/ident/'sources'/name;assert not p.exists() and not Path(str(p)+'.retrieval.json').exists();info=dict(url=url,retrieved_at=datetime.now(timezone.utc).isoformat())
 try:
  res=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35);b=res.read();info.update(status=res.status,final_url=res.url,bytes=len(b),sha256=hashlib.sha256(b).hexdigest());assert len(b)<30000000
  if name.endswith('.pdf'):assert b.startswith(b'%PDF');doc=fitz.open(stream=b,filetype='pdf');info['pages']=len(doc);Path(str(p)+'.txt').write_text('\n'.join('PAGE '+str(i+1)+'\n'+x.get_text()for i,x in enumerate(doc)))
  p.write_bytes(b);info['saved']=True
 except Exception as e:info.update(saved=False,error=str(e))
 Path(str(p)+'.retrieval.json').write_text(json.dumps(info,ensure_ascii=False,indent=2)+'\n');return dict(id=ident,file=name,**info)
with ThreadPoolExecutor(max_workers=4)as ex:
 for x in ex.map(fetch,jobs):print(json.dumps(x,ensure_ascii=False),flush=True)
