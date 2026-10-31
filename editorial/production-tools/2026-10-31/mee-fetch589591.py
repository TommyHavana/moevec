from pathlib import Path
from datetime import datetime, timezone
import urllib.request, concurrent.futures, json, re, html, hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[
('E4.8.04','anderson-publisher','https://www.hachettebookgroup.com/titles/chris-anderson/the-long-tail/9781401309664/'),
('E4.8.04','sba-market','https://www.sba.gov/business-guide/plan-your-business/market-research-competitive-analysis'),
('E4.8.05','reichheld-book','https://www.bain.com/insights/books/the-loyalty-effect/'),
('E4.8.05','reichheld-principles','https://www.netpromotersystem.com/insights/being-loyal-to-loyalty-nps-linkedin/'),
('E4.8.06','oepm-before','https://www.oepm.es/es/marcas-y-nombres-comerciales/tramitar-una-solicitud-de-marca-o-nombre-comercial/que-hacer-antes-de-tramitar/'),
('E4.8.06','oepm-national','https://administracion.gob.es/tu-espacio-europeo/derechos-obligaciones/empresas/inicio-gestion-cierre/derechos/patentes-marcas/nombre-comercial'),
('E4.8.06','europa-trademarks','https://europa.eu/youreurope/business/growing/protecting-intellectual-property/trade-marks/index_es.htm'),
('E4.8.06','europa-faq','https://intellectual-property-helpdesk.ec.europa.eu/regional-ip-helpdesks/european-ip-helpdesk/europe-frequently-asked-questions_en'),
('E4.8.06','impi-faq','https://pase.impi.gob.mx/Faqs/PreguntasFrecuentes.pdf')]
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
