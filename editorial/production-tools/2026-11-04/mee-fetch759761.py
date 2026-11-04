from pathlib import Path
from urllib.request import Request,urlopen
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import hashlib,json,re
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,d):self.parts.append(d)
jobs=[
('E2.2.09','argentina-civil.html','https://www.argentina.gob.ar/normativa/nacional/ley-26994-235975/actualizacion'),
('E2.2.09','notariado-deudas.html','https://andalucia.notariado.org/portal/preguntas-y-respuestas'),
('E2.2.10','ley5-2012.html','https://www.boe.es/buscar/act.php?id=BOE-A-2012-9112'),
('E2.2.10','directiva2008-52.html','https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32008L0052'),
('E2.2.11','ley50-1980.html','https://www.boe.es/buscar/act.php?id=BOE-A-1980-22501'),
('E2.2.11','lopdgdd.html','https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673'),
('E2.2.11','aepd-fallecidos.html','https://www.aepd.es/preguntas-frecuentes/0-conceptos-basicos/FAQ-0011-sobre-datos-personales-de-personas-fallecidas'),
('E2.2.11','consumo-beneficiarios.html','https://www.dsca.gob.es/en/consumo/preguntas-frecuentes/puedo-cambiar-beneficiario-seguro-vida')]
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
