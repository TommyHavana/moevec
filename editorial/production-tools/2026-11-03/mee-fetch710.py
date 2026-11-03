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
jobs=[('E6.6.05', 'investor-ponzi.html', 'https://www.investor.gov/protect-your-investments/fraud/types-fraud/ponzi-scheme'), ('E6.6.05', 'uspis-history.html', 'https://www.uspis.gov/about/old-history-dont-share'), ('E6.6.05', 'sec-oig509-2009.pdf', 'https://www.sec.gov/news/studies/2009/oig-509.pdf'), ('E6.6.05', 'supersoc-dmg2021.pdf', 'https://www.supersociedades.gov.co/documents/58444/262419/2021-01-737492-AAE.PDF/129ef1a1-3d25-a4a5-f7a1-865c6023a276?t=1667312543471'), ('E6.6.05', 'cnmv-decalogo.html', 'https://www.cnmv.es/portal/inversor/Decalogo-chiringuitos')]
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
