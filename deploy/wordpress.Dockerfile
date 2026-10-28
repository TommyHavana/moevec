FROM wordpress:php8.3-apache
COPY wordpress/themes/hello-elementor /opt/mee/themes/hello-elementor
COPY wordpress/themes/mee-child /opt/mee/themes/mee-child
COPY wordpress/plugins/mee-editorial /opt/mee/plugins/mee-editorial
COPY wordpress/plugins/two-factor /opt/mee/plugins/two-factor
RUN a2enmod expires headers
COPY deploy/wordpress-performance.conf /etc/apache2/conf-enabled/mee-performance.conf
RUN printf "expose_php=Off\n" > /usr/local/etc/php/conf.d/mee.ini
COPY deploy/wordpress-blog.conf /etc/apache2/conf-enabled/mee-blog.conf
COPY deploy/wordpress-entrypoint.sh /usr/local/bin/mee-wordpress-entrypoint
RUN chmod +x /usr/local/bin/mee-wordpress-entrypoint
ENTRYPOINT ["mee-wordpress-entrypoint"]
CMD ["apache2-foreground"]
