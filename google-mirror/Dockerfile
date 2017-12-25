FROM alpine:latest
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV NGINX_VER=1.13.7 \
    LANG=zh-CN
RUN apk --update --no-cache add git openssl-dev pcre-dev zlib-dev wget build-base && \
    mkdir src && cd src && \
    wget http://nginx.org/download/nginx-${NGINX_VER}.tar.gz && \
    tar xzf nginx-${NGINX_VER}.tar.gz && \
    git clone --depth 1 https://github.com/cuber/ngx_http_google_filter_module && \
    git clone --depth 1 https://github.com/yaoweibin/ngx_http_substitutions_filter_module && \
    cd nginx-${NGINX_VER} && \
    ./configure --prefix=/opt/nginx \
        --with-http_ssl_module \
        --add-module=../ngx_http_google_filter_module \
        --add-module=../ngx_http_substitutions_filter_module && \
    make && make install && \
    apk del git build-base && \
    rm -rf /src && \
    rm -rf /var/cache/apk/*

ADD nginx.conf /opt/nginx/conf/nginx.conf
EXPOSE 80

CMD sed -i "s/zh-CN/${LANG}/g" /opt/nginx/conf/nginx.conf && /opt/nginx/sbin/nginx -g "daemon off;"
