#!/usr/bin/env python3
"""Check every published article against the live WordPress metadata snapshot."""
import concurrent.futures
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.h1s=[]; self.h1=None; self.titles=[]; self.title=None
        self.meta={}; self.canonicals=[]; self.images=[]; self.schemas=[]; self.schema=None
        self.links=[]; self.feed(html)
    def handle_starttag(self, tag, pairs):
        attrs=dict(pairs)
        if tag=='h1': self.h1=''
        if tag=='title': self.title=''
        if tag=='meta': self.meta.setdefault(attrs.get('name',attrs.get('property','')),[]).append(attrs.get('content',''))
        if tag=='link' and attrs.get('rel')=='canonical': self.canonicals.append(attrs.get('href'))
        if tag=='img': self.images.append(attrs)
        if tag=='a': self.links.append(attrs.get('href',''))
        if tag=='script' and attrs.get('type')=='application/ld+json': self.schema=''
    def handle_data(self, value):
        if self.h1 is not None: self.h1+=value
        if self.title is not None: self.title+=value
        if self.schema is not None: self.schema+=value
    def handle_endtag(self, tag):
        if tag=='h1' and self.h1 is not None: self.h1s.append(self.h1.strip()); self.h1=None
        if tag=='title' and self.title is not None: self.titles.append(self.title.strip()); self.title=None
        if tag=='script' and self.schema is not None:
            try: self.schemas.append(json.loads(self.schema))
            except json.JSONDecodeError: self.schemas.append({'invalid':True})
            self.schema=None

def fetch(url):
    request=urllib.request.Request(url,headers={'User-Agent':'MEE-SEO-Verification/1.0'})
    with urllib.request.urlopen(request,timeout=45) as response:
        return response.status,response.geturl(),response.read().decode('utf-8'),dict(response.headers)

def check(entry):
    issues=[]
    try:
        status,url,html,headers=fetch(entry['url']); page=Page(html)
        if status!=200 or url!=entry['url']: issues.append('HTTP/redirect')
        if len(page.h1s)!=1 or page.h1s[0].rstrip('.')!=entry['title'].rstrip('.'): issues.append('H1')
        if page.titles!=[entry['seo_title']]: issues.append('SEO title')
        if page.meta.get('description')!=[entry['description']]: issues.append('description')
        if page.canonicals!=[entry['url']]: issues.append('canonical')
        if len(page.meta.get('robots',[]))!=1 or 'noindex' in page.meta['robots'][0] or 'noindex' in headers.get('X-Robots-Tag',''): issues.append('robots')
        graph=[]
        for schema in page.schemas: graph+=schema.get('@graph',[schema])
        articles=[node for node in graph if node.get('@type')=='Article']
        if len(articles)!=1 or articles[0].get('headline')!=entry['title']: issues.append('Article schema')
        elif set(articles[0].get('image',[]))!={image['url'] for image in entry['images']}: issues.append('schema images')
        for image in entry['images']:
            # WordPress serves the existing 1024px interior derivatives, while
            # schema refers to their 1600px originals. Both belong to the same image.
            image_url=re.compile(re.escape(image['url'][:-5])+r'(?:-\d+x\d+)?\.webp$')
            match=[img for img in page.images if image_url.fullmatch(img.get('src',''))]
            if not match or match[0].get('alt')!=image['alt']: issues.append('image/alt '+image['role'])
            elif match:
                request=urllib.request.Request(match[0]['src'],method='HEAD',headers={'User-Agent':'MEE-SEO-Verification/1.0'})
                with urllib.request.urlopen(request,timeout=30) as response:
                    if response.status!=200 or 'image/webp' not in response.headers.get('Content-Type',''): issues.append('image HTTP '+image['role'])
        if not any('/empieza-aqui/' in link for link in page.links): issues.append('reading hub link')
        if 'mee-article-toc' not in html: issues.append('heading TOC')
        return {'id':entry['id'],'url':entry['url'],'status':status,'issues':issues}
    except Exception as error: return {'id':entry['id'],'url':entry['url'],'issues':[str(error)]}

if __name__=='__main__':
    snapshot=json.loads(Path(sys.argv[1]).read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        rows=list(pool.map(check,snapshot['entries']))
    namespaces={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    index=ET.fromstring(fetch('https://moevec.org/blog/sitemap_index.xml')[2])
    maps=[loc.text for loc in index.findall('.//s:sitemap/s:loc',namespaces)]
    posts=[]; image_count=0
    for url in maps:
        if '/post-sitemap' not in url: continue
        tree=ET.fromstring(fetch(url)[2])
        posts += [loc.text for loc in tree.findall('.//s:url/s:loc',namespaces)]
        image_count+=len(tree.findall('.//{http://www.google.com/schemas/sitemap-image/1.1}image'))
    expected={entry['url'] for entry in snapshot['entries']}
    # Rank Math includes the blog landing URL in its first post sitemap.
    landing='https://moevec.org/blog/'
    article_posts=[url for url in posts if url!=landing]
    root=ET.fromstring(fetch('https://moevec.org/sitemap.xml')[2])
    main_urls=[loc.text for loc in root.findall('.//s:url/s:loc',namespaces)]
    main=[]
    for url in main_urls:
        status,final,html,_=fetch(url);p=Page(html)
        main.append({'url':url,'status':status,'h1':len(p.h1s),'descriptions':len(p.meta.get('description',[])),'canonicals':p.canonicals,'issues':[] if status==200 and len(p.h1s)==1 and len(p.meta.get('description',[]))==1 and p.canonicals==[url] else ['main page SEO']})
    result={'checked_at':datetime.now(timezone.utc).isoformat(),'article_count':len(rows),'articles_ok':sum(not row['issues'] for row in rows),'article_errors':[row for row in rows if row['issues']],'wordpress_sitemaps':maps,'sitemap_article_count':len(article_posts),'sitemap_unique_articles':len(set(article_posts)),'blog_landing_in_sitemap':landing in posts,'missing_from_sitemap':sorted(expected-set(article_posts)),'unexpected_sitemap_posts':sorted(set(article_posts)-expected),'sitemap_image_entries':image_count,'main_pages':main}
    Path(sys.argv[2]).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({key:value for key,value in result.items() if key not in ['main_pages','wordpress_sitemaps']},ensure_ascii=False))
    sys.exit(0 if not result['article_errors'] and set(article_posts)==expected and len(article_posts)==840 and not any(row['issues']for row in main) else 2)
