FROM alpine:3.9
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ADD Caddyfile /Caddyfile
 
RUN apk --no-cache add curl && \
    curl "https://caddyserver.com/download/linux/amd64?plugins=http.filebrowser&license=personal&telemetry=off" | tar -xz caddy && \    
    mkdir -p /share /db && \
    mv caddy /usr/bin/caddy && \
    chmod -R 777 /usr/bin/caddy /share /db && \
    apk del --purge curl

CMD caddy -conf /Caddyfile
    
WORKDIR /share
EXPOSE 80
