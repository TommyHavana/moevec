<?php
defined('ABSPATH') || exit;
add_filter('rank_math/researches/toc_plugins',function($plugins){
    if(get_stylesheet()==='mee-child')$plugins['mee-editorial/mee-editorial.php']='MEE · índice de lectura por encabezados';
    return $plugins;
});

// Rank Math owns the HTML head. This adapter preserves MEE's real identity,
// taxonomy and exclusions without a second producer of metadata or schema.
add_filter('rank_math/frontend/robots',function($robots){
    $noindex=is_search()||is_attachment()||is_author()||is_date()||is_tag()
        ||(is_singular('post')&&get_post_meta(get_the_ID(),'_mee_demo',true))
        ||(is_category()&&get_term_meta(get_queried_object_id(),'_mee_demo_only',true))
        ||mee_discovery_level()||isset($_GET['category_name'])||is_404();
    if($noindex){unset($robots['index']);$robots['index']='noindex';}
    $robots['follow']='follow';$robots['max-image-preview']='max-image-preview:large';
    return $robots;
});
add_filter('rank_math/frontend/canonical',function($url){
    if(mee_discovery_level()||isset($_GET['category_name'])){
        if(is_category())return get_category_link(get_queried_object_id());
        if(!is_search())return home_url('/');
    }
    return $url;
});
add_filter('rank_math/sitemap/entry',function($entry,$type,$object){
    if($type==='user')return false;
    if($type==='post'&&($object->post_type==='attachment'||get_post_meta($object->ID,'_mee_demo',true)))return false;
    if($type==='term'&&($object->taxonomy==='post_tag'||get_term_meta($object->term_id,'_mee_demo_only',true)))return false;
    return $entry;
},10,3);
add_filter('rank_math/json_ld',function($data){
    if(is_404()||is_search()||is_author()||is_attachment())return [];
    $origin='https://moevec.org';$name='MEE · Movimiento de Evolución Económica';
    $url=is_singular()?get_permalink():(is_category()?get_category_link(get_queried_object_id()):home_url('/'));
    if(get_query_var('paged')>1)$url=get_pagenum_link(get_query_var('paged'));
    $core=['Organization','Person','WebSite','WebPage','CollectionPage','BreadcrumbList','Article','BlogPosting','NewsArticle','ImageObject'];
    foreach($data as$key=>$node){$types=(array)($node['@type']??[]);if(array_intersect($types,$core))unset($data[$key]);}
    $data['meeOrganization']=['@type'=>'Organization','@id'=>$origin.'/#organization','name'=>$name,'url'=>$origin.'/','logo'=>['@type'=>'ImageObject','url'=>$origin.'/brand/mee-logo-tinta-rojo-640.webp','width'=>640,'height'=>244]];
    $data['meeWebsite']=['@type'=>'WebSite','@id'=>$origin.'/#website','name'=>$name,'url'=>$origin.'/','inLanguage'=>'es','publisher'=>['@id'=>$origin.'/#organization']];
    $items=[];foreach(mee_breadcrumb_items()as$i=>$item)$items[]=['@type'=>'ListItem','position'=>$i+1,'name'=>$item['name'],'item'=>$item['url']];
    $data['meeBreadcrumb']=['@type'=>'BreadcrumbList','@id'=>$url.'#breadcrumb','itemListElement'=>$items];
    $description=is_singular()?get_post_meta(get_the_ID(),'rank_math_description',true):mee_seo_data()['description'];
    $data['meeWebpage']=['@type'=>is_singular()?'WebPage':'CollectionPage','@id'=>$url.'#webpage','url'=>$url,'name'=>wp_get_document_title(),'description'=>$description,'inLanguage'=>'es','isPartOf'=>['@id'=>$origin.'/#website'],'breadcrumb'=>['@id'=>$url.'#breadcrumb']];
    if(is_singular('post')&&!get_post_meta(get_the_ID(),'_mee_demo',true)){
        $images=array_values(array_filter(array_map('wp_get_attachment_url',(array)get_post_meta(get_the_ID(),'_mee_editorial_images',true))));
        $data['meeEditorial']=['@type'=>'Organization','@id'=>$origin.'/#editorial','name'=>'MEE · Editorial','url'=>$origin.'/sobre-mee/'];
        $data['meeArticle']=['@type'=>'Article','@id'=>$url.'#article','headline'=>get_the_title(),'description'=>$description,'image'=>$images,'datePublished'=>get_the_date(DATE_W3C),'dateModified'=>get_the_modified_date(DATE_W3C),'inLanguage'=>'es','author'=>['@id'=>$origin.'/#editorial'],'publisher'=>['@id'=>$origin.'/#organization'],'isPartOf'=>['@id'=>$origin.'/#website'],'mainEntityOfPage'=>['@id'=>$url.'#webpage']];
    }
    return $data;
},999);

// All legacy sitemap links keep a single destination after migration.
add_action('template_redirect',function(){
    if(!mee_has_rank_math())return;
    $path=parse_url($_SERVER['REQUEST_URI']??'',PHP_URL_PATH);
    if($path==='/blog/wp-sitemap.xml'){wp_safe_redirect(home_url('/sitemap_index.xml'),301);exit;}
},0);
