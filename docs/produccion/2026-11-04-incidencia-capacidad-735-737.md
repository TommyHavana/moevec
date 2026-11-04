# Interrupción de capacidad · bloque735–737

Durante la conversión del interior1 de E2.1.01, PIL informó `OSError: [Errno28] No space left on device`. La siguiente comprobación con un documento here mostró el mismo límite. No se llamó a imagegen para el siguiente recurso.

El original inspeccionado `exec-04003a1a-2e2d-4e3a-944d-9da642c6d2a2.png` se conservó. La comprobación posterior encontró únicamente la portada WebP, sin un interior parcial. Se continuó con redacción y fuentes; el espacio disponible pasó después a unos2,1GB. Se convirtió ese mismo original y se prosiguió tras superar de nuevo el umbral de200MiB antes de cada generación.

No se borraron copias, originales o trabajo ajeno. No se atribuye una causa a la variación externa de espacio. No se publicó una entrada incompleta ni se regeneró el recurso conservado.

## Segunda interrupción y protección del registro

WordPress creó737 /E2.1.02 /post4221 con sus tres adjuntos; después falló la sincronización local por ENOSPC. No se repitió el publicador. También falló el guardado local de la verificación; se repitieron solo sincronización y comprobación, manteniendo las publicaciones.

La exportación MD/CSV/JSON ahora prepara los tres temporales completos y los sincroniza antes de reemplazar las versiones anteriores. Una prueba con ENOSPC inyectado en el segundo archivo verificó que ambos destinos conservaron sus contenidos previos y que una exportación posterior pudo completarse. No es una transacción atómica entre tres rutas: evita truncar destinos durante la preparación.
