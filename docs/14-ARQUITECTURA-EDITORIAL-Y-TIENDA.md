# Arquitectura editorial y tienda · propuesta, no migración ejecutada

## Recomendación dada al fundador

Continuar con Next.js/React para la experiencia gráfica; WordPress para contenido editorial; WooCommerce para la futura venta de arte. Se considera la solución recomendada, **pendiente de decisión final**. No hay WordPress operativo ni tienda instalada. El fundador pidió conocer esta opinión antes de solicitar una auditoría total; el paquete no convierte esa recomendación en autorización para implementar la tienda ahora.

| Responsabilidad | Propuesta |
| --- | --- |
| Portada, categorías y escenas de subcategorías | Next.js/React con contenido y recursos propios. |
| Edición de textos, artículos y campos de contenido | WordPress; definir un contrato de datos antes de conectar. |
| Productos, variantes, pedidos, pago y descargas | WooCommerce. |
| Primera compra completa | Páginas de producto/carrito/checkout de WooCommerce con la identidad MEE. |
| Checkout enteramente en React | Posibilidad futura; no recomendado como primer alcance. |

## Estado técnico real

El Next.js existente usa `output: "export"` y `trailingSlash: true`. Genera páginas estáticas durante el build. Se puede consumir contenido de WordPress en compilación; los cambios necesitan regenerar la exportación. Si se necesita revalidación, sesión de servidor o funciones de backend en Next, habrá que revisar el despliegue y el modo de ejecución. Ninguna de esas funciones está implementada por este paquete.

El diseño se organizará con datos estables para que más adelante el contenido deje de depender de archivos locales sin rehacer toda la composición. Para WordPress son posibles los tipos de contenido y los campos expuestos por REST; ACF es una opción de edición, no una dependencia ya elegida para cada campo. Elementor puede servir en páginas editoriales editables; las escenas especiales no se diseñarán dos veces, en React y en un constructor de páginas.

## Arte digital

Primera definición pendiente: venta de archivo descargable, impresión física o ambas. Por obra registrar autor autorizado, título, colección, miniatura pública, formato, dimensiones/resolución del archivo, licencia de uso, variantes, precio y entrega. Los archivos de venta se separan de las miniaturas públicas. WooCommerce admite productos virtuales/descargables, límites y caducidad de descarga; su protección debe configurarse y probarse en el servidor real. No colocar originales comerciales en `public/` de React.

Si también se venden impresiones, definir producción, tamaños, materiales, embalaje, envío y devoluciones antes de ofrecerlas. No inventar productos ni afirmar permisos de artistas. Las condiciones, impuestos y derechos se revisarán con información y asesoramiento adecuados al país de venta antes de publicar.

## Decisiones a resolver cuando llegue la fase

- Papel de WordPress: solo editorial, o también contenido de las páginas de categorías.
- Ruta editorial `/blog/` o `/lab/`, rutas de tienda y composición bajo el dominio. Son propuestas, no URLs finales.
- Padre/tema hijo y necesidad real de Elementor y ACF gratuitos; no introducir versiones de pago sin autorización.
- Galería de obra en Next o en WooCommerce; primera versión de compra en WooCommerce.
- Actualización de contenidos: recompilación explícita o Next con servidor y revalidación.
- Alojamiento, pagos y almacenamiento de descargas. El software libre no elimina costes de hosting o transacción.

## Secuencia propuesta

Definir modelo y sistema visual → validar piloto de movimiento → terminar React → abrir WordPress editorial local → montar WooCommerce local → probar contenido, compra y entrega de un producto de prueba → integrar navegación y publicación cuando se autorice. El momento de la auditoría lo decide el fundador de forma expresa.

## Referencias técnicas consultadas el 28/10/2026

- Next.js, exportación estática: https://nextjs.org/docs/app/guides/static-exports
- WordPress, tipos de contenido en REST: https://developer.wordpress.org/rest-api/extending-the-rest-api/adding-rest-api-support-for-custom-content-types/
- WooCommerce, Store API: https://developer.woocommerce.com/docs/apis/store-api/
- WooCommerce, productos virtuales y descargables: https://woocommerce.com/document/managing-products/virtual-downloadable/
- WooCommerce, entrega de descargas: https://woocommerce.com/document/digital-downloadable-product-handling/

Estas referencias respaldan capacidades de producto, no prueban que estén implementadas en MEE.
