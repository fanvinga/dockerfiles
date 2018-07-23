FROM alpine:3.8 as builder
MAINTAINER FAN VINGA<fanalcest@gmail.com>

RUN apk add --no-cache --virtual .build-deps \
        libstdc++ \
        nodejs \
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

FROM alpine:3.8

RUN apk add --no-cache nginx
COPY --from=builder /vue-music-webapp/dist /dist/. 
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD nginx
