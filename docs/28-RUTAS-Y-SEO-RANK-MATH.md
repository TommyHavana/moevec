# Rutas de lectura y SEO coordinado · 05/11/2026

## Encargo y alcance

El fundador autorizó ejecutar sin nuevas confirmaciones el paquete «Empieza aquí» y después instalar Rank Math, coordinar SEO de WordPress y Next.js y organizar el descubrimiento y la continuidad. Search Console, tracking y analytics quedan a cargo del fundador. Se conservan las 840 entradas, sus ID, H1, slugs y los 2520 originales.

## Entrega de producto publicada

- `/empieza-aqui/`: tres rutas de seis lecturas existentes, con propósito y orden editorial.
- Rutas: organizar tus finanzas (37 min estimados), mejorar tus capacidades laborales (46 min), entender la economía (38 min).
- Marcas voluntarias de lectura en almacenamiento local, sin transmitir actividad; persistencia después de recargar comprobada. Privacidad actualizada.
- Enlace desde portada y navegación de React y WordPress. Los 18 artículos enlazan al siguiente paso y a su ruta.
- Descubrimiento por tema y nivel, tiempo estimado de lectura y relacionados por tema y nivel.
- `/seguir-mee/`: RSS general y por las siete áreas, regreso a las rutas y contacto editorial. No se crea un servicio de boletines ni se prometen correos automáticos.
- Vista móvil de 390 px comprobada sin desbordamiento en la ruta y en los filtros del blog; escritorio inspeccionado y capturas en `inventario/rutas-seo-2026-11-05/`.

## Instalación y causa del error

El directorio `wp-content/plugins` pertenece a root y tiene modo 0755. WordPress corre como UID33, por lo que no puede crear una carpeta nueva dentro. `uploads` y `upgrade` sí son escribibles y había 240,7 GB libres: el error no era falta de disco. El despliegue anterior usa `cp -a`, que preserva propietarios.

La revisión automática rechazó dar a WordPress escritura sobre toda la carpeta padre, por ampliar sus permisos. No se aplicó ese cambio. Se instaló exclusivamente Rank Math desde el paquete oficial mediante despliegue. El directorio padre sigue protegido. Las futuras instalaciones de plugins requieren el mismo procedimiento de despliegue o una decisión administrativa expresa.

Rank Math gratuito **1.0.281** instalado y activo. Paquete oficial de WordPress, 3.369.147 bytes, SHA256 `d3d464bb2b3b619e46cd93c16a8d21073c473bd411867c1c8d73110debd0ba29`. Fuente vendorizada y declarada en el Dockerfile; se preserva una versión posterior que ya exista en el volumen. Se usa la opción normal del plugin para omitir su cuenta opcional. No hay cuenta RankMath.com, conexión de Google, licencia de pago ni analytics configurados.

## Metadatos e integración

- 840 entradas: título SEO, descripción, palabra clave, canonical explícito, categoría primaria, robots y vista social.
- 2520 imágenes: alt descriptivo, título y descripción del medio. Son metadatos de adjuntos, no una supuesta etiqueta HTML de metadescripción por imagen.
- 66 portadas recibieron contexto de tema en el alt; la revisión posterior ajustó 10. Se compararon los 2520 originales públicos con los locales por SHA256: cero diferencias.
- Revisión de 59 casos: palabras clave naturales, 23 descripciones más precisas y cinco títulos SEO. Ningún H1 ni slug alterado por este trabajo.
- Rank Math es el único emisor del head SEO de WordPress. Se elimina la descripción adicional de Hello Elementor. El SEO anterior queda como alternativa si Rank Math no llega a arrancar.
- Schema coherente entre plataformas: Organization MEE en la raíz, WebSite, BreadcrumbList, WebPage y Article con los tres originales; autor editorial como Organization, sin inventar una persona.
- Búsquedas, filtros, etiquetas, adjuntos, autores, fechas, muestras y errores fuera del índice. Las 122 categorías y la asignación de cada artículo se conservan.
- Robots enlaza `/sitemap.xml` y `/blog/sitemap_index.xml`. El antiguo `/blog/wp-sitemap.xml` redirige al índice de Rank Math.
- El índice real por encabezados de la plantilla se declara mediante el filtro oficial de compatibilidad de TOC de Rank Math.

## Medición real de Rank Math

Se ejecutó «Status & Tools → Database Tools → Update SEO Scores» en la sesión administrativa, incluyendo entradas con puntuación previa. No se asignaron puntuaciones artificiales.

| Medida | Primera medición | Después de la revisión |
|---|---:|---:|
| Entradas con puntuación | 840 | 840 |
| Media | 73,91 | 78,27 |
| Mínimo / máximo | 25 / 86 | 67 / 88 |
| Verde (80 o más) | 33 | 513 |
| Por debajo de 50 | 47 | 0 |

La puntuación evalúa criterios del plugin; no garantiza indexación ni posiciones. No se alargaron artículos ni se añadieron números, promesas o repeticiones para forzar un 100.

## Verificación y copias

- `npm run build`: correcto, TypeScript y exportación estática incluidos; 18 páginas en el sitemap principal.
- Auditoría de base de datos: 840 entradas, 2520 imágenes, 122 categorías, 0 borradores, metadatos y asignaciones sin errores.
- Auditoría HTTP definitiva posterior al despliegue, 2026-11-05T12:57:23.085744+00:00: **840/840 entradas correctas**, H1 preservado, un título SEO, una descripción, un canonical, robots indexable y un Article con los tres originales. Las 2520 imágenes renderizadas responden HTTP200 y son WebP, con alt correcto. Se admiten los derivados interiores de 1024px que WordPress ya servía; no se han sustituido originales.
- Sitemap de Rank Math: 840 URLs únicas de artículos, 2520 referencias de imagen y portada del blog; sin artículos ausentes ni ajenos. El sitemap principal contiene18 páginas, todas HTTP200, con H1, descripción única y canonical correcto. El antiguo sitemap redirige al nuevo índice.
- Las18 continuaciones y los8 RSS están comprobados; filtros por tema/nivel y búsqueda vacía funcionan, con noindex. Las notas78,10/461verdes comunicadas durante el proceso fueron lecturas intermedias; el corte final de base de datos registra78,27/513.
- Copia previa proporcional local `mee-backups/MEE_Pre_Rutas_SEO_2026-11-05_123935.zip`, CRC comprobado; cadena editorial anterior preservada. SQL y código previos en `/data/mee-backups/rutas-seo-20261105/`. Copia consistente posterior de metadatos `after-seo-metadata.sql.gz`, integridad gzip comprobada, SHA256 `af5f9cff8d4d1d580511c04e538f5728ae651638aa7ca367d3fa3507bdc53d04`. Su descarga local fue rechazada por revisión automática al incluir potencialmente datos sensibles y credenciales; se conserva en el VPS con permisos privados. La evidencia SEO y el código sí se conservan localmente.
- **Despliegue definitivo terminado** en Coolify: `mtwkdp9b1exqpphniveo4z7c`, producto `e104c62c8b92fdaf13fc6a3a806538ee4094f14f`. Contenedores nuevos web`78470416b307`, WordPress`ee580eacc175`, MariaDB`347bccb70020`; imágenes web/WordPress etiquetadas con ese commit y base de datos saludable. Nueve archivos de plugin/tema coinciden por SHA256 con la fuente. WordPress7.1.4 y PHP8.3.36 conservados; Rank Math1.0.281 activo; tracking de uso del plugin desactivado.
- Copia local de fuente proporcional `MEE_Rutas_RankMath_Source_e104c62c_2026-11-05.tar.gz`: 4.963.592bytes, 2442rutas, lectura tar comprobada, SHA256`c3b8502fc9569c0f8f141250acd3aa73cf123c01155bf2fad40435b06abcb6f2`. También guardada en el VPS. Los archivos editoriales originales y su cadena de copias anteriores se conservan.

## Continuidad exacta

La producción editorial permanece cerrada: **840/840, 0 en curso, 0 pendientes**, sin reactivar la automatización antigua. Este paquete también está terminado y verificado. No hay trabajos de publicación, imágenes o despliegue pendientes de esta entrega. El fundador hará las conexiones de Search Console y analítica; los mapas de sitio ya están disponibles. Para trabajos futuros, partir de la fuente privada actual y de `editorial/seo-upgrade-state.json`; no repetir la migración ni crear otra automatización por este cierre.
