from pathlib import Path
from datetime import datetime,timezone
from PIL import Image
import json,re,html,hashlib,sys,urllib.request

r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');sys.path.insert(0,str(r/'scripts'))
from atomic_export import atomic_export
now=datetime.now(timezone.utc).isoformat();reg=json.load(open(r/'inventario/plan-editorial-840-status.json'));plan=json.load(open(r/'wordpress/plugins/mee-editorial/data/production-plan.json'));s=json.load(open(r/'editorial/production-state.json'))
assert reg['counts']=={'terminada':834,'en curso':0,'pendiente':6}
data={
 'E2.3.04':dict(keyword='ahorro para la jubilación',links=['E2.3.01','E2.3.02','E2.3.03'],sources=[
  dict(name='CFPB · How does compound interest work? · revisión19/10/2023',url='https://www.consumerfinance.gov/ask-cfpb/how-does-compound-interest-work-en-1683/',scope='Página primaria leída en web: definición de interés compuesto. Recuperación local403 registrada; no HTML fingido. No se usa el5% de su ejemplo como previsión.',public_scope='Definición educativa del interés compuesto. Los escenarios numéricos de este artículo son cálculos propios de MEE.'),
  dict(name='SEC, Investor.gov · Compound Interest Calculator · consulta05/11/2026',url='https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator',scope='Página y variables de calculadora leídas, HTML48371B SHA256 9e83a7b03a600e6aeef66b5cd472690f459810a09fe767dc69dae9b882e8e8f6. No simulación ejecutada en web; cálculo MEE independiente por fórmula anual al final de periodo, resultados guardados.',public_scope='Variables de una calculadora educativa. No rentabilidad esperada, producto recomendado o resultado individual.'),
  dict(name='SEC, Investor.gov · What is Risk? · consulta05/11/2026',url='https://www.investor.gov/introduction-investing/investing-basics/what-risk',scope='Apartados generales, inflación y liquidez leídos. HTML62399B SHA256 e777fe2012dde08ffa10808d5d538c5cbe653c99f2a5a8ed1da607825d9b268f. Sin trasladar garantías o topes de EEUU a otros países.',public_scope='Orientación general sobre pérdidas, inflación y disponibilidad. No condiciones jurídicas de un producto local.'),
  dict(name='OCDE · Pensions at a Glance2025 ·27/11/2025',url='https://www.oecd.org/en/publications/pensions-at-a-glance-2025_e40274c1-en.html',scope='Resumen primario web leído, cobertura OCDE/G20 y diseño/indicadores. Sin PDF248p íntegro, estadísticas ni edades o ventajas fiscales nacionales trasladadas. Local403 registrado. F114 del brief; F065 libro no leído y no usado para afirmar resultados.',public_scope='Presentación del informe2025 y su cobertura. Sin una lectura íntegra o una recomendación de producto o sistema para una persona.'),
  dict(name='OIT · Frequently asked questions, Convention102 ·06/08/2024',url='https://www.ilo.org/frequently-asked-questions-social-security-minimum-standards-convention',scope='Página primaria leída, especialmente marco R202 y protección de mayores. HTML88853B SHA256 db0476c54746b1041c2144002b635e6797b87adbb6ee4c2e9b02f3bbe4cdd916. No confundir recomendación con prestación universal ya exigible ni revisión completa de legislación nacional.',public_scope='Argumento sobre pisos de protección y seguridad básica de ingresos en la vejez, de definición nacional. No determina derechos individuales.'),
 ],omitted=['Título original compara de forma absoluta plazo e ingresos: no acreditado; propuesta ya consultada sin nueva pregunta.','Sin rentabilidad garantizada, impuestos o productos locales, cifras de pensión, recomendaciones de aportación individual o libroF065 fingido.','Simulación MEE al3% nominal constante: aportación al final de año, capital inicial0, sin gastos/impuestos/inflación; resultados75401/53741/107481, redondeo a unidad. Dos casos hipotéticos.']),
 'E2.6.08':dict(keyword='clientelismo',links=['E7.10.01','E2.6.01','E2.6.02'],sources=[
  dict(name='Stokes, Dunning, Nazareno y Brusco · Brokers, Voters, and Clientelism · Cambridge2013, extracto',url='https://assets.cambridge.org/97811070/42209/excerpt/9781107042209_excerpt.pdf',scope='Extracto10p145547B, PDF3/4/5/6/7/8/9/10 leídas, PDF7 visual. Conceptos de reparto programático/no programático, intercambio condicionado, ejemplos históricos atribuidos, apoyo y atractivo de intermediación. No libro íntegro, evaluación actual de programas o sentencia revisada. No cifras históricas de beneficiarios/incidencia trasplantadas a2026.',public_scope='Conceptos y ejemplos históricos del extracto inicial, incluidas diferencias entre reglas públicas y su aplicación. No lectura del libro completo ni diagnóstico actual de países.'),
  dict(name='Susan Stokes · Clientelism and development: is there a poverty trap? · UNU-WIDER91/2021',url='https://www.wider.unu.edu/publication/clientelism-and-development-there-poverty-trap',scope='Resumen primario leído y reconfirmado05/11/2026; HTML46099B archivado, PDF403 no leído. Mecanismo teórico posible y evidencia preliminar de coincidencia histórica con crecimiento. No empobrecimiento universal ni causalidad medida en un programa local.',public_scope='Resumen de argumentos teóricos y observaciones históricas preliminares. Sin lectura del PDF completo ni estimación causal propia.'),
 ],omitted=['Título que empobrece sin condición no respaldado universalmente; no aplicar propuesta de título antes de resolución.','Noacusación de delito o persona actual, instrucciones de manipulación electoral o voto condicionado atribuido a todos los receptores de ayudas.','Joel y Mariela hipotéticos; criterios de rendición de cuentas MEE, sin eficacia probada o vía jurídica universal.'])
}
exports=[]
def j(p,x):exports.append((p,json.dumps(x,ensure_ascii=False,indent=2)+'\n'))
def wc(t):return len(re.findall(r'\S+',html.unescape(re.sub('<[^>]+>',' ',t))))
for ident,m in data.items():
 d=r/'editorial/articles'/ident;t=(d/'body-draft.html').read_text();assert 'id="fuentes"'not in t
 intro=re.search('<p>(.*?)</p>',t,re.S)[1];faqs=re.findall('<h3>.*?</h3><p>(.*?)</p>',t,re.S)
 checks=dict(main_words=wc(t),opening_words=wc(intro),faq_words=[wc(x)for x in faqs],hypothetical_examples=t.count('Ejemplo hipotético:'))
 assert 900<=checks['main_words']<=1300 and 40<=checks['opening_words']<=60 and len(faqs)==3 and all(40<=wc(x)<=70 for x in faqs)and checks['hypothetical_examples']==2
 assert all(k in t for k in ['El mejor argumento en contra','La lectura de MEE','Qué puedes hacer tú'])and t.count('{{INTERIOR_1}}')==t.count('{{INTERIOR_2}}')==1
 md=json.load(open(d/'metadata-draft.json'));hashes=[]
 for role,im in md['images'].items():
  f=d/im['file'];assert f.stat().st_size<250000 and im['alt']and Image.open(f).size==((1200,630)if role=='featured'else(1600,900));hashes.append(hashlib.sha256(f.read_bytes()).hexdigest())
 assert len(set(hashes))==3
 if ident=='E2.3.04':
  md['images']['featured']['alt']='Ilustración de dos árboles de distinto tamaño y un reloj de arena, metáfora del tiempo de ahorro.'
  md['images']['interior-1']['alt']='Reloj de papel con discos azules sin números y manecillas rojas en un paisaje ficticio.'
  md['images']['interior-2']['alt']='Hucha conceptual azul con forma de casa y una ranura roja en el tejado.'
 footer='<h2 id="seguir-aprendiendo">Para seguir aprendiendo</h2><ul>'
 for target in m['links']:
  x=next(z for z in reg['entries']if z['id']==target);assert x['status']=='terminada'
  response=urllib.request.urlopen(urllib.request.Request(x['url'],headers={'User-Agent':'MEE-editorial-verification'}),timeout=25);assert response.status==200
  footer+='<li><a href="'+x['url']+'">'+html.escape(x['title'])+'</a></li>'
 footer+='</ul><h2 id="fuentes">Fuentes y alcance</h2><p>Consulta y revisión:05/11/2026. Ejemplos hipotéticos y propuestas prácticas de MEE. Lecturas y límites:</p><ol>'+''.join('<li><a href="'+html.escape(x['url'],quote=True)+'">'+html.escape(x['name'])+'</a>. '+html.escape(x['public_scope'])+'</li>'for x in m['sources'])+'</ol>\n'
 exports.append((d/'article.html',t+'\n'+footer));exports.append((d/'research-notes.md','# Investigación y título pendiente · '+ident+'\n\n'+'\n\n'.join(x['name']+'\n'+x['url']+'\n'+x['scope']for x in m['sources'])+'\n\nExcluido:\n'+'\n'.join('- '+x for x in m['omitted'])+'\n\nTres originales y cuerpo conservados. Título del plan sin cambios; no publicar hasta resolver la consulta ya enviada.\n'))
 review=dict(id=ident,checked_on='2026-11-05',sources_verified=False,title_checked=False,body_sources_verified=True,body_editorial_checked=True,images_visually_checked=True,original_images=True,text_checks=checks,sources=m['sources'],omitted_claims=m['omitted'],publication_blocked='Título original sin respaldo suficiente; consulta previa sin respuesta.',image_review='Seis nativos y mosaico769818 vistos.769 árboles distintos/reloj/hucha;818 manos con bolsa y papel en blanco/urna con cuerda/tarjeta ficticia. Sin datos, programas, comicios o personas reales. Originales nativos conservados según registros.')
 review['archived_files']=[dict(file=str(p.relative_to(d)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())for p in sorted((d/'sources').rglob('*'))if p.is_file()]
 j(d/'source-review.json',review);j(d/'sources/reading-scope.json',dict(checked_on='2026-11-05',sources=m['sources'],full_books_read=False,full_legal_corpus_reviewed=False));exports.append((d/'review.md','# Revisión del cuerpo · '+ident+'\n\n'+json.dumps(checks,ensure_ascii=False)+'\n\nFuentes del cuerpo contrastadas, tres originales con alt/dimensiones/pesos/hash, nativos y mosaico vistos. Tres enlaces internos200. Título original pendiente; ninguna publicación ni medio creado en WordPress. No se cambia ID, slug o título, ni se crea article.json publicable.\n'))
 for name in ['research.json','metadata-draft.json','source-preparation.json']:
  x=md if name=='metadata-draft.json'else json.load(open(d/name));x.update(phase='title_review_pending',article_complete=False,body_complete=True,body_sources_verified=True,body_editorial_checked=True,sources_verified=False,title_checked=False,images_generated=3,images_complete=True,images_visually_checked=True,published=False,review_status='BODY_READY_TITLE_PENDING',pending=['Resolución de la consulta de título ya enviada, sin repetirla.','Revisión final de título y metadatos, publicación y comprobación pública.'],updated_at=now);j(d/name,x)
 for x in s['local_preparations']:
  if x['id']==ident:x.update(images=3,images_visually_checked=True,body_complete=True,body_sources_verified=True,article_complete=False,sources_verified=False,title_checked=False,published=False,phase='title_review_pending')
 print(ident,json.dumps(checks),flush=True)
 s['storage_block'].update(local_webps_ready=sum(x['images']for x in s['local_preparations']),body_drafts_ready=sum(x.get('body_complete',False)for x in s['local_preparations']),free_bytes=__import__('shutil').disk_usage(r).free,checked_at=now)
s.update(phase='awaiting_title_review',updated_at=now);s['storage_block']['current_reason']='834/840 publicadas.769/818 con cuerpo revisado y3/3originales; las seis pendientes conservan bloqueo de título. No generar más imágenes ni repetir preguntas.'
j(r/'editorial/production-state.json',s)
atomic_export(exports)
