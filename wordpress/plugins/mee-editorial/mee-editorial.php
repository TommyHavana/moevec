<?php
/**
 * Plugin Name: MEE Editorial
 * Description: Categorías y campos del blog editorial de MEE.
 * Version: 0.1.0
 * Requires PHP: 8.0
 * Text Domain: mee-editorial
 */

defined('ABSPATH') || exit;

function mee_editorial_categories() {
    return [
        'educacion-y-valores' => 'Educación y valores',
        'tribu' => 'Tribu',
        'comunidad' => 'Comunidad',
        'trabajo' => 'Trabajo',
        'capitalismo-consciente' => 'Capitalismo consciente',
        'economia-compartida' => 'Economía compartida',
        'politica-y-economia' => 'Política y economía',
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
