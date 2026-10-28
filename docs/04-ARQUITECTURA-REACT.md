# Arquitectura técnica de la fase React

> Actualización 28/10/2026: ver documento 17 para el contrato visual propuesto (no implementado) y documento 14 para la arquitectura editorial/tienda recomendada, pendiente de decisión final.

## Decisión y alcance

Next.js con React y TypeScript, usando App Router y `output: 'export'`. `npm run build` debe generar HTML, CSS y JS estáticos en `out/`; no se necesita un servidor Node para servir esta fase cuando se publique. La exportación estática exige generar las siete rutas de área en tiempo de compilación mediante `generateStaticParams`. Documentación oficial: https://nextjs.org/docs/app/guides/static-exports.

**Entorno actual:** proyecto local. `npm run dev` en `http://localhost:3000`; el blog WordPress queda pendiente. No usar Git, GitHub Actions, API externa, autenticación ni base de datos en React.

## Rutas y responsabilidades

| Ruta | Archivo | Contenido |
| --- | --- | --- |
| `/` | `app/page.tsx` | Entrada y mosaico de siete categorías |
| `/areas/[slug]/` | `app/areas/[slug]/page.tsx` | Imagen, resumen, subcategorías, temas anidados y siguiente área |
| Otras | `app/not-found.tsx` | Mensaje de error y vuelta al índice |

`app/layout.tsx` contiene cabecera, salto al contenido, metadatos y pie. `app/styles.css` mantiene estilos responsive y estados de foco. Las imágenes están en `public/images/areas/`.

## Fuentes de verdad

1. **Taxonomía editorial original:** `fuentes/claude/docs/02-taxonomia.md`. Archivo histórico; no modificar sin registrar una nueva decisión.
2. **Texto editorial editable:** `docs/03-EDITORIAL-CATEGORIAS.md`. El fundador revisará promesas, resúmenes y beneficios.
3. **Datos de máquina:** `content/taxonomia.json` y `content/editorial.json`, generados respectivamente con `node scripts/sync-taxonomy.mjs` y `node scripts/sync-editorial.mjs`.
4. **Modelo de interfaz:** `lib/areas.ts`, que combina los datos por orden y entrega siete objetos con `sections`. Los scripts validan número, orden y nombres antes de exportar.

Si se cambia un título o el orden: ajustar el documento editorial de trabajo y su referencia taxonómica de forma explícita, ejecutar primero sincronización de taxonomía y después la editorial, revisar el JSON resultante y construir. **No editar JSON a mano:** se perdería en la siguiente sincronización. Los slugs son direcciones públicas de React; no cambiarlos sin plan de redirecciones al publicar.

## Contrato visual de cada área

`/areas/[slug]/` muestra una cabecera con título e imagen original; un índice superior `position: sticky` desplazable horizontalmente; una tesis y un párrafo de contexto; tantas secciones como temas reales existan. Para Política y Economía se muestran diez ejes, cada uno con lista de temas y subtemas anidados. El enlace «siguiente área» cierra el recorrido. El índice apunta a `id` estables y debe seguir operable con teclado y sin animación.

## Contrato futuro con WordPress

React es la presentación de las capacidades; WordPress aportará artículos, perfiles de autor y archivo editorial. No fijar desde ahora la ruta pública `/blog/` o `/lab/` como definitiva: los documentos antiguos y las conversaciones recientes discrepan. Mientras WordPress no esté listo, React no muestra enlaces muertos. La posible consulta a REST API y la estrategia de cache se decidirán cuando exista contenido publicado; el export estático por sí solo no actualizará en vivo artículos nuevos.

## Organización para copias locales

Guardar código, documentación y activos; excluir `node_modules`, `.next`, `out`, `.env.local` y credenciales. El ZIP de entrega sirve como fotografía del estado, no sustituye una copia de los futuros datos de WordPress. No publicar esta versión sin aprobar logotipo, textos y navegación final.
