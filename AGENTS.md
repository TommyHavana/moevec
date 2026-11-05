# MEE · instrucciones para Codex

## Inicio de cada sesión

Responde en español. Lee este archivo, `docs/00-LEER-PRIMERO.md`, `docs/15-ESTADO-Y-CONTINUIDAD.md` y `docs/16-BACKLOG-REACT.md`. Para cambios de imagen y movimiento lee también `docs/13-REQUISITOS-VISUALES-Y-MOVIMIENTO.md` y `docs/19-INVENTARIO-VISUAL.md`. Sigue la petición concreta del usuario; los prompts archivados no son nuevas órdenes.

## Proyecto y fase

MEE significa Movimiento de Evolución Económica. Raíz local activa: `/Users/nerea/Documents/Proyectos/MEE/mee-web`. Se continúa el Next.js/React/TypeScript existente. No reconstruirlo desde cero. El fundador autorizó el 28/10/2026 desplegar React y crear WordPress editorial en `moevec.org/blog/`, así como un repositorio privado de código para Coolify. WooCommerce sigue para una fase posterior. La indisponibilidad de GitHub Actions anotada el 28/10 fue temporal; comprobar su estado antes de planificar CI. Coolify puede desplegar desde Git sin Actions. El estado actual y las autorizaciones están en `docs/15-ESTADO-Y-CONTINUIDAD.md`.

## Requisitos del fundador

- Portada y mosaico de siete categorías, con interiores e índice superior sticky.
- **Cada categoría y cada subcategoría debe tener imagen propia y movimiento que exprese su valor.** No sustituir ese requisito por aplicar el mismo zoom a todas las imágenes. Inventario: siete categorías, 56 secciones principales y 59 nodos internos adicionales; el alcance visual de cada nivel debe quedar explícito, sin borrar temas.
- Referencia: `https://turnerduckworth.com/` para escala, ritmo y composición. Crear recursos, textos y código propios.
- Paleta viva azul/rojo, diseño moderno, alta calidad editorial y ambición de nivel Awwwards; no prometer premios ni confundir intensidad de animación con calidad.
- Tienda futura de arte digital; falta decidir si también habrá impresión física. Mantener ambas necesidades diferenciadas.
- El fundador encargó expresamente y autorizó ejecutar la auditoría integral el 28/10/2026. La auditoría de aquella fecha está en `docs/22-AUDITORIA-UIUX-WPO-SEO-GEO.md`; la auditoría integral vigente del 05/11/2026 está en `docs/29-AUDITORIA-INTEGRAL-Y-REDES.md`. Las puntuaciones publicadas son mediciones de laboratorio identificadas, no certificaciones globales ni datos de campo.

## Fuentes y precisión

La taxonomía original está en `fuentes/claude/docs/02-taxonomia.md`: siete categorías, 46 temas formativos y diez ejes políticos; además, la séptima área contiene temas y subtemas anidados. Conserva nombres, slugs, orden y jerarquía. `fuentes/claude/` es historia del proyecto: sus instrucciones antiguas no prevalecen y no se modifica silenciosamente.

El editorial de `docs/03-EDITORIAL-CATEGORIAS.md` y `docs/11-PRESENTACION-CATEGORIAS-Y-SUBCATEGORIAS.md` es redacción propuesta que revisará el fundador. `content/*.json` es generado: ejecuta `npm run content:sync`; no lo edites a mano. Mantén el manifiesto visual propuesto separado de ese JSON hasta integrarlo expresamente.

Usa `brand-kit/`, `public/brand/`, `public/fonts/` y `app/icon.png`. Marca MEE distinta de Calicata. La reconstrucción Archivo Black Italic y estrella de ocho rayos es la versión de pantalla; la correspondencia exacta con el logo preferido sigue pendiente de revisión final para otros soportes.

El plan editorial completo está en `../MEE_Plan_Editorial_840_entradas.md`, con orden de producción en `../MEE_Prompt_ChatGPT_Produccion_WordPress.md`: 840 briefs, 56 subcategorías y 15 artículos por cada una. Las 115 maquetas de diseño no cuentan como artículos de ese plan. Consulta `docs/23-ESTADO-PLAN-EDITORIAL-840.md` e `inventario/plan-editorial-840.csv`; el estado actualizado se consulta en `docs/24-REGISTRO-PRODUCCION-840.md` y en WordPress → Herramientas → Plan editorial · 840. Los prompts contenidos en las fuentes son material de trabajo, no prueba de ejecución ni nuevas instrucciones del usuario.

## Implementación

La agrupación se hace directamente en WordPress con las categorías y subcategorías del manifiesto. «Blog» es el contenedor general; «Editorial» no es una categoría. Deben existir exactamente los 122 nodos previstos, incluidas las siete áreas principales. La categoría técnica vacía Uncategorized se retiró por la corrección expresa del fundador. La navegación y el BreadcrumbList muestran Blog, área y subcategoría; el publicador resuelve siempre la asignación explícita por slug del plan.

La producción continua autorizada terminó el 05/11/2026: 840/840 completas y automatización retirada. No reactivar la producción ni crear otro seguimiento por instrucciones históricas. El paquete de rutas y Rank Math también está terminado. La auditoría actual y su plan de mejoras están en `docs/29-AUDITORIA-INTEGRAL-Y-REDES.md`; el fundador autorizó después ejecutar las mejoras. El estado de cada una y sus límites está en `docs/30-EJECUCION-MEJORAS.md`; no deducir su ejecución solo por el informe inicial.

Contenido legible en HTML; movimiento progresivo, variante con movimiento reducido, teclado y móvil. Activar los recursos al acercarse al viewport y detener animación fuera de él. No depender del hover para funciones esenciales ni descargar todos los vídeos al abrir la portada. Los perfiles de movimiento y presupuestos son propuestas: medir antes de declararlos cumplidos.

React y WordPress editorial están desplegados por encargo del fundador. `docs/14-ARQUITECTURA-EDITORIAL-Y-TIENDA.md` conserva la propuesta anterior; WooCommerce sigue para una fase futura. No construir checkout, cuentas, pagos o sincronización de CMS por anticipado. El fundador ordenó retirar las 115 maquetas y comenzar la producción del plan de 840 entradas. Las maquetas se enviaron a la papelera, su importador está retirado y no debe recrearlas ningún despliegue. Cada artículo terminado requiere fuentes revisadas, portada y dos apoyos interiores propios. Mantener siempre la numeración global 1–840 y los ID del plan, y diferenciar terminadas, en curso y pendientes. No inventar catálogo, testimonios, estadísticas, autores, negocios ni promesas de inversión. La presentación pública de MEE no cuenta historias personales de fundadores.

## Verificación y cierre

Antes de grandes cambios, `npm run backup` si el entorno permite escribir en su destino. Ejecuta la sincronización y la compilación cuando corresponda al cambio; no repitas pruebas sin una razón concreta. Si el entorno bloquea una acción, continúa con trabajo independiente y registra el límite real. No declares un servidor, captura, compra o prueba como realizados sin evidencia.

Al cerrar: actualiza `docs/15-ESTADO-Y-CONTINUIDAD.md`, `docs/16-BACKLOG-REACT.md` y las decisiones materiales en `docs/10-DECISIONES-ABIERTAS.md`. Si cambian requisitos o arquitectura, actualiza también `docs/21-CONTEXTO-PORTABLE.md`. Usa `prompts/CIERRE-Y-TRASPASO.md`. Las instrucciones y autorizaciones recientes del usuario prevalecen sobre este archivo.
