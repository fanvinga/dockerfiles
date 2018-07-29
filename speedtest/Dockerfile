FROM alpine:3.8
MAINTAINER FAN VINGA<fanalcest@gmail.com>

COPY . /app/
WORKDIR /app
EXPOSE 80

RUN apk --no-cache add php7		 \
		       php7-fpm 	 \
		       php7-json	 \
		       php-openssl       \
		       nginx          && \
    cp  nginx.conf /etc/nginx/        && cp php-fpm.conf             /etc/php7/        && \
    sed -i "s/memory_limit = 128M/memory_limit = 512M/g"             /etc/php7/php.ini && \
    sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 100M/g" /etc/php7/php.ini && \
    sed -i "s/post_max_size = 8M/post_max_size = 100M/g"             /etc/php7/php.ini

CMD nginx && \
    php-fpm7 --nodaemonize --fpm-config /etc/php7/php-fpm.conf -c /etc/php7/php.ini
