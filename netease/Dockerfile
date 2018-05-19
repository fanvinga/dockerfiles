FROM alpine:3.7
MAINTAINER FAN VINGA<fanalcest@gmail.com>

RUN apk add --no-cache libstdc++ nginx nodejs && \
    apk add --no-cache --virtual .build-deps \
        nodejs-npm \
        binutils-gold \
        git \
        curl \
        g++ \
        gcc \
        gnupg \
        libgcc \
        linux-headers \
        make \
        python && \
    git clone https://github.com/CaiJinyc/vue-music-webapp --depth 1 && \
    cd /vue-music-webapp && \
    npm install && npm run build && \
    npm cache clean --force && \
    apk del --purge .build-deps

ADD nginx.conf /etc/nginx/nginx.conf

WORKDIR /vue-music-webapp

CMD nginx && node prod.server.js
