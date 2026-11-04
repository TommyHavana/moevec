from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,re,hashlib
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');base=r/'editorial/articles';ids=['E6.7.09','E6.7.10','E6.7.11'];c=Path('/tmp/mee-wp-container.txt').read_text().strip();assert re.fullmatch('[0-9a-f]+',c)
pre=json.load(open(r/'inventario/auditoria-2026-10-28/editorial-729-731-preflight.json'));assert {x['id']for x in pre}==set(ids)and all(not x['posts_and_media']and not x['keyword_matches']and not x['slug_occupied']for x in pre)
def run(args):return subprocess.run(args,text=True,capture_output=True,check=True)
stage='/data/mee-editorial-work/20261028/articles-729-731'
for ident in ids:
 d=base/ident;assert not(d/'publication.json').exists()
 run(['ssh','-o','BatchMode=yes','calicata-root',f'docker exec {c} mkdir -p /tmp/{ident} && docker cp {stage}/{ident}/. {c}:/tmp/{ident} && docker exec {c} chown -R 33:33 /tmp/{ident}'])
 got=run(['ssh','-o','BatchMode=yes','calicata-root',f'docker exec {c} sha256sum /tmp/{ident}/article.json']).stdout.split()[0];assert got==hashlib.sha256((d/'article.json').read_bytes()).hexdigest()
 x=run(['ssh','-o','BatchMode=yes','calicata-root',f'docker exec --user 33:33 {c} php /tmp/publish-editorial.php /tmp/{ident}/article.json'])
 journal=dict(checked_at=datetime.now(timezone.utc).isoformat(),returncode=x.returncode,stdout_bytes=len(x.stdout.encode()),stderr_bytes=len(x.stderr.encode()),preflight_absent_verified=True)
 (d/'publication-attempt-reconciled.json').write_text(json.dumps(journal,ensure_ascii=False,indent=2)+'\n')
 assert x.stdout.strip(),'Respuesta vacía; reconciliar WordPress antes de otro intento'
 pub=json.loads(x.stdout);assert pub.get('created')and len(pub['image_ids'])==3;(d/'publication.json').write_text(json.dumps(pub,ensure_ascii=False,indent=2)+'\n');print('Publicada',json.dumps(pub,ensure_ascii=False),flush=True)
 j=json.loads(run(['python3',str(r/'scripts/sync-production-status.py')]).stdout);print('Registro',j['counts'],flush=True)
