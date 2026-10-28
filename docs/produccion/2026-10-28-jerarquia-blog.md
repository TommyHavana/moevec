# Corrección de la jerarquía del blog

El fundador preguntó por una aparente categoría «Editorial» y pidió corregir cualquier agrupación errónea antes de continuar la producción.

## Comprobación y resultado

- No existía una categoría Editorial. Era el rótulo del enlace al índice del blog en la ruta de navegación.
- Las nueve entradas publicadas estaban correctamente asignadas a Capitalismo Consciente y Definición Esencial, en el orden del manifiesto. No se reasignaron a otra área.
- La ruta visual omitía el área principal. Se corrigió a Inicio → Blog → Capitalismo Consciente → Definición Esencial. El schema añade después el artículo.
- El archivo de la subcategoría destaca ahora su categoría principal en la navegación.
- Existía una categoría técnica Uncategorized, ID 1, sin objetos asociados en ningún estado. Tras copia SQL y del volumen WordPress, se cambió la categoría predeterminada a la ya existente Capitalismo Consciente (ID 6) y se eliminó únicamente ese término vacío. El publicador sigue asignando explícitamente las categorías de cada ID.
- Inventario final: 122 nodos y siete raíces, con nombres, slugs y padres idénticos a las fuentes planificadas. No se añadieron categorías ni se modificaron los slugs del plan o de las entradas.

## Evidencia y archivos

- `category-organization-audit.json`: estado previo.
- `category-hierarchy-fixed.json`: coincidencia exacta con el manifiesto tras retirar el término técnico.
- `editorial-hierarchy-public-checks.json`: nueve rutas visuales y schemas correctos, área destacada y artículos presentes en sitemap.
- Cambios: `wordpress/plugins/mee-editorial/inc/seo.php`, `wordpress/themes/mee-child/single.php` y `functions.php`. Lint PHP correcto y publicación directa del parche, sin reiniciar servicios.
- Copia previa: `/data/mee-backups/produccion-840-jerarquia-blog-20261028/`, SQL y volumen completos; se conservaron también los tres archivos anteriores. La producción 10–12 se reanudó después de comprobar la corrección.
