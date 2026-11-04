from pathlib import Path
from datetime import datetime, timezone
import json

r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web')
plan=json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json'))
lines=(r.parent/'MEE_Plan_Editorial_840_entradas.md').read_text().splitlines()
style='Use case: stylized-concept. Original MEE editorial illustration in tactile layered cut paper, matte cobalt blue #1547BB, vivid red #EF383E, warm ivory #F7F6F2, soft studio light, generous margins. No text, digits, letters, logos, brands, flags, watermarks, currency signs, official seals, charts or UI. One independent original fictional scene. '
scenes={
 'E2.1.03':[
 ('One fictional ivory paper child planting one small red paper seedling in cobalt ground while one adult ivory paper figure holds a broad plain ivory paper sunshade above both. Respectful family cooperation, no money amount, age claim, educational outcome or guaranteed growth. Landscape1200:630.', 'Una figura infantil ficticia planta una semilla mientras una adulta sostiene una sombra de papel.'),
 ('One plain ivory paper marshmallow cube on a cobalt table, next to one simple red paper clock with blank face and two plain hands. No digits, test results, data, psychological diagnosis, children, stopwatch or promise of future success. Landscape1600:900.', 'Un malvavisco imaginario sobre una mesa junto a un reloj sin cifras, como metáfora de una espera.'),
 ('One plain translucent ivory paper savings jar with a simple cobalt mortarboard-shaped lid, containing a few unmarked red paper discs. No currency symbols, interest rate, numbers, real financial product or guaranteed return. Landscape1600:900.', 'Frasco simbólico con fichas sin valor monetario y una tapa con forma de birrete.')],
 'E2.1.04':[
 ('Three adult faceless ivory paper figures beneath a floating cobalt paper roof, one standing calmly with arms raised supporting its edge, two seated on a simple red paper bench. No injury, visible suffering, diagnosis, children or measured burden. Organizational imbalance metaphor only. Landscape1200:630.', 'Tres figuras adultas ficticias bajo un techo, una sostiene un borde mientras dos están sentadas.'),
 ('One loose red paper cord with a visibly frayed middle resting on warm ivory ground, with two cobalt paper supports beside it. No body parts, no person tied, violence, wounds, medical diagnosis or danger scene. Metaphor only. Landscape1600:900.', 'Una cuerda roja deshilachada descansa entre dos apoyos de papel, como metáfora de un límite.'),
 ('Four equal adult faceless ivory paper figures around one red paper table, all raising arms together to support a light cobalt paper roof above the table. No real family, pressure, injury, diagnosis or claim of fairness measured. Landscape1600:900.', 'Cuatro figuras adultas ficticias comparten el apoyo de un techo sobre una mesa.')],
 'E2.1.05':[
 ('A small caravan of four faceless ivory paper adult figures walking together over a cobalt paper path toward a soft ivory circle of light at the horizon, red hills. No actual migration route, national flags, deprivation, rescue claim, numbers or guaranteed happiness. Landscape1200:630.', 'Caravana imaginaria de figuras adultas por un camino azul hacia una luz suave en el horizonte.'),
 ('A gently curving cobalt paper path with three small blank red and ivory pennants on plain short poles marking intermediate points. No national signs, text, numbers, goals measured or promises. Landscape1600:900.', 'Camino de papel con pequeños banderines sin símbolos, como metáfora de etapas revisables.'),
 ('A small round cobalt paper table with one single red paper candle with a soft ivory paper flame at its centre, two plain ivory paper cups and four empty simple paper chairs. No party text, religious symbols, birthday digits, outcomes or actual family. Landscape1600:900.', 'Mesa imaginaria con una vela y sillas vacías, como metáfora de reconocer una etapa compartida.')]
}
for row in [x for x in plan if 738<=x['number']<=740]:
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
