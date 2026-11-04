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

WordPress: **796/840 terminadas,2388 imágenes originales públicas,0 borradores y44 pendientes**. Último bloque **799–801 / E2.5.04–06**, posts4526/4531/4536. Tribu → Agradecimiento **6/15**. HTTP200, H1, canonical, indexabilidad, Article, tres originales con alt/hash/renderizados, categorías, etiquetas, jerarquía, BreadcrumbList, sitemap y enlaces existentes comprobados. Una publicación y tres adjuntos porID; taxonomía122/7. Advertencia conocida de dos meta descripciones idénticas; tema sin modificar. No se acredita indexación efectiva ni restauración completa arrancada.

- 799: Seligman y otros2005, revisión final autoral22abril2005, PDF19p453187B, leídos resumen yPDF7–11método/resultados/discusión.577baseline/411completaron seguimientos. Visita=carta más entrega presencial; mejoras al mes, no tres meses; no seis meses de otros ejercicios trasladados a carta. Muestra voluntaria web; criterio de reconocimiento concreto propuesto porMEE, no superioridad universal demostrada. Dos ejemplos hipotéticos.1007palabras principales,apertura50,FAQ49/50/49.
- 800: Frankl, extracto de segunda parte sobre búsqueda de sentido en reproducción Panarchy; ficha Beacon como contexto, no libro íntegro. F050esFrankl, noTalBenShahar. Emmons2003 resumen/método1, no evidencia de conformismo justo ni gratitud que cure ansiedad o garantice éxito. Compatibilidad normativa MEE. Dos emprendedores hipotéticos.1081palabras,apertura52,FAQ51/50/51.
- 801: acotada la afirmación central antes de escribir; no se afirma deuda legal por educación/salud ni coacción de todos los agradecimientos. Granma2abril2015 testimonios sobre deuda conChávez/deber de apoyo aVenezuela, no decreto; opinión15jun2025 reconocecarencias/defiende médicos, no sanción acreditada. Presupuesto29jul2026 comunicación de declaraciones delministro, sin cifrasoLey181/2026 sin contrastar norma íntegra. BastiatIIIImpuestos leído en copia primaria yWikisource177–204; reconoce servicios útiles ycostesalternativos. Bastiat.org abre en bucle, nueva copiaWikisource200257796B conservada; no libro íntegro. FH2026Overview/hechos2025/ediciónabreviada, contexto de disenso yno motivos individuales.1123palabras,apertura52,FAQ51/52/48. Dos casos hipotéticos.

Nueve imágenes originales finales y mosaico WebP vistos; portada1200×630/interiores1600×900, cada archivo<250KB. Sin texto legible, marcas, emblemas oficiales o personas reales identificadas. Prompts y trazabilidad de nativos en cada expediente.

VPS `/data/mee-backups/produccion-840-incremento-799-801-20261104`: SQL30419635B,66derivados en archivo3845772B;254incrementos más base. Hashes y miembros verificados, sin nueva prueba de arranque de restauración. ZIP local incremental y copia privada acreditados por `../mee-backups/produccion-799-801-entrega-20261104.json`; conservar toda la cadena.

Continuar **802–804 / E2.5.07–09**, Tribu → Agradecimiento. Briefs originales y nueve prompts nuevos conservados, **0/9 imágenes y textos pendientes**. No reinicializar carpetas. Preparación de investigación:802 Grant/Gino2010 PDFautorWharton identificado, no ensayo de retención de clientes; declaración primaria Grant enManyCoAuthors#123leída26dic2023, datos crudos de1/2nunca disponibles para él, réplicaexplorada,no acusación de fraude del artículo por asociación. Gallup2026páginafuenteleída como contextoempleado2025; Gallup/Workhuman2024seguimiento2022–24identificado, asociación no causalidad.803 Ambler2015 estudio experimental DC/ElSalvador identificado enPubMed/PMC, no salariosmensualesrealesni todasfamilias; F069BancoMundial costos de remesas por contrastar.804 Cregg/Cheavens2021(volumen;online2020) resumen editorial primarioleído27estudios/N3675, g−0,29pos/−0,23seguimiento, comparación listaesperavscontrolactivo; sin tasascuración ni29%. Cuerpoeditorial suscripción,no lecturaíntegra. OMSfichaactual11sept2026identificada: tratamientos eficaces, no sustituir con gratitud. Descargar/conservar/verificar contenidos primarios antes de redactar; después802–804y805–807.

Capacidad recuperada: 4207886336B a2026-11-04T22:55:56.301847+00:00. Comprobar al menos200MiB(209715200B) antes de cada generación y margen proporcional para copias. No borrar originales o copias. Sin error de cuota de imágenes en este bloque.

501/512/649/707/769 siguen retenidos por título; sin publicación ni aprobación específica. Preguntas ya enviadas, no repetir ni tomar silencio como aprobación. Seguimiento del mismo chat activo cada tres minutos, sin procesos duplicados.
