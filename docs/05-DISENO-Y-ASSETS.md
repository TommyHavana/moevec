# Diseño visual y sistema de imágenes

> Actualización 28/10/2026: cada categoría y subcategoría necesita imagen y movimiento con significado. Ver documentos 13 y 19 para el nuevo alcance; las imágenes por subcategoría y su animación específica todavía no están implementadas.

## Referencia de experiencia

https://turnerduckworth.com/ inspira jerarquía tipográfica rotunda, apertura breve, imágenes a gran escala y capítulos editoriales. El encargo pide una aproximación muy fiel al **ritmo, proporción y transición** entre portada y páginas de detalle. No copiar su logotipo, fotografías, nombres de proyectos, código ni textos. Las imágenes de MEE representan ideas y capacidades del instituto, no trabajo de la agencia de referencia.

## Primera dirección de MEE

- Primera pantalla: mensaje de entrada de gran tamaño, poco texto y acceso a explorar. El titular actual es provisional; el ZIP histórico contiene varias frases candidatas, sin aprobación final.
- Segunda pantalla: siete cuadros de imágenes originales y una pieza de cierre; mosaico de tres columnas en escritorio, dos en tableta y una en móvil. El titular entra en secuencia, los cuadros aparecen al llegar al scroll y el foco o hover da movimiento sutil a cada imagen.
- Interior: titular e imagen al mismo nivel visual, índice sticky con tema activo señalado durante la lectura y capítulos que aparecen al llegar a ellos, sin repetir plantillas de cartera de clientes.
- Dos colores vivos inspirados en Cuba: azul `#1547BB`, rojo `#EF383E`; papel `#F7F6F2` y tinta `#15171B`. Valores de la primera versión del kit de marca para pantallas.
- Identidad de pantalla: MEE compacto e inclinado con Archivo Black Italic y estrella roja de ocho rayos, dibujada como isotipo. La dirección procede de la cabecera que el fundador prefirió frente al logotipo anterior. Variantes de contorno SVG y PNG/WebP en `brand-kit/` desde la raíz del proyecto; los activos usados en la web están en `public/brand/` y el favicon en `app/icon.png`.

## Activos disponibles

Siete escenas surrealistas originales, una por categoría, en `public/images/areas/<slug>.jpg` de 1254 × 1254 px y `<slug>-680.jpg` de 680 × 680 px. Los originales generados están fuera de esta carpeta en `generated_images/`; las copias de producción optimizadas ocupan juntas unos 3,5 MB. Las imágenes se entregan con texto HTML superpuesto; no llevan letras incrustadas.

| Área | Metáfora visual inicial |
| --- | --- |
| Educación y Valores | Libro convertido en escalera hacia un horizonte |
| Tribu | Personas reunidas alrededor de una luz común |
| Comunidad | Puentes entre viviendas alrededor de un patio |
| Trabajo | Construcción de herramientas sostenida por una mano |
| Capitalismo Consciente | Árbol vivo dentro de un maletín |
| Economía Compartida | Dos manos sostienen un recurso compartido |
| Política y Economía | Foro circular y arquitectura de decisiones |

**Revisión de arte:** comprobar a 360, 390, 768, 1024 y 1440 px los puntos focales y si el texto conserva contraste. La escena de Tribu muestra cuerpos azules próximos; confirmar que representa bien la visión inclusiva de tribu del fundador. Cualquier ajuste creativo a imágenes debe volver al proceso de generación/edición de imagen. No sustituir las imágenes por referencias ajenas descargadas.

## Responsive y acceso

- Móvil hasta 640 px: una columna, titular sin recorte, hero cuadrado e índice que permite desplazamiento horizontal con teclado.
- Tableta 641–900 px: dos columnas; el índice sigue utilizable y el contenido no depende de hover.
- Escritorio desde 901 px: tres columnas y cabecera de interior en dos bloques.
- `picture` envía la variante pequeña en móvil; las imágenes de áreas que quedan debajo de la primera fila se cargan al llegar a ellas. Tamaño intrínseco fijado para evitar saltos.
- Contraste, texto alternativo en imágenes informativas, títulos legibles, foco visible, movimiento reducido y funcionamiento sin animaciones son requisitos de aceptación.
- El movimiento es progresivo: el contenido se lee sin JavaScript; al solicitar movimiento reducido se desactivan entradas, desplazamientos y transiciones. El navegador puede animar el cambio entre páginas si admite View Transitions.
- Antes de publicar comprobar presupuesto de datos real en red lenta: las siete imágenes juntas no deben cargarse de golpe en una conexión limitada.

## Tipografía

La web usa Archivo Black para encabezados (italización según el contexto) y Manrope variable para cuerpo y navegación. Son fuentes gratuitas OFL alojadas en `public/fonts/` como subconjuntos WOFF2 latinos; los TTF completos y sus licencias se entregan en el kit. El logo usa contornos independientes del renderizado de fuente del navegador. Ver `GUIA-MARCA.md` del kit para colores, variantes y tamaños.
