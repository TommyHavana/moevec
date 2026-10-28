<?php
defined('ABSPATH') || exit;

function mee_production_plan() {
    static $plan;
    if ($plan === null) $plan = json_decode(file_get_contents(__DIR__.'/../data/production-plan.json'), true) ?: [];
    return $plan;
}

function mee_production_snapshot() {
    $posts = get_posts(['post_type'=>'post','post_status'=>['publish','draft','pending','future','private'], 'posts_per_page'=>-1, 'meta_key'=>'_mee_plan_id']);
    $by_id = [];
    foreach ($posts as $post) $by_id[get_post_meta($post->ID, '_mee_plan_id', true)] = $post;
    $rows = [];
    foreach (mee_production_plan() as $entry) {
        $post = $by_id[$entry['id']] ?? null;
        $images = $post ? array_unique(array_filter(array_map('intval', (array)get_post_meta($post->ID, '_mee_editorial_images', true)))) : [];
        $valid_images = array_filter($images, function($id) { return get_post_mime_type($id)==='image/webp' && is_file(get_attached_file($id)) && get_post_meta($id,'_wp_attachment_image_alt',true); });
        $words = $post ? preg_match_all('/[\p{L}\p{N}]+(?:[’\x{0027}-][\p{L}\p{N}]+)*/u', wp_strip_all_tags(strip_shortcodes($post->post_content))) : 0;
        $done = $post && $post->post_status==='publish' && count($valid_images)===3 && $words>=600 && get_post_meta($post->ID, '_mee_reviewed', true)==='1';
        $rows[] = array_merge($entry, ['status'=>$done?'terminada':($post?'en curso':'pendiente'), 'wp_status'=>$post?$post->post_status:null, 'post_id'=>$post?$post->ID:null, 'url'=>$post&&$post->post_status==='publish'?get_permalink($post):'', 'words'=>$words, 'images'=>count($valid_images)]);
    }
    return $rows;
}

function mee_production_register() {
    if (!current_user_can('edit_posts')) return '<p>Inicia sesión con una cuenta editorial para consultar el registro.</p>';
    $rows = mee_production_snapshot();
    $done = count(array_filter($rows, fn($row)=>$row['status']==='terminada'));
    $ongoing = count(array_filter($rows, fn($row)=>$row['status']==='en curso'));
    ob_start();
    echo '<p><strong>'.esc_html($done).'/840 terminadas</strong> · '.esc_html($ongoing).' en curso · '.esc_html(840-$done-$ongoing).' pendientes. Cada terminada incluye portada y dos apoyos interiores propios, en WebP.</p>';
    echo '<p>La numeración global conserva el orden de las 56 tandas del plan. «Terminada» exige publicación, revisión editorial, al menos 600 palabras y tres imágenes distintas con texto alternativo.</p>';
    echo '<div style="overflow-x:auto"><table class="widefat striped"><thead><tr><th>N.º /840</th><th>Tanda /56</th><th>ID · entrada /15</th><th>Artículo</th><th>Estado</th><th>Palabras</th><th>Imágenes /3</th><th>Acceso</th></tr></thead><tbody>';
    foreach ($rows as $row) {
        echo '<tr><td>'.esc_html($row['number']).'</td><td>'.esc_html($row['batch']).'</td><td>'.esc_html($row['id'].' · '.$row['entry'].'/15').'</td><td>'.esc_html($row['title']).'<br><small>'.esc_html($row['topic_name']).'</small></td><td>'.esc_html(ucfirst($row['status'])).'</td><td>'.esc_html($row['words']).'</td><td>'.esc_html($row['images']).'/3</td><td>';
        if ($row['post_id']) echo '<a href="'.esc_url(get_edit_post_link($row['post_id'])).'">Editar</a> ';
        if ($row['url']) echo '<a href="'.esc_url($row['url']).'">Ver</a>';
        echo '</td></tr>';
    }
    echo '</tbody></table></div>';
    return ob_get_clean();
}
add_shortcode('mee_production_register', 'mee_production_register');
add_action('admin_menu', function() { add_management_page('Plan editorial MEE · 840', 'Plan editorial · 840', 'edit_posts', 'mee-production', function() { echo '<div class="wrap"><h1>Plan editorial MEE · 840 entradas</h1>'.mee_production_register().'</div>'; }); });

// Retired sample URLs retain a useful route to their topic, without restoring samples.
add_action('template_redirect', function() {
    if (!is_404()) return;
    $path = trim((string)parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH), '/');
    foreach ((json_decode(file_get_contents(__DIR__.'/../data/topics.json'),true) ?: []) as $entry) {
        $entry['topic']=$entry['slug'];
        if ($path==='blog/muestra-'.$entry['area'].'-'.$entry['topic']) {
            $term=get_term_by('slug', $entry['topic'], 'category');
            if ($term) { wp_safe_redirect(get_category_link($term), 301); exit; }
        }
    }
}, 5);

add_filter('pre_get_document_title', function($title) { if (is_single()) { $seo=get_post_meta(get_the_ID(), '_mee_seo_title', true); if ($seo) return $seo; } return $title; });
add_filter('wp_robots', function($robots) { if (is_singular() && get_post_status()==='private') { $robots['noindex']=true; $robots['nofollow']=true; } if (is_tag(['fundamentos','desarrollo','aplicacion']) || is_date()) $robots['noindex']=true; return $robots; });
