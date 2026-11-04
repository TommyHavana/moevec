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


## Continuación exacta ·05/11/2026

WordPress: **802/840 terminadas,2406 imágenes originales públicas,0 borradores y38 pendientes**. Último bloque **805–807 / E2.5.10–12**, posts4556/4561/4566. Tribu → Agradecimiento **12/15**. HTTP200,H1,canonical,indexabilidad,Article,tresWebPconalt/hash/renderizados, categorías, etiquetas, BreadcrumbList, sitemap y enlaces internos existentes verificados. Una publicación y tres adjuntos porID;taxonomía122/7. Advertencia conocida de dos metadescripciones idénticas, tema sin cambios. No afirmar indexación efectiva ni restauración completa arrancada.

- 805: CAFAbout/comunicado2026 y metodologíaPDF10p164679B SHA92f448... consultados; resumen/método/límitesPDF2–5. WGR sucede al WGI, comparación directa desaconsejada por método/periodo. Donor pregunta2025 por encuesta2026. RutaPDFversion1/cuerpoVersion2 contiene incongruencia Charity fechas: no números ni comparaciones Charity publicados. No ranking de virtud, porcentajes ni recomendaciones de entidades. Singer presentación primariaYale, ficha paperback2016, no libro íntegro ni edición española leída.1012palabras,apertura49,FAQ46/46/51.
- 806: AmabileHBSentrevista2011 e investigación de diarios laborales238empleados7empresas; no ensayo30días emprendedores. Emmons2003resumen/método1PDF1/3–4releídos,10registrossemanales; copia primaria previa preservada y procedencia explícita. Treinta días/treslíneas son propuestaMEE, sin ventas/motivación/clínica garantizadas.1094palabras,apertura50,FAQ48/50/49. Interior1 corregido conimagegen dosveces: quitariconosajenos y ampliar márgenes; cincofilasseiscolumnascontadas,30celdascompletas enWebP1600x900. Descartesypromptsconservados.
- 807: FrohSefickEmmons2008PDF21p300824B SHA86796d... leídosresumen/métodoPDF5–10/resultadosydiscusiónPDF15–17.221adolescentes11clases, dossemanasescolares+seguimiento3semanas. Satisfacciónescolar favorablefrentegrupos, nula diferencia condiciónconductaprosocial; otrasvariablesdependecomparador. No evidenciafrascopreescolares, hitosuniversales, notaso saludprometida.1102palabras,apertura49,FAQ50/51/49.

Dos ejemplos hipotéticos y tresFAQ en cada entrada. Nueve nativos y mosaico final vistos; portadas1200×630/interiores1600×900, cadaWebP<250KB. Escenasficticias ymetáforas sin pacientes o entidades reales. Texto, fuentes, revisión yprompts conservados.

VPS `/data/mee-backups/produccion-840-incremento-805-807-20261105`: SQL30608083B,66derivados enarchivo3723462B;256incrementosmásbase. Hashesy miembrosverificados, sin nuevoarranque de restauración. ZIP incremental local y copia privada acreditados por `../mee-backups/produccion-805-807-entrega-20261105.json`;conservar toda la cadena.

Continuar **808–810 / E2.5.13–15**, Tribu → Agradecimiento. Briefs y nueve prompts conservados, **0/9 imágenes y textos pendientes**; no reinicializar expedientes. 808 ChettyFriedmanRockoff2014AERparteII, PDFautoral77pidentificado/resumenleído; leer método/limitacionesantesafirmarresultados,no trasladardólares históricosactuales/Cuba.809 Hirschman1970fragmentocap8autorizado y fuentes primarias del debateE1.3.15localdisponibles, no libroíntegro.810Planoriginalexpresapolíticacomunidadpendiente; páginaactualSobreMEEconsultada4nov2026presentaredcomo futura. Escribir propuestaeditorial con consentimiento/verificación, sin murooperativo/puntos/perfiles/políticaaprobada o fechaactivación. Después811–813.

501/512/649/707/769 siguen retenidos por título, sin publicación ni aprobación específica. Consultas ya enviadas: no repetir ni interpretar silencio como aprobación. Seguimiento del mismo chat activo cada tres minutos, sin procesos duplicados.

Capacidad medida antes del cierre: 2957893632B. Comprobar200MiB(209715200B) antes de cada generación y margen proporcional para copias. Conservar todos los originales yrespaldos, sinborrados. Sin error de cuotaimagegen en este bloque.
