from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import urllib.request,urllib.error,json,hashlib
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
items=[('E4.11.01', 'march-informs.html', 'https://pubsonline.informs.org/doi/10.1287/orsc.2.1.71'), ('E4.11.03', 'rohrer-wenz2024-full.html', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11572929/'), ('E4.11.03', 'arslan2024-full.html', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11572980/'), ('E4.11.03', 'sandel-new-harvard.html', 'https://sandel.scholars.harvard.edu/publications/what-money-cant-buy-moral-limits-markets')]
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
