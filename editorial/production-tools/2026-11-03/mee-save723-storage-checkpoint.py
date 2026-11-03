from pathlib import Path
from datetime import datetime,timezone
import json,shutil,hashlib,zipfile,subprocess
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');private=r.parent/'mee-deploy-source';backs=r.parent/'mee-backups';sp=r/'editorial/production-state.json';s=json.load(open(sp));reg=json.load(open(r/'inventario/plan-editorial-840-status.json'));priorproof=Path(s['last_delivery_proof']);ev=json.load(open(priorproof));assert reg['counts']==dict(terminada=718,**{'en curso':0},pendiente=122);assert s['current_block']==[723,724,725]
base=Path(ev['local_backup']['zip']);bh=hashlib.sha256(base.read_bytes()).hexdigest();assert bh==ev['local_backup_sha256']
z=backs/'MEE_Editorial_723-725_2026-11-03_preparacion.zip';proof=backs/'produccion-723-725-preparacion-20261103.json';assert not z.exists()and not proof.exists()
def git(*a):return subprocess.check_output(['git','-C',str(private),*a],text=True).rstrip('\n')
subprocess.run(['git','-C',str(private),'fetch','origin','main'],capture_output=True,check=True);assert not git('status','--porcelain');assert git('rev-parse','HEAD')==git('rev-parse','origin/main')==ev['private_commit']
s.update(last_delivery_proof=str(proof),last_local_backup=str(z),local_backup_kind='incremental-preparation-checkpoint',local_backup_base={'path':str(base),'sha256':bh});sp.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
candidates=[]
for ident in ['E6.7.03','E6.7.04','E6.7.05']:
 candidates.extend(p for p in(r/'editorial/articles'/ident).rglob('*')if p.is_file())
candidates.extend(p for p in(r/'editorial/production-tools/2026-11-03').rglob('*')if p.is_file())
candidates.extend(r/x for x in ['editorial/production-state.json','docs/15-ESTADO-Y-CONTINUIDAD.md','docs/16-BACKLOG-REACT.md','docs/10-DECISIONES-ABIERTAS.md','docs/26-PRODUCCION-CONTINUA.md','docs/produccion/2026-11-03-punto-723-capacidad.md','docs/produccion/2026-11-03-ejecucion-desde-586.md'])
selected=[]
for p in sorted(set(candidates)):
 q=private/p.relative_to(r)
 if not q.exists()or hashlib.sha256(q.read_bytes()).digest()!=hashlib.sha256(p.read_bytes()).digest():selected.append(p)
assert sp in selected;total=sum(p.stat().st_size for p in selected);assert shutil.disk_usage(r).free>max(167772160,3*total)
manifest=[dict(path='mee-web/'+str(p.relative_to(r)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())for p in selected]
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED)as f:
 for p in selected:f.write(p,'mee-web/'+str(p.relative_to(r)))
 f.writestr('SHA256-MANIFEST.json',json.dumps(dict(base_backup=str(base),base_sha256=bh,files=manifest),ensure_ascii=False,indent=2)+'\n');f.writestr('RESTORE-INCREMENTAL.txt','Preserve the full chain ending '+base.name+'. Apply this preparation overlay after it. No new published articles: WordPress remains718/840. Resume723 at interior-2 only; existing featured and interior-1 must not be regenerated.724/725 have no images or text. No new SQL or boot restore test.\n')
with zipfile.ZipFile(z)as f:
 assert f.testzip()is None and len(f.namelist())==len(set(f.namelist()))
 for x in manifest:assert hashlib.sha256(f.read(x['path'])).hexdigest()==x['sha256']
rels=[str(p.relative_to(r))for p in selected]
for p in selected:
 q=private/p.relative_to(r);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q);assert q.read_bytes()==p.read_bytes()
subprocess.run(['git','-C',str(private),'add','--',*rels],check=True);assert set(git('diff','--cached','--name-only').splitlines())<=set(rels);subprocess.run(['git','-C',str(private),'commit','-q','-m','editorial: conserva723 con2 imagenes y punto exacto de capacidad'],check=True);subprocess.run(['git','-C',str(private),'push','origin','main'],check=True);commit=git('rev-parse','HEAD');assert commit==git('rev-parse','origin/main')and not git('status','--porcelain')
e=dict(checked_at=datetime.now(timezone.utc).isoformat(),counts=reg['counts'],public_original_images=2154,completed_this_run=s['completed_this_run'],run_started_with_completed=s['run_started_with_completed'],published=[],unpublished_gaps=s['title_reviews_pending'],local_preparations=s['local_preparations'],remote_backup=s['last_backup'],local_backup=dict(zip=str(z),zip_bytes=z.stat().st_size,zip_files=len(selected)+2,kind='incremental-preparation-checkpoint',base_backup=str(base),base_sha256=bh),local_backup_sha256=hashlib.sha256(z.read_bytes()).hexdigest(),private_commit=commit,private_clean=True,selected_files_equal=len(selected),next_block=s['current_block'],next_after_block=s['next_after_block'],full_restore_boot_test=False,previous_delivery_proof=str(priorproof),storage_free_after_bytes=shutil.disk_usage(r).free)
proof.write_text(json.dumps(e,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(counts=reg['counts'],private_commit=commit,files_equal=len(selected),zip_bytes=z.stat().st_size,free_bytes=shutil.disk_usage(r).free)))
