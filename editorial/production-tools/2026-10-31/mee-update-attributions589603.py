# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,re,tarfile,hashlib
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');base=r/'editorial/articles';out=r/'inventario/auditoria-2026-10-28';ids=json.load(open(out/'editorial-601-603-attribution-preparation.json'))['update_ids'];c=Path('/tmp/mee-wp-container.txt').read_text().strip();assert re.fullmatch('[0-9a-f]+',c)
def run(a,**kw):return subprocess.run(a,capture_output=True,text=True,check=True,**kw)
def wp(php):return run(['ssh','-o','BatchMode=yes','calicata-root',f'docker exec -i {c} php'],input=php).stdout
def snapshot():
 php="<?php require '/var/www/html/wp-load.php';$ids="+str(ids).replace('[','[').replace(']',']')+";$out=[];foreach($ids as$id){$p=get_posts(['post_type'=>'post','post_status'=>['publish','draft','pending','future','private','trash'],'meta_key'=>'_mee_plan_id','meta_value'=>$id,'posts_per_page'=>2]);if(count($p)!==1||$p[0]->post_status!=='publish')throw new RuntimeException('Unexpected post state');$p=$p[0];$a=get_posts(['post_type'=>'attachment','post_status'=>'inherit','post_parent'=>$p->ID,'meta_key'=>'_mee_plan_id','meta_value'=>$id,'posts_per_page'=>4,'fields'=>'ids']);sort($a);$out[$id]=['post_id'=>$p->ID,'content_sha256'=>hash('sha256',$p->post_content),'attachments'=>$a];}echo json_encode($out);"
 return json.loads(wp(php))
before=snapshot();assert all(len(x['attachments'])==3 for x in before.values());(out/'editorial-601-603-attribution-before.json').write_text(json.dumps(before,indent=2)+'\n')
remote='/data/mee-editorial-work/20261028'
run(['scp',str(r/'scripts/publish-editorial.php'),'calicata-root:'+remote+'/publish-editorial-reviewed-20261031.php'])
lint=run(['ssh','calicata-root',f'docker cp {remote}/publish-editorial-reviewed-20261031.php {c}:/tmp/publish-editorial-reviewed.php && docker exec {c} php -l /tmp/publish-editorial-reviewed.php']);assert'No syntax errors'in lint.stdout
bad=json.load(open(base/'E4.9.01/article.json'));bad['text_update']=dict(post_id=before['E4.9.01']['post_id'],expected_content_sha256='0'*64,reason='Verify rejection of stale content without mutation')
# Send manifest bytes via a literal base64 string, without shell interpolation.
import base64
encoded=base64.b64encode(json.dumps(bad,ensure_ascii=False).encode()).decode();wp("<?php file_put_contents('/tmp/mee-update-rejection.json',base64_decode('"+encoded+"')); ")
test=subprocess.run(['ssh','calicata-root',f'docker exec {c} php /tmp/publish-editorial-reviewed.php /tmp/mee-update-rejection.json --update-text'],capture_output=True,text=True);assert test.returncode!=0 and 'Contenido cambió desde la revisión'in test.stderr
aftertest=snapshot();assert before==aftertest
guard=dict(checked_at=datetime.now(timezone.utc).isoformat(),php_lint=True,stale_content_rejected=True,posts_and_attachments_unchanged=True,reason='Expected stale SHA256 fails before any content or metadata mutation');(out/'editorial-601-603-update-guard.json').write_text(json.dumps(guard,indent=2)+'\n')
run(['ssh','calicata-root',f'test ! -e {remote}/publish-editorial-before-attribution-20261031.php && docker cp {c}:/tmp/publish-editorial.php {remote}/publish-editorial-before-attribution-20261031.php && docker exec {c} cp /tmp/publish-editorial-reviewed.php /tmp/publish-editorial.php'])
for i in ids:
 p=base/i/'article.json';a=json.load(open(p));assert 'text_update'not in a;a['text_update']=dict(post_id=before[i]['post_id'],expected_content_sha256=before[i]['content_sha256'],reason='Add explicit primary-source attribution to the best counterargument, preserving article identity and original media');p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
archive=Path('/tmp/mee-attribution-589-603.tar.gz');assert not archive.exists()
with tarfile.open(archive,'w:gz')as f:
 for i in ids:
  a=json.load(open(base/i/'article.json'))
  for n in ['article.json','article.html']+[x['file']for x in a['images'].values()]:f.add(base/i/n,arcname=i+'/'+n)
stage=remote+'/articles-attribution-589-603';run(['scp',str(archive),'calicata-root:'+remote+'/'+archive.name]);run(['ssh','calicata-root',f'mkdir {stage} && tar -xzf {remote}/{archive.name} -C {stage} && docker cp {stage} {c}:/tmp/articles-attribution-589-603 && docker exec {c} chown -R 33:33 /tmp/articles-attribution-589-603'])
updated=[]
for i in ids:
 p=base/i/'text-update-publication.json';assert not p.exists();res=json.loads(run(['ssh','calicata-root',f'docker exec --user 33:33 {c} php /tmp/publish-editorial.php /tmp/articles-attribution-589-603/{i}/article.json --update-text']).stdout)
 assert res['updated']and res['post_id']==before[i]['post_id']and sorted(res['image_ids'].values())==before[i]['attachments']and res['content_before_sha256']==before[i]['content_sha256'];p.write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n');updated.append(res);print('Revisada',i,res['post_id'],res['image_ids'],flush=True)
 sync=json.loads(run(['python3','scripts/sync-production-status.py'],cwd=r).stdout);assert sync['counts']['terminada']==601;print('Registro',sync['counts'],flush=True)
after=snapshot()
for i in ids:assert before[i]['post_id']==after[i]['post_id']and before[i]['attachments']==after[i]['attachments']and before[i]['content_sha256']!=after[i]['content_sha256']
e=dict(checked_at=datetime.now(timezone.utc).isoformat(),updated=updated,after=after,posts_preserved=True,media_preserved=True,no_new_public_media=True,counts=sync['counts']);(out/'editorial-601-603-attribution-updates.json').write_text(json.dumps(e,ensure_ascii=False,indent=2)+'\n');print('Revisión completada',len(updated),flush=True)
