"use client";
import { useGSAP } from "@gsap/react";
import gsap from "gsap";
import { mountMotion } from "../lib/motion-engine";
gsap.registerPlugin(useGSAP);
export default function MotionLayer() {
  useGSAP(() => mountMotion(document.body));
  return null;
}
