# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.8.13', 'gaceta73-oficial-intento', 'https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-o73.pdf'), ('E4.8.13', 'gaceta73-reproduccion', 'https://www.directoriocubano.com/wp-content/uploads/dc-gaceta/archive/pdf/2026/09/ordinaria/073/gaceta.pdf'), ('E4.8.13', 'wipo-gi', 'https://www.wipo.int/en/web/geographical-indications'), ('E4.8.13', 'wipo-cuba228', 'https://wipolex-res.wipo.int/edocs/lexdocs/laws/es/cu/cu003es.html'), ('E4.8.13', 'atlas-about', 'https://growthlab.hks.harvard.edu/atlas-economic-complexity'), ('E4.8.14', 'shenkar-hbr-ficha', 'https://store.hbr.org/product/imitation-is-more-valuable-than-innovation/F1004F'), ('E4.8.14', 'wipo-copyright', 'https://www.wipo.int/en/web/copyright/protection'), ('E4.8.14', 'wipo-types', 'https://www.wipo.int/en/web/about-ip'), ('E4.8.15', 'bain-loyalty1996', 'https://www.bain.com/insights/the-loyalty-effect/'), ('E4.8.15', 'reichheld2019', 'https://www.bain.com/insights/being-loyal-to-loyalty/'), ('E4.8.15', 'mee-price', 'https://moevec.org/blog/precio-por-valor/')]
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
