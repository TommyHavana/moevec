<?php
defined('ABSPATH') || exit;
function mee_network_config(){
 static $config;
 if(isset($config))return $config;
 $file='/run/mee-secrets/red-integration.json';
 $config=is_readable($file)?json_decode(file_get_contents($file),true):[];
 return is_array($config)?$config:[];
}
function mee_network_enabled(){ $c=mee_network_config();return !empty($c['enabled'])&&($c['url']??'')==='https://red.moevec.org'&&strlen($c['secret']??'')>=32; }
function mee_post_area($id){
 foreach(wp_get_post_categories($id,['fields'=>'all'])as$term){
  $parents=array_merge([$term->term_id],get_ancestors($term->term_id,'category','taxonomy'));
  foreach($parents as$parent){$candidate=get_term($parent,'category');if($candidate&&!is_wp_error($candidate)&&array_key_exists($candidate->slug,mee_editorial_categories()))return $candidate->slug;}
 }return null;
}
function mee_network_queue($event,WP_Post $post){
 if(!mee_network_enabled()||get_post_meta($post->ID,'_mee_demo',true))return;
 $payload=['event'=>$event,'post'=>['id'=>$post->ID,'url'=>get_permalink($post),'title'=>html_entity_decode(get_the_title($post),ENT_QUOTES,'UTF-8'),'excerpt'=>mb_substr(wp_strip_all_tags(get_the_excerpt($post)),0,2000),'area_slug'=>mee_post_area($post->ID),'published_at'=>get_post_time('c',true,$post)]];
 update_option('mee_red_queue_'.$post->ID,['payload'=>$payload,'attempt'=>0],false);
 if(!wp_next_scheduled('mee_network_dispatch',[$post->ID]))wp_schedule_single_event(time()+2,'mee_network_dispatch',[$post->ID]);
}
add_action('wp_after_insert_post',function($id,$post,$update,$before){
 if($post->post_type!=='post'||wp_is_post_revision($id)||wp_is_post_autosave($id))return;
 if($post->post_status==='publish')mee_network_queue($before&&$before->post_status==='publish'?'post.updated':'post.published',$post);
 elseif($before&&$before->post_status==='publish')mee_network_queue('post.withdrawn',$post);
},10,4);
add_action('before_delete_post',function($id,$post){if($post->post_type==='post'&&$post->post_status==='publish')mee_network_queue('post.withdrawn',$post);},10,2);
add_action('mee_network_dispatch',function($id){
 if(!mee_network_enabled())return;
 $entry=get_option('mee_red_queue_'.$id);if(!$entry)return;
 $config=mee_network_config();$body=wp_json_encode($entry['payload'],JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);$timestamp=(string)time();
 $response=wp_remote_post($config['url'].'/api/webhooks/moevec',['timeout'=>8,'redirection'=>0,'headers'=>['Content-Type'=>'application/json','X-Mee-Timestamp'=>$timestamp,'X-Mee-Signature'=>'sha256='.hash_hmac('sha256',$timestamp.'.'.$body,$config['secret'])],'body'=>$body]);
 if(!is_wp_error($response)&&wp_remote_retrieve_response_code($response)>=200&&wp_remote_retrieve_response_code($response)<300){delete_option('mee_red_queue_'.$id);delete_option('mee_red_error_'.$id);return;}
 $delays=[60,300,1800,7200,21600];$attempt=(int)$entry['attempt'];
 update_option('mee_red_error_'.$id,['time'=>time(),'status'=>is_wp_error($response)?'connection_error':wp_remote_retrieve_response_code($response),'attempt'=>$attempt+1],false);
 if(isset($delays[$attempt])){$entry['attempt']=$attempt+1;update_option('mee_red_queue_'.$id,$entry,false);wp_schedule_single_event(time()+$delays[$attempt],'mee_network_dispatch',[$id]);}
});
function mee_network_posts($area,$sub='',$limit=5){
 if(!mee_network_enabled())return ['enabled'=>false];
 $config=mee_network_config();$url=$config['url'].'/areas/'.rawurlencode($area).($sub?'?sub='.rawurlencode($sub):'');
 $key='mee_network_'.md5($area.'|'.$sub.'|'.$limit);$cached=get_transient($key);if($cached!==false)return $cached;
 $response=wp_remote_get(add_query_arg(array_filter(['sub'=>$sub,'limit'=>$limit]),$config['url'].'/api/v1/areas/'.rawurlencode($area).'/posts'),['timeout'=>3,'redirection'=>0]);
 $result=['enabled'=>true,'available'=>false,'url'=>$url,'posts'=>[]];
 if(!is_wp_error($response)&&wp_remote_retrieve_response_code($response)===200){
  $body=json_decode(wp_remote_retrieve_body($response),true);
  if(is_array($body['posts']??null)){$result['available']=true;foreach(array_slice($body['posts'],0,$limit)as$p){$u=wp_parse_url($p['url']??'');if(($u['scheme']??'')==='https'&&($u['host']??'')==='red.moevec.org')$result['posts'][]=['title'=>sanitize_text_field($p['title']??''),'url'=>esc_url_raw($p['url'])];}}
 }
 set_transient($key,$result,$result['available']?120:30);return $result;
}
add_action('rest_api_init',function(){register_rest_route('mee/v1','/conversation',['methods'=>'GET','permission_callback'=>'__return_true','callback'=>function(WP_REST_Request $r){$area=sanitize_title($r->get_param('area')??'');if(!array_key_exists($area,mee_editorial_categories()))return new WP_Error('area','Área desconocida',['status'=>404]);return new WP_REST_Response(mee_network_posts($area),200,['Cache-Control'=>'public, max-age=60']);}]);});
add_shortcode('mee_conversacion',function($atts){$a=shortcode_atts(['area'=>'','sub'=>'','limit'=>5],$atts);$area=sanitize_title($a['area']);if(!array_key_exists($area,mee_editorial_categories()))return '';$d=mee_network_posts($area,sanitize_title($a['sub']),max(1,min(20,(int)$a['limit'])));if(!$d['enabled'])return '';$html='<section class="mee-conversacion"><h2>La conversación en la red</h2>';if(!$d['available'])$html.='<p>La red no responde en este momento.</p>';elseif(!$d['posts'])$html.='<p>Todavía no hay publicaciones en esta área.</p>';else{ $html.='<ul>';foreach($d['posts']as$p)$html.='<li><a href="'.esc_url($p['url']).'">'.esc_html($p['title']).'</a></li>';$html.='</ul>';}$html.='<a href="'.esc_url($d['url']).'">Participar en la red</a></section>';return $html;});
