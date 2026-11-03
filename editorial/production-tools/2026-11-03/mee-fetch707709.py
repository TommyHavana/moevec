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
jobs=[('E6.6.03', 'mexico-lritf.pdf', 'https://www.diputados.gob.mx/LeyesBiblio/pdf/LRITF.pdf'), ('E6.6.03', 'espana-ley5-2015.html', 'https://www.boe.es/buscar/act.php?id=BOE-A-2015-4607'), ('E6.6.03', 'eu-council2020.html', 'https://www.consilium.europa.eu/es/press/press-releases/2020/07/20/capital-markets-union-council-adopts-new-rules-for-crowdfunding-platforms/'), ('E6.6.04', 'nobel2016-press.html', 'https://www.nobelprize.org/prizes/economic-sciences/2016/press-release/'), ('E6.6.04', 'szabo1994.html', 'https://nakamotoinstitute.org/library/smart-contracts/')]
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
