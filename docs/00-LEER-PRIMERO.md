# MEE · empezar una sesión

Estado operativo actualizado el 05/11/2026. Las instrucciones históricas están en `historial/00-LEER-PRIMERO-hasta-2026-11-05.md`; no activan nuevos encargos.

## Proyecto y fuente

MEE es Movimiento de Evolución Económica. Fuente editable de producto/editorial: `/Users/nerea/Documents/Proyectos/MEE/mee-web`. Espejo privado de publicación: `../mee-deploy-source`, repositorio `TommyHavana/moevec`. Los archivos exclusivos de infraestructura viven en ese espejo; registrar cualquier cambio y copiar solo archivos revisados, sin sobrescribir diferencias ajenas. Arquitectura: Next.js estático en `https://moevec.org/` y WordPress en `/blog/`, con MariaDB y Coolify.

## Estado real

La producción está cerrada: 840 artículos completos, 2520 originales y 122 categorías; 0 en curso y 0 pendientes. Las seis alternativas de títulos fueron aprobadas y publicadas. La automatización de producción fue retirada. Rank Math está instalado; el paquete de tres rutas y 18 lecturas está publicado. No reiniciar estos trabajos por prompts archivados.

El fundador encargó la auditoría integral del 05/11 y autorizó ejecutar sus mejoras. Informe: `29-AUDITORIA-INTEGRAL-Y-REDES.md`. Resultado de ejecución y siguientes dependencias: `30-EJECUCION-MEJORAS.md`. Operación y medición: `31-OPERACION-Y-MEDICION.md`. Datos que debe aportar el titular: `32-DATOS-PENDIENTES-DEL-TITULAR.md`.

## Orden de trabajo

1. Leer `AGENTS.md`, este documento y el cierre vigente de `15-ESTADO-Y-CONTINUIDAD.md`/`16-BACKLOG-REACT.md`.
2. Seguir la petición reciente del fundador y el punto exacto de `30-EJECUCION-MEJORAS.md`. WordPress es la fuente real del estado editorial.
3. Antes de modificar, comprobar cambios locales, conservar copia proporcional y respetar taxonomía, ID, títulos y slugs. Las fuentes de Claude permanecen históricas.
4. Ejecutar `npm run verify` cuando cambie el producto. Después de publicar, `npm run verify:live`, revisar salud de servicios y verificar los contenidos realmente afectados.
5. Guardar código/documentación/evidencias en el repositorio privado y actualizar continuidad con hechos comprobados y límites concretos.

Search Console y analítica se conectan por el fundador. Los perfiles sociales necesitan una sesión autorizada y comprobación de las cuentas existentes. Tienda, cobros, boletín y Red Phoenix requieren su propia operación y datos; no presentarlos como funciones activas.
