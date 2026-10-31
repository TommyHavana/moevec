from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import urllib.request,urllib.error,json,hashlib
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
items=[('E4.11.01', 'march1991.pdf', 'https://web.stanford.edu/group/e145/cgi-bin/winter/drupal/upload/handouts/March.pdf'), ('E4.11.02', 'gollwitzer1999.pdf', 'https://wp.nyu.edu/motivationlab/wp-content/uploads/sites/6235/2019/02/gollwitzer-1999-implementation-intentions.pdf'), ('E4.11.02', 'goals-gone-wild-hbs-alt.pdf', 'https://www.hbs.edu/ris/Publication%20Files/09-083.pdf'), ('E4.11.03', 'xoan-beneficio-search.html', 'https://xoandelugo.org/?s=beneficio'), ('E4.11.03', 'sandel-macmillan.html', 'https://us.macmillan.com/books/9780374533656/whatmoneycantbuy/')]
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
