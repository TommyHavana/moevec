<?php
/** Run explicitly with WP-CLI eval-file. Idempotent: never edits existing articles. */
if(!defined('ABSPATH') || !defined('WP_CLI'))exit;
require_once ABSPATH.'wp-admin/includes/image.php';
$topics=json_decode(file_get_contents(__DIR__.'/data/topics.json'),true);
$ids=[];$created=0;$existing=0;$area_positions=[];
foreach(mee_editorial_categories()as$slug=>$name){$term=get_term_by('slug',$slug,'category');if(!$term){$new=wp_insert_term($name,'category',['slug'=>$slug]);if(is_wp_error($new))WP_CLI::error($new->get_error_message());$term=get_term($new['term_id'],'category');}wp_update_term($term->term_id,'category',['name'=>$name]);$ids[$slug]=$term->term_id;}
foreach($topics as$index=>$topic){
 $area_position=$area_positions[$topic['area']]??0;$area_positions[$topic['area']]=$area_position+1;$area_index=array_search($topic['area'],array_keys(mee_editorial_categories()),true);$display_order=(int)$topic['depth']*10000+$area_position*7+$area_index;
 $slug=$topic['slug'];$parent=$ids[$topic['parent']??$topic['area']];$term=get_term_by('slug',$slug,'category');
 if(!$term){$insert=wp_insert_term($topic['name'],'category',['slug'=>$slug,'parent'=>$parent,'description'=>$topic['benefit']]);if(is_wp_error($insert))WP_CLI::error($insert->get_error_message());$term=get_term($insert['term_id'],'category');}
 elseif((int)$term->parent!==$parent){WP_CLI::warning('Existing taxonomy parent differs for '.$slug.'; preserved.');}
 $ids[$slug]=$term->term_id;
 $post_slug='muestra-'.$topic['area'].'-'.$slug;
 $found=get_page_by_path($post_slug,OBJECT,'post');
 if($found&&get_post_meta($found->ID,'_mee_demo',true)){
  update_post_meta($found->ID,'_mee_demo_order',$display_order);
  $repaired_content=str_replace(['Examiner ','dans le contexte de'],['Examinar ','en el contexto de'],$found->post_content);
  $repaired_excerpt=str_replace(['Examiner ','dans le contexte de'],['Examinar ','en el contexto de'],$found->post_excerpt);
  if($repaired_content!==$found->post_content||$repaired_excerpt!==$found->post_excerpt)wp_update_post(['ID'=>$found->ID,'post_content'=>$repaired_content,'post_excerpt'=>$repaired_excerpt]);
 }
 if($found&&(!get_post_meta($found->ID,'_mee_demo',true)||($found->post_status==='publish'&&has_post_thumbnail($found->ID)))){$existing++;continue;}
 $image='https://moevec.org'.$topic['image'];$name=esc_html($topic['name']);$benefit=esc_html(ucfirst($topic['benefit']));$area=esc_html($topic['areaName']);
 $prompts=[
 '¿Qué decisión puedes tomar por ti y qué información te falta para tomarla con criterio?',
 '¿Qué estás recibiendo de otras generaciones y qué te gustaría transmitir?',
 '¿Qué necesita cada persona del intercambio y cómo se puede hacer visible?',
 '¿Qué recurso puedes desarrollar hoy para abrir una opción de trabajo mañana?',
 '¿Qué se aporta, qué se recibe y bajo qué condiciones se produce el intercambio?',
 '¿Cómo puede crecer un recurso compartido sin perder la autonomía de quienes participan?',
 '¿Qué regla se está examinando, a quién afecta y con qué evidencia se pueden estudiar sus efectos?'
 ];
 $ai=array_search($topic['area'],array_keys(mee_editorial_categories()),true);$question=$prompts[$ai];
 $body='<!-- wp:paragraph {"className":"mee-demo-note"} --><p class="mee-demo-note"><strong>Maqueta editorial.</strong> Esta entrada permite comprobar el diseño, las imágenes y la navegación de este tema. El ejercicio es hipotético y está pendiente de desarrollo y revisión editorial.</p><!-- /wp:paragraph -->';
 $body.='<!-- wp:heading {"anchor":"idea"} --><h2 class="wp-block-heading" id="idea">La idea de partida</h2><!-- /wp:heading --><!-- wp:paragraph --><p>'.$benefit.' Este tema forma parte de '.$area.' y propone una pregunta para explorar cómo una idea puede convertirse en una capacidad concreta.</p><!-- /wp:paragraph -->';
 $body.='<!-- wp:quote --><blockquote class="wp-block-quote"><p>'.esc_html($question).'</p></blockquote><!-- /wp:quote -->';
 $body.='<!-- wp:heading {"anchor":"practica"} --><h2 class="wp-block-heading" id="practica">Un ejercicio para llevarlo a la práctica</h2><!-- /wp:heading --><!-- wp:paragraph --><p>Elige una situación cotidiana relacionada con '.$name.'. Describe lo que ocurre antes de decidir qué cambiar. Distingue las personas implicadas, los recursos disponibles y las condiciones que cada una puede aceptar.</p><!-- /wp:paragraph -->';
 $body.='<!-- wp:list {"ordered":true} --><ol class="wp-block-list"><!-- wp:list-item --><li>Define la pregunta con tus propias palabras y anota qué dato necesitas conocer.</li><!-- /wp:list-item --><!-- wp:list-item --><li>Compara al menos dos opciones y haz visibles sus límites.</li><!-- /wp:list-item --><!-- wp:list-item --><li>Propón un paso pequeño, reversible y que permita aprender algo.</li><!-- /wp:list-item --></ol><!-- /wp:list -->';
 if($index%2===0)$body.='<!-- wp:image {"sizeSlug":"large"} --><figure class="wp-block-image size-large"><img src="'.esc_url($image).'" alt="'.esc_attr($topic['concept']).'" width="1200" height="900" loading="lazy"/><figcaption>'.esc_html($topic['concept']).'. Ilustración conceptual de MEE.</figcaption></figure><!-- /wp:image -->';
 $body.='<!-- wp:heading {"anchor":"ejemplo"} --><h2 class="wp-block-heading" id="ejemplo">Un caso hipotético, para conversar</h2><!-- /wp:heading --><!-- wp:paragraph --><p>Imagina que un pequeño grupo quiere aplicar esta idea a una actividad compartida. Antes de actuar, cada participante explica qué puede aportar, qué necesita y qué espera. El grupo acuerda una prueba limitada y un momento para revisar lo aprendido. Este ejemplo no describe una experiencia real ni demuestra un resultado.</p><!-- /wp:paragraph -->';
 $body.='<!-- wp:heading {"anchor":"preguntas"} --><h2 class="wp-block-heading" id="preguntas">Preguntas que quedan abiertas</h2><!-- /wp:heading --><!-- wp:list --><ul class="wp-block-list"><!-- wp:list-item --><li>¿Qué cambiaría si los recursos o las condiciones fueran distintos?</li><!-- /wp:list-item --><!-- wp:list-item --><li>¿Quién podría aportar otra perspectiva y qué evidencia permitiría contrastarla?</li><!-- /wp:list-item --><!-- wp:list-item --><li>¿Cómo sabríamos si el siguiente paso ha sido útil?</li><!-- /wp:list-item --></ul><!-- /wp:list -->';
 $body.='<!-- wp:paragraph --><p>Esta muestra no presenta datos empíricos ni sustituye una investigación sobre el tema. La versión editorial deberá incorporar contexto, referencias primarias y una revisión de sus afirmaciones antes de dejar de ser una maqueta.</p><!-- /wp:paragraph --><!-- wp:paragraph --><p><a href="https://moevec.org/areas/'.esc_attr($topic['area']).'/#'.esc_attr($topic['slug']).'">Volver al mapa de '.$area.'</a> o <a href="https://moevec.org/contacto/">proponer una perspectiva a MEE</a>.</p><!-- /wp:paragraph -->';
 $post_id=$found ? $found->ID : wp_insert_post(['post_type'=>'post','post_status'=>'draft','post_title'=>$topic['name'],'post_name'=>$post_slug,'post_excerpt'=>ucfirst($topic['benefit']),'post_content'=>$body,'post_category'=>array_values(array_unique([$ids[$topic['area']],$term->term_id])),'meta_input'=>['_mee_demo'=>'1','_mee_demo_order'=>$display_order,'_mee_area'=>$topic['area'],'_mee_topic'=>$slug]],true);
 if(is_wp_error($post_id))WP_CLI::error($post_id->get_error_message());
 $source='/opt/mee/topic-images/'.$topic['area'].'/'.$slug.'-1200.webp';
 if(!is_readable($source))WP_CLI::error('Missing image '.$source);
 $upload=wp_upload_bits($topic['area'].'-'.$slug.'.webp',null,file_get_contents($source));
 if($upload['error'])WP_CLI::error($upload['error']);
 $attachment=wp_insert_attachment(['post_mime_type'=>'image/webp','post_title'=>$topic['name'],'post_status'=>'inherit'], $upload['file'],$post_id,true);
 if(is_wp_error($attachment))WP_CLI::error($attachment->get_error_message());
 wp_update_attachment_metadata($attachment,wp_generate_attachment_metadata($attachment,$upload['file']));
 update_post_meta($attachment,'_wp_attachment_image_alt',$topic['concept']);set_post_thumbnail($post_id,$attachment);
 wp_update_post(['ID'=>$post_id,'post_status'=>'publish']);$created++;
}
foreach($ids as$id){$q=new WP_Query(['post_type'=>'post','post_status'=>'publish','posts_per_page'=>1,'fields'=>'ids','cat'=>$id,'meta_query'=>[['key'=>'_mee_demo','compare'=>'NOT EXISTS']]]);if(!$q->posts)update_term_meta($id,'_mee_demo_only','1');else delete_term_meta($id,'_mee_demo_only');}
update_option('posts_per_page',12);$real=new WP_Query(['post_type'=>'post','post_status'=>'publish','posts_per_page'=>1,'fields'=>'ids','meta_query'=>[['key'=>'_mee_demo','compare'=>'NOT EXISTS']]]);update_option('mee_has_real_articles',(bool)$real->posts,false);
WP_CLI::success(wp_json_encode(['topics'=>count($topics),'created'=>$created,'existing'=>$existing,'categories'=>count($ids)]));
