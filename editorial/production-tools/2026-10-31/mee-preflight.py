# -*- coding: utf-8 -*-
from pathlib import Path
import subprocess,json,hashlib,re,sys,base64
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');start,end=map(int,sys.argv[1:3]);plan=json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json'));rows=[x for x in plan if start<=x['number']<=end];payload=[]
for x in rows:
 a=json.load(open(r/'editorial/articles'/x['id']/'article.json'));assert all(a[k]==x[k]for k in ['id','number','title','slug']);payload.append(dict(id=x['id'],slug=x['slug'],keyword=a['keyword']))
c=subprocess.check_output(['ssh','-o','BatchMode=yes','calicata-root','docker ps -q --filter label=coolify.applicationUuid=h7kfs9qe620lg5mqip36npt4 --filter label=com.docker.compose.service=wordpress'],text=True).strip();assert re.fullmatch('[0-9a-f]+',c);Path('/tmp/mee-wp-container.txt').write_text(c)
raw=subprocess.check_output(['ssh','-o','BatchMode=yes','calicata-root',f'docker exec {c} cat /tmp/publish-editorial.php']);assert hashlib.sha256(raw).digest()==hashlib.sha256((r/'scripts/publish-editorial.php').read_bytes()).digest()
encoded=base64.b64encode(json.dumps(payload).encode()).decode()
php='''<?php require '/var/www/html/wp-load.php'; $rows=json_decode(base64_decode("'''+encoded+'''"),true);$out=[];$states=['publish','draft','pending','future','private','trash','inherit'];foreach($rows as$r){$posts=get_posts(['post_type'=>['post','attachment'],'post_status'=>$states,'posts_per_page'=>-1,'meta_key'=>'_mee_plan_id','meta_value'=>$r['id'],'fields'=>'ids']);$focus=get_posts(['post_type'=>'post','post_status'=>$states,'posts_per_page'=>-1,'meta_key'=>'_mee_focus_keyword','meta_value'=>$r['keyword'],'fields'=>'ids']);$slug=get_page_by_path($r['slug'],OBJECT,'post');$out[]=['id'=>$r['id'],'posts_and_media'=>$posts,'keyword_matches'=>$focus,'slug_occupied'=>(bool)$slug];}echo json_encode($out);'''
p=subprocess.run(['ssh','-o','BatchMode=yes','calicata-root',f'docker exec -i --user 33:33 {c} php'],input=php,text=True,capture_output=True,check=True);a=json.loads(p.stdout);assert len(a)==len(rows)and all(not x['posts_and_media']and not x['keyword_matches']and not x['slug_occupied']for x in a),a
(r/f'inventario/auditoria-2026-10-28/editorial-{start}-{end}-preflight.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n');print(json.dumps(a,ensure_ascii=False))
