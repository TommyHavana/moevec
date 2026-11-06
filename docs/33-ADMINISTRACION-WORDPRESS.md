# Administración de temas y plugins · 06/11/2026

El titular necesita instalar y actualizar temas y plugins desde su cuenta administradora en https://moevec.org/blog/wp-admin/.

## Incidencia y reparación

Hello Elementor quedó vacío durante un intento de actualización. También estaban incompletos Twenty Twenty-Four y Twenty Twenty-Five. El fallback de WordPress había dejado activa la opción `twentytwentyfive`, igualmente dañada. Los directorios padre `wp-content/themes` y `wp-content/plugins` pertenecían a root con modo 0755: PHP podía borrar archivos de algunos temas, pero no reemplazar sus carpetas. La cuenta `mee_admin` sí tenía las capacidades de instalación y actualización.

Se guardó copia privada de los árboles de temas y plugins en `/data/mee-backups/admin-management-20261106/` antes de reparar. Se restauró Hello Elementor desde el paquete del despliegue y los temas secundarios desde los originales de WordPress; se reactivó `mee-child` con padre `hello-elementor`. Después, la actualización de Hello Elementor a 3.5.2 se completó desde el panel real.

## Decisión administrativa expresa

La revisión automática rechazó inicialmente ampliar la propiedad de los árboles. Se pidió autorización explicando las carpetas afectadas y el riesgo de que un plugin vulnerable pueda modificar esos archivos. El titular respondió: «Sí, autoriza la gestión de temas y plugins desde WordPress».

Con esa autorización, themes y plugins, incluido su contenido, pertenecen a `www-data:www-data`. Los padres conservan modo 0755, sin permisos 777. No se modifica la configuración, las credenciales ni la protección `DISALLOW_FILE_EDIT`. Esta decisión sustituye la restricción histórica de instalación exclusivamente mediante despliegue recogida en el documento 28.

## Persistencia

`mee-deploy-source/deploy/wordpress-entrypoint.sh` conserva las instalaciones y actualizaciones de Hello Elementor, Two-Factor y Rank Math del volumen: sus paquetes solo se copian si faltan. El código propio `mee-child` y `mee-editorial` sigue actualizándose desde el repositorio; sus cambios de código deben mantenerse allí. El arranque aplica la propiedad autorizada exclusivamente en los árboles de temas y plugins.

Estado del nuevo despliegue: pendiente de comprobación final.

## Verificación

- Panel: actualización de Hello Elementor completada correctamente; cinco temas sin errores.
- Instalador real de WordPress: plugin temporal vacío instalado, sustituido por otra versión y retirado; nunca activado. La lista de plugins activos no cambió.
- Blog público: HTTP 200, H1 «Ideas en movimiento.» y hoja de estilo MEE presente.
- Inventario previo: 840 entradas publicadas y 122 categorías; no se editan artículos en esta reparación.
- Evidencia: `inventario/admin-wordpress-2026-11-06/verification.json`.

## Uso

Acceder al panel con la cuenta administradora. Actualizar temas desde Apariencia → Temas; instalar o actualizar plugins desde Plugins. Mantener MEE Editorial como tema activo para conservar el diseño. La portada React sigue gestionándose desde el código.
