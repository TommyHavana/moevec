<?php
defined('ABSPATH') || exit;

add_action('wp_enqueue_scripts', function () {
    wp_enqueue_style('hello-elementor-parent', get_template_directory_uri() . '/style.css', [], wp_get_theme('hello-elementor')->get('Version'));
    wp_enqueue_style('mee-editorial', get_stylesheet_uri(), ['hello-elementor-parent'], wp_get_theme()->get('Version'));
});

add_action('after_setup_theme', function () {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', ['search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script']);
    add_theme_support('custom-logo');
});

function mee_frontend_url() {
    return defined('MEE_FRONTEND_URL') ? MEE_FRONTEND_URL : 'https://moevec.org/';
}

function mee_category_nav() {
    $categories = get_categories(['hide_empty' => false]);
    if (!$categories) return;
    echo '<nav class="mee-termnav" aria-label="Categorías editoriales">';
    foreach ($categories as $category) {
        if ($category->slug === 'uncategorized' || $category->slug === 'sin-categoria') continue;
        echo '<a href="' . esc_url(get_category_link($category)) . '">' . esc_html($category->name) . '</a>';
    }
    echo '</nav>';
}
