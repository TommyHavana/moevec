import { areas } from '../lib/areas';
import { pageMeta } from '../lib/seo';
export const metadata=pageMeta('MEE · El futuro se hace en común','Explora siete áreas para desarrollar capacidades, compartir conocimiento y participar en la evolución económica. Descubre el movimiento MEE.','/');
export default function HomePage(){
 return <main id="contenido">
  <section className="landing-intro" data-motion-hero data-ambient aria-labelledby="titulo">
   <div className="ambient-field" aria-hidden="true"><i/><i/><i/><i/><i/></div>
   <div className="landing-intro-copy"><p className="hero-context">Movimiento de Evolución Económica</p>
    <h1 id="titulo"><span className="hero-line"><span className="hero-word">El futuro</span></span><span className="hero-line"><span className="hero-word">se hace</span></span><span className="hero-line"><span className="hero-word">en común<span className="title-dot">.</span></span></span></h1>
    <div className="intro-bottom"><p>Ideas que se convierten en capacidades.<br/>Personas que abren posibilidades.</p><a href="#areas" className="pill-link">Explorar las áreas <span aria-hidden="true">↓</span></a></div>
   </div>
   <div className="intro-orbit" aria-hidden="true"><div className="orbit-tilt"><div className="orbit-body"><div className="orbit-ridges"/><div className="orbit-shine"/><div className="orbit-satellite"/></div></div></div>
   <span className="hero-caption" aria-hidden="true">Todo empieza con un movimiento.</span>
  </section>
  <section className="areas-section" id="areas" aria-labelledby="areas-title"><div className="areas-heading"><p className="eyebrow">Un mapa para pasar a la acción</p><h2 id="areas-title">Siete maneras<br/>de avanzar.</h2><p>Aprender, aportar, crear. Cada área abre una forma de participar en lo que viene.</p></div>
   <div className="area-grid">{areas.map((area,index)=><a className={`area-card area-card-${index}`} data-ambient href={`/areas/${area.slug}/`} key={area.slug}><picture><img src={`/images/areas/${area.slug}-680.webp`} srcSet={`/images/areas/${area.slug}-480.webp 480w, /images/areas/${area.slug}-680.webp 680w, /images/areas/${area.slug}.webp 1254w`} alt="" width="1254" height="1254" loading="lazy" sizes="(max-width:640px) 100vw, 50vw"/></picture><span className="area-card-shade" aria-hidden="true"/><span className="area-card-top"><span>{area.sections.length} temas para explorar</span><span aria-hidden="true">↗</span></span><span className="area-card-title">{area.name}</span><span className="card-orbit" aria-hidden="true"/></a>)}
   <div className="grid-outro" data-ambient><img className="asterisk" src="/brand/mee-estrella-blanca-256.webp" alt="" aria-hidden="true" width="256" height="256"/><p>Las ideas crecen cuando se encuentran.</p><a href="/blog/">Abrir el editorial</a></div></div>
  </section>
  <section className="home-thesis"><p className="eyebrow">Qué nos mueve</p><h2>La economía también<br/>se construye entre personas.</h2><div><p>MEE reúne educación, valores, comunidad y trabajo para pensar cómo creamos y compartimos valor. Un lugar para entender las reglas, desarrollar criterio y convertir el conocimiento en capacidad de acción.</p><a className="text-link" href="/sobre-mee/">Conocer el movimiento</a></div></section>
 </main>;
}
