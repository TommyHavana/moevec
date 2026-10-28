import type { Metadata } from "next";
import type { ReactNode } from "react";
import "./styles.css";
import MotionLayer from "./MotionLayer";

export const metadata: Metadata = {
  title: { default: "MEE | Movimiento de Evolución Económica", template: "%s | MEE" },
  description: "MEE reúne ideas y capacidades para participar en la evolución económica.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return <html lang="es"><body>
    <a className="skip-link" href="#contenido">Saltar al contenido</a>
    <header className="site-header"><a className="brand" href="/" aria-label="MEE, volver al inicio"><img src="/brand/mee-logo-tinta-rojo-640.webp" width="640" height="244" alt="" /></a><nav aria-label="Navegación principal"><a href="/#areas">Áreas</a><a href="/blog/">Blog</a></nav></header>
    {children}
    <footer className="site-footer"><span>MEE · Movimiento de Evolución Económica</span><a href="/blog/">Ir al blog ↗</a></footer>
    <MotionLayer />
  </body></html>;
}
