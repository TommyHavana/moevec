# Requisitos de imagen y movimiento · 28/10/2026

## Petición explícita

Cada categoría y subcategoría tendrá una imagen propia. Todas tendrán movimiento, y ese movimiento deberá evocar el valor o idea de su contenido. Se trata de un requisito del fundador, **todavía no implementado en las subcategorías**. La web debe aspirar a una ejecución gráfica y de interacción sobresaliente.

## Alcance y jerarquía

La interfaz actual presenta siete categorías y 56 secciones principales (9/6/4/12/8/7/10). Política y Economía añade 48 temas y once subtemas internos. Son 122 nodos contando las categorías. El inventario reserva identidad visual a todos; los primeros 63 tienen propuestas creativas iniciales. Los 59 internos no se eliminan ni se declaran cubiertos por una imagen del eje. Antes de producir esa segunda tanda se definirá cómo se presentan visualmente y qué profundidad de navegación necesitan.

## Qué significa movimiento con significado

Cada pieza tendrá una ficha con idea, metáfora, acción, inicio, desarrollo, final legible y versión quieta. Por ejemplo, Autonomía puede representar una pieza que construye su propio recorrido; Comunidad, puentes que llegan a conectarse; Trabajo, elementos que se transforman en una herramienta. Una entrada o zoom genéricos pueden acompañar la composición, pero no bastan para expresar el concepto de todas las piezas.

Las propuestas concretas de `19-INVENTARIO-VISUAL.md` no están aprobadas. En asuntos políticos y económicos la imagen explica el tema, sin convertir la postura editorial en una supuesta evidencia sobre resultados reales.

## Sistema propuesto

- Imagen base original con espacio pensado para la tipografía HTML; no incrustar nombres en el archivo.
- Plano principal, fondo y elementos separados cuando la escena necesite movimiento interno.
- Un verbo compartido por familia visual y una acción concreta para cada subcategoría.
- Usar CSS/SVG/Canvas o una biblioteca de animación según el prototipo; no elegir una dependencia por moda. Los clips breves quedan para escenas donde el movimiento no se pueda expresar de forma convincente con capas.
- Imagen de respaldo incluso cuando exista vídeo o render en tiempo real. PNG cuando se necesite transparencia; WebP/AVIF para las variantes web según pruebas. Los formatos del vídeo se elegirán al producirlo y probar navegadores.

## Comportamiento

Cargar primero lo visible; preparar lo cercano y pausar lo que queda fuera de pantalla. En móvil, usar activación por visibilidad o toque cuando corresponda. Evitar audio automático, movimientos que desplacen el contenido de lectura, destellos y scroll forzado que impida navegar. La versión con `prefers-reduced-motion` conserva el significado en una composición quieta. Cuando un movimiento continuo lo requiera, ofrecer control de pausa.

## Producción por etapas

1. Piloto de una categoría y dos subcategorías representativas; preparar storyboard, imagen quieta, capas y prototipo de movimiento.
2. Revisar dirección de arte con el fundador. El piloto no autoriza producir 122 imágenes sin validar su lenguaje.
3. Completar las siete categorías y 56 subcategorías principales por lotes, sin reutilizar una misma imagen como solución final de conceptos diferentes.
4. Desarrollar el tratamiento de los 59 nodos internos de Política y Economía y registrar su alcance.
5. Medir carga, fluidez y comprensión al integrar cada lote. La auditoría total sigue pendiente de petición expresa.

## Ficha mínima por pieza

ID estable; categoría y nodo; objetivo editorial; metáfora propuesta; acción y valor que comunica; guion; assets; encuadre móvil/escritorio; alternativa quieta; texto alternativo; estado de producción; procedencia/licencia; tamaños reales; resultado de pruebas; versión y fecha.
