# Verificación de React antes de pasar a WordPress

> Checklist para cambios y cierre React. No es la auditoría total ni una orden de ejecutarla: esa auditoría espera petición expresa del fundador, según el documento 18. Las casillas marcadas recogen comprobaciones históricas, no nuevas pruebas de esta entrega documental.

## Contenido y navegación

- [ ] Siete cuadros y siete rutas correctas, en el mismo orden que la fuente original.
- [ ] Temas 9 / 6 / 4 / 12 / 8 / 7 y diez ejes políticos; los temas internos de Política y Economía siguen en su eje correspondiente.
- [ ] Todos los enlaces del índice fijo apuntan a un `id` existente y el encabezado destino queda visible bajo la barra sticky.
- [ ] Enlaces entre áreas completos. Sin enlace editorial que conduzca a WordPress inactivo.
- [ ] Resúmenes y frases de beneficio revisados por el fundador; afirmaciones verificables sustentadas antes de publicar.

## Pantallas y accesibilidad

- [ ] Revisado a 360, 390, 768, 1024 y 1440 px: sin desbordamiento horizontal de toda la página ni recortes de título.
- [ ] Los cuadros conservan punto focal; el texto encima mantiene contraste suficiente.
- [ ] Se puede entrar y recorrer todo con teclado, y el foco permanece visible en el índice horizontal.
- [ ] Hay un h1 por página, salto al contenido, jerarquía de encabezados y texto alternativo razonable.
- [ ] Con imágenes desactivadas, siguen visibles categoría y enlace. Con movimiento reducido, la navegación sigue funcionando.
- [ ] Probado en móvil real y navegador de escritorio; verificar lector de pantalla cuando el diseño esté estable.

## Rendimiento y estructura

- [x] `npm install` completa y `package-lock.json` se guarda en la carpeta; actualizar el ZIP de respaldo.
- [x] `node scripts/sync-taxonomy.mjs` y `node scripts/sync-editorial.mjs` terminan sin errores.
- [x] `npm run build` termina; `out/index.html` y `out/areas/<slug>/index.html` para los siete slugs están presentes.
- [ ] Carga móvil en red limitada: imágenes posteriores no se descargan inmediatamente; revisar peso total transferido y tiempos observados, sin asumir resultados de esta máquina.
- [ ] Títulos, descripciones, idioma y enlazado interno correctos; revisar el logo integrado, favicon y contraste a tamaños reales.

## Estado verificado al preparar el paquete

Comprobados: ZIP de Claude leído, 7 categorías originales, 46 temas de teoría, 10 ejes de Política y Economía, 56 beneficios sincronizados, 14 imágenes, instalación de npm, compilación Next, validación de activos de marca y capturas previas a la integración de fuentes de la portada en Chrome a 1440 y 390 px. **Pendiente:** revisión visual con la nueva tipografía y de todas las rutas interiores, anchos adicionales, teclado, móvil físico y conexión lenta. El kit de marca de pantalla y el editorial siguen sujetos a revisión; PHP, Docker y WordPress no se han probado.

## Entrega local

Una carpeta `mee-web/` autocontenida y una copia ZIP sin `node_modules`, `.next`, `out`, contraseñas ni archivos de entorno privado. Guardar una nueva copia tras aprobar textos y diseño. Antes de añadir WordPress, revisar `10-DECISIONES-ABIERTAS.md`.
