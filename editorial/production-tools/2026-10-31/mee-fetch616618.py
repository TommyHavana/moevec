# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.10.01', 'burkeman-publisher2021', 'https://us.macmillan.com/books/9780374715243/fourthousandweeks/'), ('E4.10.01', 'seneca-latin-text', 'https://www.thelatinlibrary.com/sen/sen.brevita.shtml'), ('E4.10.01', 'newport-publisher2016', 'https://www.hachettebookgroup.com/titles/cal-newport/deep-work/9781455586660/'), ('E4.10.02', 'whillans-pnas2017', 'https://www.pnas.org/doi/10.1073/pnas.1706541114'), ('E4.10.03', 'parkinson-economist-attempt', 'https://www.economist.com/news/1955/11/19/parkinsons-law'), ('E4.10.03', 'amabile-pubmed2002', 'https://pubmed.ncbi.nlm.nih.gov/12195920/'), ('E4.10.03', 'amabile-harvard2011', 'https://www.library.hbs.edu/working-knowledge/how-small-wins-unleash-creativity')]
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
