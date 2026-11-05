import fs from 'node:fs/promises';import sharp from 'sharp';
const root='/Users/nerea/Documents/Proyectos/MEE/mee-web',dir=root+'/editorial/social/assets/carousels';await fs.mkdir(dir,{recursive:true});
const pilot=JSON.parse(await fs.readFile(root+'/editorial/social/pilot.json','utf8'));
const logo=(await fs.readFile(root+'/brand-kit/pantallas/mee-logo-blanco-rojo-640.png')).toString('base64');
const esc=t=>t.replaceAll('&','&amp;').replaceAll('<','&lt;');
function wrap(t,n){let a=[''];for(const w of t.split(' ')){let i=a.length-1;if((a[i]+' '+w).trim().length>n)a.push(w);else a[i]=(a[i]+' '+w).trim();}return a;}
for(const post of pilot.filter((p,i)=>[0,4,8].includes(i))){
 for(let i=0;i<post.carousel.length;i++){
  const slide=post.carousel[i],head=wrap(slide.headline,23),body=wrap(slide.text,36),bodyY=260+head.length*86;
  const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350"><rect width="1080" height="1350" fill="#1642cd"/><circle cx="1020" cy="130" r="290" stroke="#3d60d7" stroke-width="68" fill="none"/><image href="data:image/png;base64,${logo}" x="72" y="55" width="190" height="73"/><g font-family="Arial,sans-serif" fill="#fff" font-size="69" font-weight="900">${head.map((t,j)=>`<text x="72" y="${235+j*86}">${esc(t)}</text>`).join('')}</g><g font-family="Arial,sans-serif" fill="#fff" font-size="42">${body.map((t,j)=>`<text x="75" y="${bodyY+j*62}">${esc(t)}</text>`).join('')}</g><path d="M75 1160 H1005" stroke="#fff" stroke-width="2"/><text x="75" y="1220" font-family="Arial,sans-serif" font-size="32" fill="#fff">moevec.org · ${i+1}/${post.carousel.length}</text><text x="75" y="1275" font-family="Arial,sans-serif" font-size="28" fill="#fff">Lee el contexto y las fuentes en el artículo.</text></svg>`;
  const stem=dir+'/'+post.id+'-'+(i+1);await fs.writeFile(stem+'.svg',svg);await sharp(Buffer.from(svg)).png().toFile(stem+'.png');
 }
 post.ready_assets=post.carousel.map((_,i)=>'assets/carousels/'+post.id+'-'+(i+1)+'.png');post.asset_alt=post.carousel.map(s=>s.headline+'. '+s.text);
 const lines=post.video_script.map((s,i)=>`${i+1}\n00:00:${i===0?'00':i===1?'05':'18'},000 --> 00:00:${i===0?'05':i===1?'18':'28'},000\n${s.voice}\n`).join('\n');await fs.writeFile(dir+'/'+post.id+'.srt',lines);
}
await fs.writeFile(root+'/editorial/social/pilot.json',JSON.stringify(pilot,null,2)+'\n');console.log('Tres carruseles de cuatro diapositivas y sus guiones de subtítulos preparados.');
