# MEE · contexto portable para un nuevo chat

Fecha: 28/10/2026, Europe/Madrid. Lee este documento antes de continuar. Es una fotografía del estado y las decisiones: contrasta cualquier cambio posterior con los archivos actuales. No da acceso al código de otro chat ni reemplaza una instrucción reciente del fundador.

## Proyecto

MEE, Movimiento de Evolución Económica. Web de capacidades, educación y reflexión económica organizada en siete áreas. Identidad propia distinta de Calicata. Presentación pública sin historias personales de fundadores. Referencia de escala, ritmo gráfico y experiencia: https://turnerduckworth.com/; crear contenido, escenas y código propios. Aspiración a calidad de una candidatura Awwwards, sin prometer premio.

## Carpeta y tecnología

`/Users/nerea/Documents/Proyectos/MEE/mee-web` es la carpeta local usada en esta sesión. Abrir esa carpeta en Codex. Existe una base Next.js/React/TypeScript, App Router, `output: "export"`, siete rutas de área y portada. `npm ci`; `npm run dev`; localhost:3000; `npm run content:sync`; `npm run build`; `npm run backup`. No reconstruir el proyecto. El fundador ha encargado desplegar con Coolify y avanzar WordPress; el estado exacto está en `docs/15-ESTADO-Y-CONTINUIDAD.md`.

## Decisiones y requisitos

- React sigue en desarrollo. El 28/10/2026 el fundador compró `moevec.org` y encargó expresamente DNS, Coolify y WordPress editorial con tema hijo de Hello Elementor. La publicación y la instalación se verifican por separado; no declarar el blog operativo antes de comprobarlo.
- Portada y mosaico de siete categorías; interior con índice superior sticky por subcategoría. Conservar nombres, orden y slugs originales.
- Cada categoría y subcategoría tendrá imagen propia y movimiento que evoque su valor. Un zoom común no cumple por sí solo la intención semántica.
- Hay siete categorías y 56 secciones principales (9/6/4/12/8/7/10). La séptima área añade 48 temas y once subtemas internos: 122 nodos contando categorías. Los 63 principales tienen propuestas visuales; el tratamiento de los otros 59 necesita definición y no se omite.
- Todas las escenas deben conservar una composición quieta legible, alternativa de movimiento reducido y carga responsable. No reproducir 63 vídeos simultáneamente.
- Tienda futura de arte digital. Confirmar si además venderá impresiones físicas y cómo se autorizan obras y licencias.
- **No ejecutar la auditoría total todavía.** El fundador pidió primero la recomendación arquitectónica, ya respondida. Preparar documentos no equivale a encargar la auditoría.

## Arquitectura recomendada, aún no decidida definitivamente

Next.js para la experiencia visual, WordPress para gestión editorial y WooCommerce para productos, compra y descargas. El fundador ya ha elegido avanzar WordPress editorial con Hello Elementor como padre y tema hijo propio. React se prepara en `moevec.org/` y el blog en `moevec.org/blog/`, mediante una aplicación Compose en Coolify y repositorio privado de solo código. La tienda sigue sin encargo de implementación. El modo estático de Next necesita recompilar para publicar cambios de contenido; valorar servidor/revalidación cuando se defina edición real.

## Marca

Paleta de trabajo: azul #1547BB, rojo #EF383E, papel #F7F6F2, tinta #15171B y blanco. Kit en `brand-kit/`: MEE compacto e inclinado, Archivo Black Italic y estrella roja de ocho rayos; PNG/WebP comprimidos, SVG y fuentes con licencias. Archivo para display y Manrope para lectura; WOFF2 locales. Logo reconstruido a partir de la cabecera preferida; falta comparación final para usos fuera de pantalla. No sustituirlo por el logo de Calicata ni afirmar una aprobación gráfica inexistente.

## Estado comprobado y pendientes

Existe la maqueta, siete imágenes de categoría y variantes, resúmenes, índice sticky, efectos iniciales, logo y favicon. La plantilla de secciones examinada no tiene imagen por subcategoría. No hay movimiento específico terminado para cada concepto. No hay WordPress ni WooCommerce funcionales comprobados. Un build satisfactorio está documentado el 28/10/2026; no se ha repetido al crear este paquete documental. Las capturas históricas de portada no validan los interiores ni la tipografía más reciente. No se hizo auditoría total.

Los textos editoriales de presentación y beneficios son propuestas para revisión; no transformarlos en afirmaciones históricas o estadísticas demostradas. No inventar testimonios, autores, inversiones recomendadas, productos o permisos de artistas.

## Fuentes y continuidad

`AGENTS.md` es la guía de Codex; `fuentes/claude/docs/02-taxonomia.md` es la fuente original preservada. `content/*.json` se genera mediante scripts; no editarlo a mano. Los archivos históricos de Claude no prevalecen sobre instrucciones recientes. Estado en `docs/15-ESTADO-Y-CONTINUIDAD.md`; backlog en 16; requisitos visuales en 13; arquitectura propuesta en 14; brief futuro de auditoría en 18; inventario en 19; protocolo de chats en 20.

Tarea siguiente propuesta: piloto de una categoría y dos subcategorías, con metáfora, guion, imagen quieta, capas y movimiento. El encargo concreto del usuario determina qué ejecutar. No fabricar la colección completa sin revisar el lenguaje visual del piloto. Al cerrar, dejar tarea, archivos, evidencia, decisiones, pendientes y siguiente paso en un traspaso; pedir solo archivos realmente imprescindibles si no se tiene acceso al proyecto.

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
