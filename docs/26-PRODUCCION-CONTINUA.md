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

WordPress: **790/840 terminadas, 2370 imágenes originales públicas, 0 borradores y 50 pendientes**. Último bloque **793–795 / E2.4.13–15**, posts 4496/4501/4506. Tribu → Transmisión de Valores **15/15**. HTTP 200, H1, canonical, indexabilidad, Article, tres imágenes con alt y hash, categorías, etiquetas, enlaces y sitemap comprobados. Advertencia SEO conocida: dos meta descripciones idénticas; tema sin modificar.

- 793: Whitebread/Bingham 2013, reproducción primaria del informe, PDF 34 páginas, leídas introducción y pasajes 20–21/24. Revisión de estudios, no ensayo del plan doméstico ni hábitos irreversibles a siete años. Marco UE/OCDE 2023, páginas 6–10 por web; grupos 6–10/11–15/16–18 separados de los cuatro tramos propios de MEE. Sin mayoría de edad universal ni requisitos de contratación nacional inventados.
- 794: Mill, capítulos I/II, pasajes sobre madurez y argumentos contrarios; páginas 67–69 de la edición conservada, no otra paginación. Referencia filosófica, no protocolo clínico. Artículo propio E1.3.15 leído; conversación voluntaria y límites, sin promesa de conversión política.
- 795: OCDE 2024, resumen, definición y autoempleo por necesidad; datos de 2022, 13,8% de ocupados nacidos fuera y 13,4% de ocupados nativos, promedio de 37 países. No proporción de todos los migrantes ni éxito o virtud. Ficha/índice Portes/Stepick 1993, sin libro íntegro. Besley/Coate/Loury 1993, resumen/inicio 792–793, modelo y posibilidad de incumplimiento. OCDE 2025 revisada como contexto; 2026 anunciado para 12 de noviembre, todavía futuro al consultar. Nueve originales y mosaico vistos.

VPS `/data/mee-backups/produccion-840-incremento-793-795-20261104`: SQL 30225859 B, 66 derivados en archivo de 3340695 B; 252 incrementos más base. Hashes y miembros verificados, sin nueva prueba de arranque de una restauración. Completar ZIP local incremental y copia privada antes de seguir.

Continuar **796–798 / E2.5.01–03**, Tribu → Agradecimiento: briefs y nueve prompts conservados, **0/9 imágenes y textos pendientes**. Investigación preliminar: Mauss, fuente UQAM identificada y lectura inicial del PDF por web (introducción, regalos aparentemente voluntarios y realmente obligatorios); descarga de otra reproducción 406 excluida. Smith TMS Gutenberg copiado: pasaje beneficencia libre frente a justicia y censura moral releído, lectura parcial. Emmons/McCullough 2003 PDF 13 páginas conservado; resumen y método del primer estudio leídos (201 iniciales, 192 analizados, diez informes semanales), no todos los métodos/resultados todavía. Dickens 2017 ficha editorial/autoría, cuerpo 403, no fingir lectura. PNAS Choi y otros 2025: resumen e introducción leídos por web, 145 trabajos/163 muestras/24804 participantes/28 países, g=0,19; no 19% de mejora. Aperturas posteriores devuelven barrera de cookies, sin intentar resolverla. Read 1958 y OIT/UNICEF estimaciones 2024 publicadas en 2025 conservados, cuerpo por leer; Hayek 1945 copiado. Después 799–801.

Comprobar al menos 200 MiB antes de cada generación y margen proporcional para copias. Último espacio medido 360394752 B, fluctuante; no borrar originales o copias.

501/512/649/707/769 siguen retenidos por título, sin publicación ni aprobación específica. Preguntas ya enviadas: no repetir ni interpretar silencio como aprobación. Conservar toda la cadena de copias. Seguimiento del mismo chat activo cada tres minutos.
