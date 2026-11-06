#!/bin/sh
set -eu
mkdir -p /var/www/html/wp-content/themes /var/www/html/wp-content/plugins
# MEE code follows the repository. Third-party packages are bootstrapped only
# when absent so dashboard updates survive container recreation.
cp -a /opt/mee/themes/mee-child /var/www/html/wp-content/themes/
cp -a /opt/mee/plugins/mee-editorial /var/www/html/wp-content/plugins/
if [ ! -f /var/www/html/wp-content/themes/hello-elementor/style.css ]; then
    cp -a /opt/mee/themes/hello-elementor /var/www/html/wp-content/themes/
fi
if [ ! -f /var/www/html/wp-content/plugins/two-factor/two-factor.php ]; then
    cp -a /opt/mee/plugins/two-factor /var/www/html/wp-content/plugins/
fi
if [ ! -f /var/www/html/wp-content/plugins/seo-by-rank-math/rank-math.php ]; then
    cp -R /opt/mee/vendor/seo-by-rank-math /var/www/html/wp-content/plugins/seo-by-rank-math
fi
# The owner explicitly authorized dashboard installs and updates on 2026-11-06.
# Limit ownership changes to themes and plugins; leave config/secrets untouched.
chown -R www-data:www-data /var/www/html/wp-content/themes /var/www/html/wp-content/plugins
exec docker-entrypoint.sh "$@"
