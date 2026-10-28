<!doctype html><html <?php language_attributes(); ?>><head><meta charset="<?php bloginfo('charset'); ?>"><meta name="viewport" content="width=device-width, initial-scale=1"><?php wp_head(); ?></head>
<body <?php body_class(); ?>><?php wp_body_open(); ?>
<a class="mee-skip" href="#contenido">Saltar al contenido</a>
<header class="mee-header"><a class="mee-brand" href="<?php echo esc_url(mee_frontend_url()); ?>" aria-label="MEE, volver al inicio"><img src="<?php echo esc_url(get_stylesheet_directory_uri() . '/assets/mee-logo-tinta-rojo-640.webp'); ?>" alt="MEE" width="200" height="76"></a><nav aria-label="Navegación principal"><a href="<?php echo esc_url(mee_frontend_url()); ?>#areas">Áreas</a><a href="<?php echo esc_url(home_url('/')); ?>">Editorial</a></nav></header>
