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
jobs=[('E6.5.05', 'suri-jack2016.pdf', 'https://www.findevgateway.org/sites/default/files/publications/files/new_jack_and_suri_paper_1.pdf'), ('E6.5.05', 'vodafone-launch.html', 'https://www.vodafone.com/news/newsroom/people/mpesa-marks-15-years'), ('E6.5.05', 'pix-bcb.html', 'https://bcb.gov.br/estabilidadefinanceira/pix-sobre'), ('E6.5.06', 'mckenzie-woodruff2014.pdf', 'https://openknowledge.worldbank.org/server/api/core/bitstreams/cbf23c46-7c97-5a20-b403-a5fe1f0ffe5f/content'), ('E6.5.06', 'campos2017.pdf', 'https://documents1.worldbank.org/curated/en/865931506094667006/pdf/119938-REVISED-Teaching-personal-initiative-beats-traditional-training-in-boosting-small-business-in-West-Africa-Working-Paper.pdf'), ('E6.5.06', 'mckenzie2025-followup.html', 'https://blogs.worldbank.org/en/impactevaluations/personal-initiative-training-continues-to-yield-positive-benefit'), ('E6.5.07', 'wbl2026.pdf', 'https://openknowledge.worldbank.org/bitstreams/4407cff6-6c6b-44cf-b89b-d1260f1a0700/download'), ('E6.5.07', 'wbl2026-report.html', 'https://wbl.worldbank.org/en/publications/flagship-report'), ('E6.5.07', 'wbl-methodology.html', 'https://wbl.worldbank.org/en/data/methodology'), ('E6.5.07', 'mckenzie2025-followup.html', 'https://blogs.worldbank.org/en/impactevaluations/personal-initiative-training-continues-to-yield-positive-benefit')]
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
