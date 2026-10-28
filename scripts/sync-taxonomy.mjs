import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const source = resolve(root, "fuentes/claude/docs/02-taxonomia.md");
const target = resolve(root, "content/taxonomia.json");
const lines = readFileSync(source, "utf8").split(/\r?\n/);

function slug(text) {
  return text.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase()
    .replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
}
function title(raw) {
  const bold = raw.match(/^\*\*(.*?)\*\*/);
  return (bold ? bold[1] : raw.split(/\s+—\s+/)[0])
    .replace(/\*\([^)]*\)\*/g, "").replace(/\*\*/g, "").trim();
}

const categories = [];
let category = null;
let group = null;
let lastTopic = null;
for (const line of lines) {
  const heading = line.match(/^## ([1-7])\. (.+)$/);
  if (heading) {
    const name = heading[2].split(/\s+—\s+/)[0].trim();
    category = { number: Number(heading[1]), slug: slug(name), name, topics: [], groups: [] };
    categories.push(category);
    group = null;
    continue;
  }
  if (!category) continue;
  const subheading = line.match(/^### 7\.([1-9][0-9]*) (.+)$/);
  if (subheading && category.number === 7) {
    group = { number: Number(subheading[1]), slug: slug(subheading[2]), name: subheading[2].trim(), topics: [] };
    category.groups.push(group);
    lastTopic = null;
    continue;
  }
  if (category.number < 7) {
    const item = line.match(/^\d+\.\s+(.+)$/);
    if (item) { const name = title(item[1]); category.topics.push({ slug: slug(name), name, original: item[1] }); }
  } else if (group) {
    const item = line.match(/^(-|  -)\s+(.+)$/);
    if (!item) continue;
    const name = title(item[2]);
    const topic = { slug: slug(name), name, original: item[2], children: [] };
    if (item[1] === "-") { group.topics.push(topic); lastTopic = topic; }
    else if (lastTopic) lastTopic.children.push(topic);
  }
}
if (categories.length !== 7 || categories[6].groups.length !== 10) throw new Error("Taxonomía incompleta: se esperan siete categorías y diez ejes políticos.");
if (categories.some((c) => c.number < 7 && !c.topics.length)) throw new Error("Faltan subcategorías.");
writeFileSync(target, JSON.stringify({ source: "fuentes/claude/docs/02-taxonomia.md", levels: ["Fundamentos", "Desarrollo", "Aplicación"], categories }, null, 2) + "\n");
console.log(`Taxonomía sincronizada: ${categories.length} categorías, ${categories.slice(0, 6).reduce((n, c) => n + c.topics.length, 0)} temas de teoría, ${categories[6].groups.length} ejes de aplicación.`);
