FROM wordpress:cli-php8.3
COPY deploy/install-wordpress.sh /opt/mee/install-wordpress.sh

COPY public/images/topics /opt/mee/topic-images
