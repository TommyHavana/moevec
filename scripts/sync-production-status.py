#!/usr/bin/env python3
"""Read production WordPress and export the complete numbered status, without writing to it."""
import csv, io, json, re, subprocess
from datetime import datetime, timezone
from pathlib import Path
from atomic_export import atomic_export

root=Path(__file__).resolve().parents[1]
container=subprocess.check_output(['ssh','-o','BatchMode=yes','calicata-root','docker ps -q --filter label=coolify.applicationUuid=h7kfs9qe620lg5mqip36npt4 --filter label=com.docker.compose.service=wordpress'],text=True).strip()
if not re.fullmatch('[0-9a-f]+',container): raise RuntimeError('No se identificó un único WordPress')
php="""<?php
require '/var/www/html/wp-load.php';
$rows=mee_production_snapshot();
$samples=get_posts(['post_type'=>'post','post_status'=>'publish','posts_per_page'=>-1,'fields'=>'ids','meta_key'=>'_mee_demo','meta_value'=>'1']);
echo json_encode(['checked_at'=>gmdate('c'),'published_samples'=>count($samples),'entries'=>$rows],JSON_UNESCAPED_SLASHES|JSON_UNESCAPED_UNICODE);
"""
result=subprocess.run(['ssh','-o','BatchMode=yes','calicata-root',f'docker exec -i --user 33:33 {container} php'],input=php,text=True,capture_output=True,check=True)
report=json.loads(result.stdout)
rows=report['entries']
assert len(rows)==840 and len({row['id'] for row in rows})==840
counts={state:sum(row['status']==state for row in rows) for state in ['terminada','en curso','pendiente']}
report['counts']=counts
csv_text=io.StringIO(newline='')
writer=csv.DictWriter(csv_text,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
lines=['# MEE · Registro numerado de las 840 entradas','',f"Comprobado en WordPress: {report['checked_at']}.",'',f"**{counts['terminada']}/840 terminadas · {counts['en curso']} en curso · {counts['pendiente']} pendientes.**",'',f"Maquetas publicadas: **{report['published_samples']}**.",'','Una entrada terminada debe estar publicada, revisada y tener al menos 600 palabras y tres imágenes WebP propias y distintas con texto alternativo: portada + dos interiores. La comprobación del registro verifica publicación, marca de revisión, extensión y tres archivos; la revisión editorial del texto y las escenas se registra por artículo.','', '[Registro en WordPress](https://moevec.org/blog/wp-admin/tools.php?page=mee-production) · [CSV completo](../inventario/plan-editorial-840.csv)','', '| N.º /840 | Tanda /56 · entrada /15 | ID | Título | Estado | Imágenes | URL |','|---:|---|---|---|---|---:|---|']
for row in rows:
    title=row['title'].replace('|','\\|')
    url=f"[Leer]({row['url']})" if row['url'] else '—'
    lines.append(f"| {row['number']} | {row['batch']}/56 · {row['entry']}/15 | {row['id']} | {title} | {row['status']} | {row['images']}/3 | {url} |")
atomic_export([
    (root/'inventario/plan-editorial-840-status.json',json.dumps(report,ensure_ascii=False,indent=2)+'\n'),
    (root/'inventario/plan-editorial-840.csv',csv_text.getvalue()),
    (root/'docs/24-REGISTRO-PRODUCCION-840.md','\n'.join(lines)+'\n'),
])
print(json.dumps({'checked_at':report['checked_at'],'counts':counts,'published_samples':report['published_samples'],'completed':[{'number':row['number'],'id':row['id'],'url':row['url'],'images':row['images'],'words':row['words']} for row in rows if row['status']=='terminada']},ensure_ascii=False,indent=2))
