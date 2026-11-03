# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime,timezone
import json,re,html,hashlib
from PIL import Image
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');base=r/'editorial/articles';meta=json.load(open('/tmp/mee-meta649651.json'));plan=json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json'));reg=json.load(open(r/'inventario/plan-editorial-840-status.json'))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def plain(x):return html.unescape(re.sub('<[^>]+>',' ',x))
def wc(x):return len(re.findall(r'\S+',plain(x)))
links={'E4.12.04':['E4.12.01','E4.12.03','E4.8.07'],'E4.12.05':['E1.9.12','E4.12.01','E5.7.08'],'E4.12.06':['E4.4.11','E6.1.12','E4.12.03']}
prepared=[]
for ident,m in meta.items():
 d=base/ident;assert not(d/'article.json').exists();body=(d/'article.html').read_text();assert 'id="fuentes"'not in body
 intro=re.search('<p>(.*?)</p>',body,re.S)[1];faqs=re.findall('<h3>.*?</h3><p>(.*?)</p>',body,re.S)
 checks=dict(main_words=wc(body),opening_words=wc(intro),faq_words=[wc(x)for x in faqs],seo_title_characters=len(m['seo_title']),description_characters=len(m['description']),two_hypothetical_examples=body.count('Ejemplo hipotético:')==2,keyword_h2=any(m['keyword'].lower()in plain(x).lower()for x in re.findall('<h2.*?>(.*?)</h2>',body,re.S)))
 print(ident,checks,flush=True)
 assert 900<=checks['main_words']<=1300 and 40<=checks['opening_words']<=60 and len(faqs)==3 and all(40<=wc(x)<=70 for x in faqs),checks
 assert 50<=len(m['seo_title'])<=60 and m['seo_title'].endswith(' | MEE')and 140<=len(m['description'])<=155,checks
 assert checks['two_hypothetical_examples']and checks['keyword_h2'];assert all(m['keyword'].lower()in t.lower()for t in[plain(intro),m['description'],m['standfirst'],m['seo_title']]);assert body.count('{{INTERIOR_1}}')==body.count('{{INTERIOR_2}}')==1
 assert any(name in body.split('id="contra"')[1].split('<h2')[0] for name in ['Panko','Acemoglu','n8n']);p=next(x for x in plan if x['id']==ident);research=json.load(open(d/'research.json'));assert all(p[k]==research[k]for k in['id','number','title','slug'])
 assert m['keyword'].lower()in p['title'].lower()
 footer=[]
 for i in links[ident]:
  row=next(x for x in reg['entries']if x['id']==i);assert row['status']=='terminada';footer.append('<li><a href="'+row['url']+'">'+html.escape(row['title'])+'</a></li>')
 body+='\n<h2 id="seguir-aprendiendo">Para seguir aprendiendo</h2><ul>'+''.join(footer)+'</ul>\n<h2 id="fuentes">Fuentes y alcance</h2><p>Consulta y revisión: 31/10/2026. Los ejemplos hipotéticos y las pautas prácticas son propuestas de MEE. Se indica el alcance de las fuentes consultadas.</p><ol>'+''.join('<li><a href="'+html.escape(s['url'],quote=True)+'">'+html.escape(s['name'])+'</a>. '+html.escape(s['public_scope'])+' Consulta: 31/10/2026.</li>'for s in m['sources'])+'</ol>\n'
 md=json.load(open(d/'metadata-draft.json'));imgs=md['images'];imgs['featured']['alt']='Ilustración sobre '+m['keyword']+': '+imgs['featured']['alt'][0].lower()+imgs['featured']['alt'][1:];hs=[]
 for role,im in imgs.items():
  f=d/im['file'];im['caption']='';assert f.stat().st_size<250000 and im['alt'];assert Image.open(f).size==((1200,630)if role=='featured'else(1600,900));hs.append(hashlib.sha256(f.read_bytes()).hexdigest())
 assert len(set(hs))==3
 prepared.append((ident,m,p,research,body,checks,md,imgs))
for ident,m,p,research,body,checks,md,imgs in prepared:
 d=base/ident;review=dict(sources_verified=True,editorial_checked=True,title_checked=True,body_sources_verified=True,checked_on='2026-10-31',counterargument_attribution_checked=True,original_images=True,images_visually_checked=True,illustrative_examples=True,sources=m['sources'],omitted_claims=m['omitted'])
 a={k:p[k]for k in['number','id','title','slug']};a.update({k:v for k,v in m.items()if k not in['sources','omitted']});a.update(tags=research['planned_tags'],images=imgs,review=review)
 (d/'article.html').write_text(body);write(d/'article.json',a)
 write(d/'sources/reading-scope.json',dict(checked_on='2026-10-31',sources=m['sources'],full_books_read=False,full_legal_pdf_read=False))
 write(d/'sources/reading-status.json',dict(reviewed_on='2026-10-31',claims_checked=True,scope_file='reading-scope.json',note='Lecturas parciales explícitas con alcance exacto en reading-scope.json. No libros o papers íntegros; propuestas y ejemplos de MEE identificados.'))
 files=[dict(file=str(f.relative_to(d)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest())for f in sorted((d/'sources').rglob('*'))if f.is_file()]
 write(d/'source-review.json',dict(checked_on='2026-10-31',sources=m['sources'],archived_files=files,omitted_claims=m['omitted'],text_checks=checks,scope='649: PankoEuSpRIG2000arXivdeposit2008abstract/PDFp1–2/renderp1,no artículo1998íntegro; LibreOffice definiciones10funciones/currentfreepageverificadas. Títulofijosuperlativorentabilidadsinrespaldo,retener.650: QJE2025resumen/introducción,5172/15%heterogéneoempresaúnica,noWP14%;NIST2024PDFp10–11/renderp10/noíntegro;AcemogluRestrepo2019AEAabstractdesplazamientonuevastareas.651: WordPressdocsintroducción/accesorequieretemadebloques; n8nexportJSON/migraciónnocopiainstanciaentera ybackupapartados leídos; sin recomendarserviciodepago/pruebaspropias. EjemplosMEEhipotéticos.',image_review='Nueve originales649–651 inspeccionados nativos y mosaicoWebP. Cuadrículamapanegocioficticio/10fichascontadas/lupacuadradocolor; mostradorlampara/lupafigura/candadotarjetas; tiendapapelpantalla/murobloques/plataformacandadopuente. 649interior1editadoconimage_genparaquitarsímbolosygráfico,no publicadoprimeroriginal,ambosnativosconservados. No datos, UIsmarcareal,seguridadcertificadaoíndicesrentabilidad.1200x630y1600x900<250000B,alt/hashes comprobados.'))
 (d/'review.md').write_text('# Revisión editorial · '+ident+'\n\n- ID, título, slug, área/tema y etiquetas del plan conservados.\n- Texto principal '+str(checks['main_words'])+' palabras, apertura de 40–60, dos ejemplos hipotéticos, tres FAQ de 40–70, argumento contrario atribuido a autor real, lectura de MEE y práctica.\n- Fuentes y alcance parcial documentados; sin retorno universal, productividad de cualquier negocio o portabilidad automática afirmados. Variantes SEO del título/slug fijo identificadas.\n- Tres originales generados con herramienta integrada, inspeccionados, tamaños, alt y hash comprobados.\n- Pendiente publicación y verificación pública.\n')
 write(d/'source-preparation.json',dict(id=ident,phase='ready_for_publication',sources_verified=True,article_complete=True,images_complete=True,pending=['Publicación y comprobación pública']))
 sp=d/'sources/research-scope-progress.json'
 if sp.exists():write(sp,dict(reviewed_on='2026-10-31',phase='ready_for_publication',sources_verified=True,note='Revisión y alcance en source-review.json; publicación y comprobación pública pendientes.'))
 (d/'research-notes.md').write_text('# Investigación · '+ident+'\n\n'+'\n\n'.join(s['name']+'\n'+s['url']+'\n'+s['scope']for s in m['sources'])+'\n\nExcluido:\n'+'\n'.join('- '+x for x in m['omitted'])+'\n')
 research.update(images_visually_checked=True,phase='ready_for_publication',article_complete=True,images_complete=True,sources_verified=True,claims_checked=True,review_status='READY_FOR_PUBLICATION',pending=['Publicación y comprobación pública'],updated_at=datetime.now(timezone.utc).isoformat());write(d/'research.json',research);md.update(images_visually_checked=True,article_complete=True,images_complete=True,sources_verified=True,images=imgs,review_status='READY_FOR_PUBLICATION');write(d/'metadata-draft.json',md)
held='E4.12.04';d=base/held
proposal='Hojas de cálculo: usos prácticos para tu negocio'
write(d/'title-review.json',dict(id=held,number=649,original_title='Hojas de cálculo: la herramienta más rentable que puedes aprender',proposed_title=proposal,slug_preserved='hojas-de-calculo-herramienta-rentable',phase='title_review_pending',reason='Las fuentes consultadas describen usos, funciones y errores, sin comparación que sustente mayor rentabilidad para cualquier lector. La instrucción conserva el título fijo; se retiene hasta aclaración.',article_body_words=1084,body_complete=True,images=3,published=False,question_sent=False))
p=d/'article.json';x=json.load(open(p));x['review'].update(sources_verified=False,title_checked=False,body_sources_verified=True);write(p,x)
for n in ['research.json','metadata-draft.json','source-preparation.json']:
 p=d/n;x=json.load(open(p));x.update(phase='title_review_pending',article_complete=True,images_complete=True,sources_verified=False,body_sources_verified=True,title_checked=False,review_status='TITLE_REVIEW_PENDING',pending=['Aclarar el título fijo comparativo antes de publicar.']);write(p,x)
p=d/'review.md';p.write_text(p.read_text()+'\n## Retención por título\n\nNo publicable: el título fijo afirma rentabilidad máxima sin comparación verificada. Texto y fuentes del cuerpo preparados; tres imágenes completas. Propuesta de título: «'+proposal+'». No se modifica el manifiesto ni se cuenta como terminada.\n')
write(d/'sources/research-scope-progress.json',dict(phase='title_review_pending',sources_verified=False,body_sources_verified=True,title_checked=False,published=False))
state=json.load(open(r/'editorial/production-state.json'));state.update(phase='two_ready_one_title_pending',updated_at=datetime.now(timezone.utc).isoformat())
for x in state['local_preparations']:
 if x['id']in meta:x.update(images=3,article_complete=True,sources_verified=x['id']!=held,body_sources_verified=True,phase='title_review_pending'if x['id']==held else'ready_for_publication',published=False)
state['storage_block'].update(next_images_ready=9,local_webps_ready=9,texts_ready=3,sources_verified=False,phase='resolved_capacity_available',free_bytes=__import__('shutil').disk_usage(r).free);write(r/'editorial/production-state.json',state)
