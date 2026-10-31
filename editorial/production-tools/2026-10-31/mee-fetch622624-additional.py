# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.10.07','oecd-worktime-policy2022','https://www.oecd.org/en/publications/oecd-employment-outlook-2022_1bb305a6-en/full-report/component-9.html'),('E4.10.08','une-nota-informativa','https://www.unionelectrica.cu/nota-informativa/'),('E4.10.08','fao-sofi2025-summary','https://www.fao.org/agrifood-economics/publications/detail/en/c/1740904/'),('E4.10.09','mee-documentar-negocio','https://moevec.org/blog/documentar-negocio-sin-ti/'),('E4.10.09','wef-future-jobs2025','https://www.weforum.org/publications/the-future-of-jobs-report-2025/'),('E4.10.09','libreoffice-current','https://www.libreoffice.org/'),('E4.10.09','calc-templates262','https://books.libreoffice.org/en/CG262/CG26204-StylesAndTemplates.html'),('E4.10.09','calc-autocalculate','https://help.libreoffice.org/latest/en-US/text/scalc/01/06070000.html'),('E4.10.09','thunderbird-recurring-event','https://support.mozilla.org/en-US/kb/creating-a-recurring-event')]
def fetch(x):
 i,n,u=x;d=base/i/'sources';a=dict(url=u,accessed_at=datetime.now(timezone.utc).isoformat())
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=50)as f:b=f.read();a.update(status=f.status,final_url=f.url,content_type=f.headers.get('Content-Type'))
  ext='.pdf'if b.startswith(b'%PDF')else'.html';(d/(n+ext)).write_bytes(b);a.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  if ext=='.html':
   t=b.decode('utf-8','replace');t=re.sub(r'<(script|style|nav|header|footer)\b.*?</\1>','',t,flags=re.S|re.I);t=html.unescape(re.sub('<[^>]+>',' ',t));t=re.sub(r'\s+',' ',t);(d/(n+'.txt')).write_text(t);a['text_file']=n+'.txt'
 except Exception as e:a['error']=str(e)
 (d/(n+'-access.json')).write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n');return i,n,a
with concurrent.futures.ThreadPoolExecutor(max_workers=5)as ex:
 for i,n,a in ex.map(fetch,spec):print(i,n,json.dumps(a),flush=True)
