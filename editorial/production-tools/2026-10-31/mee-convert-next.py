from pathlib import Path
from datetime import datetime,timezone
from PIL import Image,ImageOps
import json,hashlib,sys,shutil,os
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');i,role,src=sys.argv[1:4];d=r/'editorial/articles'/i;src=Path(src);assert src.is_file();pr=json.load(open(d/'image-prompts.json'))[role];file=d/pr['file'];assert not file.exists();native=src
im=ImageOps.fit(Image.open(src).convert('RGB'),(pr['width'],pr['height']),method=Image.Resampling.LANCZOS);im.save(file,format='WEBP',quality=83,method=6);assert file.stat().st_size<250000
p=d/'image-generation-record.json';records=json.load(open(p))if p.exists()else[];assert role not in[x['role']for x in records];records.append(dict(role=role,native_path=str(native),native_generated_path=str(src),native_sha256=hashlib.sha256(native.read_bytes()).hexdigest(),file=file.name,bytes=file.stat().st_size,sha256=hashlib.sha256(file.read_bytes()).hexdigest(),width=pr['width'],height=pr['height'],quality=83,prompt=pr['prompt'],tool='image_gen',visually_checked=True,native_local_complete=True,webp_complete=True))
def write(p,x):
 t=p.with_name(p.name+'.pending');assert not t.exists();t.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');t.replace(p)
write(p,records)
for name in['research.json','metadata-draft.json']:
 p=d/name;x=json.load(open(p));x.update(images_generated=len(records),images_complete=len(records)==3,images_visually_checked=len(records)==3,phase='research_preparation_images_ready'if len(records)==3 else'research_and_images_in_progress');write(p,x)
s=json.load(open(r/'editorial/production-state.json'))
for x in s['local_preparations']:
 if x['id']==i:x.update(images=len(records),images_visually_checked=len(records)==3,phase='research_preparation_images_ready'if len(records)==3 else'research_and_images_in_progress')
s.update(updated_at=datetime.now(timezone.utc).isoformat());s['storage_block'].update(free_bytes=shutil.disk_usage(r).free,next_images_ready=sum(x['images']for x in s['local_preparations']if x['number']in s['current_block']));write(r/'editorial/production-state.json',s);print(json.dumps(dict(id=i,role=role,images=len(records),bytes=file.stat().st_size,free_bytes=shutil.disk_usage(r).free)))
