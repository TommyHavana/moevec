from pathlib import Path
from datetime import datetime, timezone
import json

r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web')
plan=json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json'))
lines=(r.parent/'MEE_Plan_Editorial_840_entradas.md').read_text().splitlines()
style='Use case: stylized-concept. Original MEE editorial illustration in tactile layered cut paper, matte cobalt blue #1547BB, vivid red #EF383E, warm ivory #F7F6F2, soft studio light, generous margins. No text, digits, letters, logos, brands, flags, watermarks, currency signs, official seals, charts or UI. One independent original fictional scene. '
scenes={
 'E2.1.12':[
 ('Four fictional adult ivory paper hands, one with subtle folded paper creases of an older adult, gathered around one cobalt table and one large blank ivory paper sheet. One plain red paper pen rests above the empty sheet, no ink marks or signatures. No real contract, legal validity, money, text, digits or official seals. Landscape1200:630.','Cuatro manos adultas ficticias junto a una hoja en blanco y un bolígrafo rojo sobre una mesa azul.'),
 ('One round layered ivory paper cake-like disc cleanly divided into three visibly unequal plain portions, separated slightly on a cobalt paper plate, red paper background accent. No values, numbers, percentages, food brand, actual ownership allocation or guaranteed fairness. Landscape1600:900.','Disco imaginario de papel dividido en tres porciones de tamaños diferentes sobre un plato azul.'),
 ('An imaginary flat ivory paper room plan made from three simple cobalt folded paper walls, one open red doorway and one broad blank ivory path leading out. No technical drawing, text, dimensions, building regulation, actual contract or guaranteed exit. Landscape1600:900.','Plano imaginario de paredes de papel con una puerta roja abierta y un camino hacia fuera.')],
 'E2.1.13':[
 ('One fictional faceless adult ivory paper figure standing between a tiny empty red paper cradle and an empty cobalt paper armchair, one open hand extended gently toward each symbolic object. No baby, actual patient, injury, impossible lifting, crisis, diagnosis, data or text. Landscape1200:630.','Figura adulta ficticia entre una cuna vacía roja y una silla azul, con las manos extendidas hacia ambas.'),
 ('One simple cobalt paper clock face divided into three blank irregular ivory and red paper sectors, two simple plain hands at centre, no digits or tick marks. Symbolic competing time needs only, no prescribed time allocation, measured hours, text or data. Landscape1600:900.','Reloj imaginario sin cifras dividido en tres sectores de papel de tamaños distintos.'),
 ('Four different fictional faceless adult ivory paper neighbours around a cobalt paper courtyard, one holding a blank red paper tote bag, one holding an ivory paper book, two exchanging a plain red paper basket. Respectful community coordination scene, no children, real group, text, logos, outcomes or guaranteed services. Landscape1600:900.','Cuatro figuras adultas ficticias en un patio de papel, con una bolsa, un libro y una cesta.')],
 'E2.1.14':[
 ('One simple cobalt paper balance with a small ivory paper family house with a red roof on one pan and a small abstract cobalt paper workshop with one red gear shape on the other, both at equal height. Conceptual comparison of housing exposure and business only. No actual mortgage, money, rates, approval, numbers, data, text or financial recommendation. Landscape1200:630.','Balanza imaginaria con una casa de techo rojo en un platillo y un pequeño taller de papel en el otro.'),
 ('One loose coil of thick red paper rope resting gently on warm ivory ground beside one plain cobalt paper peg. No attached people, restraints, dangerous action, certification, guaranteed safety, actual collateral, numbers or text. Landscape1600:900.','Cuerda roja de papel enrollada junto a un apoyo azul, como metáfora de una precaución.'),
 ('Three separate simple cobalt and red paper door frames standing open on warm ivory ground, each leading to a different short plain paper path. No financial products, interest rates, bank brands, human figures, rankings, guarantees, text or numbers. Landscape1600:900.','Tres puertas de papel abiertas hacia caminos cortos distintos, como metáfora de opciones por estudiar.')]
}
for row in [x for x in plan if 747<=x['number']<=749]:
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
