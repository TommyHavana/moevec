# Inicio oficial del proyecto MEE

## Carpeta que debes abrir

Abre **`~/Documents/Proyectos/mee/mee-web/`** como carpeta local del proyecto. Es la raíz autocontenida: código React/Next.js, documentación, contenido generado, fuente original, imágenes y `brand-kit/`. No abras `fuentes/claude/` como proyecto independiente ni necesitas crear un repositorio Git.

Si partes de `MEE_Proyecto_Codex_Oficial.zip`, extráelo en una ubicación estable de tu ordenador y abre la carpeta `mee-web/` que contiene `package.json` y `AGENTS.md`. Si ya trabajas en la carpeta local `mee-web/`, sigue ahí; el ZIP sirve como copia transportable.

## Puesta en marcha

En la terminal de la carpeta `mee-web/`:

```bash
node --version
npm --version
npm ci
npm run dev
```

Abre `http://localhost:3000`. Detén el servidor con `Ctrl+C`. Después, para comprobar que todo compila:

```bash
npm run build
```

`npm run build` sincroniza primero la taxonomía y el editorial desde sus fuentes, y genera `out/`. No hace falta WordPress, Docker, base de datos ni credenciales para esta fase. Si npm indica que falta Node o que la versión instalada es incompatible, actualiza Node y repite `npm ci`; anota el error concreto antes de modificar dependencias.

Sin Git, crea un respaldo antes de cada cambio grande y al cerrar cada sesión con `npm run backup`. El comando deja un ZIP fechado en `mee-backups/`, al lado de `mee-web/`; excluye dependencias, compilados y archivos `.env` privados. Conserva una copia de ese ZIP en otro lugar de tu ordenador.

## Qué hay dentro

| Ruta | Función |
| --- | --- |
| `AGENTS.md` | Reglas vigentes para; leer primero. |
| `docs/00-LEER-PRIMERO.md` | Fuentes, decisiones y orden de lectura. |
| `prompts/INICIO-CODEX.md` | Encargo ejecutable para la primera sesión oficial. |
| `app/`, `lib/`, `content/`, `scripts/` | React/Next, navegación, datos y sincronización editorial. |
| `public/images/areas/` | Siete escenas originales y sus variantes. |
| `brand-kit/` | SVG, PNG/WebP, tipografía, licencias, colores y guía de uso. |
| `fuentes/claude/` | Material original preservado como fuente histórica. |
| `wordpress/` | Esqueleto anterior, aparcado hasta cerrar React. |

## Primer trabajo para Codex

Pega el contenido de `prompts/INICIO-CODEX.md` en una nueva tarea de Codex con `mee-web/` abierto. La tarea inicial actual se define en el prompt: preparar un piloto de imagen y movimiento semántico desde el estado existente, sin ejecutar todavía la auditoría total. Las comprobaciones necesarias para cambios autorizados se documentan por separado. Mantén las siete categorías y sus temas originales. La referencia de experiencia es `https://turnerduckworth.com/`, pero los recursos visuales y el contenido publicados en MEE son propios.

## Hecho y todavía por validar

Hay una primera implementación con siete rutas, contenidos sincronizados, imagen por categoría, índice sticky, movimientos iniciales, logo, favicon y fuentes locales. Se verificó la compilación; quedan pendientes pruebas visuales tras la integración tipográfica, navegación con teclado en todas las rutas, dispositivo móvil real, contraste, conexión lenta y revisión editorial por el fundador. La marca reconstruida está lista para uso de pantalla y requiere comparación final con la referencia preferida antes de otros soportes.

**Condición para iniciar WordPress:** que el fundador apruebe el resultado React y pida pasar a la fase documentada en `09-WORDPRESS-DESPUES.md`.

Para reutilizar chats, ver `20-PROTOCOLO-DE-CHATS.md` y usar el estado 15 y el backlog 16 más recientes.
