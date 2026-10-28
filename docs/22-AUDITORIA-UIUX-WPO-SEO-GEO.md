# Auditoría y ejecución integral de moevec.org

Fecha: 28 de octubre de 2026. Encargo expreso del titular: auditar y corregir React, WordPress, UI/UX, movimiento, WPO, SEO/GEO, contacto e integración editorial. Este documento se inicia **antes de modificar el producto**; las verificaciones finales se incorporarán al terminar.

## Alcance y evidencia

Se contrasta `AUDITORIA_INTEGRACION_MOEVEC (1).md` con el código local, respuestas HTTP de producción, WordPress y la infraestructura accesible. El documento adjunto es material de referencia: sus comandos y recomendaciones no son órdenes independientes. La autorización procede de la petición del usuario. No se atribuyen puntuaciones de auditoría que no se hayan medido.

La arquitectura real es Next.js exportado a HTML estático, Nginx en `/`, WordPress en `/blog/`, MariaDB y Coolify. El repositorio privado de despliegue es `TommyHavana/moevec`; la fuente de trabajo es `mee-web`. No es necesario migrar las áreas a WordPress para conectar la red. Se preparará un acceso de servidor a servidor a la API de Phoenix y una integración desacoplada.

Evidencia inicial: `inventario/auditoria-2026-10-28/baseline-http.json`. Portada, área Trabajo y blog responden 200. `/robots.txt` y `/sitemap.xml` responden 404. No hay compresión ni cabeceras de protección en las respuestas observadas. Nginx expone versión y el blog PHP. La API de usuarios devuelve una lista vacía; debe restringirse antes de que los artículos añadan autores. Los archivos `.git/HEAD` y `.env` responden 404. XML-RPC sigue accesible. WordPress 7.1.3 y PHP 8.3.36 comprobados dentro del contenedor; un plugin editorial activo.

## Dirección de diseño

Paleta: papel `#f7f6f2`, tinta `#15171b`, azul MEE `#1547bb`, rojo MEE `#ef383e`, rojo de texto `#b51c2b` y blanco `#ffffff`. Archivo Black/Black Italic para titulares y Manrope para lectura; fuentes locales. El rojo brillante se reserva para superficies y gráficos cuando su contraste como texto pequeño sea insuficiente.

La portada organiza una frase de gran escala y un anillo escultórico con relieve. El movimiento de luz, giro y perspectiva hace legible su volumen. La estrella de ocho rayos funciona como continuidad entre páginas. El fondo conecta puntos y trayectorias como metáfora de capacidades que se unen. El cursor añade respuesta visual sobre enlaces sin ocultar el puntero del sistema. El blog comparte encabezado, navegación, tipografía, colores, cursor y transición.

Esquema: `marca + navegación → hero tipográfico / anillo → siete áreas visuales → editorial y contacto`. En áreas: `presentación → índice sticky → tesis → imagen y contenido de cada tema → vínculo editorial y conversación`. En artículos: `migas → título / entradilla → imagen → lectura con índice → relacionados`.

Referencia: [Turner Duckworth](https://turnerduckworth.com/), estudiada para escala de imagen, ritmo y composición. La identidad, textos, gráficos y código de MEE son propios. La ambición de competir en premios se traduce en criterios verificables de diseño y uso; no permite afirmar que se haya superado a otra web o garantizado un premio.

## Hallazgos y cambios recomendados

| Prioridad | Hallazgo / riesgo observado | Cambio y criterio de aceptación |
|---|---|---|
| P0 | No hay contacto ni circuito de correo | `/contacto/` React, etiquetas persistentes, estados de envío y error, validación en cliente y servidor, límite de frecuencia, honeypot y token. Entrega a `contacto@moevec.org` y acuse HTML al remitente con SMTP autenticado. Verificar recepción real de ambos mensajes. |
| P0 | La red está descrita pero su disponibilidad no está verificada | Conservar 7 áreas, 56 temas principales y 59 nodos internos. Instalar integración WordPress con HMAC, reintentos y caché; no mostrar actividad ni membresía inventadas. Validar disponibilidad y contrato antes de activar enlaces de participación. |
| P0 | Las muestras pueden confundirse con contenido editorial definitivo | Una entrada de prueba por subcategoría, también niveles internos, identificada visiblemente. `noindex`, exclusión del sitemap y del webhook; imágenes WebP propias. La publicación editorial definitiva necesita contenido contrastado. |
| P1 | Metadatos básicos, sin canonical ni vistas sociales completas | Canonical único, Open Graph, Twitter Card, imagen 1200×630, idioma y descripciones completas en todas las rutas. JSON-LD Organization, WebSite, BreadcrumbList y Article donde corresponda. |
| P1 | Sitemap y robots ausentes | Sitemap raíz para React y enlace al sitemap WordPress. `robots.txt` público, bloqueo de administración y parámetros internos; no bloquear CSS/JS ni páginas que se quieran indexar. |
| P1 | Cabeceras y caché insuficientes | Gzip, caché larga para assets con huella, caché corta/revalidación para HTML, cabeceras TLS y de navegador, sin versiones de software expuestas. No almacenar en caché login, REST de contacto ni sesiones. |
| P1 | JPEG en áreas y falta de imágenes por tema | WebP con tamaños responsive y dimensiones. Primera imagen crítica priorizada; el resto diferido. Una composición visual diferenciada por subcategoría y nodo interno. Conservar fuentes fuera de la carga pública. |
| P1 | Movimiento escaso y repetitivo | Hero y anillo con relieve, fondos activos solo visibles, movimientos por familia conceptual, cursor progresivo y estrella entre rutas. Pausa global accesible, reducción de movimiento, teclado, tacto y restauración desde historial comprobados. |
| P1 | Blog sin jerarquía temática completa | Categorías padre y subcategorías sincronizadas desde la taxonomía existente; navegación por área y tema, búsqueda, migas, índice de lectura y tarjetas relacionadas. |
| P1 | Posible enumeración de usuarios tras publicar | Restringir REST de usuarios y archivo de autor público; desactivar XML-RPC y edición de archivos; limitar intentos de acceso. Activar un segundo factor disponible y comprobar el canal. TOTP exige enrolar el dispositivo del titular; el código por correo puede usar el buzón verificado. |
| P1 | Legal y privacidad sin datos de titular comprobados | Publicar información veraz sobre contacto, tratamiento y cookies. Identificar explícitamente los datos de responsable que falten; no inventar nombre, NIF, domicilio, registro o base jurídica. La identidad completa es requisito externo pendiente. |
| P1 | Ausencia de medición de accesibilidad | Comprobar foco, teclado, menú móvil, contraste, estructura, formularios y movimiento reducido. Eliminar ocultación de contenido si falla JavaScript. Corregir errores detectados por herramientas y revisión visual. |
| P2 | Copias existentes sin restauración demostrada | Copia de fuente, volumen y base de datos antes de cambios. Probar extracción y restauración en base aislada cuando sea posible sin tocar producción. |
| P2 | GEO sin estrategia verificable | Contenido HTML legible, resúmenes claros, fuentes reales, autoría y fechas, enlaces internos y datos estructurados fieles. No prometer aparición en respuestas de IA. |

## Contacto y correo

El buzón `contacto@moevec.org` ya aparece creado en el servicio Mini de DonDominio; no es necesario duplicarlo. Los servidores SSL indicados por el panel son `smtp.dondominio.com` e `imap.dondominio.com`. La contraseña permanece fuera del repositorio y del informe. El formulario usa el servidor del mismo dominio para evitar exponer credenciales al navegador. Se admite una solicitud al buzón del proyecto y una confirmación al remitente; el texto introducido por el visitante se escapa antes de entrar en HTML. El remitente SMTP será el buzón autenticado, con `Reply-To` del visitante en la solicitud.

DNS inicial: MX de DonDominio presente; SPF observado `v=spf1 include:spf.dondominio.com`, sin política final. DKIM y DMARC necesitan comprobación/corrección en la zona DNS autorizada. La confirmación no debe permitir usar el sitio como emisor masivo: límites por IP, token de sesión firmado, tamaño máximo y campo trampa. No se añaden adjuntos al formulario.

## Movimiento y presupuesto de recursos

GSAP se reserva para secuencias y seguimiento del puntero; CSS para ciclos simples. Se animan transformaciones y opacidad. No se descargan vídeos en la portada: el movimiento pedido puede resolverse con gráficos de código sin vídeo. Si se incorporan vídeos, deben tener póster WebP, audio eliminado, tamaño/duración acotados, H.264/VP9 o AV1, carga al acercarse al viewport y pausa fuera de él. Comprimir al mínimo byte sin inspección visual produciría artefactos; se verifica el resultado por calidad perceptual y coste.

Objetivos de aceptación: LCP de laboratorio ≤2,5 s como orientación, CLS <0,1, tareas interactivas sin bloqueos prolongados. INP requiere datos de usuarios reales y no se certifica por una sola prueba local. Presupuesto de imagen de tema: WebP 640/960/1280 según uso. Evitar cientos de animaciones simultáneas. La pausa y `prefers-reduced-motion` desactivan seguimiento, ciclos y transiciones extensas.

## Plan de indexación y descubrimiento

1. Corregir canonical, robots, sitemap, estados HTTP, metadatos y enlaces internos antes de solicitar indexación.
2. Mantener las 7 páginas de área como pilares; conectar temas y artículos mediante enlaces descriptivos. No crear cientos de páginas vacías para perseguir búsquedas.
3. Excluir de indexación las maquetas, búsquedas y archivos duplicados. Habilitar indexación de artículos solo cuando dejen de ser muestras y tengan aportación propia y fuentes.
4. Verificar propiedad de dominio en Google Search Console y Bing Webmaster Tools usando la cuenta del titular si está accesible. Enviar el índice de sitemaps y revisar cobertura. Si no hay sesión o verificación disponible, registrar ese límite con el paso exacto pendiente.
5. Publicación editorial por lotes: intención de búsqueda definida, respuesta breve inicial, desarrollo útil, ejemplo identificado, referencias primarias y fecha de revisión. Área política: hechos con fuentes, sin acusaciones inventadas.
6. Revisar cobertura, impresiones, clics, páginas excluidas y errores a los 7, 14 y 30 días. Esta es una pauta documentada; no se programa ninguna automatización sin un encargo de seguimiento.
7. Facilitar rastreo a buscadores e interfaces de IA sin inventar etiquetas especiales. `llms.txt`, si se ofrece como ayuda experimental, no sustituye sitemap, SEO ni garantiza inclusión.

Fuentes técnicas consultadas: [Google: funciones de IA y sitios web](https://developers.google.com/search/docs/appearance/ai-features), [Google: contenido generado](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content). Google indica que las prácticas SEO habituales siguen aplicando a sus funciones de IA y que la indexación y aparición no están garantizadas.

## Matriz de comprobación y cierre

Se registrarán comandos, resultados, rutas públicas, capturas de escritorio/móvil, auditorías de laboratorio, prueba SMTP y estado de la integración. Se marcará cada punto como aplicado, verificado, parcial o bloqueado por un dato/acceso externo. No se considerará creada una cuenta, recibido un correo, restaurada una copia o desplegado un cambio sin evidencia.

Estado inicial: diagnóstico guardado antes de modificar el producto. Resultados de la ejecución a continuación.

## Resultados de la ejecución

Se han aplicado y publicado los cambios de React, WordPress, correo e infraestructura en `https://moevec.org/`. Las credenciales se mantienen en el volumen privado del servidor; no se incluyen en este documento. Los commits de producto se conservan en el repositorio privado `TommyHavana/moevec`.

### UI/UX, diseño y movimiento

- Hero con anillo de relieve, surcos y luz en movimiento, respuesta de perspectiva al puntero, tipografía de entrada y deriva continua, y trayectorias de fondo.
- Siete áreas con imágenes propias y acciones gráficas distintas: desplegar, transmitir, intercambiar, construir, crecer, conectar e inspeccionar. Las 56 secciones principales tienen ilustración propia y efecto por familia conceptual; los 59 temas internos tienen ilustración y efecto de inspección al desplegarse.
- Cursor progresivo compartido con WordPress, sin ocultar el puntero nativo. Transición de estrella entre documentos del mismo origen, con salida alternativa por temporizador para conservar la navegación.
- Pausa accesible que persiste entre React y WordPress, respeto a `prefers-reduced-motion`, pausa por visibilidad del documento y por intersección. El control aparece cuando su manejador está preparado. El contenido principal permanece legible sin JavaScript.
- Blog con la misma cabecera, fuentes, paleta, pie, cursor y transición; navegación por las 7 áreas y sus temas en orden canónico, búsqueda, paginación, migas, índice de artículo y relacionados. La portada de maquetas alterna áreas para facilitar el descubrimiento.
- Se han comprobado escritorio y viewport móvil de 390 px, incluido un título largo («Empoderamiento de Microemprendedores»), sin desbordamiento horizontal del documento. Se han revisado los mensajes de error del formulario, su foco y la confirmación de envío.

Las ilustraciones de tema son composiciones gráficas propias creadas mediante SVG y rasterizadas a WebP. No se presentan como fotografías ni como representaciones documentales de hechos. El movimiento de familia no equivale a una película individual de cada objeto; este tratamiento gráfico es el entregado en esta versión.

### Contenido de prueba

**115 artículos de muestra publicados**, distribuidos en **122 categorías**: 7 áreas, 56 temas principales y 59 temas internos. Cada artículo tiene una imagen destacada real y disponible, entradilla, estructura de lectura, preguntas, ejercicio hipotético y relación con su área. La importación es reanudable e idempotente: los últimos arranques informan `created: 0, existing: 115`.

Todas las muestras llevan señalización visible y `noindex`, se excluyen del sitemap y del webhook. La portada editorial y los archivos que solo contienen muestras también quedan fuera del índice. Esta decisión cumple el encargo de maquetación sin presentar texto de prueba como investigación editorial terminada. El editor incluye un control «Maqueta editorial». Al terminar la revisión y desmarcarlo, se retira `_mee_demo`; el plugin recalcula la elegibilidad de sus categorías y habilita el comportamiento editorial normal.

Las 127 rutas comprobadas —12 páginas React y 115 artículos— responden correctamente, tienen un H1, canonical único y metadatos esenciales. Se verificaron las 115 anclas de temas principales e internos y las 345 variantes de ilustración. En WordPress hay 115 imágenes destacadas, ninguna ausente y ningún fragmento de idioma incorrecto en las entradas publicadas. No se borraron revisiones históricas al corregir las muestras.

### WPO y mediciones

Mediciones de Lighthouse en modo móvil, con Chrome headless y simulación de red/CPU de la herramienta. No son datos de usuarios reales, ni certifican INP de campo. Los JSON incluyen versión, hora y parámetros de cada ejecución.

| Plantilla | Rendimiento | Accesibilidad | Buenas prácticas | SEO | LCP | CLS | TBT |
|---|---:|---:|---:|---:|---:|---:|---:|
| Portada inicial, antes | 83 | 100 | 100 | 100 | 1,2 s | 0 | 660 ms |
| Portada actual | 98 | 100 | 100 | 100 | 1,0 s | 0 | 160 ms |
| Área Trabajo | 98 | 100 | 100 | 100 | 2,1 s | 0 | 100 ms |
| Contacto | 97 | 100 | 100 | 100 | 1,3 s | 0 | 200 ms |
| Índice del blog | 97 | 100 | 100 | 69* | 1,5 s | 0 | 200 ms |
| Artículo de muestra | 98 | 100 | 100 | 69* | 1,6 s | 0 | 150 ms |

\* La reducción de la puntuación SEO del blog y la muestra corresponde a su exclusión deliberada de indexación. No debe retirarse `noindex` para obtener una puntuación de herramienta: primero debe existir contenido editorial definitivo. Una de las mediciones intermedias de área coincidió con un reinicio y registró 503 al solicitar robots; se repitió tras estabilizar el servicio y se conserva la evidencia intermedia.

Las imágenes de categoría equivalentes bajaron de **3.661.698 a 1.286.236 bytes (64,9 % menos)**. Se añadieron variantes para móvil y vistas sociales. Las 345 imágenes de temas ocupan aproximadamente 3,9 MB en el repositorio; se solicitan según tamaño y proximidad, no como una descarga inicial de toda la colección. Los maestros JPEG quedaron fuera de `public/`. Los recursos gráficos públicos nuevos son WebP; favicon y archivos técnicos de WordPress conservan el formato que requiere su función.

Nginx aplica gzip, caché de recursos, protección de rutas y caché breve de páginas WordPress anónimas. Las sesiones de edición, REST, formularios, búsquedas y escrituras evitan esa caché. Apache aplica expiración a imágenes y recursos editoriales; los CSS llevan versión derivada del archivo para que los cambios se actualicen. Se eliminaron CSS redundantes del tema padre que alteraban colores y contraste. Las fuentes son locales y usan `font-display: swap`.

No había vídeos publicados que comprimir. Las animaciones nuevas se resuelven con gráficos, CSS y GSAP; no se añade una descarga de vídeo para producir estos efectos. Los criterios de vídeo descritos antes quedan como contrato para recursos futuros, sin afirmar una compresión que no se haya hecho.

### Contacto y entregabilidad

El formulario React usa `POST /blog/wp-json/mee/v1/contact`, con validación en servidor, token HMAC ligado al cliente, caducidad de 30 minutos, un mínimo de tiempo, campo trampa, control de origen y límites de frecuencia. Los datos se escapan antes de componer HTML. Se valida el destino de respuesta y el remitente SMTP es siempre `contacto@moevec.org`.

Límites actuales: 3 envíos por IP y 2 por correo en una ventana de 15 minutos; límite global de 30 en 15 minutos. El token aceptado se recuerda para evitar duplicados al reintentar. La confirmación fallida se programa para reenvío sin perder la solicitud ya entregada.

Pruebas realizadas:

| Prueba | Resultado |
|---|---|
| Formulario vacío | Errores asociados a campos y foco en el primer error |
| Solicitud válida al buzón del proyecto | Recibida, referencia `MEE-20261028-AD6779FA` |
| Acuse HTML al mismo buzón de prueba | Recibido con la misma referencia |
| Acuse externo a la cuenta Gmail del titular | Recibido en INBOX, referencia `MEE-20261028-F3C5A7C6` |
| Autenticación en Gmail | SPF **pass**, DKIM **pass**, DMARC **pass**, TLS 1.3 |
| Origen externo | 403 |
| Token incorrecto | 403 |
| Campos inválidos | 400 |
| Campo trampa completo | 200 sin enviar correo |

DNS comprobado tras guardar: MX de DonDominio, SPF `v=spf1 include:spf.dondominio.com ~all`, DKIM con selector `dddk` y DMARC `v=DMARC1; p=quarantine; adkim=r; aspf=r; pct=100`. La prueba externa confirma el funcionamiento conjunto; los mensajes internos de un mismo servidor no tenían esos sellos y no se usaron como prueba de autenticación externa.

### Seguridad y continuidad

- WordPress 7.1.3 y PHP 8.3.36 comprobados. Plugins activos: MEE Editorial y Two-Factor 0.17.0 procedente del repositorio oficial de WordPress.
- Se activó el segundo factor **por correo** para `mee_admin`. Los códigos y la recuperación usan el buzón operativo `contacto@moevec.org`, corrigiendo la dirección inicial `admin@moevec.org`. La contraseña no se cambió. TOTP y códigos de respaldo adicionales pueden configurarse en el perfil; no se inventó un dispositivo del titular.
- REST de usuarios y XML-RPC responden 404. Los directorios y archivos sensibles probados devuelven 403 o 404. Edición de archivos desactivada, limitación de intentos de acceso y respuesta de error genérica.
- Cabeceras de protección presentes, versiones de Nginx/PHP retiradas de las respuestas, CSP en modo de observación con los recursos propios necesarios. `wp-config.php` con permisos 640. Ocho claves/sales diferentes, longitud mínima comprobada de 40 caracteres, sin mostrar sus valores.
- Cron real del sistema cada minuto, compatible con nombres cambiantes de contenedores; WP-Cron de visitas desactivado.
- `npm audit`: **0 vulnerabilidades conocidas** en el grafo analizado. Esto no equivale a una certificación de ausencia de vulnerabilidades de toda la infraestructura.
- Copia previa SQL y volumen WordPress guardada en `/data/mee-backups/pre-auditoria-20261028`, con directorios privados. Restauración SQL en una base aislada: 12 tablas coincidentes; extracción de archivos y presencia de configuración/tema comprobadas. No se declara probado un arranque completo de una web restaurada en otro servidor. Continúan las copias diarias existentes de Coolify.

El primer arranque del importador reveló la diferencia entre UID de Alpine y Debian. Se corrigió `wordpress-init` a `33:33`, se reparó la primera entrada incompleta y se verificaron arranques sucesivos sin duplicación. Los reinicios de Compose causan una breve interrupción de servicio; el registro de despliegue conserva ese comportamiento.

### SEO, GEO e indexación ejecutada

Canonical, Open Graph, Twitter Card, migas y JSON-LD se incorporaron en React y WordPress. La información estructurada describe contenido visible; las muestras no se marcan como artículos definitivos con autoría inventada. Existen páginas de presentación del movimiento, contacto, privacidad e información del sitio.

Se verificó **la propiedad de dominio en Google Search Console mediante DNS** y se envió `https://moevec.org/sitemap.xml`. Google muestra **«Correcto» y 12 páginas descubiertas**. Descubrir páginas no equivale a que estén indexadas o posicionadas. El sitemap WordPress excluye las maquetas y podrá incorporar artículos reales cuando existan.

Bing Webmaster Tools se abrió para comprobar disponibilidad: mostró la página de acceso sin sesión activa. No se creó una cuenta adicional ni se afirmó un envío inexistente. Como siguiente canal opcional, el titular puede autenticar su cuenta, añadir `moevec.org`, verificarla y enviar el mismo sitemap. La base técnica de rastreo ya está publicada.

Para GEO se han aplicado las prácticas comprobables: HTML legible, organización clara, resúmenes, jerarquía y enlaces internos, vocabulario consistente y datos estructurados fieles. No se crean promesas de aparición en respuestas de IA ni contenido masivo indexable de prueba. No se añade `llms.txt` como supuesto requisito de Google.

### Red social: preparado y límite real

El puente está implementado en `mee-editorial/inc/network.php`, con webhook firmado, marcas de tiempo, cola y reintentos; respuesta pública cacheada y consumo desde React por el mismo origen. Las muestras se excluyen de la sincronización. El archivo `integrations/README.md` documenta la configuración privada y el contrato; `integrations/phoenix/` conserva los módulos recibidos del usuario.

La API `https://red.moevec.org/api/v1/areas` **no está operativa con TLS válido**: el certificado observado no corresponde a `red.moevec.org`, y el DNS apunta al servicio de hosting de DonDominio. No se dispone aquí del proyecto Phoenix completo ni de una instancia de Kali accesible. Por eso no se activó el puente hacia un destino incorrecto. El sitio sigue funcionando y ofrece contacto.

Para completar la integración de producción faltan la aplicación Phoenix completa, su despliegue, el DNS/TLS de `red.moevec.org`, el secreto compartido privado y las pruebas de publicación/retirada/firmas contra esa instancia. Los ensayos de Elixir descritos por la auditoría adjunta no se presentan como ejecutados de nuevo en esta sesión.

## Correspondencia con la auditoría adjunta

| IDs | Estado al cierre | Evidencia / límite |
|---|---|---|
| A-01, A-05 | Aplicados | React estático y WordPress separados; código y despliegue versionados |
| A-02 | Verificado con alcance | PHP y copias; restauración SQL aislada y extracción, sin arranque completo de otro sitio |
| A-03, A-04 | Verificados | HTTPS saliente 200 y cron del sistema |
| A-06 | Verificado | Dos plugins activos e inventariados |
| A-07 | Parcial por servicio externo | 7/56/59 preservados localmente; comparación con API Phoenix pendiente de su despliegue |
| S-01, S-02 | Aplicados y comprobados | HTTPS, redirecciones y cabeceras; sin escaneo exhaustivo de todas las suites TLS |
| S-03 a S-09 | Aplicados y comprobados | Generador, usuarios, acceso con segundo factor, edición, XML-RPC, rutas sensibles y directorios |
| S-10 | Alcance explícito | Auditoría npm sin vulnerabilidades conocidas; no se ejecutó WPScan con base de pago ni se certifica un pentest |
| S-11 a S-14 | Aplicados / comprobados según evidencia | Configuración 640, sales, cabeceras y correo autenticado |
| P-01 a P-05 | Aplicados y medidos | Tabla Lighthouse, WebP, caché, gzip y fuentes locales; INP de campo pendiente de usuarios reales |
| E-01 a E-06 | Aplicados | Metadatos, HTML, sitemap y Search Console; exclusiones intencionales de maquetas |
| E-07 | Preparado | Enlaces de participación se activarán con la red válida |
| X-01 a X-05 | Comprobaciones realizadas | Alternativas, foco, contraste, movimiento y H1; Lighthouse 100 no certifica por sí solo toda WCAG 2.2 AA |
| L-01, L-02 | Parciales: dato del titular | Falta identidad jurídica, datos fiscales/domicilio aplicable y política definitiva de conservación |
| L-03 | Descrito conforme a la instalación actual | Sin seguimiento no esencial; preferencias locales y cookies técnicas de editores documentadas |
| L-04 | Preparado para la futura red | Criterios editoriales publicados; reglas definitivas de comunidad pendientes de la aplicación social |
| L-05 | Sin licencia abierta general | No se asignaron derechos de terceros ni una licencia que el titular no había definido |
| C-01 | Encargo de maquetación cumplido | 115 muestras; la publicación editorial definitiva queda diferenciada |
| C-02 | Parcial por servicio externo | Fuente original preservada; no se pudo comparar textos de una API Phoenix activa |

## Evidencias y entrega

Carpeta: `inventario/auditoria-2026-10-28/`.

- `baseline-http.json`, `final-http.json`: antes/después de rutas y cabeceras.
- `public-route-checks.json`: 127 rutas comprobadas sin fallos estructurales detectados.
- `taxonomy-assets-check.json`, `visuals-build.json`: taxonomía y recursos.
- `lighthouse-before.json`, `lighthouse-final-home.json`, `lighthouse-final-area.json`, `lighthouse-contact.json`, `lighthouse-final-blog.json`, `lighthouse-final-article.json`: mediciones conservadas.
- `contact-boundaries.json`, `mail-receipt-check.json`, `mail-authentication.json`: contacto y entregabilidad.
- `security-check.json`, `npm-audit.json`: comprobaciones técnicas.
- Capturas de portada en escritorio/móvil, blog, artículo móvil, contacto enviado, dominio verificado y sitemap con 12 páginas.

Las evidencias locales pueden contener datos operativos del titular. No se sirven desde `public/`. Las contraseñas, claves SMTP, códigos de autenticación y copias SQL no se adjuntan a este informe.

**Pendientes concretos:** completar la identidad y el expediente legal del responsable; desplegar/verificar la aplicación Phoenix para activar el puente; desarrollar y revisar contenido editorial definitivo antes de indexarlo; configurar Bing si se desea ese panel; valorar copia externa cifrada y una restauración completa en otro entorno. La ejecución técnica y gráfica descrita queda entregada sin atribuir premios, posición en buscadores ni cumplimiento legal no demostrado.


## Registro final de versión y respaldos

Producto publicado y comprobado: commit `4b90ce989daa7d8d47d2af20d07b773a68bd960a`. Web y WordPress arrancados, importador terminado correctamente, 115 maquetas conservadas, segundo factor activo y rutas principales con HTTP 200. La portada queda con movimiento normal y el panel de transición oculto tras navegar. Un tema interno se abrió mediante su control accesible: imagen cargada y animación en ejecución únicamente al quedar visible. La portada editorial comienza con una muestra de cada una de las siete áreas.

Copia de fuente: `/Users/nerea/Documents/Proyectos/MEE/mee-backups/MEE_Codex_2026-10-28_060357.zip` (653 archivos). Copia de producción posterior: `/data/mee-backups/post-auditoria-20261028/`, SQL de 2,7 MB y archivos de aproximadamente 33 MB, con directorio privado. Evidencia: `deployment-check.json`, `security-check.json`, `motion-checks.json` y `tema-interno-check.json`. Se retiró la copia temporal local de la credencial SMTP y se detuvo el servidor de revisión; la configuración operativa permanece en el volumen privado del servidor.
