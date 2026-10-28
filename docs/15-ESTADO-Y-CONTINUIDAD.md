# Estado de MEE y continuidad · 28/10/2026

## Ubicación

Proyecto usado en esta sesión: `/Users/nerea/Documents/Proyectos/MEE/mee-web`.
La carpeta `MEE` es contenedora; `mee-web` es la raíz con `package.json`.

## Evidencia y límites de esta entrega

Se leyeron la documentación, `package.json`, la taxonomía JSON, `lib/areas.ts` y la plantilla de área del proyecto local. Se generó este paquete de documentación en otra carpeta autorizada. **No se modificó el código ni la documentación de la carpeta activa, no se arrancó el servidor y no se ejecutó una auditoría o un build en esta tarea.** El instalador incluido permite al usuario incorporar los documentos con copia previa.

| Elemento | Estado |
| --- | --- |
| React/Next.js/TypeScript y exportación estática | Existe. |
| Portada y siete rutas de área | Implementación inicial existente. |
| Fuente original y taxonomía | Preservadas; siete áreas, 46 temas formativos, diez ejes políticos, 48 temas políticos y once subtemas. |
| Editorial | Siete resúmenes y 56 beneficios/presentaciones propuestos, pendientes de revisión editorial. |
| Categorías: imagen | Siete escenas originales con variantes, dirección inicial. |
| Subcategorías: imagen propia | No implementada en las 56 secciones de la plantilla examinada. |
| Movimiento | Primera capa de entrada/revelado/hover e índice; falta el movimiento semántico por escena. |
| Marca | Kit de pantalla, PNG/WebP, SVG, Archivo/Manrope y favicon; falta revisar fidelidad final al logo preferido para otros soportes. |
| Compilación | Hay un build satisfactorio documentado del 28/10/2026, anterior a esta tarea; no sustituye repetirlo cuando cambie código. |
| Pruebas visuales | Capturas históricas de portada a 1440/390; no validan todos los interiores ni la tipografía actual. |
| WordPress y WooCommerce | Fase posterior; esqueleto de WordPress aparcado, sin funcionamiento comprobado. |
| Auditoría total de usabilidad | No realizada; espera petición expresa. |

## Últimas instrucciones del fundador

1. Usar la carpeta local indicada y seguir sin Git.
2. Cada categoría/subcategoría tendrá imagen y movimiento vinculados a su valor.
3. Ambición de una web con ejecución del nivel de una candidatura Awwwards; no hay promesa de premio.
4. Preparar la arquitectura para arte digital y WordPress, sin adelantar su implementación.
5. No hacer la auditoría total todavía.
6. Crear documentación portable para Codex y chats nuevos.

## Propuesta pendiente de aprobación final

Arquitectura híbrida: Next para experiencia visual, WordPress para edición y WooCommerce para tienda/checkout. Sigue siendo recomendación; ver `14-ARQUITECTURA-EDITORIAL-Y-TIENDA.md`.

## Siguiente paso propuesto

Tras incorporar estos documentos, preparar un piloto visual de una categoría y dos subcategorías. Primero guion y estructura; la producción de escenas se realiza al recibir un encargo de implementación/creación, sin generar toda la colección por anticipado. Resolver también cómo se presentan los 59 nodos internos antes de afirmar que el alcance de imagen está completo.

## Registro para la siguiente sesión

### Incorporación documental · 28/10/2026, Europe/Madrid

- Tarea recibida: leer `EMPEZAR-AQUI.md`, aplicar el instalador y confirmar la incorporación; sin auditoría ni WordPress.
- Archivos leídos: guía del paquete, instalador, `AGENTS.md`, `docs/00-LEER-PRIMERO.md`, este estado, `docs/16-BACKLOG-REACT.md` y el prompt de cierre.
- Archivos cambiados: 24 archivos documentales incorporados por el instalador; después, este estado y `docs/16-BACKLOG-REACT.md` para registrar el resultado.
- Comandos y resultados: `python3 ../MEE_Documentacion_Codex_y_Chats/APLICAR_DOCUMENTACION.py .` incorporó 24 archivos y creó copias previas en `../mee-backups/documentacion_2026-10-28_022055_760890/`. Se compararon los 32 archivos del manifiesto con el paquete: cero discrepancias inmediatamente después de instalar.
- Pruebas visuales realmente realizadas: ninguna en esta sesión.
- Decisiones nuevas del fundador: ninguna sobre diseño o arquitectura; la petición limita esta sesión a incorporar documentación.
- Propuestas aún no aceptadas: piloto visual y arquitectura híbrida, tal como constan arriba.
- Bloqueos y permisos reales del entorno: ninguno para esta incorporación.
- Próximo paso concreto: cuando el fundador encargue implementación, preparar el guion y la estructura del piloto de una categoría y dos subcategorías; resolver el tratamiento de los 59 nodos internos antes de dar por cerrado el alcance visual. La auditoría total sigue pendiente de petición expresa.

No borrar el historial útil. Sustituir las casillas vacías por evidencia al cerrar cada sesión. Adjuntar este documento y el backlog al siguiente chat, junto a los archivos que necesite leer.

### Despliegue solicitado · 28/10/2026, Europe/Madrid

- Tarea recibida: configurar `moevec.org` con DonDominio, Contabo y Coolify; crear WordPress y avanzar el blog con tema hijo Hello Elementor. El fundador ha autorizado esta fase expresamente.
- Estado verificado: dominio activo en DonDominio con parking y DNS del registrador; VPS Contabo `5.189.183.51`; servidor Coolify validado. Se creó el proyecto `mee`, la red `mee-production` y el servicio `mee-wordpress` con MariaDB. Se programaron copias locales diarias de base de datos y volumen WordPress; todavía no se ha ejecutado ninguna.
- Código: tema hijo local actualizado con logo y fuentes del kit MEE y paquete `wordpress/mee-child.zip` preparado. `npm run build` de React terminó correctamente y generó portada y siete rutas. Se creó una copia mínima de fuente de despliegue en `../mee-deploy-source/`, aún sin repositorio ni publicación.
- El fundador corrigió el destino a `moevec.org/blog/` y autorizó un repositorio privado para Coolify. Se descartó sin guardar el registro A de `blog.moevec.org` y la ruta del subdominio en Coolify. GitHub Actions no es necesario para este despliegue.
- Se creó el repositorio privado `TommyHavana/moevec` a partir de `../mee-deploy-source/`, con Next estático, Hello Elementor, tema hijo, plugin editorial y `compose.yaml` para Nginx, WordPress y MariaDB. La copia compiló con `npm ci && npm run build`; el archivo de dependencias llevaba URLs locales de tarballs y se normalizó en la copia de despliegue. Coolify lee el repositorio con una clave exclusiva de solo lectura y detectó `compose.yaml`; se creó la aplicación `mee-web-blog` en la red MEE. Ningún recurso se ha desplegado aún.
- Publicación completada con autorización específica del fundador: DonDominio tiene el registro A de `moevec.org` hacia `5.189.183.51`, `www` apunta por CNAME al dominio principal y el ANAME antiguo del parking se eliminó con autorización adicional. La página de parking está desactivada. Los registros de correo se conservaron.
- La aplicación activa en Coolify es `mee-web-blog` (Compose desde el repositorio privado; actualización React `dac21ed`), con React en `https://moevec.org/` y WordPress en `https://moevec.org/blog/`. Ambos devuelven HTTP 200 con TLS válido; HTTP redirige a HTTPS. WordPress tiene activo el tema hijo `mee-child` de Hello Elementor y el plugin editorial, con siete categorías creadas. El acceso administrativo es `https://moevec.org/blog/wp-admin/`, usuario `mee_admin`; la contraseña inicial está en el volumen privado `secret-files` del servicio WordPress y se entregó al fundador por el chat, sin guardarla en el repositorio. La navegación React incluye enlace al blog.
- Se crearon dos programaciones diarias de copia local para la aplicación activa: volumen MariaDB (contenedores detenidos durante la copia para consistencia) y volumen WordPress. La primera ejecución de ambas terminó correctamente el 28/10/2026 (2,8 MB y 37,31 MB). No se ha comprobado una restauración. El servicio anterior `mee-wordpress` quedó sin desplegar y no forma parte de la publicación.
- Pendiente de producto: revisar textos, imágenes, animaciones y las 56 secciones React antes del cierre; no se ha realizado la auditoría total ni se ha instalado la tienda.
