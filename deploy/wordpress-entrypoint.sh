#!/bin/sh
set -eu
mkdir -p /var/www/html/wp-content/themes /var/www/html/wp-content/plugins
cp -a /opt/mee/themes/. /var/www/html/wp-content/themes/
cp -a /opt/mee/plugins/. /var/www/html/wp-content/plugins/
# Bootstrap only the explicitly requested plugin. Keep the protected parent
# directory and preserve any subsequent installed Rank Math version in the volume.
if [ ! -f /var/www/html/wp-content/plugins/seo-by-rank-math/rank-math.php ]; then
    cp -R /opt/mee/vendor/seo-by-rank-math /var/www/html/wp-content/plugins/seo-by-rank-math
fi
chown -R www-data:www-data /var/www/html/wp-content/themes/hello-elementor /var/www/html/wp-content/themes/mee-child /var/www/html/wp-content/plugins/mee-editorial
exec docker-entrypoint.sh "$@"
