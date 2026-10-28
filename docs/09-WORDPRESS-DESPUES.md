# WordPress: fase posterior a React

> Actualización 28/10/2026: el fundador añadió venta de arte digital. La propuesta arquitectónica más reciente y sus decisiones pendientes están en el documento 14. Sigue sin autorizarse la implementación de WordPress/tienda en esta fase React.

**No ejecutar durante la fase React.** Este documento conserva los requisitos y resuelve la transición cuando se aprueben diseño, contenido y rutas de la parte visual.

## Encargo actual

- WordPress editorial en local, con Elementor para páginas editables, ACF para datos editoriales y un tema hijo propio que comparta identidad con React.
- El fundador ha mencionado WooCommerce para vender arte reproducible en cuadros de diseñadores cubanos y anticomunistas. Es una fase comercial posterior, con artistas, derechos de reproducción, variantes, impresión, envío, pago e impuestos por definir.
- El ZIP de Claude propone Astra y `/lab` para contenido, comunidad y debate. La conversación reciente propuso Hello Elementor y `/blog/`. **No tratar el conflicto como resuelto por costumbre:** se confirmará ruta pública, tema base y alcances cuando se inicie la fase WordPress.

## Preparación que ya existe

`wordpress/compose.yaml` y `wordpress/themes/mee-child/` son un esqueleto local creado antes de recibir el ZIP de Claude. No se ha ejecutado WordPress ni instalado Elementor o ACF. El tema hijo actual declara Hello Elementor como padre y las plantillas PHP cubren archivo, artículo y página; es una propuesta técnica provisional, no la elección final del fundador.

## Orden futuro

1. Dar por cerrada React y cerrar ruta pública `/blog/` frente a `/lab/` y alcance de cada sección.
2. Arrancar WordPress local y decidir entre padre Hello Elementor o Astra con una prueba comparada de plantillas y coste de mantenimiento. No contratar Elementor Pro sin autorización.
3. Instalar y configurar Elementor/ACF gratuitos; crear categorías y, si interesa, niveles Fundamentos/Desarrollo/Aplicación como taxonomía transversal.
4. Integrar el diseño editorial con React, migrar desde `03-EDITORIAL-CATEGORIAS.md` sólo textos aprobados y publicar artículos con fuentes.
5. Diseñar aparte normas de identidad, privacidad, moderación y voto público antes de comunidad y gamificación.
6. Diseñar tienda WooCommerce y contratos de explotación de imágenes antes de crear productos.
7. Unificar rutas detrás del servidor elegido, probar enlaces y despliegue sin depender de GitHub Actions.
