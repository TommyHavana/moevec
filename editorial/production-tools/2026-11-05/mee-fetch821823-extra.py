from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import urllib.request,json,hashlib,fitz
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
jobs=[('E2.6.12','worldbank2008-diaspora-bonds.pdf','https://documents1.worldbank.org/curated/en/202621468156251840/pdf/456450PUB0978010ONLY10Sept030102008.pdf'),('E2.6.12','ifad2026-remittances.html','https://www.ifad.org/en/w/news/remittances-nearly-doubled-in-a-decade-to-reach-us-729-billion-in-2025-new-ifad-report-finds'),('E2.6.13','ief2015.pdf','https://www.iefamiliar.com/wp-content/uploads/2019/08/la-empresa-familiar-en-espana-2015.pdf'),('E2.6.13','ebep-consolidado.html','https://www.boe.es/buscar/act.php?id=BOE-A-2015-11719')]
def fetch(j):
 ident,name,url=j;p=base/ident/'sources'/name;assert not p.exists()and not Path(str(p)+'.retrieval.json').exists();i=dict(url=url,retrieved_at=datetime.now(timezone.utc).isoformat())
 try:
  res=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35);b=res.read();assert len(b)<30000000;i.update(status=res.status,final_url=res.url,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  if name.endswith('.pdf'):
   assert b.startswith(b'%PDF');doc=fitz.open(stream=b,filetype='pdf');i['pages']=len(doc);Path(str(p)+'.txt').write_text('\n'.join('PAGE '+str(n+1)+'\n'+x.get_text()for n,x in enumerate(doc)))
  p.write_bytes(b);i['saved']=True
 except Exception as e:i.update(saved=False,error=str(e))
 Path(str(p)+'.retrieval.json').write_text(json.dumps(i,ensure_ascii=False,indent=2)+'\n');return dict(id=ident,file=name,**i)
with ThreadPoolExecutor(max_workers=4)as ex:
 for x in ex.map(fetch,jobs):print(json.dumps(x,ensure_ascii=False),flush=True)
