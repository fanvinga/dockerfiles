FROM alpine:3
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV H5AI_VERSION=0.29.2 \
    LD_PRELOAD=/usr/lib/preloadable_libiconv.so

RUN apk --no-cache --virtual run add \
                               php7-fpm       \
                               php7-curl      \
                               php7-iconv     \
                               php7-xml       \
                               php7-dom       \
                               php7-json      \
                               php7-zlib      \
                               php7-session   \
                               php7-exif      \
                               php7-gd        \
                               zip            \
                               nginx          \
                               ffmpeg         \
                               graphicsmagick&&\
    apk --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/community add gnu-libiconv

COPY . /tmp/

RUN apk --no-cache --virtual tools add tini patch ca-certificates             && \
    cd /tmp && mkdir -p /app                                                  && \
    wget release.larsjung.de/h5ai/h5ai-${H5AI_VERSION}.zip                    && \
    unzip h5ai-${H5AI_VERSION}.zip -d /app                                    && \
    cp -rf options.json /app/_h5ai/private/conf/options.json                  && \
    patch -p1 -ud /app/_h5ai/private/php/core/ -i /tmp/class-setup.php.patch  && \
    chown nginx:www-data /app/_h5ai/public/cache/                             && \
    chown nginx:www-data /app/_h5ai/private/cache/                            && \
    cp  nginx.conf /etc/nginx/nginx.conf && cp php-fpm.conf /etc/php7/        && \
    apk del --purge tools && rm -rf /tmp/*

EXPOSE 80

CMD nginx && \
    php-fpm7 --nodaemonize --fpm-config /etc/php7/php-fpm.conf -c /etc/php7/php.ini
