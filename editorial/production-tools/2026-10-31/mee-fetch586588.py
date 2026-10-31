from pathlib import Path
from datetime import datetime,timezone
import urllib.request,concurrent.futures,json,re,html,hashlib
base=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
spec=[('E4.8.01','porter-isc','https://www.isc.hbs.edu/strategy/business-strategy/Pages/strategic-positioning.aspx'),('E4.8.01','porter-strategy-publisher','https://www.simonandschuster.com/books/Competitive-Strategy/Michael-E-Porter/9780684841489'),('E4.8.01','porter-advantage-publisher','https://www.simonandschuster.com/books/Competitive-Advantage/Michael-E-Porter/9780684841465'),('E4.8.02','strategyzer-canvas','https://www.strategyzer.com/library/the-value-proposition-canvas'),('E4.8.02','strategyzer-testing','https://www.strategyzer.com/library/roadmap-to-test-your-value-proposition'),('E4.8.02','christensen-jtbd','https://www.christenseninstitute.org/theory/jobs-to-be-done/'),('E4.8.03','blue-ocean-definition','https://www.blueoceanstrategy.com/what-is-blue-ocean-strategy/'),('E4.8.03','blue-ocean-actions','https://www.blueoceanstrategy.com/tools/four-actions-framework/'),('E4.8.03','blue-ocean-cirque','https://www.blueoceanstrategy.com/blue-ocean-strategy-examples/cirque-du-soleil/')]
def fetch(x):
 i,n,u=x;d=base/i/'sources';a=dict(url=u,accessed_at=datetime.now(timezone.utc).isoformat())
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40)as f:b=f.read();a.update(status=f.status,final_url=f.url,content_type=f.headers.get('Content-Type'))
  (d/(n+'.html')).write_bytes(b);a.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest());t=b.decode('utf-8','replace');t=re.sub(r'<(script|style|nav|header|footer)\b.*?</\1>','',t,flags=re.S|re.I);t=html.unescape(re.sub('<[^>]+>',' ',t));t=re.sub(r'\s+',' ',t);(d/(n+'.txt')).write_text(t);a['text_file']=n+'.txt'
 except Exception as e:a['error']=str(e)
 (d/(n+'-access.json')).write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n');return i,n,a
with concurrent.futures.ThreadPoolExecutor(max_workers=5)as ex:
 for i,n,a in ex.map(fetch,spec):print(i,n,json.dumps(a),flush=True)
