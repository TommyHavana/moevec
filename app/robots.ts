export const dynamic = 'force-static';
import type { MetadataRoute } from 'next';
export default function robots():MetadataRoute.Robots{return {rules:{userAgent:'*',allow:'/',disallow:['/blog/wp-admin/','/blog/wp-login.php','/blog/?s=','/blog/wp-json/mee/v1/contact']},sitemap:['https://moevec.org/sitemap.xml','https://moevec.org/blog/wp-sitemap.xml'],host:'https://moevec.org'};}
