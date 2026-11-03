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
jobs=[
('E4.12.04','panko2000-arxiv.html','https://arxiv.org/abs/0802.3457'),
('E4.12.04','panko2000-arxiv.pdf','https://arxiv.org/pdf/0802.3457'),
('E4.12.04','libre-sum.html','https://help.libreoffice.org/latest/es/text/scalc/01/func_sum.html'),
('E4.12.04','libre-functions.html','https://help.libreoffice.org/latest/es/text/scalc/01/04060100.html'),
('E4.12.04','libre-free.html','https://www.libreoffice.org/discover/libreoffice/'),
('E4.12.05','brynjolfsson2025.html','https://oup.silverchair-cdn.com/article-minimal/7990658'),
('E4.12.05','acemoglu2019.html','https://www.aeaweb.org/articles?id=10.1257/jep.33.2.3'),
('E4.12.05','nist-ai600-1.pdf','https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf'),
('E4.12.06','wordpress-site-editor.html','https://wordpress.org/documentation/article/site-editor/'),
('E4.12.06','n8n-export.md','https://docs.n8n.io/build/manage-workflows/export-and-import.md'),
('E4.12.06','n8n-migration.html','https://support.n8n.io/article/migrating-from-cloud-to-self-hosted'),
('E4.12.06','n8n-backup.md','https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/backup-and-restore.md')]
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
