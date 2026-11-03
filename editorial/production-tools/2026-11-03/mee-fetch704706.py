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
jobs=[('E6.5.14', 'sba-startup-costs.html', 'https://www.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs'), ('E6.5.14', 'sba-break-even.html', 'https://www.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs/break-even-point'), ('E6.5.14', 'bhide-bootstrap.html', 'https://pubmed.ncbi.nlm.nih.gov/10122688/'), ('E6.5.15', 'mentors-aea.html', 'https://www.aeaweb.org/articles?id=10.1257/app.20170042'), ('E6.5.15', 'mentors-jpal.html', 'https://www.povertyactionlab.org/evaluation/local-mentorship-and-business-training-increase-profits-among-microenterprises-kenya'), ('E6.5.15', 'mckenzie-2025.html', 'https://blogs.worldbank.org/en/impactevaluations/long-term-impacts-of-personal-initiative-training-in-togo'), ('E6.6.01', 'ecsp-eurlex.html', 'https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=celex%3A32020R1503'), ('E6.6.01', 'cnmv-risk-guide.pdf', 'https://www.cnmv.es/DocPortal/Publicaciones/Guias/GUIA_FINANCIACION_PARTICIPATIVA.pdf')]
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
