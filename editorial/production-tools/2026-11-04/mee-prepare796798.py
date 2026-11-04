from pathlib import Path
from datetime import datetime,timezone
from PIL import Image
import json,re,html,hashlib
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');base=r/'editorial/articles';meta=json.load(open(r/'editorial/production-tools/2026-11-04/metadata796798.json'));plan=json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json'));reg=json.load(open(r/'inventario/plan-editorial-840-status.json'))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def plain(t):return html.unescape(re.sub('<[^>]+>',' ',t))
def wc(t):return len(re.findall(r'\S+',plain(t)))
links={'E2.5.01':['E2.4.05','E2.4.08','E1.1.01'],'E2.5.02':['E1.3.15','E2.4.11','E2.4.12'],'E2.5.03':['E5.1.09','E5.1.03','E1.1.10']}
image_review='Nueve nativos finales y mosaico796798 WebP vistos.796 manos abiertas con semillas, cinta abierta sin atar mano y balanza nivelada con flor/rama.797 cuaderno vacío con tres bandas luminosas, planta hacia ventana y persona ficticia observa con lupa tres bloques sin ejes ni datos.798 lápiz conectado a bosque/excavación/fábrica ficticios, manos alrededor de esfera abstracta y mesa con alimentos conectada a campos/talleres simbólicos. Sin datos empíricos, marcas, fabricantes identificados, tratamiento ilustrado o procedencias verificadas.'

ready=[]
for ident,m in meta.items():
 d=base/ident;assert not(d/'article.json').exists();body=(d/'article.html').read_text();assert 'id="fuentes"'not in body
 intro=re.search('<p>(.*?)</p>',body,re.S)[1];faqs=re.findall('<h3>.*?</h3><p>(.*?)</p>',body,re.S)
 checks=dict(main_words=wc(body),opening_words=wc(intro),faq_words=[wc(x)for x in faqs],seo_title_characters=len(m['seo_title']),description_characters=len(m['description']),hypothetical_examples=body.count('Ejemplo hipotético:'))
 assert 900<=wc(body)<=1300 and 40<=wc(intro)<=60 and len(faqs)==3 and all(40<=wc(x)<=70 for x in faqs),checks
 assert 50<=len(m['seo_title'])<=60 and m['seo_title'].endswith(' | MEE')and 140<=len(m['description'])<=155
 assert 2<=len(m['keyword'].split())<=5 and checks['hypothetical_examples']==2
 assert all(m['keyword'].lower()in t.lower()for t in[plain(intro),m['description'],m['standfirst'],m['seo_title']]);assert any(m['keyword'].lower()in plain(t).lower()for t in re.findall('<h2.*?>(.*?)</h2>',body,re.S))
 assert all(s in body for s in['El mejor argumento en contra','La lectura de MEE','Qué puedes hacer tú']);assert body.count('{{INTERIOR_1}}')==body.count('{{INTERIOR_2}}')==1
 contra=body.split('id="contra"')[1].split('id="mee"')[0];assert {'E2.5.01':'Smith','E2.5.02':'Emmons','E2.5.03':'OIT'}[ident]in contra
 p=next(x for x in plan if x['id']==ident);research=json.load(open(d/'research.json'));assert all(p[k]==research[k]for k in['id','number','title','slug'])
 assert m['keyword'].lower()in p['title'].lower()
 footer=[]
 for i in links[ident]:
  row=next(x for x in reg['entries']if x['id']==i);assert row['status']=='terminada';footer.append('<li><a href="'+row['url']+'">'+html.escape(row['title'])+'</a></li>')
 body+='\n<h2 id="seguir-aprendiendo">Para seguir aprendiendo</h2><ul>'+''.join(footer)+'</ul>\n<h2 id="fuentes">Fuentes y alcance</h2><p>Consulta y revisión: 04/11/2026. Los ejemplos hipotéticos y las propuestas prácticas son elaboración de MEE. Se precisa el alcance de las lecturas y de las interpretaciones históricas.</p><ol>'+''.join('<li><a href="'+html.escape(s['url'],quote=True)+'">'+html.escape(s['name'])+'</a>. '+html.escape(s['public_scope'])+' Consulta: 04/11/2026.</li>'for s in m['sources'])+'</ol>\n'
 md=json.load(open(d/'metadata-draft.json'));imgs=md['images'];imgs['featured']['alt']='Ilustración para '+m['keyword']+': '+imgs['featured']['alt'][0].lower()+imgs['featured']['alt'][1:]
 hashes=[]
 for role,im in imgs.items():
  f=d/im['file'];assert f.stat().st_size<250000 and im['alt'];assert Image.open(f).size==((1200,630)if role=='featured'else(1600,900));hashes.append(hashlib.sha256(f.read_bytes()).hexdigest());im['caption']=''
 assert len(set(hashes))==3;ready.append((ident,m,p,research,body,checks,md,imgs));print(ident,json.dumps(checks),flush=True)
for ident,m,p,research,body,checks,md,imgs in ready:
 d=base/ident;review=dict(sources_verified=True,editorial_checked=True,title_checked=True,body_sources_verified=True,checked_on='2026-11-04',counterargument_attribution_checked=True,original_images=True,images_visually_checked=True,illustrative_examples=True,sources=m['sources'],omitted_claims=m['omitted'])
 a={k:p[k]for k in['number','id','title','slug']};a.update({k:v for k,v in m.items()if k not in['sources','omitted']});a.update(tags=research['planned_tags'],images=imgs,review=review)
 (d/'article.html').write_text(body);write(d/'article.json',a);write(d/'sources/reading-scope.json',dict(checked_on='2026-11-04',sources=m['sources'],full_books_read=False,full_legal_corpus_reviewed=False))
 write(d/'sources/reading-status.json',dict(reviewed_on='2026-11-04',claims_checked=True,scope_file='reading-scope.json',note='Lecturas parciales explícitas; sin libros completos o videos no consultados. Fallos de recuperación no usados como fuentes leídas.'))
 files=[dict(file=str(f.relative_to(d)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest())for f in sorted((d/'sources').rglob('*'))if f.is_file()]
 write(d/'source-review.json',dict(checked_on='2026-11-04',sources=m['sources'],archived_files=files,omitted_claims=m['omitted'],text_checks=checks,image_review=image_review,scope='796 Mauss introducción/obligaciones/conclusiones parciales y SmithII.I/II.II parciales, posiciones no idénticas a MEE.797 Emmons2003resumen/método1, Dickensficha yChoi2025resumen/intro/resultadosiniciales, sin19%mejora o indicaciónclínica.798 Read1958pasajes, Hayek1945inicio yOITUNICEF2024publicado2025, sin cadenasactuales auditadas oacusaciónfabricante.'))
 (d/'review.md').write_text('# Revisión editorial · '+ident+'\n\n- ID, título yslug delplan conservados. Cuerpo'+str(checks['main_words'])+'palabras,apertura40–60,dosejemploshipotéticos,tresFAQ40–70.\n- Argumento contrario fiel con fuente primaria, lectura MEE y práctica. Fuentesfechadas,condicionesjurídicasyestadísticasdelimitadas. Detalleensource-review.json.\n- TresoriginalesWebP,alt,dimensiones,pesosyhashescomprobados;nativosymosaicovistos.\n- Publicaciónyverificaciónpúblicapendientes.\n')
 write(d/'source-preparation.json',dict(id=ident,phase='ready_for_publication',sources_verified=True,article_complete=True,images_complete=True,pending=['Publicación y comprobación pública']))
 (d/'research-notes.md').write_text('# Investigación · '+ident+'\n\n'+'\n\n'.join(s['name']+'\n'+s['url']+'\n'+s['scope']for s in m['sources'])+'\n\nExcluido:\n'+'\n'.join('- '+x for x in m['omitted'])+'\n')
 research.update(images_visually_checked=True,phase='ready_for_publication',article_complete=True,images_complete=True,sources_verified=True,claims_checked=True,review_status='READY_FOR_PUBLICATION',pending=['Publicación y comprobación pública'],updated_at=datetime.now(timezone.utc).isoformat());write(d/'research.json',research)
 md.update(images_visually_checked=True,article_complete=True,images_complete=True,sources_verified=True,images=imgs,review_status='READY_FOR_PUBLICATION');write(d/'metadata-draft.json',md)
 for f in (d/'sources').glob('*progress.json'):
  x=json.load(open(f));x.update(final_review_file='../source-review.json',final_sources_reviewed=True,phase='ready_for_publication',note='Registro de investigación inicial; revisión final prevalece en source-review.json. No equivale a lectura completa de PDFs.');write(f,x)
state=json.load(open(r/'editorial/production-state.json'));state.update(phase='ready_for_publication',updated_at=datetime.now(timezone.utc).isoformat())
for x in state['local_preparations']:
 if x['id']in meta:x.update(images=3,article_complete=True,sources_verified=True,phase='ready_for_publication')
state['storage_block'].update(next_images_ready=9,local_webps_ready=9,texts_ready=3,sources_verified=True,phase='resolved_capacity_available');state['resume_point']=dict(number=796,id='E2.5.01',next_action='publish_796_798_after_preflight',accepted_images=9,article_complete=True,sources_verified=True);write(r/'editorial/production-state.json',state)
