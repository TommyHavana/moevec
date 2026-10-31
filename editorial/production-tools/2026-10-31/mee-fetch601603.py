# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.9.01', 'findex-report-page', 'https://www.worldbank.org/en/publication/globalfindex/report'), ('E4.9.01', 'findex-report2025', 'https://openknowledge.worldbank.org/bitstreams/9288bdc5-7a9b-42de-a47c-3746fd68f22a/download'), ('E4.9.01', 'cfpb-emergency', 'https://www.consumerfinance.gov/an-essential-guide-to-building-an-emergency-fund/'), ('E4.9.01', 'mee-fund', 'https://moevec.org/blog/fondo-de-emergencia/'), ('E4.9.02', 'mee-diversification', 'https://moevec.org/blog/diversificacion-personal/'), ('E4.9.02', 'mee-side-project', 'https://moevec.org/blog/proyecto-paralelo-trabajar-de-dia/'), ('E4.9.02', 'cfpb-emergency', 'https://www.consumerfinance.gov/an-essential-guide-to-building-an-emergency-fund/'), ('E4.9.03', 'house-debt-publisher', 'https://press.uchicago.edu/ucp/books/book/chicago/H/bo20832545.html'), ('E4.9.03', 'house-debt-excerpt', 'https://press.uchicago.edu/books/excerpt/2014/Mian-Sufi_House_of_Debt.html'), ('E4.9.03', 'mee-debt', 'https://moevec.org/blog/autonomia-y-deuda/')]
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
