# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.8.07', 'kaizen-definition', 'https://kaizen.com/what-is-kaizen/'), ('E4.8.07', 'christensen-disruption', 'https://www.christenseninstitute.org/theory/disruptive-innovation/'), ('E4.8.08', 'desoto-publisher', 'https://www.hachettebookgroup.com/titles/hernando-de-soto/the-other-path/9780465016105/'), ('E4.8.08', 'ilo-regional2025', 'https://www.ilo.org/publications/innovative-approaches-promoting-transition-formality-latin-america-and'), ('E4.8.08', 'ilo-r204', 'https://wwwex.ilo.org/dyn/f?p=NORMLEXPUB:12100:0::NO::P12100_INSTRUMENT_ID:3243110'), ('E4.8.09', 'simon-publisher', 'https://link.springer.com/book/10.1007/978-3-319-20400-0'), ('E4.8.09', 'simon-kucher-value', 'https://www.simon-kucher.com/en/consulting/commercial-strategy-pricing-consulting/pricing-strategy-revenue-management/value-based-pricing')]
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
