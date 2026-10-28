<?php
defined('ABSPATH') || exit;
remove_action('wp_head','wp_generator');
add_filter('the_generator','__return_empty_string');
add_filter('xmlrpc_enabled','__return_false');
add_filter('wp_headers',function($headers){unset($headers['X-Pingback']);return $headers;});
add_filter('rest_endpoints',function($routes){if(!current_user_can('list_users')){unset($routes['/wp/v2/users'],$routes['/wp/v2/users/(?P<id>[\\d]+)']);}return $routes;});
add_action('template_redirect',function(){if(is_author() || isset($_GET['author'])){global $wp_query;$wp_query->set_404();status_header(404);nocache_headers();include get_404_template();exit;}});
add_filter('authenticate',function($user,$username){
 if(!$username)return $user;
 $key='mee_login_'.mee_client_hash();
 if((int)get_transient($key)>=8)return new WP_Error('mee_login_limited','Demasiados intentos. Espera 15 minutos antes de volver a intentarlo.');
 return $user;
},99,2);
add_action('wp_login_failed',function(){ $key='mee_login_'.mee_client_hash();set_transient($key,(int)get_transient($key)+1,15*MINUTE_IN_SECONDS);});
add_action('wp_login',function(){delete_transient('mee_login_'.mee_client_hash());});
add_filter('login_errors',function(){return 'No se ha podido iniciar sesión. Revisa tus datos o espera unos minutos.';});
add_filter('wp_sitemaps_users_pre_url_list','__return_empty_array');
add_filter('wp_sitemaps_add_provider',function($provider,$name){return $name==='users'?false:$provider;},10,2);
add_filter('wp_sitemaps_posts_query_args',function($args){$args['meta_query']=[['key'=>'_mee_demo','compare'=>'NOT EXISTS']];return $args;});
add_filter('wp_sitemaps_taxonomies_query_args',function($args){$args['meta_query']=[['key'=>'_mee_demo_only','compare'=>'NOT EXISTS']];return $args;});
add_filter('wp_robots',function($robots){if(is_search() || is_attachment() || is_author() || is_singular('post')&&get_post_meta(get_the_ID(),'_mee_demo',true) || (is_category()&&get_term_meta(get_queried_object_id(),'_mee_demo_only',true)) || (is_home()&&!get_option('mee_has_real_articles'))){$robots['noindex']=true;unset($robots['index']);}$robots['max-image-preview']='large';return $robots;});
add_action('save_post_post',function(){
 $q=new WP_Query(['post_type'=>'post','post_status'=>'publish','posts_per_page'=>1,'fields'=>'ids','meta_query'=>[['key'=>'_mee_demo','compare'=>'NOT EXISTS']]]);
 update_option('mee_has_real_articles',(bool)$q->posts,false);
});
