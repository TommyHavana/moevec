from pathlib import Path
import json

def source(name,url,scope,public_scope):return dict(name=name,url=url,scope=scope,public_scope=public_scope)

lecture='https://www.nobelprize.org/uploads/2018/06/becker-lecture.pdf'
metadata={
'E6.7.15':dict(
 seo_title='Crecer con autonomía: cinco decisiones de diseño | MEE',
 description='Crecer con autonomía: cinco decisiones sobre trabajo, facultades e información. MEE propone una ficha, ejemplos hipotéticos y revisión de los acuerdos.',
 keyword='crecer con autonomía',secondary=['diseño organizativo','facultades','información compartida','revisión de acuerdos'],
 standfirst='Crecer con autonomía: síntesis práctica de MEE con cinco decisiones de diseño, responsabilidades comunes y una ficha para conversar sobre un primer cambio.',
 sources=[source('F. A. Hayek · The Use of Knowledge in Society · 1945','https://oll-resources.s3.us-east-2.amazonaws.com/oll3/store/titles/92/Hayek_0766_EBk_v6.0.pdf',
 'PDF primario archivado, páginas5 y7 consultadas sobre coordinación de conocimiento disperso. Un párrafo breve del argumento contrario, no manual empresarial ni escala de madurez. Cinco decisiones, ficha y ejemplos propios de MEE; síntesis de la serie E6.7.01–14, con cinco enlaces a entradas completas. No14 artículos externos declarados leídos íntegros. Derivación de esta fuente sumada a732 limitada: aproximadamente40 palabras de cuerpo y referencia breve, no reproducción.',
 'Páginas5 y7 del PDF; aplicación al diseño organizativo propuesta por MEE.')],
 omitted=['No funciones que siempre deban centralizarse en toda empresa.', 'Sin resultados empresariales medidos o facultades que sustituyan requisitos profesionales.', 'Cinco decisiones son preguntas propias, no un estándar validado.']),
'E2.1.01':dict(
 seo_title='Sacrificio tribal: acuerdos, límites y apoyo familiar | MEE',
 description='Sacrificio tribal: cómo revisar un esfuerzo compartido, su duración y sus costes. MEE propone acuerdos revisables y contrasta la crítica del cuidado.',
 keyword='sacrificio tribal',secondary=['cooperación familiar','cuidados','Nancy Folbre','acuerdos revisables'],
 standfirst='Sacrificio tribal: el criterio de MEE sobre acuerdo, duración y beneficio compartido, con ejemplos hipotéticos y una crítica sobre el coste de cuidar.',
 sources=[
 source('Gary S. Becker · conferencia Nobel · 1992',lecture,
 'PDF primario descargado200,225007B,21 páginas. Leídas PDF1 y9–11, render1 inspeccionado; página19bibliografía extraída sin utilizar afirmaciones. Para736: altruismo, obligación y restricción de tiempo, párrafo breve; no justicia garantizada ni retorno, historia de la familia/porcentajes/divorcio/hipótesis biológicas utilizados. No A Treatise1981 íntegro leído. Derivación conjunta736–737 mantenida breve, sin reproducir su teorema o ecuaciones.',
 'Páginas1 y9–11 del PDF; enfoque económico, sin leer el libro completo.'),
 source('Nancy Folbre · Making Care Affordable is Key to Our Economic Future · 2026','https://www.ucpress.edu/blog-posts/making-care-affordable-is-key-to-our-economic-future',
 'Artículo firmado por autora, UCPress2enero2026, HTML200190636B y texto visible33–48 leído. Valor del cuidado no remunerado, reducción de oportunidades de ingresos y límites de los precios para captar beneficios sociales. No todas sus estadísticas/diagnósticos estadounidenses asumidos ni actualización de leyes o inflación. The Invisible Heart2001 como antecedente del brief, no leído entero. Tres condiciones éticas, hoja y ejemplos son MEE, no escala clínica de Folbre.',
 'Texto firmado de2026 sobre costes y beneficios del cuidado; no lectura íntegra de The Invisible Heart.')],
 omitted=['Tribu como término editorial, sin origen antropológico universal.', 'Sin relación familiar equiparada a aceptación, deuda o disponibilidad ilimitadas.', 'Sin resultados educativos, ingresos futuros o reciprocidad garantizados.']),
'E2.1.02':dict(
 seo_title='Familia como primera empresa: tiempo y cuidados | MEE',
 description='Familia como primera empresa: una metáfora para revisar recursos, cuidados y tareas. MEE explica su alcance, datos de uso del tiempo y acuerdos del hogar.',
 keyword='familia como primera empresa',secondary=['economía doméstica','trabajo no remunerado','uso del tiempo','Gary Becker'],
 standfirst='Familia como primera empresa: una comparación delimitada para examinar tiempo y recursos, con preguntas de MEE sobre cuidados, tareas y participación.',
 sources=[
 source('Comité del Nobel · presentación de Becker · 1992','https://www.nobelprize.org/prizes/economic-sciences/1992/press-release/',
 'Fuente institucional primaria del premio, HTML200174440B; apartado Household and Family de la página consultado por búsqueda y HTML. Hogar combina bienes/tiempo, ejemplo comidas/alojamiento; publicación1981 del Treatise. No modelo propio de MEE atribuido aBecker ni libro íntegro consultado. No cifras históricas o efectos demográficos del comunicado como actual2026.',
 'Apartado sobre hogar y familia; explicación institucional del enfoque, sin leer el libro completo.'),
 source('Gary S. Becker · conferencia Nobel · 1992',lecture,
 'Mismo PDF primario archivado, lectura páginas1 y9–11, render1. Para737: reconocimiento de amor/obligación/deber y diferencia entre familia y empleados en PDF11/impresa48. Un párrafo breve del contraargumento, más referencia breve en apertura. No historia universal, cifras de divorcio, explicaciones biológicas o teoremas de altruismo como recomendaciones. Alcance parcial explícito.',
 'Páginas1 y9–11 del PDF; pasajes sobre motivaciones y relaciones familiares.'),
 source('OCDE · base de uso del tiempo','https://www.oecd.org/en/data/datasets/time-use-database.html',
 'Página oficial: apartados3713–3723 About y actualización30abril2026 leídos en web; directo403 registrado. Cinco grandes categorías y muestra15–64; cautelas por diarios/encuestas/clasificación y diferentes años de campo. No tablas actuales completas descargadas ni precios/salarios/valor monetario calculados. FuenteF114 del brief tratada mediante página actual, no cifras de un archivo inaccesible. Sin inferencia individual desde medias poblacionales.',
 'Presentación y cautelas metodológicas de la base, con actualización de2026; sin asignar cifras nacionales a un hogar.')],
 omitted=['No familia registrada como empresa ni autoridad ilimitada por aportar dinero.', 'Sin precio universal del cuidado ni porcentajes o medias históricas publicados como actuales.', 'Sin tarifas, deudas, resultados o reparto obligatorio deducidos de una metáfora.'])}
for ident,m in metadata.items():
 print(ident,len(m['seo_title']),len(m['description']))
 assert 50<=len(m['seo_title'])<=60 and 140<=len(m['description'])<=155
p=Path(__file__).with_name('metadata735737.json');assert not p.exists();p.write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
