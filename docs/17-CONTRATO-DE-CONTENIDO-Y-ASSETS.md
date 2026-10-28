# Contrato propuesto de contenido y assets

**Diseño de datos, todavía no implementado.** La aplicación actual combina taxonomía y editorial en `lib/areas.ts`. Mantener esa fuente y sus IDs; incorporar una capa visual separada en lugar de incrustar rutas, parámetros y escenas repetidas en cada JSX.

## Unidad visual

Un nodo tiene ID basado en la ruta completa (`area/subcategoria/tema/...`), slug original, nombre, padre, profundidad, resumen editorial y referencia a su ficha visual. El slug solo puede repetirse en ramas distintas; por eso el ID incluye los padres. No cambiar los slugs para acomodar nombres de archivos.

```json
{
  "id": "educacion-y-valores/autonomia",
  "taxonomySlug": "autonomia",
  "name": "Autonomía",
  "visual": {
    "status": "propuesto",
    "concept": "Una pieza construye su propio recorrido",
    "action": "elegir y avanzar",
    "poster": null,
    "mobilePoster": null,
    "layers": [],
    "clip": null,
    "motionProfile": null,
    "reducedMotionPoster": null,
    "alt": null,
    "rights": null
  }
}
```

`null` significa pendiente, no una URL válida ni un permiso concedido. Los campos de medios se completan solo al existir el archivo. Ver inventario de planificación en `inventario/visuales.json`; no es aún el manifiesto que consume la web.

## Responsabilidades propuestas

- Fuente histórica: nombres, orden, jerarquía y significado del documento original.
- Editorial de trabajo: resúmenes, beneficios y descripciones revisables.
- Manifiesto visual: recursos existentes, encuadres, alternativas y perfil de movimiento por ID.
- Componente de escena: render, carga, activación y pausa; no contiene la definición política/editorial del nodo.
- Adaptador futuro de CMS: convierte los datos de WordPress a ese contrato. No filtrar credenciales al cliente.

## Archivos y variantes

Propuesta de ruta: `public/images/subcategorias/<area>/<slug>/` para posters públicos. Definir encuadres y anchos a partir del espacio real en el layout y densidad de pantalla; entregar dimensiones intrínsecas para evitar saltos. Capas y clips se referencian mediante el manifiesto. Los originales de edición y archivos de venta no se colocan en `public/`.

Mantener tipografía HTML y punto focal por breakpoint. No prometer que recortar automáticamente una única imagen resuelve todos los formatos. Los logos conservan sus exportaciones transparentes del kit.

## Puente con WordPress

Cuando llegue esa fase, decidir qué se edita: texto, medio, texto alternativo, orden visual o perfil de movimiento. No ofrecer campos de código arbitrario para animar cada entrada. La web validará datos y estados antes de renderizar. Una actualización editorial necesita una estrategia explícita de compilación/revalidación.
