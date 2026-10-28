import { areas } from "../lib/areas";

export default function HomePage() {
  return <main id="contenido">
    <section className="landing-intro" data-motion-hero aria-labelledby="titulo"><div className="landing-intro-copy">
      <p className="eyebrow">Movimiento de Evolución Económica <span>· 01 / 02</span></p>
      <h1 id="titulo"><span className="hero-line">EL FUTURO</span><span className="hero-line"><em>SE HACE</em></span><span className="hero-line">EN COMÚN<span className="title-dot">.</span></span></h1>
      <div className="intro-bottom"><p>Ideas que se convierten en capacidades. Capacidades que abren nuevas posibilidades.</p><a href="#areas" className="pill-link">Explorar las áreas <span aria-hidden="true">↓</span></a></div>
    </div><span className="intro-orbit" aria-hidden="true" /></section>
    <section className="areas-section" id="areas" aria-labelledby="areas-title"><div className="areas-heading" data-reveal>
      <p className="eyebrow">Mapa de posibilidades <span>· 02 / 02</span></p><h2 id="areas-title">Siete maneras<br />de <em>avanzar.</em></h2><p>Entra en un área para descubrir qué capacidad puede crear en la vida de las personas.</p>
    </div><div className="area-grid">{areas.map((area, index) => <a className="area-card" data-reveal href={`/areas/${area.slug}/`} key={area.slug} aria-label={`Explorar ${area.name}`}>
      <picture><source media="(max-width: 720px)" srcSet={`/images/areas/${area.slug}-680.jpg`} /><img src={`/images/areas/${area.slug}.jpg`} alt="" width="1254" height="1254" loading={index < 3 ? "eager" : "lazy"} /></picture>
      <span className="area-card-shade" aria-hidden="true"/><span className="area-card-top"><span>{String(index + 1).padStart(2, "0")} / 07</span><span aria-hidden="true">↗</span></span><span className="area-card-title">{area.name}</span>
    </a>)}<div className="grid-outro" data-reveal><img className="asterisk" src="/brand/mee-estrella-blanca-256.webp" alt="" width="256" height="256" /><p>Una conversación puede ser el principio de algo mucho más grande.</p><a href="/blog/">Explorar el blog ↗</a></div></div></section>
  </main>;
}
