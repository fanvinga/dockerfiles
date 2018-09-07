FROM alpine:3.8
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV ADMIN_NAME=admin         \
    ADMIN_PASSWORD=password  \
    PASSWORD_SALT=salt 	     \
    PROTOCOL=wss

RUN apk --no-cache add git nodejs nodejs-npm nginx        && \
    git clone https://github.com/hack-chat/main --depth 1 && \
    cd main/server && npm install && cd /main             && \
    ln -s /main/client /app                               && \
    rm -rf .git clientSource documentation                && \
    apk del --purge git nodejs-npm

ADD config.json /main/server/config/config.json
ADD nginx.conf  /etc/nginx/nginx.conf

WORKDIR /main/server
EXPOSE 80

CMD sed -i "s|ws://|${PROTOCOL}://|g"             /main/client/client.js          && \
    sed -i "s|:6060|/ws|g"                        /main/client/client.js          && \
    sed -i "s/ADMIN_NAME/${ADMIN_NAME}/g"         /main/server/config/config.json && \
    sed -i "s/ADMIN_PASSWORD/${ADMIN_PASSWORD}/g" /main/server/config/config.json && \
    sed -i "s/PASSWORD_SALT/${PASSWORD_SALT}/g"   /main/server/config/config.json && \
    nginx && node main.js
