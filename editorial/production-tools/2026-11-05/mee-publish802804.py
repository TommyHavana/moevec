import subprocess,json,re,tarfile
from pathlib import Path
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');base=r/'editorial/articles';ids=['E2.5.07','E2.5.08','E2.5.09'];c=Path('/tmp/mee-wp-container.txt').read_text().strip();assert re.fullmatch('[0-9a-f]+',c)
def run(args,**kw):return subprocess.run(args,text=True,capture_output=True,check=True,**kw)
pre=json.load(open(r/'inventario/auditoria-2026-10-28/editorial-802-804-preflight.json'));assert {x['id']for x in pre}==set(ids) and all(not x['posts_and_media']and not x['keyword_matches']and not x['slug_occupied']for x in pre)
archive=Path('/tmp/mee-editorial-802-804.tar.gz');assert not archive.exists()
with tarfile.open(archive,'w:gz')as f:
 for i in ids:
  d=base/i;a=json.load(open(d/'article.json'))
  for n in ['article.json','article.html']+[im['file']for im in a['images'].values()]:f.add(d/n,arcname=i+'/'+n)
run(['scp',str(archive),'calicata-root:/data/mee-editorial-work/20261028/mee-editorial-802-804.tar.gz'])
stage='/data/mee-editorial-work/20261028/articles-802-804';run(['ssh','calicata-root',f'mkdir {stage} && tar -xzf /data/mee-editorial-work/20261028/mee-editorial-802-804.tar.gz -C {stage}'])
for i in ids:
 assert not(base/i/'publication.json').exists()
 run(['ssh','calicata-root',f'docker exec {c} mkdir /tmp/{i} && docker cp {stage}/{i}/. {c}:/tmp/{i} && docker exec {c} chown -R 33:33 /tmp/{i}'])
 x=run(['ssh','calicata-root',f'docker exec --user 33:33 {c} php /tmp/publish-editorial.php /tmp/{i}/article.json']);assert x.stdout.strip(),'Respuesta vacía; reconciliar WordPress antes de otro intento';pub=json.loads(x.stdout);(base/i/'publication.json').write_text(json.dumps(pub,ensure_ascii=False,indent=2)+'\n');assert pub.get('created')and len(pub['image_ids'])==3,pub;print('Publicada',json.dumps(pub,ensure_ascii=False),flush=True)
 sync=json.loads(run(['python3','scripts/sync-production-status.py'],cwd=r).stdout);print('Registro',sync['counts'],flush=True)
