# Registro de decisiones y pendientes

## Cerrado para trabajar en local

| Decisión | Estado | Fuente |
| --- | --- | --- |
| MEE · Movimiento de Evolución Económica | Elegido | ZIP Claude / `docs/01-proyecto.md` |
| Siete áreas y taxonomía interna | Fuente recibida y preservada | ZIP Claude / `docs/02-taxonomia.md` |
| Primera fase: React local | Confirmado | Instrucción reciente del fundador |
| Sin Git ni GitHub Actions | Superado el 28/10/2026 para el despliegue: repositorio privado autorizado; Actions no disponible tres días | Nueva instrucción del fundador |
| Portada de dos tiempos, siete imágenes e interiores con índice sticky | Dirección aprobada para construir y revisar | Instrucción reciente del fundador |
| WordPress después de terminar React | Superado el 28/10/2026: blog encargado en paralelo | Nueva instrucción del fundador |

## Propuesta de trabajo, pendiente de aprobación visual/editorial

El 27/10/2026 se instaló Next, se creó `package-lock.json` y `npm run build` pasó. La portada se capturó completa en Chrome a 1440 y 390 px; esto valida la representación actual, no su aprobación visual definitiva ni las páginas interiores.

- Los siete resúmenes, 56 frases de beneficio y títulos de interfaz escritos en este paquete. Los nombres de los temas originales no son provisionales; la redacción nueva sí.
- El texto de presentación para las siete categorías y sus 56 apartados de `11-PRESENTACION-CATEGORIAS-Y-SUBCATEGORIAS.md`, redactado el 27/10/2026, está pendiente de aprobación editorial.
- Paleta exacta `#1547BB` / `#EF383E`, encuadres de siete imágenes surrealistas y proporciones del mosaico.
- Ajustes finos de la primera versión del kit de marca: revisar visualmente el MEE reconstruido con Archivo y su estrella antes de aplicarlos a impresión.
- Animaciones y comportamiento detallado del scroll.

El 28/10/2026 se aclaró que React se eligió para obtener una experiencia de movimiento inspirada en la referencia. Primera implementación local: entrada secuencial del titular, desplazamiento sutil del elemento circular, revelado al scroll, énfasis de imágenes al hover o foco, índice activo y transición de página cuando el navegador la admita. Falta revisión visual y ajuste fino en dispositivos reales; no se copian los recursos ni el código de la web de referencia.

## Decidir antes de WordPress, no ahora

| Tema | Alternativas presentes en el historial | Punto de decisión |
| --- | --- | --- |
| Ruta de contenido | `/lab` en el ZIP; `/blog/` en conversación posterior | Unificar destino público y enlaces |
| Tema padre | Astra en el ZIP; Hello Elementor en base local posterior | Evaluar junto al uso real de Elementor |
| Comunidad | Perfiles, voto visible, rankings en ZIP | Definir consentimiento, moderación y reglas |
| Arte y WooCommerce | Intención de vender reproducciones | Artistas, licencias, producción, pedidos y fiscalidad |
| Dominio y servidor | Sin decisión final | Elegir cuando llegue despliegue |

## Marca en pantalla · 28/10/2026

El fundador prefirió el MEE inclinado y compacto con estrella roja de la cabecera frente al logo anterior y pidió usarlo directamente en el kit de marca para pantallas. Se dibujó el símbolo de ocho rayos y se convirtió a contornos el lettering Archivo Black Italic. Se entregan variantes tinta, blanco y azul con acento rojo, isotipos, favicons, SVG maestros, PNG/WebP optimizados, paleta, Archivo/Manrope OFL, WOFF2 latinos y guía en `brand-kit/`. La cabecera React, la estrella del cierre, el favicon y la navegación usan esos activos. Falta la confirmación visual de que la reconstrucción reproduce exactamente la versión preferida para otros usos. El ZIP original con la flecha y `fuentes/claude/brand/` se conserva como historia de diseño.

## Proyecto Codex autocontenido · 28/10/2026

La raíz `mee-web/` agrupa código React, fuente histórica, editorial, kit de marca, imágenes, guía de apertura y prompt de la siguiente fase. Se entrega como carpeta local y ZIP sin dependencias generadas, sin Git ni credenciales. Ver `docs/12-INICIO-OFICIAL-CODEX.md`. Próximo trabajo: revisión visual y funcional real de portada y siete áreas, seguida de correcciones concretas; WordPress sigue aparcado.

## Qué hacer cuando se toma una decisión

Actualizar aquí la fecha, decisión, razón, archivos afectados y quién la validó. Si cambia un nombre de tema, versionar una copia de la taxonomía aprobada y ejecutar las sincronizaciones; nunca reescribir el documento histórico dentro de `fuentes/claude/`.

## Nueva instrucción del fundador · 28/10/2026

El fundador ha comprado `moevec.org` y ha encargado expresamente configurar DNS, Coolify y Contabo, crear WordPress y avanzar el blog con un tema hijo de **Hello Elementor**. Esta instrucción sustituye el aplazamiento anterior de WordPress y resuelve la elección del tema padre para el blog. El fundador eligió después `moevec.org/blog/` para WordPress y `moevec.org/` para React, y autorizó un repositorio privado para Coolify sin depender de GitHub Actions. La tienda y la auditoría total no forman parte de esta instrucción. La publicación efectiva y las credenciales deben quedar registradas con evidencia tras la instalación.

## Requisitos y continuidad añadidos · 28/10/2026

- **Petición del fundador:** cada categoría/subcategoría tendrá imagen y movimiento ligado al valor de su contenido. No consta todavía implementación de las imágenes en las 56 secciones.
- **Recuento documentado:** siete categorías, 56 secciones principales y 59 nodos políticos internos. Estos últimos necesitan alcance visual explícito; no se eliminan.
- **Petición del fundador:** ambición de calidad Awwwards y futura tienda de arte digital. No hay premio ni tienda existentes.
- **Arquitectura adoptada en la fase actual:** Next/React para experiencia y WordPress para editorial en `/blog/`. WooCommerce para tienda/checkout sigue como recomendación futura, pendiente de decisión y encargo; no está instalado.
- **Límite expreso del fundador:** no ejecutar todavía la auditoría total. El documento 18 es solamente el brief. Esto prevalece sobre prompts antiguos de revisión global automática.
- **Entrega actual:** paquete portable de documentos y traspaso entre chats. No se cambió el código local; la incorporación se hace con el instalador y copia previa.

## Decisiones expresas del 28/10/2026 · auditoría integral

El fundador autorizó ejecutar la auditoría adjunta y todos los cambios recomendados en UI/UX, gráficos, WPO y SEO/GEO, con contacto React y correo DonDominio, coherencia de blog y una entrada de prueba por subcategoría. Esta autorización sustituye la espera anterior de auditoría y piloto en este encargo. Se conserva el modelo React + WordPress y se prepara el puente social sin migrar las áreas a WordPress.

Decisiones aplicadas: 115 maquetas identificadas y excluidas del índice/webhook; ilustraciones abstractas propias en WebP; movimiento de siete familias y pausa compartida; formulario del mismo origen usando SMTP privado; segundo factor por correo; Search Console y sitemap público. Las entradas pueden pasar a contenido editorial mediante el control de maqueta tras su revisión.

No se han inventado datos jurídicos del titular, una aplicación Phoenix accesible, actividad social, autores reales ni resultados de investigación. Siguen pendientes esos datos legales, el despliegue real de la red y la revisión editorial definitiva. La tienda y la licencia abierta general no se activan por este encargo.

## Decisión del fundador · inicio de las 840, 28/10/2026

Retirar las 115 maquetas e iniciar la producción editorial real, con numeración individual persistente. Cada artículo debe llevar portada y dos imágenes interiores propias. Se conserva el orden de las 56 tandas del documento de producción. Se mantienen el SEO y el schema del plugin MEE existente para evitar salidas duplicadas. Anacleto se presenta como firma editorial, sin currículum ni identidad personal inventados. El registro distingue terminadas, en curso y pendientes; consulta el documento 24 para el conteo vivo.

## Decisión del fundador · continuidad automática, 28/10/2026

Autorizó completar bloques de tres y pasar a los siguientes sin confirmaciones, manteniendo organización por categoría y subcategoría, imágenes propias y numeración individual. El seguimiento se configuró en el mismo chat, sin abrir tareas paralelas. No implica que tres artículos estén terminados por cada intervalo de comprobación.


## Jerarquia del blog confirmada por el fundador

Blog es el contenedor general, no una categoria adicional. El inventario coincide con los 122 nodos y siete areas previstos. Se corrigieron las rutas visuales y schema para incluir area y subcategoria, y se elimino la categoria tecnica vacia Uncategorized. Detalle y evidencia en docs/produccion/2026-10-28-jerarquia-blog.md. El publicador asigna siempre por el manifiesto; la produccion continua.

## Continuidad editorial ·27/840 ·28/10/2026

Bloques22–27 publicados y verificados sin cambiar categorías ni tema. Se mantiene la jerarquía del plan y se añade la etiqueta pais-cuba prevista paraE5.3.11. Los datos históricos y jurídicos conservan fecha y versión: Gallup2026, Cuba con gacetas de septiembre2026 y DL88concordado. No atribuir cuotas económicas deGAESA sin cuentas y perímetro verificables. Bloque28–30 en investigación local con nueve imágenes listas; no contarlo como completo. Respaldo completo tras27 entradas documentado en docs/produccion/2026-10-28-respaldo-veintisiete-entradas.md.

## Continuidad editorial ·30/840 ·28/10/2026

Bloque28–30 publicado y verificado. Capitalismo vs. Socialismo alcanza15/15. La tesis de Niemietz se atribuye y contrasta con una crítica contemporánea de1936. La pobreza histórica conserva método CBN y las líneas actuales del Banco Mundial su PPA2021; las correlaciones no se presentan como causalidad. Heritage2026 se identifica con sus fechas de observación, sin convertir índices económicos en juicios democráticos. Siguiente31–33: Política y Economía → Corrupción Sistémica.

## Continuidad editorial ·33/840 ·28/10/2026

Bloque31–33 publicado y comprobado en Política y Economía → Corrupción Sistémica, con etiquetas de tema/nivel y las específicas de los briefs. La fórmula de Klitgaard se trata como heurística. WGI2026 absoluta0–100 no se confunde con percentil; ENCIG2025 mantiene población urbana18+ y denominadores distintos. Odebrecht se limita al acuerdo corporativo2016 y contextualiza el superlativo del título; no se infieren condenas individuales ni sanciones cobradas. Se corrigieron tres enlaces internos antes de cerrar la verificación.

## Continuidad editorial ·36/840 ·28/10/2026

Bloque34–36publicado y verificado. LavaJato distingue fondos históricos MPF2017/panelSTF2025sin sumarlos y procesos de competencia/imparcialidad2021con alcance delimitado. Enriquecimiento ilícito diferencia InteramericanaIX/UNCAC20, artículo224mexicano y438bisespañol. Nepotismo utiliza2011como workingpaperhistórico y apellidos como indicador indirecto; selecciónabierta se propone sin efecto cuantificado inventado. Las normas españolas conservan ámbitos propios. Próximo37–39en preparación local, sin contar como completado.

## Continuidad editorial · 42/840 · 28/10/2026

Bloques 37–42 publicados y verificados, con 18 imágenes nuevas. Se mantuvo el área y la subcategoría del manifiesto. ENCIG distingue experiencia y desembolso; CICIG separa investigaciones de condenas; independencia judicial incorpora fuentes de 2026 y reformas mexicanas posteriores a 2024. Yukos diferencia resultados TEDH/arbitraje y recurso de 2025. Puertas giratorias respeta ámbitos y cambios de septiembre de 2026. ProZorro conserva límites del estudio original, sin presentar mejoras uniformes ni causalidad automática. Próximo bloque 43–45 iniciado; no hay cambio de arquitectura ni de autorización.

## Continuidad editorial · bloques43–48 · 28/10/2026

- Ejecutada la autorización continua existente: seis nuevas publicaciones completas y verificadas; total48/840. Corrupción Sistémica cierra15/15 y comienza Subsidios y Favoritismo Político3/15, conservando categorías del plan.
-49–51 preparadas con nueve imágenes propias, sin texto final ni publicación; la preparación no incrementa el total terminado.
- Criterios aplicados: canales y normas vigentes por país; rentas históricas≠pérdida social;FMI fiscal≠coste ambiental y distribución con muestra identificada. Fuentes y límites por expediente.
- Respaldo incremental43–48 comprobado. Sin nueva decisión requerida, cambio de infraestructura ni modificación de la autorización de producción.

## Producción 49–54 y continuación 55–57 · 28/10/2026

Se publicaron y verificaron dos bloques consecutivos, según la autorización de producción continua. Total: 54/840 y 162 imágenes; Subsidios y Favoritismo Político, 9/15. Categoría raíz y subcategoría explícitas, etiquetas del brief y tres adjuntos por ID comprobados. Blog es contenedor; Editorial es firma.

Las nueve imágenes de las 55–57 están guardadas, sin texto completo ni publicación. Reanudar investigación original, especialmente Graham/OSC, INDEC y multas a consultoras, y catálogo estadístico de la ONEI. El brief orienta la investigación y no demuestra sus afirmaciones. Copias SQL y Medios tras las 51 y 54 verificadas mediante hashes y miembros de archivo; sin nueva restauración completa. Sin cambios de DNS, correo, autenticación, tema o taxonomía.

## Producción 55–60 y continuación 61–63 · 28/10/2026

Publicados y verificados dos bloques consecutivos: total 60/840, con 180 imágenes originales. Subsidios y Favoritismo Político completa 15/15. Se mantuvieron categorías, etiquetas y slugs del plan; sin duplicados. Los cambios normativos de 2025 y 2026 y las diferencias entre previsión, dato y pago se documentaron por entrada.

Tanda 5 iniciada con nueve imágenes propias de E7.5.01–E7.5.03, inspeccionadas y guardadas con metadatos y fuentes iniciales. No hay textos completos ni borradores WordPress; las preparaciones siguen incluidas en pendientes. Reanudar lectura original antes de redactar. Respaldos consistentes de 55–57 y 58–60 con hashes y miembros comprobados; sin nueva prueba de restauración completa. La autorización continua sigue vigente; no se modificó infraestructura ni taxonomía.

## Producción 61–63 y continuación 64–66 · 28/10/2026

Publicadas y verificadas 61–63: total 63/840, con 189 imágenes originales. Agrupación explícita en Política y Economía → Monopolios Estatales vs. Competencia, sin duplicados. Se precisaron disputabilidad teórica, cronología comercial costarricense, unidades SUTEL y transición IFT/CRT mexicana. Textos, fuentes con alcances y originales conservados.

Continuación 64–66 con nueve WebP nuevos, revisados y optimizados, y fuentes iniciales. No hay texto final ni publicación de estas tres; faltan comprobaciones centrales documentadas. Respaldo SQL y Medios 61–63 verificado por hashes y miembros, sin nueva restauración completa. Sin cambios de infraestructura, tema o taxonomía. La producción continua autorizada sigue activa.

## Producción64–66 y continuación67–69 ·28/10/2026

Publicadas y verificadas64–66: total66/840,198 imágenes originales. Agrupación en Política y Economía → Monopolios Estatales vs. Competencia, sin duplicados. Se precisaron topes vinculantes, normas venezolanas y universos ENCOVI, y alcance de exclusividad ETECSA2025/recargas/tarifas frente a salario estatal civil2025. Fuentes y límites conservados por artículo.

67–69 tienen nueve imágenes originales optimizadas e inspeccionadas, alt/pies y fuentes iniciales; todavía sin textos completos ni publicación. Pendientes metodología/datosCNMC, TLC/VTC y sentencia/estudio farmacéutico. Respaldo64–66 comprobado por hashes y miembros, sin nueva restauración completa. Continúa autorización existente; sin cambios de infraestructura, tema o taxonomía.

## Producción 67–69 y continuación 70–72 · 28/10/2026

Publicadas y verificadas 67–69: total 69/840,207 imágenes originales. Organización exacta en Política y Economía → Monopolios Estatales vs. Competencia. Medidas de precios ferroviarios y fiabilidad separadas; texto LOTT frente a jurisprudencia y cestas de medallones diferenciados; fallo farmacéutico condicionado y evaluación CNMC 2026 con universos y límites.

70–72 iniciadas sin esperar otro mensaje, con nueve escenas originales optimizadas e inspeccionadas. Fuentes iniciales y pendientes centrales por ID; todavía no hay textos finales ni publicación. Respaldo 67–69 verificado por hashes y miembros, sin nueva restauración completa. Continúa autorización existente, sin cambios de infraestructura, tema o taxonomía.

## Producción 70–72 y continuación 73–75 · 28/10/2026

Publicadas y verificadas 70–72: 72/840, con 216 imágenes propias. Jerarquía y etiquetas del plan conservadas; una publicación y tres adjuntos por ID. Alcances de fuentes explícitos: resúmenes originales de Faccio, sin coeficientes no leídos; riesgos de contratación distintos de corrupción acreditada; tarifas aéreas comparables sin rebaja universal.

73–75 iniciadas directamente: nueve originales de image_gen optimizados e inspeccionados, briefs, metadatos y fuentes iniciales guardados. Faltan investigación y texto; no están publicadas. Respaldo VPS 70–72 verificado por hashes y miembros, sin nueva restauración completa. Sin cambios de arquitectura o taxonomía. La producción continua autorizada y la automatización siguen activas.

## Producción 73–75 y continuación 76–78 · 28/10/2026

Publicadas y verificadas 73–75: 75/840, con 225 imágenes propias. Monopolios Estatales vs. Competencia queda completa, 15/15; cinco tandas terminadas. CANTV se evalúa con datos por tecnología y periodo; Precios Cuidados distingue IPC de efecto causal; guía de denuncias actualiza CNA/ANC con fuentes oficiales y separa vías.

76–78 iniciadas directamente en Historia, Capitalismo Consciente. Nueve originales de image_gen optimizados e inspeccionados, briefs, metadatos y fuentes iniciales guardados. Faltan investigación central y textos. Respaldo VPS 73–75 verificado por hashes y miembros, sin nueva restauración completa. Sin cambios de arquitectura o taxonomía; automatización y autorización continua vigentes.

## Producción 76–78 y continuación 79–81 · 28/10/2026

78/840 verificadas y 234 imágenes públicas, directamente en Capitalismo Consciente / Historia (3/15), con las etiquetas del plan. Editorial no es una categoría. Los datos históricos conservan método y periodo; fuentes y revisión por ID.

Bloque 79–81 iniciado, con nueve WebP propios revisados, fuentes iniciales y pendientes precisos; todavía sin textos finales. Respaldo SQL y medios 76–78 verificado; sin nueva restauración completa. Para 81 se consultó la fuente primaria BM2026 sobre política industrial, evitando presentar el informe de 1993 como postura inmutable. Sin cambios de arquitectura o taxonomía; autorización y automatización continuas vigentes.

## Producción 79–84 y continuación 85–87 · 28/10/2026

Dos bloques consecutivos completados sin pedir confirmación: 84/840 y 252 imágenes públicas. Historia queda en 9/15; jerarquía y etiquetas exactas. WordPress sincronizado después de cada publicación, verificación pública y antiduplicados cerrados.

85–87 iniciadas con nueve imágenes propias terminadas e inspeccionadas, briefs, metadatos y pendientes por ID. Fuentes y textos sin completar: no cuentan como terminadas. CASEN2024 incorpora nueva metodología; comparar solo series coherentes. Respaldo VPS de ambos incrementos verificado por hashes/miembros, sin nueva restauración completa. Sin cambios de arquitectura, taxonomía o infraestructura; autorización y automatización continuas vigentes.
