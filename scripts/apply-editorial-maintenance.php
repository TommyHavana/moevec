<?php
// CLI-only, existing published posts, guarded exact replacements; dry run by default.
if(PHP_SAPI!=='cli'||empty($argv[1]))exit(1);
require '/var/www/html/wp-load.php';
$batch=json_decode(file_get_contents($argv[1]),true,512,JSON_THROW_ON_ERROR);
$apply=($argv[2]??'')==='--apply';$prepared=[];
foreach($batch['entries']as$entry){
 $posts=get_posts(['post_type'=>'post','post_status'=>'publish','posts_per_page'=>2,'meta_key'=>'_mee_plan_id','meta_value'=>$entry['id']]);
 if(count($posts)!==1||(int)$entry['post_id']!==$posts[0]->ID)throw new RuntimeException('Post mismatch '.$entry['id']);
 $post=$posts[0];$body=$post->post_content;
 if(!hash_equals($entry['expected_live_sha256'],hash('sha256',$body)))throw new RuntimeException('Concurrent content change '.$entry['id']);
 foreach($entry['replacements']as$pair){if(substr_count($body,$pair['before'])!==1)throw new RuntimeException('Fragment mismatch '.$entry['id']);$body=str_replace($pair['before'],$pair['after'],$body);}
 if($entry['append_html']&&str_contains($body,$entry['append_html']))throw new RuntimeException('Duplicate append');
 $body.=$entry['append_html'];
 $prepared[]=['id'=>$entry['id'],'post_id'=>$post->ID,'before'=>$post->post_content,'after'=>$body,'image_ids'=>get_post_meta($post->ID,'_mee_editorial_images',true),'title'=>$post->post_title,'slug'=>$post->post_name];
}
if($apply){
 $backup=dirname($argv[1]).'/before-maintenance.json';if(file_exists($backup))throw new RuntimeException('Backup already exists; inspect checkpoint');
 if(file_put_contents($backup,json_encode($prepared,JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES))===false)throw new RuntimeException('Backup failed');chmod($backup,0600);
 $wpdb->query('START TRANSACTION');
 try {
 foreach($prepared as$row){$result=wp_update_post(['ID'=>$row['post_id'],'post_content'=>wp_slash($row['after'])],true);if(is_wp_error($result))throw new RuntimeException($result->get_error_message());
  $post=get_post($row['post_id']);if($post->post_content!==$row['after']||$post->post_title!==$row['title']||$post->post_name!==$row['slug']||get_post_meta($post->ID,'_mee_editorial_images',true)!==$row['image_ids'])throw new RuntimeException('Verification failed '.$row['id']);
  add_post_meta($post->ID,'_mee_presentation_log',['date'=>gmdate('c'),'reason'=>$batch['reason'],'before_sha256'=>hash('sha256',$row['before']),'after_sha256'=>hash('sha256',$row['after'])]);
 }
 $wpdb->query('COMMIT');
 }catch(Throwable $error){$wpdb->query('ROLLBACK');foreach($prepared as$row)clean_post_cache($row['post_id']);throw $error;}
}
echo json_encode(['applied'=>$apply,'count'=>count($prepared),'entries'=>array_map(fn($row)=>['id'=>$row['id'],'post_id'=>$row['post_id'],'url'=>get_permalink($row['post_id']),'after_sha256'=>hash('sha256',$row['after'])],$prepared)],JSON_PRETTY_PRINT|JSON_UNESCAPED_SLASHES);
