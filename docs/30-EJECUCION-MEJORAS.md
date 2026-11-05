# Mejoras ejecutadas de MEE · 05/11/2026

Encargo expreso posterior a la auditoría: «Ejecuta todo lo que puedas». Esta entrega aplica el paquete de navegación, transparencia editorial, recursos, controles y preparación social. Conserva los 840 artículos y 2520 originales.

## Publicación y comprobaciones

- Producto desplegado en Coolify desde `0ae5f32aa73fdcedce8b6c571332cb070c937f38`, despliegue `2e301d37-0dc6-40b9-ac39-4883353e44c1`, terminado. El commit `72152480` incorpora los comandos npm de verificación; los cierres posteriores añaden mantenimiento, material social y evidencias.
- WordPress comprobado a las 17:19 UTC: 840 artículos, 2520 originales, 122 categorías, 0 borradores y 0 errores de metadatos/archivos. Registro MD/CSV/JSON sincronizado a las 17:23:30 UTC: 840 terminadas, 0 en curso, 0 pendientes y 0 maquetas públicas.
- `npm run verify`: compilación y TypeScript correctos; 23 HTML exportados comprobados, incluidos los errores esperados. PHP propio comprobado sin errores de sintaxis.
- GitHub Actions está disponible. Primer control correcto: [ejecución 42071768087](https://github.com/TommyHavana/moevec/actions/runs/42071768087). Se corrigió la omisión inicial de los scripts npm en el commit. Workflow con verificación de cambios y comprobación pública diaria a las 07:15 UTC; un fallo genera el resultado de error de GitHub, sin mensajes periódicos en el chat.
- 17 rutas públicas críticas: 0 fallos. 59 archivos de categorías vacías: 0 salidas sin contexto y todos siguen noindex. 40 artículos modificados: H1, SEO, canonical, schema e imágenes comprobados, sin fallos. Las 120 imágenes renderizadas de esas entradas conservan el alt y responden correctamente. Los nueve números internos se retiraron.
- Tres XLSX y cuatro tarjetas de rutas: HTTP 200 y SHA256 idéntico al archivo local. Sitemap principal con 20 URLs, incluidas método editorial y recursos. 404 devuelve 404 con una única directiva robots `noindex`.
- Los servicios web, WordPress y MariaDB están saludables con sus comprobaciones de salud activas. IDs tras desplegar: web `e056745cac54`, WordPress `aca3c4af1c28`, DB `b0648c9f294a`.

La búsqueda no indexable no exige descripción SEO. El verificador se ajustó a ese criterio y mantiene comprobación de exclusión. No se falsearon puntuaciones de Rank Math ni fechas de revisión del contenido.

## Estado por mejora de la auditoría

| ID | Estado y resultado |
|---|---|
| A01 | Parcial. Retirada la referencia obsoleta a muestras; faltan datos reales del responsable y conservación. Lista precisa en documento 32. |
| A02 | Publicada. Rutas antes del mosaico, beneficio práctico y enlace principal a elegir ruta. En la prueba móvil solicitada de 390 px, el bloque pasa de unos 4203 px a unos 888 px. |
| A03 | Publicada. Los 59 nodos conservan su jerarquía y ofrecen lecturas del padre con aviso de alcance. Las áreas enlazan al contexto disponible. |
| A04 | Primera selección aplicada. Continuaciones entre las 18 lecturas de rutas, dos dimensiones de libertad académica y doce relaciones adicionales revisadas. La falta de enlaces entrantes desde otros cuerpos baja de 328 a 311. Las 311 propuestas restantes están ordenadas para revisión, no incorporadas automáticamente. Esto no significa páginas huérfanas. |
| A05 | Publicada. Fecha de publicación, revisión acreditada y método editorial enlazado. Nueva página explica fuentes, firma Anacleto, herramientas de IA, ejemplos conceptuales y correcciones. |
| A06 | Preparación hecha; conexión pendiente. Inventario de cuentas sin perfiles inventados. Chrome no pudo operar y el control nativo confirmó que el Mac estaba bloqueado; no se pudo verificar la sesión personal de Facebook. |
| A07 | Preparada. Contrato de cinco eventos, parámetros UTM y guía de Search Console. El fundador mantiene las conexiones de analítica y la decisión de tratamiento. Sin emisor ni recogida nueva de tracking. |
| A08 | Copias y ensayo aislado en VPS: ver el apartado de recuperación. Falta destino cifrado fuera del VPS y ensayo en otra infraestructura. |
| A09 | Publicada. Se aceptan `editorial`, `Propuesta editorial`, `Consulta editorial` y `correccion`; se preselecciona Consulta editorial. Validación vacía: cuatro errores y foco correcto, sin correo enviado. |
| A10 | Publicada. Nueve filas de producción retiradas, preservando el resto del texto, títulos, slugs y los tres originales. |
| A11 | Publicada. Una directiva noindex en 404; búsqueda rastreable con noindex para que el buscador pueda leerla. |
| A12 | Publicada. Cuatro tarjetas gráficas originales a partir de la identidad existente, una por ruta y otra para el índice. SVG editables conservados; vista previa en redes pendiente de conexión. |
| A13 | Publicada. Tres entradas a rutas, selector de 56 temas en siete grupos y filtros en un desplegable. Primera tarjeta móvil a unos 789 px, frente a unos 1001 px en la auditoría. Paginación y búsqueda conservadas. |
| A14 | Publicada. Tres recursos: presupuesto mensual, práctica con diez funciones y comparación de decisiones. Ejemplos ficticios, fórmulas y cambios de entradas verificados; página de instrucciones y enlaces desde tres artículos. |
| A15 | Operativa. Calendario de 840 revisiones acreditadas y fechas siguientes propuestas. Pantalla Herramientas → Revisión editorial; responsable editorial, desencadenante y alcance. No constituye una nueva revisión de hechos. |
| A16 | Enlaces cruzados aplicados entre autonomía académica y financiación/intervención. Conservar páginas diferenciadas; evaluar consultas reales antes de hablar de canibalización. |
| A17 | Flujo aclarado. Producto se edita en mee-web y se publica desde el espejo privado con cambios acotados. Se conservaron siete variantes de imagen previamente optimizadas. Archivo binario separado o migración de historial pendientes de diseño y restauración. |
| A18 | Operativa. Puerta local, workflow real de CI, revisión pública diaria y salud de los tres servicios. En caso de fallo, revisar el estado del workflow y el servicio afectado. |
| A19 | Procedimiento documentado: fuente oficial, versión/hash, copia, prueba aislada, despliegue y rollback. Permisos protegidos de plugins conservados. CSP sigue en modo informe hasta comprobar todos los flujos administrativos. |
| A20 | Pruebas de interfaz realizadas en 320/390 px y formulario sin envío; no hay desbordamiento en las vistas probadas. Sin nueva puntuación Lighthouse ni métricas de campo; rendimiento real y evaluación accesible completa siguen abiertos. |
| A21 | Ejecutada. Punto de entrada breve sustituye instrucciones contradictorias; historia íntegra archivada, sin borrar las fuentes antiguas. |
| A22 | Diferida por dependencia. RSS y marcas locales siguen disponibles; boletín requiere proveedor, consentimiento, baja y operación real. |
| A23 | Diferida por dependencia. Red Phoenix, tienda y cobros necesitan sus datos y servicios propios; no se presentan como operativos. |
| A24 | Material de pantalla preparado: avatar, cuatro tarjetas, doce ideas con copias por canal, guiones y secuencias, y tres carruseles completos (12 PNG, SVG editables, alt y guiones SRT). No se han creado cuentas ni programado o publicado piezas sociales. |

## Integridad editorial y recursos

Las actualizaciones se aplicaron con `scripts/apply-editorial-maintenance.php`: CLI, una publicación existente por ID, hash previo, sustituciones exactas, copia privada y transacción con reversión ante error. No crea artículos ni medios y comprueba título, slug e IDs de imágenes después de guardar. Motivo: presentación, recursos y continuidad; no nueva comprobación de hechos. Recibo en `editorial/maintenance-2026-11-05/publication.json` y originales anteriores locales por ID.

Las hojas se crearon con el runtime de artefactos, recalcularon y renderizaron. Presupuesto: saldo previsto 620 y registrado 520 u.m.; al añadir 100 de gasto baja a 420. Práctica: total 103, al cambiar 8 cuadernos por 10 pasa a 112. Comparación: 3,10/3,40; una entrada ausente muestra información pendiente. Se corrigieron encabezados y alineación tras inspección visual. No se ha realizado una prueba de cada aplicación compatible con XLSX.

## Recuperación y copias

Ensayo terminado correctamente a las 17:28:37 UTC: 18 tablas y 840 entradas completas restauradas; portada del blog y dos artículos respondieron con un H1. Los contenedores, red y volúmenes temporales se retiraron. El ensayo de restauración y su informe se conservan en `/data/mee-backups/mejoras-20261105/restore-test/`. SQL y archivo de WordPress permanecen privados en el VPS; no se descargan. El informe público de verificación contiene solo recuentos, hashes, tamaños y resultados. La restauración usa red interna sin puertos publicados y credenciales temporales distintas de producción. La primera prueba detectó que el usuario de PHP no podía leer la credencial temporal del clon; se ajustó exclusivamente ese archivo y se repitió el ensayo con los mismos snapshots. Consultar `inventario/mejoras-2026-11-05/restore-report.json` para el resultado definitivo; no confundir el mismo VPS con respaldo externo.

Antes del cambio se creó una copia proporcional local con CRC correcto y se conservaron las variantes de imagen anteriores. Las evidencias y el material nuevo se guardan en ambas fuentes y en el repositorio privado. El inventario de esta entrega no contiene secretos, bases de datos ni conversaciones privadas.

## Continuidad exacta

La producción de 840 entradas permanece cerrada. No reactivar su automatización. Prioridades siguientes: datos jurídicos y conservación reales, acceso a perfiles existentes para vincular/publicar las piezas preparadas, conexión de Search Console/analítica por el fundador y respaldo externo cifrado. La revisión gradual de las 311 propuestas de enlaces continúa siendo trabajo editorial; no contarlas como enlaces publicados. Los proyectos de tienda, red y boletín conservan sus dependencias específicas.

Evidencia: `inventario/mejoras-2026-11-05/`; material social: `editorial/social/`; calendario: `editorial/review-schedule.json`. La documentación técnica consultada incluye [metadatos de Next.js](https://nextjs.org/docs/app/api-reference/functions/generate-metadata), [workflows de GitHub](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) y [variables de MariaDB con secretos en archivo](https://mariadb.com/docs/server/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/mariadb-server-docker-official-image-environment-variables).
