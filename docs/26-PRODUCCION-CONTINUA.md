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

WordPress: **769/840 terminadas, 2307 imágenes originales públicas, 0 borradores y 71 pendientes**. Último bloque **772–774 / E2.3.07–09**, publicado y verificado: posts4391/4396/4401. Tribu → Responsabilidad Generacional8/15. HTTP200, H1, canonical, indexabilidad, Article, tres imágenes con alt y hashes, categorías, etiquetas, enlaces y sitemap comprobados. Advertencia conocida de plantilla: dos meta descripciones idénticas; no se ha cambiado el tema.

-772: ficha CE2024 tabla10, gasto bruto público2022/2050 diferenciado de media actualizada2022–2050 AIReF2026; cumplimiento formal de regla no equivale a sostenibilidad integral. MEI2026 del Régimen General y cálculo aislado, sin prometer prestación individual.
-773:40años del título delimitados1981–2021 y actualización a2026. SP tipoC octubre2026, rentabilidad real deflactada por UF con horizontes diferenciados. Diagnóstico de brechas con datos2022, posición de NO+AFP y fase empresarial3,5% agosto2026–julio2027, no8,5% ya vigente. Ejemplo de reemplazo hipotético.
-774: Ley26425 original y actualizada, transferencia en especie al FGS preexistente de2007, excepciones de rentas vitalicias y aportes voluntarios. Decreto2104/2008 y respuesta44 del Informe136 al Senado de2023. Considerandos de2000 como argumento histórico de comisiones, no norma vigente. Sin valoración FGS2026: PDF no accesible, límite registrado.

VPS `/data/mee-backups/produccion-840-incremento-772-774-20261104`: SQL29527373B,66 derivados en archivo1784990B;245 incrementos más base. Hashes y miembros verificados, sin nueva prueba de arranque. ZIP local incremental y copia privada se completan antes de seguir.

Continuar **775–777 / E2.3.10–12**: briefs y nueve prompts conservados, **0/9 imágenes y textos pendientes**. Primeras fuentes descargadas: canal institucional ONEI, índice de Gaceta2025O71, Código Civil BOE y Pew2022/2026. Estas descargas aún requieren lectura y revisión; no cuentan como artículos terminados. Después778–780.

501/512/649/707/769 siguen retenidos por revisión de título, sin publicación y sin aprobación específica. Las preguntas ya se enviaron: no repetirlas ni interpretar silencio como aprobación. Conservar originales y toda la cadena de copias. Comprobar200MiB libres antes de cada generación y margen proporcional para las copias. Seguimiento del mismo chat activo cada tres minutos.
