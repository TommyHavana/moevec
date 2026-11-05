<?php
/** One-time, idempotent migration of reviewed MEE metadata to Rank Math. CLI only. */
if(PHP_SAPI!=='cli')exit(1);
require '/var/www/html/wp-load.php';
require_once ABSPATH.'wp-admin/includes/plugin.php';
$file=WP_PLUGIN_DIR.'/mee-editorial/data/seo-migration.json';
$entries=json_decode(file_get_contents($file),true,512,JSON_THROW_ON_ERROR);
if(count($entries)!==840)throw new RuntimeException('Se requieren 840 manifiestos.');
$posts=get_posts(['post_type'=>'post','post_status'=>'publish','numberposts'=>-1,'meta_key'=>'_mee_plan_id']);
$by_id=[];foreach($posts as$post)$by_id[get_post_meta($post->ID,'_mee_plan_id',true)]=$post;
if(count($by_id)!==840)throw new RuntimeException('El estado real de WordPress no coincide.');
$attachments=[];
// Complete preflight before changing any metadata.
foreach($entries as$entry){
    $post=$by_id[$entry['id']]??null;
    if(!$post||$post->post_title!==$entry['title']||$post->post_name!==$entry['slug'])throw new RuntimeException('Título o slug distinto: '.$entry['id']);
    $ids=(array)get_post_meta($post->ID,'_mee_editorial_images',true);
    if(count($ids)!==3)throw new RuntimeException('Número de imágenes distinto: '.$entry['id']);
    foreach($ids as$id){
        $role=get_post_meta($id,'_mee_image_role',true);$image=$entry['images'][$role]??null;
        if(!$image||get_post_meta($id,'_mee_plan_id',true)!==$entry['id']||!is_file(get_attached_file($id)))throw new RuntimeException('Imagen ajena o ausente: '.$entry['id']);
        $alt=get_post_meta($id,'_wp_attachment_image_alt',true);
        if($alt!==$image['previous_alt']&&$alt!==$image['alt'])throw new RuntimeException('Alt modificado fuera del manifiesto: '.$entry['id'].'/'.$role);
        $attachments[$entry['id']][$role]=(int)$id;
    }
}
update_option('rank_math_modules',['link-counter','seo-analysis','sitemap','rich-snippet','local-seo'],false);
// The free plugin supports skipping its optional RankMath.com account.
update_option('rank_math_registration_skip',true,false);
$result=activate_plugin('seo-by-rank-math/rank-math.php','',false,false);
if(is_wp_error($result))throw new RuntimeException($result->get_error_message());
$general=array_replace((array)get_option('rank-math-options-general',[]),[
    'setup_mode'=>'advanced','strip_category_base'=>'off','nofollow_external_links'=>'off','nofollow_image_links'=>'off',
    'add_img_alt'=>'off','add_img_title'=>'off','breadcrumbs'=>'off','frontend_seo_score'=>'off',
    'analytics_stats'=>'off','console_email_reports'=>'off','attachment_redirect_urls'=>'on',
    'attachment_redirect_default'=>'https://moevec.org/blog/','rss_before_content'=>'','rss_after_content'=>'',
]);
update_option('rank-math-options-general',$general,false);
$titles=array_replace((array)get_option('rank-math-options-titles',[]),[
    'knowledgegraph_type'=>'company','knowledgegraph_name'=>'MEE · Movimiento de Evolución Económica',
    'website_name'=>'MEE · Movimiento de Evolución Económica','website_alternate_name'=>'MEE',
    'knowledgegraph_logo'=>'https://moevec.org/brand/mee-logo-tinta-rojo-640.webp','url'=>'https://moevec.org/',
    'local_business_type'=>'Organization','title_separator'=>'|','twitter_card_type'=>'summary_large_image',
    'homepage_title'=>'Ideas y perspectivas sobre economía, trabajo y comunidad | MEE',
    'homepage_description'=>'Explora el editorial MEE: educación, comunidad, trabajo y economía con fuentes, ejemplos y argumentos contrarios. Elige un tema, un nivel o una ruta de lectura.',
    'pt_post_title'=>'%title% | MEE','pt_post_description'=>'%excerpt%',
    'pt_post_default_rich_snippet'=>'article','pt_post_default_article_type'=>'Article',
    'tax_category_title'=>'%term% | MEE','tax_category_description'=>'%term_description%',
    'tax_post_tag_custom_robots'=>'on','tax_post_tag_robots'=>['noindex'],
    'disable_author_archives'=>'on','disable_date_archives'=>'on','noindex_search'=>'on',
    'noindex_empty_taxonomies'=>'on','noindex_password_protected'=>'on',
]);
update_option('rank-math-options-titles',$titles,false);
$sitemap=array_replace((array)get_option('rank-math-options-sitemap',[]),[
    'items_per_page'=>200,'include_images'=>'on','include_featured_image'=>'on',
    'authors_sitemap'=>'off','html_sitemap'=>'off','pt_post_sitemap'=>'on','pt_page_sitemap'=>'on',
    'pt_attachment_sitemap'=>'off','tax_category_sitemap'=>'on','tax_post_tag_sitemap'=>'off',
]);
update_option('rank-math-options-sitemap',$sitemap,false);
update_option('rank_math_wizard_completed',true,false);
delete_transient('_rank_math_activation_redirect');
$updated=0;$image_count=0;$alt_count=0;
foreach($entries as$entry){
    $post=$by_id[$entry['id']];$url=get_permalink($post);$term=get_term_by('slug',$entry['topic'],'category');
    $cover_id=$attachments[$entry['id']]['featured'];$cover=wp_get_attachment_url($cover_id);
    $meta=['rank_math_title'=>$entry['seo_title'],'rank_math_description'=>$entry['description'],
        'rank_math_focus_keyword'=>$entry['keyword'],'rank_math_canonical_url'=>$url,'rank_math_robots'=>['index'],
        'rank_math_primary_category'=>$term?(int)$term->term_id:0,
        'rank_math_facebook_title'=>$entry['seo_title'],'rank_math_facebook_description'=>$entry['description'],
        'rank_math_facebook_image'=>$cover,'rank_math_facebook_image_id'=>$cover_id,
        'rank_math_twitter_use_facebook'=>'on','rank_math_twitter_card_type'=>'summary_large_image'];
    foreach($meta as$key=>$value)update_post_meta($post->ID,$key,$value);
    foreach($entry['images']as$role=>$image){
        $id=$attachments[$entry['id']][$role];$old=get_post_meta($id,'_wp_attachment_image_alt',true);
        if($old!==$image['alt']){update_post_meta($id,'_wp_attachment_image_alt',$image['alt']);$alt_count++;}
        $attachment=get_post($id);
        if($attachment->post_title!==$image['title']||$attachment->post_content!==$image['description']){
            $r=wp_update_post(['ID'=>$id,'post_title'=>$image['title'],'post_content'=>$image['description']],true);
            if(is_wp_error($r))throw new RuntimeException($r->get_error_message());
        }
        $image_count++;
    }
    $updated++;
}
foreach(get_terms(['taxonomy'=>'category','hide_empty'=>false])as$term){
    $description=wp_strip_all_tags(term_description($term));
    if(!$description)$description='Explora '.$term->name.' en MEE: artículos con fuentes, ejemplos y argumentos contrarios para desarrollar criterio y conectar ideas con decisiones.';
    update_term_meta($term->term_id,'rank_math_title',$term->name.' | MEE');
    update_term_meta($term->term_id,'rank_math_description',mb_substr($description,0,160));
}
flush_rewrite_rules(false);
if(class_exists('RankMath\\Helper'))\RankMath\Helper::clear_cache();
echo json_encode(['articles'=>$updated,'images'=>$image_count,'alts_changed'=>$alt_count,'rank_math_active'=>is_plugin_active('seo-by-rank-math/rank-math.php'),'score_recalculation'=>'pending_native_rank_math_tool','parent_writable'=>is_writable(WP_PLUGIN_DIR)],JSON_PRETTY_PRINT|JSON_UNESCAPED_SLASHES|JSON_UNESCAPED_UNICODE);
