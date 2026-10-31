from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import urllib.request,urllib.error,json,hashlib
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
items=[
('E4.10.10','milkie-wiley.html','https://onlinelibrary.wiley.com/doi/abs/10.1111/jomf.12170'),
('E4.10.10','milkie-bgsu.html','https://profiles.bgsu.edu/en/publications/does-the-amount-of-time-mothers-spend-with-children-or-adolescent/'),
('E4.10.10','steinhauser-pubmed.html','https://pubmed.ncbi.nlm.nih.gov/11074777/'),
('E4.10.11','drucker-routledge.html','https://www.routledge.com/The-Effective-Executive/Drucker/p/book/9781138470101'),
('E4.10.11','daily-drucker-preview.html','https://www.oreilly.com/library/view/the-daily-drucker/9780061802669/1september.xhtml'),
('E4.10.11','etkin-duke.html','https://scholars.duke.edu/publication/1134328'),
('E4.10.12','oms-oit2021.html','https://www.who.int/news/item/17-05-2021-long-working-hours-increasing-deaths-from-heart-disease-and-stroke-who-ilo'),
('E4.10.12','mee-proyecto-paralelo.html','https://moevec.org/blog/proyecto-paralelo-trabajar-de-dia/'),
('E4.10.12','mee-salud-limite.html','https://moevec.org/blog/sacrificio-y-salud-limite/')]
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
