from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import urllib.request,urllib.error,json,hashlib
from html.parser import HTMLParser
class Visible(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.out=[]
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip and d.strip():self.out.append(d.strip())
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
jobs=[('E6.5.11', 'circe-pae.html', 'https://www.pae.es/es-es/CreaEmpresaPorTiMismo/Paginas/Home.aspx'), ('E6.5.11', 'circe-one-autonomo.html', 'https://one.gob.es/es/tramites/alta-de-empresarios-individuales-autonomos'), ('E6.5.11', 'sat-personas-empresariales.html', 'https://sat.gob.mx/portal/public/personas-fisicas/pf-actividades-empresariales-y-profesionales'), ('E6.5.11', 'sat-oficina-virtual.html', 'https://www.gob.mx/sat/es/articulos/realiza-tramites-y-servicios-en-oficina-virtual-375604'), ('E6.5.11', 'dian-ruta.html', 'https://micrositios.dian.gov.co/ruta-de-la-formalizacion/pasos-de-la-formalizacion/'), ('E6.5.11', 'colombia-vue.html', 'https://www.vue.gov.co/tramites-y-consultas/creacion-empresa-persona-natural-juridica?c=41298'), ('E6.5.11', 'arca-monotributo.html', 'https://www.arca.gob.ar/monotributo/default.asp'), ('E6.5.12', 'dl88-2024-faolex.pdf', 'https://faolex.fao.org/docs/pdf/cub232597.pdf'), ('E6.5.12', 'gaceta2026-o71-official.pdf', 'https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-o71.pdf'), ('E6.5.12', 'gaceta2026-o71-reproduction.pdf', 'https://www.directoriocubano.com/wp-content/uploads/dc-gaceta/archive/pdf/2026/09/ordinaria/071/gaceta.pdf'), ('E6.5.13', 'sgr-ley1-1994.pdf', 'https://www.boe.es/buscar/pdf/1994/BOE-A-1994-5925-consolidado.pdf'), ('E6.5.13', 'sgr-ley1-1994.html', 'https://www.boe.es/buscar/act.php?id=BOE-A-1994-5925'), ('E6.5.13', 'microcredit2015.pdf', 'https://economics.mit.edu/sites/default/files/publications/Six%20Randomized%20Evaluations%20of%20Microcredit.pdf')]
def fetch(job):
 ident,name,url=job;d=r/ident/'sources';p=d/name;assert not p.exists()
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'});res=urllib.request.urlopen(req,timeout=45);data=res.read();status=res.status;final=res.url
 except urllib.error.HTTPError as e:data=e.read();status=e.code;final=e.url
 except Exception as e:return ident,name,type(e).__name__
 p.write_bytes(data);ev=dict(url=url,final_url=final,status=status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),is_pdf=data.startswith(b'%PDF'),checked_at=datetime.now(timezone.utc).isoformat());p.with_suffix(p.suffix+'.access.json').write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\n')
 if name.endswith('.html'):
  v=Visible();v.feed(data.decode('utf-8',errors='replace'));p.with_suffix('.visible.txt').write_text('\n'.join(v.out))
 return ident,name,status,len(data),data[:5].decode('utf-8',errors='replace')


with ThreadPoolExecutor(max_workers=5)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
