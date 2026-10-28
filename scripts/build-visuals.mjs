import fs from 'node:fs/promises';
import path from 'node:path';
import sharp from 'sharp';
const {categories} = JSON.parse(await fs.readFile('content/taxonomia.json','utf8'));
const {categories:copy} = JSON.parse(await fs.readFile('content/editorial.json','utf8'));
const inventory = await fs.readFile('docs/19-INVENTARIO-VISUAL.md','utf8');
const metaphors = new Map([...inventory.matchAll(/^\| `([^`]+)` \| ([^|]+) \| ([^|]+) \| ([^|]+) \|/gm)].map(m=>[m[1],{concept:m[3].trim(),action:m[4].trim()}]));
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]));
await fs.mkdir('public/images/topics',{recursive:true});
await fs.mkdir('wordpress/plugins/mee-editorial/data',{recursive:true});
const manifest=[];
const palette=[['#1649c3','#fa494b','#abc7ff'],['#e73543','#1547bb','#ffbdac'],['#1255ae','#ff8b51','#acd6e8'],['#ff642e','#193e94','#ffd082'],['#0a6158','#ef554b','#b3dac7'],['#2355d5','#ed4443','#b9cdfa'],['#192e69','#ef4547','#c1bfd8']];
function art(area,index,depth=0){
 const [base,accent,light]=palette[area], p=index%6, n=4+index%4;
 const defs=`<defs><linearGradient id="base" x2="1" y2="1"><stop stop-color="${light}"/><stop offset="1" stop-color="${base}"/></linearGradient><linearGradient id="material" x2=".7" y2="1"><stop stop-color="#fff"/><stop offset=".45" stop-color="${light}"/><stop offset="1" stop-color="${base}"/></linearGradient><linearGradient id="hot" x2="1" y2="1"><stop stop-color="#ffc3ae"/><stop offset=".45" stop-color="${accent}"/><stop offset="1" stop-color="#a9213b"/></linearGradient><filter id="shadow" x="-.5" y="-.5" width="2" height="2"><feDropShadow dx="0" dy="24" stdDeviation="20" flood-color="#071133" flood-opacity=".28"/></filter></defs>`;
 let shapes='';
 // Distinct editorial families, each with individual geometry and composition.
 if(area===0){ // autonomy, learning, balance: suspended open sheets / orbiting choices
  shapes=Array.from({length:n},(_,j)=>`<g transform="translate(${180+j*113},${210+Math.sin(j+p)*80}) rotate(${(j-n/2)*12})"><path d="M0 60 Q85 5 165 50 L165 365 Q75 310 0 360Z" fill="url(#${j===p%n?'hot':'material'})"/><path d="M20 105 Q80 65 145 98M20 140 Q80 100 145 133M20 175 Q80 135 145 168" stroke="${base}" opacity=".3" stroke-width="6"/></g>`).join('');
 }else if(area===1){ // generations: rooted interconnected arches
  shapes=Array.from({length:n},(_,j)=>`<path d="M${150+j*110} 620 V${340-j*24} Q${245+j*110} ${150-j*13} ${340+j*110} ${340-j*24} V620" fill="none" stroke="url(#${j%2?'hot':'material'})" stroke-width="70"/>`).join('')+`<circle cx="${320+p*70}" cy="${235+p*13}" r="48" fill="${accent}"/>`;
 }else if(area===2){ // transparent exchange: linked glass-like gates
  shapes=Array.from({length:n},(_,j)=>`<g transform="translate(${165+j*115},${200+(j%2)*105}) rotate(${j%2?-24:24})"><rect width="200" height="250" rx="80" fill="none" stroke="url(#${j%2?'hot':'material'})" stroke-width="55"/><circle cx="100" cy="125" r="17" fill="#fff" opacity=".8"/></g>`).join('');
 }else if(area===3){ // skills: rising bridge of crafted modules
  shapes=Array.from({length:n},(_,j)=>`<g transform="translate(${150+j*118},${510-j*(28+p*4)})"><path d="M0 0L130 -65L225 -10L95 55Z" fill="${light}"/><path d="M0 0L95 55V160L0 105Z" fill="url(#material)"/><path d="M95 55L225 -10V95L95 160Z" fill="${j===p%n?accent:base}"/></g>`).join('')+`<path d="M140 340Q530 ${40+p*18} 950 190" stroke="${accent}" stroke-width="20" fill="none" stroke-dasharray="12 22"/>`;
 }else if(area===4){ // value ecosystem: leaves, roots and an open vessel
  shapes=`<path d="M330 560Q600 780 870 560L810 730H390Z" fill="url(#hot)"/><path d="M600 625V190" stroke="url(#material)" stroke-width="36"/>`+Array.from({length:n},(_,j)=>`<g transform="translate(600,${550-j*65}) rotate(${j%2?-55:55})"><path d="M0 0Q-150 -150 0 -250Q150 -150 0 0" fill="url(#${j===p%n?'hot':'material'})"/><path d="M0 -20V-210" stroke="${base}" opacity=".4" stroke-width="5"/></g>`).join('');
 }else if(area===5){ // distributed resources: nodes and shared central object
  shapes=Array.from({length:n},(_,j)=>{const a=j*2*Math.PI/n+p*.13,x=600+Math.cos(a)*320,y=410+Math.sin(a)*245;return `<path d="M600 410L${x} ${y}" stroke="${light}" stroke-width="14"/><circle cx="${x}" cy="${y}" r="${45+j*4}" fill="url(#${j%2?'hot':'material'})"/>`}).join('')+`<path d="M600 260L740 340V500L600 580L460 500V340Z" fill="url(#material)"/><path d="M600 260V580M460 340L740 500M740 340L460 500" stroke="${accent}" stroke-width="10"/>`;
 }else{ // rules: open architectural frames and alternate paths
  shapes=Array.from({length:n},(_,j)=>`<g transform="translate(${160+j*100},${185+j*24})"><path d="M0 390V0H${320-p*14}V390" fill="none" stroke="url(#${j===p%n?'hot':'material'})" stroke-width="34"/><path d="M0 390H320" stroke="${accent}" stroke-width="14"/></g>`).join('')+`<path d="M170 710Q420 500 1010 ${620-p*20}" stroke="${accent}" fill="none" stroke-width="18" stroke-dasharray="10 18"/>`;
 }
 return `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="900" viewBox="0 0 1200 900">${defs}<rect width="1200" height="900" fill="${base}"/><circle cx="${180+p*115}" cy="100" r="570" fill="${light}" opacity=".12"/><ellipse cx="600" cy="750" rx="420" ry="45" fill="#071133" opacity=".14"/><g filter="url(#shadow)" transform="translate(${depth*7},${depth*-7})">${shapes}</g><path d="M70 790H1130" stroke="#fff" opacity=".2"/></svg>`;
}
for (const [ai,c] of categories.entries()) {
 const source=`inventario/originales/areas/${c.slug}.jpg`;
 for(const width of [480,680,1254]) {
  const dest=`public/images/areas/${c.slug}${width===1254?'':`-${width}`}.webp`;
  await sharp(source).resize(width).webp({quality:80,effort:6}).toFile(dest);
 }
 const list=c.number===7?c.groups:c.topics;
 let counter=0;
 async function walk(topics,parent=null,depth=0){
  for(const [i,t] of topics.entries()){
   const ix=counter++, visual=metaphors.get(t.slug)||{concept:`Arquitectura abierta para ${t.name}`,action:'Las relaciones entre los elementos se hacen visibles.'};
   const benefit=depth===0?copy[ai].benefits[i].benefit:`Examinar ${t.name.toLowerCase()} en el contexto de ${c.name.toLowerCase()}.`;
   const file=`${c.slug}/${t.slug}`; await fs.mkdir(path.dirname(`public/images/topics/${file}`),{recursive:true});
   const svg=Buffer.from(art(ai,ix,depth));
   for(const width of [480,800,1200]) await sharp(svg).resize(width).webp({quality:80,effort:6}).toFile(`public/images/topics/${file}-${width}.webp`);
   manifest.push({area:c.slug,areaName:c.name,slug:t.slug,name:t.name,parent,depth,benefit,concept:metaphors.get(t.slug)?.concept||`Composición sobre ${t.name}`,action:metaphors.get(t.slug)?.action||'Los elementos conectan las reglas, las decisiones y sus efectos.',image:`/images/topics/${file}-1200.webp`,motion:['unfold','inherit','exchange','build','grow','connect','inspect'][ai]});
   const children=c.number===7&&depth===0?t.topics:t.children;
   if(children?.length) await walk(children,t.slug,depth+1);
  }
 }
 await walk(list);
}
// Metadata is generated from canonical source; no manual taxonomy edits.
await fs.writeFile('content/visuals.json',JSON.stringify(manifest,null,2)+'\n');
await fs.copyFile('content/visuals.json','wordpress/plugins/mee-editorial/data/topics.json');
const initialBytes=(await Promise.all(categories.flatMap(c=>[`${c.slug}.jpg`,`${c.slug}-680.jpg`]).map(f=>fs.stat('inventario/originales/areas/'+f)))).reduce((a,s)=>a+s.size,0);
const webpBytes=(await Promise.all(categories.flatMap(c=>[`${c.slug}.webp`,`${c.slug}-680.webp`]).map(f=>fs.stat('public/images/areas/'+f)))).reduce((a,s)=>a+s.size,0);
console.log(JSON.stringify({areas:categories.length,topics:manifest.length,mainTopics:manifest.filter(x=>!x.depth).length,internal:manifest.filter(x=>x.depth).length,areaBytesBefore:initialBytes,areaBytesAfter:webpBytes,reduction:1-webpBytes/initialBytes}));
