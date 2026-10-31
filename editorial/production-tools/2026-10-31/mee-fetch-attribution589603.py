# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.8.05', 'sba-marketing-attribution', 'https://www.sba.gov/counseling/manage-your-business/#marketing-sales'), ('E4.8.06', 'sba-market-attribution', 'https://www.sba.gov/counseling/plan-your-business/#market-research'), ('E4.8.09', 'oecd-consumer-attribution', 'https://www.oecd.org/en/topics/consumer-policy-and-digital-technologies.html'), ('E4.8.10', 'hbs-positioning-attribution', 'https://www.isc.hbs.edu/strategy/business-strategy/Pages/strategic-positioning.aspx'), ('E4.9.01', 'worldbank-social-protection-attribution', 'https://www.worldbank.org/en/topic/socialprotectionandjobs/publication/state-of-social-protection-2025-2-billion-person-challenge'), ('E4.9.02', 'newport-focus-attribution', 'https://calnewport.com/the-tao-of-cal/')]
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
