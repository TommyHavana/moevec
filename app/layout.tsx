import type { Metadata } from "next";
import type { ReactNode } from "react";
import "./styles.css";
import MotionLayer from "./MotionLayer";
import { JsonLd, origin, siteName } from '../lib/seo';

export const metadata: Metadata = {
  metadataBase:new URL(origin),
  title:{default:siteName,template:'%s | MEE'},
  description:'MEE conecta educación, comunidad, trabajo y economía para convertir ideas en capacidades y construir posibilidades en común.',
  robots:{googleBot:{'max-image-preview':'large'}},
  openGraph:{type:'website',locale:'es_ES',siteName,url:origin,images:[{url:'/brand/mee-social-1200x630.webp',width:1200,height:630,alt:siteName}]},
  twitter:{card:'summary_large_image'},
};
export default function RootLayout({children}:{children:ReactNode}) {
  return <html lang="es"><head><link rel="preload" href="/fonts/Archivo-Black-Latin.woff2" as="font" type="font/woff2" crossOrigin="anonymous"/><link rel="preload" href="/fonts/Manrope-Latin-Variable.woff2" as="font" type="font/woff2" crossOrigin="anonymous"/></head><body>
    <a className="skip-link" href="#contenido">Saltar al contenido</a>
    <div className="reading-progress" aria-hidden="true"/>
    <header className="site-header"><a className="brand" href="/" aria-label="MEE, volver al inicio"><img src="/brand/mee-logo-tinta-rojo-640.webp" width="640" height="244" alt=""/></a><nav aria-label="Navegación principal"><a href="/empieza-aqui/">Empieza aquí</a><a href="/#areas">Áreas</a><a href="/blog/">Blog</a><a href="/contacto/">Contacto</a></nav></header>
    {children}
    <footer className="site-footer"><div className="footer-invitation"><p>La próxima idea<br/>puede empezar contigo.</p><a href="/contacto/">Hablemos <span aria-hidden="true">↗</span></a></div><div className="footer-bottom"><span>MEE · Movimiento de Evolución Económica</span><nav aria-label="Información"><a href="/seguir-mee/">Seguir MEE</a><a href="/sobre-mee/">Qué es MEE</a><a href="/metodo-editorial/">Método editorial</a><a href="/recursos/">Recursos</a><a href="/apoya/">Apoya a MEE</a><a href="/privacidad/">Privacidad</a><a href="/aviso-legal/">Aviso legal</a><button type="button" data-motion-toggle aria-pressed="false">Pausar movimiento</button></nav></div></footer>
    <div className="mee-cursor" aria-hidden="true"><span/></div><div className="page-transition" aria-hidden="true"><img src="/brand/mee-estrella-blanca-256.webp" width="256" height="256" alt=""/></div>
    <JsonLd data={{'@context':'https://schema.org','@graph':[{'@type':'Organization','@id':origin+'/#organization',name:siteName,url:origin,logo:origin+'/brand/mee-logo-tinta-rojo-640.webp',email:'contacto@moevec.org'},{'@type':'WebSite','@id':origin+'/#website',name:siteName,url:origin,inLanguage:'es',publisher:{'@id':origin+'/#organization'}}]}}/>
    <MotionLayer/>
  </body></html>;
}
