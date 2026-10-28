# MEE · punto de entrada para Codex

## Qué se ha recibido

`fuentes/claude/` contiene **íntegra** la entrega `mee-proyecto.zip` facilitada por el fundador: proyecto, taxonomía, debate, ejemplos económicos, naming, material de logo y arquitectura anterior. Su `AGENTS.md` original también tiene una copia llamada `AGENTS-ARCHIVO.md` para dejar claro que es histórico. **No editar esa carpeta ni seguir sus instrucciones antiguas de prioridad y WordPress:** prevalecen el `AGENTS.md` de la raíz y las decisiones actuales del fundador.

La fuente editorial primaria es `fuentes/claude/docs/02-taxonomia.md`. La representación para React, `content/taxonomia.json`, se obtiene ejecutando `node scripts/sync-taxonomy.mjs`. Un cambio de taxonomía se hace primero en una **copia de trabajo aprobada** de la fuente, nunca inventando etiquetas directamente en JSX ni alterando el archivo histórico.

## Qué decidió el fundador después de aquel ZIP

1. React y WordPress están publicados. El fundador autorizó la auditoría integral, contacto y maquetas el 28/10/2026. Consulta el informe 22 y el último estado; la tienda sigue fuera de este encargo.
2. Portada de alto impacto y mosaico gráfico de las siete categorías; interiores narrativos con navegación superior fija por subcategorías. Referencia visual: https://turnerduckworth.com/; imágenes y textos originales.
3. Paleta viva de azul y rojo inspirada en Cuba sin reproducir literalmente su bandera. La versión de marca para pantallas vive en `brand-kit/` (SVG, PNG, WebP, tipografía y guía). Es una reconstrucción de la variante preferida que todavía se revisará con el fundador para usos fuera de pantalla.
4. Sin Git, sin GitHub Actions y sin despliegue. Todo vive en esta carpeta del ordenador.
5. WordPress editorial en `https://moevec.org/blog/`, con Hello Elementor y tema hijo MEE. El ZIP histórico proponía Astra y `/lab`; el fundador eligió y autorizó la ruta `/blog/`. En local, React usa `localhost:3000` y WordPress se preparó para `localhost:8080`.
6. WooCommerce para vender imágenes de obra de diseñadores cubanos y anticomunistas será una fase posterior; no hay catálogo ni autorizaciones todavía.

## Orden de lectura

`AGENTS.md` → este documento → `01-VISION-Y-PUBLICO.md` → `02-MAPA-DE-CONTENIDOS.md` → fuente original `fuentes/claude/docs/02-taxonomia.md` → `03-EDITORIAL-CATEGORIAS.md` → `11-PRESENTACION-CATEGORIAS-Y-SUBCATEGORIAS.md` → `04-ARQUITECTURA-REACT.md` → `05-DISENO-Y-ASSETS.md` → `06-PLAN-REACT.md` → `07-CRITERIOS-EDITORIALES.md` → `08-VERIFICACION-Y-ENTREGA.md` → `09-WORDPRESS-DESPUES.md` → `10-DECISIONES-ABIERTAS.md`.

Para continuar, lee primero `15-ESTADO-Y-CONTINUIDAD.md` y `16-BACKLOG-REACT.md`. Los nuevos requisitos están en `13-REQUISITOS-VISUALES-Y-MOVIMIENTO.md`; arquitectura recomendada en `14-ARQUITECTURA-EDITORIAL-Y-TIENDA.md`. La auditoría total del documento 18 espera petición expresa. Usa `../prompts/INICIO-CODEX.md` para abrir la sesión y el documento 20 para cerrarla.

## Precisión y estado

Los nombres y jerarquía de categorías proceden del material del fundador. Los resúmenes, beneficios, primeras piezas y textos de interfaz propuestos en este paquete son **redacción editorial nueva para revisar**. Las imágenes son originales generadas para una primera dirección, no arte final aprobado. No publicar afirmaciones históricas, legales, médicas, financieras o sobre personas sin revisión y fuentes primarias.

## Requisitos añadidos el 28/10/2026

Cada categoría y subcategoría tendrá imagen y movimiento que evoque su valor. Hay 63 nodos visuales principales y 59 internos políticos; ver inventario 19. Se recomendó React + WordPress + WooCommerce, pero falta decisión final. La auditoría total está expresamente diferida. Las rutas del ordenador son `~/Documents/Proyectos/mee/mee-web`; la documentación portable no traslada ni duplica el código.

## Actualización de despliegue del 28/10/2026

Las decisiones antiguas de esta guía sobre no usar Git, no publicar y aplazar WordPress fueron sustituidas por la petición posterior del fundador. React está publicado en `moevec.org/` y WordPress editorial en `moevec.org/blog/`, con Hello Elementor, tema hijo MEE y una fuente privada de despliegue en `../mee-deploy-source/`. La carpeta de trabajo sigue siendo `mee-web/`. GitHub Actions no está disponible durante tres días y no es necesario para construir desde Coolify. El estado exacto se registra en `15-ESTADO-Y-CONTINUIDAD.md`; la auditoría integral ya se encargó y se documentó en el informe 22; WooCommerce sigue pendiente de encargo.
