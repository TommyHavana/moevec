<?php
/** Explicit deployment helper: php publish-editorial.php /path/to/article.json */
if (PHP_SAPI!=='cli' || empty($argv[1])) exit(1);
require '/var/www/html/wp-load.php';
require_once ABSPATH.'wp-admin/includes/image.php';
require_once ABSPATH.'wp-admin/includes/file.php';
require_once ABSPATH.'wp-admin/includes/media.php';
$manifest=json_decode(file_get_contents($argv[1]),true,512,JSON_THROW_ON_ERROR);
$matches=array_values(array_filter(mee_production_plan(),fn($row)=>$row['id']===$manifest['id']));
if(count($matches)!==1) throw new RuntimeException('Identificador ajeno al plan');
$entry=$matches[0];
if($entry['slug']!==$manifest['slug'] || $entry['title']!==$manifest['title']) throw new RuntimeException('El título o slug difiere del plan');
$existing=get_posts(['post_type'=>'post','post_status'=>['publish','draft','pending','future','private','trash'],'posts_per_page'=>2,'meta_key'=>'_mee_plan_id','meta_value'=>$entry['id']]);
if($existing) { echo json_encode(['existing'=>true,'post_id'=>$existing[0]->ID,'status'=>$existing[0]->post_status,'url'=>get_permalink($existing[0])]);exit; }
if(get_page_by_path($entry['slug'],OBJECT,'post')) throw new RuntimeException('Slug ocupado: revisar antes de continuar');
$categories=[];
foreach([$entry['area'],$entry['topic']] as $slug){$term=get_term_by('slug',$slug,'category');if(!$term)throw new RuntimeException('Categoría ausente: '.$slug);$categories[]=(int)$term->term_id;}
$body=file_get_contents(dirname($argv[1]).'/article.html');
if(substr_count($body,'{{INTERIOR_1}}')!==1 || substr_count($body,'{{INTERIOR_2}}')!==1)throw new RuntimeException('Faltan posiciones de imágenes interiores');
$word_count=preg_match_all('/[\p{L}\p{N}]+(?:[’\x{0027}-][\p{L}\p{N}]+)*/u',wp_strip_all_tags($body));
if($word_count<600 || empty($manifest['review']['sources_verified']) || empty($manifest['review']['editorial_checked']))throw new RuntimeException('Falta revisión editorial o extensión');
if(count($manifest['images'])!==3)throw new RuntimeException('Se requieren tres imágenes propias');
$hashes=[];
foreach($manifest['images']as$image){$path=dirname($argv[1]).'/'.$image['file'];$size=getimagesize($path);if(!$size || $size['mime']!=='image/webp' || filesize($path)>250000 || empty($image['alt']))throw new RuntimeException('Imagen inválida');$hashes[]=hash_file('sha256',$path);}
if(count(array_unique($hashes))!==3)throw new RuntimeException('Las tres imágenes deben ser distintas');
$post_id=wp_insert_post(['post_type'=>'post','post_status'=>'draft','post_author'=>1,'post_title'=>$entry['title'],'post_name'=>$entry['slug'],'post_excerpt'=>$manifest['description'],'post_category'=>$categories,'comment_status'=>'closed','ping_status'=>'closed','meta_input'=>['_mee_plan_id'=>$entry['id'],'meta_mee_id'=>$entry['id'],'_mee_plan_number'=>$entry['number'],'_mee_area'=>$entry['area'],'_mee_topic'=>$entry['topic'],'_mee_seo_title'=>$manifest['seo_title'],'_mee_seo_description'=>$manifest['description'],'_mee_focus_keyword'=>$manifest['keyword'],'_mee_signature'=>'Anacleto','mee_kicker'=>$entry['topic_name'].' · '.$entry['level'],'mee_standfirst'=>$manifest['standfirst']]],true);
if(is_wp_error($post_id))throw new RuntimeException($post_id->get_error_message());
$uploaded=[];
foreach($manifest['images']as$role=>$image){
 $path=dirname($argv[1]).'/'.$image['file'];$upload=wp_upload_bits($image['file'],null,file_get_contents($path));if($upload['error'])throw new RuntimeException($upload['error']);
 $attachment=wp_insert_attachment(['post_mime_type'=>'image/webp','post_title'=>$image['title'],'post_excerpt'=>'','post_status'=>'inherit'], $upload['file'],$post_id,true);
 if(is_wp_error($attachment))throw new RuntimeException($attachment->get_error_message());
 wp_update_attachment_metadata($attachment,wp_generate_attachment_metadata($attachment,$upload['file']));
 update_post_meta($attachment,'_wp_attachment_image_alt',$image['alt']);update_post_meta($attachment,'_mee_plan_id',$entry['id']);update_post_meta($attachment,'_mee_image_role',$role);
 $uploaded[$role]=$attachment;
 if($role==='featured')set_post_thumbnail($post_id,$attachment);
 else {$figure='<figure class="wp-block-image size-large">'.wp_get_attachment_image($attachment,'large',false,['loading'=>'lazy','decoding'=>'async','sizes'=>'(max-width: 800px) calc(100vw - 40px), 720px']).'<figcaption>'.esc_html($image['caption']).'</figcaption></figure>';$body=str_replace($role==='interior-1'?'{{INTERIOR_1}}':'{{INTERIOR_2}}',$figure,$body);}
}
$tags=[];foreach($manifest['tags']as$slug){$term=get_term_by('slug',$slug,'post_tag');if(!$term){$new=wp_insert_term($slug,'post_tag',['slug'=>$slug]);if(is_wp_error($new))throw new RuntimeException($new->get_error_message());$tags[]=(int)$new['term_id'];}else $tags[]=(int)$term->term_id;}
wp_set_post_terms($post_id,$tags,'post_tag');
update_post_meta($post_id,'_mee_editorial_images',array_values($uploaded));
update_post_meta($post_id,'_mee_review_record',$manifest['review']);
update_post_meta($post_id,'_mee_reviewed','1');
$result=wp_update_post(['ID'=>$post_id,'post_content'=>wp_slash($body),'post_status'=>'publish'],true);
if(is_wp_error($result))throw new RuntimeException($result->get_error_message());
$register=get_page_by_path('registro-de-produccion-mee',OBJECT,'page');
if(!$register)wp_insert_post(['post_type'=>'page','post_status'=>'private','post_title'=>'Registro de producción MEE','post_name'=>'registro-de-produccion-mee','post_content'=>'[mee_production_register]','post_author'=>1,'comment_status'=>'closed']);
$rows=mee_production_snapshot();
echo json_encode(['created'=>true,'number'=>$entry['number'],'id'=>$entry['id'],'post_id'=>$post_id,'url'=>get_permalink($post_id),'words'=>$word_count,'image_ids'=>$uploaded,'done'=>count(array_filter($rows,fn($row)=>$row['status']==='terminada')),'remaining'=>count(array_filter($rows,fn($row)=>$row['status']==='pendiente'))],JSON_UNESCAPED_SLASHES|JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
