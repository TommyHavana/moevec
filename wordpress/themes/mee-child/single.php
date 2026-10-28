<?php get_header(); ?>
<main id="contenido"><?php while (have_posts()) : the_post(); ?><article <?php post_class('mee-article'); ?>><p class="mee-kicker"><?php $k = function_exists('get_field') ? get_field('mee_kicker') : null; echo esc_html($k ?: 'MEE / Editorial'); ?></p><h1><?php the_title(); ?></h1>
<?php $lead = function_exists('get_field') ? get_field('mee_standfirst') : null; if ($lead || has_excerpt()) : ?><p class="mee-standfirst"><?php echo esc_html($lead ?: get_the_excerpt()); ?></p><?php endif; ?>
<?php if (has_post_thumbnail()) the_post_thumbnail('full', ['class' => 'mee-feature']); ?><div class="entry-content"><?php the_content(); ?></div><p><a href="<?php echo esc_url(home_url('/')); ?>">← Volver al editorial</a></p></article><?php endwhile; ?></main>
<?php get_footer(); ?>
