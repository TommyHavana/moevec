from pathlib import Path
from urllib.request import Request,urlopen
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import hashlib,json,re
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,d):self.parts.append(d)
jobs=[('E2.2.15', 'bde-compuesto.html', 'https://clientebancario.bde.es/pcb/en/blog/sabes-que-es-el-tipo-de-interes-compuesto-.html'), ('E2.2.15', 'bce-inflacion.html', 'https://www.ecb.europa.eu/ecb-and-you/explainers/tell-me-more/html/what_is_inflation.es.html'), ('E2.3.02', 'chile-cotizacion.html', 'https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-10906.html'), ('E2.3.02', 'suecia-norden.html', 'https://www.norden.org/en/info-norden/national-public-pension-sweden'), ('E2.3.02', 'ocde-pensions2025.html', 'https://www.oecd.org/en/publications/pensions-at-a-glance-2025_e40274c1-en.html')]
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
