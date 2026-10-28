# Primera entrega de producción editorial · 28/10/2026

## Alcance ejecutado

Por petición del fundador se retiraron las 115 maquetas y comenzó la producción del plan de 840 artículos. Se conservaron en la papelera de WordPress para recuperación, con copia previa de SQL y archivos en `/data/mee-backups/antes-produccion-840-20261028/`. El importador de maquetas está retirado y ya no se ejecuta durante el despliegue. Sus imágenes en Medios se conservan con el contenido recuperable; no se confunden con las nuevas ilustraciones.

**Terminadas y publicadas: 3/840. En curso al cerrar esta entrega: 0. Pendientes: 837, n.º 4–840.**

| N.º | Ficha | Artículo publicado | Imágenes propias |
|---:|---|---|---:|
| 1 | E5.1.01 | [Qué es el capitalismo (y qué no es)](https://moevec.org/blog/que-es-el-capitalismo/) | 3/3 |
| 2 | E5.1.02 | [Capitalismo no es consumismo: la tesis de Bastos](https://moevec.org/blog/capitalismo-no-es-consumismo/) | 3/3 |
| 3 | E5.1.03 | [El sistema de precios](https://moevec.org/blog/sistema-de-precios-coordinacion/) | 3/3 |

Siguiente pendiente: **n.º 4/840 · E5.1.04 · Capitalismo de mercado y capitalismo de amiguetes**, tanda 1/56, entrada 4/15. Esta entrega inicia el plan; no presenta las 840 como producidas ni promete ejecución desatendida posterior.

## Registro individual

- [Markdown de las 840 entradas, una fila por artículo](24-REGISTRO-PRODUCCION-840.md).
- [CSV completo](../inventario/plan-editorial-840.csv) y [comprobación JSON](../inventario/plan-editorial-840-status.json).
- [WordPress → Herramientas → Plan editorial · 840](https://moevec.org/blog/wp-admin/tools.php?page=mee-production), accesible con una cuenta editorial. También existe una página privada «Registro de producción MEE» con el mismo registro dinámico.
- La numeración global conserva el orden de las tandas definidas; cada fila mantiene además el ID original y su posición dentro de la tanda.
- «Terminada» exige publicación, revisión registrada, extensión suficiente y tres archivos WebP distintos con alt y asignación al mismo ID editorial. La revisión de las escenas, fuentes y afirmaciones se documenta por artículo; la comprobación automática no sustituye esa revisión.
- Para actualizar la exportación desde el servidor: `python3 scripts/sync-production-status.py`.

## Texto, investigación e imágenes

Cada artículo incluye respuesta inicial, ejemplos identificados como ilustrativos, argumento contrario, lectura de MEE, ejercicio práctico, preguntas frecuentes, enlaces a rutas existentes y fuentes con fecha de consulta. Anacleto se presenta como firma editorial de MEE, sin identidad personal o credenciales inventadas. La segunda entrada incorpora el aviso educativo financiero.

Se consultaron fuentes primarias de Smith, Marx, Bastos, Keynes, Hayek y Pigou, además de las explicaciones institucionales del FMI y OpenStax. Los manifiestos registran las URL y el alcance utilizado. Se descartaron afirmaciones sin pasaje verificado: entre ellas la primera aparición del término «capitalismo», atribuciones a libros no consultados y efectos empíricos no investigados. El ejemplo del estaño se identifica expresamente como hipotético.

Las nueve escenas se generaron con la herramienta integrada **image_gen.imagegen**, una generación por recurso. Se inspeccionaron sus composiciones, ausencia de texto y relación conceptual. Se exportaron a WebP de calidad 80: portadas de 1200 × 630 e interiores de 1600 × 900, todos inferiores a 250 KB. WordPress genera las variantes responsive; las interiores tienen dimensiones, texto alternativo y carga diferida.

| Artículo | Archivos finales y prompts |
|---|---|
| E5.1.01 | [Manifiesto de las tres imágenes](../editorial/articles/E5.1.01/article.json) · [Prompts exactos](../editorial/articles/E5.1.01/image-prompts.json) · carpeta `editorial/articles/E5.1.01/` |
| E5.1.02 | [Manifiesto de las tres imágenes](../editorial/articles/E5.1.02/article.json) · [Prompts exactos](../editorial/articles/E5.1.02/image-prompts.json) · carpeta `editorial/articles/E5.1.02/` |
| E5.1.03 | [Manifiesto de las tres imágenes](../editorial/articles/E5.1.03/article.json) · [Prompts exactos](../editorial/articles/E5.1.03/image-prompts.json) · carpeta `editorial/articles/E5.1.03/` |

## Integración y verificación

Se sustituyeron los enlaces a maquetas de React por archivos editoriales de sus temas, preservando la jerarquía. Las URL retiradas redirigen al archivo correspondiente, también en temas políticos internos. El índice de lectura se genera de los H2 reales del artículo. Se ajustaron títulos sin partición de palabras, lectura de subtítulos y fechas en español.

SEO: título y descripción por artículo, canonical, OG/Twitter y schema Article. Las tres publicaciones están en el sitemap de WordPress; las maquetas no aparecen. Los archivos de nivel «fundamentos/desarrollo/aplicacion» llevan noindex y se excluyen del sitemap. `robots.txt` anuncia tanto el sitemap de React como el de WordPress. Esto permite el descubrimiento; no demuestra indexación efectiva por un buscador.

Compilación de Next y TypeScript correctas; lint PHP correcto en los módulos modificados. La comprobación de 16 rutas (12 de React, blog y tres artículos) terminó sin fallos. Las evidencias de la retirada, las rutas, los recursos, la lectura móvil y el estado posterior al despliegue quedan en `inventario/auditoria-2026-10-28/`. Las mediciones de Lighthouse de la auditoría anterior no se atribuyen como mediciones nuevas de estas tres entradas.

Versión de producto desplegada: `423f3b4`. Se compararon por SHA-256 cinco archivos del plugin y tema con el volumen de producción. Después del arranque se mantuvieron 0 maquetas públicas y 3 entradas terminadas. Copia posterior SQL/archivos en `/data/mee-backups/produccion-840-primeras-3-20261028/`. Lectura comprobada a 390 px en entradas 1 y 3, sin desbordamiento horizontal; navegador restablecido a su configuración normal.
