# Puente MEE · React, WordPress y Phoenix

El frontend permanece en React. `mee-editorial/inc/network.php` implementa el puente de WordPress: webhook HMAC-SHA256, timestamp, cola, reintentos y caché. React consume la ruta del mismo origen `/blog/wp-json/mee/v1/conversation?area=trabajo`; el servidor WordPress consulta Phoenix. No se necesitan cookies compartidas ni CORS entre los navegadores y la red.

La red está **desactivada** en esta instalación. `https://red.moevec.org/api/v1/areas` no ofrece actualmente un certificado válido para ese host. El sitio muestra una invitación a contactar sin inventar publicaciones. Los archivos `phoenix/` proceden de la entrega del usuario y deben aplicarse al proyecto Phoenix completo en su entorno. No se ha ejecutado Elixir ni migrado una base Phoenix desde este Mac.

Configuración de WordPress: archivo privado `/run/mee-secrets/red-integration.json`, fuera de Git, con estas claves:

```json
{"enabled": false, "url": "https://red.moevec.org", "secret": "REEMPLAZAR_POR_UN_SECRETO_COMPARTIDO_DE_64_HEX"}
```

Después de disponer de la aplicación Phoenix completa y su despliegue HTTPS válido:

1. Aplicar los módulos y la migración al proyecto Phoenix, revisar sus versiones y ejecutar sus pruebas.
2. Comparar `GET /api/v1/areas` con las 7 áreas y 56 temas principales del sitio. La fuente actual preservada está en `content/taxonomia.json`; `content/visuals.json` contiene también los 59 nodos internos.
3. Crear un secreto aleatorio de 32 bytes, configurarlo como `MOEVEC_WEBHOOK_SECRET` en Phoenix y en el JSON privado de WordPress. Mantener permisos 640, grupo www-data, sin registrar el valor en chats o repositorios.
4. Verificar publicación, actualización, retirada, firma alterada, caducidad e idempotencia contra staging. Las maquetas con `_mee_demo=1` se excluyen del webhook.
5. Activar `enabled` y comprobar conversación disponible, vacía y caída. La caché de respuestas correctas dura 120 segundos; los fallos, 30 segundos. La cola reintenta a 1, 5, 30, 120 y 360 minutos. El cron del sistema corre cada minuto; el puente no promete entrega en menos de 5 segundos.

No instalar además el antiguo plugin `mee-red`: duplicaría la responsabilidad que ya cubre `mee-editorial`.
