#!/usr/bin/env python3
"""Focused acceptance checks for public routes and the completed numbered editorial entries."""
import concurrent.futures,json,urllib.request,urllib.error
from html.parser import HTMLParser
from pathlib import Path
class Page(HTMLParser):
 def __init__(self):super().__init__();self.h1=0;self.meta={};self.canonical=[];self.ids=set();self.images=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if a.get('id'):self.ids.add(a['id'])
  if tag=='meta':self.meta[a.get('name',a.get('property',''))]=a.get('content','')
  if tag=='link'and a.get('rel')=='canonical':self.canonical.append(a.get('href'))
  if tag=='img':self.images.append(a.get('src',''))
origin='https://moevec.org'
topics=json.loads(Path('content/visuals.json').read_text())
public=['/','/contacto/','/sobre-mee/','/privacidad/','/aviso-legal/']+list(dict.fromkeys('/areas/'+t['area']+'/'for t in topics))
snapshot=json.loads(Path('inventario/plan-editorial-840-status.json').read_text())
articles=[r['url'].removeprefix(origin)for r in snapshot['entries']if r['status']=='terminada']
paths=public+['/blog/']+articles
def check(path):
 try:
  r=urllib.request.urlopen(origin+path,timeout=20);page=Page();page.feed(r.read().decode());issues=[]
  if page.h1!=1:issues.append('h1 count '+str(page.h1))
  if page.canonical!=[origin+path]:issues.append('canonical '+str(page.canonical))
  for meta in ['description','og:title','og:description','og:image','og:url','twitter:card']:
   if not page.meta.get(meta):issues.append('missing '+meta)
  if path in articles and'noindex'in page.meta.get('robots',''):issues.append('completed article noindex')
  if path in public and'noindex'in page.meta.get('robots',''):issues.append('public page noindex')
  if path.startswith('/areas/'):
   area=path.split('/')[2]
   for t in topics:
    if t['area']==area and t['slug']not in page.ids:issues.append('missing anchor '+t['slug'])
  return {'path':path,'status':r.status,'h1':page.h1,'issues':issues}
 except Exception as e:return {'path':path,'issues':[str(e)]}
with concurrent.futures.ThreadPoolExecutor(max_workers=6)as pool:results=list(pool.map(check,paths))
report={'routes':len(paths),'public_routes':len(public),'completed_articles':len(articles),'failures':[r for r in results if r['issues']],'results':results}
Path('inventario/auditoria-2026-10-28/editorial-route-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items()if k!='results'},ensure_ascii=False,indent=2))
