# Continuar MEE entre chats

## Al abrir un chat

Adjuntar `docs/21-CONTEXTO-PORTABLE.md` (o el `MEE_CONTEXTO_PARA_NUEVO_CHAT.md` del paquete si es más reciente), el último `15-ESTADO-Y-CONTINUIDAD.md` y `16-BACKLOG-REACT.md`. Si el trabajo toca código o imágenes, facilitar acceso a los archivos concretos: no presuponer que un ZIP o carpeta de otro chat sigue accesible. El documento portable es contexto; no convierte en comprobado el estado que haya cambiado después de su fecha.

En Codex, abrir la carpeta raíz real y usar `prompts/CONTINUAR-CHAT.md`. En ChatGPT, adjuntar el contexto y pegar `ABRIR_CHAT.md` del paquete. Pedir al asistente que identifique tarea activa y último estado verificable, sin reconstruir toda la historia ni volver a pedir decisiones ya tomadas.

## Durante una sesión

Separar requisitos, recomendaciones y decisiones aceptadas. Registrar cambios de alcance. Trabajar sobre los archivos actuales; no declarar que existe una imagen, una tienda o una prueba por aparecer en un plan. Si no hay permiso para escribir en la carpeta activa, generar un paquete revisable en una ubicación autorizada y dejar instrucciones claras; no afirmar que ya se instaló.

## Al cerrar

Usar `prompts/CIERRE-Y-TRASPASO.md`. Actualizar estado, decisiones y backlog; anotar última prueba y siguiente acción. Crear respaldo cuando se permita. Si el chat no puede escribir archivos, entregar el traspaso en texto para que el siguiente lo incorpore. No copiar credenciales, tokens, datos de compradores o conversaciones personales.

## Plantilla de traspaso

```text
PROYECTO: MEE
FECHA/ZONA: [Europe/Madrid]
CARPETA: [ruta actual]
PETICIÓN ACTIVA: [encargo concreto]
TERMINADO: [archivos/resultado]
EVIDENCIA: [comandos o pruebas y fecha]
PENDIENTE: [lista corta]
DECISIONES NUEVAS: [del fundador]
PROPUESTAS SIN APROBAR: [lista]
BLOQUEO REAL: [si existe]
AUDITORÍA: [sigue pendiente / encargada expresamente el...]
SIGUIENTE PASO: [acción concreta]
ARCHIVOS ADJUNTOS: [qué debe leer el siguiente]
```

## Vigencia

Las instrucciones recientes del fundador prevalecen. Los archivos históricos de Claude permanecen como fuente; las rutas propuestas de blog, tema WordPress y arquitectura híbrida no se convierten en decisiones definitivas por repetirse en varios chats.
