import { readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const source = resolve(root, "docs/03-EDITORIAL-CATEGORIAS.md");
const target = resolve(root, "content/editorial.json");
const taxonomy = JSON.parse(readFileSync(resolve(root, "content/taxonomia.json"), "utf8"));
const chunks = readFileSync(source, "utf8").split(/^## 0?([1-7]) · (.+)$/m);
const categories = [];
for (let i = 1; i < chunks.length; i += 3) {
  const number = Number(chunks[i]);
  const name = chunks[i + 1];
  const text = chunks[i + 2];
  const promise = text.match(/\*\*Promesa:\*\*\s+([^\n]+)/);
  const beforeTopics = text.split(/\*\*Subcategorías(?: y beneficio que debe mostrar la página)?:\*\*|\*\*Diez ejes y beneficio para el lector:\*\*/)[0];
  const paragraphs = beforeTopics.split(/\n\s*\n/).map((p) => p.trim()).filter((p) => p && !p.startsWith("**Pregunta"));
  const benefits = [...text.matchAll(/^\d+\. \*\*(.+?):\*\*\s+(.+)$/gm)].map((m) => ({ name: m[1], benefit: m[2].trim() }));
  const reference = taxonomy.categories[number - 1];
  const expected = number === 7 ? reference.groups : reference.topics;
  if (name !== reference.name || !promise || paragraphs.length < 2 || benefits.length !== expected.length || benefits.some((x, n) => x.name !== expected[n].name)) {
    throw new Error(`Editorial y taxonomía no coinciden en ${name}: se esperaban ${expected.length} etiquetas en el mismo orden.`);
  }
  categories.push({ number, slug: reference.slug, name, promise: promise[1], intro: paragraphs[0], detail: paragraphs[1], benefits });
}
if (categories.length !== 7) throw new Error("Faltan resúmenes editoriales.");
writeFileSync(target, JSON.stringify({ source: "docs/03-EDITORIAL-CATEGORIAS.md", categories }, null, 2) + "\n");
console.log("Editorial sincronizado: siete resúmenes y 56 beneficios en el orden del ZIP original.");
