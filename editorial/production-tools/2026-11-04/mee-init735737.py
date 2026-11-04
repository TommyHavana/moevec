from pathlib import Path
from datetime import datetime, timezone
import json

r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web')
plan=json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json'))
lines=(r.parent/'MEE_Plan_Editorial_840_entradas.md').read_text().splitlines()
style='Use case: stylized-concept. Original MEE editorial illustration in tactile layered cut paper, matte cobalt blue #1547BB, vivid red #EF383E, warm ivory #F7F6F2, soft studio light, generous margins. No text, digits, letters, logos, brands, flags, watermarks, currency signs, official seals, charts or UI. One independent original fictional scene. '
scenes={
 'E6.7.15':[
  ('A honeycomb-shaped architectural paper plan lying on a simple cobalt worktable, a short red pencil beside it, no drawn text, scales, technical claims or real blueprint. Landscape1200:630.', 'Plano simbólico de panal sobre una mesa azul con un lápiz rojo, sin medidas ni instrucciones técnicas.'),
  ('One simple cobalt paper chest at the centre of an ivory ground, with exactly three separate red paper keys resting neatly around it. No real lock mechanism or security promises. Landscape1600:900.', 'Cofre azul imaginario con tres llaves rojas, como metáfora de responsabilidades compartidas.'),
  ('A loose cluster of seven large cobalt paper honeycomb cells, three softly lit from within by warm ivory light, others in cobalt shade. No measured sequence, arrow, chart, text or glowing digital UI. Landscape1600:900.', 'Celdas de un panal de papel con distintas iluminaciones, como metáfora de una organización que aprende.')],
 'E2.1.01':[
  ('Two equally respected adult faceless ivory paper figures cooperating: one holds a broad cobalt paper ladder securely while the other climbs one low step, red paper ground. No child, burdened body, injury, forced labour or guaranteed promise of reciprocity. A fictional shared effort metaphor. Landscape1200:630.', 'Dos figuras adultas ficticias colaboran con una escalera azul, como metáfora de apoyo acordado.'),
  ('Exactly three separate simple red paper keys lying before a single open cobalt paper doorway, warm ivory ground, soft shadows. No text, locks, branded key, legal rights or guaranteed access. Landscape1600:900.', 'Tres llaves rojas ante una puerta azul abierta, como metáfora de condiciones para colaborar.'),
  ('A small round cobalt paper table with one loose red paper cord tied in a simple visible knot resting at its centre, two unmarked ivory cards beside it. No people bound, contract text or signatures. Agreement metaphor only. Landscape1600:900.', 'Una cuerda roja anudada sobre una mesa con tarjetas sin texto, como metáfora de un acuerdo revisable.')],
 'E2.1.02':[
  ('A cutaway fictional cobalt paper home with large simple ivory paper gears integrated into one wall, two adult faceless ivory paper figures sharing everyday tasks, red details. No actual family, gender-role ranking, measured output or brand. Landscape1200:630.', 'Casa imaginaria con engranajes de papel y dos figuras adultas que comparten tareas domésticas.'),
  ('An ivory paper kitchen table, a single flat cobalt paper sheet with simple unmarked geometric shapes as a planning sketch, a red pencil and one plain cup. No text, numbers, food measurements, real floorplan or financial data. Landscape1600:900.', 'Mesa de cocina imaginaria con una hoja de planificación sin texto, un lápiz y una taza.'),
  ('Two equal-sized faceless adult ivory paper hands, from opposite sides, distributing six large blank cobalt and red round paper tokens evenly on ivory ground. No ledger, digits, clock, currency, real data or implied scientific fairness score. Landscape1600:900.', 'Dos manos ficticias reparten fichas de colores sin cifras, como metáfora de una conversación sobre tareas.')]
}
for row in [x for x in plan if 735<=x['number']<=737]:
 ident=row['id'];d=r/'editorial/articles'/ident;assert not d.exists();d.mkdir();(d/'sources').mkdir()
 j=row['source_line']-1;assert ident in lines[j]
 k=next(n for n in range(j+1,len(lines)) if lines[n].startswith('#### ') or lines[n].startswith('# '))
 (d/'brief-original.md').write_text('\n'.join(lines[j:k]).strip()+'\n')
 tags=[row['topic'],{'Aplicación':'aplicacion','Fundamentos':'fundamentos'}[row['level']]]
 x=dict(row,planned_tags=tags,phase='research_preparation_images_pending',article_complete=False,sources_verified=False,images_complete=False,images_generated=0,published=False,images_visually_checked=False,review_status='RESEARCH_PENDING',pending=['Fuentes primarias, tres originales, texto y revisión.','Publicación y comprobación pública.'],updated_at=datetime.now(timezone.utc).isoformat())
 prompts={};images={}
 for role,(scene,alt) in zip(['featured','interior-1','interior-2'],scenes[ident]):
  f=ident.lower().replace('.','-')+('-destacada.webp' if role=='featured' else '-'+role+'.webp')
  prompts[role]=dict(prompt=style+scene,file=f,width=1200 if role=='featured' else 1600,height=630 if role=='featured' else 900)
  images[role]=dict(file=f,title=alt,alt=alt,caption='')
 for name,obj in [('research.json',x),('metadata-draft.json',dict(x,images=images)),('image-prompts.json',prompts),('source-preparation.json',dict(id=ident,phase='RESEARCH_PENDING',sources_verified=False,article_complete=False,images_complete=False))]:
  (d/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
 (d/'research-notes.md').write_text('# Preparación · '+ident+'\n\nBrief y prompts conservados; investigación en curso, sin publicación.\n')
 print(ident,row['number'],tags)
