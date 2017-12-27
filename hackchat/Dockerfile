FROM alpine:3.7
MAINTAINER FAN VINGA<fanalcest@gmail.com>

RUN apk --no-cache add git make nodejs nodejs-npm supervisor nginx
RUN git clone https://github.com/AndrewBelt/hack.chat.git && \
    cd hack.chat && \
    git checkout 5ca90f9 && \
    rm -rf node_modules && \
    npm install && \
    cp config-sample.json config.json && \
    cd client && \
    npm install -g less jade http-server && \
    make && \
    apk del git make nodejs-npm

ADD client.js /hack.chat/client/client.js
ADD supervisord.conf /etc/supervisor/supervisord.conf
ADD nginx.conf /etc/nginx/nginx.conf

WORKDIR /hack.chat/
CMD supervisord -c /etc/supervisor/supervisord.conf
EXPOSE 80
