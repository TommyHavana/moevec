from pathlib import Path
from urllib.request import Request,urlopen
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,fitz
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
jobs=[
('E2.2.03','boe-civil.html','https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763'),
('E2.2.03','notariado.html','https://www.notariado.org/portal/relaciones-personales-y-familia'),
('E2.2.03','argentina-civil.html','https://www.argentina.gob.ar/normativa/nacional/ley-26994-235975/actualizacion'),
('E2.2.03','mexico-ccf.pdf','https://www.diputados.gob.mx/LeyesBiblio/pdf/CCF.pdf'),
('E2.2.03','cuba-natlex.html','https://natlex.ilo.org/dyn/natlex2/r/natlex/fe/details?p3_isn=116589'),
('E2.2.04','oecd2021.html','https://www.oecd.org/en/publications/inheritance-taxation-in-oecd-countries_e2879a7d-en/full-report.html'),
('E2.2.04','oecd2026.html','https://www.oecd.org/en/publications/financing-of-social-protection_b384fd31-en/full-report/securing-the-revenue-base-for-social-protection_fee691c9.html'),
('E2.2.04','sweden2004.html','https://www.riksdagen.se/sv/dokument-och-lagar/dokument/betankande/slopad-arvsskatt-och-gavoskatt-prop-20040525_gs01sku18/'),
('E2.2.04','sweden2005.pdf','https://rkrattsdb.gov.se/SFSdoc/05/050194.PDF'),
('E2.2.04','sweden-current.html','https://www.norden.org/en/info-norden/death-inheritance-and-wills-sweden'),
('E2.2.04','australia-ato.pdf','https://www.ato.gov.au/api/public/content/0-b5035092-39dc-4727-9c71-b6421477077c'),
('E2.2.04','canada-novascotia.pdf','https://www.novascotia.ca/sns/pdf/after-the-loss-of-a-loved-one.pdf'),
('E2.2.05','elinder2018.pdf','https://www.ifn.se/media/my4ksqb2/2018-elinder-erixon-waldenstr%C3%B6m-inheritance-and-wealth-inequality.pdf?v=20210421152907'),
('E2.2.05','chetty2014.html','https://opportunityinsights.org/paper/land-of-opportunity/')]
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip and d.strip():self.parts.append(d.strip())
def fetch(job):
 ident,name,url=job;p=r/ident/'sources'/name;rec=p.with_name(name+'.retrieval.json')
 if p.exists():return dict(id=ident,file=name,existing=True)
 x=dict(url=url,checked_on='2026-11-04',sources_verified=False,reading_complete=False)
 try:
  with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35)as f:b=f.read();x.update(status=f.status,final_url=f.url,content_type=f.headers.get('Content-Type'))
  p.write_bytes(b);x.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  if b.startswith(b'%PDF'):x['pdf_pages']=len(fitz.open(p))
  elif 'html'in x.get('content_type','')or b.lstrip().startswith(b'<!'):
   parser=Text();parser.feed(b.decode('utf-8',errors='replace'));p.with_name(name+'.visible.txt').write_text('\n'.join(parser.parts)+'\n')
  else:x['unparsed_content']=True
 except Exception as e:x['error']=type(e).__name__+': '+str(e)
 rec.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');return dict(id=ident,file=name,status=x.get('status'),bytes=x.get('bytes'),pages=x.get('pdf_pages'),error=x.get('error'))
with ThreadPoolExecutor(max_workers=4)as pool:
 for x in pool.map(fetch,jobs):print(json.dumps(x),flush=True)
