# Respaldo tras 42 entradas · 28/10/2026

- Directorio privado VPS: `/data/mee-backups/produccion-840-incremento-37-42-20261028/`.
- `wordpress.sql`: volcado completo consistente con las 42 publicaciones, **4.418.962 bytes**.
- `uploads-37-42.tar.gz`: **7.160.474 bytes**, **132 archivos**, originales 37–42 y sus variantes. Miembros y SHA-256 cotejados con `files.json`.
- `SHA256SUMS`: cuatro archivos comprobados correctamente. Directorio 700; archivos 600. SQL y secretos fuera del repositorio.

## Restauración documentada

Archivos base: `produccion-840-veintisiete-entradas-20261028/wordpress-files.tar.gz`. Superponer `produccion-840-incremento-28-36-20261028/uploads-28-36.tar.gz` y después `produccion-840-incremento-37-42-20261028/uploads-37-42.tar.gz`, conservando rutas. Importar finalmente el SQL completo de esta copia de 42; no sustituirlo por un SQL antiguo. Código en la fuente privada de despliegue.

Se comprobaron consistencia de generación del volcado, hashes y miembros del comprimido. No se ha realizado aquí una nueva prueba de arranque de restauración completa ni una copia externa cifrada. La copia local de fuente y el commit se registran al cerrar el bloque.

## Fuente local

`/Users/nerea/Documents/Proyectos/MEE/mee-backups/MEE_Codex_2026-10-28_165459.zip`: 1.366 archivos, integridad ZIP correcta y 51 archivos de artículos e imágenes recientes comparados byte a byte. Incluye nueve WebP preparados para 43–45; no son publicaciones. El ZIP es copia de fuente según las exclusiones del script, no un respaldo completo del servidor. Se creó antes de añadir esta referencia al propio informe.
