import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { areas, type Topic } from '../../../lib/areas';
import { pageMeta, Breadcrumbs } from '../../../lib/seo';
import AreaNavigation from './AreaNavigation';
import Conversation from './Conversation';
import visuals from '../../../content/visuals.json';
type Props={params:Promise<{slug:string}>};
export function generateStaticParams(){return areas.map(({slug})=>({slug}));}
export async function generateMetadata({params}:Props):Promise<Metadata>{const {slug}=await params;const area=areas.find(a=>a.slug===slug);return area?pageMeta(area.name,`${area.name}: ${area.lead.charAt(0).toUpperCase()+area.lead.slice(1)} Explora sus temas, capacidades y preguntas.`,`/areas/${slug}/`,`/images/areas/${slug}-social.webp`):{};}
function TopicTree({topics,area}:{topics:Topic[];area:string}){return <div className="nested-topics">{topics.map(t=><details key={t.slug} className="nested-topic" id={t.slug}><summary>{t.name}<span aria-hidden="true">+</span></summary><div className="nested-topic-body"><img src={`/images/topics/${area}/${t.slug}-480.webp`} width="480" height="360" loading="lazy" alt={`Ilustración conceptual de ${t.name}`}/><div><p>Una perspectiva de {t.name.toLowerCase()} para conectar las reglas con sus efectos en la vida cotidiana.</p><a href={`/blog/muestra-${area}-${t.slug}/`}>Ver maqueta de este tema</a>{t.children?.length?<TopicTree topics={t.children} area={area}/>:null}</div></div></details>)}</div>}
export default async function AreaPage({params}:Props){
 const {slug}=await params,area=areas.find(a=>a.slug===slug);if(!area)notFound();const index=areas.findIndex(a=>a.slug===slug),next=areas[(index+1)%areas.length];
 return <main id="contenido" className="story-page"><Breadcrumbs items={[{name:'Inicio',path:'/'},{name:area.name,path:`/areas/${slug}/`}]}/>
  <section className="story-opening" aria-labelledby="story-title"><div className="story-heading"><p className="eyebrow">{area.sections.length} perspectivas para avanzar</p><h1 id="story-title">{area.name}<span className="title-dot">.</span></h1><p>{area.claim.charAt(0).toUpperCase()+area.claim.slice(1)}</p></div><div className="story-hero" data-ambient><picture><source media="(max-width:720px)" srcSet={`/images/areas/${slug}-680.webp`}/><img src={`/images/areas/${slug}.webp`} width="1254" height="1254" fetchPriority="high" alt={`Imagen conceptual de ${area.name}`}/></picture></div></section>
  <AreaNavigation areaName={area.name} sections={area.sections}/>
  <div className="story-content"><section className="story-thesis"><p className="eyebrow">Lo que podemos crear</p><h2>{area.lead.charAt(0).toUpperCase()+area.lead.slice(1)}</h2><p>{area.intro}</p><p className="story-detail">{area.detail}</p></section>
   <div className="chapter-list">{area.sections.map((s,i)=>{const v=visuals.find(v=>v.area===slug&&v.slug===s.slug);return <section className={`chapter chapter-${index}`} id={s.slug} key={s.slug} aria-labelledby={`${s.slug}-title`}><figure className={`chapter-visual motion-${v?.motion}`} data-ambient><picture><source media="(max-width:640px)" srcSet={`/images/topics/${slug}/${s.slug}-480.webp`}/><img src={`/images/topics/${slug}/${s.slug}-800.webp`} width="800" height="600" loading="lazy" alt={v?.concept||`Ilustración conceptual de ${s.name}`}/></picture><span className="visual-kinetic" aria-hidden="true"><i/><i/><i/></span><figcaption>{v?.concept||s.name}</figcaption></figure><div className="chapter-copy"><p className="chapter-index">Tema {i+1} de {area.sections.length}</p><h2 id={`${s.slug}-title`}>{s.name}</h2><p className="chapter-benefit">{s.benefit.charAt(0).toUpperCase()+s.benefit.slice(1)}</p><a className="chapter-read" href={`/blog/muestra-${slug}-${s.slug}/`}>Explorar la maqueta editorial <span aria-hidden="true">↗</span></a>{s.children.length?<TopicTree topics={s.children} area={slug}/>:null}</div></section>})}</div>
   <Conversation area={slug}/>
   <div className="editorial-link"><p>Una idea puede abrir<br/>la siguiente conversación.</p><a href={`/blog/category/${slug}/`}>Ver el editorial de {area.name}</a></div>
  </div><a className="next-area" href={`/areas/${next.slug}/`}><span>Siguiente área <span aria-hidden="true">↗</span></span><strong>{next.name}</strong></a>
 </main>;
}
