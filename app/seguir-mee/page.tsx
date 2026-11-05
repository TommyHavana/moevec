import {areas} from '../../lib/areas';
import {Breadcrumbs,pageMeta} from '../../lib/seo';
export const metadata=pageMeta('Seguir MEE: nuevas lecturas y rutas','Recibe las nuevas entradas de MEE en tu lector RSS, elige un área o retoma tus rutas de lectura desde el mismo navegador.','/seguir-mee/');
export default function FollowPage(){return <main id="contenido" className="info-page">
 <Breadcrumbs items={[{name:'Inicio',path:'/'},{name:'Seguir MEE',path:'/seguir-mee/'}]}/>
 <h1>Una idea para<br/>volver<span className="title-dot">.</span></h1>
 <div className="info-sections"><section><h2>Las nuevas entradas, en tu lector</h2><p>RSS reúne las publicaciones de los sitios que eliges. Copia la dirección del canal en un lector RSS para recibir las próximas entradas de MEE.</p><a className="pill-link" href="/blog/feed/">Abrir el canal de MEE</a><p className="feed-address">https://moevec.org/blog/feed/</p></section>
 <section><h2>Sigue el área que te interesa</h2><ul className="feed-list">{areas.map(area=><li key={area.slug}><a href={`/blog/category/${area.slug}/feed/`}>{area.name}</a></li>)}</ul></section>
 <section><h2>Retoma tu recorrido</h2><p>Las rutas permiten marcar cada lectura como terminada. Vuelve desde el mismo navegador para ver tus marcas y elegir el siguiente paso.</p><a className="text-link" href="/empieza-aqui/">Volver a las rutas de lectura</a></section>
 <section><h2>Una pregunta puede abrir otra lectura</h2><p>Si falta un tema o encuentras una afirmación que necesita revisión, puedes escribirnos. Acompaña las correcciones con la fuente y el contexto.</p><a className="text-link" href="/contacto/?tema=Propuesta%20editorial">Proponer un tema o una corrección</a></section></div>
 </main>;}
