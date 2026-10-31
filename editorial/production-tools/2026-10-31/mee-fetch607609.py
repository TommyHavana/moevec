# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.9.07', 'indec-ipc-page', 'https://www.indec.gob.ar/indec/web/Nivel4-Tema-3-5-31'), ('E4.9.07', 'bcra-bands-current', 'https://www.bcra.gob.ar/regimen-de-bandas-cambiarias/'), ('E4.9.07', 'bcra-programme2026', 'https://www.bcra.gob.ar/noticias/profundizacion-del-esquema-de-agregados-monetarios-fase-de-re-monetizacion-2026/'), ('E4.9.07', 'bcra-substitution-paper', 'https://www.bcra.gob.ar/Pdfs/PublicacionesEstadisticas/proximosEnsayos/Sustitucion-de-monedas-y-efecto-histeresis-una-aplicacion-empirica-para-Argentina.pdf'), ('E4.9.08', 'wb-unmasking-paper', 'https://documents1.worldbank.org/curated/en/399751602248069405/pdf/Unmasking-the-Impact-of-COVID-19-on-Businesses-Firm-Level-Evidence-from-Across-the-World.pdf'), ('E4.9.08', 'bartik-pnas-page', 'https://www.pnas.org/doi/10.1073/pnas.2006991117'), ('E4.9.08', 'bartik-uchicago-attempt', 'https://knowledge.uchicago.edu/record/9615/files/bartik-et-al-2020-the-impact-of-covid-19-on-small-business-outcomes-and-expectations.pdf'), ('E4.9.08', 'imf-digital-resilience2022', 'https://www.elibrary.imf.org/view/journals/001/2022/034/article-A001-en.xml'), ('E4.9.08', 'wb-eastasia2023', 'https://www.worldbank.org/en/events/2023/07/11/crisis-and-recovery-learning-from-covid-19-s-economic-impact-and-policy-responses-in-east-asia-report-launch'), ('E4.9.09', 'naic-homeowners', 'https://content.naic.org/consumer/homeowners-insurance.htm'), ('E4.9.09', 'cfpb-emergency-fund', 'https://www.consumerfinance.gov/an-essential-guide-to-building-an-emergency-fund/'), ('E4.9.09', 'mee-e4-3-08', 'https://moevec.org/blog/seguros-para-emprendedores/'), ('E4.9.09', 'mee-e4-3-14', 'https://moevec.org/blog/fondo-de-emergencia/'), ('E4.9.09', 'mee-e2-6-15', '')]
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
