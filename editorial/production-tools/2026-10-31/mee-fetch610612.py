# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.9.10', 'sepe-contributiva-leaflet', 'https://www.sepe.es/dam/jcr%3A22e56e65-c269-4f04-96bd-3dc86daf8fc8/hoja_informativa_contributiva.pdf'), ('E4.9.10', 'boe-career-services2024', 'https://www.boe.es/buscar/act.php?id=BOE-A-2024-8710'), ('E4.9.11', 'cfpb-emergency-fund', 'https://www.consumerfinance.gov/an-essential-guide-to-building-an-emergency-fund/'), ('E4.9.12', 'yale-mcnamara2017', 'https://tri.yale.edu/tropical-resources/tropical-resources-vol-36/crisis-urban-agriculture-case-studies-cuba'), ('E4.9.12', 'yale-volume36', 'https://tri.yale.edu/publications/tropical-resources-bulletin/tri-bulletin-archive/tropical-resources-vol-36'), ('E4.9.12', 'cienfuegos-factors2025', 'https://remca.umet.edu.ec/index.php/REMCA/article/view/1015'), ('E4.9.10', 'mee-e4-2-05', 'https://moevec.org/blog/red-de-contactos-lazos-debiles/'), ('E4.9.11', 'mee-e1-1-15', 'https://moevec.org/blog/test-cuanta-autonomia-tienes/'), ('E4.9.12', 'mee-e3-4-08', 'https://moevec.org/blog/trueque-monedas-comunitarias/')]
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
