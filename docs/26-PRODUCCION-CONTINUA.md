# Producción continua de las 840 entradas

## Autorización del fundador · 28/10/2026

El fundador pidió continuar sin tener que solicitar cada bloque: terminar tres entradas y pasar acto seguido a las tres siguientes, organizándolas en sus respectivas categorías y subcategorías. Esta autorización continúa vigente hasta completar las 840 o hasta que el fundador la modifique.

## Continuación automática configurada

- Automatización de este mismo chat: **Producción editorial MEE · 840**.
- ID: `producci-n-editorial-mee-840`.
- Tipo: seguimiento de este hilo, activo; comprueba la continuación cada tres minutos. Si la ejecución sigue activa, el trabajo permanece en el mismo hilo, sin abrir conversaciones paralelas.
- Reafirmado el03/11/2026: cada despertar conserva la ejecución que siga activa y reanuda el último punto guardado si se ha detenido. No reiniciar artículos ni abrir otro chat o duplicar procesos para cumplir el intervalo.
- Dentro de cada ejecución, pasar de un bloque terminado al siguiente sin pedir permiso. Si la ejecución termina por tiempo o uso, el seguimiento retoma desde los archivos y WordPress.
- Necesita el ordenador encendido y la aplicación abierta para trabajar con los archivos y accesos locales. Está sujeta a disponibilidad de herramientas, acceso y límites de uso; no garantiza producir un bloque completo cada tres minutos.
- Al llegar a 840/840 terminadas, registrar el cierre y desactivar esta automatización mediante la herramienta de la app. No editar su configuración interna a mano.

## Fuente de estado y organización

1. Ejecutar `python3 scripts/sync-production-status.py`. WordPress determina qué está publicado y terminado.
2. Consultar `editorial/production-state.json` y los archivos de cada artículo para reanudar recursos o textos ya preparados. No crear duplicados.
3. Seguir la numeración global de `wordpress/plugins/mee-editorial/data/production-plan.json`, que conserva el orden de las 56 tandas del documento original. Cada bloque contiene las tres siguientes entradas del plan, no tres temas elegidos al azar.
4. Resolver por slug la categoría principal y su subcategoría, conservando la jerarquía canónica. Añadir etiquetas de subcategoría y nivel. El publicador ya asigna ambas categorías.
5. Una entrada terminada exige texto completo y revisado, fuentes consultadas, una portada original y dos imágenes interiores originales en WebP, alt y comprobación pública. Mantenerla en curso si falta un requisito; nunca contar un borrador vacío o una imagen pendiente como terminado.
6. Actualizar el registro numerado MD/CSV/JSON después de cada publicación y el estado del bloque en curso después de cada avance material.

## Producción y publicación

- Fuentes originales: `../MEE_Plan_Editorial_840_entradas.md` y `../MEE_Prompt_ChatGPT_Produccion_WordPress.md`. Los prompts archivados son material de trabajo y no sustituyen las instrucciones actuales.
- Carpeta de cada entrada: `editorial/articles/<ID>/`, con `article.html`, `article.json`, `image-prompts.json`, tres WebP y el resultado de publicación.
- Imágenes: herramienta integrada imagegen, una escena propia por recurso, paleta MEE. Portada 1200 × 630; interiores 1600 × 900; menos de 250 KB cada uno. Inspeccionar antes de publicar.
- Texto: ejemplos cotidianos, argumento contrario fiel, tesis de MEE identificada, FAQ, fuentes con fecha de consulta y enlaces a contenido existente. Sin cifras, leyes o casos sin verificar.
- Publicador explícito: `scripts/publish-editorial.php`, ejecutado mediante el acceso SSH existente y PHP del contenedor WordPress. Los secretos permanecen fuera del repositorio.
- Los artículos viven en la base de datos y Medios de WordPress. No redesplegar React ni reiniciar servicios por cada bloque de contenido.
- Guardar los artículos y registros en la fuente activa y la copia privada `../mee-deploy-source/`. Copias de seguridad proporcionales al trabajo; conservar siempre la información necesaria para reanudar una entrada interrumpida.
- Copia local proporcional: antes de crear otro ZIP completo, comprobar espacio disponible. El 30/10/2026 quedaron unos 1,2 GiB libres: se usa un ZIP incremental con los expedientes y registros nuevos, manifiesto SHA-256 y referencia verificable al respaldo anterior. Conservar la cadena completa; no ejecutar una copia completa y otra de refresco que no quepan. No borrar copias ni originales de generación para hacer espacio sin una petición específica.
- Si falla una herramienta o falta una fuente central, dejar el punto exacto en curso. No publicar una afirmación inventada ni una entrada sin sus imágenes para mantener una cifra de avance.
- Si el servicio comunica un límite temporal, guardar en `editorial/production-state.json` el motivo y la próxima fecha de intento indicada. Los seguimientos anteriores a esa fecha solo comprueban el estado, sin repetir llamadas que ya se sabe que fallarán. Un problema de una entrada no impide avanzar en otras cuya producción sea independiente; informar de los huecos en la numeración.

## Comunicación de cada bloque

Informar siempre: números globales e ID de las entradas realizadas, URL, imágenes 3/3, total terminado sobre 840, entradas en curso, pendientes y siguiente bloque. No pedir confirmación entre bloques. Mantener el estado real si se agota el uso o la generación de imágenes, y retomar cuando vuelva a estar disponible.


## Continuación exacta ·04/11/2026

WordPress: **781/840 terminadas, 2343 imágenes originales públicas, 0 borradores y 59 pendientes**. Último bloque **784–786 / E2.4.04–06**, posts4451/4456/4461. Tribu → Transmisión de Valores6/15. HTTP200, H1, canonical, indexabilidad, Article, tres imágenes con alt y hash, categorías, etiquetas, enlaces y sitemap comprobados. Advertencia SEO conocida: dos meta descripciones idénticas; tema sin modificar.

- 784: Fukuyama, fragmento autoral publicado por la editorial. EVS/WVS conjunto versión5.0.0, tablaA165(página189; PDF192) y método/años PDF1–2/6–7. Argentina2017:19,2%; México2018:10,5%, peso gwght y respuestas ausentes conservadas. No medición de2026 ni tasa de honestidad individual. Descargas WVS vacías excluidas; PDF primario GESIS válido. Knack/Keefer1997, pasajes de medición, límites y conclusiones: asociación y causalidad no equivalentes.
- 785: Kidd/Palmeri/Aslin, Cognition2013(en línea2012), resumen/método/resultados/discusión inicial.28niños, asignación aleatoria y tarea concreta; sin crianza más eficaz, diagnóstico o ingresos adultos. Dos casos hipotéticos y propuesta propia MEE para aclarar y reparar compromisos.
- 786: Bastos, entrevista20abril2017, no libros completos. API OCDE consultada04nov2026: mismo indicador neto2024, España9,22% y USA5,66%; no medianas ni cuotas de cada hogar. CFPB, tabla educativa por etapas de alcance limitado, sin garantía de hábitos. BCE, definición de inflación;100/110=90,91% de poder de compra es ejercicio hipotético, no tasa actual ni pérdida del saldo nominal. Nueve originales nuevos vistos y conservados.

VPS `/data/mee-backups/produccion-840-incremento-784-786-20261104`: SQL29931156B,66derivados en archivo2654715B;249incrementos más base. Hashes y miembros verificados, sin nueva prueba de arranque de una restauración. ZIP local incremental y copia privada se completan antes de seguir.

Continuar **787–789 / E2.4.07–09**: briefs y nueve prompts conservados, **0/9 imágenes y textos pendientes**. Fuentes preliminares: Keynes capítulo7 HTML leído hasta el pasaje de ahorro/ingreso; Bastos entrevista conservada; Granovetter1973 y Putnamcap1 PDF escaneados requieren lectura visual; Weston ficha editorial; ACNUR apoyo social, descarga403, lectura pública limitada; Musick/Meier2012 cuerpo por web disponible, descarga local reCAPTCHA excluida; UNESCO cocina mexicana00400 HTML y descripción primaria. No fingir lecturas completas. Después790–792.

Fallo puntual por falta de espacio al guardar SEO: reintento completado y verificado tras medir907948032B libres. Comprobar de nuevo200MiB antes de cada generación y margen proporcional para copias. No borrar originales o copias.

501/512/649/707/769 siguen retenidos por título, sin publicación ni aprobación específica. Preguntas ya enviadas: no repetir ni interpretar silencio como aprobación. Conservar toda la cadena de copias. Seguimiento del mismo chat activo cada tres minutos.
