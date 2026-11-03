from pathlib import Path
from datetime import datetime,timezone
import json,shutil
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');now=datetime.now(timezone.utc).isoformat();free=shutil.disk_usage(r).free
assert free<209715200,('La capacidad ha cambiado: continuar producción',free)
def write(p,a):p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
notes={
'E6.7.03':'Borrador principal de1125palabras, apertura53 yFAQ50/52/51; dos ejemplos hipotéticos. Falta interior-2, metadataSEO, revisión final, article.json y publicación. Portada e interior-1 ya aceptados: no regenerarlos. Dunbar1992: PDF25p escaneado, SOLO primera página/resumen leída e inspeccionada. Dunbar2014: resumen SAGE leído en web, hipótesis150 cognitiva y temporal, no tope empresarial. Lindenfors/Wartel/Lind2021: resumen XMLEuropePMC leído, CC-BY4; crítica a extrapolación con estimaciones distintas e intervalos amplios, no ausencia de todo límite. PMC web reCAPTCHA y DOI RoyalSoc403; no eludidos. API oficial EuropePMC OA20068986B archivada. Gore: cultura491–527 leída yHTML200; lattice, no límite actual150 por planta verificado. AWS: sección240–261 leída; menos10orientativo, foco, responsabilidad y límites de duplicación/silos; sin estadísticas secundarias citadas. Lecturas parciales explícitas, no artículos íntegros ni mediciones propias. Revisión final y fuentes al finalizar pendientes.',
'E6.7.04':'Brief y tres prompts conservados. Cero imágenes y sin texto. PDFGreiner1998 descargado200444373B; NO lectura íntegra ni inspección de todas sus páginas. HBR: límite25palabras derivadas del mismo trabajo, también si se consulta copia universitaria; no eludir usando otro URL. Verificar fases/fechas y preparar síntesis breve dentro del límite, con desarrollo propio de MEE. Contraparte primaria localizada: Phelps/Adams/Bessant2007, DOI correcto10.1111/j.1468-2370.2007.00200.x. Resumen apunta límites lineales, secuenciales y deterministas; falta lectura completa del resumen y archivo. No crecimiento inevitable ni misma secuencia para todas las organizaciones.',
'E6.7.05':'Brief y tres prompts conservados. Cero imágenes y sin texto. Ficha Penguin Scale200285069B leída: ebook16mayo2017/paperback15mayo2018, no libro496p íntegro ni sinopsis promocional como validación científica. Artículo primario de Hoffman/Yeh2018 TheBlitzscalingBasics descargado20058424B: solo inicio localizado, falta leer el cuerpo que se use. No presentar blitzscaling como rapidez irresponsable universal; conservar condiciones. PNAS2007 Growth innovation scaling and pace of life cities localizado y resumen leído en web, no artículo íntegro ni mismo exponente para ciudades/empresas. Falta fuente primaria sobre empresas si se contrastan con ciudades. Omitir fórmulas y cifras no verificadas.'}
for ident,note in notes.items():
 d=r/'editorial/articles'/ident
 (d/'research-notes.md').write_text('# Preparación e investigación · '+ident+'\n\n'+note+'\n\nEspacio inferior al mínimo operativo200MiB para nuevos originales. No hay agotamiento comunicado de image_gen.\n')
 for name in ['research.json','metadata-draft.json','source-preparation.json']:
  p=d/name;a=json.load(open(p));a.update(phase='images_pending_local_storage',article_complete=False,images_complete=False,sources_verified=False,body_draft_ready=ident=='E6.7.03',body_review_status='DRAFT_CLAIMS_CHECKED_FINAL_REVIEW_PENDING'if ident=='E6.7.03'else 'NOT_WRITTEN',images_generated=2 if ident=='E6.7.03'else 0,published=False,pending=['Recomprobar espacio >=209715200B antes de generar.','723: generar solo interior-2, conservar dos originales.724/725: tres imágenes y textos pendientes.','Completar metadatos, revisión y publicación de artículos completos.'],updated_at=now);write(p,a)
 write(d/'sources/reading-status-progress.json',dict(checked_at=now,final_sources_reviewed=False,full_books_read=False,full_papers_read=False,note=note))
p=r/'editorial/production-state.json';s=json.load(open(p));s.update(phase='images_pending_local_storage',updated_at=now,heartbeat_interval_minutes=3,resume_point=dict(number=723,id='E6.7.03',next_image='interior-2',accepted_images=2,body_draft_words=1125,body_draft_ready=True,article_json_exists=False,following=[724,725],reason='LOCAL_STORAGE_BELOW_OPERATIONAL_THRESHOLD',image_generation_quota_error=False))
for a in s['local_preparations']:
 if a['number']in[723,724,725]:a.update(images=2 if a['number']==723 else 0,article_complete=False,sources_verified=False,body_draft_ready=a['number']==723,phase='images_pending_local_storage')
s['storage_block'].update(phase='insufficient_local_storage',free_bytes=free,checked_at=now,resume_when_free_bytes_at_least=209715200,next_block=[723,724,725],next_images_ready=2,local_webps_ready=2,texts_ready=0,body_drafts_ready=1,sources_verified=False,completed=718,note='Precheck bloqueó generación con209588224B; tras recuperación temporal se completó interior-1 de723. Última medición'+str(free)+'B, inferior a209715200B.723:2/3originales y borrador1125palabras.724/725:0/3 y sin textos. No cuota image_gen. Próximo recurso:723 interior-2. Comprobar capacidad en próximo despertar de3min.');write(p,s)
text='''## Punto exacto de capacidad ·03/11/2026

WordPress: **718/840 terminadas,2154 imágenes originales públicas,0 borradores y122 pendientes**. Último bloque720–722 verificado y cerrado. Títulos retenidos501/512/649/707, sin publicar.

Preparación local723–725: **723/E6.7.03 tiene2/3WebP** y borrador principal1125palabras, apertura53, FAQ50/52/51; sin article.json ni publicación. Próximo recurso: **interior-2**. Conservar portada e interior-1. **724/E6.7.04 y725/E6.7.05:0/3 imágenes, sin texto**, con briefs, prompts y fuentes iniciales. Alcance de lectura y pendientes en cada expediente.

La comprobación previa bloqueó una generación a209588224B. Tras una recuperación temporal se generó la segunda imagen de723. Última medición antes de respaldo: FREEB; mínimo de generación209715200B. No error de cuota de image_gen. No se han borrado originales ni copias. Se conserva copia incremental de esta preparación referida al cierre720–722.

Automatización activa cada tres minutos en el mismo chat. Al disponer de capacidad, reanudar723 interior-2 y completar723–725; después726–728. No duplicar procesos ni publicaciones.
'''.replace('FREE',str(free))
(r/'docs/produccion/2026-11-03-punto-723-capacidad.md').write_text('# Preparación723–725 y capacidad local\n\n'+text)
for n in ['docs/15-ESTADO-Y-CONTINUIDAD.md','docs/16-BACKLOG-REACT.md','docs/10-DECISIONES-ABIERTAS.md','docs/26-PRODUCCION-CONTINUA.md','docs/produccion/2026-11-03-ejecucion-desde-586.md']:
 q=r/n;q.write_text(q.read_text()+'\n\n'+text)
print(json.dumps(dict(free_bytes=free,counts={'terminada':718,'en curso':0,'pendiente':122},next_image='723/E6.7.03 interior-2')))
