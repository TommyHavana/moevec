from pathlib import Path
import json,re,urllib.request,concurrent.futures,importlib.util,html,sys
start,end=map(int,sys.argv[1:3]);r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');reg=json.load(open(r/'inventario/plan-editorial-840-status.json'));rows=[x for x in reg['entries']if start<=x['number']<=end];spec=importlib.util.spec_from_file_location('v',r/'scripts/verify-editorial-publication.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
def get(u):
 with urllib.request.urlopen(u,timeout=40)as f:return f.status,f.read().decode()
_,sx=get('https://moevec.org/blog/wp-sitemap.xml')
parts=[html.unescape(u)for u in re.findall(r'<loc>([^<]+)</loc>',sx)if 'posts-post-'in u];assert parts;sx+=''.join(get(u)[1]for u in parts);out=[]
for row in rows:
 i=row['id'];d=r/'editorial/articles'/i;p=json.load(open(d/'publication.json'));_,h=get(p['url']);page=v.Page();page.feed(h);schemas=[json.loads(x)for x in page.schemas];crumb=[]
 def walk(x):
  if isinstance(x,dict):
   if x.get('@type')=='BreadcrumbList':crumb.extend(x.get('itemListElement',[]))
   for y in x.values():walk(y)
  elif isinstance(x,list):
   for y in x:walk(y)
 walk(schemas);names=[(x.get('name') or (x['item'].get('name') if isinstance(x.get('item'),dict) else x.get('item')))for x in crumb];assert names[:4]==['Inicio','Blog','Trabajo',row['topic_name']],names
 urls=sorted(set(html.unescape(u)for u in re.findall('href="([^"]+)"',(d/'article.html').read_text())if u.startswith('https://moevec.org')))
 with concurrent.futures.ThreadPoolExecutor(max_workers=5)as ex:links=[dict(url=u,status=s[0])for u,s in zip(urls,ex.map(get,urls))]
 assert all(x['status']==200 for x in links);hierarchy=all(x in h for x in ['Trabajo',row['topic_name']]);assert hierarchy and(html.escape(p['url'])in sx or p['url']in sx)
 out.append(dict(id=i,url=p['url'],visible_hierarchy=hierarchy,breadcrumb_names=names,in_sitemap=True,internal_links=links))
p=r/f'inventario/auditoria-2026-10-28/editorial-{start}-{end}-navigation.json';p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False))
