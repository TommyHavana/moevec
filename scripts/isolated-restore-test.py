import subprocess,json,gzip,os,secrets,time,hashlib
from pathlib import Path
from datetime import datetime,timezone
folder=Path('/data/mee-backups/mejoras-20261105/restore-test');folder.mkdir(parents=True,exist_ok=True);os.chmod(folder,0o700)
def cmd(args,input=None):
 p=subprocess.run(args,input=input,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if p.returncode:raise RuntimeError(args[0]+' '+args[1]+': '+p.stderr.decode(errors='replace')[:500])
 return p.stdout
def service(name):
 ids=cmd(['docker','ps','-q','--filter','label=coolify.applicationUuid=h7kfs9qe620lg5mqip36npt4','--filter','label=com.docker.compose.service='+name]).decode().strip();assert ids and '\n'not in ids;return ids
wp,db=service('wordpress'),service('database');wp_image=cmd(['docker','inspect','--format','{{.Config.Image}}',wp]).decode().strip();db_image=cmd(['docker','inspect','--format','{{.Config.Image}}',db]).decode().strip()
names={'network':'mee-restore-audit-20261105','db':'mee-restore-db-20261105','wp':'mee-restore-wp-20261105','dbvol':'mee-restore-dbdata-20261105','wpvol':'mee-restore-wpdata-20261105'}
for n in ['db','wp']:
 assert not cmd(['docker','ps','-aq','--filter','name=^/'+names[n]+'$']).strip(),'Existing test container'
baseline_php=b"<?php require '/var/www/html/wp-load.php';echo json_encode(['completed'=>count(array_filter(mee_production_snapshot(),fn($r)=>$r['status']==='terminada')),'prefix'=>$wpdb->prefix,'tables'=>count($wpdb->get_col('SHOW TABLES'))]);"
baseline=json.loads(cmd(['docker','exec','-i','--user','33:33',wp,'php'],input=baseline_php));assert baseline['completed']==840
dump=folder/'database.sql.gz'
archive=folder/'wordpress-files.tar.gz'
if not (dump.is_file() and archive.is_file() and dump.stat().st_size>0 and archive.stat().st_size>0):
 config='/tmp/mee-audit-backup-20261105.cnf'
 cmd(['docker','exec',db,'sh','-c',"umask 077; { printf '[client]\\nuser=root\\npassword='; cat /run/mee-secrets/root_password; printf '\\n'; } > "+config])
 print('Snapshot SQL consistente y privado...',flush=True)
 dump=folder/'database.sql.gz'
 try:
  with dump.open('wb')as output:
   proc=subprocess.Popen(['docker','exec',db,'mariadb-dump','--defaults-extra-file='+config,'--single-transaction','--quick','--routines','--triggers','mee_wordpress'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
   with gzip.GzipFile(fileobj=output,mode='wb',compresslevel=3)as zipped:
    while chunk:=proc.stdout.read(1024*1024):zipped.write(chunk)
   err=proc.stderr.read();assert proc.wait()==0,err.decode()[:300]
 finally:cmd(['docker','exec',db,'rm','-f',config])
 os.chmod(dump,0o600)
 print('Snapshot de archivos WordPress y uploads...',flush=True)
 archive=folder/'wordpress-files.tar.gz'
 with archive.open('wb')as output:
  proc=subprocess.Popen(['docker','exec',wp,'tar','-C','/var/www/html','-cf','-','.'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  with gzip.GzipFile(fileobj=output,mode='wb',compresslevel=1)as zipped:
   while chunk:=proc.stdout.read(1024*1024):zipped.write(chunk)
  err=proc.stderr.read();assert proc.wait()==0,err.decode()[:300]
 os.chmod(archive,0o600)
else:print('Reutilizando snapshots privados ya creados; se repite solo la restauración aislada.',flush=True)
secret=folder/'restore-secret';secret.write_text(secrets.token_urlsafe(36));os.chown(secret,33,33);os.chmod(secret,0o400)
label='mee.audit.restore=20261105';created=[]
try:
 cmd(['docker','network','create','--internal','--label',label,names['network']]);created.append(('network',names['network']))
 for k in ['dbvol','wpvol']:cmd(['docker','volume','create','--label',label,names[k]]);created.append(('volume',names[k]))
 cmd(['docker','run','-d','--name',names['db'],'--label',label,'--network',names['network'],'-v',names['dbvol']+':/var/lib/mysql','-v',str(secret)+':/run/secrets/restore:ro','-e','MARIADB_ROOT_PASSWORD_FILE=/run/secrets/restore','-e','MARIADB_DATABASE=mee_wordpress','-e','MARIADB_USER=mee_restore','-e','MARIADB_PASSWORD_FILE=/run/secrets/restore',db_image]);created.append(('container',names['db']))
 for attempt in range(45):
  p=subprocess.run(['docker','exec',names['db'],'healthcheck.sh','--connect','--innodb_initialized'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  if p.returncode==0:break
  time.sleep(2)
 else:raise RuntimeError('Restore DB did not become ready')
 # The isolated DB uses its generated private credential, never the production one.
 cmd(['docker','exec','-i',names['db'],'sh','-c','umask 077; cat > /tmp/restore.cnf'],input=('[client]\nuser=root\npassword='+secret.read_text()+'\n').encode())
 print('Restaurando base y archivos en volúmenes aislados...',flush=True)
 proc=subprocess.Popen(['docker','exec','-i',names['db'],'mariadb','--defaults-extra-file=/tmp/restore.cnf','mee_wordpress'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 with gzip.open(dump,'rb')as src:
  while chunk:=src.read(1024*1024):proc.stdin.write(chunk)
 proc.stdin.close();err=proc.stderr.read();assert proc.wait()==0,err.decode()[:300]
 # Restore files using only the already installed image; no public ports.
 proc=subprocess.Popen(['docker','run','--rm','-i','--network','none','-v',names['wpvol']+':/restore','--entrypoint','tar',wp_image,'-C','/restore','-xf','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 with gzip.open(archive,'rb')as src:
  while chunk:=src.read(1024*1024):proc.stdin.write(chunk)
 proc.stdin.close();err=proc.stderr.read();assert proc.wait()==0,err.decode()[:300]
 # Generate a fresh restore-only wp-config from environment on startup.
 cmd(['docker','run','--rm','--network','none','-v',names['wpvol']+':/restore','--entrypoint','sh',wp_image,'-c','rm -f /restore/wp-config.php; mkdir -p /restore/wp-content/mu-plugins; printf "%s" "<?php add_filter(\'redirect_canonical\',\'__return_false\');" > /restore/wp-content/mu-plugins/mee-isolated-restore.php'])
 extra="define('WP_HOME','https://moevec.org/blog');define('WP_SITEURL','https://moevec.org/blog');define('DISABLE_WP_CRON',true);define('DISALLOW_FILE_MODS',true);"
 cmd(['docker','run','-d','--name',names['wp'],'--label',label,'--network',names['network'],'-v',names['wpvol']+':/var/www/html','-v',str(secret)+':/run/secrets/restore:ro','-e','WORDPRESS_DB_HOST='+names['db']+':3306','-e','WORDPRESS_DB_NAME=mee_wordpress','-e','WORDPRESS_DB_USER=mee_restore','-e','WORDPRESS_DB_PASSWORD_FILE=/run/secrets/restore','-e','WORDPRESS_TABLE_PREFIX='+baseline['prefix'],'-e','WORDPRESS_CONFIG_EXTRA='+extra,wp_image]);created.append(('container',names['wp']))
 for attempt in range(30):
  p=subprocess.run(['docker','exec',names['wp'],'php','/opt/mee/healthcheck-wordpress.php'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  if p.returncode==0:break
  time.sleep(2)
 else:raise RuntimeError('Restored WP did not become ready')
 restored=json.loads(cmd(['docker','exec','-i','--user','33:33',names['wp'],'php'],input=baseline_php));assert restored==baseline,(restored,baseline)
 http=b'''<?php $ctx=stream_context_create(['http'=>['header'=>"Host: moevec.org\r\nX-Forwarded-Proto: https\r\n",'timeout'=>30]]);$result=[];foreach(['/blog/','/blog/que-es-el-capitalismo/','/blog/hojas-de-calculo-herramienta-rentable/']as$path){$html=file_get_contents('http://127.0.0.1'.$path,false,$ctx);if(!$html||!str_contains($html,'<h1'))throw new Exception('HTTP restore failed');$result[]=['path'=>$path,'bytes'=>strlen($html),'h1'=>substr_count($html,'<h1')];}echo json_encode($result);'''
 http_result=json.loads(cmd(['docker','exec','-i','--user','33:33',names['wp'],'php'],input=http))
 network=json.loads(cmd(['docker','network','inspect',names['network']]))[0];assert network['Internal']
 for k in ['db','wp']:
  info=json.loads(cmd(['docker','inspect',names[k]]))[0];assert not info['HostConfig']['PortBindings']
 def sha(p):
  h=hashlib.sha256()
  with p.open('rb')as f:
   while chunk:=f.read(1024*1024):h.update(chunk)
  return h.hexdigest()
 result={'checked_at':datetime.now(timezone.utc).isoformat(),'isolated_restore':True,'same_vps':True,'external_backup':False,'public_ports':False,'external_network':False,'baseline':baseline,'restored':restored,'http':http_result,'snapshots':[{'file':p.name,'bytes':p.stat().st_size,'sha256':sha(p)}for p in [dump,archive]],'sensitive_data_downloaded':False}
 (folder/'report.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
finally:
 for kind,name in reversed(created):
  if kind=='container':subprocess.run(['docker','rm','-f',name],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  elif kind=='volume':subprocess.run(['docker','volume','rm',name],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  else:subprocess.run(['docker','network','rm',name],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 secret.unlink(missing_ok=True)
