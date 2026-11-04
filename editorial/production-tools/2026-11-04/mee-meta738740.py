from pathlib import Path
import json
def source(name,url,scope,public_scope):return dict(name=name,url=url,scope=scope,public_scope=public_scope)
metadata={
'E2.1.03':dict(
 seo_title='Gratificación diferida en familia: estudios y límites | MEE',
 description='Gratificación diferida en familia: educación, necesidades presentes y resultados inciertos. MEE revisa las fuentes y propone preparar un plan compartido.',
 keyword='gratificación diferida en familia',secondary=['educación','malvavisco','réplica conceptual','necesidades presentes'],
 standfirst='Gratificación diferida en familia: fuentes sobre educación y espera, con límites explícitos y una propuesta de MEE para preparar una conversación sobre recursos.',
 sources=[
 source('Psacharopoulos y Patrinos · Returns to Investment in Education · 2018','https://documents1.worldbank.org/curated/en/442521523465644318/pdf/WPS8402.pdf',
 'PDF oficial200847604B25 páginas, SHA conservado. Leídas PDF2,4y5: resumen, introducción y métodos; render2 inspeccionado. Base1120estimaciones139países,9porciento privado medio por año adicional referido al trabajo2018, no actualidad2026 ni interés garantizado de ahorros. Costes directos/ingresos dejados de obtener, interpretación agregada no consejo individual. No25p íntegramente leídas. Pautas de planificación y casos propios de MEE; sin ranking universal más rentable del brief.',
 'Páginas2,4y5 del PDF de2018; resultados agregados y métodos, sin promesas individuales.'),
 source('Causal returns to education · International Journal of Educational Development · 2026','https://doi.org/10.1016/j.ijedudev.2026.103565',
 'Resumen primario e información bibliográfica en búsqueda del editor: volumen122,abril2026,103565. Escolaridad modificada por variaciones de políticas y estimaciones cuasiexperimentales. No texto completo consultado; no publicar10porciento,191estimaciones/145estudios/54países como resultado individual ni comparar directamente con2018. Una frase de contexto del método, sin receta familiar.',
 'Resumen del editor del estudio de2026; lectura del resumen, sin consultar íntegramente el artículo.'),
 source('Shoda, Mischel y Peake · Predicting Adolescent Competencies · 1990','https://depts.washington.edu/shodalab/wordpress/wp-content/uploads/2015/05/1990.PredictingAdolescent_Shoda.pdf',
 'PDF primario del laboratorio del coautor,2001073782B9 páginas. Leídos resumen/página1 y página8; página2 extraída pero salida parcial, no declarar lectura íntegra. Render1 inspeccionado. Asociaciones según condiciones, población de comunidad universitaria, límites muestra/generalización explícitos en8. Sin causalidad de entrenar espera ni diagnóstico/éxito predicho para niño particular. No estudio1972 íntegro declarado leído.',
 'Resumen y páginas1y8 del PDF; asociaciones y cautelas de generalización del estudio original.'),
 source('Watts, Duncan y Quan · Revisiting the Marshmallow Test · 2018','https://pmc.ncbi.nlm.nih.gov/articles/PMC6050075/',
 'Archivo HTML/visible legítimo previo de E4.1.04 reutilizado sin nueva descarga; web actual mostró comprobación de navegador y no se sorteó. Leídos resumen e introducción inicial local; búsqueda primaria actual confirma artículo, réplica conceptual, asociaciones menores y reducción tras controles familiares/cognitivos/entorno. No texto entero leído ni tamaños precisos o coeficientes utilizados.',
 'Resumen e introducción seleccionada; copia primaria previamente archivada, sin leer todo el artículo.'),
 source('Sperber y colaboradores · Delay of gratification and adult outcomes · 2024','https://pmc.ncbi.nlm.nih.gov/articles/PMC11581930/',
 'Archivo HTML/visible legítimo previo de E4.1.04 reutilizado; web actual mostró comprobación de navegador, no eludida. Resumen e introducción inicial local leídos; publicado2024, manuscritoPMC disponible2025, no ensayo2026. No predicción adulta robusta con ajustes, no prueba de que la autorregulación carezca de valor ni causalidad económica. No artículo íntegro declarado leído.',
 'Resumen e introducción seleccionada del trabajo publicado en2024; copia primaria archivada.')],
 omitted=['No inversión educativa universalmente más rentable ni retorno o empleo garantizados.', 'No resultados del malvavisco convertidos en instrucciones para calificar a niños.', 'Sin productos, créditos, porcentajes de ahorro obligatorios o precios ficticios.']),
'E2.1.04':dict(
 seo_title='Límites del sacrificio: acuerdos, cuidados y apoyo | MEE',
 description='Límites del sacrificio: tareas, disponibilidad y continuidad de los cuidados. MEE propone revisar acuerdos y buscar apoyo sin diagnósticos caseros.',
 keyword='límites del sacrificio',secondary=['cuidados','apoyo familiar','disponibilidad','deber filial'],
 standfirst='Límites del sacrificio: preguntas de MEE sobre acuerdos y continuidad del apoyo, con referencias delimitadas sobre cuidados y sin una prueba diagnóstica.',
 sources=[
 source('Zarit, Reever y Bach-Peterson · correlatos de carga · 1980','https://doi.org/10.1093/geront/20.6.649',
 'Resumen primario de Oxford Academic recuperado por búsqueda y ficha PubMed7203086 (sin abstract enPubMed). Apertura directa delDOI inaccesible; lectura limitada al resumen del editor. Estudio cuidadores de mayores con demencia; asociación menos carga/más visitas, no causalidad ni cualquier familia. No texto completo o escala aplicada, versión/cortes/ítems no reproducidos.',
 'Resumen del editor del estudio de1980; no lectura completa ni aplicación de una escala.'),
 source('OMS · ficha sobre demencia · 26/10/2026','https://www.who.int/en/news-room/fact-sheets/detail/dementia',
 'Página oficial actual26oct2026 consultada, párrafos161–162 sobre apoyo a cuidadores leídos; sin inferir diagnóstico ni estadísticas agregadas trasladadas a una familia. Apoyo de familiares/amigos/profesionales, necesidades propias y descansos; no medicación ni tratamiento específico o supuesta eficacia individual. Se archiva la respuesta web con fecha y alcance.',
 'Pasajes sobre apoyo a quienes cuidan; ficha actualizada el26/10/2026, sin evaluar una persona.'),
 source('OMS · iSupport','https://www.who.int/teams/mental-health-and-substance-use/treatment-care/isupport',
 'HTML oficial200150917B, presentación y módulos/programa consultados; recurso formativo para cuidadores de personas con demencia, objetivo no resultado garantizado. No manual entero o instrucciones adaptadas como tratamiento; ensayo2024/2025 localizado con resultados nulos no se utiliza para afirmar eficacia. F052WorldMentalHealthReport2022 solo ficha localizada, no lectura completa ni utilizada para cifras.',
 'Presentación del recurso de formación; no garantiza resultados ni sustituye una valoración profesional.'),
 source('Aristóteles · Ética a Nicómaco · libroIX, capítulo2','https://classics.mit.edu/Aristotle/nicomachaen.9.ix.html',
 'Texto primario ediciónWDRoss enMIT, pasajes40–49 libroIXcap2 leídos: prioridad de ayudar a padres necesitados y rechazo a preferir a la misma persona en todo. No obligación filial incondicional atribuida al autor, libro completo ni criterio jurídico actual. Se formula objeción fuerte sobre necesidades persistentes y respuesta ética de MEE.',
 'LibroIX, capítulo2, pasajes sobre deberes familiares; lectura parcial de la traducción deW.D.Ross.')],
 omitted=['No diagnóstico de abuso, parentalización o sobrecarga desde preguntas propias.', 'Sin horas universales, versión de escala o puntos de corte inventados.', 'Sin abandono de necesidades dependientes, derecho individual o prestación garantizada deducidos de un ejemplo.']),
'E2.1.05':dict(
 seo_title='Esfuerzo con sentido: metas, acuerdos y límites | MEE',
 description='Esfuerzo con sentido: propósito, etapas y recursos en proyectos compartidos. MEE propone escuchar motivos y revisar límites sin prometer menos cansancio.',
 keyword='esfuerzo con sentido',secondary=['propósito compartido','etapas','motivaciones','acuerdos revisables'],
 standfirst='Esfuerzo con sentido: una propuesta de MEE para escuchar motivos, describir recursos y revisar etapas, con el propósito elegido por quienes participan.',
 sources=[source('Alexander Batthyány · Instituto Viktor Frankl · presentación de logoterapia','https://www.viktorfrankl.org/logotherapy.html',
 'HTML institucional20011997B y texto visible completo leído. Uso restringido a presentación del enfoque de sentido y prohibición de imponer valores/significados, autorAlexanderBatthyány identificado. No eficacia terapéutica, técnicas, causas de trastornos o interpretación de síntomas reproducidas. El hombre en busca de sentido del brief no leído íntegro ni atribuido como fuente directa. Metas/listas/reconocimiento de etapas y dos ejemplos son MEE, no recetaFrankl validada ni garantía de menos cansancio.',
 'Presentación institucional del enfoque y del respeto al significado personal; no lectura íntegra del libro deFrankl.')],
 omitted=['No efecto universal del propósito sobre resistencia, cansancio o salud.', 'Sin analogía entre proyectos cotidianos y experiencias de campos de concentración.', 'Sin terapia, culpa o deber ilimitado derivados de una meta.'])}
for ident,m in metadata.items():
 print(ident,len(m['seo_title']),len(m['description']))
 assert 50<=len(m['seo_title'])<=60 and 140<=len(m['description'])<=155
p=Path(__file__).with_name('metadata738740.json');assert not p.exists();p.write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
