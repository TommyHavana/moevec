from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil,zipfile,subprocess,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[3]/'scripts'))
from atomic_export import atomic_export
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');private=r.parent/'mee-deploy-source';backs=r.parent/'mee-backups';s=json.load(open(r/'editorial/production-state.json'))
assert s['current_block']==[738,739,740]
prior=Path(s['last_delivery_proof']);previous=json.load(open(prior));base=Path(previous['local_backup']['zip']);base_sha=hashlib.sha256(base.read_bytes()).hexdigest();assert base_sha==previous['local_backup_sha256']
def git(*args):return subprocess.check_output(['git','-C',str(private),*args],text=True).strip()
subprocess.run(['git','-C',str(private),'fetch','origin','main'],check=True,capture_output=True)
assert not git('status','--porcelain') and git('rev-parse','HEAD')==git('rev-parse','origin/main')==previous['private_commit']
z=backs/'MEE_Editorial_738-740_preparacion2_2026-11-04_incremental.zip';proof=backs/'produccion-738-740-preparacion2-entrega-20261104.json';assert not z.exists() and not proof.exists()
assert shutil.disk_usage(r).free>167772160
s.update(last_delivery_proof=str(proof),last_local_backup=str(z),local_backup_kind='incremental_preparation',local_backup_base=dict(path=str(base),sha256=base_sha),partial_private_checkpoint=dict(proof=str(proof),images=8,bodies=3,published=False))
atomic_export([(r/'editorial/production-state.json',json.dumps(s,ensure_ascii=False,indent=2)+'\n')])
candidates=[r/'editorial/production-state.json',r/'docs/26-PRODUCCION-CONTINUA.md']
for ident in s['current_ids']:candidates.extend(p for p in (r/'editorial/articles'/ident).rglob('*') if p.is_file())
candidates.extend(p for p in (r/'editorial/production-tools/2026-11-04').rglob('*') if p.is_file())
files=[p for p in sorted(set(candidates)) if not(private/p.relative_to(r)).exists() or hashlib.sha256(p.read_bytes()).digest()!=hashlib.sha256((private/p.relative_to(r)).read_bytes()).digest()]
native=Path('/Users/nerea/.codex/generated_images/01a1808e-ebdd-7c61-84d1-6281211ff5c5/exec-87388a01-e7d2-4190-9bd4-0c27ab157a8c.png');assert native.is_file()
items=[(p,'mee-web/'+str(p.relative_to(r))) for p in files]+[(native,'native-images/'+native.name)]
assert shutil.disk_usage(r).free>max(167772160,3*sum(p.stat().st_size for p,_ in items))
manifest=[dict(path=name,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p,name in items]
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as archive:
 for p,name in items:archive.write(p,name)
 archive.writestr('SHA256-MANIFEST.json',json.dumps(dict(base_backup=str(base),base_sha256=base_sha,previous_delivery_proof=str(prior),remote_native_checkpoint=s['last_partial_remote_checkpoint'],files=manifest),ensure_ascii=False,indent=2)+'\n')
 archive.writestr('RESTORE-INCREMENTAL.txt','Preparation only. No new publication. Preserve the complete prior ZIP chain and remote checkpoint for the first six native images. This overlay preserves eight WebPs, three bodies, sources, code, continuation state, and the eighth native.\n')
with zipfile.ZipFile(z) as archive:
 assert archive.testzip() is None
 for x in manifest:assert hashlib.sha256(archive.read(x['path'])).hexdigest()==x['sha256']
for p in files:
 target=private/p.relative_to(r);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target);assert p.read_bytes()==target.read_bytes()
rels=[str(p.relative_to(r)) for p in files]
subprocess.run(['git','-C',str(private),'add','--',*rels],check=True)
assert set(git('diff','--cached','--name-only').splitlines())<=set(rels)
subprocess.run(['git','-C',str(private),'commit','-q','-m','editorial: conserva preparación738-740 y ocho imágenes; sin nuevas publicaciones'],check=True)
subprocess.run(['git','-C',str(private),'push','origin','main'],check=True)
commit=git('rev-parse','HEAD');assert commit==git('rev-parse','origin/main') and not git('status','--porcelain')
e=dict(checked_at=datetime.now(timezone.utc).isoformat(),kind='preparation_only',counts=dict(terminada=733,**{'en curso':0,'pendiente':107}),published=[],local_preparations=s['local_preparations'],next_block=s['current_block'],resume_point=s['resume_point'],remote_backup=s['last_backup'],remote_partial_checkpoint=s['last_partial_remote_checkpoint'],local_backup=dict(zip=str(z),zip_bytes=z.stat().st_size,zip_files=len(items)+2,kind='incremental_preparation',base_backup=str(base),base_sha256=base_sha),local_backup_sha256=hashlib.sha256(z.read_bytes()).hexdigest(),private_commit=commit,private_clean=True,selected_files_equal=len(files),previous_delivery_proof=str(prior),full_restore_boot_test=False)
atomic_export([(proof,json.dumps(e,ensure_ascii=False,indent=2)+'\n')]);print(json.dumps(dict(zip_bytes=z.stat().st_size,files_equal=len(files),private_commit=commit,free_bytes=shutil.disk_usage(r).free)))
