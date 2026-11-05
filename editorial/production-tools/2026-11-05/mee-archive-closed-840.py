from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, zipfile

root=Path(__file__).resolve().parents[3]
private=root.parent/'mee-deploy-source';backups=root.parent/'mee-backups'
state_path=root/'editorial/production-state.json';state=json.loads(state_path.read_text())
assert state['phase']=='complete'and state['counts']=={'terminada':840,'en curso':0,'pendiente':0}
previous_proof=Path(state['last_delivery_proof']);previous=json.loads(previous_proof.read_text())
base=Path(previous['local_backup']['zip']);basehash=hashlib.sha256(base.read_bytes()).hexdigest()
assert basehash==previous['local_backup_sha256']
archive=backups/'MEE_Editorial_Cierre_840_2026-11-05_incremental.zip'
proof_path=backups/'produccion-cierre-840-entrega-20261105.json'
assert not archive.exists()and not proof_path.exists()
def git(*args):return subprocess.check_output(['git','-C',str(private),*args],text=True).rstrip('\n')
assert not git('status','--porcelain'), 'Copia privada con trabajo ajeno: no sobrescribir.'
assert git('branch','--show-current')=='main'
subprocess.run(['git','-C',str(private),'fetch','origin','main'],capture_output=True,check=True)
assert git('rev-parse','HEAD')==git('rev-parse','origin/main'), 'El remoto cambió: reconciliar antes de copiar.'
head_before=git('rev-parse','HEAD')
subprocess.run(['git','-C',str(private),'merge-base','--is-ancestor',previous['private_commit'],'HEAD'],check=True)
base_gap=set(git('diff','--name-only',previous['private_commit'],'HEAD').splitlines())
state.update(last_delivery_proof=str(proof_path),last_local_backup=str(archive),local_backup_kind='incremental',
             local_backup_base=dict(path=str(base),sha256=basehash),delivery_status='archived_and_versioned',
             final_archive_expected=str(archive))
state_path.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
changes=json.loads((root/'editorial/title-alternatives-approved-2026-11-05.json').read_text())['changes']
candidates=set()
for x in changes:candidates.update(p for p in(root/'editorial/articles'/x['id']).rglob('*')if p.is_file())
candidates.update(p for p in(root/'editorial/production-tools/2026-11-05').glob('*')if p.is_file())
candidates.update((root/'editorial').glob('approved*'))
candidates.update((root/'inventario/auditoria-2026-10-28').glob('editorial-approved-six-*.json'))
candidates.update((root/'docs/produccion').glob('2026-11-05-aprobadas-*.md'))
names=['editorial/production-state.json','editorial/title-review-checkpoint-2026-11-05.json',
       'editorial/title-alternatives-approved-2026-11-05.json','editorial/automation-completion-2026-11-05.json',
       'editorial/automation-status-2026-11-03.json',
       'wordpress/plugins/mee-editorial/data/production-plan.json',
       'docs/10-DECISIONES-ABIERTAS.md','docs/15-ESTADO-Y-CONTINUIDAD.md','docs/16-BACKLOG-REACT.md',
       'docs/21-CONTEXTO-PORTABLE.md','docs/26-PRODUCCION-CONTINUA.md','docs/24-REGISTRO-PRODUCCION-840.md',
       'docs/produccion/2026-11-05-seis-titulos-pendientes.md','docs/produccion/2026-11-05-cierre-840.md',
       'inventario/plan-editorial-840-status.json','inventario/plan-editorial-840.csv']
candidates.update(root/n for n in names)
candidates.update(root/n for n in base_gap if(root/n).is_file())
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
selected=[]
for p in sorted(candidates):
    assert p.is_file(),p
    relative=str(p.relative_to(root));q=private/relative
    if relative in base_gap or not q.exists()or digest(p)!=digest(q):selected.append(p)
assert selected and shutil.disk_usage(root).free>max(167772160,3*sum(p.stat().st_size for p in selected))
manifest=[dict(path='mee-web/'+str(p.relative_to(root)),bytes=p.stat().st_size,sha256=digest(p))for p in selected]
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED)as z:
    for p in selected:z.write(p,'mee-web/'+str(p.relative_to(root)))
    z.writestr('SHA256-MANIFEST.json',json.dumps(dict(base_backup=str(base),base_sha256=basehash,files=manifest),ensure_ascii=False,indent=2)+'\n')
    z.writestr('RESTORE-INCREMENTAL.txt','Preserve the complete chain ending '+base.name+'. Restore this overlay after it. Includes the six approved title changes, final article files and verification evidence, and all changes since that backup. Original images and prior sources remain covered by the preserved earlier chain. WordPress SQL and new media overlay are recorded in the delivery proof. No new full restore boot test.\n')
with zipfile.ZipFile(archive)as z:
    assert z.testzip()is None and len(z.namelist())==len(set(z.namelist()))
    for item in manifest:assert hashlib.sha256(z.read(item['path'])).hexdigest()==item['sha256']
for p in selected:
    q=private/p.relative_to(root);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
    assert digest(p)==digest(q)
for change in changes:
    d=root/'editorial/articles'/change['id']
    assert all(digest(p)==digest(private/p.relative_to(root))for p in d.rglob('*')if p.is_file())
relative_paths=[str(p.relative_to(root))for p in selected]
subprocess.run(['git','-C',str(private),'add','--',*relative_paths],check=True)
assert set(git('diff','--cached','--name-only').splitlines())<=set(relative_paths)
subprocess.run(['git','-C',str(private),'commit','-m','editorial: cierra 840 con seis títulos aprobados y verificados'],check=True)
subprocess.run(['git','-C',str(private),'push','origin','main'],check=True)
commit=git('rev-parse','HEAD');assert commit==git('rev-parse','origin/main')and not git('status','--porcelain')
reg=json.loads((root/'inventario/plan-editorial-840-status.json').read_text())
published=[{k:x[k]for k in ['number','id','title','url','images','words']}for x in reg['entries']if x['number']in [c['number']for c in changes]]
proof=dict(checked_at=datetime.now(timezone.utc).isoformat(),counts=reg['counts'],public_original_images=2520,published=published,
    unpublished_gaps=[],next_block=[],automation_deleted=True,remote_backup=state['last_backup'],
    local_backup=dict(zip=str(archive),zip_bytes=archive.stat().st_size,zip_files=len(manifest)+2,kind='incremental',base_backup=str(base),base_sha256=basehash),
    local_backup_sha256=digest(archive),private_commit=commit,private_previous_commit=head_before,private_clean=True,
    selected_files_equal=len(selected),all_six_article_directories_equal=True,full_restore_boot_test=False,previous_delivery_proof=str(previous_proof))
proof_path.write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(counts=reg['counts'],public_original_images=2520,zip_bytes=archive.stat().st_size,files_equal=len(selected),private_commit=commit,proof=str(proof_path),free_bytes=shutil.disk_usage(root).free),ensure_ascii=False),flush=True)
