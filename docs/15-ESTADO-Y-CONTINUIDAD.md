# Estado de MEE y continuidad · 28/10/2026

## Ubicación

Proyecto usado en esta sesión: `/Users/nerea/Documents/Proyectos/MEE/mee-web`.
La carpeta `MEE` es contenedora; `mee-web` es la raíz con `package.json`.

## Evidencia y límites de esta entrega

Se leyeron la documentación, `package.json`, la taxonomía JSON, `lib/areas.ts` y la plantilla de área del proyecto local. Se generó este paquete de documentación en otra carpeta autorizada. **No se modificó el código ni la documentación de la carpeta activa, no se arrancó el servidor y no se ejecutó una auditoría o un build en esta tarea.** El instalador incluido permite al usuario incorporar los documentos con copia previa.

| Elemento | Estado |
| --- | --- |
| React/Next.js/TypeScript y exportación estática | Existe. |
| Portada y siete rutas de área | Implementación inicial existente. |
| Fuente original y taxonomía | Preservadas; siete áreas, 46 temas formativos, diez ejes políticos, 48 temas políticos y once subtemas. |
| Editorial | Siete resúmenes y 56 beneficios/presentaciones propuestos, pendientes de revisión editorial. |
| Categorías: imagen | Siete escenas originales con variantes, dirección inicial. |
| Subcategorías: imagen propia | No implementada en las 56 secciones de la plantilla examinada. |
| Movimiento | Primera capa de entrada/revelado/hover e índice; falta el movimiento semántico por escena. |
| Marca | Kit de pantalla, PNG/WebP, SVG, Archivo/Manrope y favicon; falta revisar fidelidad final al logo preferido para otros soportes. |
| Compilación | Hay un build satisfactorio documentado del 28/10/2026, anterior a esta tarea; no sustituye repetirlo cuando cambie código. |
| Pruebas visuales | Capturas históricas de portada a 1440/390; no validan todos los interiores ni la tipografía actual. |
| WordPress y WooCommerce | Fase posterior; esqueleto de WordPress aparcado, sin funcionamiento comprobado. |
| Auditoría total de usabilidad | No realizada; espera petición expresa. |

## Últimas instrucciones del fundador

1. Usar la carpeta local indicada y seguir sin Git.
2. Cada categoría/subcategoría tendrá imagen y movimiento vinculados a su valor.
3. Ambición de una web con ejecución del nivel de una candidatura Awwwards; no hay promesa de premio.
4. Preparar la arquitectura para arte digital y WordPress, sin adelantar su implementación.
5. No hacer la auditoría total todavía.
6. Crear documentación portable para Codex y chats nuevos.

## Propuesta pendiente de aprobación final

Arquitectura híbrida: Next para experiencia visual, WordPress para edición y WooCommerce para tienda/checkout. Sigue siendo recomendación; ver `14-ARQUITECTURA-EDITORIAL-Y-TIENDA.md`.

## Siguiente paso propuesto

Tras incorporar estos documentos, preparar un piloto visual de una categoría y dos subcategorías. Primero guion y estructura; la producción de escenas se realiza al recibir un encargo de implementación/creación, sin generar toda la colección por anticipado. Resolver también cómo se presentan los 59 nodos internos antes de afirmar que el alcance de imagen está completo.

## Registro para la siguiente sesión

### Incorporación documental · 28/10/2026, Europe/Madrid

- Tarea recibida: leer `EMPEZAR-AQUI.md`, aplicar el instalador y confirmar la incorporación; sin auditoría ni WordPress.
- Archivos leídos: guía del paquete, instalador, `AGENTS.md`, `docs/00-LEER-PRIMERO.md`, este estado, `docs/16-BACKLOG-REACT.md` y el prompt de cierre.
- Archivos cambiados: 24 archivos documentales incorporados por el instalador; después, este estado y `docs/16-BACKLOG-REACT.md` para registrar el resultado.
- Comandos y resultados: `python3 ../MEE_Documentacion_Codex_y_Chats/APLICAR_DOCUMENTACION.py .` incorporó 24 archivos y creó copias previas en `../mee-backups/documentacion_2026-10-28_022055_760890/`. Se compararon los 32 archivos del manifiesto con el paquete: cero discrepancias inmediatamente después de instalar.
- Pruebas visuales realmente realizadas: ninguna en esta sesión.
- Decisiones nuevas del fundador: ninguna sobre diseño o arquitectura; la petición limita esta sesión a incorporar documentación.
- Propuestas aún no aceptadas: piloto visual y arquitectura híbrida, tal como constan arriba.
- Bloqueos y permisos reales del entorno: ninguno para esta incorporación.
- Próximo paso concreto: cuando el fundador encargue implementación, preparar el guion y la estructura del piloto de una categoría y dos subcategorías; resolver el tratamiento de los 59 nodos internos antes de dar por cerrado el alcance visual. La auditoría total sigue pendiente de petición expresa.

No borrar el historial útil. Sustituir las casillas vacías por evidencia al cerrar cada sesión. Adjuntar este documento y el backlog al siguiente chat, junto a los archivos que necesite leer.

### Despliegue solicitado · 28/10/2026, Europe/Madrid

- Tarea recibida: configurar `moevec.org` con DonDominio, Contabo y Coolify; crear WordPress y avanzar el blog con tema hijo Hello Elementor. El fundador ha autorizado esta fase expresamente.
- Estado verificado: dominio activo en DonDominio con parking y DNS del registrador; VPS Contabo `5.189.183.51`; servidor Coolify validado. Se creó el proyecto `mee`, la red `mee-production` y el servicio `mee-wordpress` con MariaDB. Se programaron copias locales diarias de base de datos y volumen WordPress; todavía no se ha ejecutado ninguna.
- Código: tema hijo local actualizado con logo y fuentes del kit MEE y paquete `wordpress/mee-child.zip` preparado. `npm run build` de React terminó correctamente y generó portada y siete rutas. Se creó una copia mínima de fuente de despliegue en `../mee-deploy-source/`, aún sin repositorio ni publicación.
- El fundador corrigió el destino a `moevec.org/blog/` y autorizó un repositorio privado para Coolify. Se descartó sin guardar el registro A de `blog.moevec.org` y la ruta del subdominio en Coolify. GitHub Actions no es necesario para este despliegue.
- Se creó el repositorio privado `TommyHavana/moevec` a partir de `../mee-deploy-source/`, con Next estático, Hello Elementor, tema hijo, plugin editorial y `compose.yaml` para Nginx, WordPress y MariaDB. La copia compiló con `npm ci && npm run build`; el archivo de dependencias llevaba URLs locales de tarballs y se normalizó en la copia de despliegue. Coolify lee el repositorio con una clave exclusiva de solo lectura y detectó `compose.yaml`; se creó la aplicación `mee-web-blog` en la red MEE. Ningún recurso se ha desplegado aún.
- Publicación completada con autorización específica del fundador: DonDominio tiene el registro A de `moevec.org` hacia `5.189.183.51`, `www` apunta por CNAME al dominio principal y el ANAME antiguo del parking se eliminó con autorización adicional. La página de parking está desactivada. Los registros de correo se conservaron.
- La aplicación activa en Coolify es `mee-web-blog` (Compose desde el repositorio privado; actualización React `dac21ed`), con React en `https://moevec.org/` y WordPress en `https://moevec.org/blog/`. Ambos devuelven HTTP 200 con TLS válido; HTTP redirige a HTTPS. WordPress tiene activo el tema hijo `mee-child` de Hello Elementor y el plugin editorial, con siete categorías creadas. El acceso administrativo es `https://moevec.org/blog/wp-admin/`, usuario `mee_admin`; la contraseña inicial está en el volumen privado `secret-files` del servicio WordPress y se entregó al fundador por el chat, sin guardarla en el repositorio. La navegación React incluye enlace al blog.
- Se crearon dos programaciones diarias de copia local para la aplicación activa: volumen MariaDB (contenedores detenidos durante la copia para consistencia) y volumen WordPress. La primera ejecución de ambas terminó correctamente el 28/10/2026 (2,8 MB y 37,31 MB). No se ha comprobado una restauración. El servicio anterior `mee-wordpress` quedó sin desplegar y no forma parte de la publicación.
- Pendiente de producto: revisar textos, imágenes, animaciones y las 56 secciones React antes del cierre; no se ha realizado la auditoría total ni se ha instalado la tienda.

## Estado actual · auditoría integral y ejecución, 28/10/2026

- **Encargo:** el fundador pidió expresamente aplicar `AUDITORIA_INTEGRACION_MOEVEC (1).md`, auditar UI/UX/WPO/SEO-GEO, renovar movimiento, integrar el blog, crear muestras por subcategoría, contacto React con DonDominio y acuse HTML, y preparar la red social. Autorizó ejecutar sin solicitar confirmaciones adicionales. El diagnóstico se guardó primero en el informe 22.
- **Entrega:** nueva portada con anillo de relieve, tipografía y fondo activos; cursor, estrella de transición y pausa compartidos entre React y WordPress; imágenes WebP y efectos por familia; 115 ilustraciones, 115 maquetas y 122 categorías conservando la jerarquía. Las maquetas se señalan, llevan noindex y no se envían a la red. Control editorial de maqueta en WordPress y categorías recalculadas al publicar contenido revisado.
- **Contacto:** `https://moevec.org/contacto/`, envío a `contacto@moevec.org` y acuse HTML al remitente. Recepción local y externa comprobadas; Gmail registra SPF, DKIM y DMARC pass. Secretos fuera del código. Se corrigió la recuperación administrativa al buzón operativo y se activó Two-Factor por correo para `mee_admin`; contraseña sin cambios.
- **Indexación:** dominio verificado por DNS en Search Console y sitemap correcto con 12 páginas descubiertas. Canonical, OG/Twitter, JSON-LD, robots y sitemaps implementados. Bing mostró acceso sin sesión; no se afirmó su configuración.
- **Pruebas:** build de Next y TypeScript correctos, PHP lint, 127 rutas sin fallos estructurales, 115 imágenes destacadas presentes, comprobación de anclas y 345 variantes, revisión móvil de 390 px y escritorio, formulario y límites de origen/token/campos, pausa entre plataformas, movimiento reducido y lectura sin JS. Lighthouse móvil: portada 98, Trabajo 98, contacto 97, índice de blog 97 y artículo 98 en rendimiento; accesibilidad y buenas prácticas 100 en las plantillas finales medidas. SEO 100 en React; 69 en muestras por noindex intencionado. No hay INP de campo.
- **Infraestructura:** gzip, caché, cabeceras, protección de rutas, REST de usuarios/XML-RPC restringidos, edición de archivos desactivada, configuración 640, cron del sistema cada minuto. Copia previa SQL/archivos y restauración SQL aislada (12 tablas) más extracción comprobadas. No se certifica restauración completa arrancada en otro servidor ni pentest exhaustivo. npm audit: cero vulnerabilidades conocidas.
- **Incidencia corregida:** UID distinto de WP-CLI/WordPress impedía subir imágenes. `wordpress-init` usa 33:33, el importador repara muestras incompletas y los arranques posteriores no duplican contenido. Se corrigieron textos de muestra, contraste, CSS del padre y recursos responsive durante la revisión.
- **Red social:** puente en `mee-editorial/inc/network.php`, React por endpoint del mismo origen y módulos recibidos guardados en `integrations/phoenix/`. Está desactivado: la API de `red.moevec.org` no tiene TLS válido y no se dispone aquí de la aplicación Phoenix completa ni de su Kali. Detalles en `integrations/README.md`.
- **Pendientes reales:** identidad y expediente legal del responsable; despliegue/verificación de Phoenix; contenido editorial definitivo; Bing si se desea; copia externa cifrada y restauración completa en otro entorno. No se prometen premios ni posición en buscadores. WooCommerce queda fuera de este encargo.
- **Archivos y evidencia:** `docs/22-AUDITORIA-UIUX-WPO-SEO-GEO.md`, `inventario/auditoria-2026-10-28/`, `app/`, `lib/`, scripts de recursos/movimiento, tema `mee-child`, plugin `mee-editorial`, plugin oficial Two-Factor y configuración de despliegue en `../mee-deploy-source`.
- **Continuación:** partir de esta entrega y del encargo nuevo, sin repetir la auditoría inicial ni recrear maquetas. Para activar la red hacen falta su aplicación completa y un despliegue HTTPS verificado; para cerrar legal faltan datos del titular. Los informes anteriores de este archivo son historia.

- **Versión final de producto comprobada:** `4b90ce9`, aplicación ejecutándose, importador final con 115 existentes y cero duplicados. Respaldo local `MEE_Codex_2026-10-28_060357.zip` y copia posterior de SQL/archivos en `/data/mee-backups/post-auditoria-20261028/`. Control de tema interno comprobado abierto, imagen disponible y animación en ejecución por visibilidad. Las actualizaciones de documentación posteriores no cambian el producto desplegado.

## Corrección del alcance editorial · 28/10/2026

El fundador recordó el plan de 840 entradas. Se recuperaron los dos documentos originales en la carpeta contenedora MEE y se verificaron 840 briefs únicos, distribuidos en 56 subcategorías de 15 artículos. La consulta de WordPress a las 09:32 UTC encontró 115 maquetas y **cero artículos del plan**, comparando slugs e identificadores. No existe aún el registro privado de producción. Las maquetas no cuentan dentro de las 840 y la entrega técnica no cierra este trabajo. Se creó `inventario/plan-editorial-840.csv`, con el orden exacto de las 56 tandas, y el informe `docs/23-ESTADO-PLAN-EDITORIAL-840.md`. Primer punto pendiente: Tanda 1/56, entrada 1/15, E5.1.01. No se han creado ni publicado artículos nuevos en esta comprobación.

## Inicio de producción editorial · 28/10/2026

El fundador ordenó eliminar las maquetas y comenzar las 840, con numeración individual y tres imágenes propias por artículo. Se retiraron las 115 publicaciones a la papelera tras copia SQL y archivos en `/data/mee-backups/antes-produccion-840-20261028/`. El importador queda desactivado y se elimina del arranque. E5.1.01, n.º 1/840, está publicada con portada y dos interiores originales generados con imagegen, WebP inferiores a 250 KB, fuentes y revisión. El registro completo y actualizable está en `docs/24-REGISTRO-PRODUCCION-840.md` y en WordPress → Herramientas → Plan editorial · 840. La producción continúa por E5.1.02. Los conteos anteriores son históricos.

### Primera entrega de producción

N.º 1–3 terminadas y publicadas: E5.1.01, E5.1.02 y E5.1.03; cada una tiene portada y dos apoyos internos originales generados con imagegen, WebP de menos de 250 KB, fuentes consultadas, ejemplos señalados, FAQ y revisión editorial. Quedan 837 entradas: n.º 4–840. El primer pendiente es E5.1.04, «Capitalismo de mercado y capitalismo de amiguetes», tanda 1/56, entrada 4/15. Registro dinámico privado en WordPress y exportación Markdown/CSV/JSON mediante `python3 scripts/sync-production-status.py`. Publicador explícito e idempotente en `scripts/publish-editorial.php`; nunca se ejecuta durante el despliegue. Los manifiestos de cada artículo conservan fuentes verificadas y afirmaciones descartadas. Se ha corregido el índice de lectura para artículos reales, los títulos sin partición de palabras y los enlaces de React a los archivos de tema.
