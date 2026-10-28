# Taxonomía que debe aparecer en React

La jerarquía se copia de `fuentes/claude/docs/02-taxonomia.md`, conservada sin cambios. `content/taxonomia.json` es el espejo legible por React. **No usar la lista provisional de tres temas por categoría** creada antes de recuperar el ZIP.

| Orden | Categoría | Pregunta | Temas principales | Papel |
| --- | --- | --- | ---: | --- |
| 1 | Educación y Valores | ¿Qué creer? | 9 | Valores y herramientas para pensar |
| 2 | Tribu | ¿Quién te rodea? | 6 | Familia y red de apoyo inclusiva |
| 3 | Comunidad | ¿Cómo participas en grupo? | 4 | Contribución y mérito |
| 4 | Trabajo | ¿Cómo te capitalizas? | 12 | Ruta de desarrollo económico personal |
| 5 | Capitalismo Consciente | ¿Por qué funciona el sistema? | 8 | Historia, comparación y ética |
| 6 | Economía Compartida | ¿Cómo crecer beneficiando a muchos? | 7 | Prosperidad entre actores pequeños |
| 7 | Política y Economía | ¿Quién decide las reglas? | 10 ejes | Aplicación a leyes, medidas y países |

Las seis primeras son **teoría y herramientas**. La séptima es **aplicación en tiempo real** y tiene además temas y subtemas anidados. No reducir sus 10 ejes a tres conceptos genéricos. Los tres niveles transversales son **Fundamentos, Desarrollo y Aplicación**: sirven a la planificación editorial; no se convierten automáticamente en navegación ni en una taxonomía WordPress antes de diseñarla.

## Navegación

- Portada: siete mosaicos, una categoría por mosaico, enlazados a `/areas/<slug>/`.
- Interior: navegación superior fija con los 9, 6, 4, 12, 8 o 7 temas auténticos de cada área; en Política y Economía, los diez ejes. En móvil, la barra se desplaza horizontalmente con el dedo y conserva foco visible al teclado.
- En el cuerpo: cada tema tiene una sección con `id` estable, título legible y beneficio editorial. Para Política y Economía, cada eje expone sus temas y subtemas sin aplanar la jerarquía.
- Si hay demasiados temas para una lectura cómoda, agrupar visualmente o usar índice de contenidos accesible; **no eliminar nombres** ni cambiar el orden para resolver espacio.
- Los enlaces a un artículo WordPress sólo se activan cuando la entrada y su URL existan. No simular páginas de blog.

## Generación y verificación

`node scripts/sync-taxonomy.mjs` reconstruye el JSON a partir del documento fuente. Verificar siete categorías, 46 temas en las primeras seis y diez ejes políticos. El script preserva también el texto original de cada tema y los subtemas anidados de Política y Economía. El contenido histórico está en `fuentes/claude/` y no se modifica silenciosamente.
