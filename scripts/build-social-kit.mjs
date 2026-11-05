import fs from 'node:fs/promises';
import sharp from 'sharp';
const root='/Users/nerea/Documents/Proyectos/MEE/mee-web';
const paths=JSON.parse(await fs.readFile(root+'/wordpress/plugins/mee-editorial/data/reading-paths.json','utf8'));
const logo=(await fs.readFile(root+'/brand-kit/pantallas/mee-logo-blanco-rojo-640.png')).toString('base64');
const star=(await fs.readFile(root+'/brand-kit/pantallas/mee-estrella-roja-256.png')).toString('base64');
const escape=t=>t.replaceAll('&','&amp;').replaceAll('<','&lt;');
const wrap=(text,max=26)=>{let lines=[''];for(const w of text.split(' ')){let i=lines.length-1;if((lines[i]+' '+w).trim().length>max)lines.push(w);else lines[i]=(lines[i]+' '+w).trim();}return lines;};
const target=root+'/public/brand/rutas';await fs.mkdir(target,{recursive:true});
const source=root+'/editorial/social/assets';await fs.mkdir(source,{recursive:true});
const cards=[{slug:'empieza-aqui',title:'Empieza por lo que te importa',subtitle:'Tres rutas para conectar ideas y decisiones'},...paths.map(p=>({slug:p.slug,title:p.title,subtitle:'Seis lecturas para avanzar a tu ritmo'}))];
for(const c of cards){
 const lines=wrap(c.title);
 const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="#1642cd"/><circle cx="1130" cy="100" r="290" fill="none" stroke="#4166db" stroke-width="70"/><image href="data:image/png;base64,${logo}" x="65" y="42" width="175" height="67"/><image href="data:image/png;base64,${star}" x="960" y="390" width="170" height="170"/><g fill="#fff" font-family="Arial,sans-serif" font-weight="900" font-size="72">${lines.map((l,i)=>`<text x="65" y="${220+i*86}">${escape(l)}</text>`).join('')}</g><text x="68" y="${Math.max(478,240+lines.length*86)}" fill="#fff" font-family="Arial,sans-serif" font-size="28">${escape(c.subtitle)}</text><text x="68" y="574" fill="#fff" font-family="Arial,sans-serif" font-size="25">moevec.org/empieza-aqui</text></svg>`;
 await fs.writeFile(source+'/'+c.slug+'.svg',svg);await sharp(Buffer.from(svg)).webp({quality:88}).toFile(target+'/'+c.slug+'.webp');
}
// Square avatar and portrait post cover use approved screen-brand assets.
await sharp({create:{width:1080,height:1080,channels:4,background:'#1642cd'}}).composite([{input:await sharp(root+'/brand-kit/pantallas/mee-logo-blanco-rojo-640.png').resize(780).toBuffer(),gravity:'centre'}]).png().toFile(source+'/avatar-1080.png');
const pilot=[];const chosen=paths.flatMap(p=>p.steps.slice(0,4).map((s,i)=>({p,s,i})));const prompts=['¿Qué pregunta te ayudaría a empezar?','Una idea para revisar con calma','Lleva la lectura a una decisión','Qué información te falta todavía'];
for(let i=0;i<chosen.length;i++){
 const {p,s}=chosen[i];const slug='piloto-'+String(i+1).padStart(2,'0');
 const url=new URL(s.url);url.search=new URLSearchParams({utm_source:'facebook',utm_medium:'organic_social',utm_campaign:'rutas_2026_11',utm_content:s.id.toLowerCase().replaceAll('.','_')+'_enlace'}).toString();
 const body=`${s.title}\n\n${s.purpose}\n\nLee el artículo, consulta sus fuentes y compara sus argumentos. Forma parte de la ruta «${p.title}».\n\n${url}`;
 pilot.push({id:slug,week:Math.floor(i/3)+1,article_id:s.id,title:s.title,source_article:s.url,core:'Invitación a una lectura existente; sin cifras ni promesas adicionales',facebook_copy:body,instagram_copy:`${s.title}\n\n${s.purpose}\n\nEncuentra esta lectura en la ruta «${p.title}», desde Empieza aquí en moevec.org.`,carousel:[{headline:s.title,text:prompts[i%4]},{headline:'La pregunta de esta lectura',text:s.purpose},{headline:'Antes de llevarla a tu situación',text:'Comprueba la fecha, el país y el alcance de las fuentes del artículo.'},{headline:'Continúa la ruta',text:p.title+' · moevec.org/empieza-aqui'}],video_script:[{seconds:'0–5',voice:s.title},{seconds:'5–18',voice:s.purpose},{seconds:'18–28',voice:'Lee el contexto y las fuentes en MEE. Continúa desde la ruta '+p.title+'.'}],subtitles_required:true,visual_source:'Ilustraciones originales del artículo; adaptar encuadre con revisión',status:'preparado; sin programar ni publicar',published_url:null,reviewed_on:'2026-11-05'});
}
await fs.writeFile(root+'/editorial/social/pilot.json',JSON.stringify(pilot,null,2)+'\n');
await fs.writeFile(root+'/editorial/social/GUIA.md',`# MEE · preparación social\n\nBio: Ideas, fuentes y ejemplos para organizar tus finanzas, desarrollar capacidades y entender la economía. Empieza por una ruta en moevec.org/empieza-aqui/.\n\nNombre propuesto: MEE · Movimiento de Evolución Económica. Verificar disponibilidad antes de registrar un handle. El avatar utiliza el logo de pantalla aprobado.\n\nPaleta: azul #1642cd, rojo de la marca existente, blanco y tinta. Mantener márgenes del 8%, título legible y logo sin deformar. Las tarjetas de rutas están listas para compartir; los SVG son fuentes editables. Carrusel propuesto 1080×1350 y vídeo 1080×1920: son formatos de producción, comprobar encuadre y límites al subir a cada canal. Subtítulos legibles dentro de la zona segura.\n\nPilot.json contiene 12 ideas, copias por canal, guion breve y secuencia de carrusel. Estado preparado no equivale a publicado. Completar conexión, revisar la previsualización y registrar URL real al publicar. No publicar automáticamente desde este archivo.\n\nPiezas fijadas: presentación de MEE, las tres rutas y método editorial. En debates: respeto, fuentes, desacuerdo argumentado y protección de datos personales. Identificar publicidad si llega a existir.\n`);
console.log('Cuatro tarjetas sociales, avatar y 12 ideas preparadas.');
