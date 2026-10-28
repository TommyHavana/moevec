import gsap from "gsap";

/** Shared by the static React export and WordPress. */
export function mountMotion(scope: HTMLElement) {
  const root = document.documentElement;
  const reduced = matchMedia("(prefers-reduced-motion: reduce)");
  const fine = matchMedia("(hover: hover) and (pointer: fine)");
  let paused = false;
  try { paused = localStorage.getItem("mee-motion") === "paused"; } catch {}
  const button = scope.querySelector<HTMLButtonElement>("[data-motion-toggle]");
  const overlay = scope.querySelector<HTMLElement>(".page-transition");
  const cursor = scope.querySelector<HTMLElement>(".mee-cursor");
  const hero = scope.querySelector<HTMLElement>("[data-motion-hero]");
  const ring = scope.querySelector<HTMLElement>(".orbit-tilt");
  const progress = scope.querySelector<HTMLElement>(".reading-progress");
  let navigating = false, fallback = 0, frame = 0;
  const updatePreference = () => {
    root.classList.toggle("motion-paused", paused || reduced.matches || document.hidden);
    root.classList.toggle("pointer-motion", fine.matches && !paused && !reduced.matches);
    if (button) {
      button.setAttribute("aria-pressed", String(paused));
      button.textContent = paused ? "Activar movimiento" : "Pausar movimiento";
    }
  };
  updatePreference();
  root.classList.add("motion-ready");
  const ambient = new IntersectionObserver(entries => entries.forEach(e => e.target.classList.toggle("motion-playing", e.isIntersecting)), {rootMargin: "50px"});
  scope.querySelectorAll("[data-ambient]").forEach(el => ambient.observe(el));
  const ctx = gsap.context(() => {
    if (!paused && !reduced.matches) {
      const lines = scope.querySelectorAll(".hero-word");
      if (lines.length) gsap.from(lines, {yPercent: 105, rotation: 3, duration: .85, stagger: .09, ease: "power3.out", clearProps: "transform"});
      if (ring) gsap.from(ring, {scale: .72, rotation: -24, duration: 1.15, ease: "power3.out", clearProps: "transform"});
    }
  }, scope);
  const xTo = cursor ? gsap.quickTo(cursor, "x", {duration: .22, ease: "power3.out"}) : null;
  const yTo = cursor ? gsap.quickTo(cursor, "y", {duration: .22, ease: "power3.out"}) : null;
  const rx = ring ? gsap.quickTo(ring, "rotationX", {duration: 1, ease: "power3.out"}) : null;
  const ry = ring ? gsap.quickTo(ring, "rotationY", {duration: 1, ease: "power3.out"}) : null;
  const onPointer = (event: PointerEvent) => {
    if (paused || reduced.matches || !fine.matches) return;
    xTo?.(event.clientX); yTo?.(event.clientY);
    cursor?.classList.add("is-active");
    const target = event.target instanceof Element ? event.target.closest("a,button,input,textarea,select,summary") : null;
    cursor?.classList.toggle("is-link", !!target);
    if (hero && event.clientY < hero.getBoundingClientRect().bottom && ring) {
      rx?.((event.clientY / innerHeight - .5) * -16);
      ry?.((event.clientX / innerWidth - .5) * 22);
    }
  };
  const leave = () => cursor?.classList.remove("is-active");
  const scroll = () => {
    if (frame) return;
    frame = requestAnimationFrame(() => {
      frame = 0;
      if (progress) progress.style.transform = `scaleX(${Math.max(0, Math.min(1, scrollY / Math.max(1, root.scrollHeight - innerHeight)))})`;
    });
  };
  const toggle = () => {
    paused = !paused;
    try { localStorage.setItem("mee-motion", paused ? "paused" : "playing"); } catch {}
    updatePreference();
    if (paused) { ctx.getTweens().forEach((t: gsap.core.Tween) => t.progress(1)); leave(); }
  };
  const reset = () => {
    navigating = false;
    clearTimeout(fallback);
    if (overlay) { gsap.killTweensOf(overlay); gsap.set(overlay, {autoAlpha: 0}); }
  };
  const click = (event: MouseEvent) => {
    const link = event.target instanceof Element ? event.target.closest<HTMLAnchorElement>("a[href]") : null;
    if (!link || !overlay || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.altKey || event.shiftKey || link.download || (link.target && link.target !== "_self") || paused || reduced.matches || navigating) return;
    const url = new URL(link.href, location.href);
    if (url.origin !== location.origin || !/^https?:$/.test(url.protocol) || url.pathname === location.pathname && url.search === location.search || /wp-admin|wp-login|\/wp-json\//.test(url.pathname)) return;
    event.preventDefault(); navigating = true;
    const go = () => location.assign(url.href);
    fallback = window.setTimeout(go, 1100);
    gsap.set(overlay, {autoAlpha: 1});
    gsap.fromTo(overlay, {yPercent: 100}, {yPercent: 0, duration: .32, ease: "power3.inOut", onComplete: go});
    const star = overlay.querySelector("img");
    if (star) gsap.fromTo(star, {rotation: -90, scale: .5}, {rotation: 90, scale: 1, duration: .6, ease: "power2.out"});
  };
  button?.addEventListener("click", toggle);
  scope.addEventListener("pointermove", onPointer, {passive: true});
  document.addEventListener("pointerleave", leave);
  scope.addEventListener("click", click);
  document.addEventListener("visibilitychange", updatePreference);
  reduced.addEventListener("change", updatePreference); fine.addEventListener("change", updatePreference);
  addEventListener("pageshow", reset); addEventListener("scroll", scroll, {passive: true});
  scroll(); reset();
  return () => {
    ambient.disconnect(); ctx.revert();
    xTo?.tween.kill(); yTo?.tween.kill(); rx?.tween.kill(); ry?.tween.kill();
    button?.removeEventListener("click", toggle);
    scope.removeEventListener("pointermove", onPointer); scope.removeEventListener("click", click);
    document.removeEventListener("pointerleave", leave); document.removeEventListener("visibilitychange", updatePreference);
    reduced.removeEventListener("change", updatePreference); fine.removeEventListener("change", updatePreference);
    removeEventListener("pageshow", reset); removeEventListener("scroll", scroll);
    clearTimeout(fallback); cancelAnimationFrame(frame);
    root.classList.remove("motion-ready", "motion-paused", "pointer-motion");
  };
}
