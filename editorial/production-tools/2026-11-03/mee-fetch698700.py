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
jobs=[('E6.5.08', 'findex2025-report.html', 'https://www.worldbank.org/en/publication/globalfindex/report'), ('E6.5.08', 'pix-bcb.html', 'https://bcb.gov.br/estabilidadefinanceira/pix-sobre'), ('E6.5.08', 'microcredit2015.pdf', 'https://economics.mit.edu/sites/default/files/publications/Six%20Randomized%20Evaluations%20of%20Microcredit.pdf'), ('E6.5.09', 'bruhn-mckenzie2013.html', 'https://blogs.worldbank.org/en/allaboutfinance/one-stop-shops-do-they-or-don-t-they-increase-business-registration'), ('E6.5.09', 'empresa-na-hora2023.html', 'https://irn.justica.gov.pt/Noticias-do-IRN/Empresa-na-Hora-18-anos-a-transformar-ideias-em-negocios'), ('E6.5.09', 'bready-methodology.html', 'https://www.worldbank.org/en/businessready/methodology'), ('E6.5.10', 'itu2025.html', 'https://www.itu.int/en/ITU-D/Statistics/Pages/facts/default.aspx'), ('E6.5.10', 'itu2025.pdf', 'https://www.itu.int/dms_pub/itu-d/opb/ind/d-ind-ict_mdd-2025-3-pdf-e.pdf'), ('E6.5.10', 'libre-calc.html', 'https://www.libreoffice.org/discover/calc/'), ('E6.5.10', 'libre-pdf.html', 'https://help.libreoffice.org/latest/en-US/text/shared/01/ref_pdf_export.html?DbPAR=CALC&System=Unknown+OS'), ('E6.5.10', 'whatsapp-catalog.html', 'https://faq.whatsapp.com/405903568419894/?helpref=uf_share'), ('E6.5.10', 'whatsapp-business-catalog.html', 'https://whatsappbusiness.com/resources/resource-library/whatsapp-business-app-resources-whatsapp-business-catalog/'), ('E6.5.10', 'pix-bcb.html', 'https://bcb.gov.br/estabilidadefinanceira/pix-sobre')]
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
