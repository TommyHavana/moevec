# MEE · contexto portable

Actualizado el 28/10/2026 (Europe/Madrid). Estado actual, no una orden de volver a ejecutar trabajos terminados.

MEE significa Movimiento de Evolución Económica. Fuente local: `/Users/nerea/Documents/Proyectos/MEE/mee-web`. Fuente privada de despliegue: `../mee-deploy-source`, repositorio `TommyHavana/moevec`. Next.js/React/TypeScript exportado a estático, Nginx, WordPress en `/blog/`, MariaDB y Coolify. React está publicado en `https://moevec.org/`; blog, contacto y correo funcionan. No reconstruir desde cero.

El fundador encargó expresamente y autorizó ejecutar una auditoría integral de UI/UX, gráficos, WPO y SEO/GEO, contacto con `contacto@moevec.org`, una maqueta por subcategoría y preparación de la integración social. Se guardó primero el diagnóstico y se aplicaron cambios. Informe y pruebas: `docs/22-AUDITORIA-UIUX-WPO-SEO-GEO.md` e `inventario/auditoria-2026-10-28/`.

Se conservan siete áreas, 56 temas principales y 59 internos políticos. Hay 115 ilustraciones propias en WebP y 115 maquetas de artículo distribuidas en 122 categorías. Manifiesto generado: `content/visuals.json`; fuente canónica original en `fuentes/claude/docs/02-taxonomia.md`. No editar JSON generado a mano. Los textos y ejercicios de muestra están identificados como tales y no son estudios ni casos reales.

La portada tiene anillo con relieve, luz y surcos móviles, tipografía animada y fondo; React y WordPress comparten cursor, estrella de transición, identidad, pausa y reducción de movimiento. Cada familia visual tiene su acción; los temas internos se despliegan con imagen propia. Los guiones originales del inventario son propuestas: el manifiesto describe los recursos realmente integrados. Referencia de ritmo/escala: Turner Duckworth. No copiar sus recursos ni prometer Awwwards.

Contacto React usa una ruta WordPress del mismo origen. SMTP de DonDominio, solicitud al buzón y acuse HTML al remitente probados, incluso recepción externa con SPF/DKIM/DMARC pass. La configuración privada vive en el volumen de secretos; nunca copiar contraseñas a Git o documentos. WordPress `mee_admin` tiene segundo factor por correo al buzón operativo. No se cambió su contraseña.

Search Console tiene la propiedad de dominio verificada por DNS y un sitemap correcto con 12 páginas descubiertas. Maquetas y archivos que solo contienen muestras llevan noindex y se excluyen de sitemap/webhook. En el editor existe el control «Maqueta editorial»; al retirarlo tras revisión se recalculan las categorías. Las puntuaciones de laboratorio son 97–98 de rendimiento y 100 de accesibilidad/buenas prácticas; las muestras penalizan la puntuación SEO por su noindex intencionado. No hay todavía INP de campo ni garantía de indexación.

Red social: el puente WordPress/React está preparado, con HMAC, cola, reintentos y caché. `integrations/phoenix/` conserva los módulos del usuario. `red.moevec.org` no tiene API operativa con TLS válido y falta el proyecto Phoenix completo/acceso a su entorno. Mantener el puente desactivado; no fingir conversación ni cuentas. Guía: `integrations/README.md`.

Pendientes externos: identidad jurídica y expediente legal del responsable; despliegue completo de Phoenix; revisión y desarrollo editorial definitivo; Bing sin sesión; valorar copia externa cifrada y arranque de una restauración completa en otro entorno. Ya se restauró la SQL en base aislada (12 tablas) y se extrajeron los archivos del respaldo. WooCommerce y pagos siguen fuera de alcance.

Comandos: `npm run content:sync`, `npm run assets:build` (desde la fuente local con maestros), `npm run build`, `npm run backup`. Antes de continuar, leer AGENTS, estado 15, backlog 16 e informe 22. La petición nueva fija el alcance.

## Apoyo económico · actualización del 29/10/2026

El fundador encargó una página para donaciones y publicidad de empresas afines. Está publicada en `https://moevec.org/apoya/`, enlazada solo desde los footers de React y WordPress. El contacto selecciona donación o publicidad a través de `?tema=donacion` o `?tema=publicidad`. El medio de donación está pendiente; por ahora se acuerda la aportación por correo, sin cobro automático. Fuente de producto privada: commit `1d84a45`, con actualización de archivos en contenedores activos y sin reconstrucción de imágenes Docker. Verificación y límites en el estado 15 y `inventario/apoyo-2026-10-29/`. No cambia la producción editorial ni activa la tienda.

## Presentación editorial completa de categorías y subcategorías

El texto siguiente conserva el documento editorial de trabajo. Sus nombres canónicos proceden de la fuente del proyecto; sus descripciones son propuestas, no una aprobación final del fundador.

# MEE · Presentación de categorías y subcategorías

**Estado:** propuesta de texto para la web y el style guide, pendiente de revisión del fundador. Los nombres y el orden proceden de `fuentes/claude/docs/02-taxonomia.md`; las presentaciones son redacción nueva. En «Política y Economía», los diez elementos principales son **ejes** y contienen temas adicionales que se conservan en la taxonomía original.

## Presentación general de las áreas

**Título sugerido:** Siete maneras de avanzar.

**Entradilla:** Una idea puede cambiar cómo tomas una decisión. Una habilidad puede cambiar lo que eres capaz de construir. MEE reúne siete áreas para recorrer ese camino: pensar con criterio, cuidar los vínculos, participar en comunidad, trabajar con propósito, comprender la economía, crear prosperidad compartida y examinar las reglas que afectan a todos. Puedes empezar por la pregunta que hoy te resulte más cercana.

**Texto breve para el mosaico:** Explora cada área. Descubre las ideas, decisiones y capacidades que puedes llevar de la teoría a la vida real.

## 01 · Educación y Valores

**En el cuadro:** Aprende a pensar por ti mismo.

**Presentación:** Todo comienza con la forma en que interpretamos el mundo. Esta área reúne las preguntas que sostienen las demás: qué significa ser libre, cómo asumimos nuestras decisiones, qué derechos defendemos y cómo sabemos si una idea merece nuestra confianza. MEE propone explorar esos valores con argumentos y objeciones, con atención a la evidencia y a las condiciones reales en que vive cada persona. El objetivo es ganar criterio propio, no memorizar una respuesta.

**Subcategorías**

1. **Autonomía.** Comprender qué opciones tienes y ampliar tu capacidad de decidir con información.
2. **Responsabilidad Personal.** Reconocer tus decisiones y distinguirlas de circunstancias que escapan a tu control.
3. **Escepticismo Constructivo.** Poner a prueba una idea con curiosidad, buenas preguntas y disposición a corregirte.
4. **Libertad de Expresión.** Entender por qué importa poder decir, escuchar y discutir incluso lo incómodo.
5. **Propiedad Privada.** Explorar cómo se adquieren, usan, protegen y transmiten los bienes, y qué debates plantea.
6. **Iniciativa.** Convertir una inquietud en el primer paso para desarrollar capacidades propias.
7. **Salud Mental.** Pensar el bienestar personal junto a las condiciones sociales e institucionales que lo afectan.
8. **Justicia.** Examinar las reglas, los derechos y el trato entre personas desde la perspectiva que propone MEE.
9. **Educación Científica y Actualizada.** Aprender a revisar lo que creemos cuando aparecen mejores conocimientos y pruebas.

## 02 · Tribu

**En el cuadro:** Construye vínculos que perduren.

**Presentación:** Nadie avanza completamente solo. «Tribu» nombra a las personas con quienes compartimos cuidado, conocimientos y compromisos duraderos: familia de origen, familia elegida y quienes deciden acompañarse. Aquí se habla de lo que una generación puede transmitir a otra, pero también de límites, consentimiento y autonomía. La confianza se construye cuando sabemos qué podemos esperar unos de otros y podemos hablar de ello con honestidad.

**Subcategorías**

1. **Sacrificio Tribal.** Elegir un esfuerzo presente para alcanzar una meta compartida y libremente acordada.
2. **Herencia.** Pensar qué recursos, conocimientos y obligaciones se transmiten a quienes vienen después.
3. **Responsabilidad Generacional.** Considerar cómo afectan nuestras decisiones de hoy a otras etapas de la vida y a otras personas.
4. **Transmisión de Valores.** Compartir criterios y hábitos sin exigir que la siguiente generación renuncie a pensar por sí misma.
5. **Agradecimiento.** Reconocer de manera concreta el apoyo recibido y lo que hizo posible.
6. **Lealtad Tribal.** Cuidar compromisos mutuos sin convertir la cercanía en una obligación de obedecer.

## 03 · Comunidad

**En el cuadro:** Encuentra tu lugar para aportar.

**Presentación:** Una comunidad crece cuando las personas pueden entrar, expresar sus intereses y contribuir de forma visible. MEE quiere abrir espacio a la conversación, al desacuerdo razonado y al reconocimiento de las aportaciones útiles. Esta área presenta los principios para colaborar con reglas comprensibles y acceso amplio, también para quien dispone de pocos recursos o una conexión limitada. Las herramientas futuras podrán facilitarlo; la participación empieza por cómo tratamos a los demás.

**Subcategorías**

1. **Interés Transparente.** Decir con claridad qué buscas, qué ofreces y qué esperas de una colaboración.
2. **Mérito por Aporte.** Reconocer lo que ayuda a otros a comprender, crear o resolver un problema.
3. **Accesibilidad.** Reducir barreras económicas, técnicas y de lenguaje para que más personas puedan participar.
4. **Intercambio Equitativo.** Acordar qué recibe cada parte y revisar si la relación funciona para ambas.

## 04 · Trabajo

**En el cuadro:** Convierte experiencia en posibilidades.

**Presentación:** El trabajo puede ser una fuente de aprendizaje, criterio y autonomía económica. Esta área sigue la ruta que imagina MEE —de trabajador a emprendedor, empresario y, si se desea y resulta posible, inversor— sin tratarla como un destino obligatorio. Cada paso plantea decisiones distintas sobre tiempo, habilidades, socios y riesgo. El propósito es reconocer el valor de la experiencia que ya tienes y descubrir qué capacidades podrías desarrollar a partir de ella.

**Subcategorías**

1. **Sacrificio Estratégico.** Elegir qué esfuerzo merece tu tiempo porque responde a un objetivo definido.
2. **Inversión Personal.** Dedicar recursos a aprender habilidades que puedan abrir opciones reales.
3. **Riesgo Consciente.** Entender lo que puedes perder antes de comprometer dinero, tiempo o estabilidad.
4. **Escalabilidad Social.** Pensar cómo crecer creando también espacio y valor para otras personas.
5. **Selección de Socios.** Hablar de expectativas, responsabilidades y posibles desacuerdos antes de asociarte.
6. **Experiencia como Activo.** Identificar lo que aprendiste trabajando y cómo puede servir para resolver nuevos problemas.
7. **Mentoría e Inversión en Otros.** Compartir conocimientos y apoyar el desarrollo de capacidades ajenas con acuerdos claros.
8. **Diferenciación de Valor.** Explicar a quién ayudas, qué necesidad atiendes y por qué tu propuesta importa.
9. **Resiliencia Económica.** Preparar alternativas y margen de maniobra ante periodos de ingresos inciertos.
10. **Tiempo como Recurso Finito.** Decidir qué tareas merecen atención y cuáles impiden avanzar hacia una meta.
11. **Claridad de Propósito.** Tener una razón comprensible para orientar decisiones y revisar el rumbo cuando haga falta.
12. **Adaptabilidad Técnica.** Aprender herramientas y métodos nuevos sin perder de vista el problema que resuelves.

## 05 · Capitalismo Consciente

**En el cuadro:** Entiende las reglas del intercambio.

**Presentación:** Para discutir un sistema económico primero hay que saber qué significa y cómo ha cambiado. MEE propone estudiar el capitalismo desde el trabajo, el ahorro, la iniciativa y los acuerdos voluntarios, sin confundirlo con la necesidad de consumir cada vez más. Esta área abre comparaciones con otras ideas y experiencias históricas, incluidos los servicios sociales, sus resultados y sus críticas. Las convicciones del proyecto se presentan como argumentos que pueden examinarse, no como sustitutos de los datos.

**Subcategorías**

1. **Definición Esencial.** Acordar de qué hablamos cuando usamos la palabra «capitalismo».
2. **Historia.** Situar instituciones, cambios y experiencias económicas en su época y contexto.
3. **Capitalismo vs. Socialismo.** Comparar principios, incentivos y resultados con definiciones y evidencia precisas.
4. **Capitalismo en Esferas Inesperadas.** Reconocer cooperación e intercambio voluntario fuera de los ejemplos habituales.
5. **Modelos Nórdicos.** Estudiar políticas concretas y sus contextos antes de extraer conclusiones generales.
6. **Servicios Sociales.** Preguntar cómo se financian, a quién llegan y qué resultados muestran.
7. **Ética en el Intercambio.** Examinar consentimiento, información, responsabilidad y trato justo en cada acuerdo.
8. **Ahorro y Frugalidad.** Entender cómo reservar recursos hoy puede ampliar opciones mañana.

## 06 · Economía Compartida

**En el cuadro:** Crece sin dejar a otros atrás.

**Presentación:** MEE llama «economía compartida» a una forma de pensar la prosperidad en la que muchos actores pequeños pueden crear y conservar valor. La propuesta se interesa por las capacidades locales, por las redes de proveedores y por acuerdos que permitan colaborar sin perder autonomía. En esta área examinamos cómo se forma una cadena de valor, qué puede fortalecerla y qué preguntas debe responder cualquier participación económica antes de ponerse en marcha. Los ejemplos sirven para aprender a decidir; no son ofertas de inversión.

**Subcategorías**

1. **Definición de Economía Compartida.** Entender el sentido específico que MEE da a esta propuesta de prosperidad distribuida.
2. **Solidaridad Capitalista.** Explorar cuándo un intercambio voluntario puede fortalecer a productores y servicios cercanos.
3. **Especialización Estratégica Escalonada.** Desarrollar capacidades locales sin depender de una única actividad.
4. **Diversificación Comercial Inteligente.** Abrir distintas vías de intercambio para reducir vulnerabilidades.
5. **Empoderamiento de Microemprendedores.** Facilitar conocimientos y herramientas a quienes construyen proyectos pequeños.
6. **Inversión Distribuida y Contratos Comunitarios.** Comprender aportaciones, derechos y riesgos antes de considerar cualquier acuerdo de participación.
7. **Escalabilidad con Autonomía.** Diseñar colaboraciones que puedan crecer sin quitar capacidad de decisión a sus participantes.

## 07 · Política y Economía

**En el cuadro:** Pregunta quién decide las reglas.

**Presentación:** Las ideas anteriores adquieren otra dimensión cuando una ley, un impuesto o una decisión pública cambia lo que las personas pueden hacer. Esta área aplica las herramientas de MEE al análisis de medidas concretas, de distintos países y épocas. Cada caso deberá indicar qué norma se estudia, cuándo y dónde rige, a quién afecta, qué razones la apoyan, qué críticas recibe y qué evidencia existe sobre sus efectos. El propósito es discutir decisiones públicas con contexto y precisión, sin atribuir intenciones o delitos sin pruebas.

**Diez ejes principales**

1. **Regulación y Emprendimiento.** Examinar los trámites y límites que intervienen al abrir o mantener una actividad.
2. **Impuestos y Redistribución.** Seguir cómo se recaudan recursos, quién soporta la carga y cómo se utilizan.
3. **Propiedad Privada y Expropiación.** Distinguir nacionalización, límites de uso e inseguridad jurídica para analizar cada caso con precisión.
4. **Inversión y Capital.** Revisar las reglas que afectan al ahorro, las inversiones y el movimiento de capital.
5. **Monopolios Estatales vs. Competencia.** Investigar qué opciones tienen las personas y qué barreras enfrentan posibles alternativas.
6. **Subsidios y Favoritismo Político.** Preguntar cómo se asignan recursos públicos y con qué criterios se justifican.
7. **Libertad de Expresión Económica.** Observar qué información puede difundirse y debatirse sobre decisiones financieras y económicas.
8. **Migración de Capital.** Entender las condiciones para mover dinero y patrimonio entre monedas y países.
9. **Regulación Financiera.** Estudiar las exigencias que afectan a bancos, nuevos servicios y acceso al crédito.
10. **Corrupción Sistémica.** Analizar mecanismos de abuso de poder únicamente a partir de hechos documentados y fuentes comprobables.

**Profundidad del tercer eje:** «Propiedad Privada y Expropiación» se desarrolla en **Nacionalizaciones y Confiscaciones Estatales**, **Regulaciones que Limitan el Uso de la Propiedad** e **Inseguridad Jurídica (Cambios de Leyes Retroactivos)**. Los dos últimos agrupan once temas más específicos sobre vivienda, uso de tierra, transferencias, trato a extranjeros, retroactividad, cambios tributarios, derechos de propiedad, estabilidad normativa, interpretación de leyes, aplicación selectiva y moneda. Sus títulos completos figuran en la taxonomía original y deben mantenerse en cualquier navegación o publicación posterior.

## Uso en la interfaz

- La frase **«En el cuadro»** cabe sobre la imagen de cada categoría y puede servir también de texto de apoyo accesible.
- La **presentación** puede ir debajo del título en la página interior. Cada frase de subcategoría funciona como entrada breve junto al índice y permite enlazar futuras piezas editoriales.
- El texto es una propuesta: no implica que haya ya artículos, comunidad, ofertas de inversión, análisis de leyes ni tienda publicados.

## Actualización · producción editorial de 840 entradas

El fundador ordenó retirar las 115 maquetas e iniciar el plan de 840 briefs (56 subcategorías × 15). Su importador está desactivado y fuera del arranque. La numeración global sigue el orden de tandas del documento original, no el orden taxonómico: n.º 1 = E5.1.01. Las primeras tres están publicadas con nueve imágenes originales en total; n.º 4–840 pendientes en esta entrega. Cada artículo requiere fuentes abiertas y contrastadas, portada y dos interiores propios, WebP inferiores a 250 KB y verificación. `docs/24-REGISTRO-PRODUCCION-840.md` y WordPress → Herramientas → Plan editorial · 840 contienen el estado individual. `scripts/sync-production-status.py` vuelve a leer WordPress y actualiza MD/CSV/JSON. No contar maquetas ni borradores vacíos como producción. Siguiente: E5.1.04.

## Continuidad automática

El fundador autorizó avanzar continuamente en bloques de tres hasta completar las 840. La automatización de este hilo ya existe y está ACTIVE: `producci-n-editorial-mee-840`; comprueba la continuación cada cinco minutos y cada ejecución puede seguir al bloque siguiente. No duplicarla. Leer `docs/26-PRODUCCION-CONTINUA.md`, WordPress y `editorial/production-state.json`. El ordenador debe estar encendido y la app abierta para los accesos locales. Primer bloque en investigación: n.º 4–6, E5.1.04–06, Capitalismo Consciente → Definición Esencial; no confundir sus notas de investigación con artículos completos.


## Jerarquia del blog confirmada por el fundador

Blog es el contenedor general, no una categoria adicional. El inventario coincide con los 122 nodos y siete areas previstos. Se corrigieron las rutas visuales y schema para incluir area y subcategoria, y se elimino la categoria tecnica vacia Uncategorized. Detalle y evidencia en docs/produccion/2026-10-28-jerarquia-blog.md. El publicador asigna siempre por el manifiesto; la produccion continua.


## Cierre editorial ·05/11/2026

**840/840 terminadas, 2520 imágenes originales públicas, 0 en curso y 0 pendientes.** Las seis alternativas fueron aprobadas explícitamente por el fundador, publicadas y verificadas. Se conservan todos los identificadores y slugs; el plan editorial queda cerrado y la automatización eliminada.

Títulos definitivos y comprobaciones en `docs/produccion/2026-11-05-cierre-840.md`. Los seis originales de título permanecen documentados en la aprobación y en los briefs; ID y slugs se conservan. No hay próximo bloque ni seguimiento de producción activo.


## Rutas y Rank Math ·05/11/2026

Encargo autorizado sin nuevas confirmaciones: paquete «Empieza aquí» publicado con tres rutas y 18 lecturas, marcas locales, filtros de tema/nivel, relacionados, continuidad y RSS. Rank Math 1.0.281 instalado y activo; 840 entradas y 2520 imágenes con metadatos migrados; 122 categorías conservadas. Se corrige la descripción duplicada de Hello Elementor y se coordinan schema y sitemaps con Next.js. Puntuación real tras revisión: media78,27, mínimo67, máximo88, 513 verdes y0 por debajo de50. Search Console, tracking y analytics los configurará el fundador. El padre de plugins permanece protegido después del rechazo automático a ampliar sus permisos; la instalación se realizó solo por despliegue. Ver `28-RUTAS-Y-SEO-RANK-MATH.md` para evidencia y el punto de verificación/despliegue final. La producción840 ya está cerrada y su automatización retirada.


### Entrega definitiva de rutas y SEO ·05/11/2026

Terminado y desplegado desde `e104c62c` (Coolify `mtwkdp9b1exqpphniveo4z7c`). Auditoría posterior:840/840 URLs correctas,2520 imágenes WebP servidas,18 páginas principales correctas,840 artículos únicos en sitemap y2520 referencias de imagen. H1/slugs/122categorías conservados, cero borradores y cero errores de metadatos. Nueve archivos de plugin/tema coinciden por SHA256. Rank Math1.0.281 activo, puntuación real final media78,27, mínimo67, máximo88,513verdes y0 por debajo de50; las cifras78,10/461fueron un corte intermedio. Tres rutas,18continuaciones y8RSS comprobados; marcas locales persistentes y móvil390px sin desbordamiento. Tracking de uso de Rank Math desactivado.

Copias: fuente proporcional local y VPS; SQL consistente posterior guardado solo en VPS (su descarga local fue rechazada por revisión automática por datos sensibles potenciales; no se descargó). Permisos del padre de plugins preservados; instalación acotada por despliegue. Evidencia en `inventario/rutas-seo-2026-11-05/` y detalle en `28-RUTAS-Y-SEO-RANK-MATH.md`. Pendiente para el fundador: conectar Search Console y analytics. No hay implementación ni despliegue pendiente de este paquete y no se creó otra automatización.


## Auditoría integral y redes · 05/11/2026

Auditoría entregada en `29-AUDITORIA-INTEGRAL-Y-REDES.md`, con 24 mejoras priorizadas y evidencia en `inventario/auditoria-integral-2026-11-05/`. Consulta nueva de WordPress a las 13:28 UTC: 840 artículos, 2520 originales, 122 categorías, 0 borradores y 0 errores de metadatos. Se realizaron 154 comprobaciones públicas sin fallos de carga y con el 404 esperado. Hallazgos: 59 archivos internos vacíos; 328 piezas sin enlaces entrantes desde otros cuerpos (no equivale a páginas huérfanas); 9 cuerpos con numeración interna; asunto editorial no preseleccionado; 404 con robots contradictorios; datos legales pendientes y distribución social sin conexión acreditada.

Se corrigen instrucciones de continuidad obsoletas. No se modifica producción ni se crean cuentas, publicaciones o automatizaciones; el plan de corrección queda propuesto. Métricas privadas y aceptación de cuentas siguen bajo control del fundador. Siguiente paso propuesto: corregir A09/A10/A11 y ejecutar el primer ciclo del informe. Evidencias: auditoría HTTP, consulta WordPress, estructura de enlaces, capturas móviles, observaciones operativas y `npm audit --omit=dev` sin avisos. La comprobación no certifica todos los hechos publicados, cumplimiento legal ni accesibilidad global.
