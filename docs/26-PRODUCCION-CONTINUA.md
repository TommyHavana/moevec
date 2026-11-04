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

WordPress: **793/840 terminadas, 2379 imágenes originales públicas, 0 borradores y 47 pendientes**. Último bloque **796–798 / E2.5.01–03**, posts 4511/4516/4521. Tribu → Agradecimiento **3/15**. HTTP200, H1, canonical, indexabilidad, Article, tres WebP con alt y hash, categorías, etiquetas, enlaces internos, jerarquía, BreadcrumbList y sitemap comprobados. Una publicación y tres adjuntos por ID; taxonomía122/7. Advertencia SEO conocida: dos meta descripciones idénticas, sin modificar el tema. No se acredita indexación efectiva en buscadores.

- 796: Mauss, PDF106p conservado, introducción/método, dar/recibir/devolver y conclusiones parciales mediante Graz. Mezcla de obligación/libertad; no atribuirle la postura de MEE. Smith TMS, II.I e II.II parciales: beneficencia libre y censura de ingratitud compatibles, distintos de justicia. Título normativo no cancela contratos o préstamos aceptados. Dos casos propios hipotéticos.
- 797: Emmons/McCullough2003, resumen y método1:201iniciales/192analizados, no N de tres experimentos. Dickens2017 ficha autoral, cuerpo403 no leído. Choi y otros PNAS2025, resumen/introducción/resultados iniciales por web:145trabajos/163muestras/24804participantes/28países, g=0,19, IC95[0,15;0,22]; no19%mejora ni todosRCT. Efectos medios pequeños, sin obligación emocional o tratamiento. PNAS posterior barrera de cookies; no bypass ni afirmar lectura íntegra.
- 798: Read1958, pasajes del lápiz/cooperación, ensayo histórico y no censo actual de fabricante; millones atribuidos al autor. Hayek1945 inicio sobre conocimiento disperso, lectura parcial. OIT/UNICEF, resultados2024 publicados11/06/2025, presentación leída, sin acusación sobre fabricante de Read. Reconocimiento compatible con crítica. Nueve originales finales y mosaico WebP vistos.

VPS `/data/mee-backups/produccion-840-incremento-796-798-20261104`: SQL30322806B,66derivados en archivo2811269B;253incrementos más base. Hashes y miembros verificados, sin nueva prueba de arranque de restauración. ZIP local incremental y copia privada acreditados por la prueba externa `../mee-backups/produccion-796-798-entrega-20261104.json`; conservar toda la cadena.

Continuar **799–801 / E2.5.04–06**, Tribu → Agradecimiento. Briefs y nueve prompts conservados, **0/9 imágenes**. No reinitializar carpetas ni regenerar lo existente.

- 799/E2.5.04: `body-draft.html`1007palabras, apertura50 y FAQ49/50/49, dos ejemplos hipotéticos. Fuente revisada: Seligman y otros2005, revisión final autoral22abril2005, PDF19p453187B; leídos resumen, método y resultados PDF7–9, discusión10–11.577iniciales/411completaron seguimientos; visita=carta más entrega presencial. Mejoras al mes, no tres meses; no trasladar seis meses de otros ejercicios ni afirmar que agradecer específicamente supera siempre al gracias genérico. Muestra voluntaria web, lectura parcial, no tratamiento ni programa laboral obligatorio. Montaje de fuentes/enlaces, imágenes y revisión final pendientes.
- 800/E2.5.05: `body-draft.html`1081palabras, apertura52 y FAQ51/50/51, dos emprendedores hipotéticos. F050 es Frankl, no Tal Ben-Shahar. Reproducción primaria del pasaje de segunda parte sobre búsqueda de sentido, Panarchy, HTML37407B; ficha Beacon contexto, no libro íntegro. Emmons2003 resumen/método1, copia con procedencia y hash. Compatibilidad normativa MEE, sin prometer estabilidad sin ansiedad, éxito o mayores ingresos. Montaje, imágenes y revisión final pendientes.
- 801/E2.5.06: fuentes y notas conservadas, sin texto ni imágenes. Granma presupuesto29jul2026 leído como comunicación del ministro, no ley íntegra o auditoría; evitar número/año legal y cifras sin contrastar. Granma2abril2015 testimonios de deuda con Chávez y deber de apoyo a Venezuela, no prueba de obligación general por educación/salud cubanas. Opinión Defensores de la vida15jun2025 leída, no decreto; reconocer su defensa de médicos, carencias y lenguaje agradecidos/desagradecidos sin imputar coacción a cada firmante. Freedom in the World2026Cuba: Overview, hechos2025 y aviso de edición abreviada leídos; contexto de restricciones, no prueba causal de gratitud forzada. Seleccionar/delimitar fuente central o retirar generalización antes de redactar. F039Bastiat pendiente de lectura para esta pieza.

**Capacidad:** medida 194281472B a 2026-11-04T09:22:00.631590+00:00. Por debajo del umbral operativo209715200B(200MiB) antes de generar. No se ha llamado a image_gen para799–801; no existe error de cuota de imágenes de este bloque. Conservar originales y copias, sin borrarlos para hacer espacio. Reanudar portada799 cuando haya al menos200MiB y margen para copias. Los dos borradores y tres expedientes locales no cuentan como terminados ni borradores WordPress.

501/512/649/707/769 siguen retenidos por título, sin publicación ni aprobación específica. Preguntas ya enviadas: no repetir ni interpretar silencio como aprobación. Siguiente bloque después de799–801:802–804. Seguimiento del mismo chat activo cada tres minutos, sin procesos duplicados.
