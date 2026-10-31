# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.10.07','nature-fourday2025','https://www.nature.com/articles/s41562-025-02259-6'),('E4.10.07','oecd-hours-current','https://www.oecd.org/es/data/indicators/hours-worked.html'),('E4.10.07','oecd-productivity-current','https://www.oecd.org/en/data/indicators/gdp-per-hour-worked.html'),('E4.10.07','owid-working-hours','https://ourworldindata.org/working-hours'),('E4.10.08','kornai-publications','https://www.kornai-janos.hu/en/publications/'),('E4.10.08','kornai-2012-primary','https://www.kornai-janos.hu/media/konyvek_cikkek/w20825/Kornai2012_ActaOeconomica.pdf'),('E4.10.08','cibercuba-une20251001','https://www.cibercuba.com/noticias/2025-10-01-u1-e207888-s27061-nid312087-cuba-inicia-octubre-apagones-masivos-deficit-casi'),('E4.10.08','une-home-access','https://www.unionelectrica.cu/'),('E4.10.09','gds-service-standard3','https://www.gov.uk/service-manual/service-standard/point-3-join-up-across-channels'),('E4.10.09','mee-sistemas','https://moevec.org/blog/sistemas-para-tu-negocio/')]
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
