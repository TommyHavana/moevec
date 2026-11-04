"""Preserve partial editorial work remotely without needing another local ZIP."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,io,json,shlex,subprocess,zipfile,shutil
from atomic_export import atomic_export

r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');private=r.parent/'mee-deploy-source'
state=json.load(open(r/'editorial/production-state.json'))
assert state['current_block']==[738,739,740]
selected=[];natives=[]
for ident in state['current_ids']:
    directory=r/'editorial/articles'/ident
    selected.extend(p for p in directory.rglob('*') if p.is_file())
    record=directory/'image-generation-record.json'
    if record.exists():
        natives.extend(Path(x['native_path']) for x in json.load(open(record)))
selected.extend(p for p in (r/'editorial/production-tools/2026-11-04').glob('*') if p.is_file())
selected.extend(r/p for p in ['editorial/production-state.json','docs/26-PRODUCCION-CONTINUA.md'])
selected=sorted(set(selected))
selected=[p for p in selected if not(private/p.relative_to(r)).exists() or hashlib.sha256(p.read_bytes()).digest()!=hashlib.sha256((private/p.relative_to(r)).read_bytes()).digest()]
items=[(p,'mee-web/'+str(p.relative_to(r))) for p in selected]
items.extend((p,'native-images/'+p.name) for p in sorted(set(natives)))
manifest=[dict(path=name,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p,name in items]
assert len({x['path'] for x in manifest})==len(manifest)
memory=io.BytesIO()
with zipfile.ZipFile(memory,'w',zipfile.ZIP_DEFLATED) as archive:
    for p,name in items:archive.write(p,name)
    archive.writestr('SHA256-MANIFEST.json',json.dumps(dict(previous_delivery_proof=state['last_delivery_proof'],completed=733,partial_block=[738,739,740],files=manifest),ensure_ascii=False,indent=2)+'\n')
payload=memory.getvalue();sha=hashlib.sha256(payload).hexdigest()
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
destination='/data/mee-backups/produccion-840-progreso-738-740-'+stamp
remote='''import sys,pathlib,hashlib,zipfile,io,json,os
os.umask(0o077)
d=pathlib.Path(DESTINATION);d.mkdir(mode=0o700)
b=sys.stdin.buffer.read();assert hashlib.sha256(b).hexdigest()==EXPECTED
with zipfile.ZipFile(io.BytesIO(b)) as z:
 assert z.testzip() is None
 m=json.loads(z.read('SHA256-MANIFEST.json'))
 for x in m['files']:
  data=z.read(x['path']);assert len(data)==x['bytes'] and hashlib.sha256(data).hexdigest()==x['sha256']
p=d/'progress.zip';p.write_bytes(b)
(d/'SHA256SUMS').write_text(EXPECTED+'  progress.zip\\n')
print(json.dumps(dict(directory=str(d),file=str(p),bytes=len(b),sha256=EXPECTED,files=len(m['files']),native_images=sum(x['path'].startswith('native-images/') for x in m['files']),verified=True)))
'''.replace('DESTINATION',repr(destination)).replace('EXPECTED',repr(sha))
result=subprocess.run(['ssh','-o','BatchMode=yes','calicata-root','python3 -c '+shlex.quote(remote)],input=payload,capture_output=True,check=True)
proof=json.loads(result.stdout);proof.update(local_free_bytes=shutil.disk_usage(r).free,private_copy_pending_for_partial=True)
state['last_partial_remote_checkpoint']=proof
atomic_export([(r/'editorial/production-state.json',json.dumps(state,ensure_ascii=False,indent=2)+'\n')])
print(json.dumps(proof,ensure_ascii=False))
