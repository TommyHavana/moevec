from pathlib import Path
from datetime import datetime, timezone
from PIL import Image
import copy, hashlib, html, json, re, sys

root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(root/'scripts'))
from atomic_export import atomic_export

approval = json.loads((root/'editorial/title-alternatives-approved-2026-11-05.json').read_text())
plan_path = root/'wordpress/plugins/mee-editorial/data/production-plan.json'
plan = json.loads(plan_path.read_text())
assert hashlib.sha256(plan_path.read_bytes()).hexdigest() == approval['original_plan_sha256']
snapshot = json.loads((root/'inventario/plan-editorial-840-status.json').read_text())
stamp = datetime.now(timezone.utc).isoformat()
metadata = {
 'E4.2.06': dict(seo_title='Aprender idiomas: valorar el retorno y elegir método | MEE',
  description='Aprender idiomas exige revisar propósito, recursos y costes. Contrasta evidencia salarial y aprendizaje sin prometer el mayor retorno o empleo garantizado.',
  keyword='aprender idiomas', secondary_keywords=['prima salarial del inglés','práctica de recuperación','recursos gratuitos de inglés','coste de aprender idiomas'],
  standfirst='Aprender idiomas puede ampliar tus opciones. Revisa qué muestra la evidencia salarial, cómo observar el aprendizaje y qué costes comparar antes de elegir una formación.'),
 'E4.3.02': dict(seo_title='Aversión a la pérdida: evidencia y decisiones reales | MEE',
  description='Examina la aversión a la pérdida, sus estimaciones y límites. MEE propone comparar alternativas y consecuencias sin asignar un miedo fijo a cada persona.',
  keyword='aversión a la pérdida', secondary_keywords=['teoría prospectiva','Kahneman y Tversky','metaanálisis de aversión a la pérdida','punto de referencia'],
  standfirst='La aversión a la pérdida necesita contexto. Revisa estimaciones y críticas, y compara las consecuencias de una decisión sin convertir un promedio en una regla personal.'),
 'E4.12.04': dict(seo_title='Hojas de cálculo: funciones, usos y revisión práctica | MEE',
  description='Hojas de cálculo para organizar tareas: diez funciones de Calc, una alternativa gratuita y preguntas para revisar errores antes de utilizar los resultados.',
  keyword='hojas de cálculo', secondary_keywords=['LibreOffice Calc','errores en hojas de cálculo','funciones de Calc','datos de un pequeño negocio'],
  standfirst='Las hojas de cálculo ayudan a organizar información y realizar operaciones. Explora diez funciones de Calc y aprende qué comprobar antes de utilizar los resultados.'),
 'E6.6.02': dict(seo_title='Grupos de ahorro rotativo: reglas, costes y riesgos | MEE',
  description='Los grupos de ahorro rotativo reúnen cuotas y reparten el fondo por turnos. Comprende sus variantes, compromisos y riesgos antes de considerar participar.',
  keyword='grupos de ahorro rotativo', secondary_keywords=['tandas y natilleras','susu y hui','aportaciones por turnos','riesgo de incumplimiento'],
  standfirst='Los grupos de ahorro rotativo exigen entender el ciclo completo. Revisa aportaciones, turnos, variantes y riesgos con ejemplos ilustrativos y preguntas para aclarar el acuerdo.'),
 'E2.3.04': dict(seo_title='Ahorro para la jubilación: tiempo y aportaciones | MEE',
  description='El ahorro para la jubilación combina tiempo, aportaciones y riesgos. Compara ejemplos ilustrativos y prepara preguntas sobre derechos, costes y liquidez.',
  keyword='ahorro para la jubilación', secondary_keywords=['interés compuesto','aportaciones de ahorro','riesgo e inflación','protección en la vejez'],
  standfirst='El ahorro para la jubilación combina tiempo, ingresos y riesgos. Entiende una simulación con supuestos explícitos y prepara preguntas sobre tus derechos y las condiciones del ahorro.'),
 'E2.6.08': dict(seo_title='Favores políticos y clientelismo: cómo reconocerlos | MEE',
  description='Los favores políticos condicionados plantean preguntas sobre el clientelismo. Distingue ayudas con reglas, dependencia y evidencia al sacar conclusiones.',
  keyword='favores políticos', secondary_keywords=['clientelismo político','ayudas públicas','lealtad política','reglas de acceso a programas'],
  standfirst='Los favores políticos pueden condicionar el acceso a una ayuda. Aprende a distinguir reglas públicas e intercambios particulares, con evidencia histórica y propuestas de MEE.'),
}

def plain(text): return html.unescape(re.sub('<[^>]+>', ' ', text))
def wc(text): return len(re.findall(r'\S+', plain(text)))
def omit_paragraph(body, starts):
    pattern = r'<p>'+re.escape(starts)+r'.*?</p>\s*'
    body, count = re.subn(pattern, '', body, count=1, flags=re.S)
    assert count == 1, starts
    return body

outputs = []
all_hashes = []
checks_out = []
plan_before = copy.deepcopy(plan)
for change in approval['changes']:
    ident = change['id']; d = root/'editorial/articles'/ident
    row = next(x for x in plan if x['id']==ident)
    actual = next(x for x in snapshot['entries'] if x['id']==ident)
    assert actual['status']=='pendiente' and not (d/'publication.json').exists()
    assert row['title']==change['original_title'] and row['slug']==change['slug']
    row['title'] = change['proposed_title']
    before = (d/'article.html').read_text()
    assert not (d/'article.pre-title-approval.html').exists()
    outputs.append((d/'article.pre-title-approval.html', before))
    body = before.split('<h2 id="seguir-aprendiendo">')[0]
    body = body.replace('<h 2 ', '<h2 ')
    body = body.replace('<p>{{INTERIOR_1}}</p>', '{{INTERIOR_1}}').replace('<p>{{INTERIOR_2}}</p>', '{{INTERIOR_2}}')
    if ident=='E4.2.06':
        for starts in ['Ese alcance impide convertir sus resultados', 'Antes de comprar formación, escribe', 'También conviene distinguir una necesidad actual', 'Conserva una descripción de la tarea inicial', 'Elige también una tarea relacionada con tu propósito']:
            body = omit_paragraph(body, starts)
        body = body.replace('<p>Para MEE, invertir en un idioma', '<h2 id="lectura-mee">La lectura de MEE</h2>\n<p>Para MEE, invertir en un idioma')
    if ident=='E4.3.02':
        body = omit_paragraph(body, 'La existencia de estimaciones favorables y críticas')
    if ident=='E4.12.04':
        body = body.replace('Consultamos sus páginas iniciales como referencia alternativa al artículo de 1998 del brief.', 'Sus páginas iniciales permiten examinar qué sabemos sobre los errores y cómo revisar una hoja.')
        body = body.replace('<p>La respuesta de MEE combina aprendizaje', '<h2 id="lectura-mee">La lectura de MEE</h2>\n<p>La respuesta de MEE combina aprendizaje')
    if ident=='E2.3.04':
        body = body.replace('((1,03 elevado al número de años menos 1)/0,03)', '<code>(1,03<sup>n</sup> − 1) / 0,03</code>, donde <em>n</em> es el número de años')
        body = body.replace('del G 20', 'del G20')
    if ident=='E2.6.08':
        body = body.replace('un intercambio particular de favores.', 'un intercambio particular de favores políticos.', 1)
        body = body.replace('>Qué es el clientelismo</h2>', '>Qué es el clientelismo: favores políticos condicionados</h2>')
    m = metadata[ident]
    intro = re.search('<p>(.*?)</p>', body, re.S)[1]
    faqs = re.findall('<h3>.*?</h3><p>(.*?)</p>', body, re.S)
    checks = dict(main_words=wc(body), opening_words=wc(intro), faq_words=[wc(x)for x in faqs],
                  seo_title_characters=len(m['seo_title']), description_characters=len(m['description']),
                  hypothetical_examples=body.count('Ejemplo hipotético:'), malformed_h2=body.count('<h 2'))
    assert 900<=wc(body)<=1300 and 40<=wc(intro)<=60 and len(faqs)==3 and all(40<=wc(x)<=70 for x in faqs), (ident,checks)
    assert 50<=len(m['seo_title'])<=60 and m['seo_title'].endswith(' | MEE') and 140<=len(m['description'])<=155, (ident,checks)
    assert 2<=len(m['keyword'].split())<=5
    assert all(m['keyword'].lower() in text.lower() for text in [plain(intro),row['title'],m['seo_title'],m['description'],m['standfirst']]), ident
    assert any(m['keyword'].lower() in plain(t).lower() for t in re.findall('<h2.*?>(.*?)</h2>',body,re.S))
    assert all(s in body for s in ['El mejor argumento en contra','La lectura de MEE','Qué puedes hacer tú'])
    assert checks['hypothetical_examples']==2 and body.count('{{INTERIOR_1}}')==body.count('{{INTERIOR_2}}')==1
    review = json.loads((d/'source-review.json').read_text())
    outputs.append((d/'source-review.pre-title-approval.json',json.dumps(review,ensure_ascii=False,indent=2)+'\n'))
    sources = copy.deepcopy(review['sources'])
    for source in sources:
        source['scope'] = source['scope'].split('Título fijo')[0].strip()
        if 'public_scope' not in source: source['public_scope']=source['scope']
    # La DOI se conserva; la copia primaria facilita consultar el resumen revalidado.
    if ident=='E4.3.02':
        sources[2]['author_copy_url']='https://wrap.warwick.ac.uk/id/eprint/185745/13/1-s2.0-S0167487024000485-main.pdf'
        sources[2]['scope'] += ' Revalidado el resumen de la copia institucional de Warwick el 05/11/2026; no lectura íntegra del PDF.'
    olddate = '31/10/2026' if ident in ['E4.2.06','E4.3.02','E4.12.04'] else ('03/11/2026' if ident=='E6.6.02' else '05/11/2026')
    links = re.findall(r'<a href="(https://moevec.org[^\"]+)"', before)
    assert 3<=len(set(links))<=5
    footer = before.split('<h2 id="seguir-aprendiendo">')[1].split('<h2 id="fuentes">')[0]
    body += '\n<h2 id="seguir-aprendiendo">'+footer
    body += '<h2 id="fuentes">Fuentes y alcance</h2><p>Revisión editorial final: 05/11/2026. Los ejemplos hipotéticos y las pautas prácticas son elaboración de MEE. Se identifica el alcance de las lecturas.</p><ol>'
    for source in sources:
        body += '<li><a href="'+html.escape(source['url'],quote=True)+'">'+html.escape(source['name'])+'</a>. '+html.escape(source['public_scope'])+' Consultado el '+olddate+'.'
        if source.get('author_copy_url'): body += ' <a href="'+source['author_copy_url']+'">Copia institucional del artículo</a>, resumen revalidado el 05/11/2026.'
        body += '</li>'
    body += '</ol>\n'
    old_manifest_path = d/'article.json'
    a = json.loads(old_manifest_path.read_text()) if old_manifest_path.exists() else {}
    if a: outputs.append((d/'article.pre-title-approval.json',json.dumps(a,ensure_ascii=False,indent=2)+'\n'))
    draft = json.loads((d/'metadata-draft.json').read_text())
    imgs = copy.deepcopy(a.get('images',draft['images']))
    for role, im in imgs.items():
        f=d/im['file'];size=Image.open(f).size
        assert f.stat().st_size<250000 and Image.open(f).format=='WEBP' and size==((1200,630)if role=='featured'else(1600,900))
        all_hashes.append(hashlib.sha256(f.read_bytes()).hexdigest())
        im['caption']=''
        if role=='featured' and m['keyword'].lower() not in im['alt'].lower():
            im['alt']='Ilustración sobre '+m['keyword']+': '+im['alt'][0].lower()+im['alt'][1:]
    completed_review=dict(sources_verified=True,editorial_checked=True,title_checked=True,body_sources_verified=True,
        checked_on='2026-11-05',counterargument_attribution_checked=True,original_images=True,images_visually_checked=True,
        illustrative_examples=True,sources=sources,omitted_claims=review.get('omitted_claims',a.get('review',{}).get('omitted_claims',[])),
        title_resolution=dict(approved_title=row['title'],original_title=change['original_title'],approval_file='editorial/title-alternatives-approved-2026-11-05.json'))
    research_path=d/'research.json';research=json.loads(research_path.read_text())
    a={k:row[k]for k in ['number','id','title','slug']}
    a.update(m,tags=[row['topic'],row['level'].lower()],images=imgs,review=completed_review)
    research.update(title=row['title'],phase='ready_for_publication',title_checked=True,title_approved=True,sources_verified=True,
        article_complete=True,images_complete=True,images_visually_checked=True,review_status='READY_FOR_PUBLICATION',pending=['Publicación y comprobación pública'],updated_at=stamp)
    draft.update(title=row['title'],phase='ready_for_publication',title_checked=True,title_approved=True,sources_verified=True,
        article_complete=True,images_complete=True,images_visually_checked=True,review_status='READY_FOR_PUBLICATION',images=imgs,pending=['Publicación y comprobación pública'])
    review.update(completed_review,text_checks=checks,final_review_complete=True,approval_file='../../title-alternatives-approved-2026-11-05.json',
        image_review='Mosaico de los 18 WebP inspeccionado el 05/11/2026; originales nativos conservados y revisión anterior en cada expediente. Escenas conceptuales, sin datos o personas documentales.',pending=['Publicación y comprobación pública'],next_action='publish_after_remote_plan_sync_and_duplicate_preflight')
    review.pop('publication_blocked',None)
    for filename,data in [('article.json',a),('research.json',research),('metadata-draft.json',draft),('source-review.json',review),
        ('title-review.json',dict(id=ident,number=row['number'],original_title=change['original_title'],approved_title=row['title'],slug=row['slug'],status='approved_and_reviewed',approved_at=approval['approved_at'],approval_file='../../title-alternatives-approved-2026-11-05.json')),
        ('source-preparation.json',dict(id=ident,phase='ready_for_publication',sources_verified=True,title_checked=True,article_complete=True,images_complete=True,pending=['Publicación y comprobación pública']))]:
        outputs.append((d/filename,json.dumps(data,ensure_ascii=False,indent=2)+'\n'))
    outputs += [(d/'article.html',body),(d/'body-draft.html',body.split('<h2 id="seguir-aprendiendo">')[0]),
        (d/'review.md','# Revisión final · '+ident+' · 05/11/2026\n\n- Alternativa de título aprobada explícitamente; ID y slug conservados.\n- Cuerpo '+str(checks['main_words'])+' palabras; apertura '+str(checks['opening_words'])+'; tres FAQ '+str(checks['faq_words'])+'. Dos ejemplos hipotéticos.\n- Argumento contrario, lectura MEE, práctica y fuentes con alcance revisados. HTML de encabezados y posiciones de imagen comprobados.\n- Tres originales WebP con tamaño, peso, alt y hashes distintos; mosaico final inspeccionado.\n- Publicación y comprobación pública pendientes.\n')]
    checks_out.append(dict(id=ident,number=row['number'],title=row['title'],checks=checks))

assert len(all_hashes)==len(set(all_hashes))==18
changed=[(a,b)for a,b in zip(plan_before,plan)if a!=b]
assert len(changed)==6 and all({k for k in a if a[k]!=b[k]}=={'title'}for a,b in changed)
outputs.append((root/'editorial/production-tools/2026-11-05/production-plan-before-approved-titles.json',json.dumps(plan_before,ensure_ascii=False,indent=2)+'\n'))
outputs.append((plan_path,json.dumps(plan,ensure_ascii=False,indent=2)+'\n'))
state_path=root/'editorial/production-state.json';state=json.loads(state_path.read_text())
state.update(phase='ready_for_publication',updated_at=stamp)
for x in state['local_preparations']:
    if x['id']in metadata: x.update(phase='ready_for_publication',title_checked=True,sources_verified=True,article_complete=True)
state['resume_point'].update(next_action='sync_approved_remote_plan_then_preflight_and_publish_501_512_649',article_complete=True,sources_verified=True,title_checked=True)
outputs.append((state_path,json.dumps(state,ensure_ascii=False,indent=2)+'\n'))
outputs.append((root/'editorial/approved-six-final-review-2026-11-05.json',json.dumps(dict(reviewed_at=stamp,checks=checks_out,images=18,unique_image_hashes=18),ensure_ascii=False,indent=2)+'\n'))
atomic_export(outputs)
print(json.dumps(checks_out,ensure_ascii=False,indent=2))
