<?php
defined('ABSPATH') || exit;
add_action('wp_enqueue_scripts',function(){
 $version=(string)filemtime(get_stylesheet_directory().'/style.css');
 wp_enqueue_style('mee-editorial',get_stylesheet_uri(),[],$version);
 wp_enqueue_script('mee-motion',get_stylesheet_directory_uri().'/assets/mee-motion.js',[],$version,['in_footer'=>true,'strategy'=>'defer']);
 wp_add_inline_script('mee-motion','window.addEventListener("DOMContentLoaded",function(){if(window.MEEMotion)window.MEEMotion.mountMotion(document.body);});','after');
});
add_action('after_setup_theme',function(){add_theme_support('title-tag');add_theme_support('post-thumbnails');add_theme_support('html5',['search-form','gallery','caption','style','script']);add_image_size('mee-card',800,600,true);add_image_size('mee-social',1200,630,true);});
function mee_frontend_url(){return 'https://moevec.org/';}
function mee_category_nav(){
 echo '<nav class="mee-termnav" aria-label="Áreas editoriales"><a href="'.esc_url(home_url('/')).'"'.(is_home()?' aria-current="page"':'').'>Todas las áreas</a>';
 foreach(mee_editorial_categories()as$slug=>$name){$term=get_term_by('slug',$slug,'category');if($term)echo '<a href="'.esc_url(get_category_link($term)).'"'.(is_category($term->term_id)?' aria-current="page"':'').'>'.esc_html($name).'</a>';}
 echo '</nav>';
 if(is_category()){$term=get_queried_object();$parent=$term->parent?$term->parent:$term->term_id;$children=get_categories(['parent'=>$parent,'hide_empty'=>false]);if($children){$source=json_decode(file_get_contents(WP_PLUGIN_DIR.'/mee-editorial/data/topics.json'),true);$positions=array_flip(array_column($source?:[],'slug'));usort($children,fn($a,$b)=>($positions[$a->slug]??PHP_INT_MAX)<=>($positions[$b->slug]??PHP_INT_MAX));echo '<nav class="mee-topicnav" aria-label="Temas de esta área">';foreach($children as$child)echo '<a href="'.esc_url(get_category_link($child)).'"'.(is_category($child->term_id)?' aria-current="page"':'').'>'.esc_html($child->name).'</a>';echo '</nav>';}}
}
function mee_article_term(){foreach(get_the_category()as$term)if($term->parent)return $term;return null;}

add_action('wp_enqueue_scripts',function(){foreach(['hello-elementor','hello-elementor-theme-style','hello-elementor-header-footer'] as $handle)wp_dequeue_style($handle);},20);
