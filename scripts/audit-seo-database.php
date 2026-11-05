<?php
/** Read-only audit of reviewed metadata, taxonomy and original image files. CLI only. */
if(PHP_SAPI!=='cli')exit(1);
require '/var/www/html/wp-load.php';
require_once ABSPATH.'wp-admin/includes/plugin.php';
$base=WP_PLUGIN_DIR.'/mee-editorial/data/';
$manifest=json_decode(file_get_contents($base.'seo-migration.json'),true);
$plan=[];foreach(json_decode(file_get_contents($base.'production-plan.json'),true)as$entry)$plan[$entry['id']]=$entry;
$posts=[];foreach(get_posts(['post_type'=>'post','post_status'=>'publish','numberposts'=>-1,'meta_key'=>'_mee_plan_id'])as$post)$posts[get_post_meta($post->ID,'_mee_plan_id',true)]=$post;
$rows=[];$errors=[];$image_count=0;
foreach($manifest as$entry){
    $id=$entry['id'];$post=$posts[$id]??null;$issues=[];$images=[];
    if(!$post){$errors[]=$id.': missing published article';continue;}
    $url=get_permalink($post);$expected=$plan[$id];
    if($post->post_title!==$entry['title']||$post->post_name!==$entry['slug'])$issues[]='title/slug changed';
    foreach(['rank_math_title'=>'seo_title','rank_math_description'=>'description','rank_math_focus_keyword'=>'keyword']as$key=>$field){if(get_post_meta($post->ID,$key,true)!==$entry[$field])$issues[]=$key.' differs';}
    if(get_post_meta($post->ID,'rank_math_canonical_url',true)!==$url)$issues[]='canonical differs';
    $categories=wp_get_post_categories($post->ID,['fields'=>'slugs']);sort($categories);
    $required=[$expected['area'],$expected['topic']];sort($required);
    if($categories!==$required)$issues[]='category assignment differs';
    $tags=wp_get_post_tags($post->ID,['fields'=>'slugs']);
    if(!in_array(sanitize_title($expected['level']),$tags,true)||!in_array($expected['topic'],$tags,true))$issues[]='topic/level tags absent';
    foreach((array)get_post_meta($post->ID,'_mee_editorial_images',true)as$attachment_id){
        $role=get_post_meta($attachment_id,'_mee_image_role',true);$file=get_attached_file($attachment_id);$meta=wp_get_attachment_metadata($attachment_id);
        $image=$entry['images'][$role]??null;$attachment=get_post($attachment_id);
        if(!$image||!is_file($file)){ $issues[]='missing image '.$role;continue; }
        $alt=get_post_meta($attachment_id,'_wp_attachment_image_alt',true);
        if(get_post_meta($attachment_id,'_mee_plan_id',true)!==$id||$alt!==$image['alt']||$attachment->post_content!==$image['description'])$issues[]='image metadata differs '.$role;
        if(basename($file)!==$image['file'])$issues[]='image file changed '.$role;
        $width=$meta['width']??0;$height=$meta['height']??0;
        $dimensions=$role==='featured'?[1200,630]:[1600,900];
        if([$width,$height]!==$dimensions||filesize($file)>=250000||get_post_mime_type($attachment_id)!=='image/webp')$issues[]='image format/size '.$role;
        $images[]=['id'=>$attachment_id,'role'=>$role,'url'=>wp_get_attachment_url($attachment_id),'alt'=>$alt,'width'=>$width,'height'=>$height,'bytes'=>filesize($file),'sha256'=>hash_file('sha256',$file)];$image_count++;
    }
    if(count($images)!==3)$issues[]='image count';
    if($issues)$errors[]=['id'=>$id,'issues'=>$issues];
    $rows[]=['id'=>$id,'number'=>$expected['number'],'title'=>$post->post_title,'url'=>$url,'seo_title'=>$entry['seo_title'],'description'=>$entry['description'],'keyword'=>$entry['keyword'],'score'=>(int)get_post_meta($post->ID,'rank_math_seo_score',true),'categories'=>$categories,'images'=>$images];
}
$scores=array_column($rows,'score');
$report=['checked_at'=>gmdate('c'),'articles'=>count($rows),'images'=>$image_count,'categories'=>wp_count_terms(['taxonomy'=>'category','hide_empty'=>false]),'drafts'=>(int)(wp_count_posts()->draft??0),'rank_math_version'=>get_plugin_data(WP_PLUGIN_DIR.'/seo-by-rank-math/rank-math.php')['Version'],'rank_math_active'=>is_plugin_active('seo-by-rank-math/rank-math.php'),'plugin_parent_writable'=>is_writable(WP_PLUGIN_DIR),'score'=>['count'=>count($scores),'min'=>min($scores),'max'=>max($scores),'mean'=>array_sum($scores)/count($scores),'green'=>count(array_filter($scores,fn($n)=>$n>=80)),'below_50'=>count(array_filter($scores,fn($n)=>$n<50))],'errors'=>$errors,'entries'=>$rows];
echo json_encode($report,JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES)."\n";
exit($errors?2:0);
