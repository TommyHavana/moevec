import type { Metadata } from 'next';
export const origin = 'https://moevec.org';
export const siteName = 'MEE · Movimiento de Evolución Económica';
export function pageMeta(title:string, description:string, path:string, image='/brand/mee-social-1200x630.webp'):Metadata {
  return {title:{absolute:title.includes('MEE')?title:`${title} | MEE`},description,alternates:{canonical:origin+path},openGraph:{type:'website',locale:'es_ES',siteName,title,description,url:origin+path,images:[{url:image,width:1200,height:630,alt:title}]},twitter:{card:'summary_large_image',title,description,images:[image]}};
}
export function JsonLd({data}:{data:Record<string,unknown>}){
  return <script type="application/ld+json" dangerouslySetInnerHTML={{__html:JSON.stringify(data).replace(/</g,'\\u003c')}}/>;
}
export function Breadcrumbs({items}:{items:{name:string;path:string}[]}) {
  return <><nav className="breadcrumbs" aria-label="Ruta de navegación"><ol>{items.map((item,i)=><li key={item.path}>{i===items.length-1?<span aria-current="page">{item.name}</span>:<a href={item.path}>{item.name}</a>}</li>)}</ol></nav><JsonLd data={{'@context':'https://schema.org','@type':'BreadcrumbList',itemListElement:items.map((x,i)=>({'@type':'ListItem',position:i+1,name:x.name,item:origin+x.path}))}}/></>;
}
