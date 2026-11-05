from pathlib import Path
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import hashlib, json, re, shutil, sys

root=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(root/'scripts'))
from atomic_export import atomic_export
stamp=datetime.now(timezone.utc).isoformat()
reg=json.loads((root/'inventario/plan-editorial-840-status.json').read_text())
assert reg['counts']=={'terminada':840,'en curso':0,'pendiente':0} and reg['published_samples']==0
assert len(reg['entries'])==len({x['id']for x in reg['entries']})==840
assert sum(x['images']for x in reg['entries'])==2520
approval=json.loads((root/'editorial/title-alternatives-approved-2026-11-05.json').read_text())
changes=approval['changes'];ids=[x['id']for x in changes]
backup=json.loads((root/'inventario/auditoria-2026-10-28/editorial-approved-six-backup.json').read_text())
assert backup['completed_articles']==840 and backup['checksums_verified']and backup['archive_verified']and backup['published_media_coverage_complete']
for block in [1,2]:
    report=json.loads((root/f'inventario/auditoria-2026-10-28/editorial-approved-six-block-{block}-verification.json').read_text())
    assert len(report['basic'])==3 and all(not x['issues']and x['images']==3 for x in report['basic'])
completion=json.loads((root/'editorial/automation-completion-2026-11-05.json').read_text())
assert completion['deleted']and completion['automation_id']=='producci-n-editorial-mee-840'
rows=[next(x for x in reg['entries']if x['id']==ident)for ident in ids]
table='| Global | ID | Título aprobado | URL | Imágenes |\n|---|---|---|---|---|\n'+'\n'.join('| '+str(x['number'])+' | '+x['id']+' | '+x['title']+' | '+x['url']+' | 3/3 |'for x in rows)+'\n'
summary='**840/840 terminadas, 2520 imágenes originales públicas, 0 en curso y 0 pendientes.** Las seis alternativas fueron aprobadas explícitamente por el fundador, publicadas y verificadas. Se conservan todos los identificadores y slugs; el plan editorial queda cerrado y la automatización eliminada.'
detail='# Cierre del plan editorial ·840/840 ·05/11/2026\n\n'+summary+'\n\n## Seis huecos cerrados\n\n'+table+'\n## Revisión y comprobaciones\n\n- Títulos aprobados en `editorial/title-alternatives-approved-2026-11-05.json`; el manifiesto local y el de WordPress solo cambian esos seis títulos. Copia anterior conservada.\n- Textos y 18 imágenes existentes reutilizados para terminar sus propios expedientes, sin generación adicional. Cuerpos principales de1260,1261,1090,1211,1081 y1078 palabras; aperturas40–60, dos ejemplos hipotéticos y tresFAQ de40–70 palabras por artículo. Corregidos encabezados HTML y metadatos pendientes.\n- Fuentes primarias y alcances por expediente; lecturas parciales y fallos de recuperación identificados, sin fingir documentos completos o asesoramiento individual.\n- HTTP200,H1,canonical,indexabilidad,Article,TOC,tresWebP/alt/hash/dimensiones/recursos renderizados,navegación,BreadcrumbList,sitemap,enlaces internos200,SEO y organización comprobados. Taxonomía122 nodos/7 raíces, sin cambios de categorías.\n- Firma públicaAnacleto yautor de schemaMEEEditorial conforme a la plantilla existente. Persisten dos meta descripciones idénticas de plantilla, incidencia previa fuera de producción; no se modificó el tema. Indexabilidad comprobada, sin afirmar indexación efectiva en buscadores.\n\n## Conservación\n\nRespaldo VPS: `'+backup['directory']+'`, SQL consistente de'+str(backup['sql_bytes'])+' bytes, '+str(backup['upload_files'])+' archivos de medios nuevos y18 originales, archivo de'+str(backup['uploads_bytes'])+' bytes. Hashes y extracción comprobados; cadena previa más este incremento conserva la cobertura de las840 publicaciones. Se incluye el manifiesto con los seis títulos aprobados. Sin prueba nueva de arranque de restauración completa.\n\nLa copia privada y el ZIP incremental final se documentan en `../mee-backups/produccion-cierre-840-entrega-20261105.json`. La cadena completa de respaldos y todos los originales se conservan. No se cambió DNS, correo, autenticación, tema o taxonomía.\n\n## Seguimiento\n\nAutomatización `producci-n-editorial-mee-840` eliminada mediante la herramienta de la aplicación después de verificar840/840. Evidencia: `editorial/automation-completion-2026-11-05.json`. No hay próximo bloque.\n'
outputs=[(root/'docs/produccion/2026-11-05-cierre-840.md',detail)]
for row in rows:
    d=root/'editorial/articles'/row['id']
    for name in ['research.json','metadata-draft.json','source-preparation.json','source-review.json']:
        p=d/name;x=json.loads(p.read_text())
        x.update(phase='published_verified',published=True,article_complete=True,sources_verified=True,title_checked=True,title_approved=True,
                 images_complete=True,images_visually_checked=True,review_status='PUBLISHED_VERIFIED',pending=[],updated_at=stamp,url=row['url'],public_verification=True)
        x.pop('publication_blocked',None)
        if name=='metadata-draft.json':
            a=json.loads((d/'article.json').read_text());x.update({k:a[k]for k in ['title','seo_title','description','keyword','secondary_keywords','standfirst','tags','images']})
        if name=='source-review.json':
            x['archived_files']=[dict(file=str(f.relative_to(d)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest())for f in sorted((d/'sources').rglob('*'))if f.is_file()]
            x['next_action']='none_plan_complete'
            x['text_checks']['description_characters']=len(json.loads((d/'article.json').read_text())['description'])
        outputs.append((p,json.dumps(x,ensure_ascii=False,indent=2)+'\n'))
    old=(d/'review.md').read_text().replace('- Publicación y comprobación pública pendientes.','- Publicación y comprobación pública completas: '+row['url']+'; imágenes3/3 y organización conforme al plan.')
    outputs.append((d/'review.md',old))
cp_path=root/'editorial/title-review-checkpoint-2026-11-05.json';cp=json.loads(cp_path.read_text())
for held in cp['held']:
    row=next(x for x in rows if x['id']==held['id']);pub=json.loads((root/'editorial/articles'/held['id']/'publication.json').read_text())
    held.update(published=True,title_checked=True,title_approved=True,article_complete=True,requires_final_metadata_review=False,url=row['url'],post_id=pub['post_id'],public_verification=True)
cp.update(counts=reg['counts'],public_original_images=2520,next_block=[],automation_active=False,closed_at=stamp,phase='complete')
outputs.append((cp_path,json.dumps(cp,ensure_ascii=False,indent=2)+'\n'))
state_path=root/'editorial/production-state.json';state=json.loads(state_path.read_text())
state.update(phase='complete',current_block=[],current_ids=[],next_after_block=[],title_reviews_pending=[],
    updated_at=stamp,completed_at=stamp,counts=reg['counts'],public_original_images=2520,automation_active=False,
    last_completed_block=[707,769,818],approved_title_completed_numbers=[x['number']for x in rows],last_backup=backup,
    notes=summary,last_run_closed_at_madrid=datetime.now(ZoneInfo('Europe/Madrid')).isoformat(),
    resume_point=dict(next_action='none_plan_complete',completed=840,pending=0),delivery_status='final_local_archive_pending')
state['completed_this_run']=sorted(set(state.get('completed_this_run',[]))|{x['number']for x in rows})
state['last_published_numbers']=sorted(set(state.get('last_published_numbers',[]))|{x['number']for x in rows})
state['resolved_title_reviews']=state.pop('title_review_pending',[])
state['storage_check'].update(free_bytes=shutil.disk_usage(root).free,checked_at=stamp,originals_and_backups_preserved=True)
for x in state['local_preparations']:
    if x['id']in ids:x.update(published=True,phase='published_verified',article_complete=True,title_checked=True,sources_verified=True,public_verification=True)
state['storage_block'].update(current_reason='Plan840/840 verificado, sin siguiente bloque.',phase='resolved_plan_complete')
outputs.append((state_path,json.dumps(state,ensure_ascii=False,indent=2)+'\n'))
for name in ['docs/15-ESTADO-Y-CONTINUIDAD.md','docs/16-BACKLOG-REACT.md']:
    p=root/name;text=p.read_text()
    pattern=r'(?:Último estado: )?\*\*834/840 terminadas[^\n]+'
    text,count=re.subn(pattern,summary,text,count=1);assert count==1
    if name.endswith('16-BACKLOG-REACT.md'):
        text=re.sub(r'Próximo bloque por número global:.*?(?=\n\n)', 'Plan cerrado: las entradas501,512,649,707,769 y818 están publicadas con los títulos aprobados y3/3 imágenes. No hay próximo bloque. Detalle en `docs/produccion/2026-11-05-cierre-840.md`.',text,count=1,flags=re.S)
    text+='\n\n## Cierre verificado ·05/11/2026\n\n'+summary+'\n\n'+table+'\nDetalle y límites: `docs/produccion/2026-11-05-cierre-840.md`. La documentación anterior conserva el historial de producción; las esperas de título quedan resueltas.\n'
    outputs.append((p,text))
for name in ['docs/10-DECISIONES-ABIERTAS.md','docs/26-PRODUCCION-CONTINUA.md','docs/21-CONTEXTO-PORTABLE.md']:
    p=root/name;outputs.append((p,p.read_text()+'\n\n## Cierre editorial ·05/11/2026\n\n'+summary+'\n\nTítulos definitivos y comprobaciones en `docs/produccion/2026-11-05-cierre-840.md`. Los seis originales de título permanecen documentados en la aprobación y en los briefs; ID y slugs se conservan. No hay próximo bloque ni seguimiento de producción activo.\n'))
outputs.append((root/'docs/produccion/2026-11-05-seis-titulos-pendientes.md','# Seis títulos resueltos y publicados ·05/11/2026\n\n'+summary+'\n\n'+table+'\nAprobación explícita: «usa todas las alternativas que preparaste creo que es lo mejor». Los18 originales se conservaron. Detalle de cierre: `2026-11-05-cierre-840.md`.\n'))
atomic_export(outputs)
print(json.dumps(dict(counts=reg['counts'],public_original_images=2520,closed_ids=ids,automation_deleted=True,remote_backup=backup['directory']),ensure_ascii=False))
