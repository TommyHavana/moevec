from pathlib import Path
from datetime import datetime,timezone
import json,shutil,sys

r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web')
sys.path.insert(0,str(r/'scripts'))
from atomic_export import atomic_export

reg=json.load(open(r/'inventario/plan-editorial-840-status.json'))
s=json.load(open(r/'editorial/production-state.json'))
out=r/'inventario/auditoria-2026-10-28'
backup=json.load(open(out/'editorial-839-840-backup.json'))
org=json.load(open(out/'editorial-839-840-organization.json'))
nav=json.load(open(out/'editorial-839-840-navigation.json'))
rows=[x for x in reg['entries']if 839<=x['number']<=840]
assert len(rows)==len(org)==len(nav)==2 and all(x['ok']for x in org)
assert all(x['status']=='terminada'and x['images']==3 for x in rows)
assert reg['counts']=={'terminada':834,'en curso':0,'pendiente':6}
held=[x for x in reg['entries']if x['status']!='terminada']
assert [x['number']for x in held]==[501,512,649,707,769,818]
now=datetime.now(timezone.utc).isoformat()
exports=[]
def j(p,x):exports.append((p,json.dumps(x,ensure_ascii=False,indent=2)+'\n'))
def table(rs):return '| Global | ID | URL | Imágenes |\n|---|---|---|---|\n'+''.join(f"| {x['number']} | {x['id']} | {x['url']} | 3/3 |\n"for x in rs)

words=[]
for row in rows:
 d=r/'editorial/articles'/row['id']
 v=json.load(open(d/'verification.json'));assert not v['issues']and len(v['images'])==3
 words.append(json.load(open(d/'source-review.json'))['text_checks']['main_words'])
 for name in ['research.json','metadata-draft.json','source-preparation.json']:
  x=json.load(open(d/name));x.update(phase='published_verified',published=True,article_complete=True,images_complete=True,sources_verified=True,review_status='PUBLISHED_VERIFIED',pending=[],verified_at=now);j(d/name,x)
 exports.append((d/'review.md',(d/'review.md').read_text()+'\n## Publicación comprobada\n\nHTTP200, H1, canonical, indexabilidad, Article, tres originales con alt y hash, imágenes renderizadas, índice, BreadcrumbList, sitemap y enlaces existentes comprobados. Una publicación y tres adjuntos por ID; categorías y etiquetas del plan, taxonomía122/7. No acredita indexación efectiva ni una nueva prueba de restauración completa.\n'))

summary='**834/840 terminadas, 2502 imágenes originales públicas, 0 en curso o borradores WordPress y 6 pendientes**. Salud mental15/15. El número global840 está publicado; el plan completo sigue abierto por seis huecos anteriores.'
continuation='Próximo bloque por número global: **501/E4.2.06,512/E4.3.02 y649/E4.12.04**, después707/E6.6.02,769/E2.3.04 y818/E2.6.08. Las seis entradas están retenidas por afirmaciones de sus títulos originales sin respaldo suficiente; no se cambian títulos ni se publican sin resolver esa incompatibilidad. Las consultas específicas ya se enviaron una vez; no repetirlas ni tomar el silencio como aprobación. Conservar los textos y originales existentes y completar el trabajo independiente que falte. Mantener la automatización del mismo chat cada tres minutos; no declarar840/840 ni eliminarla todavía.'
review='Textos principales de1070 y1131 palabras; aperturas55/52, dos ejemplos hipotéticos y tresFAQ por entrada.839: OMS2022 recomendación organizativa condicional con evidencia de certeza muy baja, sin recomendación de cribado laboral; UNESCO mediante presentación, sin informe íntegro.840: OMSes2012 secciones delimitadas, NIMH general,024 verificado para España con enlaces conservados; aviso destacado, límites, urgencias y ausencia de promesas clínicas. Seis nativos y mosaico vistos. Detalles en source-review.json de cada expediente. Incidencia de plantilla ya registrada: dos meta descripciones idénticas; no se modifica el tema en esta producción.'
back=f"VPS `{backup['directory']}`: SQL vigente {backup['sql_bytes']} B, {backup['upload_files']} medios nuevos; cadena de{backup['overlays']} overlays más base. Cobertura completa de medios publicados y huecos501/512/649/707/769/818. Hashes y miembros comprobados, sin nueva prueba de arranque de restauración. ZIP local incremental y prueba de entrega externa conservan la cadena anterior."
nums=sorted(set(s.get('completed_this_run',[])+[839,840]));runrows=[x for x in reg['entries']if x['number']in nums]
report='# Bloque839–840 ·05/11/2026\n\n'+summary+'\n\n'+table(rows)+'\n## Revisión\n\n'+review+'\n\n## Continuación\n\n'+continuation+'\n'
exports.append((r/'docs/produccion/2026-11-05-bloque-839-840.md',report))
exports.append((r/'docs/produccion/2026-11-05-respaldo-839-840.md','# Respaldo839–840\n\n'+back+'\n'))
exports.append((r/f'docs/produccion/2026-11-05-ejecucion-desde-{s["run_started_with_completed"]}.md',f'# Ejecución desde{s["run_started_with_completed"]} ·05/11/2026\n\n'+summary+f'\n\n{len(nums)} nuevas entradas y{3*len(nums)} originales públicos.\n\n'+table(runrows)+'\n'+continuation+'\n'))
p=r/'docs/15-ESTADO-Y-CONTINUIDAD.md';old=p.read_text();tail=old[old.index('## Página de apoyo, donaciones y publicidad'):].split('\n\n## Punto exacto de capacidad ·03/11/2026')[0]
exports.append((p,'# Estado de MEE y continuidad ·05/11/2026 ·Europe/Madrid\n\n## Estado actual\n\n'+summary+'\n\nFuente activa `/Users/nerea/Documents/Proyectos/MEE/mee-web`.\n\n## Trabajo de esta ejecución\n\n'+f'Inicio{s["run_started_with_completed"]};{len(nums)} nuevas entradas y{3*len(nums)} originales públicos.\n\n'+table(runrows)+'\n## Revisión del último bloque\n\n'+review+'\n\n## Continuación exacta\n\n'+continuation+'\n\n## Copias y capacidad\n\n'+back+'\n\nUmbral operativo200MiB antes de cada imagen, copias proporcionales y conservación de originales. La automatización está activa cada tres minutos en el mismo chat; no duplicar procesos.\n\n'+tail))
p=r/'docs/16-BACKLOG-REACT.md';t=p.read_text();exports.append((p,'# Backlog de MEE\n\nÚltimo estado: '+summary+'\n\n'+continuation+'\n\n'+t[t.index('Historial anterior:'):].split('\n\n## Punto exacto de capacidad ·03/11/2026')[0]))
p=r/'docs/10-DECISIONES-ABIERTAS.md';exports.append((p,p.read_text()+'\n\n## Continuación editorial839–840 ·05/11/2026\n\n'+summary+'\n\n'+review+'\n\n'+continuation+'\n'))
p=r/'docs/26-PRODUCCION-CONTINUA.md';exports.append((p,p.read_text()+'\n\n## Punto de continuidad ·05/11/2026 ·839–840\n\n'+summary+'\n\n'+continuation+'\n'))
local=[x for x in s['local_preparations']if x['number']in s['title_reviews_pending']]
first=held[:3]
s.update(completed_this_run=nums,last_published_numbers=nums,last_completed_block=[839,840],current_block=[x['number']for x in first],current_ids=[x['id']for x in first],area=first[0]['area'],topic=first[0]['topic'],phase='awaiting_title_review',next_after_block=[707,769,818],updated_at=now,notes=summary+' '+continuation,last_backup=backup,local_preparations=local,heartbeat_interval_minutes=3)
s['storage_block'].update(phase='resolved_capacity_available'if shutil.disk_usage(r).free>=209715200 else'insufficient_local_storage',free_bytes=shutil.disk_usage(r).free,checked_at=now,completed=834,next_block=s['current_block'],next_images_ready=sum(x['images']for x in local if x['number']in s['current_block']),local_webps_ready=sum(x['images']for x in local),texts_ready=sum(x.get('article_complete',False)for x in local),sources_verified=False,body_drafts_ready=sum(x.get('body_complete',False)for x in local),current_reason='839–840 publicadas y verificadas; seis títulos retenidos, completar preparación independiente sin publicar ni cambiar títulos.',note='Conservar originales y copias; no reiniciar expedientes ni duplicar medios.')
s['resume_point']=dict(number=501,id='E4.2.06',next_action='await_existing_title_review_answer_and_finish_independent_preparations',accepted_images=3,article_complete=False,sources_verified=False,title_checked=False)
j(r/'editorial/production-state.json',s)
atomic_export(exports)
print(json.dumps(dict(counts=reg['counts'],next=s['current_block'],held=s['title_reviews_pending'],free_bytes=shutil.disk_usage(r).free)))
