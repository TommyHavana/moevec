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
jobs=[('E6.6.06', 'nceo-numbers.html', 'https://www.nceo.org/research/employee-ownership-by-the-numbers'), ('E6.6.06', 'dol-erisa.html', 'https://www.dol.gov/general/topic/retirement/erisa'), ('E6.6.06', 'irs-esop.html', 'https://www.irs.gov/retirement-plans/employee-stock-ownership-plans-esops'), ('E6.6.06', 'boe-44-2015.html', 'https://www.boe.es/buscar/act.php?id=BOE-A-2015-11071'), ('E6.6.06', 'nber-shared.html', 'https://www.nber.org/books-and-chapters/shared-capitalism-work-employee-ownership-profit-and-gain-sharing-and-broad-based-stock-options'), ('E6.6.06', 'nber-introduction.pdf', 'https://www.nber.org/system/files/chapters/c8085/revisions/c8085.rev0.pdf'), ('E6.6.07', 'yc-safe.html', 'https://www.ycombinator.com/safe'), ('E6.6.07', 'sec-startup.html', 'https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/common-startup-securities'), ('E6.6.07', 'enisa-startups.html', 'https://www.enisa.es/servicios/financiacion/startups-y-pymes/'), ('E6.6.07', 'aeban.html', 'https://aeban.es/inversor-bussines-angel/'), ('E6.6.07', 'lavca-trends2026.html', 'https://www.lavca.org/research/2026-lavca-trends-in-tech/'), ('E6.6.08', 'atc-prestamos.html', 'https://atc.gencat.cat/es/que-cal-fer/prestec-particulars/'), ('E6.6.08', 'atc-plazo.html', 'https://atc.gencat.cat/es/tributs/itpajd/tpo/tramit-altres-tpo/')]
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
