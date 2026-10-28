FROM wordpress:php8.3-apache
COPY wordpress/themes/hello-elementor /opt/mee/themes/hello-elementor
COPY wordpress/themes/mee-child /opt/mee/themes/mee-child
COPY wordpress/plugins/mee-editorial /opt/mee/plugins/mee-editorial
COPY deploy/wordpress-blog.conf /etc/apache2/conf-enabled/mee-blog.conf
COPY deploy/wordpress-entrypoint.sh /usr/local/bin/mee-wordpress-entrypoint
RUN chmod +x /usr/local/bin/mee-wordpress-entrypoint
ENTRYPOINT ["mee-wordpress-entrypoint"]
CMD ["apache2-foreground"]
