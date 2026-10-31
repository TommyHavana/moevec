# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.8.13', 'atlas-primary-release', 'https://growthlab.hks.harvard.edu/news/atlas-economic-complexity-100-brings-new-data-and-product-space-design/'), ('E4.8.13', 'wipo-gi-faq', 'https://www.wipo.int/en/web/geographical-indications/faq_geographicalindications'), ('E4.8.14', 'wipo-patents', 'https://www.wipo.int/en/web/patents'), ('E4.8.14', 'wipo-patent-faq', 'https://www.wipo.int/en/web/patents/faq_patents'), ('E4.8.14', 'mee-ip', 'https://moevec.org/blog/propiedad-intelectual-debate-liberal/'), ('E4.8.15', 'bain-book1996', 'https://www.bain.com/insights/books/the-loyalty-effect/')]
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
