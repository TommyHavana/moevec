from pathlib import Path
from datetime import datetime, timezone
import json

r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web')
plan=json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json'))
lines=(r.parent/'MEE_Plan_Editorial_840_entradas.md').read_text().splitlines()
style='Use case: stylized-concept. Original MEE editorial illustration in tactile layered cut paper, matte cobalt blue #1547BB, vivid red #EF383E, warm ivory #F7F6F2, soft studio light, generous margins. No text, digits, letters, logos, brands, flags, watermarks, currency signs, official seals, charts or UI. One independent original fictional scene. '
scenes={
 'E2.1.06':[
 ('Three fictional adult faceless ivory paper figures with differing adult heights behind a cobalt paper shop counter, plain red awning above, one plain ivory parcel on counter. No children, text, letters, logos, currency, real shop or measured profit. Landscape1200:630.','Tres figuras adultas ficticias detrás del mostrador de una tienda azul con toldo rojo.'),
 ('A cobalt paper round table with a stack of blank ivory pages neatly tied with one red paper ribbon, two plain chairs. No signatures, writing, official seal or legal validity implied. Landscape1600:900.','Mesa de papel con hojas en blanco unidas por una cinta roja.'),
 ('An abstract ivory paper tree whose cobalt branches end in red and ivory blank rectangular paper frames, several roots visible on warm ivory ground. No real family, text, people portraits, numbers or measured hierarchy. Landscape1600:900.','Árbol imaginario cuyas ramas terminan en recuadros vacíos, como metáfora de funciones familiares.')],
 'E2.1.07':[
 ('Two small imaginary cobalt and ivory paper city clusters separated by a wide empty red paper valley, connected by one soft ivory paper bridge with three tiny closed red paper envelopes resting on it. No real cities, borders, flags, currency, routes, data or promises. Landscape1200:630.','Dos ciudades imaginarias unidas por un puente con tres sobres rojos de papel.'),
 ('Two adult faceless ivory paper hands at opposite sides of a cobalt paper tabletop, one sliding a single closed red paper envelope toward the other open palm. No money visible, no bank interface, signature, currency, numbers or actual person. Landscape1600:900.','Dos manos adultas ficticias intercambian un sobre cerrado sobre una mesa azul.'),
 ('An imaginary small cobalt paper house with one completed lower level and an open unfinished ivory paper upper frame, one red paper door and three loose plain blocks beside it. No claim of actual housing outcomes, money, people, text, safety certification or technical building drawing. Landscape1600:900.','Casa imaginaria con planta baja azul y una estructura superior abierta junto a piezas de papel.')],
 'E2.1.08':[
 ('An adult smooth ivory paper hand gently holding an older adult ivory paper hand with subtle folded paper crease details, both resting above a cobalt paper table, one small red folded paper cloth nearby. Respectful invented adult scene, no injuries, medical diagnosis, actual patient, drugs, text or logos. Landscape1200:630.','Dos manos adultas ficticias se acompañan sobre una mesa azul; una tiene pliegues de papel visibles.'),
 ('A single upright ivory paper calendar-like grid of blank squares arranged in seven columns, some squares filled with red paper and some cobalt, standing on warm ivory ground. No digits, weekdays, dates, text, schedule prescribed or measured workload. Landscape1600:900.','Cuadrícula imaginaria de casillas vacías, rojas y azules, como metáfora de tareas compartidas.'),
 ('One small imaginary cobalt paper house with an ivory paper ramp leading gently to a single plain red doorway, one blank ivory window, warm ivory ground. No technical scale, regulatory compliance, actual dwelling, people, medical symbol, writing, digits or guarantee of accessibility. Landscape1600:900.','Casa azul imaginaria con una rampa de papel hacia la puerta roja.')]
}
for row in [x for x in plan if 741<=x['number']<=743]:
 ident=row['id'];d=r/'editorial/articles'/ident;assert not d.exists();d.mkdir();(d/'sources').mkdir()
 j=row['source_line']-1;assert ident in lines[j]
 k=next(n for n in range(j+1,len(lines)) if lines[n].startswith('#### ') or lines[n].startswith('# '))
 (d/'brief-original.md').write_text('\n'.join(lines[j:k]).strip()+'\n')
 tags=[row['topic'],{'Aplicación':'aplicacion','Fundamentos':'fundamentos','Desarrollo':'desarrollo'}[row['level']]]
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
