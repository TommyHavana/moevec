import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import sharp from 'sharp';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const plan=JSON.parse(await fs.readFile(path.join(root,'wordpress/plugins/mee-editorial/data/production-plan.json'),'utf8'));
for(const id of process.argv.slice(2)){
 const entry=plan.find(x=>x.id===id);if(!entry)throw new Error('ID ajeno al plan: '+id);
 const dir=path.join(root,'editorial/articles',id);
 const spec=JSON.parse(await fs.readFile(path.join(dir,'image-prompts.json'),'utf8'));
 const result={};
 for(const role of ['featured','interior-1','interior-2']){
  const source=spec.sources[role];if(!source)throw new Error('Falta imagen generada '+id+' '+role);
  const width=role==='featured'?1200:1600,height=role==='featured'?630:900;
  const name=id.toLowerCase().replaceAll('.','-')+'-'+entry.slug+'-'+(role==='featured'?'destacada':role)+'.webp';
  const output=path.join(dir,name);let quality=80;
  while(true){await sharp(source).resize(width,height,{fit:'cover'}).webp({quality,effort:6}).toFile(output);if((await fs.stat(output)).size<250000)break;quality-=4;if(quality<64)throw new Error('Imagen demasiado pesada: '+output);}
  result[role]={file:name,width,height,bytes:(await fs.stat(output)).size,quality};
 }
 await fs.writeFile(path.join(dir,'assets.json'),JSON.stringify(result,null,2)+'\n');
 console.log(JSON.stringify({id,assets:result}));
}
