from pathlib import Path
import subprocess,json
remote=r'''from pathlib import Path
import subprocess,hashlib,json,shutil,os,re
os.umask(0o077)
d=Path('/data/mee-backups/produccion-840-incremento-601-603-20261031');assert d.is_dir();f=d/'wordpress-after-attribution.sql';assert not f.exists()
db=subprocess.check_output(['docker','ps','-q','--filter','label=coolify.applicationUuid=h7kfs9qe620lg5mqip36npt4','--filter','label=com.docker.compose.service=database'],text=True).strip();assert re.fullmatch('[0-9a-f]+',db)
with f.open('wb')as target:subprocess.run(['docker','exec',db,'sh','-c','export MYSQL_PWD; MYSQL_PWD=$(cat "$MARIADB_ROOT_PASSWORD_FILE"); exec mariadb-dump --single-transaction --quick --routines --triggers --events -uroot "$MARIADB_DATABASE"'],stdout=target,stderr=subprocess.PIPE,check=True)
assert f.stat().st_size>20000000
for name in ['SHA256SUMS','RESTORE-NOTES.txt']:
 dest=d/(name+'.before-attribution');assert not dest.exists();shutil.copy2(d/name,dest)
p=d/'RESTORE-NOTES.txt';p.write_text(p.read_text()+'\nLATEST TEXT REVISION CHECKPOINT: use wordpress-after-attribution.sql for the current database after fourteen explicit counterargument attribution updates on globals589–603, with601 published articles and1803 original public media. All post IDs and media preserved. Prior wordpress.sql remains intact as pre-revision snapshot; no new media overlay and no new full restore boot test.\n')
names=['wordpress.sql','wordpress-after-attribution.sql','uploads-601-603.tar.gz','files.json','RESTORE-NOTES.txt','RESTORE-NOTES.txt.before-attribution','SHA256SUMS.before-attribution'];hashes={n:hashlib.sha256((d/n).read_bytes()).hexdigest()for n in names};(d/'SHA256SUMS').write_text(''.join(v+'  '+k+'\n'for k,v in hashes.items()));assert all(hashlib.sha256((d/n).read_bytes()).hexdigest()==v for n,v in hashes.items())
print(json.dumps(dict(latest_sql_file=f.name,latest_sql_bytes=f.stat().st_size,latest_sql_sha256=hashes[f.name],text_revision_backup=True,previous_sql_preserved=True,checksums_verified=True,no_new_media=True,restore_test=False)))
'''
x=subprocess.run(['ssh','-o','BatchMode=yes','calicata-root','python3 -'],input=remote,text=True,capture_output=True,check=True);data=json.loads(x.stdout);p=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/inventario/auditoria-2026-10-28/editorial-601-603-backup.json');b=json.load(open(p));b.update(data);p.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n');print(json.dumps(data))
