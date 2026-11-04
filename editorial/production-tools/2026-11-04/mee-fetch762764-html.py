from pathlib import Path
from urllib.request import Request,urlopen
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import hashlib,json,re
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,d):self.parts.append(d)
jobs=[('E2.2.12', 'gudmunson-danes2011.html', 'https://link.springer.com/article/10.1007/s10834-011-9275-y'), ('E2.2.13', 'reglamento650-2012.html', 'https://www.boe.es/buscar/doc.php?id=DOUE-L-2012-81342'), ('E2.2.13', 'hcch-status.html', 'https://www.hcch.net/en/instruments/status-table?cid=41'), ('E2.2.13', 'consulado-cuba-legalizaciones.html', 'https://www.exteriores.gob.es/Consulados/lahabana/es/ServiciosConsulares/Paginas/index.aspx?scca=Legalizaci%C3%B3n+o+Apostilla.+Compulsa+y+Registro&scco=Cuba&scd=166&scs=Legalizaci%C3%B3n+y+apostilla+de+la+Haya'), ('E2.2.14', 'reich-stanford.html', 'https://politicalscience.stanford.edu/publications/just-giving-why-philanthropy-failing-democracy-and-how-it-can-do-better'), ('E2.2.14', 'ley50-2002.html', 'https://www.boe.es/buscar/act.php?id=BOE-A-2002-25180')]
def fetch(j):
 id,name,u=j;p=Path('editorial/articles')/id/'sources'/name
 if p.exists():return dict(existing=name)
 x=dict(url=u,checked_on='2026-11-04',sources_verified=False,full_read=False)
 try:
  with urlopen(Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=25)as f:b=f.read();x.update(status=f.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  p.write_bytes(b);a=Parser();a.feed(b.decode('utf-8',errors='replace'));p.with_name(name+'.visible.txt').write_text(re.sub(r'\s+',' ',' '.join(a.parts)))
 except Exception as e:x['error']=str(e)
 p.with_name(name+'.retrieval.json').write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');return x
with ThreadPoolExecutor(max_workers=4)as p:
 for x in p.map(fetch,jobs):print(json.dumps(x),flush=True)
