# MEE · Movimiento de Evolución Económica

Proyecto oficial local con React/Next.js y el kit de marca en **una sola carpeta**. **Ahora se termina React; WordPress vendrá después.** Sin Git, sin GitHub Actions y sin despliegue. La fuente completa que aportó el fundador desde Claude se conserva en `fuentes/claude/`.

## Empezar en el ordenador

1. Abre **esta carpeta `mee-web`** como proyecto; no abras la carpeta `fuentes/claude` como proyecto principal.
2. Lee [la guía de inicio oficial](docs/12-INICIO-OFICIAL-CODEX.md), `AGENTS.md` y `docs/00-LEER-PRIMERO.md`. Si vas a trabajar el contenido, lee `docs/03-EDITORIAL-CATEGORIAS.md` y la fuente `fuentes/claude/docs/02-taxonomia.md`.
3. En la terminal de `mee-web`, ejecuta `npm ci`; `npm run build` sincroniza el contenido automáticamente.
4. Ejecuta `npm run dev` y abre `http://localhost:3000`.
5. Revisa la portada, las siete áreas y los índices fijos a cada ancho indicado en `docs/05-DISENO-Y-ASSETS.md`.
6. Después de ajustar textos y diseño, ejecuta `npm run build` y sigue `docs/08-VERIFICACION-Y-ENTREGA.md`.

Sin Git, usa `npm run backup` antes de cambios grandes y al finalizar cada sesión: genera una copia fechada en la carpeta hermana `mee-backups/`, excluyendo `node_modules`, `.next`, `out` y archivos de entorno privados.

El 27/10/2026 se instalaron las dependencias, se generó `package-lock.json`, `npm run build` terminó y se revisó la portada completa en Chrome a 1440 y 390 px. Repite la instalación y las pruebas en tu ordenador cuando continúes. No se necesita WordPress para trabajar en React.

## Documentos imprescindibles

| Documento | Uso |
| --- | --- |
| [Punto de entrada](docs/00-LEER-PRIMERO.md) | Fuente, decisiones recientes y orden de lectura |
| [Presentación de categorías y subcategorías](docs/11-PRESENTACION-CATEGORIAS-Y-SUBCATEGORIAS.md) | Texto breve para portada y páginas de las siete áreas y sus 56 apartados |
| [Visión y público](docs/01-VISION-Y-PUBLICO.md) | Misión, audiencia, método y límites |
| [Mapa de contenidos](docs/02-MAPA-DE-CONTENIDOS.md) | Jerarquía auténtica y reglas de navegación |
| [Siete resúmenes editoriales](docs/03-EDITORIAL-CATEGORIAS.md) | Tesis de cada área y 56 beneficios propuestos |
| [Arquitectura React](docs/04-ARQUITECTURA-REACT.md) | Rutas, fuente de datos y exportación |
| [Diseño y activos](docs/05-DISENO-Y-ASSETS.md) | Referencia, paleta, imágenes y responsive |
| [Plan React](docs/06-PLAN-REACT.md) | Secuencia de implementación |
| [Criterios editoriales](docs/07-CRITERIOS-EDITORIALES.md) | Evidencia, voz y revisión |
| [Verificación](docs/08-VERIFICACION-Y-ENTREGA.md) | Checklist antes de cerrar React |
| [WordPress después](docs/09-WORDPRESS-DESPUES.md) | Documento histórico; estado vigente en el informe 22 |
| [Decisiones abiertas](docs/10-DECISIONES-ABIERTAS.md) | Conflictos y aprobaciones pendientes |
| [Inicio oficial Codex](docs/12-INICIO-OFICIAL-CODEX.md) | Carpeta, comandos y primera tarea |
| [Prompt inicial Codex](prompts/INICIO-CODEX.md) | Encargo listo para copiar |

## Estado actual

React está publicado en `https://moevec.org/` y WordPress en `https://moevec.org/blog/`. Hay siete áreas, 115 ilustraciones de tema, 115 entradas de maqueta y una página React de contacto con SMTP y confirmación HTML. La identidad y el movimiento se comparten entre ambas plataformas. Las muestras no se indexan; Search Console tiene el dominio verificado y el sitemap con 12 páginas públicas. La auditoría, las mediciones y los pendientes externos están en `docs/22-AUDITORIA-UIUX-WPO-SEO-GEO.md`. Los datos de fuente se sincronizan por scripts; no editar JSON generado a mano.
