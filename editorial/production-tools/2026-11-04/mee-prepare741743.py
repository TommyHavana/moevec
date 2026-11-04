# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime,timezone
import json,re,html,hashlib
from PIL import Image
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');base=r/'editorial/articles';meta=json.load(open(str(r/'editorial/production-tools/2026-11-04/metadata741743.json')));plan=json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json'));reg=json.load(open(r/'inventario/plan-editorial-840-status.json'))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def plain(x):return html.unescape(re.sub('<[^>]+>',' ',x))
def wc(x):return len(re.findall(r'\S+',plain(x)))
links={'E2.1.06':['E2.1.02','E6.7.15','E2.1.04'],'E2.1.07':['E1.5.12','E7.8.10','E2.1.03'],'E2.1.08':['E2.1.04','E2.1.02','E4.2.11']}
prepared=[]
for ident,m in meta.items():
 d=base/ident;assert not(d/'article.json').exists();body=(d/'article.html').read_text();assert 'id="fuentes"'not in body
 intro=re.search('<p>(.*?)</p>',body,re.S)[1];faqs=re.findall('<h3>.*?</h3><p>(.*?)</p>',body,re.S)
 checks=dict(main_words=wc(body),opening_words=wc(intro),faq_words=[wc(x)for x in faqs],seo_title_characters=len(m['seo_title']),description_characters=len(m['description']),two_hypothetical_examples=body.count('Ejemplo hipotético:')==2,keyword_h2=any(m['keyword'].lower()in plain(x).lower()for x in re.findall('<h2.*?>(.*?)</h2>',body,re.S)))
 print(ident,checks,flush=True)
 assert 900<=checks['main_words']<=1300 and 40<=checks['opening_words']<=60 and len(faqs)==3 and all(40<=wc(x)<=70 for x in faqs),checks
 assert 50<=len(m['seo_title'])<=60 and m['seo_title'].endswith(' | MEE')and 140<=len(m['description'])<=155,checks
 assert checks['two_hypothetical_examples']and checks['keyword_h2'];assert all(m['keyword'].lower()in t.lower()for t in[plain(intro),m['description'],m['standfirst'],m['seo_title']]);assert body.count('{{INTERIOR_1}}')==body.count('{{INTERIOR_2}}')==1
 assert any(name in body.split('id="contra"')[1].split('<h2')[0] for name in ['Bloom','Chami','Sandra Huenchuan']);p=next(x for x in plan if x['id']==ident);research=json.load(open(d/'research.json'));assert all(p[k]==research[k]for k in['id','number','title','slug'])
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
 write(d/'source-review.json',dict(checked_on='2026-11-04',sources=m['sources'],archived_files=files,omitted_claims=m['omitted'],text_checks=checks,scope='741: presentación IEF2025 con alcance sociedades mercantiles, manualIFC PDF12–14/23 leído parcialmente, resumen CEP2006 y referencia QJE2007; sin causalidad de parentesco, retorno o supervivencia garantizada.742: análisis BIDjun2026 con cifras2025, RPWQ32025 lectura parcial web y promedio no cotización, ficha/resumen FMI2003 no hogar evaluado.743: extracto primario CEPAL2025 y ficha Huenchuan2025, OMS continuidad y presentación paquete2024, sin normativa/precios locales ni dependencia por edad. Listas y casos propios de MEE. Alcances de acceso y omisiones individualizados en sources.',image_review='Nueve nativos y mosaico WebP741–743 inspeccionados:741 tres adultos en tienda, mesa con hojas/cinta, árbol con recuadros vacíos;742 dos ciudades imaginarias con puente y sobres, manos con sobre cerrado, casa inacabada;743 manos adultas acompañando mano con pliegues, calendario sin cifras, casa con rampa imaginaria. No datos medidos, beneficiarios reales, efecto financiero, instrucciones técnicas o certificación de accesibilidad.'))
 (d/'review.md').write_text('# Revisión editorial · '+ident+'\n\n- ID, título, slug, área/tema y etiquetas del plan conservados.\n- Texto principal '+str(checks['main_words'])+' palabras, apertura de 40–60, dos ejemplos hipotéticos, tres FAQ de 40–70, argumento contrario atribuido a autor real, lectura de MEE y práctica.\n- Fuentes y alcance parcial documentados; sin programas operativos ni retornos o resultados garantizados. Lecturas parciales explícitas; propuestas MEE y ejemplos hipotéticos. Cifras por fecha y ámbito; negocio sin garantía, remesas sin tarifa individual y cuidados sin prestaciones o diagnóstico inventados. Criterios éticos y ejercicios propios de MEE. Variantes SEO del título/slug fijo identificadas.\n- Tres originales generados con herramienta integrada, inspeccionados, tamaños, alt y hash comprobados.\n- Pendiente publicación y verificación pública.\n')
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
state=__import__('json').load(open(r/'editorial/production-state.json'));state['resume_point']=dict(number=741,id='E2.1.06',next_action='publish_741_743_after_preflight',accepted_images=9,article_complete=True,sources_verified=True);write(r/'editorial/production-state.json',state)
