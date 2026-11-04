from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import urllib.request,json,hashlib
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
jobs=[('E6.7.09', 'holacracy-constitution-v5.html', 'https://www.holacracy.org/constitution/5.0/'), ('E6.7.09', 'hsieh-interview-2017.html', 'https://www.mckinsey.com/capabilities/people-and-organization/our-insights/safe-enough-to-try-an-interview-with-zappos-ceo-tony-hsieh'), ('E6.7.09', 'insead-case-abstract.html', 'https://www.insead.edu/faculty-research/publications/case-studies/tony-hsieh-zappos-structure-culture-and-change-spanish'), ('E6.7.10', 'ley-7-1996-consolidada.html', 'https://www.boe.es/buscar/act.php?id=BOE-A-1996-1072'), ('E6.7.10', 'rd-201-2010-consolidado.html', 'https://www.boe.es/buscar/act.php?id=BOE-A-2010-4175'), ('E6.7.10', 'rdl-20-2018.html', 'https://www.boe.es/buscar/act.php?id=BOE-A-2018-16791'), ('E6.7.11', 'ivarsson-scaling-agile-2012.html', 'https://aivarsson.wordpress.com/2012/11/14/scaling-agile-spotify/'), ('E6.7.11', 'spotify-scaling-2012.pdf', 'https://blog.crisp.se/wp-content/uploads/2012/11/SpotifyScaling.pdf')]
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
