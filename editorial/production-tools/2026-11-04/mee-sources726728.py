from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import urllib.request,json,hashlib
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
jobs=[('E6.7.06','morningstar-model.html','https://www.morningstarco.com/interactive-smi-model/'),('E6.7.06','morningstar-2011-reference.html','https://www.morningstarco.com/self-management-hbr-takes-a-look-inside-morning-star/'),('E6.7.07','semler-interview-2005.html','https://www.strategy-business.com/article/05408'),('E6.7.07','semco-institute.html','https://semcostyle.com/about-us/'),('E6.7.07','seven-day-weekend-publisher.html','https://www.penguinrandomhouse.com/books/292934/the-seven-day-weekend-by-ricardo-semler/'),('E6.7.08','haier-2025-esg.pdf','https://imagegroup1.haier.com/global/csr/W020260430669489102494.pdf'),('E6.7.08','haier-electronics-2018-esg.pdf','https://imagegroup1.haier.com/global/csr/W020200721604468832059.pdf')]
class Text(HTMLParser):
 def __init__(self):super().__init__();self.bits=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip and d.strip():self.bits.append(d.strip())
def fetch(job):
 ident,name,url=job;p=r/ident/'sources'/name;meta=dict(url=url,checked_at=datetime.now(timezone.utc).isoformat())
 if p.exists():return dict(file=name,existing=True)
 try:
  q=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60);b=q.read();meta.update(status=q.status,final_url=q.url,bytes=len(b),sha256=hashlib.sha256(b).hexdigest());assert b and (b[:4]==b'%PDF' if name.endswith('.pdf') else True);p.write_bytes(b)
  if name.endswith('.html'):
   t=Text();t.feed(b.decode('utf-8',errors='replace'));p.with_suffix('.visible.txt').write_text('\n'.join(t.bits)+'\n')
 except Exception as e:meta.update(error=str(e))
 p.with_name(p.name+'.access.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n');return dict(file=name,**meta)
with ThreadPoolExecutor(max_workers=4)as pool:
 for result in pool.map(fetch,jobs):print(json.dumps(result,ensure_ascii=False),flush=True)
