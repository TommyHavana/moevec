"""Read-only, bounded public audit. No forms submitted or external state changed."""
import concurrent.futures, json, re, sys, time, urllib.request, urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime, timezone
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
from importlib import util
spec=util.spec_from_file_location('seo',Path(__file__).resolve().parents[2]/'scripts/audit-seo-public.py')
seo=util.module_from_spec(spec);spec.loader.exec_module(seo)
root=Path(__file__).resolve().parents[2];out=Path(__file__).resolve().parent
origin='https://moevec.org'
def fetch(url):
    started=time.monotonic()
    try:
        response=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'MEE-Project-Audit/1.0'}),timeout=30)
    except urllib.error.HTTPError as e: response=e
    body=response.read().decode('utf-8',errors='replace')
    return response.status,response.geturl(),body,dict(response.headers),round(time.monotonic()-started,3)
def inspect(url):
    try:
        status,final,html,headers,seconds=fetch(url);p=seo.Page(html)
        graph=[]
        for schema in p.schemas:graph+=schema.get('@graph',[schema])
        return {'url':url,'final':final,'status':status,'seconds_single_request':seconds,'html_bytes':len(html.encode()),'h1':p.h1s,'title':p.titles,'description':p.meta.get('description',[]),'canonical':p.canonicals,'robots':p.meta.get('robots',[]),'og_image':p.meta.get('og:image',[]),'social_profile_links':[l for l in p.links if re.search(r'(?:facebook\.com|instagram\.com|youtube\.com|tiktok\.com|linkedin\.com|x\.com|bsky\.app)',l)],'article_links':sorted(set(l for l in p.links if l.startswith(origin+'/blog/') and l.rstrip('/').count('/')==4)),'time_elements':len(re.findall(r'<time\b',html)),'schema_dates':[{'type':n.get('@type'),'published':n.get('datePublished'),'modified':n.get('dateModified')} for n in graph if n.get('datePublished')],'security_headers':{k:v for k,v in headers.items() if k.lower() in ['strict-transport-security','x-content-type-options','x-frame-options','content-security-policy','content-security-policy-report-only','referrer-policy','permissions-policy','cache-control']},'missing_alt':sum('alt' not in i for i in p.images),'external_script_domains':sorted(set(re.findall(r'<script[^>]+src=[\"\'](https?://[^/]+)',html))),'visible_sample_reference':'entradas de muestra' in html,'links':p.links}
    except Exception as e:return {'url':url,'error':str(e)}
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
main=[x.text for x in ET.fromstring(fetch(origin+'/sitemap.xml')[2]).findall('.//s:url/s:loc',ns)]
snapshot=json.loads((root/'inventario/rutas-seo-2026-11-05/seo-database-final.json').read_text())
sampleids=['E1.2.06','E2.3.04','E3.3.01','E4.12.04','E5.1.01','E6.6.02','E7.9.13','E1.4.08','E7.6.08']
articles=[e['url'] for e in snapshot['entries'] if e['id'] in sampleids]
categories=[]
for page in (1,2):categories+=json.loads(fetch(origin+f'/blog/wp-json/wp/v2/categories?per_page=100&page={page}&hide_empty=false')[2])
paths=main+[origin+'/blog/']+articles+[c['link'] for c in categories]+[origin+'/blog/?s=responsabilidad',origin+'/blog/?s=zzzxxyyauditnone',origin+'/no-existe-auditoria-mee-20261105/',origin+'/blog/wp-sitemap.xml']
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(inspect,paths))
report={'checked_at':datetime.now(timezone.utc).isoformat(),'scope':'18 main pages, 9 article sample, all122 category archives, blog, two searches,404,legacy sitemap','total_requests':len(paths),'categories':[{'id':c['id'],'name':c['name'],'count':c['count'],'parent':c['parent'],'url':c['link']} for c in categories],'pages':rows}
(out/'public-current.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'requests':len(rows),'http_status_counts':{s:sum(r.get('status')==s for r in rows) for s in {r.get('status') for r in rows}},'errors':[r for r in rows if r.get('error')],'categories':len(categories),'zero_direct_posts':sum(c['count']==0 for c in categories),'main_og_images':{r['url']:r.get('og_image') for r in rows if r['url'] in main}},ensure_ascii=False,indent=2))
