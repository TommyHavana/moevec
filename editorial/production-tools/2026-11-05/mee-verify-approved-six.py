from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser
import base64, concurrent.futures, html, importlib.util, json, re, subprocess, sys, urllib.request

root=Path(__file__).resolve().parents[3]
changes=json.loads((root/'editorial/title-alternatives-approved-2026-11-05.json').read_text())['changes']
ids=[x['id']for x in changes]
block=sys.argv[1]
ids=ids[:3] if block=='1' else ids[3:] if block=='2' else ids
label='approved-six-block-'+block
audit=root/'inventario/auditoria-2026-10-28'
spec=importlib.util.spec_from_file_location('verify_editorial',root/'scripts/verify-editorial-publication.py')
verify=importlib.util.module_from_spec(spec);spec.loader.exec_module(verify)
with concurrent.futures.ThreadPoolExecutor(max_workers=3)as pool:
    basic=list(pool.map(verify.verify,ids))
assert all(not x['issues'] and x['images']==3 and x['status']==200 for x in basic),basic
plan=json.loads((root/'wordpress/plugins/mee-editorial/data/production-plan.json').read_text())
areas={x['area']:x['areaName']for x in json.loads((root/'wordpress/plugins/mee-editorial/data/topics.json').read_text())}
def get(url):
    with urllib.request.urlopen(url,timeout=40)as response:return response.status,response.read().decode()
_,sx=get('https://moevec.org/blog/wp-sitemap.xml')
parts=[html.unescape(u)for u in re.findall(r'<loc>([^<]+)</loc>',sx)if 'posts-post-'in u]
assert parts
sx+=''.join(get(u)[1]for u in parts)
class SEO(HTMLParser):
    def __init__(self):super().__init__();self.in_title=False;self.titles=[];self.descriptions=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='title':self.in_title=True;self.titles.append('')
        if tag=='meta'and a.get('name')=='description':self.descriptions.append(a.get('content'))
    def handle_endtag(self,tag):
        if tag=='title':self.in_title=False
    def handle_data(self,data):
        if self.in_title:self.titles[-1]+=data
reports=[]
for ident in ids:
    d=root/'editorial/articles'/ident;a=json.loads((d/'article.json').read_text());pub=json.loads((d/'publication.json').read_text())
    row=next(x for x in plan if x['id']==ident)
    status,body=get(pub['url']);page=verify.Page();page.feed(body);seo=SEO();seo.feed(body)
    schemas=[json.loads(s)for s in page.schemas];crumb=[];authors=[]
    def walk(value):
        if isinstance(value,dict):
            if value.get('@type')=='BreadcrumbList':crumb.extend(value.get('itemListElement',[]))
            if value.get('@type')in ['Article','BlogPosting']:authors.append(value.get('author'))
            for item in value.values():walk(item)
        elif isinstance(value,list):
            for item in value:walk(item)
    walk(schemas)
    names=[x.get('name')or(x['item'].get('name')if isinstance(x.get('item'),dict)else x.get('item'))for x in crumb]
    assert names[:4]==['Inicio','Blog',areas[row['area']],row['topic_name']],names
    assert all(x in body for x in [areas[row['area']],row['topic_name']])
    assert pub['url']in sx or html.escape(pub['url'])in sx
    assert seo.titles==[a['seo_title']]
    assert seo.descriptions and all(x==a['description']for x in seo.descriptions)
    # La plantilla identifica a Anacleto como firma editorial y al autor del
    # schema como la organización MEE; no se inventa una persona jurídica.
    assert 'Anacleto · firma editorial de MEE'in body
    assert any(isinstance(x,dict)and x.get('@type')=='Organization'and x.get('name')=='MEE · Editorial'for x in authors),authors
    urls=sorted(set(html.unescape(u)for u in re.findall('href="([^"]+)"',(d/'article.html').read_text())if u.startswith('https://moevec.org')))
    with concurrent.futures.ThreadPoolExecutor(max_workers=5)as pool:
        links=[dict(url=u,status=s[0])for u,s in zip(urls,pool.map(get,urls))]
    assert len(links)>=3 and all(x['status']==200 for x in links)
    reports.append(dict(id=ident,number=row['number'],url=pub['url'],status=status,title_matches=True,description_matches=True,
        description_tag_count=len(seo.descriptions),warnings=['Dos meta descripciones idénticas; incidencia de plantilla preexistente fuera del alcance editorial.']if len(seo.descriptions)>1 else[],
        visible_hierarchy=True,breadcrumb_names=names,in_sitemap=True,article_authors=authors,internal_links=links))
container=(Path('/tmp')/'mee-wp-container.txt').read_text().strip();assert re.fullmatch('[0-9a-f]+',container)
payload=[]
for ident in ids:
    row=next(x for x in plan if x['id']==ident)
    a=json.loads((root/'editorial/articles'/ident/'article.json').read_text())
    payload.append(dict(id=ident,number=row['number'],title=row['title'],slug=row['slug'],area=row['area'],topic=row['topic'],tags=a['tags']))
encoded=base64.b64encode(json.dumps(payload).encode()).decode()
php="""<?php require '/var/www/html/wp-load.php';$rows=json_decode(base64_decode('"""+encoded+"""'),true);$org=[];foreach($rows as$r){$posts=get_posts(['post_type'=>'post','post_status'=>['publish','draft','pending','future','private','trash'],'posts_per_page'=>-1,'meta_key'=>'_mee_plan_id','meta_value'=>$r['id']]);$p=count($posts)===1?$posts[0]:null;$cats=$p?wp_get_post_terms($p->ID,'category',['fields'=>'slugs']):[];$tags=$p?wp_get_post_terms($p->ID,'post_tag',['fields'=>'slugs']):[];$expected=[$r['area'],$r['topic']];$want=$r['tags'];sort($cats);sort($tags);sort($expected);sort($want);$parent=get_term_by('slug',$r['area'],'category');$child=get_term_by('slug',$r['topic'],'category');$ok=$p&&$p->post_status==='publish'&&$p->post_title===$r['title']&&$p->post_name===$r['slug']&&$cats===$expected&&$tags===$want&&$parent&&$child&&(int)$child->parent===(int)$parent->term_id&&get_post_meta($p->ID,'_mee_reviewed',true)==='1'&&get_post_meta($p->ID,'_mee_signature',true)==='Anacleto'&&(int)get_post_meta($p->ID,'_mee_plan_number',true)===(int)$r['number'];$org[]=['id'=>$r['id'],'post_id'=>$p?$p->ID:null,'categories'=>$cats,'tags'=>$tags,'ok'=>(bool)$ok];}$t=get_terms(['taxonomy'=>'category','hide_empty'=>false]);$taxonomy=['count'=>count($t),'roots'=>count(array_filter($t,fn($x)=>$x->parent==0)),'forbidden'=>array_values(array_filter(array_map(fn($x)=>$x->slug,$t),fn($x)=>in_array($x,['uncategorized','editorial'])))];echo json_encode(['organization'=>$org,'taxonomy'=>$taxonomy],JSON_UNESCAPED_UNICODE);"""
p=subprocess.run(['ssh','-o','BatchMode=yes','calicata-root',f'docker exec -i --user 33:33 {container} php'],input=php,text=True,capture_output=True,check=True)
organization_report=json.loads(p.stdout);org=organization_report['organization'];taxonomy=organization_report['taxonomy']
assert len(org)==len(ids)and all(x['ok']for x in org),org
assert taxonomy['count']==122 and taxonomy['roots']==7 and not taxonomy['forbidden']
report=dict(checked_at=datetime.now(timezone.utc).isoformat(),basic=basic,navigation_and_seo=reports,organization=org,taxonomy=taxonomy)
(audit/('editorial-'+label+'-verification.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verified=ids,images=len(ids)*3,issues=0,taxonomy=taxonomy,report=str(audit/('editorial-'+label+'-verification.json'))),ensure_ascii=False),flush=True)
