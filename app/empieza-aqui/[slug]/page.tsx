import {notFound} from 'next/navigation';
import {readingPaths} from '../../../lib/reading-paths';
import {Breadcrumbs,JsonLd,origin,pageMeta} from '../../../lib/seo';
import ReadingChecklist from '../ReadingChecklist';
type Props={params:Promise<{slug:string}>};
export function generateStaticParams(){return readingPaths.map(p=>({slug:p.slug}));}
export async function generateMetadata({params}:Props){const {slug}=await params;const path=readingPaths.find(p=>p.slug===slug);return path?pageMeta(path.title+' · Ruta de lectura MEE',path.intro,`/empieza-aqui/${slug}/`):{};}
export default async function ReadingPathPage({params}:Props){const {slug}=await params;const path=readingPaths.find(p=>p.slug===slug);if(!path)notFound();return <main id="contenido" className="reading-path">
 <Breadcrumbs items={[{name:'Inicio',path:'/'},{name:'Empieza aquí',path:'/empieza-aqui/'},{name:path.title,path:`/empieza-aqui/${slug}/`}]}/>
 <header className="reading-intro"><h1>{path.title}<span className="title-dot">.</span></h1><div><p>{path.intro}</p><p className="reading-duration">6 lecturas · unos {path.minutes} minutos en total</p></div></header>
 <section className="reading-outcome"><h2>Qué puedes llevarte</h2><p>{path.outcome}</p><p>Las fuentes, los ejemplos y los argumentos contrarios están en cada artículo. El tiempo de lectura es una estimación.</p></section>
 <ol className="reading-steps">{path.steps.map((step,i)=><li key={step.id}><span className="reading-step-number" aria-hidden="true">{String(i+1).padStart(2,'0')}</span><article><p className="reading-duration">{step.level} · unos {step.minutes} minutos</p><h2><a href={step.url}>{step.title}</a></h2><p>{step.purpose}</p><div className="reading-step-actions"><a className="text-link" href={step.url}>Leer este artículo <span aria-hidden="true">↗</span></a><ReadingChecklist id={step.id}/></div></article></li>)}</ol>
 <aside className="reading-local-note"><p>Las marcas de lectura se guardan solo en este navegador. No se envían a MEE y pueden perderse al borrar sus datos.</p></aside>
 <section className="reading-other"><h2>Después de la última lectura</h2><p>Anota una decisión que quieras revisar, qué información te falta y cuándo volverás a observarla.</p><div><a className="text-link" href="/empieza-aqui/">Elegir otra ruta</a><a className="text-link" href="/seguir-mee/">Seguir leyendo MEE</a><a className="text-link" href="/contacto/?tema=Propuesta%20editorial">Proponer una lectura</a></div></section>
 <JsonLd data={{'@context':'https://schema.org','@type':'CollectionPage','@id':origin+`/empieza-aqui/${slug}/#webpage`,name:path.title,url:origin+`/empieza-aqui/${slug}/`,description:path.intro,isPartOf:{'@id':origin+'/#website'},mainEntity:{'@type':'ItemList',itemListOrder:'https://schema.org/ItemListOrderAscending',numberOfItems:path.steps.length,itemListElement:path.steps.map((s,i)=>({'@type':'ListItem',position:i+1,url:s.url,name:s.title}))}}}/>
 </main>;}
