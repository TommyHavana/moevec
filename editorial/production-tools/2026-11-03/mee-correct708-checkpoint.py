from pathlib import Path
import json
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web')
p=r/'editorial/production-state.json';s=json.loads(p.read_text());s['title_reviews_pending']=[501,512,649,707]
plan=json.loads((r/'wordpress/plugins/mee-editorial/data/production-plan.json').read_text())
for number in s['title_reviews_pending']:
 if not any(x['number']==number for x in s['local_preparations']):
  row=next(x for x in plan if x['number']==number);d=r/'editorial/articles'/row['id'];research=json.loads((d/'research.json').read_text())
  s['local_preparations'].append(dict(number=number,id=row['id'],images=len(list(d.glob('*.webp'))),body_complete=research.get('body_complete',True),article_complete=research.get('article_complete',False),published=False,phase='title_review_pending',sources_verified=False,title_checked=False))
p.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
q=r/'docs/produccion/2026-11-03-correccion-cierre-708-710.md';assert not q.exists();q.write_text('''# Corrección del checkpoint 708–710 · 03/11/2026

El cierre 708–710 invocó por error el helper histórico de 31/10. Se conservan su ZIP y prueba de entrega, sin renombrarlos ni modificar sus hashes: `MEE_Editorial_708-710_2026-10-31_incremental.zip`, `produccion-708-710-entrega-20261031.json`, commit `672d8f07a1910968028837cd93d30d8fe4a9c76f`.

La fecha real de la producción y de la verificación fue 03/11/2026. El bloque dejó 706/840 completas y 2118 imágenes públicas, 0 borradores WordPress y 134 pendientes. Los cuatro huecos reales eran 501, 512, 649 y 707, todos por revisión de título. La prueba histórica enumera solo 501 y 512 por la versión antigua del helper; esa lista queda corregida por este documento y los checkpoints posteriores. Los expedientes locales de 649 y 707 se conservaron en disco, sin publicar ni borrar recursos; se restituyeron en `local_preparations` y se incluyen sus cambios en la siguiente copia.

El VPS de ese bloque es `/data/mee-backups/produccion-840-incremento-708-710-20261103`, con SQL de 27331292 bytes, 66 derivados nuevos, overlay de 1886048 bytes y 224 overlays más base. La cobertura de medios publicados se verificó; no hubo nueva prueba de arranque de restauración.

Se utiliza desde ahora el helper actual de `2026-11-03`. El siguiente cierre 711–713 reemplaza los documentos de estado y conserva esta corrección en el repositorio y el ZIP siguiente. No cambia el estado de WordPress ni cuenta borradores como completos.
''')
p=r/'editorial/production-tools/2026-11-03/mee-archive-block.py';t=p.read_text();needle="prior_candidates.extend((r/'inventario/auditoria-2026-10-28').glob(f'editorial-{start-3}-{end-3}-*.json'))";assert needle in t;t=t.replace(needle,needle+"\nprior_candidates.extend((r/'docs/produccion').glob('*.md'))");p.write_text(t)
print('Checkpoint: cuatro revisiones preservadas y corrección documental preparada.')
