from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import urllib.request,urllib.error,json,hashlib
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
items=[('E4.11.01', 'frankl-editorial.html', 'https://www.penguinrandomhouse.com/books/206272/mans-search-for-meaning-by-viktor-e-frankl/'), ('E4.11.01', 'locke-latham2002.pdf', 'https://goal-lab.psych.umn.edu/orgPsych/2020/readings/5.%20Motivation/Locke%20%26%20Latham%20%282002%29.pdf'), ('E4.11.02', 'gollwitzer-publications.html', 'https://wp.nyu.edu/motivationlab/publications/peter-gollwitzer/'), ('E4.11.02', 'goals-gone-wild2009.pdf', 'https://www.hbs.edu/ris/download.aspx?name=09-083.pdf'), ('E4.11.03', 'kahneman-deaton2010.html', 'https://pubmed.ncbi.nlm.nih.gov/20823223/'), ('E4.11.03', 'killingsworth2021.html', 'https://pubmed.ncbi.nlm.nih.gov/33468644/'), ('E4.11.03', 'kkm2023.html', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10013834/'), ('E4.11.03', 'kkm-reply2024.html', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11572976/'), ('E4.11.03', 'comment-rohrer2024.html', 'https://pubmed.ncbi.nlm.nih.gov/39480845/'), ('E4.11.03', 'comment-arslan2024.html', 'https://pubmed.ncbi.nlm.nih.gov/39480843/'), ('E4.11.03', 'bastos-entrevista2017.html', 'https://www.mises.org.es/2017/04/entrevista-a-miguel-anxo-bastos-boubeta/'), ('E4.11.03', 'sandel-market-limits.html', 'https://scholar.harvard.edu/sandel/publications/what-money-cant-buy-moral-limits-markets')]
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
