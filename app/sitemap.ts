export const dynamic = 'force-static';
import type { MetadataRoute } from 'next';
import { areas } from '../lib/areas';
export default function sitemap():MetadataRoute.Sitemap{return ['/',...areas.map(a=>`/areas/${a.slug}/`),'/contacto/','/sobre-mee/','/privacidad/','/aviso-legal/'].map(path=>({url:'https://moevec.org'+path}));}
