# MEE · fuente privada de despliegue

Esta carpeta contiene únicamente los archivos necesarios para publicar la web React y el blog WordPress en Coolify. El trabajo editorial y visual continúa en `../mee-web`.

- `compose.yaml`: web estática en `/`, WordPress en `/blog/` y MariaDB privada.
- `Dockerfile`: compila Next.js y sirve el resultado con Nginx.
- `deploy/wordpress.Dockerfile`: instala Hello Elementor, el tema hijo MEE y el plugin editorial desde código.
- `wordpress/`: código versionado de temas y plugin. No hay contenido de la base de datos ni contraseñas.

Para publicar cambios desde el Mac: copiar los archivos modificados de `../mee-web` a esta carpeta, ejecutar `npm ci && npm run build`, confirmar y subir el commit privado con `git push`. En Coolify se puede desplegar el nuevo commit manualmente, sin GitHub Actions.

La ruta pública prevista es `https://moevec.org` y `https://moevec.org/blog/`. El DNS y el administrador de WordPress se configuran al activar el servicio; el repositorio no contiene secretos.
