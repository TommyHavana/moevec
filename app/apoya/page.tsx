import { Breadcrumbs, pageMeta } from '../../lib/seo';
import styles from './support.module.css';

export const metadata = pageMeta(
  'Apoya a MEE: donaciones y publicidad',
  'Apoya el trabajo del Movimiento de Evolución Económica con una donación o propón publicidad para tu empresa en moevec.org.',
  '/apoya/',
);

export default function SupportPage() {
  return (
    <main id="contenido" className={styles.page}>
      <Breadcrumbs items={[{ name: 'Inicio', path: '/' }, { name: 'Apoya a MEE', path: '/apoya/' }]} />

      <section className={styles.hero} aria-labelledby="support-title">
        <div>
          <h1 id="support-title">Ayuda a mover<br />estas ideas<span className="title-dot">.</span></h1>
          <p>MEE reúne ideas sobre educación, libertad económica y cooperación. Si compartes esta forma de entender el mundo, puedes apoyar el trabajo que hay detrás.</p>
          <nav className={styles.choices} aria-label="Formas de apoyar a MEE">
            <a className={styles.button} href="#donar">Quiero donar</a>
            <a className={styles.textLink} href="#publicidad">Quiero anunciar mi empresa</a>
          </nav>
        </div>
        <div className={styles.symbol} aria-hidden="true">
          <span /><span />
          <img src="/brand/mee-estrella-roja.svg" width="256" height="256" alt="" />
        </div>
      </section>

      <section id="donar" className={styles.donation} aria-labelledby="donation-title">
        <div className={styles.sectionIntro}>
          <h2 id="donation-title">Tu aportación<br />sostiene el trabajo.</h2>
          <p>Investigar, escribir y mantener esta plataforma requiere tiempo y recursos. Una donación es una forma de contribuir a su continuidad.</p>
          <a className={styles.button} href="/contacto/?tema=donacion">Contactar para donar</a>
          <p className={styles.note}>Por ahora, las aportaciones se acuerdan por correo. Escríbenos y concretamos contigo cómo hacerla.</p>
        </div>
        <div className={styles.purposes}>
          <h3>Qué puedes ayudar a sostener</h3>
          <dl>
            <div><dt>Investigación y contenidos</dt><dd>La consulta de fuentes y la elaboración de artículos para comprender y debatir la economía.</dd></div>
            <div><dt>Diseño y divulgación</dt><dd>Las ilustraciones y los recursos que acompañan las ideas y facilitan su lectura.</dd></div>
            <div><dt>La plataforma</dt><dd>El alojamiento, el mantenimiento y las mejoras de acceso a los contenidos.</dd></div>
          </dl>
        </div>
      </section>

      <section id="publicidad" className={styles.advertising} aria-labelledby="advertising-title">
        <div className={styles.sectionIntro}>
          <h2 id="advertising-title">Tu empresa también<br />puede formar parte.</h2>
          <p>Si tu empresa comparte el valor de la iniciativa, la responsabilidad y el intercambio voluntario, podemos hablar de publicidad en MEE.</p>
          <p>Cuéntanos qué haces y qué quieres dar a conocer. Estudiaremos cómo encaja tu propuesta en la plataforma.</p>
          <a className={styles.button} href="/contacto/?tema=publicidad">Proponer publicidad</a>
        </div>
        <div className={styles.proposal}>
          <h3>Hablemos de una propuesta concreta</h3>
          <p>Incluye el nombre y la web de tu empresa, el producto o servicio que quieres anunciar y el periodo que tienes en mente. Si ya tienes un presupuesto orientativo, puedes indicarlo.</p>
          <p>Acordaremos contigo el formato, la ubicación, la duración y el precio antes de publicar.</p>
          <div className={styles.editorial}>
            <h3>Publicidad identificada. Criterio editorial propio.</h3>
            <p>Las colaboraciones deberán encajar con los valores de MEE. La publicidad se identificará como tal y el apoyo económico no dará control sobre los contenidos editoriales.</p>
          </div>
        </div>
      </section>

      <section className={styles.closing} aria-labelledby="support-contact-title">
        <h2 id="support-contact-title">El apoyo empieza<br />con una conversación.</h2>
        <div>
          <p>Si tienes otra forma de colaborar en mente, también nos gustaría conocerla.</p>
          <a className={styles.textLink} href="mailto:contacto@moevec.org">contacto@moevec.org</a>
        </div>
      </section>
    </main>
  );
}
