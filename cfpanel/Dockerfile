FROM alpine:3.8
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV HOST_KEY=YOUR_CLOUDFLARE_API_KEY \
    HOST_MAIL=YOUR_CLOUDFLARE_MAIL

RUN apk --no-cache --virtual php-exts add php7          \
                                          php7-fpm      \
                                          php7-json     \
                                          php7-gettext  \
                                          php7-curl     \
                                          php7-apcu   &&\
    apk --no-cache add nginx git                                              && \
    git clone --depth 1 https://github.com/ZE3kr/Cloudflare-CNAME-Setup /app  && \
    cp /app/config.example.php /app/config.php && apk del --purge git                                   

COPY nginx.conf   /etc/nginx/nginx.conf
COPY php-fpm.conf /etc/php7/php-fpm.conf

CMD sed -i "s/e9e4498f0584b7098692512db0c62b48/${HOST_KEY}/g" /app/config.php && \
    sed -i "s/ze3kr@example.com/${HOST_MAIL}/g"               /app/config.php && \
    nginx                                                                     && \
    php-fpm7 --nodaemonize --fpm-config /etc/php7/php-fpm.conf -c /etc/php7/php.ini