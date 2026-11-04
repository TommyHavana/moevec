# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime,timezone
import json,re,html,hashlib
from PIL import Image
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');base=r/'editorial/articles';meta=json.load(open(str(r/'editorial/production-tools/2026-11-04/metadata735737.json')));plan=json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json'));reg=json.load(open(r/'inventario/plan-editorial-840-status.json'))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def plain(x):return html.unescape(re.sub('<[^>]+>',' ',x))
def wc(x):return len(re.findall(r'\S+',plain(x)))
links={'E6.7.15':['E6.7.01','E6.7.02','E6.7.12','E6.7.13','E6.7.14'],'E2.1.01':['E4.1.01','E4.1.05','E4.11.12'],'E2.1.02':['E5.4.09','E4.10.10','E4.10.11']}
prepared=[]
for ident,m in meta.items():
 d=base/ident;assert not(d/'article.json').exists();body=(d/'article.html').read_text();assert 'id="fuentes"'not in body
 intro=re.search('<p>(.*?)</p>',body,re.S)[1];faqs=re.findall('<h3>.*?</h3><p>(.*?)</p>',body,re.S)
 checks=dict(main_words=wc(body),opening_words=wc(intro),faq_words=[wc(x)for x in faqs],seo_title_characters=len(m['seo_title']),description_characters=len(m['description']),two_hypothetical_examples=body.count('Ejemplo hipotético:')==2,keyword_h2=any(m['keyword'].lower()in plain(x).lower()for x in re.findall('<h2.*?>(.*?)</h2>',body,re.S)))
 print(ident,checks,flush=True)
 assert 900<=checks['main_words']<=1300 and 40<=checks['opening_words']<=60 and len(faqs)==3 and all(40<=wc(x)<=70 for x in faqs),checks
 assert 50<=len(m['seo_title'])<=60 and m['seo_title'].endswith(' | MEE')and 140<=len(m['description'])<=155,checks
 assert checks['two_hypothetical_examples']and checks['keyword_h2'];assert all(m['keyword'].lower()in t.lower()for t in[plain(intro),m['description'],m['standfirst'],m['seo_title']]);assert body.count('{{INTERIOR_1}}')==body.count('{{INTERIOR_2}}')==1
 assert any(name in body.split('id="contra"')[1].split('<h2')[0] for name in ['Hayek','Folbre','Becker']);p=next(x for x in plan if x['id']==ident);research=json.load(open(d/'research.json'));assert all(p[k]==research[k]for k in['id','number','title','slug'])
 assert m['keyword'].lower()in p['title'].lower()
 footer=[]
 for i in links[ident]:
  row=next(x for x in reg['entries']if x['id']==i);assert row['status']=='terminada';footer.append('<li><a href="'+row['url']+'">'+html.escape(row['title'])+'</a></li>')
 body+='\n<h2 id="seguir-aprendiendo">Para seguir aprendiendo</h2><ul>'+''.join(footer)+'</ul>\n<h2 id="fuentes">Fuentes y alcance</h2><p>Consulta y revisión: 04/11/2026. Los ejemplos hipotéticos y las pautas prácticas son propuestas de MEE. Se indica el alcance de las fuentes consultadas.</p><ol>'+''.join('<li><a href="'+html.escape(s['url'],quote=True)+'">'+html.escape(s['name'])+'</a>. '+html.escape(s['public_scope'])+' Consulta: 04/11/2026.</li>'for s in m['sources'])+'</ol>\n'
 md=json.load(open(d/'metadata-draft.json'));imgs=md['images'];imgs['featured']['alt']=('Ilustración para '+m['keyword']+': ')+imgs['featured']['alt'][0].lower()+imgs['featured']['alt'][1:];hs=[]
 for role,im in imgs.items():
  f=d/im['file'];im['caption']='';assert f.stat().st_size<250000 and im['alt'];assert Image.open(f).size==((1200,630)if role=='featured'else(1600,900));hs.append(hashlib.sha256(f.read_bytes()).hexdigest())
 assert len(set(hs))==3
 prepared.append((ident,m,p,research,body,checks,md,imgs))
for ident,m,p,research,body,checks,md,imgs in prepared:
 d=base/ident;review=dict(sources_verified=True,editorial_checked=True,title_checked=True,body_sources_verified=True,checked_on='2026-11-04',counterargument_attribution_checked=True,original_images=True,images_visually_checked=True,illustrative_examples=True,sources=m['sources'],omitted_claims=m['omitted'])
 a={k:p[k]for k in['number','id','title','slug']};a.update({k:v for k,v in m.items()if k not in['sources','omitted']});a.update(tags=research['planned_tags'],images=imgs,review=review)
 (d/'article.html').write_text(body);write(d/'article.json',a)
 write(d/'sources/reading-scope.json',dict(checked_on='2026-11-04',sources=m['sources'],full_books_read=False,full_legal_pdf_read=False))
 write(d/'sources/reading-status.json',dict(reviewed_on='2026-11-04',claims_checked=True,scope_file='reading-scope.json',note='Lecturas parciales explícitas con alcance exacto en reading-scope.json. No libros o papers íntegros; propuestas y ejemplos de MEE identificados.'))
 files=[dict(file=str(f.relative_to(d)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest())for f in sorted((d/'sources').rglob('*'))if f.is_file()]
 write(d/'source-review.json',dict(checked_on='2026-11-04',sources=m['sources'],archived_files=files,omitted_claims=m['omitted'],text_checks=checks,scope='735: síntesis propia de MEE con cinco decisiones, no receta validada ni funciones siempre centralizadas; Hayek PDF5y7 como objeción sobre información.736: Becker conferencia PDF1y9–11, no libro1981 íntegro; Folbre artículo firmado2026, no InvisibleHeart íntegro; condiciones éticas MEE sin reciprocidad garantizada.737: comunicado institucional Nobel apartado hogar y familia, conferenciaBecker1y9–11 y OCDEpresentación/cautelas2026; sin datos nacionales trasladados a individuos o precios universales. Lecturas parciales explícitas.',image_review='Nueve nativos y mosaico WebP735–737 inspeccionados.735: modelo imaginario de panal con lápiz; cofre y tres llaves; SEIS celdas visibles con tres iluminadas, variación del prompt de siete aceptada como metáfora sin recuento exigido por el texto.736: adultos colaborando con escalera; tres llaves y puerta; nudo libre sobre mesa con dos tarjetas.737: casa con engranajes y dos figuras en tareas domésticas; figura femenina añadida por generación sobre mesa de cocina y formas sin texto, alt actualizado; dos manos y seis fichas sin cifras. Sin instalaciones reales, promesas de reciprocidad, puntuación de reparto justo o datos medidos.'))
 (d/'review.md').write_text('# Revisión editorial · '+ident+'\n\n- ID, título, slug, área/tema y etiquetas del plan conservados.\n- Texto principal '+str(checks['main_words'])+' palabras, apertura de 40–60, dos ejemplos hipotéticos, tres FAQ de 40–70, argumento contrario atribuido a autor real, lectura de MEE y práctica.\n- Fuentes y alcance parcial documentados; sin programas operativos ni retornos o resultados garantizados. Lecturas parciales explícitas; propuestas MEE y ejemplos hipotéticos. Cinco decisiones organizativas propias; cooperación familiar con límites y desigualdad discutible, sin resultados o deudas universales. Variantes SEO del título/slug fijo identificadas.\n- Tres originales generados con herramienta integrada, inspeccionados, tamaños, alt y hash comprobados.\n- Pendiente publicación y verificación pública.\n')
 write(d/'source-preparation.json',dict(id=ident,phase='ready_for_publication',sources_verified=True,article_complete=True,images_complete=True,pending=['Publicación y comprobación pública']))
 sp=d/'sources/research-scope-progress.json'
 if sp.exists():write(sp,dict(reviewed_on='2026-11-04',phase='ready_for_publication',sources_verified=True,note='Revisión y alcance en source-review.json; publicación y comprobación pública pendientes.'))
 (d/'research-notes.md').write_text('# Investigación · '+ident+'\n\n'+'\n\n'.join(s['name']+'\n'+s['url']+'\n'+s['scope']for s in m['sources'])+'\n\nExcluido:\n'+'\n'.join('- '+x for x in m['omitted'])+'\n')
 research.update(images_visually_checked=True,phase='ready_for_publication',article_complete=True,images_complete=True,sources_verified=True,claims_checked=True,review_status='READY_FOR_PUBLICATION',pending=['Publicación y comprobación pública'],updated_at=datetime.now(timezone.utc).isoformat());write(d/'research.json',research);md.update(images_visually_checked=True,article_complete=True,images_complete=True,sources_verified=True,images=imgs,review_status='READY_FOR_PUBLICATION');write(d/'metadata-draft.json',md)
state=json.load(open(r/'editorial/production-state.json'));state.update(phase='ready_for_publication',updated_at=datetime.now(timezone.utc).isoformat())
for x in state['local_preparations']:
 if x['id']in meta:x.update(images=3,article_complete=True,sources_verified=True,phase='ready_for_publication')
state['storage_block'].update(next_images_ready=9,local_webps_ready=9,texts_ready=3,sources_verified=True,phase='resolved_capacity_available');write(r/'editorial/production-state.json',state)

for ident in meta:
 d=base/ident
 p=d/'sources/reading-status-progress.json'
 if p.exists():
  x=__import__('json').load(open(p));x.update(phase='ready_for_publication',final_sources_reviewed=True,sources_verified=True,note='Revisión final y alcances exactos en source-review.json y sources/reading-scope.json; publicación pendiente.');write(p,x)
state=__import__('json').load(open(r/'editorial/production-state.json'));state['resume_point']=dict(number=735,id='E6.7.15',next_action='publish_735_737_after_preflight',accepted_images=9,article_complete=True,sources_verified=True);write(r/'editorial/production-state.json',state)
