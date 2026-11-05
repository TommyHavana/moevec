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

WordPress: **829/840 terminadas,2487 originales públicos,0 borradores,11 pendientes**. Bloque833–835/E1.7.08–10 completo; posts4691/4696/4701, imágenes4692–94/4697–99/4702–04. HTTP200,H1,canonical,indexabilidad,Article,tresoriginalesalt/hash/renderizados,navegación,BreadcrumbList,sitemap,enlaces200,organización122/7 comprobados. Dos metadescripciones idénticas siguen como incidencia de plantilla fuera de producción. No acredita indexación efectiva o arranque de restauración.

833: Peters2017PDF25p3477145B SHA731e406e50f5a4197dbab0633ec2a6ab41e7fd24c2f4b7ca159b870621b62374, abstract1, introducciónseleccionada2 yhabituación19leídos/19visual; marco teórico,no medicióncausalreformas. BOEresumen2025actualjun2026 asignaciónazar informacióninflación/decisionesfinancieras,no saludmental. CEPAL2019Venezuelahistórico leídoPDFporweb/localdos403, noPDFfingido; WHOmigraciónyACNURmanualpasajesseleccionados/no todaspersonaspatologizadas. Marina/Samuelhipotéticos.1110palabras,apertura53,FAQ51/51/52.
834: WHOAtlas2024publicado2sep2025PDF98p4453365B SHA953e3f74b036854fb8d2c1bacd8c5b0c0269ca05ec02394e388805fb1f38d31d;11/20–22/51leídos,51visual.144paísesrespuestatotal,tabla18mediana2.1%gastosanitariogubernamental75países,no2.1%mundial. Recogidajul2024–mar2025,ausenciadatos/sesgos/diferenciasinternas. OECD2025PDF244p18901751B SHA2a4438ee4d36a6cb4927748b9f56f72d31d0517ca7855e465f121af8dbe6e6aa,104/112–113leídos,104visual,coberturanoacceso,esperascirugíano rankingpsicoterapia. Suiza/NLoficialesconsultaactual, NZa22jul2025esperasGGZelevadas; WHO2021presentaciónpersonacentroy derechos. No mixtossiempremásrápidos. Patricia/Álvarohipotéticos.1130palabras,apertura55,FAQ52/52/49.
835: WHO2020PDF104p4041257B SHA50b66c44e7083cc3752849f301ae1d60d9360d511e34c0c948b39bdf6e13dc88;27/42–44leídos,42visual. Adultos18–64,150–300moderadao75–150vigorosaoequivalentesemana,fortalecimiento2días,gradualidad,no dosiscuración. Guíanoabordasueñocomocomportamiento, NHLBI24mar2022guíahorarioentornoturnos. WHOfichaactividad4nov2026yconexión30jun2025. Cochraneactual8ene2026resumensencillo73estudiosalmenos4985adultosdepresión,búsquedahastanov2023,sesgoycortoseguimiento; abstractantiguo39ensayosdelamismapáginano usadocomoactualización. No sustituciónmedicación/terapia, culpaohábitosgarantía. Nuria/Tomáshipotéticos.1141palabras,apertura55,FAQ49/55/53.

AvisosNIMHgeneralconservados; sin tratamientoindividual, teléfonosinventadosoesperaobligatoriaantepeligro. Nueve nativos y mosaico vistos,1200×630/1600×900WebP<250KB. Fuentes,revision,prompts,imagenes,textosycomprobacionesporID.

VPS `/data/mee-backups/produccion-840-incremento-833-835-20261105`: SQL31518583B,66derivados en2569412B,266incrementosmásbase. Rangos1–500,502–511,513–648,650–706,708–768,770–817,819–835;huecos501/512/649/707/769/818. Entrega local/privada en `../mee-backups/produccion-833-835-entrega-20261105.json` al terminararchivado. Preservar cadena/originales; sin nuevo arranquerestauración.

Continuar **836–838/E1.7.11–13**, SaludMental11–13/15. Briefs/nuevepromptsconservados,0/9imágenes,textospendientes.836Cuba:datosOPSactualesconfecha, no prevalenciaclínicasinnacionalrepresentativa, contrastarfortalezainstitucionalconaccesoactual;país-cubaetiqueta.837Achotegui2009/2012evidenciaprimaria, no fasesuniversalesopatologizartodosmigrantes.838Freeman2019online2018muestraconveniencia242+93autoinforme,nocausal/no72%todosfundadores. Después839–840 (últimobloquedepúblicación2entradas).

Títulos501/512/649/707/769/818 retenidos, preguntasyaenviadassinrespuesta;no repetirni silencioigualaprobación. Seguimiento mismo chat cada tres minutos; no duplicarprocesos. Comprobar200MiBantesgenerar ymargenproporcionalcopias, sin borraroriginales.
