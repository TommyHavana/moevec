from pathlib import Path
import subprocess,zipfile,io,hashlib,json,sys,shutil
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');private=r.parent/'mee-deploy-source'
assert shutil.disk_usage(r).free>=209715200
reg=json.load(open(r/'inventario/plan-editorial-840-status.json'));assert reg['counts']=={'terminada':819,'en curso':0,'pendiente':21}
remote='/data/mee-backups/produccion-840-progreso-824-826-20261105T014105Z'
raw=subprocess.check_output(['ssh','-o','BatchMode=yes','calicata-root','cat '+remote+'/progress.zip'])
assert hashlib.sha256(raw).hexdigest()=='de9270a08c47507ffdd2e6386e31f6c844d94a8b75b8dcaa88b3f3913329a699'
z=zipfile.ZipFile(io.BytesIO(raw));assert z.testzip()is None
m=json.loads(z.read('SHA256-MANIFEST.json'));assert all(hashlib.sha256(z.read(x['path'])).hexdigest()==x['sha256']for x in m['files'])
backup=r.parent/'mee-backups/MEE_Editorial_824-826_checkpoint_2026-11-05.zip';assert not backup.exists();backup.write_bytes(raw)
selected=['editorial/production-state.json','docs/15-ESTADO-Y-CONTINUIDAD.md','docs/16-BACKLOG-REACT.md','docs/10-DECISIONES-ABIERTAS.md','docs/26-PRODUCCION-CONTINUA.md','docs/produccion/2026-11-05-bloque-824-826-parcial.md','docs/produccion/2026-11-05-respaldo-824-825.md']
for name in selected:
 p=r/name
 if name.startswith('docs/')and p.exists():assert p.read_bytes()==(private/name).read_bytes(),name
for ident in ['E2.6.14','E2.6.15']:
 d=r/'editorial/articles'/ident;v=json.load(open(d/'verification.json'));assert not v['issues']and len(v['images'])==3
 assert (d/'article.html').read_bytes()==z.read('editorial/articles/'+ident+'/article.html')
 selected.extend('editorial/articles/'+ident+'/'+n for n in ['research.json','metadata-draft.json','source-preparation.json','review.md'])
s=json.loads(z.read('editorial/production-state.json'));assert s['resume_point']['number']==826 and s['last_partial_block']['completed']==[824,825]
s['storage_block'].update(phase='resolved_capacity_available',free_bytes=shutil.disk_usage(r).free,current_reason='Capacidad recuperada; reanudar última imagen826 sin repetir recursos.',originals_and_backups_preserved=True)
s['last_partial_remote_checkpoint'].update(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),verified=True,local_checkpoint=str(backup),local_final_export_status='recovered')
sys.path.insert(0,str(r/'scripts'));from atomic_export import atomic_export
exports=[(r/n,json.dumps(s,ensure_ascii=False,indent=2)+'\n'if n=='editorial/production-state.json'else z.read(n).decode())for n in selected]
atomic_export(exports)
print(json.dumps(dict(recovered_exports=len(exports),checkpoint_bytes=len(raw),free_bytes=shutil.disk_usage(r).free)))
