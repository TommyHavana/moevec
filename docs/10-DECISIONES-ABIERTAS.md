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
