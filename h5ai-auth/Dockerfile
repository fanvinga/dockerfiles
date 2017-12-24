FROM alpine:latest
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV H5AI_VERSION=0.29.0 \
    USER=vinga          \
    PASSWD=vinga

RUN apk --update --no-cache --virtual runtimes  add            \
                               php7-fpm       \
                               php7-curl      \
                               php7-iconv     \
                               php7-xml       \
                               php7-dom       \
                               php7-json      \
                               php7-zlib      \
                               php7-session   \
                               php7-gd        \
                               nginx          \
                               ffmpeg         \
                               openssl        \
                               graphicsmagick     

COPY . /tmp/

RUN apk --update --no-cache --virtual tools add zip unzip tini wget patch ca-certificates                  &&\ 
    cd /tmp && wget release.larsjung.de/h5ai/h5ai-${H5AI_VERSION}.zip && unzip h5ai-${H5AI_VERSION}.zip -d /usr/share/h5ai       && \
    cp -rf options.json /usr/share/h5ai/_h5ai/private/conf/options.json                   && \
    patch -p1 -ud /usr/share/h5ai/_h5ai/private/php/core/ -i /tmp/class-setup.php.patch     && \
    chown nginx:www-data /usr/share/h5ai/_h5ai/public/cache/                               && \
    chown nginx:www-data /usr/share/h5ai/_h5ai/private/cache/ && chmod +x entrypoint.sh    && \
    cp php-fpm.conf  /etc/php7/php-fpm.conf && \
    cp nginx.conf    /etc/nginx/nginx.conf  && \
    cp entrypoint.sh /entrypoint.sh         && \
    apk del --purge tools                   && \   
    rm -rf /var/cache/apk/* /tmp/*   

CMD echo -n "${USER}:" >> /passwd && openssl passwd ${PASSWD} >> /passwd && /entrypoint.sh
EXPOSE 80
