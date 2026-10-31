# -*- coding: utf-8 -*-
from pathlib import Path
from html.parser import HTMLParser
import urllib.request,json,sys,concurrent.futures
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');start,end=map(int,sys.argv[1:3]);rows=[x for x in json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json'))if start<=x['number']<=end]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.in_title=False;self.titles=[];self.descriptions=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='title':self.in_title=True;self.titles.append('')
  if tag=='meta'and a.get('name')=='description':self.descriptions.append(a.get('content'))
 def handle_endtag(self,tag):
  if tag=='title':self.in_title=False
 def handle_data(self,data):
  if self.in_title:self.titles[-1]+=data
def verify(row):
 d=r/'editorial/articles'/row['id'];a=json.load(open(d/'article.json'));pub=json.load(open(d/'publication.json'))
 with urllib.request.urlopen(pub['url'],timeout=40)as f:text=f.read().decode()
 p=Page();p.feed(text);out=dict(id=row['id'],url=pub['url'],titles=p.titles,descriptions=p.descriptions,title_matches=p.titles==[a['seo_title']],description_matches=bool(p.descriptions)and all(x==a['description']for x in p.descriptions),description_tag_count=len(p.descriptions),warnings=['Duplicate identical description meta tags; template change outside authorized editorial scope']if len(p.descriptions)>1 else[]);assert out['title_matches']and out['description_matches'],out;return out
with concurrent.futures.ThreadPoolExecutor(max_workers=3)as ex:out=list(ex.map(verify,rows))
(r/f'inventario/auditoria-2026-10-28/editorial-{start}-{end}-seo.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False))
