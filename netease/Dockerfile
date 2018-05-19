FROM node:alpine
MAINTAINER FAN VINGA<fanalcest@gmail.com>

RUN apk add --no-cache libstdc++ nginx && \
    apk add --no-cache --virtual .build-deps \
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
    apk del --purge .build-deps

ADD nginx.conf /etc/nginx/nginx.conf

WORKDIR /vue-music-webapp

CMD nginx && node prod.server.js
