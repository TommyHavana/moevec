from pathlib import Path
import base64, json, subprocess

root=Path(__file__).resolve().parents[3]
approval=json.loads((root/'editorial/title-alternatives-approved-2026-11-05.json').read_text())
state=json.loads((root/'editorial/production-state.json').read_text())
previous=state['last_backup']
assert previous['completed_articles']==834 and sorted(previous['unpublished_gaps'])==sorted(x['number']for x in approval['changes'])
params=base64.b64encode(json.dumps(dict(previous=previous,changes=approval['changes'])).encode()).decode()
remote=r'''
from pathlib import Path
from datetime import datetime,timezone
import base64,hashlib,json,os,re,subprocess,tarfile
os.umask(0o077)
parameters=json.loads(base64.b64decode('PARAMETERS'))
previous=parameters['previous'];changes=parameters['changes']
def run(args,**kw):return subprocess.run(args,capture_output=True,check=True,**kw)
def container(service):
 c=run(['docker','ps','-q','--filter','label=coolify.applicationUuid=h7kfs9qe620lg5mqip36npt4','--filter','label=com.docker.compose.service='+service]).stdout.decode().strip()
 assert re.fullmatch('[0-9a-f]+',c);return c
wp=container('wordpress');db=container('database')
d=Path('/data/mee-backups/produccion-840-cierre-seis-aprobadas-20261105');assert not d.exists();d.mkdir(mode=0o700)
php="""<?php require '/var/www/html/wp-load.php';$rows=mee_production_snapshot();$counts=[];foreach($rows as$r)$counts[$r['status']]=($counts[$r['status']]??0)+1;$ids=IDS;$files=[];$originals=[];foreach($ids as$id){$posts=get_posts(['post_type'=>'attachment','post_status'=>'inherit','posts_per_page'=>-1,'meta_key'=>'_mee_plan_id','meta_value'=>$id]);if(count($posts)!==3)throw new RuntimeException('Medios no coinciden');foreach($posts as$p){$f=get_attached_file($p->ID);$originals[]=['id'=>$id,'attachment_id'=>$p->ID,'path'=>substr($f,strlen('/var/www/html/')),'sha256'=>hash_file('sha256',$f)];}}$it=new RecursiveIteratorIterator(new RecursiveDirectoryIterator('/var/www/html/wp-content/uploads',FilesystemIterator::SKIP_DOTS));foreach($it as$f){if($f->isFile()&&preg_match('PATTERN',$f->getFilename()))$files[]=['path'=>substr($f->getPathname(),strlen('/var/www/html/')),'bytes'=>$f->getSize(),'sha256'=>hash_file('sha256',$f->getPathname())];}echo json_encode(['counts'=>$counts,'files'=>$files,'originals'=>$originals]);"""
ids=[x['id']for x in changes]
prefixes=[x.lower().replace('.','-')for x in ids]
pattern='/^(?:'+'|'.join(re.escape(x)for x in prefixes)+')-.*[.]webp$/'
php=php.replace('IDS',json.dumps(ids)).replace('PATTERN',pattern)
report=json.loads(run(['docker','exec','-i','--user','33:33',wp,'php'],input=php.encode()).stdout)
assert report['counts']=={'terminada':840},report['counts']
files=sorted(report['files'],key=lambda x:x['path']);originals=report['originals']
assert len(originals)==18 and len({x['path']for x in originals})==18 and len(files)>=18
assert {x['path']for x in originals}<={x['path']for x in files}
with(d/'wordpress.sql').open('wb')as f:
 subprocess.run(['docker','exec',db,'sh','-c','export MYSQL_PWD; MYSQL_PWD=$(cat "$MARIADB_ROOT_PASSWORD_FILE"); exec mariadb-dump --single-transaction --quick --routines --triggers --events -uroot "$MARIADB_DATABASE"'],stdout=f,stderr=subprocess.PIPE,check=True)
assert(d/'wordpress.sql').stat().st_size>30000000
archive='uploads-approved-six.tar.gz'
with(d/archive).open('wb')as f:
 subprocess.run(['docker','exec','-i',wp,'tar','-czf','-','-C','/var/www/html','-T','-'],input=('\n'.join(x['path']for x in files)+'\n').encode(),stdout=f,stderr=subprocess.PIPE,check=True)
with tarfile.open(d/archive)as tar:
 assert set(tar.getnames())=={x['path']for x in files}
 for x in files:
  data=tar.extractfile(x['path']).read();assert len(data)==x['bytes']and hashlib.sha256(data).hexdigest()==x['sha256']
(d/'files.json').write_text(json.dumps(files,ensure_ascii=False,indent=2)+'\n')
(d/'originals.json').write_text(json.dumps(originals,ensure_ascii=False,indent=2)+'\n')
plan=run(['docker','exec',wp,'cat','/var/www/html/wp-content/plugins/mee-editorial/data/production-plan.json']).stdout
(d/'production-plan.json').write_bytes(plan)
(d/'title-changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
prior=Path(previous['directory'])
(d/'RESTORE-NOTES.txt').write_text('Final checkpoint:840/840 articles complete, no unpublished gaps. Use this consistent full SQL. Restore the entire prior media chain below, then overlay '+archive+'. Restore production-plan.json to the editorial plugin data directory: six titles were explicitly approved; IDs and slugs are unchanged. Original 834-article media coverage was verified in the prior checkpoint; this archive adds the18 original assets and their responsive variants for the six former gaps. No new full restore boot test.\n\nPRIOR CHAIN:\n'+(prior/'RESTORE-NOTES.txt').read_text()+'\nFINAL OVERLAY: '+str(d/archive)+'\n')
names=['wordpress.sql',archive,'files.json','originals.json','production-plan.json','title-changes.json','RESTORE-NOTES.txt']
hashes={name:hashlib.sha256((d/name).read_bytes()).hexdigest()for name in names}
(d/'SHA256SUMS').write_text(''.join(h+'  '+n+'\n'for n,h in hashes.items()))
assert all(hashlib.sha256((d/name).read_bytes()).hexdigest()==value for name,value in hashes.items())
print(json.dumps(dict(checked_at=datetime.now(timezone.utc).isoformat(),directory=str(d),completed_articles=840,max_published_number=840,published_ranges=[[1,840]],unpublished_gaps=[],sql_bytes=(d/'wordpress.sql').stat().st_size,upload_files=len(files),original_images=18,uploads_bytes=(d/archive).stat().st_size,archives=[dict(file=archive,files=len(files),bytes=(d/archive).stat().st_size)],checksums_verified=True,archive_verified=True,overlays=previous['overlays']+1,chain_contiguous=True,published_media_coverage_complete=True,previous_directory=str(prior),restore_test=False)))
'''.replace('PARAMETERS',params)
process=subprocess.run(['ssh','-o','BatchMode=yes','calicata-root','python3 -'],input=remote,text=True,capture_output=True,check=True)
result=json.loads(process.stdout)
path=root/'inventario/auditoria-2026-10-28/editorial-approved-six-backup.json'
path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False),flush=True)
