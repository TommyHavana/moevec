from pathlib import Path
from datetime import datetime, timezone
import json

r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web')
plan=json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json'))
lines=(r.parent/'MEE_Plan_Editorial_840_entradas.md').read_text().splitlines()
style='Use case: stylized-concept. Original MEE editorial illustration in tactile layered cut paper, matte cobalt blue #1547BB, vivid red #EF383E, warm ivory #F7F6F2, soft studio light, generous margins. No text, digits, letters, logos, brands, flags, watermarks, currency signs, official seals, charts or UI. One independent original fictional scene. '
scenes={
 'E2.1.09':[
 ('Two fictional adult faceless ivory paper siblings at a cobalt table, one gently holding a plain red paper desk lamp above an open blank ivory book that the other reads. Both are adults. No tuition prices, actual academic achievement, hierarchy of human worth, children, digits or text. Landscape1200:630.','Dos figuras adultas ficticias: una sostiene una lámpara mientras la otra lee un libro en blanco.'),
 ('A simple cobalt paper balance with one open blank ivory paper book on one pan and a plain red paper wrench on the other, both at equal height. No numbers, salary data, real valuation, text or claim about relative worth of study versus work. Landscape1600:900.','Balanza imaginaria con un libro y una herramienta de papel a la misma altura.'),
 ('Two fictional adult faceless ivory paper hands passing one simple red paper key across a cobalt paper tabletop, warm ivory background. No actual contract, debt, property title, guaranteed reciprocity, time labels, digits or text. Landscape1600:900.','Dos manos adultas ficticias se pasan una llave roja de papel.')],
 'E2.1.10':[
 ('One small round cobalt paper table with four different adult faceless ivory paper figures freely seated around it in foreground; in far background a few abstract identical flat cobalt silhouettes stand in a single row, red paper ground. A conceptual contrast about choice, not an actual country or event. No soldiers, uniforms, weapons, flags, symbols, identifiable people, slogans, text or digits. Landscape1200:630.','Mesa imaginaria con cuatro figuras adultas y, al fondo, una fila de siluetas abstractas.'),
 ('Two separate tactile paper panels: one plain cobalt wall with a broad open ivory doorway and a warm red path through it, another solid red paper wall without opening. Conceptual voluntary exit, no actual country, detention, people, injury, building blueprint, text or numerals. Landscape1600:900.','Dos paneles imaginarios: uno con una puerta abierta y otro cerrado, como metáfora de una salida posible.'),
 ('Four distinct adult faceless ivory paper hands loosely forming an open circle above a round cobalt paper table, one small red paper disc in centre. No grasping, restraints, voting result, money value, real group, text, symbols or numerals. Landscape1600:900.','Cuatro manos adultas ficticias forman un círculo abierto sobre una mesa azul.')],
 'E2.1.11':[
 ('An imaginary cobalt paper sea separates two halves of a warm ivory paper dining table, each side with one plain red plate and one empty ivory paper chair; soft studio light joins both sides visually. No actual map, Cuba outline, flags, migrant count, actual family, deprivation, text or currency. Landscape1200:630.','Dos partes de una mesa imaginaria con platos rojos a ambos lados de un mar de papel azul.'),
 ('Three plain closed ivory paper shipping boxes arranged as low steps across a cobalt paper floor with one small red paper ribbon beside them. No address, shipping labels, logos, customs stamp, digits, text, actual delivery route or guarantee. Landscape1600:900.','Tres cajas cerradas sin etiquetas forman peldaños imaginarios sobre un suelo azul.'),
 ('A small imaginary cobalt paper kitchen table with one plain red mug and an open ivory paper laptop; screen shows two friendly abstract adult faceless cobalt paper figures, soft warm ivory glow. No real app, brands, interface, letters, actual family, promise of connectivity or text. Landscape1600:900.','Cocina imaginaria con una taza roja y una pantalla que muestra dos figuras adultas de papel.')]
}
for row in [x for x in plan if 744<=x['number']<=746]:
 ident=row['id'];d=r/'editorial/articles'/ident;assert not d.exists();d.mkdir();(d/'sources').mkdir()
 j=row['source_line']-1;assert ident in lines[j]
 k=next(n for n in range(j+1,len(lines)) if lines[n].startswith('#### ') or lines[n].startswith('# '))
 (d/'brief-original.md').write_text('\n'.join(lines[j:k]).strip()+'\n')
 tags=[row['topic'],{'Aplicación':'aplicacion','Fundamentos':'fundamentos','Desarrollo':'desarrollo'}[row['level']]]+(['pais-cuba']if ident=='E2.1.11'else[])
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
