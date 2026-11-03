from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import urllib.request,urllib.error,json,hashlib
from html.parser import HTMLParser
class Visible(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.out=[]
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip and d.strip():self.out.append(d.strip())
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
jobs=[('E6.6.12', 'ostrom-lecture-page.html', 'https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/lecture/'), ('E6.6.12', 'ostrom2009.pdf', 'https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf'), ('E6.6.12', 'ostrom-interview2009.html', 'https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/164465-ostrom-williamson-interview-transcript/'), ('E6.6.13', 'ley118-2026-es11-mirror.pdf', 'https://www.directoriocubano.com/wp-content/uploads/dc-gaceta/archive/pdf/2026/09/edicion-especial/011/gaceta.pdf'), ('E6.6.13', 'ley118-2026-official-page.html', 'https://www.gacetaoficial.gob.cu/es/ley-118-de-2014-de-asamblea-nacional-del-poder-popular-0'), ('E6.6.13', 'ofac758.html', 'https://ofac.treasury.gov/faqs/758'), ('E6.6.13', 'ofac1273.html', 'https://ofac.treasury.gov/faqs/1273'), ('E6.6.13', 'ecfr515584.html', 'https://www.ecfr.gov/current/title-31/subtitle-B/chapter-V/part-515/subpart-E/section-515.584')]
def fetch(job):
 ident,name,url=job;d=r/ident/'sources';p=d/name;assert not p.exists()
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'});res=urllib.request.urlopen(req,timeout=45);data=res.read();status=res.status;final=res.url
 except urllib.error.HTTPError as e:data=e.read();status=e.code;final=e.url
 except Exception as e:return ident,name,type(e).__name__
 p.write_bytes(data);ev=dict(url=url,final_url=final,status=status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),is_pdf=data.startswith(b'%PDF'),checked_at=datetime.now(timezone.utc).isoformat());p.with_suffix(p.suffix+'.access.json').write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\n')
 if name.endswith('.html'):
  v=Visible();v.feed(data.decode('utf-8',errors='replace'));p.with_suffix('.visible.txt').write_text('\n'.join(v.out))
 return ident,name,status,len(data),data[:5].decode('utf-8',errors='replace')


with ThreadPoolExecutor(max_workers=5)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
