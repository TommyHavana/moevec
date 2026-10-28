#!/bin/sh
set -eu
cd /var/www/html

attempt=0
until test -f wp-config.php && test -f wp-includes/version.php; do
  attempt=$((attempt + 1))
  if [ "$attempt" -ge 60 ]; then
    echo "WordPress files did not become ready" >&2
    exit 1
  fi
  sleep 2
done

if ! wp core is-installed --path=/var/www/html --quiet; then
  WORDPRESS_ADMIN_PASSWORD=$(cat /run/mee-secrets/admin_password)
  wp core install \
    --path=/var/www/html \
    --url=https://moevec.org/blog \
    --title='MEE · Blog' \
    --admin_user=mee_admin \
    --admin_password="$WORDPRESS_ADMIN_PASSWORD" \
    --admin_email=admin@moevec.org \
    --skip-email \
    --quiet
  sample_ids=$(wp post list --post_type=post,page --format=ids --path=/var/www/html)
  if [ -n "$sample_ids" ]; then
    # The installer creates sample content. Remove it before the site opens.
    wp post delete $sample_ids --force --path=/var/www/html --quiet
  fi
fi

chmod 640 /var/www/html/wp-config.php
wp theme activate mee-child --path=/var/www/html --quiet
wp plugin activate two-factor --path=/var/www/html --quiet
wp plugin activate mee-editorial --path=/var/www/html --quiet
wp rewrite structure '/%postname%/' --hard --path=/var/www/html --quiet
wp option update blogdescription 'Movimiento de Evolución Económica' --path=/var/www/html --quiet

# Editorial production is explicit. Retired samples must never be regenerated.
