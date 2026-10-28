"use client";

import { useEffect, useState } from "react";

type Section = { slug: string; name: string };

export default function AreaNavigation({ areaName, sections }: { areaName: string; sections: Section[] }) {
  const [active, setActive] = useState("");

  useEffect(() => {
    const elements = sections.map(({ slug }) => document.getElementById(slug)).filter((element): element is HTMLElement => !!element);
    let frame = 0;
    const update = () => {
      frame = 0;
      let current = "";
      for (const element of elements) {
        if (element.getBoundingClientRect().top <= 170) current = element.id;
      }
      setActive((previous) => previous === current ? previous : current);
    };
    const onScroll = () => {
      if (!frame) frame = window.requestAnimationFrame(update);
    };
    update();
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    return () => {
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onScroll);
      if (frame) window.cancelAnimationFrame(frame);
    };
  }, [sections]);

  return <nav className="story-nav" aria-label={`Subcategorías de ${areaName}`}>
    <span className="story-nav-label">En esta área <img src="/brand/mee-estrella-roja-64.webp" width="64" height="64" alt="" /></span>
    <div className="story-nav-links">{sections.map((section) => <a
      href={`#${section.slug}`}
      key={section.slug}
      aria-current={active === section.slug ? "location" : undefined}
    >{section.name}</a>)}</div>
  </nav>;
}
