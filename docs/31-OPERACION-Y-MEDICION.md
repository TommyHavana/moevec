# Operación y medición MEE · 05/11/2026

## Fuente de trabajo y publicación

Editar producto, editorial y documentación en `mee-web`. `mee-deploy-source` es el espejo privado de publicación: no iniciar otra edición allí. Los archivos exclusivos de despliegue (`deploy/`, Dockerfile, compose) se mantienen en el espejo; sus cambios deben registrarse en este documento. Comparar diferencias antes de copiar, sincronizar solo los archivos del encargo y detenerse ante cambios ajenos. No reescribir Git ni retirar originales históricos. El repositorio pesado conserva sus activos hasta disponer de un destino de archivo probado.

## Puerta de publicación

`npm run verify` compila y valida el HTML exportado y sus recursos. `npm run verify:live` comprueba una selección crítica de rutas públicas, schema, canonical, imágenes y robots; no envía formularios. El workflow manual y de cambios de producto ejecuta estas verificaciones. Después de publicar comprobar contenedores saludables y el resultado público antes de cerrar. Un fallo debe producir un código de salida distinto de cero.

## Actualizaciones y recuperación

WP, tema y plugins se actualizan desde la fuente oficial: registrar versión/hash, copia privada previa, prueba aislada, despliegue, comprobación y rollback. El padre de plugins protegido se conserva; no resolver una instalación abriendo permisos generales. Revisar si la versión instalada supera el paquete fijado antes de copiarlo. CSP permanece en modo informe hasta probar el conjunto de funciones administrativas y públicas.

Copias: mantener SQL y uploads con permisos privados en el VPS, comprobar integridad y registrar restauraciones. El objetivo pendiente es una copia cifrada externa con credenciales bajo control del titular y una restauración completa en otra infraestructura. No se ha configurado un destino nuevo ni se declara cumplido ese objetivo. No descargar bases de datos de producción por esta tarea.

## Conexión de medición a cargo del fundador

Antes de crear una propiedad, comprobar la propiedad de dominio existente de `moevec.org`. Mapas: https://moevec.org/sitemap.xml y https://moevec.org/blog/sitemap_index.xml. Registrar semanalmente cobertura/indexación y consultas por página, separado de puntuaciones de Rank Math. Anotar la fecha del despliegue para comparar periodos.

Contrato preparado de eventos: `route_start` (slug de ruta), `article_next` (ID de origen/destino), `reading_mark` (ID/estado), `resource_download` (slug) y `contact_success` (sin contenido del mensaje). Activar solo tras elegir herramienta, configurar privacidad y validar cada evento. Ningún nombre, correo, mensaje o URL arbitraria debe ir en parámetros. No se incorpora un emisor ni una cola de tracking por anticipado.

UTM: source=facebook/instagram, medium=organic_social, campaign=rutas_2026_11, content=ID_formato. Usar minúsculas y no incluir datos personales. Canonical sin parámetros. Los enlaces de bio pueden ir al índice; cada publicación concreta debe ir a su contenido prometido.

## Contenido, revisión y cuentas

El calendario `editorial/review-schedule.json` registra las fechas acreditadas y una próxima revisión propuesta. La fecha de revisión no se actualiza al cambiar formato, enlaces o SEO. Priorizar cambios en normas/productos, correcciones y fuentes caducadas. La comprobación de vigencia sigue requiriendo revisión editorial.

Inventario social en `editorial/social/accounts.json`: URL pública, handle, titularidad verificada y estado. Completar tras comprobar cuentas reales. No publicar enlaces inventados, solicitar contraseñas por chat ni duplicar perfiles. Preparar piezas en `editorial/social/pilot.json`; estado preparado no significa publicado. El titular resuelve login, identidad y aceptación de condiciones cuando la plataforma lo solicite.
