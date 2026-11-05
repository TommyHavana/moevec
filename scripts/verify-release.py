#!/usr/bin/env python3
"""Bounded release gate; checks public HTML without submitting forms."""
import argparse,concurrent.futures,json,sys,urllib.request,urllib.error
from pathlib import Path
from urllib.parse import urlparse,unquote
import importlib.util
module_spec=importlib.util.spec_from_file_location('mee_seo',Path(__file__).with_name('audit-seo-public.py'))
module=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(module);Page=module.Page
ROOT=Path(__file__).resolve().parents[1]
ORIGIN='https://moevec.org'
def inspect(path,html,static=None,expected_canonical=None):
 p=Page(html);issues=[];error=path in ['/404.html','/404/','/_not-found/']
 if len(p.h1s)!=1:issues.append('one H1 required')
 if len(p.titles)!=1:issues.append('one title required')
 if not error and len(p.meta.get('description',[]))!=1:issues.append('one description required')
 if expected_canonical and p.canonicals!=[expected_canonical]:issues.append('canonical')
 robots=p.meta.get('robots',[])
 if error and (len(robots)!=1 or 'noindex' not in robots[0]):issues.append('404 needs one noindex')
 if not error and '?'not in path and any('noindex'in x for x in robots):issues.append('unexpected noindex')
 for node in p.schemas:
  if node.get('invalid'):issues.append('invalid schema JSON')
 if static:
  assets=[img.get('src','')for img in p.images]+p.meta.get('og:image',[])+p.meta.get('twitter:image',[])
  links=p.links
  for raw in assets+links:
   u=urlparse(raw)
   if u.netloc and u.netloc!='moevec.org':continue
   target=unquote(u.path)
   if not target.startswith('/')or target.startswith('/blog/'):continue
   f=static/target.lstrip('/')
   if not f.is_file()and not(f/'index.html').is_file():issues.append('missing destination '+target)
 return {'path':path,'issues':list(dict.fromkeys(issues))}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--static',type=Path);ap.add_argument('--live',action='store_true');ap.add_argument('--output',type=Path);a=ap.parse_args();rows=[]
 if a.static:
  for f in sorted(a.static.rglob('*.html')):
   if '_next'in f.parts or f.name.startswith('_'):continue
   rel=f.relative_to(a.static).as_posix();path='/'+rel.removesuffix('index.html')if rel.endswith('index.html')else'/'+rel
   rows.append(inspect(path,f.read_text(),a.static,None if path in ['/404.html','/404/','/_not-found/']else ORIGIN+path))
 if a.live:
  catalog=json.loads((ROOT/'wordpress/plugins/mee-editorial/data/article-discovery.json').read_text())
  paths=['/','/empieza-aqui/','/metodo-editorial/','/recursos/','/contacto/?tema=editorial','/seguir-mee/','/blog/','/blog/?s=presupuesto','/blog/category/politica-y-economia/','/blog/category/politica-y-economia/regulacion-financiera/']
  paths += [urlparse(catalog[k]['url']).path for k in ['E5.1.01','E1.2.06','E4.12.04','E7.9.13']]
  paths += ['/empieza-aqui/'+p['slug']+'/'for p in json.loads((ROOT/'wordpress/plugins/mee-editorial/data/reading-paths.json').read_text())]
  def fetch(path):
   try:
    with urllib.request.urlopen(urllib.request.Request(ORIGIN+path,headers={'User-Agent':'MEE-Release-Check/1.0'}),timeout=30)as res:
     html=res.read().decode();row=inspect(path,html,expected_canonical=None if'?'in path else ORIGIN+path)
     if path.startswith('/blog/') and not any(x in path for x in ['category/','?'])and path!='/blog/':
      p=Page(html)
      if len(p.images)<3:row['issues'].append('article images')
      if 'mee-editorial-dates'not in html:row['issues'].append('editorial dates')
     if'?s='in path and'noindex'not in html:row['issues'].append('search exclusion')
     return row
   except Exception as ex:return {'path':path,'issues':[str(ex)]}
  with concurrent.futures.ThreadPoolExecutor(max_workers=3)as pool:rows+=list(pool.map(fetch,paths))
 report={'checked':len(rows),'failures':[x for x in rows if x['issues']],'results':rows}
 if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items()if k!='results'},ensure_ascii=False,indent=2));return bool(report['failures'])
if __name__=='__main__':sys.exit(main())
