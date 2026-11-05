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

WordPress: **817/840 terminadas,2451 imágenes originales públicas,0 borradores y23 pendientes**. Último bloque **821–823 / E2.6.11–13**, posts4631/4636/4641; Tribu → Lealtad Tribal12/15. HTTP200,H1,canonical,indexabilidad,Article,tresWebPconalt/hash/renderizados, organización122/7,BreadcrumbList,sitemap y enlacesinternos200 verificados. Advertencia conocida: dos metadescripciones idénticas. No afirmar indexación efectiva o restauración completa arrancada.

-821: BOE LSCconsolidadaart28/29/86 yDGRN31/07/2018 expedienteconcreto. No cláusulas definitivas ni validez universal dearrastre/acompañamiento. Palabraclave socios leales evita colisión conE4.5.06, enlazado; título yslugintactos. Texto1174palabras,apertura50,FAQ52/50/51.
-822: NewlandMPI2009 introducción parcial; WBdefiniciónremesas; IFAD14/09/2026 dato728600millonesUSD en2025 a paísesingresosbajosmedianos; Ketkar/Ratha2008cap3Israel/India histórico; Irlanda2026–30objetivosnomedición; OFACFAQ1273 vigente30/09/2026cambioespecíficocuentasempresarios,noprohibicióngeneraltodasremesas. DescargalocalIFAD403registrada, lecturawebhonesta. Texto1172,apertura55,FAQ47/51/51.
-823: Bennedsenetal NBER2006antecedenteQJE2007,sucesiónCEOdanesa ysupuestosinstrumentales,nocontratacióncualquierprimo; IEF2015cuestionariopuestos/reglasnoestadísticasactuales; EBEPart55empleopúblicodistintocontrataciónprivada. Texto1208,apertura54,FAQ52/51/52.

Nueve nativos y mosaico final vistos;3/3 porentrada, portadas1200×630/interiores1600×900,cadaWebP<250KB. Ejemploshipotéticos, fuentesfechadas yalcanceparcialexplícito.

VPS `/data/mee-backups/produccion-840-incremento-821-823-20261105`: SQL31092355B,66 derivados enarchivo3242974B;261incrementosmásbase. Rangos1–500,502–511,513–648,650–706,708–768,770–817,819–823; huecos501/512/649/707/769/818. Hashesymiem brosverificados,sinnuevoarranquederestauración. ZIPincremental y copia privada acreditados por `../mee-backups/produccion-821-823-entrega-20261105.json`; conservar cadena yoriginales.

Continuar **824–826 / E2.6.14,E2.6.15,E1.7.01**. Briefs y nueveprompts guardados;0/9imágenes,textospendientes.824HirschmanF035pasajesarchivadosycontrapuntoabusosinaviso.825F058Granovetter1973 yF055Putnam2000, no promesa multiplicaraprendizaje.826OMSprimariaactual, avisosaludmentalobligatorio, sin diagnósticootratamiento. Después827–829.

501/512/649/707/769/818 siguen retenidos por título. Consultas ya enviadas: no repetir ni interpretar silencio como aprobación. Seguimiento mismo chat cada tres minutos, sin procesos duplicados.

Comprobar200MiB(209715200B) antes de cada generación y margen proporcional para copias. Sin error de cuotaimagegen. Conservar originales yrespaldos.
