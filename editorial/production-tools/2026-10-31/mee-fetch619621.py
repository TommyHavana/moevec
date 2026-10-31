# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.10.04','simon-cmu-catalog','https://digitalcollections.library.cmu.edu/node/37574'),('E4.10.04','newport-publisher2016','https://www.hachettebookgroup.com/titles/cal-newport/deep-work/9781455586660/'),('E4.10.04','eu-guidelines-minors2025','https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-protection-minors'),('E4.10.05','zhu-oup2018','https://doi.org/10.1093/jcr/ucy008'),('E4.10.06','bready-methodology-current','https://www.worldbank.org/en/businessready/methodology'),('E4.10.06','bready-handbook2026','https://thedocs.worldbank.org/en/doc/6364c306d685203c859c60a075df5c3a-0540012026/original/B-READY-MH-2026.pdf'),('E4.10.06','bready-faq-current','https://www.worldbank.org/en/businessready/about-us/faq'),('E4.10.06','enterprise-regulation-tax','https://www.enterprisesurveys.org/en/data/exploretopics/regulations-and-taxes')]
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
