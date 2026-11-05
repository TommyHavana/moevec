from pathlib import Path
from datetime import datetime, timezone
import base64, fcntl, hashlib, json, re, subprocess, sys, tarfile

root=Path(__file__).resolve().parents[3]
approval=json.loads((root/'editorial/title-alternatives-approved-2026-11-05.json').read_text())
changes=approval['changes']
ids=[x['id']for x in changes]
audit=root/'inventario/auditoria-2026-10-28'
mode=sys.argv[1]
def run(args,**kw): return subprocess.run(args,capture_output=True,check=True,**kw)
def text_run(args,**kw): return run(args,text=True,**kw).stdout
def write(path,value):
    sys.path.insert(0,str(root/'scripts'))
    from atomic_export import atomic_export
    atomic_export([(path,json.dumps(value,ensure_ascii=False,indent=2)+'\n')])
def ssh(command,**kw): return text_run(['ssh','-o','BatchMode=yes','calicata-root',command],**kw)
container=ssh('docker ps -q --filter label=coolify.applicationUuid=h7kfs9qe620lg5mqip36npt4 --filter label=com.docker.compose.service=wordpress').strip()
assert re.fullmatch('[0-9a-f]+',container)
(Path('/tmp')/'mee-wp-container.txt').write_text(container)
publisher=run(['ssh','-o','BatchMode=yes','calicata-root',f'docker exec {container} cat /tmp/publish-editorial.php']).stdout
assert hashlib.sha256(publisher).digest()==hashlib.sha256((root/'scripts/publish-editorial.php').read_bytes()).digest()
lock=open('/tmp/mee-publish-approved-six-20261105.lock','w')
fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)

def preflight(selected,allow_published=False):
    payload=[]
    for ident in selected:
        a=json.loads((root/'editorial/articles'/ident/'article.json').read_text())
        payload.append(dict(id=ident,slug=a['slug'],title=a['title'],keyword=a['keyword']))
    encoded=base64.b64encode(json.dumps(payload,ensure_ascii=False).encode()).decode()
    php="""<?php require '/var/www/html/wp-load.php';$rows=json_decode(base64_decode('"""+encoded+"""'),true);$plan=mee_production_plan();$states=['publish','draft','pending','future','private','trash','inherit'];$out=[];foreach($rows as$r){$p=array_values(array_filter($plan,fn($x)=>$x['id']===$r['id']));$posts=get_posts(['post_type'=>['post','attachment'],'post_status'=>$states,'posts_per_page'=>-1,'meta_key'=>'_mee_plan_id','meta_value'=>$r['id'],'fields'=>'ids']);$focus=get_posts(['post_type'=>'post','post_status'=>$states,'posts_per_page'=>-1,'meta_key'=>'_mee_focus_keyword','meta_value'=>$r['keyword'],'fields'=>'ids']);$slug=get_page_by_path($r['slug'],OBJECT,'post');$out[]=['id'=>$r['id'],'plan_matches'=>count($p)===1&&$p[0]['title']===$r['title']&&$p[0]['slug']===$r['slug'],'posts_and_media'=>$posts,'keyword_matches'=>$focus,'slug_occupied'=>(bool)$slug];}echo json_encode($out,JSON_UNESCAPED_UNICODE);"""
    result=json.loads(ssh(f'docker exec -i --user 33:33 {container} php',input=php))
    assert len(result)==len(selected) and all(x['plan_matches']for x in result),result
    if not allow_published: assert all(not x['posts_and_media']and not x['keyword_matches']and not x['slug_occupied']for x in result),result
    return result

if mode=='plan':
    dest='/var/www/html/wp-content/plugins/mee-editorial/data/production-plan.json'
    local=(root/'wordpress/plugins/mee-editorial/data/production-plan.json').read_bytes()
    newhash=hashlib.sha256(local).hexdigest()
    remote=run(['ssh','-o','BatchMode=yes','calicata-root',f'docker exec {container} cat {dest}']).stdout
    oldhash=hashlib.sha256(remote).hexdigest()
    proof=root/'editorial/approved-titles-remote-plan-2026-11-05.json'
    backup='/data/mee-backups/produccion-840-approved-title-plan-20261105'
    if oldhash!=newhash:
        assert oldhash==approval['original_plan_sha256'], 'El plan remoto cambió; no sobrescribir.'
        original=json.loads(remote);updated=json.loads(local)
        differences=[(a,b)for a,b in zip(original,updated)if a!=b]
        assert len(original)==len(updated)==840 and len(differences)==6
        assert all({k for k in a if a[k]!=b[k]}=={'title'}for a,b in differences)
        before=root/'editorial/production-tools/2026-11-05/production-plan-remote-original.json'
        before.write_bytes(remote)
        ssh(f'mkdir -m 700 {backup}')
        text_run(['scp',str(before),f'calicata-root:{backup}/production-plan.before.json'])
        stage='/data/mee-editorial-work/20261028/production-plan-approved-20261105.json'
        text_run(['scp',str(root/'wordpress/plugins/mee-editorial/data/production-plan.json'),f'calicata-root:{stage}'])
        temporary=dest+'.approved-20261105.tmp'
        ssh(f'docker cp {stage} {container}:{temporary} && docker exec {container} chown 33:33 {temporary}')
        php="<?php $p="+json.dumps(dest)+";$tmp="+json.dumps(temporary)+";if(hash_file('sha256',$p)!=='"+oldhash+"'||hash_file('sha256',$tmp)!=='"+newhash+"')throw new RuntimeException('Plan cambió');if(!rename($tmp,$p))throw new RuntimeException('No se pudo actualizar el plan');echo hash_file('sha256',$p);"
        assert ssh(f'docker exec -i {container} php',input=php).strip()==newhash
    else:
        assert proof.exists(), 'Plan ya actualizado; reconciliar la prueba antes de reintentar.'
    verified=preflight(ids)
    write(proof,dict(checked_at=datetime.now(timezone.utc).isoformat(),before_sha256=approval['original_plan_sha256'],after_sha256=newhash,backup_directory=backup,changes=changes,only_titles_changed=True,category_or_slug_changes=False,preflight=verified))
    write(audit/'editorial-approved-six-preflight.json',verified)
    print(json.dumps(dict(remote_plan_updated=True,preflight=verified),ensure_ascii=False),flush=True)
elif mode=='publish':
    block=int(sys.argv[2]);selected=ids[:3] if block==1 else ids[3:]
    proof=json.loads((root/'editorial/approved-titles-remote-plan-2026-11-05.json').read_text())
    assert proof['only_titles_changed']
    archive=Path('/tmp/mee-approved-six-20261105.tar.gz')
    stage='/data/mee-editorial-work/20261028/articles-approved-six-20261105'
    stageproof=root/'editorial/approved-six-staging-2026-11-05.json'
    if not stageproof.exists():
        assert not archive.exists()
        with tarfile.open(archive,'w:gz')as tar:
            for ident in ids:
                d=root/'editorial/articles'/ident;a=json.loads((d/'article.json').read_text())
                for name in ['article.json','article.html']+[x['file']for x in a['images'].values()]:tar.add(d/name,arcname=ident+'/'+name)
        text_run(['scp',str(archive),'calicata-root:/data/mee-editorial-work/20261028/mee-approved-six-20261105.tar.gz'])
        ssh(f'mkdir {stage} && tar -xzf /data/mee-editorial-work/20261028/mee-approved-six-20261105.tar.gz -C {stage}')
        ssh(f'docker exec {container} mkdir /tmp/mee-approved-six-20261105 && docker cp {stage}/. {container}:/tmp/mee-approved-six-20261105 && docker exec {container} chown -R 33:33 /tmp/mee-approved-six-20261105')
        write(stageproof,dict(container=container,directory=stage,archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),ids=ids))
    else:
        assert json.loads(stageproof.read_text())['container']==container, 'Contenedor cambió; reconciliar preparación.'
    for ident in selected:
        d=root/'editorial/articles'/ident
        if (d/'publication.json').exists():
            print('Ya consta publicación; verificar sin repetir',ident,flush=True)
            continue
        preflight([ident])
        a=json.loads((d/'article.json').read_text())
        assert a['review']['title_checked'] and a['review']['sources_verified'] and a['review']['editorial_checked']
        raw=ssh(f'docker exec --user 33:33 {container} php /tmp/publish-editorial.php /tmp/mee-approved-six-20261105/{ident}/article.json')
        assert raw.strip(), 'Respuesta vacía: reconciliar WordPress antes de repetir.'
        pub=json.loads(raw);write(d/'publication.json',pub)
        assert pub.get('created')and pub['id']==ident and len(pub['image_ids'])==3,pub
        print('PUBLICADA',json.dumps(pub,ensure_ascii=False),flush=True)
        synced=json.loads(text_run(['python3','scripts/sync-production-status.py'],cwd=root))
        print('REGISTRO',synced['counts'],flush=True)
        state_path=root/'editorial/production-state.json';state=json.loads(state_path.read_text())
        state.update(phase='published_pending_verification',updated_at=datetime.now(timezone.utc).isoformat(),last_published_id=ident)
        state.setdefault('approved_title_publications',{})[ident]=pub
        write(state_path,state)
else: raise SystemExit('Modo desconocido')
