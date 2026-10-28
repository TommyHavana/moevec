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
| P1 | Posible enumeración de usuarios tras publicar | Restringir REST de usuarios y archivo de autor público; desactivar XML-RPC y edición de archivos; limitar intentos de acceso. 2FA requiere enrolamiento de un dispositivo del titular, no simularlo. |
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

Estado inicial: diagnóstico guardado; ejecución autorizada en curso.
