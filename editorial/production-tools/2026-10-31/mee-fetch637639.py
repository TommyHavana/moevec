from pathlib import Path
from datetime import datetime,timezone
import urllib.request,urllib.error,json,hashlib,concurrent.futures
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
items=[
('E4.11.07','cci-home.html','https://www.consciouscapitalism.org/'),
('E4.11.07','damodaran2021.html','https://aswathdamodaran.blogspot.com/2021/09/the-esg-movement-goodness-gravy-train.html'),
('E4.11.07','bastos2017.html','https://www.mises.org.es/2017/04/entrevista-a-miguel-anxo-bastos-boubeta/'),
('E4.11.08','hayek1944-spanish.pdf','https://cdn.mises.org/RoadtoSerfdom_camino-de-servidumbre.pdf'),
('E4.11.08','ostrom2009.pdf','https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf'),
('E4.11.09','winn2014.html','https://theviewinside.me/what-is-your-ikigai'),
('E4.11.09','winn-origin.html','https://theviewinside.me/ikigai'),
('E4.11.09','newport2012.html','https://calnewport.com/my-new-book-and-a-chance-to-speak-with-me-one-on-one/')]
def fetch(item):
 ident,name,url=item;p=r/ident/'sources'/name;assert not p.exists()
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'});res=urllib.request.urlopen(req,timeout=50);data=res.read();status=res.status;final=res.url
 except urllib.error.HTTPError as e:data=e.read();status=e.code;final=e.url
 except Exception as e:return dict(id=ident,file=name,error=type(e).__name__)
 p.write_bytes(data);p.with_name(name+'.access.json').write_text(json.dumps(dict(url=url,final_url=final,status=status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),is_pdf=data.startswith(b'%PDF'),retrieved_at=datetime.now(timezone.utc).isoformat(),reading_confirmed=False),ensure_ascii=False,indent=2)+'\n');return dict(id=ident,file=name,status=status,bytes=len(data),is_pdf=data.startswith(b'%PDF'))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for result in pool.map(fetch,items):print(json.dumps(result),flush=True)
