<?php
defined('ABSPATH') || exit;
function mee_seo_data(){
 $description=get_bloginfo('description');$image='https://moevec.org/brand/mee-social-1200x630.webp';$url=home_url('/');
 if(is_singular()){$url=get_permalink();$description=wp_strip_all_tags(get_post_meta(get_the_ID(),'_mee_seo_description',true) ?: get_the_excerpt());$cover=get_the_post_thumbnail_url(null,'mee-social');if($cover)$image=$cover;}
 elseif(is_category()){$term=get_queried_object();$url=get_category_link($term);$description=wp_strip_all_tags(term_description($term));if(!$description)$description='Explora las ideas de '.$term->name.' en el editorial del Movimiento de Evolución Económica.';}
 elseif(is_home()){$description='Ideas y perspectivas sobre educación, comunidad, trabajo y economía. Explora el editorial del Movimiento de Evolución Económica.';}
 elseif(is_search()){$url=home_url('/?s='.rawurlencode(get_search_query()));$description='Resultados de búsqueda en el editorial MEE.';}
 if(get_query_var('paged')>1)$url=get_pagenum_link(get_query_var('paged'));
 return ['title'=>wp_get_document_title(),'description'=>mb_substr($description,0,180),'image'=>$image,'url'=>$url];
}
add_action('wp_head',function(){
 if(is_404())return;$d=mee_seo_data();
 // Core emits the canonical on singular posts.
 if(!is_singular())echo '<link rel="canonical" href="'.esc_url($d['url']).'">';
 echo '<meta name="description" content="'.esc_attr($d['description']).'"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="es_ES"><meta property="og:site_name" content="MEE"><meta property="og:type" content="'.(is_single()?'article':'website').'">';
 foreach(['title','description','image','url']as$key)echo '<meta property="og:'.$key.'" content="'.esc_attr($d[$key]).'">';
 echo '<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="'.esc_attr($d['title']).'"><meta name="twitter:description" content="'.esc_attr($d['description']).'"><meta name="twitter:image" content="'.esc_url($d['image']).'">';
 $graph=[['@type'=>'Organization','@id'=>'https://moevec.org/#organization','name'=>'MEE · Movimiento de Evolución Económica','url'=>'https://moevec.org/','logo'=>'https://moevec.org/brand/mee-logo-tinta-rojo-640.webp']];
 $crumbs=[['@type'=>'ListItem','position'=>1,'name'=>'Inicio','item'=>'https://moevec.org/'],['@type'=>'ListItem','position'=>2,'name'=>'Editorial','item'=>home_url('/')]];
 if(is_single()||is_category())$crumbs[]=['@type'=>'ListItem','position'=>3,'name'=>is_single()?get_the_title():single_cat_title('',false),'item'=>$d['url']];
 $graph[]=['@type'=>'BreadcrumbList','itemListElement'=>$crumbs];
 if(is_single()&&!get_post_meta(get_the_ID(),'_mee_demo',true))$graph[]=['@type'=>'Article','headline'=>get_the_title(),'description'=>$d['description'],'image'=>$d['image'],'datePublished'=>get_the_date('c'),'dateModified'=>get_the_modified_date('c'),'author'=>['@type'=>'Organization','name'=>'MEE · Editorial','url'=>home_url('/')],'publisher'=>['@id'=>'https://moevec.org/#organization'],'mainEntityOfPage'=>$d['url']];
 echo '<script type="application/ld+json">'.wp_json_encode(['@context'=>'https://schema.org','@graph'=>$graph],JSON_HEX_TAG|JSON_HEX_AMP|JSON_HEX_APOS|JSON_HEX_QUOT|JSON_UNESCAPED_SLASHES|JSON_UNESCAPED_UNICODE).'</script>';
},5);
