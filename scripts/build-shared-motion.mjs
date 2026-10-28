import { build } from "esbuild";
import { copyFile } from "node:fs/promises";
await build({entryPoints:["lib/motion-engine.ts"],outfile:"public/mee-motion.js",bundle:true,minify:true,format:"iife",globalName:"MEEMotion",target:"es2020"});
await copyFile("public/mee-motion.js", "wordpress/themes/mee-child/assets/mee-motion.js");
