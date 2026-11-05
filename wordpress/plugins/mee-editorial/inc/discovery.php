<?php
defined('ABSPATH') || exit;
function mee_discovery_data($name) {
    static $cache=[];
    if (!isset($cache[$name])) {
        $file=dirname(__DIR__).'/data/'.$name.'.json';
        $cache[$name]=is_readable($file)?(json_decode(file_get_contents($file),true)?:[]):[];
    }
    return $cache[$name];
}
function mee_reading_details($post_id) {
    $catalog=mee_discovery_data('article-discovery');
    $id=get_post_meta($post_id,'_mee_plan_id',true);
    return $catalog[$id]??['level'=>'','minutes'=>max(1,(int)round(str_word_count(wp_strip_all_tags(get_post_field('post_content',$post_id)))/200))];
}
function mee_discovery_level() {
    $value=isset($_GET['mee_level'])?sanitize_key(wp_unslash($_GET['mee_level'])):'';
    return in_array($value,['fundamentos','desarrollo','aplicacion'],true)?$value:'';
}
add_action('pre_get_posts',function($query){
    if(is_admin()||!$query->is_main_query()||!($query->is_home()||$query->is_search()||$query->is_category()))return;
    $query->set('post_type','post');
    if($level=mee_discovery_level())$query->set('tag_slug__and',array_unique(array_merge((array)$query->get('tag_slug__and'),[$level])));
});
add_filter('wp_robots',function($robots){
    if(mee_discovery_level()||isset($_GET['category_name'])){$robots['noindex']=true;unset($robots['index']);}
    return $robots;
});
function mee_related_article_ids($post_id,$term,$limit=3) {
    $details=mee_reading_details($post_id);$level=sanitize_title($details['level']);$ids=[];
    $topics=$term?[$term->term_id]:[];$area=$term?($term->parent?:$term->term_id):0;
    foreach([[$topics,$level],[$topics,''],[$area?[$area]:[],$level],[$area?[$area]:[],'']] as [$categories,$level_slug]){
        if(count($ids)>=$limit)break;
        if(!$categories)continue;
        $args=['post_type'=>'post','post_status'=>'publish','posts_per_page'=>$limit-count($ids),'fields'=>'ids','no_found_rows'=>true,'post__not_in'=>array_merge([$post_id],$ids),'category__in'=>$categories,'meta_query'=>[['key'=>'_mee_demo','compare'=>'NOT EXISTS']]];
        if($level_slug)$args['tag_slug__and']=[$level_slug];
        $ids=array_merge($ids,get_posts($args));
    }
    return array_values(array_unique($ids));
}
function mee_reading_continuation($post_id) {
    $id=get_post_meta($post_id,'_mee_plan_id',true);
    foreach(mee_discovery_data('reading-paths') as $path){
        foreach($path['steps'] as $index=>$step){
            if($step['id']!==$id)continue;
            echo '<nav class="mee-path-continuation" aria-label="Continuar la ruta de lectura"><p>Lectura '.esc_html($index+1).' de '.count($path['steps']).' en <a href="https://moevec.org/empieza-aqui/'.esc_attr($path['slug']).'/">'.esc_html($path['title']).'</a></p>';
            $next=$path['steps'][$index+1]??null;
            if($next)echo '<h2>La siguiente lectura</h2><a class="text-link" href="'.esc_url($next['url']).'">'.esc_html($next['title']).'</a>';
            else echo '<h2>Has llegado al final de esta ruta.</h2><a class="text-link" href="https://moevec.org/empieza-aqui/">Elegir otro recorrido</a>';
            echo '</nav>';return;
        }
    }
}

require_once __DIR__.'/editorial-quality.php';
