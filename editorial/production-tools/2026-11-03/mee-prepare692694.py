# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime,timezone
import json,re,html,hashlib
from PIL import Image
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');base=r/'editorial/articles';meta=json.load(open('/tmp/mee-meta692694.json'));plan=json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json'));reg=json.load(open(r/'inventario/plan-editorial-840-status.json'))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def plain(x):return html.unescape(re.sub('<[^>]+>',' ',x))
def wc(x):return len(re.findall(r'\S+',plain(x)))
links={'E6.5.02':['E1.5.02','E7.1.04','E6.5.01'],'E6.5.03':['E6.5.01','E7.1.04','E6.4.12'],'E6.5.04':['E6.5.01','E5.8.15','E4.4.05']}
prepared=[]
for ident,m in meta.items():
 d=base/ident;assert not(d/'article.json').exists();body=(d/'article.html').read_text();assert 'id="fuentes"'not in body
 intro=re.search('<p>(.*?)</p>',body,re.S)[1];faqs=re.findall('<h3>.*?</h3><p>(.*?)</p>',body,re.S)
 checks=dict(main_words=wc(body),opening_words=wc(intro),faq_words=[wc(x)for x in faqs],seo_title_characters=len(m['seo_title']),description_characters=len(m['description']),two_hypothetical_examples=body.count('Ejemplo hipotético:')==2,keyword_h2=any(m['keyword'].lower()in plain(x).lower()for x in re.findall('<h2.*?>(.*?)</h2>',body,re.S)))
 print(ident,checks,flush=True)
 assert 900<=checks['main_words']<=1300 and 40<=checks['opening_words']<=60 and len(faqs)==3 and all(40<=wc(x)<=70 for x in faqs),checks
 assert 50<=len(m['seo_title'])<=60 and m['seo_title'].endswith(' | MEE')and 140<=len(m['description'])<=155,checks
 assert checks['two_hypothetical_examples']and checks['keyword_h2'];assert all(m['keyword'].lower()in t.lower()for t in[plain(intro),m['description'],m['standfirst'],m['seo_title']]);assert body.count('{{INTERIOR_1}}')==body.count('{{INTERIOR_2}}')==1
 assert any(name in body.split('id="contra"')[1].split('<h2')[0] for name in ['Woodruff','La Porta','CGAP']);p=next(x for x in plan if x['id']==ident);research=json.load(open(d/'research.json'));assert all(p[k]==research[k]for k in['id','number','title','slug'])
 assert m['keyword'].lower()in p['title'].lower()
 footer=[]
 for i in links[ident]:
  row=next(x for x in reg['entries']if x['id']==i);assert row['status']=='terminada';footer.append('<li><a href="'+row['url']+'">'+html.escape(row['title'])+'</a></li>')
 body+='\n<h2 id="seguir-aprendiendo">Para seguir aprendiendo</h2><ul>'+''.join(footer)+'</ul>\n<h2 id="fuentes">Fuentes y alcance</h2><p>Consulta y revisión: 03/11/2026. Los ejemplos hipotéticos y las pautas prácticas son propuestas de MEE. Se indica el alcance de las fuentes consultadas.</p><ol>'+''.join('<li><a href="'+html.escape(s['url'],quote=True)+'">'+html.escape(s['name'])+'</a>. '+html.escape(s['public_scope'])+' Consulta: 03/11/2026.</li>'for s in m['sources'])+'</ol>\n'
 md=json.load(open(d/'metadata-draft.json'));imgs=md['images'];imgs['featured']['alt']=('Ilustración para '+m['keyword']+': ')+imgs['featured']['alt'][0].lower()+imgs['featured']['alt'][1:];hs=[]
 for role,im in imgs.items():
  f=d/im['file'];im['caption']='';assert f.stat().st_size<250000 and im['alt'];assert Image.open(f).size==((1200,630)if role=='featured'else(1600,900));hs.append(hashlib.sha256(f.read_bytes()).hexdigest())
 assert len(set(hs))==3
 prepared.append((ident,m,p,research,body,checks,md,imgs))
for ident,m,p,research,body,checks,md,imgs in prepared:
 d=base/ident;review=dict(sources_verified=True,editorial_checked=True,title_checked=True,body_sources_verified=True,checked_on='2026-11-03',counterargument_attribution_checked=True,original_images=True,images_visually_checked=True,illustrative_examples=True,sources=m['sources'],omitted_claims=m['omitted'])
 a={k:p[k]for k in['number','id','title','slug']};a.update({k:v for k,v in m.items()if k not in['sources','omitted']});a.update(tags=research['planned_tags'],images=imgs,review=review)
 (d/'article.html').write_text(body);write(d/'article.json',a)
 write(d/'sources/reading-scope.json',dict(checked_on='2026-11-03',sources=m['sources'],full_books_read=False,full_legal_pdf_read=False))
 write(d/'sources/reading-status.json',dict(reviewed_on='2026-11-03',claims_checked=True,scope_file='reading-scope.json',note='Lecturas parciales explícitas con alcance exacto en reading-scope.json. No libros o papers íntegros; propuestas y ejemplos de MEE identificados.'))
 files=[dict(file=str(f.relative_to(d)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest())for f in sorted((d/'sources').rglob('*'))if f.is_file()]
 write(d/'source-review.json',dict(checked_on='2026-11-03',sources=m['sources'],archived_files=files,omitted_claims=m['omitted'],text_checks=checks,scope='Alcance por fuente en reading-scope.json.692: ILDcap3condensado20061262BtesisSotolibro2000versiónF&D2001no libroíntegro;ElotroSenderop173–175reproducciónarchivadareleída,Ateverano1983tallerconfeccionespersonanatural289días11requisitos,no vivienda/plazovigente. Galiani2010PDFprimario200582332B55pcoverCEDLASAug2010/interior28ene2010soloPDF2–4+34imp32leídos,resumenrenderinspeccionado;experimento naturalhogaresno créditoaleatorio/efectomundial. WoodruffprimarioOxfordtextoindexadoimp1222/fichaAEAleído,directoURLErrorTimeout/AEA403,no PDFreseñacompletaleído;pasosjudicialesinsolvenciaregulaciónmásallátítulos.693: OITenero2026comunicadoprimario20071424Bproyección2.1b2026noobservaciónnov;ILOSTAT11may2026definición21ICLS2023yempleoinformal≠sectorinformalwebprimarioleído/local403; BREADY2025metodología200107027BGeneralBusinessEntryyFAQ2026timecostLLC200451204Bcasosestandarizadosno todoautónomo/resultados2026;LaPortaShleifer2014NBERPDF923282BpasajesintroducciónyPDF11–12registro/modelodual,no briefmonocausalniresultados2014comotodos2026.694: Nobel2006PazYunusGrameenHTML200165334Bleído/webtool403;MITBanerjeeKarlanZinman2015PDF2001401373B21p,p1/10–11leídos/p10renderinspeccionado,no6estudiosíntegros;efectosmodestamentepositivosNOtransformadorescorrigebrief. CGAP2010PDF8p284112Bpasajes1/3/4/6leídos/contextocrisisdeudamúltipleincentivosregulacióntransparencia/p3renderinspeccionado,no balancefinalsuicidioscausales/cifras2010comovigentes. Aritmética100→120diferencia20hipótesis,no20%anualsinfechas/costes.',image_review='Nueve originales692–694 inspeccionados nativos y mosaicoWebP: casa/documentovacíoqueformallavemetáfora;personaficticiacargapapelesanteventanillas;barriocasasficticiasnoimagenantesdespuésdelestudio;mercadoficticiosombraedificiosinsellos/nopaísreal;muropapelesvacíos;paraguasazulpanelrojorasgado;seismujeresficticiascuadernoblanco;seislupassobremapaabstractonopaísesdelosestudios;escaleracobaltounpeldañorojorotosinpersonas. Sintextocifraslogos,negociospersonasreales,documentotítuloauténticoonormaautorizaciónrepresentada;dimensionespesosalt/hashcomprobados.'))
 (d/'review.md').write_text('# Revisión editorial · '+ident+'\n\n- ID, título, slug, área/tema y etiquetas del plan conservados.\n- Texto principal '+str(checks['main_words'])+' palabras, apertura de 40–60, dos ejemplos hipotéticos, tres FAQ de 40–70, argumento contrario atribuido a autor real, lectura de MEE y práctica.\n- Fuentes y alcance parcial documentados; sin título igual a crédito garantizado, causa única de informalidad o microcrédito transformador universal. Fechas, método, población, lecturas parciales y proyecciones conservados; ejemplos hipotéticos. Variantes SEO del título/slug fijo identificadas.\n- Tres originales generados con herramienta integrada, inspeccionados, tamaños, alt y hash comprobados.\n- Pendiente publicación y verificación pública.\n')
 write(d/'source-preparation.json',dict(id=ident,phase='ready_for_publication',sources_verified=True,article_complete=True,images_complete=True,pending=['Publicación y comprobación pública']))
 sp=d/'sources/research-scope-progress.json'
 if sp.exists():write(sp,dict(reviewed_on='2026-11-03',phase='ready_for_publication',sources_verified=True,note='Revisión y alcance en source-review.json; publicación y comprobación pública pendientes.'))
 (d/'research-notes.md').write_text('# Investigación · '+ident+'\n\n'+'\n\n'.join(s['name']+'\n'+s['url']+'\n'+s['scope']for s in m['sources'])+'\n\nExcluido:\n'+'\n'.join('- '+x for x in m['omitted'])+'\n')
 research.update(images_visually_checked=True,phase='ready_for_publication',article_complete=True,images_complete=True,sources_verified=True,claims_checked=True,review_status='READY_FOR_PUBLICATION',pending=['Publicación y comprobación pública'],updated_at=datetime.now(timezone.utc).isoformat());write(d/'research.json',research);md.update(images_visually_checked=True,article_complete=True,images_complete=True,sources_verified=True,images=imgs,review_status='READY_FOR_PUBLICATION');write(d/'metadata-draft.json',md)
state=json.load(open(r/'editorial/production-state.json'));state.update(phase='ready_for_publication',updated_at=datetime.now(timezone.utc).isoformat())
for x in state['local_preparations']:
 if x['id']in meta:x.update(images=3,article_complete=True,sources_verified=True,phase='ready_for_publication')
state['storage_block'].update(next_images_ready=9,local_webps_ready=9,texts_ready=3,sources_verified=True,phase='resolved_capacity_available');write(r/'editorial/production-state.json',state)
