#!/bin/sh
set -eu
mkdir -p /var/www/html/wp-content/themes /var/www/html/wp-content/plugins
cp -a /opt/mee/themes/. /var/www/html/wp-content/themes/
cp -a /opt/mee/plugins/. /var/www/html/wp-content/plugins/
chown -R www-data:www-data /var/www/html/wp-content/themes/hello-elementor /var/www/html/wp-content/themes/mee-child /var/www/html/wp-content/plugins/mee-editorial
exec docker-entrypoint.sh "$@"
