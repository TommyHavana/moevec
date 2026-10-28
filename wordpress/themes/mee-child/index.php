<?php get_header(); ?>
<main id="contenido"><div class="mee-wrap"><p class="mee-kicker">MEE / Editorial</p><h1 class="mee-title"><?php echo is_category() ? esc_html(single_cat_title('', false)) : 'Ideas para movernos.'; ?></h1><p class="mee-intro"><?php echo is_category() ? esc_html(category_description() ? wp_strip_all_tags(category_description()) : 'Artículos sobre esta área.') : 'Ideas, perspectivas y conversaciones para pensar la evolución económica.'; ?></p></div>
<?php mee_category_nav(); ?>
<?php if (have_posts()) : ?><div class="mee-post-grid"><?php while (have_posts()) : the_post(); ?><a class="mee-post-card" href="<?php the_permalink(); ?>">
<?php if (has_post_thumbnail()) : the_post_thumbnail('large', ['loading' => 'lazy']); else : ?><span class="mee-fallback" aria-hidden="true">✳</span><?php endif; ?>
<div class="mee-post-card-body"><h2><?php the_title(); ?></h2><small><?php echo esc_html(get_the_date()); ?> ↗</small></div></a><?php endwhile; ?></div><div class="mee-pagination"><?php previous_posts_link('← Más recientes'); next_posts_link('Anteriores →'); ?></div>
<?php else : ?><p class="mee-empty">Todavía no hay artículos publicados en esta sección.</p><?php endif; ?></main>
<?php get_footer(); ?>
