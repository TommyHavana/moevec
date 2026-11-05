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


## Continuación exacta · 05/11/2026

WordPress: **823/840 terminadas, 2469 imágenes originales públicas, 0 borradores y 17 pendientes**. Bloque **827–829 / E1.7.02–04** completo, posts4661/4666/4671. Salud Mental4/15. HTTP200,H1,canonical,indexabilidad,Article,tres imágenes con alt/hash/renderizados, navegación,BreadcrumbList,sitemap,enlacesinternos200 y organización122/7 comprobados. Dos metadescripciones idénticas siguen como incidencia conocida de plantilla. No se acredita indexación efectiva ni un nuevo arranque de restauración.

827: Mani2013 PDF6p leído parcialmente por web2–5/imp976–979; local403 registrado, sin PDF fingido o suplemento. Laboratorio con escenarios hipotéticos y comparación agrícola de ingresos naturales, no asignación aleatoria de riqueza. DeAlmeidaetal2024 PDF19p1808560B, abstract/introducción1–2, PDF1visual; metaanálisis amplio con asociación adversa promedio condicionada por educación. Szecsi/Szaszi2024 abstract/discusión/limitaciones leídos porweb, local403: señales financieras y efecto desigual por ingresos, resultado sensible a priors y datos limitados. Alcances distintos, sin coeficienteIQ universal ni incapacidad personal por pobreza. HarvardfichaEscasez2013, no libro completo; CFPBguíaweb, local403, ahorro según posibilidades y control de saldos. Texto1138,apertura54,FAQ49/50/49; Teresa/Iván hipotéticos.

828: Frankl edición inglesaBeacon2006 PDF148p781304B, solo98–102leídos,102visual; tres vías, sufrimiento no necesario y atender causas evitables. No cifras de supervivencia o caso clínico como eficacia. VFIcronología1942/1945 y pensamiento previo a campos, Batthyánypresentaciónlogoterapia; no supervivencia por actitud ni terapia prescrita. Texto1184,apertura57,FAQ51/49/51; Marta/Sergio hipotéticos.

829: NHSHTML78358B lectura general de preocupaciones/bienestar; Gallup28/04/2026 HTML168144B yPDF18p493444B, metodología1 ytabla4leídas/vistas. Campo1–15abril2026,1001adultos18+EEUU50estados+DC, teléfonoaleatorio ponderado;31%costevidainflaciónQ10abiertamúltiple, margen4pp95%. No prevalencia clínica o mundohispano. MoneyHelperUKguíaleídaweb, local403, asesoría y condiciones por territorio; orden no crea excedente ni cura. Texto1237,apertura56,FAQ50/50/50; Beatriz/Raúl hipotéticos.

Avisos educativos de salud mental y orientación profesional en las tres; financiero también827/829. NIMHabril2026 compartido, sin tratamiento individual, teléfonos inventados o espera obligatoria ante peligro. Nueve nativos y mosaico final vistos;3/3 por entrada,1200×630/1600×900,WebP<250KB.829últimoalt ajustado a persona ficticia entre ondas, no protocolo respiratorio.

VPS `/data/mee-backups/produccion-840-incremento-827-829-20261105`: SQL31299191B,66derivados en2692453B,264incrementosmásbase. Rangos1–500,502–511,513–648,650–706,708–768,770–817,819–829; huecos501/512/649/707/769/818. Hashes y miembros comprobados; sin nuevo arranque de restauración. Entrega local/privada acreditada en `../mee-backups/produccion-827-829-entrega-20261105.json`; preservar cadena completa.

Recuperación de capacidad del checkpoint824–826 completada sin borrar originales; entrega de ese bloque privada85b24b66f86300a93bf10a394b785c97069c9db6. Checkpoint remoto histórico `/data/mee-backups/produccion-840-progreso-824-826-20261105T014105Z`, ZIPlocal26419616B conservados. Comprobar209715200B antes de cada generación y margen proporcional para copias.

Continuar **830–832 / E1.7.05–07**, Salud Mental, tanda56/56entradas5–7/15. Briefs y nueveprompts conservados;0/9imágenes,textospendientes.830HoltLunstad2010asociaciónno tratamiento, Putnam ycontrapuntoOMS2025políticaspúblicas.831Gallup2026compromiso/empleados, WHOQD85fenómenoocupacionalnoenfermedad,nocompararcuantitativamenteautonomíaysalario sin datos.832Haidt2024, OdgersNature2024, Orben/Przybylski2019asociaciónnocausal, leyAustralia vigente desde10/12/2025 con alcanceplataformas, no eficacia sanitaria inferida. Después833–835.

Títulos501/512/649/707/769/818 siguen retenidos, preguntas ya enviadas sin respuesta: no repetirlas ni interpretar silencio como aprobación. Seguimiento activo mismo chat cada tres minutos, sin procesos duplicados.
