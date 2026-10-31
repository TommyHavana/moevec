# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.8.10', 'gladwell-publisher', 'https://www.hachettebookgroup.com/titles/malcolm-gladwell/david-and-goliath/9780316204361/'), ('E4.8.10', 'stigler-original', 'https://www.rasmusen.org/zg601/readings/Stigler.1971.pdf'), ('E4.8.10', 'oecd-regulation2025', 'https://www.oecd.org/en/publications/2025/12/oecd-economic-outlook-volume-2025-issue-2_413f7d0a/full-report/time-for-a-regulatory-reset_90ca6147.html'), ('E4.8.11', 'strategyzer-canvas', 'https://www.strategyzer.com/library/the-value-proposition-canvas'), ('E4.8.11', 'sba-market', 'https://www.sba.gov/counseling/plan-your-business/#market-research'), ('E4.8.12', 'sba-market', 'https://www.sba.gov/counseling/plan-your-business/#market-research'), ('E4.8.12', 'mee-case', 'https://moevec.org/blog/historial-profesional-para-clientes/'), ('E4.8.12', 'mee-niches', 'https://moevec.org/blog/nichos/')]
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
