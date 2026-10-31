from pathlib import Path
from datetime import datetime,timezone
import urllib.request,urllib.error,json,hashlib,concurrent.futures
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
items=[
('E4.12.01','nas2000-transfer.html','https://www.nationalacademies.org/read/9853/chapter/6'),
('E4.12.01','wef2025.pdf','https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf'),
('E4.12.02','comin-hobijn2010-aea.html','https://www.aeaweb.org/articles?id=10.1257/aer.100.5.2031'),
('E4.12.02','suri-mit-publications.html','https://mitsloan.mit.edu/faculty/directory/tavneet-suri'),
('E4.12.02','bateman2019-repository.html','https://ueaeprints.uea.ac.uk/id/eprint/71521/'),
('E4.12.03','digcomp3-jrc.html','https://joint-research-centre.ec.europa.eu/scientific-activities/key-competences-lifelong-learning/digital-competence-framework-digcomp/digcomp-30_en'),
('E4.12.03','digcomp22-jrc.html','https://publications.jrc.ec.europa.eu/repository/handle/JRC128415'),
('E4.12.03','oecd-piaac2024-insights.pdf','https://www.oecd.org/content/dam/oecd/en/publications/support-materials/2024/12/survey-of-adult-skills-2023_1ab54c9e/PIAAC2024_InsightsInterpretations_FULL.pdf'),
('E4.12.03','gcfglobal-es.html','https://edu.gcfglobal.org/es/')]
def fetch(item):
 ident,name,url=item;p=r/ident/'sources'/name;assert not p.exists()
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'});res=urllib.request.urlopen(req,timeout=50);data=res.read();status=res.status;final=res.url
 except urllib.error.HTTPError as e:data=e.read();status=e.code;final=e.url
 except Exception as e:return dict(id=ident,file=name,error=type(e).__name__)
 p.write_bytes(data);p.with_name(name+'.access.json').write_text(json.dumps(dict(url=url,final_url=final,status=status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),is_pdf=data.startswith(b'%PDF'),retrieved_at=datetime.now(timezone.utc).isoformat(),reading_confirmed=False),ensure_ascii=False,indent=2)+'\n');return dict(id=ident,file=name,status=status,bytes=len(data),is_pdf=data.startswith(b'%PDF'))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for result in pool.map(fetch,items):print(json.dumps(result),flush=True)
