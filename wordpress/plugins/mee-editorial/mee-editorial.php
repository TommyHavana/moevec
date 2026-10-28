<?php
/**
 * Plugin Name: MEE Editorial
 * Description: Categorías y campos del blog editorial de MEE.
 * Version: 1.0.0
 * Requires PHP: 8.0
 * Text Domain: mee-editorial
 */

defined('ABSPATH') || exit;

function mee_editorial_categories() {
    return [
        'educacion-y-valores' => 'Educación y Valores',
        'tribu' => 'Tribu',
        'comunidad' => 'Comunidad',
        'trabajo' => 'Trabajo',
        'capitalismo-consciente' => 'Capitalismo Consciente',
        'economia-compartida' => 'Economía Compartida',
        'politica-y-economia' => 'Política y Economía',
    ];
}

register_activation_hook(__FILE__, function () {
    foreach (mee_editorial_categories() as $slug => $name) {
        if (!term_exists($slug, 'category')) {
            wp_insert_term($name, 'category', ['slug' => $slug]);
        }
    }
});

// Los campos son opcionales: los artículos muestran excerpt si ACF no está activo.
add_action('acf/init', function () {
    if (!function_exists('acf_add_local_field_group')) return;
    acf_add_local_field_group([
        'key' => 'group_mee_article',
        'title' => 'MEE · Editorial',
        'fields' => [
            ['key' => 'field_mee_kicker', 'label' => 'Antetítulo', 'name' => 'mee_kicker', 'type' => 'text'],
            ['key' => 'field_mee_standfirst', 'label' => 'Entradilla', 'name' => 'mee_standfirst', 'type' => 'textarea', 'rows' => 3],
        ],
        'location' => [[['param' => 'post_type', 'operator' => '==', 'value' => 'post']]],
    ]);
});

foreach (["contact", "security", "seo", "network", "production"] as $module) require_once __DIR__ . "/inc/" . $module . ".php";

add_action('add_meta_boxes_post', function() {
    add_meta_box('mee-editorial-state', 'Producción editorial MEE', function($post) {
        wp_nonce_field('mee-editorial-state-'.$post->ID, 'mee_editorial_nonce');
        $id=get_post_meta($post->ID,'_mee_plan_id',true);
        $number=get_post_meta($post->ID,'_mee_plan_number',true);
        if (!$id) { echo '<p>Esta entrada no está asignada a una ficha del plan de 840 artículos.</p>'; return; }
        echo '<p><strong>N.º '.esc_html($number).'/840 · '.esc_html($id).'</strong></p>';
        echo '<label><input type="checkbox" name="mee_reviewed" value="1" '.checked(get_post_meta($post->ID,'_mee_reviewed',true),'1',false).'> Texto, fuentes e imágenes revisados</label>';
        echo '<p>Antes de marcar la revisión, comprueba las afirmaciones y las tres ilustraciones propias. El registro también exige publicación, extensión y archivos válidos.</p>';
        echo '<p><a href="'.esc_url(admin_url('tools.php?page=mee-production')).'">Ver estado de las 840 entradas</a></p>';
    }, 'post', 'side');
});
add_action('save_post_post', function($id) {
    if (wp_is_post_autosave($id)||wp_is_post_revision($id)||!current_user_can('edit_post',$id)||empty($_POST['mee_editorial_nonce'])||!wp_verify_nonce(sanitize_text_field(wp_unslash($_POST['mee_editorial_nonce'])),'mee-editorial-state-'.$id)) return;
    if (!get_post_meta($id,'_mee_plan_id',true)) return;
    if (!empty($_POST['mee_reviewed'])) update_post_meta($id,'_mee_reviewed','1');
    else delete_post_meta($id,'_mee_reviewed');
},5);
