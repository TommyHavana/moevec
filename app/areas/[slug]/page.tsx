import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { areas } from "../../../lib/areas";
import AreaNavigation from "./AreaNavigation";

type Props = { params: Promise<{ slug: string }> };
export function generateStaticParams() { return areas.map(({ slug }) => ({ slug })); }
export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const area = areas.find((item) => item.slug === slug);
  return { title: area?.name ?? "Área", description: area?.lead };
}
export default async function AreaPage({ params }: Props) {
  const { slug } = await params;
  const area = areas.find((item) => item.slug === slug);
  if (!area) notFound();
  const index = areas.findIndex((item) => item.slug === slug);
  const next = areas[(index + 1) % areas.length];
  return <main id="contenido" className="story-page">
    <section className="story-opening" aria-labelledby="story-title"><div className="story-heading" data-reveal><p className="eyebrow">MEE / Área {String(index + 1).padStart(2, "0")}</p><h1 id="story-title">{area.name}<span className="title-dot">.</span></h1><p>{area.claim}</p></div><div className="story-hero" data-reveal><picture><source media="(max-width: 720px)" srcSet={`/images/areas/${slug}-680.jpg`} /><img src={`/images/areas/${slug}.jpg`} width="1254" height="1254" alt={`Imagen conceptual de ${area.name}`} /></picture></div></section>
    <AreaNavigation areaName={area.name} sections={area.sections} />
    <div className="story-content"><section className="story-thesis" data-reveal><p className="eyebrow">Lo que podemos crear</p><h2>{area.lead}</h2><p>{area.intro}</p><p className="story-detail">{area.detail}</p></section>
      <div className="chapter-list">{area.sections.map((s, i) => <section className="chapter" data-reveal id={s.slug} key={s.slug} aria-labelledby={`${s.slug}-title`}><p className="chapter-index">{String(i + 1).padStart(2, "0")} / {String(area.sections.length).padStart(2, "0")}</p><div><h2 id={`${s.slug}-title`}>{s.name}</h2><p className="chapter-benefit">{s.benefit}</p>{s.children.length > 0 && <ul className="chapter-topics">{s.children.map((child) => <li key={child.slug}>{child.name}{child.children?.length ? <ul>{child.children.map((nested) => <li key={nested.slug}>{nested.name}</li>)}</ul> : null}</li>)}</ul>}</div></section>)}</div>
      <div className="editorial-link"><span className="eyebrow">Blog MEE</span><p>Las ideas viven en la conversación.</p><a href="/blog/">Explorar el blog ↗</a></div></div>
    <a className="next-area" href={`/areas/${next.slug}/`}><span>Siguiente área <span aria-hidden="true">↗</span></span><strong>{next.name}</strong></a>
  </main>;
}
