# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime,timezone
import json,re,html,hashlib
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');base=r/'editorial/articles'
sba='https://www.sba.gov/counseling/plan-your-business/#market-research'
market='https://www.sba.gov/counseling/manage-your-business/#marketing-sales'
oecd='https://www.oecd.org/en/topics/consumer-policy-and-digital-technologies.html'
hbs='https://www.isc.hbs.edu/strategy/business-strategy/Pages/strategic-positioning.aspx'
wb='https://www.worldbank.org/en/topic/socialprotectionandjobs/publication/state-of-social-protection-2025-2-billion-person-challenge'
cal='https://calnewport.com/the-tao-of-cal/'
para={
'E4.8.04':f'La <a href="{sba}">Small Business Administration</a> pide investigar demanda, tamaño y saturación del mercado. Esas preguntas fundamentan esta objeción: una especialización necesita compradores suficientes. MEE aplica ese criterio al riesgo de concentrar la oferta, sin atribuir a la guía un resultado universal sobre nichos.',
'E4.8.05':f'La <a href="{market}">Small Business Administration</a> distingue la ventaja ofrecida del plan para llegar al comprador y vender. Su guía también pide presupuestar esas acciones. MEE recoge esa distinción para formular la objeción: un buen servicio necesita una vía practicable para ser conocido.',
'E4.8.06':f'La <a href="{sba}">Small Business Administration</a> propone contrastar demanda y precios de alternativas antes de comprometer recursos. MEE toma esa pregunta como base de la objeción: invertir en identidad no demuestra por sí solo que exista demanda para la oferta.',
'E4.8.08':'La <a href="https://www.ilo.org/sites/default/files/wcmsp5/groups/public/%40ed_norm/%40relconf/documents/meetingdocument/wcms_377774.pdf">OIT, en el preámbulo de la Recomendación204</a>, reconoce causas estructurales de la informalidad y la falta de alternativas de sustento. Esa posición fundamenta una objeción a confiar únicamente en mejoras individuales del negocio.',
'E4.8.09':f'La <a href="{oecd}">OCDE, en su presentación sobre política de consumo digital</a>, identifica costes inesperados y problemas de transparencia como riesgos para el comprador. MEE toma esa preocupación como límite a una política de precios: explicar «valor» no sustituye informar de condiciones comprensibles.',
'E4.8.10':f'El <a href="{hbs}">Institute for Strategy and Competitiveness de Harvard Business School</a> presenta el menor coste como una fuente de ventaja competitiva. Esa perspectiva fundamenta la objeción: un pequeño negocio debe examinar la ventaja de costes del rival, sin suponer que cercanía o flexibilidad la compensan siempre.',
'E4.8.11':'<a href="https://www.strategyzer.com/library/the-value-proposition-canvas">Strategyzer</a> señala que completar un lienzo es un punto de partida y que el encaje debe contrastarse con evidencia de clientes. Esa advertencia fundamenta el argumento contrario al ejercicio: terminar una sesión no acredita todavía un encaje real.',
'E4.8.12':f'La <a href="{sba}">Small Business Administration</a> incluye competidores indirectos y secundarios en el análisis de alternativas. MEE aplica esa pregunta a la objeción: un perfil más amplio también puede resolver una necesidad del comprador y merece entrar en la comparación.',
'E4.8.13':'El <a href="https://www.directoriocubano.com/wp-content/uploads/dc-gaceta/archive/pdf/2026/09/ordinaria/073/gaceta.pdf">MINCEX, en los artículos1–4 de la Resolución126/2026</a>, establece condiciones para facultades y mercancías. MEE parte de ese marco para formular la objeción: una historia de origen no reemplaza comprobar las condiciones institucionales de una operación.',
'E4.8.14':'La <a href="https://www.wipo.int/en/web/about-ip">OMPI</a> presenta el reconocimiento y beneficio para quienes crean, junto con el equilibrio con el interés público, como razones del sistema de propiedad intelectual. Esa posición fundamenta el argumento sobre incentivos que una defensa de la imitación debe atender.',
'E4.8.15':'<a href="https://www.netpromotersystem.com/insights/being-loyal-to-loyalty-nps-linkedin/">Fred Reichheld, en su ensayo de2019</a>, vincula la lealtad con principios y servicio a las personas. MEE aplica esa perspectiva como objeción a reducir la evaluación del negocio a una puntuación, sin atribuir al autor nuestra hoja de observación.',
'E4.9.01':f'El <a href="{wb}">Banco Mundial, en la presentación de su informe de protección social de2025</a>, defiende ampliar cobertura y preparar sistemas capaces de responder a shocks. Esa posición fundamenta la objeción: la preparación personal debe examinarse junto con los apoyos institucionales disponibles.',
'E4.9.02':f'<a href="{cal}">Cal Newport, en The Tao of Cal, del3/12/2024</a>, defiende reducir tareas concurrentes y proteger el trabajo que requiere concentración. Es una posición práctica sobre la atención, que MEE usa para formular la objeción al exceso de actividades; no demuestra una rentabilidad universal del ingreso único.',
'E4.9.03':'Mian y Sufi reconocen en el <a href="https://press.uchicago.edu/books/excerpt/2014/Mian-Sufi_House_of_Debt.html">extracto citado de House of Debt</a> que una función de los mercados financieros es compartir riesgos. Esa consideración permite formular una objeción a descartar toda financiación: interesa examinar qué posibilidades abre y cómo reparte las obligaciones.'
}
new={
'E4.8.05':('U.S. Small Business Administration · Marketing and sales',market,'Lectura parcial del plan de marketing, canales y presupuesto. Guía estadounidense, sin trasladar programas o normas a otros países.'),
'E4.8.06':('U.S. Small Business Administration · Market research and competitive analysis',sba,'Lectura de preguntas sobre demanda, tamaño, saturación y alternativas; sin garantía de ventas.'),
'E4.8.09':('OCDE · Consumer policy and digital technologies',oecd,'Lectura parcial de la presentación sobre costes inesperados y transparencia. No es una norma nacional ni una estimación del daño de un negocio concreto.'),
'E4.8.10':('Harvard Business School · Institute for Strategy and Competitiveness · Strategic Positioning',hbs,'Lectura de tipos de ventaja y liderazgo en costes. No demuestra que el mayor tamaño garantice menores costes en cualquier actividad.'),
'E4.9.01':('Banco Mundial · State of Social Protection Report2025 · presentación',wb,'Lectura de la presentación sobre cobertura y sistemas que responden a shocks. No informe íntegro ni evaluación de una prestación nacional.'),
'E4.9.02':('Cal Newport · The Tao of Cal ·3/12/2024',cal,'Lectura de la sección Knowledge Work. Consejo atribuido al autor sobre atención, no estudio causal de rentabilidad de fuentes de ingreso.')
}
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
prepared=[]
for ident,text in para.items():
 d=base/ident;p=d/'article.html';body=p.read_text();assert not(d/'article-before-attribution.html').exists()
 pat=r'(<h2[^>]*>[^<]*El mejor argumento en contra[^<]*</h2>)';assert len(re.findall(pat,body))==1
 after=re.sub(pat,lambda m:m[1]+'\n<p>'+text+'</p>',body,count=1)
 added=None
 if ident in new:
  name,url,scope=new[ident];added=dict(name=name,url=url,scope=scope,public_scope=scope)
  li='<li><a href="'+html.escape(url,quote=True)+'">'+html.escape(name)+'</a>. '+html.escape(scope)+' Consulta:31/10/2026.</li>'
  a,b=after.rsplit('</ol>',1);after=a+li+'</ol>'+b
 core=after.split('<h2 id="seguir-aprendiendo">')[0];wc=len(re.findall(r'\S+',html.unescape(re.sub('<[^>]+>',' ',core))));assert 900<=wc<=1300,(ident,wc)
 prepared.append((ident,body,after,wc,added,text))
for ident,before,after,wc,added,text in prepared:
 d=base/ident;(d/'article-before-attribution.html').write_text(before);(d/'article.html').write_text(after)
 a=json.load(open(d/'article.json'));a['review'].update(counterargument_attribution_checked=True,attribution_checked_on='2026-10-31')
 if added:
  assert not any(x['url']==added['url']for x in a['review']['sources']);a['review']['sources'].append(added)
 write(d/'article.json',a)
 for file in ['source-review.json','sources/reading-scope.json']:
  p=d/file;x=json.load(open(p))
  if added:x['sources'].append(added)
  x['counterargument_attribution_checked']=True
  if file=='source-review.json':
   x['text_checks']['main_words']=wc;x['attribution_revision']=dict(checked_on='2026-10-31',added_paragraph=text,original_body_file='article-before-attribution.html',source_scopes_explicit=True)
   x['archived_files']=[dict(file=str(f.relative_to(d)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest())for f in sorted((d/'sources').rglob('*'))if f.is_file()]
  write(p,x)
 p=d/'review.md';p.write_text(p.read_text()+'\n## Atribución del argumento contrario ·31/10/2026\n\nSe identifica autor u organismo real y fuente primaria, diferenciando la formulación propia de MEE. Texto principal revisado:'+str(wc)+'palabras. Revisión sobre el mismo artículo y sus mismos tres medios; comprobación pública pendiente.\n')
 p=d/'research-notes.md';t=p.read_text();note='\n\nAtribución revisada31/10/2026: '+re.sub('<[^>]+>','',text)+'\n'+(('Fuente adicional: '+added['url']+'\nAlcance: '+added['scope'])if added else'Fuente ya consultada, con alcance conservado.')+'\n\n';p.write_text(t.replace('Excluido:',note+'Excluido:',1)if'Excluido:'in t else t+note)
 print(ident,wc)
write(r/'inventario/auditoria-2026-10-28/editorial-601-603-attribution-preparation.json',dict(checked_on='2026-10-31',update_ids=list(para),already_explicit=['E4.8.07'],requirement='Checklist of original WordPress production prompt: best counterargument attributed to a real author. Institutional authors identified where they issue the primary guide/norm. Own inference explicitly separated.'))
