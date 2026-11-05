<?php
defined('ABSPATH') || exit;
function mee_editorial_dates($post_id){
 $record=get_post_meta($post_id,'_mee_review_record',true);
 $date=is_array($record)?($record['checked_on']??''):'';
 if(!preg_match('/^\d{4}-\d{2}-\d{2}$/',$date))$date=mee_discovery_data('editorial-reviews')[get_post_meta($post_id,'_mee_plan_id',true)]['reviewed_on']??'';
 echo '<div class="mee-editorial-dates"><span>Publicado: <time datetime="'.esc_attr(get_the_date(DATE_W3C,$post_id)).'">'.esc_html(get_the_date('j \d\e F \d\e Y',$post_id)).'</time></span>';
 if($date)echo '<span>Revisión de contenido: <time datetime="'.esc_attr($date).'">'.esc_html(wp_date('j \d\e F \d\e Y',strtotime($date.' 12:00:00 UTC'))).'</time></span>';
 echo '<a href="https://moevec.org/metodo-editorial/">Fuentes, firma y correcciones</a></div>';
}
function mee_empty_category_parent(){
 if(!is_category())return null;
 $term=get_queried_object();if(!$term||$term->count>0)return null;
 while($term->parent){$term=get_term($term->parent,'category');if(is_wp_error($term))return null;if($term->count>0)return $term;}
 return null;
}

add_action('admin_menu',function(){add_management_page('Revisión editorial MEE','Revisión editorial','edit_posts','mee-quality',function(){
 echo '<div class="wrap"><h1>Calendario de revisión editorial</h1><p>Fechas acreditadas en los registros de contenido. Las próximas fechas son un calendario de trabajo: no equivalen a una revisión ya realizada. Priorizar una corrección o un cambio de fuente antes del plazo previsto.</p><table class="widefat striped"><thead><tr><th>ID</th><th>Título</th><th>Revisión registrada</th><th>Próxima revisión</th><th>Responsable</th><th>Motivo de adelanto</th></tr></thead><tbody>';
 $catalog=mee_discovery_data('article-discovery');$rows=mee_discovery_data('editorial-reviews');uasort($rows,fn($a,$b)=>strcmp($a['next_review_on'],$b['next_review_on']));foreach($rows as$id=>$row){$article=$catalog[$id]??null;if(!$article)continue;echo '<tr><td>'.esc_html($id).'</td><td><a href="'.esc_url($article['url']).'">'.esc_html($article['title']).'</a></td><td>'.esc_html($row['reviewed_on']).'</td><td>'.esc_html($row['next_review_on']).'</td><td>'.esc_html($row['owner']).'</td><td>'.esc_html($row['trigger']).'</td></tr>';}
 echo '</tbody></table></div>';
 });});
