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

WordPress: **820/840 terminadas, 2460 imágenes originales públicas, 0 borradores y 20 pendientes**. Bloque **824–826 / E2.6.14, E2.6.15, E1.7.01** completo, posts4646/4651/4656. Todas las páginas, H1, canonical, indexabilidad, Article, tres imágenes con alt/hash/renderizados, navegación, BreadcrumbList, sitemap y enlaces internos200 comprobados. Organización122nodos/7raíces. Advertencia conocida: dos metadescripciones idénticas; no acreditar indexación efectiva ni un arranque de restauración.

824: Hirschman1970, lectura visual parcial de impresas4–5/78–79;1800RESPECT sobre planificación individual ante abuso. Aviso previo y cierre no son obligaciones universales ni garantía de seguridad o reconciliación. Texto1030, apertura52, FAQ49/50/48; Adriana/Óscar hipotéticos.
825: Granovetter1973 PDF22p2216242B, visual1portada y2–3imp1360–1361; Putnam, extracto de edición2020 leído por web328–345, descarga local403 registrada. No libro completo2000 ni promesa de ventas/aprendizaje multiplicado. Texto1100, apertura53, FAQ49/49/50; Julia/Esteban hipotéticos.
826: fichaOMS11/09/2026, presentación oficial del informe2022 y NIMHabril2026; lecturas generales parciales, sin diagnóstico, tratamiento, culpa o prestaciones universales. Aviso educativo obligatorio y no esperar dos semanas ante empeoramiento o peligro. Texto1237, apertura54, FAQ51/51/51; Raquel/Bruno hipotéticos.

Nueve nativos y mosaico final vistos;3/3 por entrada, portadas1200×630 e interiores1600×900, WebP<250KB. Los primeros ocho recursos estaban conservados: solo se generó la ventana pendiente de826 al recuperar capacidad, sin repetir imágenes.

Copia VPS en dos etapas: `/data/mee-backups/produccion-840-incremento-824-825-20261105` contiene44derivados/1850285B; `/data/mee-backups/produccion-840-incremento-826-826-20261105` contiene22derivados/1128251B y SQL final31189471B. Cadena263incrementos más base. Rangos1–500,502–511,513–648,650–706,708–768,770–817,819–826. Huecos501/512/649/707/769/818. Hashes y miembros comprobados, sin nuevo arranque de restauración.
Prueba de entrega local/privada: `../mee-backups/produccion-824-826-entrega-20261105.json`.

El checkpoint de capacidad `/data/mee-backups/produccion-840-progreso-824-826-20261105T014105Z` conserva8nativos,3cuerpos y166archivos en26419616B. Recuperación local comprobada de15exportaciones, sin sobrescribir otros trabajos; copia local `../mee-backups/MEE_Editorial_824-826_checkpoint_2026-11-05.zip`. ENOSPC previo resuelto, sin borrar originales ni respaldos. Comprobar209715200B antes de cada generación y margen proporcional para cada copia.

Continuar **827–829 / E1.7.02–04**, Educación y Valores → Salud Mental, tanda56/56 entradas2–4/15. Briefs y nueve prompts conservados,0/9imágenes y textos pendientes.827: Mani2013, deAlmeida2024 y Szecsi/Szaszi2024 requieren distinguir asociación general, tareas y señales de escasez; no coeficienteIQ universal ni estudios con idéntico alcance.828: Frankl, experiencia y logoterapia con lectura primaria parcial, sin romantizar sufrimiento o reemplazar atención.829: encuestas primarias2026 con país/muestra/fecha y orientación pública de deudas; sin cura por ordenar papeles. Después830–832.

Seis títulos retenidos501/512/649/707/769/818; consultas ya enviadas, sin respuesta. No repetirlas ni interpretar silencio como aprobación. Automatización del mismo chat cada tres minutos, sin procesos duplicados.
