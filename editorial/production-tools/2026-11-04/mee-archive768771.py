from pathlib import Path
from datetime import datetime,timezone
import json,shutil,hashlib,zipfile,subprocess,sys
start,end,nextstart=map(int,sys.argv[1:4]);label=f'{start}-{end}'
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');private=r.parent/'mee-deploy-source';backs=r.parent/'mee-backups';s=json.load(open(r/'editorial/production-state.json'));priorproof=Path(s['last_delivery_proof']);ev=json.load(open(priorproof));base=Path(ev['local_backup']['zip']);bh=hashlib.sha256(base.read_bytes()).hexdigest();assert bh==ev['local_backup_sha256']
def git(*a):return subprocess.check_output(['git','-C',str(private),*a],text=True).rstrip('\n')
subprocess.run(['git','-C',str(private),'fetch','origin','main'],capture_output=True,check=True);assert not git('status','--porcelain');assert git('rev-parse','HEAD')==git('rev-parse','origin/main')==ev['private_commit']
z=backs/f'MEE_Editorial_{label}_2026-11-04_incremental.zip';proof=backs/f'produccion-{label}-entrega-20261104.json';assert not z.exists()and not proof.exists();assert shutil.disk_usage(r).free>167772160
s.update(last_delivery_proof=str(proof),last_local_backup=str(z),local_backup_kind='incremental',local_backup_base={'path':str(base),'sha256':bh});(r/'editorial/production-state.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
selected=[]
plan=json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json')); ids=[x['id']for x in plan if start<=x['number']<=end or nextstart<=x['number']<nextstart+3]
for ident in ids:
 selected.extend(p for p in(r/'editorial/articles'/ident).rglob('*')if p.is_file())
for entry in s.get('local_preparations',[]):
 if entry['number'] in s.get('title_reviews_pending',[501,512,649]):
  for p in(r/'editorial/articles'/entry['id']).rglob('*'):
   if p.is_file():
    q=private/p.relative_to(r)
    if not q.exists()or hashlib.sha256(q.read_bytes()).digest()!=hashlib.sha256(p.read_bytes()).digest():selected.append(p)
prior_ids=[x['id']for x in plan if x['number']in s.get('completed_this_run',[])and x['number']<start]
prior_candidates=[p for ident in prior_ids for p in(r/'editorial/articles'/ident).rglob('*')if p.is_file()]
prior_candidates.extend((r/'inventario/auditoria-2026-10-28').glob(f'editorial-{start-3}-{end-3}-*.json'))
prior_candidates.extend((r/'docs/produccion').glob('*.md'))
for p in prior_candidates:
 q=private/p.relative_to(r)
 if not q.exists()or hashlib.sha256(q.read_bytes()).digest()!=hashlib.sha256(p.read_bytes()).digest():selected.append(p)
selected.extend(p for p in(r/'editorial/production-tools').rglob('*')if p.is_file());selected.extend(r/x for x in ['editorial/automation-status-2026-11-03.json','scripts/publish-editorial.php','scripts/sync-production-status.py','scripts/atomic_export.py','docs/10-DECISIONES-ABIERTAS.md','docs/15-ESTADO-Y-CONTINUIDAD.md','docs/16-BACKLOG-REACT.md','docs/26-PRODUCCION-CONTINUA.md','docs/24-REGISTRO-PRODUCCION-840.md','inventario/plan-editorial-840-status.json','inventario/plan-editorial-840.csv','editorial/production-state.json',f'docs/produccion/2026-11-04-bloque-{label}.md',f'docs/produccion/2026-11-04-respaldo-{label}.md',f'docs/produccion/2026-11-04-ejecucion-desde-{s["run_started_with_completed"]}.md']);selected.extend((r/'inventario/auditoria-2026-10-28').glob(f'editorial-{label}-*.json'));selected=sorted(set(selected));assert all(p.is_file()for p in selected);selected=[p for p in selected if not(private/p.relative_to(r)).exists()or hashlib.sha256(p.read_bytes()).digest()!=hashlib.sha256((private/p.relative_to(r)).read_bytes()).digest()];assert shutil.disk_usage(r).free>max(167772160,3*sum(p.stat().st_size for p in selected))
manifest=[dict(path='mee-web/'+str(p.relative_to(r)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())for p in selected]
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED)as f:
 for p in selected:f.write(p,'mee-web/'+str(p.relative_to(r)))
 f.writestr('SHA256-MANIFEST.json',json.dumps(dict(base_backup=str(base),base_sha256=bh,files=manifest),ensure_ascii=False,indent=2)+'\n');f.writestr('RESTORE-INCREMENTAL.txt','Preserve full chain ending '+base.name+'; restore this overlay after it. Contains verified completed articles for this block and the exact pending resources recorded in production-state.\n')
with zipfile.ZipFile(z)as f:
 assert f.testzip()is None and len(f.namelist())==len(set(f.namelist()))
 for x in manifest:assert hashlib.sha256(f.read(x['path'])).hexdigest()==x['sha256']
rels=[str(p.relative_to(r))for p in selected]
for p in selected:
 q=private/p.relative_to(r);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q);assert q.read_bytes()==p.read_bytes()
subprocess.run(['git','-C',str(private),'add','--',*rels],check=True);assert set(git('diff','--cached','--name-only').splitlines())<=set(rels);subprocess.run(['git','-C',str(private),'commit','-q','-m',f'editorial: publica y verifica{label}; conserva siguiente bloque'],check=True);subprocess.run(['git','-C',str(private),'push','origin','main'],check=True);commit=git('rev-parse','HEAD');assert commit==git('rev-parse','origin/main')and not git('status','--porcelain')
reg=json.load(open(r/'inventario/plan-editorial-840-status.json'));published=[{k:x[k]for k in['number','id','url','images','words']}for x in reg['entries']if start<=x['number']<=end and x['status']=='terminada'];assert len(published)==3;e=dict(checked_at=datetime.now(timezone.utc).isoformat(),run_started_with_completed=s['run_started_with_completed'],completed_this_run=s['completed_this_run'],counts=reg['counts'],public_original_images=sum(x['images']for x in reg['entries']if x['status']=='terminada'),published=published,unpublished_gaps=s.get("title_reviews_pending",[501,512,649]),local_preparations=s['local_preparations'],remote_backup=s['last_backup'],local_backup=dict(zip=str(z),zip_bytes=z.stat().st_size,zip_files=len(selected)+2,kind='incremental',base_backup=str(base),base_sha256=bh),local_backup_sha256=hashlib.sha256(z.read_bytes()).hexdigest(),private_commit=commit,private_clean=True,selected_files_equal=len(selected),next_block=s['current_block'],next_after_block=s['next_after_block'],full_restore_boot_test=False,previous_delivery_proof=str(priorproof));proof.write_text(json.dumps(e,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'counts':reg['counts'],'zip_bytes':z.stat().st_size,'files_equal':len(selected),'private_commit':commit,'free_bytes':shutil.disk_usage(r).free}))
