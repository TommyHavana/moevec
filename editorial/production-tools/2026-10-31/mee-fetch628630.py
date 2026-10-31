from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import urllib.request,urllib.error,json,hashlib
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
items=[('E4.10.13', 'mckeown-chapter1.pdf', 'https://gregmckeown.com/preview/chpt1_essentialism.pdf'), ('E4.10.13', 'essentialism-editorial.html', 'https://www.penguinrandomhouse.com/books/228364/essentialism-by-greg-mckeown/9780804137393/'), ('E4.10.14', 'stutzer-frey2008.pdf', 'https://www.bsfrey.ch/wp-content/uploads/2021/08/stress-that-doesnt-pay-the-commuting-paradox.pdf'), ('E4.10.14', 'hybrid-bloom2024.html', 'https://www.nature.com/articles/s41586-024-07500-2'), ('E4.10.15', 'planning2025.html', 'https://www.annualreviews.org/content/journals/10.1146/annurev-psych-021524-110536'), ('E4.10.15', 'mee-plan-personal.html', 'https://moevec.org/blog/plan-anual-inversion-personal/'), ('E4.10.15', 'mee-tiempo-sacrificar.html', 'https://moevec.org/blog/cuanto-tiempo-sacrificar/')]
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
