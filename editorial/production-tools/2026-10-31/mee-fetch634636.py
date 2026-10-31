from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import urllib.request,urllib.error,json,hashlib
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
items=[('E4.11.04', 'schwartz2012.html', 'https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/'), ('E4.11.04', 'bardi2009.html', 'https://pubmed.ncbi.nlm.nih.gov/19857010/'), ('E4.11.05', 'duckworth2016.html', 'https://www.simonandschuster.com/books/Grit/Angela-Duckworth/9781501111112'), ('E4.11.05', 'crede2017.html', 'https://pubmed.ncbi.nlm.nih.gov/27845531/'), ('E4.11.05', 'wrosch2003.html', 'https://pubmed.ncbi.nlm.nih.gov/15018681/'), ('E4.11.06', 'gartenberg2019.html', 'https://pubsonline.informs.org/doi/abs/10.1287/orsc.2018.1230'), ('E4.11.06', 'gartenberg2019.pdf', 'https://www.ecgi.global/sites/default/files/Corporate%20Purpose%20and%20Financial%20Performance-%20Paper.pdf'), ('E4.11.06', 'friedman1970-nyt.html', 'https://www.nytimes.com/1970/09/13/archives/a-friedman-doctrine-the-social-responsibility-of-business-is-to.html')]
def fetch(x):
 i,n,u=x;p=r/i/'sources'/n;assert not p.exists()
 try:
  try:v=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 MEE editorial source review'}),timeout=40)
  except urllib.error.HTTPError as e:v=e
  b=v.read();p.write_bytes(b);o=dict(url=u,status=v.code,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),checked_at=datetime.now(timezone.utc).isoformat(),reading_confirmed=False)
 except (urllib.error.URLError,TimeoutError)as e:o=dict(url=u,error=type(e).__name__,reading_confirmed=False)
 p.with_suffix(p.suffix+'.access.json').write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n');return i,n,o.get('status',o.get('error')),o.get('bytes',0)
with ThreadPoolExecutor(max_workers=5)as ex:
 for x in ex.map(fetch,items):print(*x,flush=True)
