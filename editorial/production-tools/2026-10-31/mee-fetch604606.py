# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.9.04', 'bonanno-publisher2019', 'https://www.hachettebookgroup.com/titles/george-a-bonanno/the-other-side-of-sadness/9781541699427/'), ('E4.9.04', 'bonanno-original-bibliography', 'https://www.tc.columbia.edu/articles/2013/june/george-bonanno/'), ('E4.9.04', 'who-mental-report2022', 'https://www.who.int/publications-detail-redirect/9789240049338/'), ('E4.9.04', 'who-stress2026', 'https://www.who.int/news-room/questions-and-answers/item/stress'), ('E4.9.05', 'fergusson-publisher2010', 'https://www.hachettebookgroup.com/titles/adam-fergusson/when-money-dies/9781586489946/'), ('E4.9.05', 'imf-zimbabwe-land2020', 'https://www.elibrary.imf.org/view/journals/002/2020/082/article-A005-en.xml'), ('E4.9.05', 'imf-zimbabwe-money2020', 'https://www.elibrary.imf.org/view/journals/002/2020/082/article-A004-en.xml'), ('E4.9.05', 'imf-venezuela2022', 'https://www.elibrary.imf.org/view/journals/087/2022/019/article-A001-en.xml'), ('E4.9.06', 'imf-venezuela2022', 'https://www.elibrary.imf.org/view/journals/087/2022/019/article-A001-en.xml'), ('E4.9.06', 'imf-nowcast2026', 'https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026020-source-pdf.pdf'), ('E4.9.06', 'encovi2024-page', 'https://www.proyectoencovi.com/encovi-2024'), ('E4.9.06', 'encovi2024-presentation', 'https://cdn.prod.website-files.com/5d14c6a5c4ad42a4e794d0f7/6803aeed2dfc5c19a4ac96cd_ENCOVI%202024_presentacio%CC%81n_integrada.pdf'), ('E4.9.06', 'encovi2024-technical', 'https://cdn.prod.website-files.com/5d14c6a5c4ad42a4e794d0f7/6a14bd96d60e55c930d7efae_ENCOVI%202024_Documento%20Te%CC%81cnico%20%281%29.pdf'), ('E4.9.06', 'bcv-consumer-attempt', 'https://www.bcv.org.ve/estadisticas/consumidor'), ('E4.9.06', 'bcv-expression-attempt', 'https://www.bcv.org.ve/billetes-y-monedas/nueva-expresion-monetaria'), ('E4.9.06', 'venezuela-un2021', 'https://gadebate.un.org/sites/default/files/gastatements/76/ve_es.pdf')]
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
