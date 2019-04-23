FROM alpine:3.9
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ADD Caddyfile /Caddyfile
 
RUN apk --no-cache add curl bash && \
    curl https://getcaddy.com | bash -s personal http.filebrowser && \    
    mkdir -p /share /db     && \
    chmod -R 777 /share /db && \
    apk del --purge curl bash

CMD caddy -conf /Caddyfile
    
WORKDIR /share
EXPOSE 80
