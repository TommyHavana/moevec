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

WordPress: **808/840 terminadas,2424 imágenes originales públicas,0 borradores y32 pendientes**. Último bloque **811–813 / E2.6.01–03**, posts4586/4591/4596. Tribu → Lealtad Tribal **3/15**; Agradecimiento **15/15**. HTTP200,H1,canonical,indexabilidad,Article,tresWebPconalt/hash/renderizados, categorías, etiquetas, BreadcrumbList, sitemap y enlaces internos existentes verificados. Una publicación y tres adjuntos porID;taxonomía122/7. Advertencia conocida de dos metadescripciones idénticas, tema sin cambios. No afirmar indexación efectiva ni restauración completa arrancada.

- 811: Hirschman1970copia44pescaneada839119B SHA3a8154... releída visualmenteimp4–5/78–79,reading5/31conservadas. No confundirreading4=2–3o39=94–95. Salida/voz,lealtadpuederetrasarsalida,autoradmitebarrerasendeterminadascondiciones. PosiciónMEEvoluntariedadidentificada, no libertadlegalabsolutaoseguirgrupoindefinido.1016palabras,apertura51,FAQ48/52/51.
- 812: Banfield1958PDF104p7127762B SHA337c860... introducciónPDF7imp10–11, campo1954–55/9meses/representatividadincierta yteoríatentativa; cap5PDF44imp85(no83)hipótesisycoincidencianoprueba. No libroíntegro ni causalidadregional. Silverman1968resumenprimariopublisherleídoweb,inviertedireccióncausalhaciaestructuraagraria; descargalocal403registrada. Fukuyama2000PDF/HTML403y429no usadoscomoleídos,nilbro1995/F018fingidos. Alba/Estebanshipotéticos, sincifrasclientelismoLatAmoculturaspatológicas.1090palabras,apertura51,FAQ50/53/50.
- 813: Slovic1993manuscritoautoralOregon29p1032874B SHAaa01cbc... resumen/contexto yPDF7–10asimetría/juiciosnoticiashipotéticascentralnuclear, noseguimientoplazosfamiliaempresa. AxelrodHamilton1981PDF11p340674B contieneartículosajenos: leídotextopropioPDF3–6modelo/repetición/TFT/condiciones, no libro1984ni estrategiaúnicaforhumanos. ReparaciónvoluntariapropuestaMEE, sin perdónobligatoriorelojuniversal.1078palabras,apertura51,FAQ50/51/49.

Dos ejemplos hipotéticos y tresFAQ en cada entrada. Nueve nativos y mosaico vistos; portadas1200×630/interiores1600×900,cadaWebP<250KB. 812puenteeditadoconimagegenpararetirarmotivosregionalesajenos; descarte/promptconservados. 813jarrónreparadoesmetáfora,nogarantíareconciliación.

VPS `/data/mee-backups/produccion-840-incremento-811-813-20261105`: SQL30795520B,66derivados enarchivo2951103B;258incrementosmásbase. Hashesy miembrosverificados, sin nuevoarranque de restauración. ZIP incremental local y copia privada acreditados por `../mee-backups/produccion-811-813-entrega-20261105.json`;conservar toda la cadena.

Correcciónbibliográficainterna806: F-054delplanesEmmonsMcCulloughartículo2003, no libro2007. Artículo y fuentes públicas ya citabancorrectamente2003; se corrigieron rótulosinternos/revisión, sinpublicaciónomediosnuevos. Modificacionesincluidasenrespaldo811–813.

Continuar **814–816 / E2.6.04–06**, Tribu → Lealtad Tribal. Briefs y nueve prompts conservados, **0/9 imágenes y textos pendientes**; no reinicializar expedientes.814Royce1908PDFediciónprimariaidentificado, leerlealtadalealtadantesafirmar; distinguirposturaéticadeencubrimientolegal, ningunaobligaciónjurídicauniversal.815Kahan2013JDM8(4)407–424PDFCambridgeprimarioidentificado/resumenleído; descargarmétodoylímites, no capacidadcognitivagarantíainmunidad/polarizaciónafectivamedidaportestdistinto.816Reichheld1996/Hirschmanlealtadclientes: investigarcomparativosantesredactar; mejorfidelizaciónexigecriterioexplícitoMEE libertad/elección,nopromesaempíricauniversalderetenciónmásalta. Si laafirmacióncentralnoessostenible,mantenerencursoynocambiartítulosinaprobación. Después817–819.

501/512/649/707/769 siguen retenidos por título, sin publicación ni aprobación específica. Consultas ya enviadas: no repetir ni interpretar silencio como aprobación. Seguimiento del mismo chat activo cada tres minutos, sin procesos duplicados.

Capacidad medida antes del cierre: 1079824384B. Comprobar200MiB(209715200B) antes de cada generación y margen proporcional para copias. Conservar todos los originales yrespaldos, sinborrados. Sin error de cuotaimagegen en este bloque.
