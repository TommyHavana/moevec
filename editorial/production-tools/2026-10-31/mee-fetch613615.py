# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.9.13', 'banrep-basic-current', 'https://www.banrep.gov.co/es/politica-monetaria-cambiaria/regulacion-operaciones-cambiarias/conceptos-basicos'), ('E4.9.13', 'mexico-isr-current', 'https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf'), ('E4.9.13', 'imf-areaer-overview', 'https://www.imf.org/en/publications/sprolls/annual-report-on-exchange-arrangements-and-exchange-restrictions'), ('E4.9.14', 'boe-insolvency-current', 'https://www.boe.es/eli/es/rdlg/2020/05/05/1/con'), ('E4.9.14', 'boe-reform2022', 'https://www.boe.es/eli/es/l/2022/09/05/16'), ('E4.9.14', 'armour-cumming2008', 'https://doi.org/10.1093/aler/ahn008'), ('E4.9.15', 'iso22301-overview', 'https://www.iso.org/standard/75106.html?frame=0'), ('E4.9.15', 'iso22301-brochure', 'https://www.iso.org/files/live/sites/isoorg/files/store/en/PUB100442.pdf'), ('E4.9.15', 'utah-business-plan', 'https://beready.utah.gov/business/bcp/'), ('E4.9.15', 'redcross-exercise', 'https://www.readyrating.org/resource-center/training-and-exercises/business-continuity-exercise-plan-template')]
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
