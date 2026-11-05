export const dynamic = 'force-static';
import type { MetadataRoute } from 'next';
import { areas } from '../lib/areas';
import { readingPaths } from '../lib/reading-paths';
export default function sitemap():MetadataRoute.Sitemap{return ['/',...areas.map(a=>`/areas/${a.slug}/`),'/empieza-aqui/',...readingPaths.map(p=>`/empieza-aqui/${p.slug}/`),'/seguir-mee/','/metodo-editorial/','/recursos/','/contacto/','/apoya/','/sobre-mee/','/privacidad/','/aviso-legal/'].map(path=>({url:'https://moevec.org'+path}));}
