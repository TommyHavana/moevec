from pathlib import Path
import subprocess,json
remote=r'''from pathlib import Path
import subprocess,json,re,hashlib,tarfile,os
os.umask(0o077)
def run(a,**kw):return subprocess.run(a,capture_output=True,check=True,**kw)
def container(s):
 c=run(['docker','ps','-q','--filter','label=coolify.applicationUuid=h7kfs9qe620lg5mqip36npt4','--filter','label=com.docker.compose.service='+s]).stdout.decode().strip();assert re.fullmatch('[0-9a-f]+',c);return c
wp=container('wordpress');db=container('database');d=Path('/data/mee-backups/produccion-840-incremento-589-591-20261031');assert not d.exists();d.mkdir(mode=0o700)
php=r'''+'"""'+r'''<?php $root='/var/www/html/';$out=[];$it=new RecursiveIteratorIterator(new RecursiveDirectoryIterator($root.'wp-content/uploads',FilesystemIterator::SKIP_DOTS));foreach($it as$f){if($f->isFile()&&preg_match('/^e4-8-(04|05|06)-.*[.]webp$/',$f->getFilename())){$out[]=['path'=>substr($f->getPathname(),strlen($root)),'bytes'=>$f->getSize(),'sha256'=>hash_file('sha256',$f->getPathname())];}}echo json_encode($out);'''+'"""'+r'''
files=json.loads(run(['docker','exec','-i',wp,'php'],input=php.encode()).stdout);files.sort(key=lambda x:x['path']);assert len(files)==66 and len({x['path']for x in files})==66
with (d/'wordpress.sql').open('wb')as f:
 x=subprocess.run(['docker','exec',db,'sh','-c','export MYSQL_PWD; MYSQL_PWD=$(cat "$MARIADB_ROOT_PASSWORD_FILE"); exec mariadb-dump --single-transaction --quick --routines --triggers --events -uroot "$MARIADB_DATABASE"'],stdout=f,stderr=subprocess.PIPE,check=True)
assert(d/'wordpress.sql').stat().st_size>20000000
with(d/'uploads-589-591.tar.gz').open('wb')as f:subprocess.run(['docker','exec','-i',wp,'tar','-czf','-','-C','/var/www/html','-T','-'],input=('\n'.join(x['path']for x in files)+'\n').encode(),stdout=f,stderr=subprocess.PIPE,check=True)
with tarfile.open(d/'uploads-589-591.tar.gz')as f:
 assert set(f.getnames())=={x['path']for x in files}
 for x in files:
  b=f.extractfile(x['path']).read();assert len(b)==x['bytes']and hashlib.sha256(b).hexdigest()==x['sha256']
(d/'files.json').write_text(json.dumps(files,ensure_ascii=False,indent=2)+'\n')
prior=Path('/data/mee-backups/produccion-840-incremento-586-588-20261031')
(d/'RESTORE-NOTES.txt').write_text('Checkpoint after589 verified articles. Full consistent SQL covers globals1–500,502–511,513–591. Gaps501/512 remain unpublished pending title review. Restore prior complete media chain described below, then overlay uploads-589-591.tar.gz; use this newest SQL. No new full restore boot test.\n\nPREVIOUS CHAIN:\n'+(prior/'RESTORE-NOTES.txt').read_text()+'\nNEW OVERLAY: '+str(d/'uploads-589-591.tar.gz')+'\n')
names=['wordpress.sql','uploads-589-591.tar.gz','files.json','RESTORE-NOTES.txt'];hashes={n:hashlib.sha256((d/n).read_bytes()).hexdigest()for n in names};(d/'SHA256SUMS').write_text(''.join(h+'  '+n+'\n'for n,h in hashes.items()));assert all(hashlib.sha256((d/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
print(json.dumps(dict(directory=str(d),completed_articles=589,max_published_number=591,published_ranges=[[1,500],[502,511],[513,591]],unpublished_gaps=[501,512],sql_bytes=(d/'wordpress.sql').stat().st_size,upload_files=len(files),uploads_bytes=(d/'uploads-589-591.tar.gz').stat().st_size,archives=[dict(file='uploads-589-591.tar.gz',files=len(files),bytes=(d/'uploads-589-591.tar.gz').stat().st_size)],checksums_verified=True,archive_verified=True,overlays=185,chain_contiguous=False,published_media_coverage_complete=True,restore_test=False)))
'''
p=subprocess.run(['ssh','-o','BatchMode=yes','calicata-root','python3 -'],input=remote,text=True,capture_output=True,check=True);j=json.loads(p.stdout);Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/inventario/auditoria-2026-10-28/editorial-589-591-backup.json').write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n');print(json.dumps(j))
